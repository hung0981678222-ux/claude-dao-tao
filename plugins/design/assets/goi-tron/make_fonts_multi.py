"""Tạo nhiều font thương hiệu từ các khung chữ khác nhau (đều SIL OFL), cùng nét riêng: dấu mũ là chiếc bánh.
Chạy: python3 make_fonts_multi.py -> fonts-moi/<Ten>.ttf và .woff2
"""
import copy
import os
import unicodedata

import pathops
from fontTools import subset
from fontTools.merge import Merger
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(HERE)
OUT = os.path.join(HERE, "fonts-moi")
K = .5523
CIRC = "âêôÂÊÔấầẩẫậếềểễệốồổỗộẤẦẨẪẬẾỀỂỄỆỐỒỔỖỘ"
BASES = set("aeoAEO")


def fs_files(fam, w, root=None, subs=("latin", "vietnamese", "latin-ext")):
    root = root or os.path.join(HERE, fam, "files")
    return [p for p in (os.path.join(root, f"{fam}-{s}-{w}-normal.woff2") for s in subs) if os.path.exists(p)]


FONTS = {
    # tên hiển thị: (danh sách file, tên PostScript, mô tả)
    "Bricolage": (fs_files("bricolage-grotesque", 800), "AnTamBricolage", "Hiện đại, có khía mực, cá tính trẻ"),
    "Fraunces": ([os.path.join(SCR, "nl", f"fr50-{s}-900.woff2") for s in ("latin", "vietnamese")], "AnTamFraunces", "Có chân mềm, ấm, sang"),
    "Anton": (fs_files("anton", 400, os.path.join(SCR, "anton", "package", "files")), "AnTamAnton", "Cao hẹp, mạnh, hợp biển hiệu và bậc thang"),
    "Baloo": (fs_files("baloo-2", 800), "AnTamBaloo", "Tròn mập, thân thiện, đồ ăn vặt"),
    "Grandstander": (fs_files("grandstander", 900), "AnTamGrandstander", "Vui, nghịch, như vẽ tay"),
    "Dela": (fs_files("dela-gothic-one", 400), "AnTamDela", "Rất đậm, rộng, nổi bật từ xa"),
    "Unbounded": (fs_files("unbounded", 800), "AnTamUnbounded", "Rộng, tròn kỹ thuật, rất hiện đại"),
    "Playfair": (fs_files("playfair-display", 900), "AnTamPlayfair", "Có chân tương phản cao, sang trọng kiểu tạp chí"),
    "Pacifico": (fs_files("pacifico", 400), "AnTamPacifico", "Chữ viết tay liền nét, vui, kiểu quán ven biển"),
    "Bungee": (fs_files("bungee", 400), "AnTamBungee", "Chữ biển hiệu đường phố, vuông, khối"),
    "Phudu": (fs_files("phudu", 800), "AnTamPhudu", "Hẹp, gọn, đậm vừa, rất dễ đọc"),
    "Paytone": (fs_files("paytone-one", 400), "AnTamPaytone", "Đậm tròn, chắc chắn, hơi cổ điển"),
    "Sigmar": (fs_files("sigmar", 400), "AnTamSigmar", "Siêu mập, hoạt hình, rất nổi"),

}


def ellipse(cx, cy, rx, ry):
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((cx + rx, cy))
    pen.curveTo((cx + rx, cy + K * ry), (cx + K * rx, cy + ry), (cx, cy + ry))
    pen.curveTo((cx - K * rx, cy + ry), (cx - rx, cy + K * ry), (cx - rx, cy))
    pen.curveTo((cx - rx, cy - K * ry), (cx - K * rx, cy - ry), (cx, cy - ry))
    pen.curveTo((cx + K * rx, cy - ry), (cx + rx, cy - K * ry), (cx + rx, cy))
    pen.closePath(); return p


def dome(x0, x1, y0, y1):
    w = x1 - x0; cx = (x0 + x1) / 2; h = y1 - y0
    p = pathops.Path(); pen = p.getPen()
    pen.moveTo((x0, y0)); pen.curveTo((x0, y0 + h * 1.32), (x1, y0 + h * 1.32), (x1, y0)); pen.closePath()
    for dx, dy, r in [(-.24, .36, .075), (.02, .62, .06), (.22, .34, .085)]:
        u = min(w * .5, h * 1.1)
        p = pathops.op(p, ellipse(cx + dx * w, y0 + dy * h, r * u * 2.1, r * u * 1.45), pathops.PathOp.DIFFERENCE)
    return p


def gpath(f, n):
    p = pathops.Path(); gs = f.getGlyphSet()
    gs[n].draw(p.getPen(glyphSet=gs)); return p


def set_glyph(f, n, p):
    pen = TTGlyphPen(f.getGlyphSet()); p.draw(Cu2QuPen(pen, 1.0, reverse_direction=True))
    f["glyf"][n] = pen.glyph()


def replace_cap(p, min_y, tone=None, gap=25):
    """Trong đường p, đường viền rộng nhất nằm trên min_y là dấu mũ -> thay bằng chiếc bánh.
    Dấu thanh (sắc, huyền, hỏi, ngã) được đặt lại: ngã nằm giữa trên đỉnh bánh, các dấu khác tựa vai phải.
    Các đường viền còn lại vẽ chung một lần để giữ nguyên lỗ trong (counter)."""
    cs = [c for c in p.contours if c.bounds]
    upper = [c for c in cs if c.bounds[1] >= min_y]
    if not upper:
        return p
    wmax = max(c.bounds[2] - c.bounds[0] for c in upper)
    # dấu mũ: đường viền đủ rộng nằm thấp nhất (dấu ngã có thể rộng hơn nhưng luôn nằm trên)
    widest = min((c for c in upper if c.bounds[2] - c.bounds[0] >= wmax * .6), key=lambda c: c.bounds[1])
    tones = [c for c in upper if c is not widest] if tone else []
    rest = pathops.Path(); pen = rest.getPen()
    for c in cs:
        if c is not widest and c not in tones:
            c.draw(pen)
    x0, y0, x1, y1 = widest.bounds; pad = (x1 - x0) * .06
    lower = [c.bounds[3] for c in cs if c is not widest and c not in tones and c.bounds[1] < min_y]
    bot = max(y0, (max(lower) + gap) if lower else y0)
    h = min((x1 - x0 + 2 * pad) * .42, gap * 9)  # dáng vòm đồng đều; gap = 5% chiều cao chữ thường
    out = pathops.op(rest, dome(x0 - pad, x1 + pad, bot, bot + h), pathops.PathOp.UNION, fix_winding=True)
    if tones:
        tx0 = min(c.bounds[0] for c in tones); tx1 = max(c.bounds[2] for c in tones); ty0 = min(c.bounds[1] for c in tones)
        cx = (x0 + x1) / 2; w = x1 - x0 + 2 * pad
        if tone == "tilde":
            dx = cx - (tx0 + tx1) / 2; dy = bot + h + gap - ty0
        else:
            dx = cx + w * .5 - tx0 - (tx1 - tx0) * .15; dy = bot + h * .55 - ty0
        tp = pathops.Path(); tpen = tp.getPen()
        for c in tones:
            c.draw(tpen)
        moved = pathops.Path(); tp.draw(TransformPen(moved.getPen(), (1, 0, 0, 1, dx, dy)))
        out = pathops.op(out, moved, pathops.PathOp.UNION, fix_winding=True)
    return out


TONES = {"\u0301": "acute", "\u0300": "grave", "\u0309": "hook", "\u0303": "tilde"}
MARK_TONES = {"0301": "acute", "0300": "grave", "0309": "hook", "0303": "tilde"}


def targets(f):
    """Mọi glyph có dấu mũ mà trình duyệt có thể dùng: chữ trong cmap và các biến thể/ dấu rời sinh ra qua GSUB."""
    cmap = f.getBestCmap()
    rev = {}
    for ch in CIRC:
        n = cmap.get(ord(ch))
        if n:
            rev.setdefault(n, ch)
    o = subset.Options(); o.layout_features = ["*"]; o.notdef_outline = True
    ss = subset.Subsetter(o); ss.populate(unicodes=[ord(c) for c in CIRC])
    fc = copy.deepcopy(f)  # bước dựng tập con có thể sửa font, nên chạy trên bản sao
    ss._prune_pre_subset(fc); ss._closure_glyphs(fc)
    out = {}
    for g in ss.glyphs_retained | set(rev):
        base = g.split(".")[0]
        ch = rev.get(g) or rev.get(base)
        if ch:
            tone = next((v for k, v in TONES.items() if k in unicodedata.normalize("NFD", ch)), None)
            out[g] = ("upper" if ch.isupper() else "lower", tone)
        elif base.startswith("uni0302"):
            out[g] = ("mark", MARK_TONES.get(base[7:11]))
        elif "circumflex" in base.lower() and base.lower() in ("circumflex", "circumflexcomb", "circumflexcomb.case"):
            out[g] = ("mark", None)
    return out


def process(f):
    """Tách rời từng glyph có dấu mũ (kể cả biến thể do GSUB sinh ra) rồi thay dấu mũ bằng bánh."""
    xh = getattr(f["OS/2"], "sxHeight", 0) or 500
    cap = getattr(f["OS/2"], "sCapHeight", 0) or 700
    tg = targets(f)
    paths = {g: gpath(f, g) for g in tg}
    for g, (kind, tone) in tg.items():
        min_y = {"lower": xh * .98, "upper": cap * .98, "mark": -1e9}[kind]
        set_glyph(f, g, replace_cap(paths[g], min_y, tone, gap=xh * .05))
    return len(tg)


def rename(f, fam, ps):
    for rec in f["name"].names:
        if rec.nameID in (1, 16):
            rec.string = fam
        elif rec.nameID in (2, 17):
            rec.string = "Regular"
        elif rec.nameID == 4:
            rec.string = fam
        elif rec.nameID == 6:
            rec.string = ps
        elif rec.nameID == 3:
            rec.string = ps + ";1.0"
    for t in ("hdmx", "LTSH", "VDMX", "fpgm", "prep", "cvt ", "gasp"):
        if t in f:
            del f[t]


def build(name):
    files, ps, _ = FONTS[name]
    os.makedirs(OUT, exist_ok=True)
    tmp = []
    for i, fp in enumerate(files):
        f = TTFont(fp); f.flavor = None
        t = os.path.join(OUT, f"_{ps}-{i}.ttf"); f.save(t); tmp.append(t)
    m = Merger().merge(tmp) if len(tmp) > 1 else TTFont(tmp[0])
    t = os.path.join(OUT, f"_{ps}.ttf"); m.save(t); m = TTFont(t)
    total = process(m)
    rename(m, f"An Tam {name}", ps)
    m.save(os.path.join(OUT, f"{ps}.ttf"))
    m.flavor = "woff2"; m.save(os.path.join(OUT, f"{ps}.woff2"))
    for x in tmp + [t]:
        os.remove(x)
    c = TTFont(os.path.join(OUT, f"{ps}.ttf")).getBestCmap()
    ok = all(ord(x) in c for x in "ẨẤỐỰđươâêôĂ")
    print(f"{name}: sửa {total} glyph, đủ tiếng Việt={ok}")


if __name__ == "__main__":
    for n in FONTS:
        build(n)
