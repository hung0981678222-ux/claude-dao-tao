"""Trang so sánh biểu tượng Điểm Chỉ có dấu riêng. Chạy: python3 build_dau_rieng.py OUT.html"""
import sys

import build_chuan as C
import dau_rieng as D

V, K, DO, MUC = D.V, D.KEM, D.DO, D.MUC

OPTS = [
    ("hien-tai", "Hiện tại · Vân xoáy", lambda c=DO: D.hien_tai(c), lambda: D.hien_tai(K),
     "Dấu vân tay xoáy chung chung – đúng ý điểm chỉ nhưng ai dùng cũng được (bảo mật, ngân hàng, mở khoá vân tay).", "Thấp"),
    ("mai-leu", "A · Vân mái lều = chữ A", lambda c=DO: D.mai_leu(c), lambda: D.mai_leu(K),
     "Dùng dạng vân tay có thật – vân \"mái lều\" (tented arch). Các đường vân nhọn đỉnh lồng nhau, lõi trong cùng thành chữ A của An Tâm. Nhìn xa là dấu vân tay, nhìn gần thấy chữ A.", "Cao"),
    ("van-cuon", "B · Vân cuộn = lát cắt cuốn bánh", lambda c=DO: D.van_cuon(c), lambda: D.van_cuon(K),
     "Vân tay xoáy vẽ thành một đường xoắn liền, đuôi duỗi ra như mép bánh – đúng hình mặt cắt của một cuốn tortilla/kebab. Một hình, hai nghĩa: dấu tay cam kết và chiếc bánh cuộn.", "Cao"),
    ("dau-mu", "C · Dấu mũ â", lambda c=DO: D.dau_mu(c), lambda: D.dau_mu(K, DO),
     "Lấy chữ \"â\" trong chữ Tâm từ font riêng An Tâm Tròn Bánh – dấu mũ là ba đường vân tay. Biểu tượng và font là một hệ, rất dễ nhận ra ở cỡ nhỏ (ảnh đại diện, favicon, tem).", "Rất cao"),
    ("an-a", "D · Ấn Â", lambda c=DO: D.an_a(c), lambda: D.an_a(K),
     "Chữ Â hoa của font An Tâm Tròn Bánh (dấu mũ ba đường vân) đặt trong vòng vân tay đứt nét như dấu son vừa ấn. Chắc, trang trọng, hợp làm con dấu và tem niêm phong.", "Rất cao"),
    ("van-at", "E · Vân AT", lambda c=DO: D.van_at(c), lambda: D.van_at(K),
     "Phát triển từ A: lớp vân ngoài là mái lều (chữ A), lõi vân là chữ T – ghép thành AT (An Tâm) giấu trong một dấu vân tay.", "Cao"),
    ("hat-lua-mi", "F · Vân hạt lúa mì", lambda c=DO: D.hat_lua_mi(c), lambda: D.hat_lua_mi(K),
     "Đầu ngón tay vẽ thành hạt lúa mì – nguyên liệu làm vỏ bánh. Nói về sản phẩm và độ thật của bột, vẫn giữ cảm giác vân tay.", "Khá"),
    ("giot-son", "G · Giọt son", lambda c=DO: D.giot_son(c), lambda: D.giot_son(K),
     "Dấu vân tay trong dáng giọt mực son – đúng chất điểm chỉ. Lưu ý: hình giọt dễ bị liên tưởng tới dầu, nước – cần thử với khách.", "Trung bình"),
]


def lockup(mark, fg=DO, sub=MUC, bg=None):
    m = f'<g transform="translate(110 128) scale(0.95)">{mark}</g>'
    t0, _ = V.text("ẨM THỰC", 24, "xb", 232, 70, sub, track=.32)
    t1, w1 = V.text("An Tâm", 118, "xb", 226, 176, fg, track=-.02)
    t2, w2 = V.text("Sản Phẩm Tận Tâm · Phát Triển Xứng Tầm", 17, "md", 232, 214, sub, track=.02)
    W = 232 + max(w1, w2) + 30
    r = f'<rect x="10" y="10" width="{W}" height="230" fill="{bg}"/>' if bg else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="10 10 {W} 230" role="img" aria-label="Logo">{r}{m}{t0}{t1}{t2}</svg>'


def avatar(mark_on_red):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-110 -110 220 220" role="img" aria-label="Ảnh đại diện"><circle r="108" fill="{DO}"/><g transform="scale(.78)">{mark_on_red}</g></svg>'


def tui(mark):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 240" role="img" aria-label="Túi bánh">'
            f'<path d="M30,20 H170 L178,228 H22 Z" fill="{K}" stroke="#E6D6C2"/><rect x="30" y="20" width="140" height="14" fill="{DO}"/>'
            f'<g transform="translate(100 104) scale(.48)">{mark}</g>{V.text("An Tâm", 30, "xb", 100, 190, DO, "middle")[0]}'
            f'<rect x="22" y="204" width="156" height="24" fill="{DO}"/>{V.text("BÁNH TORTILLA", 11, "xb", 100, 221, K, "middle", .1)[0]}</svg>')


def card(i, key, name, f, g, story, score):
    small = "".join(D.svg(f(), s) for s in (16, 24, 32, 48))
    return f"""<section class="s" id="{key}"><div class="num">{'Tham chiếu' if i == 0 else 'Phương án'}</div><h2>{name}</h2>
<p class="lead">{story} <b>Tính riêng: {score}.</b></p>
<div class="g g4"><div class="card">{D.svg(f(), 220)}</div><div class="card d">{D.svg(g(), 220)}</div>
<div class="card">{avatar(g())}<p class="cap">Ảnh đại diện Facebook/Zalo</p></div><div class="card">{tui(f())}<p class="cap">Trên túi bánh</p></div></div>
<div class="g g2" style="margin-top:18px"><div class="card">{lockup(f())}</div><div class="card d">{lockup(g(), K, K)}</div></div>
<div class="card" style="margin-top:18px"><div class="sm">{small}</div><p class="cap">Cỡ nhỏ 16 · 24 · 32 · 48 px (favicon, tem, ô ảnh đại diện)</p></div></section>"""


def page():
    css = C.CSS + """.card svg{display:block;width:100%;height:auto}.sm{display:flex;gap:18px;align-items:end}.sm svg{width:auto!important}
.hm{display:flex;gap:12px}.hm svg{width:25%!important}.verdict{max-width:1200px;margin:56px auto 0;padding:0 20px}"""
    secs = "".join(card(i, *o) for i, o in enumerate(OPTS))
    toc = "".join(f'<a href="#{o[0]}">{o[1].split(" · ")[0]}</a>' for o in OPTS)
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dấu riêng Điểm Chỉ</title><style>{C.faces()}\n{css}</style></head><body>
<header class="hero"><div class="in"><div><div class="k">Điểm Chỉ · Làm biểu tượng có dấu riêng</div><h1>Vân tay của riêng An Tâm</h1>
<p>Giữ ý điểm chỉ – cam kết bằng dấu tay son – nhưng cho dấu vân tay một chi tiết chỉ An Tâm có: chữ A, chữ AT, chiếc bánh cuộn, hạt lúa mì, hoặc dấu mũ trong chữ Tâm. 7 phương án.</p></div>
<div class="card hm">{D.svg(D.mai_leu(), 120)}{D.svg(D.van_cuon(), 120)}{D.svg(D.dau_mu(DO), 120)}{D.svg(D.an_a(), 120)}</div></div></header>
<nav class="toc">{toc}</nav>{secs}
<div class="verdict"><div class="card"><h4>Đề xuất của Thiết kế AN TÂM</h4>
<p><b>Nhóm mạnh nhất là hệ "dấu mũ vân tay": C · Dấu mũ â và D · Ấn Â.</b> Biểu tượng lấy thẳng từ font riêng nên không thương hiệu nào trùng được, rõ ở cỡ nhỏ, và cả hệ thống (logo, chữ, tem) nói cùng một ngôn ngữ. Gợi ý: <b>D</b> làm con dấu/tem niêm phong, <b>C</b> làm ảnh đại diện/favicon.</p>
<p>Nếu muốn logo vẫn có hình vân tay rõ: <b>A · Vân mái lều</b> hoặc <b>E · Vân AT</b> cho logo ngang. <b>B · Vân cuộn</b> và <b>F · Hạt lúa mì</b> hợp làm hoạ tiết bao bì.</p>
<p class="cap">Trước khi chốt nên tra cứu nhãn hiệu tại Cục Sở hữu trí tuệ để chắc không trùng.</p></div></div>
<div class="end"><h2 style="color:var(--do);font-weight:800">Bạn chọn phương án nào (A–G)?</h2></div></body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())
