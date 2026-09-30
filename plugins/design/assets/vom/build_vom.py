"""Bảng nhận diện hướng Vòm cho Ẩm Thực An Tâm. Chạy: python3 build_vom.py OUT.html"""
import base64, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
LOGO = "/home/user/claude-dao-tao/plugins/design/assets/logo-am-thuc-an-tam.jpg"
g = json.loads(subprocess.check_output([sys.executable, os.path.join(HERE, "chu_vom.py")]))
WM, WMW = g["wm_goc"]["d"], g["wm_goc"]["w"]
MK, MKW = g["mark"]["d"], g["mark"]["w"]


def img(name):
    return "data:image/svg+xml;base64," + base64.b64encode(open(f"{MH}/{name}.svg", "rb").read()).decode()


LOGO_URI = "data:image/jpeg;base64," + base64.b64encode(open(LOGO, "rb").read()).decode()


AT = '<b class="amt">' + "".join(f"<span>{c}</span>" for c in "ẨM THỰC") + "</b>"


def wm(cls="", label="An Tâm"):
    return (f'<svg class="wm {cls}" viewBox="-2 -40 {WMW + 4:.0f} 142" role="img" aria-label="{label}">'
            f'<path fill="currentColor" d="{WM}"/></svg>')


def mk(cls=""):
    return (f'<svg class="mk {cls}" viewBox="-14 -40 {MKW + 28:.0f} 142" role="img" aria-label="Biểu tượng An Tâm">'
            f'<path fill="currentColor" d="{MK}"/></svg>')


def lockup(cls=""):
    return (f'<div class="lock {cls}">{mk()}<span class="rule"></span>'
            f'<div class="lk-t">{AT}{wm()}</div></div>')


def stack(cls=""):
    return f'<div class="stack {cls}">{AT}{wm()}</div>'


PRODUCTS = [("banh-tortillas", "Bánh tortillas", "Bánh nền, bán sỉ cho doanh nghiệp", "kem"),
            ("taco", "Taco", "Gập đôi, nhân đầy", "vang"),
            ("doner-tru-quay", "Doner kebab", "Thịt nướng trụ quay", "do"),
            ("doner-cuon", "Doner cuộn", "Cuộn chặt, ăn gọn", "muc")]

CSS = """
:root{--do:#D7150E;--do2:#A80F0A;--kem:#FAF5EC;--bot:#F1E6D2;--muc:#241612;--vang:#F2A93B;--banh:#EFD9AE;--xam:#6B5A52;--line:#E6DACB;
--f:'Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}
*{box-sizing:border-box;margin:0}
body{background:var(--kem);color:var(--muc);font:400 16px/1.55 var(--f);-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}
.w{max-width:1200px;margin:0 auto;padding:0 32px}
section{padding:96px 0}
.eye{display:flex;gap:14px;align-items:center;font:700 12px/1 var(--f);letter-spacing:.22em;text-transform:uppercase;color:var(--do);margin-bottom:18px}
.eye i{font-style:normal;display:inline-grid;place-items:center;width:34px;height:40px;border-radius:17px 17px 4px 4px;background:var(--do);color:var(--kem);letter-spacing:0}
h2{font:800 clamp(34px,5vw,60px)/1.02 var(--f);letter-spacing:-.03em;max-width:17ch}
h2 em{font-style:normal;color:var(--do)}
.lead{max-width:60ch;color:var(--xam);margin-top:16px;font-size:17px}
.wm{display:block;width:100%;height:auto}
.mk{display:block;height:100%;width:auto}

/* hero */
.hero{background:var(--do);color:var(--kem);padding:28px 0 0;overflow:hidden;position:relative}
.nav{display:flex;justify-content:space-between;align-items:center;font:600 13px/1 var(--f);letter-spacing:.08em}
.nav .mk{height:40px}
.nav span{opacity:.8}
.hero .big{margin-top:72px;display:grid;grid-template-columns:1.25fr 1fr;gap:48px;align-items:end}
.hero .amt{font-size:clamp(14px,1.8vw,22px)}
.hero h1{font:500 clamp(18px,2vw,22px)/1.45 var(--f);margin-top:34px;max-width:30ch;opacity:.92}
.hero .tag{display:inline-flex;gap:10px;margin-top:26px;font:700 12px/1 var(--f);letter-spacing:.16em;text-transform:uppercase}
.hero .tag span{border:1.5px solid rgba(250,245,236,.5);padding:10px 14px;border-radius:999px}
.hwin{aspect-ratio:4/5;background:var(--kem);border-radius:999px 999px 0 0;display:grid;place-items:end center;padding:0 8% 12%;position:relative}
.hwin::before{content:"";position:absolute;inset:22px 22px 0;border-radius:999px 999px 0 0;border:2px dashed var(--banh)}
.hwin img{position:relative;width:100%}
.strip{display:flex;height:64px;margin-top:0}
.strip div{flex:1;border-radius:999px 999px 0 0;background:var(--do2)}
.strip div:nth-child(3n+2){background:var(--vang)}
.strip div:nth-child(3n){background:var(--kem)}

/* cấu trúc */
.build{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:48px;align-items:stretch}
.build .c{background:#fff;border:1px solid var(--line);border-radius:24px;padding:22px;display:flex;flex-direction:column;gap:14px}
.build .c svg{height:150px;width:100%}
.build .op{display:grid;place-items:center;font:300 48px/1 var(--f);color:var(--do);background:none;border:0}
.build h3{font:800 18px/1.2 var(--f)}
.build p{font-size:14px;color:var(--xam)}
.build .c.red{background:var(--do);color:var(--kem);border-color:var(--do)}
.build .c.red p{color:rgba(250,245,236,.8)}
.rules{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:14px}
.rules div{border-top:2px solid var(--muc);padding-top:14px;font-size:14px;color:var(--xam)}
.rules b{display:block;color:var(--muc);font:800 15px/1.3 var(--f);margin-bottom:4px}

/* logo */
.bento{display:grid;grid-template-columns:repeat(12,1fr);gap:14px;margin-top:48px}
.tile{border-radius:28px;padding:40px;display:grid;place-items:center;min-height:300px;position:relative}
.tile .cap{position:absolute;left:24px;bottom:18px;font:700 11px/1 var(--f);letter-spacing:.16em;text-transform:uppercase;opacity:.65}
.t-kem{background:#fff;border:1px solid var(--line);color:var(--do)}
.t-do{background:var(--do);color:var(--kem)}
.t-muc{background:var(--muc);color:var(--kem)}
.t-vang{background:var(--vang);color:var(--muc)}
.t-bot{background:var(--bot);color:var(--do)}
.s8{grid-column:span 8}.s4{grid-column:span 4}.s6{grid-column:span 6}.s3{grid-column:span 3}
.lock{display:flex;align-items:center;gap:22px;width:min(100%,520px)}
.lock .mk{height:96px;flex:none}
.lock .rule{width:2px;align-self:stretch;background:currentColor;opacity:.35}
.lk-t{flex:1;display:flex;flex-direction:column;gap:8px}
.amt{font:800 15px/1 var(--f);display:flex;justify-content:space-between;padding:0 1%}.amt span:nth-child(3){width:.6em}
.stack{display:flex;flex-direction:column;gap:12px;width:100%}
.tile .stack{width:min(100%,320px)}
.tile .mk.solo{height:150px}
.appi{width:132px;aspect-ratio:4/5;border-radius:999px 999px 26px 26px;background:var(--do);color:var(--kem);display:grid;place-items:center;padding:30px 22px 18px}
.appi .mk{height:auto;width:100%}
.av{width:132px;aspect-ratio:1;border-radius:50%;background:var(--kem);color:var(--do);display:grid;place-items:center;padding:24px}
.av .mk{height:auto;width:100%}
.row{display:flex;gap:26px;align-items:end;flex-wrap:wrap;justify-content:center}
.row small{display:block;text-align:center;font:600 11px/1 var(--f);margin-top:10px;opacity:.7}
.sz{display:flex;gap:28px;align-items:end;color:var(--do)}
.sz div{text-align:center;font:600 11px/1 var(--f);color:var(--xam)}
.sz .mk{margin:0 auto 10px;color:var(--do)}
.clear{position:relative;padding:34px;outline:1.5px dashed var(--do);outline-offset:0;width:min(100%,460px)}
.clear::after{content:"x";position:absolute;right:8px;top:6px;font:700 12px/1 var(--f);color:var(--do)}
.old{display:flex;gap:28px;align-items:center;margin-top:14px;background:#fff;border:1px solid var(--line);border-radius:24px;padding:22px 28px}
.old img{width:140px;border-radius:12px}
.old p{font-size:14px;color:var(--xam);max-width:70ch}
.old b{color:var(--muc)}

/* màu */
.pal{display:grid;grid-template-columns:5fr 3fr 1.3fr 1fr;gap:12px;margin-top:48px;height:380px}
.pal div{border-radius:999px 999px 22px 22px;padding:26px 22px;display:flex;flex-direction:column;justify-content:flex-end;font:600 13px/1.5 var(--f)}
.pal b{font:800 20px/1.1 var(--f);display:block;margin-bottom:6px}
.pal .n{font:800 44px/1 var(--f);letter-spacing:-.03em;margin-bottom:14px}
.pal .p1{background:var(--do);color:var(--kem)}
.pal .p2{background:#fff;border:1px solid var(--line)}
.pal .p3{background:var(--muc);color:var(--kem)}
.pal .p4{background:var(--vang)}
.pal .p3 .n,.pal .p4 .n{font-size:30px}
.pairs{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:12px}
.pairs div{border-radius:16px;padding:16px 18px;font:800 22px/1.1 var(--f);display:flex;justify-content:space-between;align-items:end}
.pairs small{font:600 11px/1 var(--f);opacity:.75}

/* chữ */
.type{display:grid;grid-template-columns:1.2fr 1fr;gap:14px;margin-top:48px}
.spec{background:#fff;border:1px solid var(--line);border-radius:28px;padding:36px}
.spec .aa{font:800 150px/.9 var(--f);letter-spacing:-.05em;color:var(--do)}
.spec h3{font:800 26px/1.2 var(--f);margin-top:18px}
.spec p{color:var(--xam);font-size:15px;margin-top:6px}
.scale div{border-bottom:1px solid var(--line);padding:14px 0;display:flex;justify-content:space-between;gap:16px;align-items:baseline}
.scale small{font:600 11px/1 var(--f);color:var(--xam);white-space:nowrap}
.s1{font:800 44px/1.05 var(--f);letter-spacing:-.03em}
.s2{font:800 26px/1.15 var(--f);letter-spacing:-.02em}
.s3t{font:700 12px/1 var(--f);letter-spacing:.22em;text-transform:uppercase;color:var(--do)}
.s4t{font:400 16px/1.55 var(--f)}

/* hoạ tiết */
.pats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:48px}
.pat{aspect-ratio:1;border-radius:24px;overflow:hidden;position:relative}
.pat svg{width:100%;height:100%;display:block}
.pat span{position:absolute;left:14px;bottom:12px;background:var(--kem);color:var(--muc);font:700 11px/1 var(--f);padding:8px 10px;border-radius:999px}

/* sản phẩm */
.prod{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:48px}
.prod .a{aspect-ratio:3/4;border-radius:999px 999px 24px 24px;display:grid;place-items:end center;padding:0 10% 16%}
.prod h3{font:800 20px/1.2 var(--f);margin-top:16px}
.prod p{font-size:14px;color:var(--xam)}
.bg-kem{background:var(--bot)}.bg-vang{background:var(--vang)}.bg-do{background:var(--do)}.bg-muc{background:var(--muc)}

/* ứng dụng */
.apps{display:grid;grid-template-columns:repeat(12,1fr);gap:14px;margin-top:48px}
.bag{grid-column:span 4;background:var(--bot);border-radius:28px;display:grid;place-items:center;padding:44px 20px}
.bagb{width:min(100%,260px);aspect-ratio:3/4.2;background:var(--do);color:var(--kem);border-radius:14px 14px 22px 22px;position:relative;padding:34px 26px 24px;display:flex;flex-direction:column;align-items:center;gap:18px;box-shadow:0 30px 40px -24px rgba(36,22,18,.45)}
.bagb::before{content:"";position:absolute;top:0;left:0;right:0;height:18px;background:var(--do2);border-radius:14px 14px 0 0}
.bagb .stack{width:78%}.bagb .amt{font-size:9px}
.bagb .win{width:84%;flex:1;background:var(--banh);border:6px solid var(--kem);border-radius:999px 999px 10px 10px;display:grid;place-items:end center;padding:0 8% 10%}
.bagb small{font:700 10px/1 var(--f);letter-spacing:.2em}
.store{grid-column:span 8;background:var(--muc);border-radius:28px;padding:44px 40px 0;display:flex;flex-direction:column;overflow:hidden;color:var(--kem)}
.fac{margin-top:auto;display:grid;grid-template-columns:1fr 1.3fr 1fr;gap:10px;align-items:end}
.fac .d{background:var(--do);border-radius:999px 999px 0 0;aspect-ratio:3/4.2;display:grid;place-items:center;padding:22%}
.fac .d.mid{aspect-ratio:3/3.6;padding:18% 14%;align-content:center;gap:12px}
.fac .d.mid .amt{font-size:10px}
.fac .d.side{background:var(--kem);padding:0 12% 0;place-items:end center}
.fac .d.side img{width:100%;margin-bottom:-6%}
.fac .d .mk{height:auto;width:62%}
.store .sign{display:flex;justify-content:space-between;align-items:end;margin-bottom:32px;gap:20px}
.store .sign b{font:800 28px/1.1 var(--f);letter-spacing:-.02em;max-width:18ch}
.store .sign small{font:600 12px/1.5 var(--f);opacity:.7;text-align:right}
.post{grid-column:span 5;background:var(--vang);border-radius:28px;padding:30px;display:flex;flex-direction:column;aspect-ratio:4/5;position:relative;overflow:hidden}
.post .top{display:flex;justify-content:space-between;align-items:center;color:var(--do)}
.post .top .mk{height:40px}
.post .top small{font:700 11px/1 var(--f);letter-spacing:.2em;color:var(--muc)}
.post h3{font:800 clamp(34px,4.2vw,52px)/1 var(--f);letter-spacing:-.035em;margin-top:18px;color:var(--muc)}
.post h3 span{color:var(--do)}
.post h3{position:relative;z-index:2}.post .arc{position:absolute;left:14%;right:-10%;bottom:0;height:54%;border-radius:999px 999px 0 0;background:var(--do);display:grid;place-items:start center;padding:8% 12% 0}
.post .arc img{width:66%}
.post .foot{position:absolute;left:30px;bottom:24px;font:700 12px/1.4 var(--f);color:var(--kem);z-index:2}
.card2{grid-column:span 7;display:grid;grid-template-rows:auto auto;gap:14px;align-content:start}
.nc{border-radius:28px;display:grid;grid-template-columns:1fr 1fr;overflow:hidden;border:1px solid var(--line)}
.nc .f{background:var(--do);color:var(--kem);display:grid;place-items:center;padding:30px}
.nc .f .stack{width:min(100%,240px)}.nc .f .amt{font-size:11px}
.nc .b{background:#fff;padding:28px 30px;display:flex;flex-direction:column;justify-content:space-between;font-size:13px;color:var(--xam)}
.nc .b b{font:800 18px/1.2 var(--f);color:var(--muc);display:block}
.nc .b .mk{height:30px;color:var(--do);align-self:flex-start}
.nc .b .ct{font:600 13px/1.7 var(--f);color:var(--muc)}
.box{border-radius:28px;background:var(--kem);border:1px solid var(--line);display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:22px}
.box div{border-radius:999px 999px 14px 14px;display:grid;place-items:center;padding:34px 0 22px}
.box .mk{width:46%;height:auto}
.foot-b{background:var(--muc);color:var(--kem);padding:64px 0 40px}
.foot-b .w{display:grid;grid-template-columns:1fr auto;gap:40px;align-items:end}
.foot-b .stack{max-width:420px}
.foot-b p{font-size:13px;opacity:.7;margin-top:22px;max-width:52ch}
.foot-b .ct{text-align:right;font:600 14px/1.8 var(--f)}
@media(max-width:900px){.w{padding:0 16px}section{padding:64px 0}
.hero .big{grid-template-columns:1fr}.hwin{max-width:360px}
.build{grid-template-columns:1fr 1fr}.build .op{display:none}.rules{grid-template-columns:1fr}
.s8,.s4,.s6,.s3{grid-column:1/-1}.tile{min-height:220px;padding:32px 22px}
.pal{grid-template-columns:1fr 1fr;height:auto}.pal div{min-height:200px}.pairs{grid-template-columns:1fr 1fr}
.type{grid-template-columns:1fr}.spec .aa{font-size:110px}
.pats,.prod{grid-template-columns:1fr 1fr}
.bag,.store,.post,.card2{grid-column:1/-1}.nc{grid-template-columns:1fr}
.foot-b .w{grid-template-columns:1fr}.foot-b .ct{text-align:left}.lock .mk{height:70px}}
"""


def pattern_svgs():
    D = "#D7150E"; K = "#FAF5EC"; V = "#F2A93B"; M = "#241612"; B = "#EFD9AE"
    # 1. hàng mái vòm
    a = [f'<rect width="400" height="400" fill="{D}"/>']
    for r in range(5):
        for c in range(5):
            x, y = c * 80 + (40 if r % 2 else 0) - 20, r * 80 + 10
            a.append(f'<path d="M{x+10},{y+70} v-30 a30,30 0 0 1 60,0 v30 z" fill="{"#B8110B" if (r+c)%3 else V}"/>')
    # 2. nửa bánh
    b = [f'<rect width="400" height="400" fill="{K}"/>']
    for r in range(8):
        for c in range(7):
            x, y = c * 64 - (32 if r % 2 else 0), r * 52 + 40
            b.append(f'<path d="M{x},{y} a24,24 0 0 1 48,0 z" fill="{D if (r*3+c)%4 else V}"/>')
    # 3. chữ Â lặp
    cc = [f'<rect width="400" height="400" fill="{M}"/>']
    for r in range(4):
        for c in range(4):
            x, y = c * 100 + 22, r * 100 + 40
            cc.append(f'<g transform="translate({x} {y}) scale(.56)" fill="{D if (r+c)%2 else "#3A2620"}"><path d="{MK}"/></g>')
    # 4. cổng vòm lồng nhau
    d = [f'<rect width="400" height="400" fill="{V}"/>']
    for i, col in enumerate([D, K, D, B, D]):
        w = 340 - i * 60
        x = 200 - w / 2
        d.append(f'<path d="M{x},400 V{200 - w/2 + 40 + i*18} a{w/2},{w/2} 0 0 1 {w},0 V400 z" fill="{col}"/>')
    names = ["Hàng mái vòm", "Nửa chiếc bánh", "Chữ Â lặp", "Cổng lồng"]
    return [(names[i], f'<svg viewBox="0 0 400 400" preserveAspectRatio="xMidYMid slice">{"".join(s)}</svg>')
            for i, s in enumerate([a, b, cc, d])]


def build_steps():
    A = g["A"]["d"]
    arch = '<svg viewBox="-10 -45 104 150"><path d="M0,100 V42 a42,42 0 0 1 84,0 V100 h-23 V42 a19,19 0 0 0 -38,0 V100 z" fill="#D7150E"/></svg>'
    moon = '<svg viewBox="-10 -45 104 150"><path d="M20,50 a22,22 0 0 1 44,0 z" fill="#F2A93B"/><path d="M20,50 h44" stroke="#241612" stroke-width="1.5" stroke-dasharray="3 3"/></svg>'
    ahat = f'<svg viewBox="-10 -45 104 150"><path fill="#D7150E" d="{MK}"/></svg>'
    mark = f'<svg viewBox="-10 -45 104 150" style="color:#FAF5EC"><path fill="currentColor" d="{MK}"/></svg>'
    return f"""
<div class="build">
 <div class="c">{arch}<h3>Mái vòm</h3><p>Cửa hàng, cổng đón khách. Một nét dày 23 đơn vị cho mọi chữ.</p></div>
 <div class="op">+</div>
 <div class="c">{moon}<h3>Nửa chiếc bánh</h3><p>Bánh tortilla gập đôi thành hình bán nguyệt, làm dấu mũ.</p></div>
 <div class="op">=</div>
 <div class="c red">{mark}<h3>Chữ Â, biểu tượng</h3><p>Chữ Â của "Tâm" tách riêng thành dấu nhận diện.</p></div>
</div>
<div class="rules">
 <div><b>Một độ dày nét</b>A, N, T, Â, M cùng nét 23 trên chiều cao 100. Không chữ nào mảnh hơn.</div>
 <div><b>Hai chữ A là mái vòm</b>Đỉnh tròn, lòng chữ là ô cửa. N, T, M giữ góc vuông để dễ đọc từ xa.</div>
 <div><b>Dấu mũ là bánh</b>Hình bán nguyệt rộng bằng nửa chữ A, cách đỉnh 12 đơn vị. Không thay bằng dấu mũ thường.</div>
</div>"""


def page():
    prod = "".join(f'<div><div class="a bg-{c}"><img src="{img(n)}" alt="{t}"></div><h3>{t}</h3><p>{d}</p></div>' for n, t, d, c in PRODUCTS)
    pats = "".join(f'<div class="pat">{s}<span>{n}</span></div>' for n, s in pattern_svgs())
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>An Tâm Vòm</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&display=swap">
<style>{CSS}</style></head><body>

<header class="hero"><div class="w">
 <div class="nav">{mk()}<span>BỘ NHẬN DIỆN · HƯỚNG VÒM</span></div>
 <div class="big">
  <div>{stack()}
   <h1>Mái vòm của cửa hàng, nửa chiếc bánh gập đôi. Gọn thành một chữ Â.</h1>
   <div class="tag"><span>Bánh tortillas</span><span>Taco</span><span>Doner kebab</span></div>
  </div>
  <div class="hwin"><img src="{img('taco')}" alt="Taco"></div>
 </div>
</div>
<div class="strip">{'<div></div>' * 14}</div>
</header>

<section><div class="w">
 <div class="eye"><i>01</i>Cấu trúc</div>
 <h2>Hai hình khối, <em>một chữ Â</em></h2>
 <p class="lead">Chữ AN TÂM và biểu tượng dùng chung một bộ hình: mái vòm và nửa chiếc bánh. Nhìn biểu tượng là nhận ra chữ, nhìn chữ là thấy biểu tượng.</p>
 {build_steps()}
</div></section>

<section style="background:#fff"><div class="w">
 <div class="eye"><i>02</i>Logo</div>
 <h2>Chữ AN TÂM và <em>biểu tượng rút gọn</em></h2>
 <div class="bento">
  <div class="tile t-kem s8">{lockup()}<span class="cap">Bản ngang, dùng chính</span></div>
  <div class="tile t-do s4">{mk("solo")}<span class="cap">Biểu tượng</span></div>
  <div class="tile t-do s4">{stack()}<span class="cap">Bản đứng</span></div>
  <div class="tile t-muc s4">{lockup()}<span class="cap">Trên nền tối</span></div>
  <div class="tile t-vang s4" style="color:var(--do)">{stack()}<span class="cap">Trên nền vàng</span></div>
  <div class="tile t-bot s6"><div class="row"><div><div class="appi">{mk()}</div><small>Ứng dụng, Zalo OA</small></div><div><div class="av">{mk()}</div><small>Ảnh đại diện</small></div></div><span class="cap">Ô biểu tượng</span></div>
  <div class="tile t-kem s6"><div><div class="clear">{lockup()}</div>
   <div class="sz" style="margin-top:34px;justify-content:center"><div>{mk().replace('class="mk "','class="mk" style="height:64px"')}64 px</div><div>{mk().replace('class="mk "','class="mk" style="height:32px"')}32 px</div><div>{mk().replace('class="mk "','class="mk" style="height:16px"')}16 px, nhỏ nhất</div></div></div>
   <span class="cap">Vùng trống bằng cao dấu mũ (x)</span></div>
 </div>
 <div class="old"><img src="{LOGO_URI}" alt="Logo gốc Ẩm Thực An Tâm"><p><b>Logo gốc vẫn là logo chính thức</b> cho tới khi công ty duyệt hướng Vòm. Trên nhãn bao bì, hoá đơn, hợp đồng vẫn ghi đủ tên pháp lý Công ty TNHH SX-TM Ẩm Thực An Tâm.</p></div>
</div></section>

<section><div class="w">
 <div class="eye"><i>03</i>Màu</div>
 <h2>Đỏ dẫn đầu, <em>kem làm nền</em></h2>
 <div class="pal">
  <div class="p1"><span class="n">55%</span><b>Đỏ ruy băng</b>#D7150E<br>Đỏ đậm #A80F0A</div>
  <div class="p2"><span class="n">30%</span><b>Kem bột</b>#FAF5EC<br>Bột mì #F1E6D2</div>
  <div class="p3"><span class="n">10%</span><b>Mực</b>#241612</div>
  <div class="p4"><span class="n">5%</span><b>Vàng lúa</b>#F2A93B</div>
 </div>
 <div class="pairs">
  <div style="background:var(--do);color:var(--kem)">Aa<small>Kem trên đỏ · 4,8:1</small></div>
  <div style="background:var(--kem);color:var(--do);border:1px solid var(--line)">Aa<small>Đỏ trên kem · 4,8:1</small></div>
  <div style="background:var(--muc);color:var(--kem)">Aa<small>Kem trên mực · 16:1</small></div>
  <div style="background:var(--vang);color:var(--muc)">Aa<small>Mực trên vàng · 8,8:1</small></div>
 </div>
 <p class="lead">Không đặt chữ vàng trên nền đỏ. Chữ đỏ trên kem chỉ dùng cho chữ từ 18 px đậm trở lên.</p>
</div></section>

<section style="background:#fff"><div class="w">
 <div class="eye"><i>04</i>Chữ</div>
 <h2>Một họ chữ, <em>đủ dấu tiếng Việt</em></h2>
 <div class="type">
  <div class="spec"><div class="aa">Ẩm Ự</div><h3>Be Vietnam Pro</h3><p>Nét hình học, cùng tinh thần với chữ AN TÂM hệ Vòm. Dấu tiếng Việt rõ, không chồng lên nhau. Miễn phí trên Google Fonts.</p></div>
  <div class="spec scale">
   <div><span class="s1">Gập đôi là ngon</span><small>Tiêu đề · 800</small></div>
   <div><span class="s2">Bánh tortillas giao tận nơi</span><small>Tiêu đề phụ · 800</small></div>
   <div><span class="s3t">Nhượng quyền cửa hàng</span><small>Nhãn · 700</small></div>
   <div><span class="s4t">Bữa nhẹ tiện lợi cho nhân viên văn phòng, đặt qua hotline 0348.635.222.</span><small>Nội dung · 400</small></div>
  </div>
 </div>
</div></section>

<section><div class="w">
 <div class="eye"><i>05</i>Hoạ tiết</div>
 <h2>Cắt ra từ <em>chính logo</em></h2>
 <div class="pats">{pats}</div>
</div></section>

<section style="background:#fff"><div class="w">
 <div class="eye"><i>06</i>Sản phẩm</div>
 <h2>Mỗi món <em>một ô vòm</em></h2>
 <div class="prod">{prod}</div>
</div></section>

<section><div class="w">
 <div class="eye"><i>07</i>Ứng dụng</div>
 <h2>Từ túi bánh <em>tới mặt tiền</em></h2>
 <div class="apps">
  <div class="bag"><div class="bagb">{stack()}<div class="win"><img src="{img('banh-tortillas')}" alt="Bánh tortillas"></div><small>BÁNH TORTILLAS</small></div></div>
  <div class="store">
   <div class="sign"><b>Cửa hàng nhượng quyền: ba ô vòm, một chữ Â</b><small>Biển hiệu đỏ<br>Cửa kính hình vòm</small></div>
   <div class="fac"><div class="d side"><img src="{img('doner-tru-quay')}" alt="Doner"></div><div class="d mid">{mk()}{stack()}</div><div class="d side"><img src="{img('doner-cuon')}" alt="Doner cuộn"></div></div>
  </div>
  <div class="post"><div class="top">{mk()}<small>BÀI ĐĂNG 1080×1350</small></div><h3>Bữa nhẹ <span>văn phòng</span>, giao tận nơi.</h3><div class="arc"><img src="{img('doner-cuon')}" alt="Doner cuộn"></div><div class="foot">antamfoods.com<br>0348.635.222</div></div>
  <div class="card2">
   <div class="nc"><div class="f">{stack()}</div><div class="b">{mk()}<div><b>[Cần điền: họ tên]</b>[Cần điền: chức danh]</div><div class="ct">0348.635.222<br>antamfoods.com<br>TP.HCM</div></div></div>
   <div class="box"><div style="background:var(--do);color:var(--kem)">{mk()}</div><div style="background:var(--vang);color:var(--do)">{mk()}</div><div style="background:var(--muc);color:var(--kem)">{mk()}</div></div>
  </div>
 </div>
</div></section>

<footer class="foot-b"><div class="w">
 <div>{stack()}<p>Bản đề xuất hướng Vòm, chờ công ty duyệt. Logo gốc vẫn dùng cho tới khi duyệt. Sản Phẩm Tận Tâm - Phát Triển Xứng Tầm.</p></div>
 <div class="ct">0348.635.222<br>antamfoods.com</div>
</div></footer>
</body></html>"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())
