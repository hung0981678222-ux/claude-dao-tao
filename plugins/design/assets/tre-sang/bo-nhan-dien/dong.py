"""An Tâm bản động: trình bày bộ nhận diện bằng chuyển động, chữ cực lớn, bậc thang 3D thật.
Chạy: python3 dong.py OUT.html"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "nl2"))

import build_font_page as FP  # noqa: E402
import build_font_page2 as FP2  # noqa: E402
import build_tre as BTR  # noqa: E402
import logo_tre as T  # noqa: E402
import nen_tre as N  # noqa: E402
from mascot4 import be_cuon  # noqa: E402

CH, CH2, KEM, HONG, BO, DEN = T.CHERRY, T.CHERRY2, T.KEM, T.HONG, T.BO, T.DEN


def anim_wordmark(cls="awm", hat_cls="hat"):
    """Chữ an tâm: thân chữ đổi màu theo biến CSS, chiếc bánh tách riêng để nảy."""
    b = T.WB
    hat = T.hat(T.A2_CX - 4, T.A_TOP - 6, 44, "HATC", "WMC")
    hat = hat.replace('fill="HATC"', 'style="fill:var(--hatc)"').replace('fill="WMC"', 'style="fill:var(--wmc)"')
    return (f'<svg class="{cls}" viewBox="{b[0] - 6:.0f} {T.A_TOP - 46:.0f} {b[2] - b[0] + 12:.0f} {-T.A_TOP + 54:.0f}" role="img" aria-label="an tâm">'
            f'<path class="wm-body" d="{T.WM}"/><g class="{hat_cls}">{hat}</g></svg>')


def badge(text, uid):
    return (f'<svg class="badge" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="{uid}" d="M100,100 m-78,0 a78,78 0 1 1 156,0 a78,78 0 1 1 -156,0"/></defs>'
            f'<text style="font:800 15px \'An Tam Sans\';letter-spacing:4px" fill="currentColor"><textPath href="#{uid}">{text}</textPath></text></svg>')


def fill(svg):
    return svg.replace("<svg ", '<svg style="width:100%;height:100%;display:block" ', 1)


CSS = """
/* Bố cục: trang trình diễn thương hiệu toàn màn hình; mảng màu tràn viền, chữ cực lớn, chuyển động nhẹ, cảnh 3D cho chữ bậc thang. */
:root{--ch:#B5121B;--ch2:#7D0A10;--kem:#FFF4E8;--hong:#F7CFC6;--bo:#FFD37A;--den:#1B1B1B;--xam:#6B5A57;
--f:'An Tam Sans',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;--nd:'An Tam Sans Net Dut','An Tam Sans',sans-serif;--dn:'An Tam Sans Dom Nuong','An Tam Sans',sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
html{scroll-behavior:smooth;overflow-x:clip}
body{background:var(--den);color:var(--kem);font:400 17px/1.6 var(--f);-webkit-font-smoothing:antialiased;overflow-x:clip}
svg{max-width:100%}
.w{max-width:1320px;margin:0 auto;padding-inline:40px}
.lab{font:800 13px/1 var(--f);letter-spacing:.18em;text-transform:uppercase;display:flex;gap:10px;align-items:center}
.lab::before{content:"";width:10px;height:10px;border-radius:50%;background:currentColor}
.h{font:800 clamp(44px,7vw,112px)/.9 var(--f);letter-spacing:-.06em;text-wrap:balance}

/* HERO */
.hero{position:relative;min-height:min(100vh,900px);background:var(--ch);overflow:hidden;display:flex;flex-direction:column}
.hero .nav{display:flex;justify-content:space-between;align-items:center;padding:24px 40px;font:800 13px/1 var(--f);letter-spacing:.16em;position:relative;z-index:3}
.hero .nav a{color:var(--kem);text-decoration:none;opacity:.85}
.hero .stage{flex:1;position:relative;display:grid;place-items:center;padding:20px 40px 0}
.awm{width:min(92vw,1180px);height:auto;display:block;--wmc:var(--kem);--hatc:var(--bo);position:relative;z-index:2;overflow:visible}
.awm .wm-body{fill:var(--wmc)}
.hero .sub{position:relative;z-index:3;display:flex;justify-content:space-between;align-items:flex-end;gap:24px;padding:0 40px 28px;flex-wrap:wrap}
.hero .sub p{font:400 clamp(18px,2vw,26px)/1.3 var(--f);max-width:30ch}
.hero .sub p b{font-weight:800;color:var(--bo)}
.hero .badge{position:absolute;right:6vw;top:10vh;width:clamp(120px,14vw,200px);color:var(--bo);z-index:1}
.hero .masc{position:absolute;left:4vw;bottom:-2vh;width:clamp(140px,17vw,260px);z-index:3;filter:drop-shadow(0 20px 30px rgba(0,0,0,.35))}
.hero .blob{position:absolute;border-radius:50%;filter:blur(2px)}
.b1{width:46vw;height:46vw;right:-14vw;bottom:-22vw;background:var(--ch2)}
.b2{width:18vw;height:18vw;left:18vw;top:-6vw;background:var(--hong);opacity:.9}
.b3{width:9vw;height:9vw;right:30vw;bottom:12vh;background:var(--bo)}
.cta{display:inline-flex;gap:10px;align-items:center;background:var(--kem);color:var(--ch);font:800 15px/1 var(--f);padding:16px 22px;border-radius:999px;text-decoration:none}
.cta:focus-visible,.hero .nav a:focus-visible{outline:2px solid var(--bo);outline-offset:3px}

/* chữ chạy cực lớn */
.run{overflow:hidden;white-space:nowrap;padding-block:18px;line-height:.95}
.run div{display:inline-block;font-size:clamp(80px,14vw,220px);letter-spacing:-.05em}
.run span{padding-inline:.25em}
.run i{font-style:normal;display:inline-block;width:.42em;height:.42em;border-radius:50%;vertical-align:middle;margin-inline:.1em}
.r1{background:var(--kem);color:var(--ch)}.r1 div{font-family:var(--f);font-weight:800}.r1 i{background:var(--bo)}
.r2{background:var(--bo);color:var(--den)}.r2 div{font-family:var(--nd)}.r2 i{background:var(--ch)}
.r3{background:var(--den);color:var(--bo)}.r3 div{font-family:var(--dn)}.r3 i{background:var(--hong)}

/* bậc thang 3D */
.st3{background:radial-gradient(120% 90% at 50% 10%,#2A0A0E,#120507 70%);padding-block:110px 140px;overflow:hidden}
.st3 .w{display:grid;grid-template-columns:.8fr 1.2fr;gap:40px;align-items:center}
.st3 .h span{color:var(--bo)}
.st3 p{color:rgba(255,244,232,.75);margin-top:18px;max-width:42ch}
.scene{height:560px;perspective:1600px;display:grid;place-items:center;max-width:100%;overflow:clip}
.stairs{position:relative;width:520px;height:120px;transform-style:preserve-3d;transform:rotateX(-24deg) rotateY(-34deg) translateY(150px)}
.step{position:absolute;left:0;bottom:0;width:520px;height:120px;transform-style:preserve-3d}
.face{position:absolute;left:0;width:520px;display:flex;align-items:center;padding-inline:26px;font:800 86px/1 var(--f);letter-spacing:-.04em;backface-visibility:hidden}
.front{top:0;height:120px}
.top{top:0;height:130px;transform-origin:top;transform:rotateX(90deg) translateZ(0);font-size:72px}
.side{position:absolute;top:0;left:520px;width:130px;height:120px;transform-origin:left;transform:rotateY(90deg)}

/* logo động */
.dyn{background:var(--kem);color:var(--den);padding-block:110px}
.dyn .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:48px}
.tile{border-radius:36px;aspect-ratio:3/4;display:grid;place-items:center;padding:12%;position:relative;overflow:hidden}
.tile .awm{width:100%}
.tile small{position:absolute;left:20px;bottom:18px;font:800 12px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;opacity:.7}
.t1{background:var(--ch)}.t1 .awm{--wmc:var(--kem);--hatc:var(--bo)}
.t2{background:var(--bo);color:var(--den)}.t2 .awm{--wmc:var(--ch);--hatc:var(--kem)}
.t3{background:var(--hong)}.t3 .awm{--wmc:var(--den);--hatc:var(--ch)}
.t4{background:var(--den);color:var(--kem)}.t4 .awm{--wmc:transparent;--hatc:var(--bo)}
.t4 .awm .wm-body{stroke:#FFB3BA;stroke-width:2.4;filter:drop-shadow(0 0 6px #ff5a6a) drop-shadow(0 0 14px #ff2a40)}
.sys{display:grid;grid-template-columns:1.2fr 1fr;gap:16px;margin-top:16px}
.colors{display:flex;gap:10px;height:300px}
.colors div{flex:1;border-radius:28px;padding:18px;display:flex;flex-direction:column;justify-content:flex-end;font:800 15px/1.2 var(--f);transition:flex .45s cubic-bezier(.2,.8,.2,1)}
.colors div:hover{flex:2.4}
.colors small{display:block;font-weight:400;font-size:12px;opacity:.85}
.typo{border-radius:28px;background:var(--den);color:var(--kem);padding:28px;display:flex;flex-direction:column;justify-content:space-between;height:300px;overflow:hidden}
.typo .big{font:800 132px/.85 var(--f);letter-spacing:-.06em;color:var(--bo)}
.typo .row{display:flex;gap:16px;font-size:22px;flex-wrap:wrap}

/* sản phẩm nổi */
.float{background:linear-gradient(160deg,var(--hong),#F3B9AE);color:var(--den);padding-block:110px;overflow:hidden}
.float .stage3{display:grid;grid-template-columns:repeat(4,1fr);gap:28px;margin-top:56px;perspective:1400px}
.card3{border-radius:28px;overflow:hidden;box-shadow:0 40px 60px -30px rgba(90,0,10,.55),0 10px 20px -10px rgba(90,0,10,.3);transform:rotateY(-14deg) rotateX(6deg);background:#fff}
.card3:nth-child(even){transform:rotateY(14deg) rotateX(6deg) translateY(40px)}
.card3 svg{display:block;width:100%;height:auto}
.float .bigline{font:800 clamp(60px,9vw,150px)/.88 var(--f);letter-spacing:-.06em;color:var(--ch)}

/* nền chạy ngang */
.bgs{background:var(--ch);padding-block:100px;overflow:hidden}
.bgs .h{color:var(--kem)}.bgs .h span{color:var(--bo)}
.belt{display:flex;gap:18px;margin-top:48px;width:max-content}
.belt figure{width:230px;flex:none}
.belt .ph{aspect-ratio:9/16;border-radius:22px;overflow:hidden;box-shadow:0 20px 30px -18px rgba(0,0,0,.5)}
.belt figcaption{font:800 15px/1.2 var(--f);margin-top:10px}

/* kết */
.end{background:var(--bo);color:var(--den);padding-block:110px 60px;overflow:hidden}
.end .huge{font:800 clamp(90px,19vw,300px)/.82 var(--f);letter-spacing:-.07em;color:var(--ch)}
.end .huge span{font-family:var(--dn);font-weight:400;color:var(--den)}
.end .meta{display:flex;justify-content:space-between;gap:24px;flex-wrap:wrap;margin-top:40px;font:800 18px/1.5 var(--f)}
.end p{font:400 13px/1.5 var(--f);max-width:62ch;opacity:.75}

@media (prefers-reduced-motion:no-preference){
 .hero .hat{transform-box:fill-box;transform-origin:50% 100%;animation:nay 2.4s cubic-bezier(.3,.7,.3,1) infinite}
 @keyframes nay{0%,55%,100%{transform:translateY(0) rotate(0)}22%{transform:translateY(-22%) rotate(-8deg)}38%{transform:translateY(0) rotate(4deg)}}
 .hero .badge{animation:xoay 18s linear infinite}@keyframes xoay{to{transform:rotate(360deg)}}
 .hero .masc .vay{animation:vay 1.4s ease-in-out infinite}@keyframes vay{50%{transform:rotate(-16deg)}}
 .hero .masc .nhun{animation:nhun 2.6s ease-in-out infinite}@keyframes nhun{50%{transform:translateY(-8px)}}
 .hero .blob{animation:troi 9s ease-in-out infinite}.b2{animation-duration:7s}.b3{animation-duration:5s}@keyframes troi{50%{transform:translate(12px,-16px) scale(1.04)}}
 .run div{animation:chay 30s linear infinite}.r2 div{animation-direction:reverse;animation-duration:36s}.r3 div{animation-duration:26s}@keyframes chay{to{transform:translateX(-50%)}}
 .stairs{animation:lac 12s ease-in-out infinite}@keyframes lac{0%,100%{transform:rotateX(-24deg) rotateY(-34deg) translateY(150px)}50%{transform:rotateX(-18deg) rotateY(-14deg) translateY(150px)}}
 .tile .hat{transform-box:fill-box;transform-origin:50% 100%;animation:nay 2.4s cubic-bezier(.3,.7,.3,1) infinite}
 .t2 .hat{animation-delay:.3s}.t3 .hat{animation-delay:.6s}.t4 .hat{animation-delay:.9s}
 .t4 .awm .wm-body{animation:nhay 3s steps(1) infinite}@keyframes nhay{0%,100%{opacity:1}92%{opacity:.35}94%{opacity:1}96%{opacity:.5}}
 .card3{animation:noi 6s ease-in-out infinite}.card3:nth-child(even){animation-delay:-3s}
 @keyframes noi{50%{translate:0 -14px}}
 .belt{animation:bang 40s linear infinite}@keyframes bang{to{transform:translateX(-50%)}}
}
@media (max-width:900px){.w{padding-inline:18px}.hero .nav,.hero .sub{padding-inline:18px}
 .st3 .w,.sys{grid-template-columns:1fr}.scene{height:420px;transform:scale(.62)}
 .dyn .grid,.float .stage3{grid-template-columns:1fr 1fr}.colors{height:220px}.typo .big{font-size:90px}}
"""


def stairs3d():
    steps = [("bánh", "nóng", "var(--ch)", "var(--kem)", "var(--ch2)"), ("cuộn", "mềm", "var(--bo)", "var(--ch)", "#D9A94A"),
             ("ăn là", "an tâm", "var(--kem)", "var(--ch)", "#E9D6BF")]
    out = ""
    for i, (front, top, bg, fg, side) in enumerate(steps):
        out += (f'<div class="step" style="transform:translate3d(0,{-i * 120}px,{-i * 130}px)">'
                f'<div class="face front" style="background:{bg};color:{fg}">{front}</div>'
                f'<div class="face top" style="background:{bg};color:{fg};filter:brightness(1.08)">{top}</div>'
                f'<div class="side" style="background:{side}"></div></div>')
    return f'<div class="scene" aria-label="Chữ bậc thang 3D: bánh nóng, cuộn mềm, ăn là an tâm"><div class="stairs">{out}</div></div>'


def run(cls, words):
    seq = "".join(f"<span>{w}</span><i></i>" for w in words) * 3
    return f'<div class="run {cls}" aria-hidden="true"><div>{seq}{seq}</div></div>'


def page():
    W = BTR
    masc = be_cuon("hero", "cuoi", "chao").replace("<svg ", '<svg class="masc" ', 1)
    belt = "".join(f'<figure><div class="ph">{fill(fn(1080, 1920))}</div><figcaption>{name}</figcaption></figure>' for k, (name, d, fn) in N.NEN.items())
    cards = "".join(f'<div class="card3">{svg}</div>' for svg in (W.cup(), W.tote(), W.phone(), W.box()))
    h = f"""<title>An Tâm Chuyển Động</title>
<style>{FP.faces()}
{FP2.faces2()}
{CSS}</style>

<header class="hero">
 <div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
 <nav class="nav"><span>ẨM THỰC AN TÂM</span><a href="#he-thong">Bộ nhận diện ↓</a></nav>
 {badge("ẨM THỰC AN TÂM · ĂN LÀ AN TÂM · ", "bd")}
 <div class="stage">{anim_wordmark()}</div>
 {masc}
 <div class="sub"><span></span><p>Bánh tortillas và doner kebab cho thế hệ văn phòng mới. <b>Ăn là an tâm.</b></p><a class="cta" href="#he-thong">Xem hệ thống →</a></div>
</header>

{run("r1", ["bánh nóng", "cuộn mềm", "giao liền"])}
{run("r2", ["ăn là an tâm", "tận tâm", "đúng hẹn"])}
{run("r3", ["tortillas", "taco", "doner kebab"])}

<section class="st3"><div class="w">
 <div><p class="lab" style="color:var(--bo)">Chữ bậc thang 3D</p><h2 class="h" style="margin-top:18px">Chữ <span>leo bậc</span>, thật sự 3D</h2>
 <p>Chữ bậc thang giờ là khối 3D thật: mặt đứng là thành bậc, mặt nằm là mặt bậc, xoay nhẹ như đang đi lên. Dùng cho màn hình cửa hàng, video, trang web, sự kiện.</p></div>
 {stairs3d()}
</div></section>

<section class="dyn" id="he-thong"><div class="w">
 <p class="lab" style="color:var(--ch)">Logo động</p><h2 class="h" style="margin-top:18px">Một logo, <span style="color:var(--ch)">bốn tâm trạng</span></h2>
 <div class="grid">
  <div class="tile t1">{anim_wordmark()}<small style="color:var(--kem)">Cherry · chính</small></div>
  <div class="tile t2">{anim_wordmark()}<small>Vàng bơ · khuyến mãi</small></div>
  <div class="tile t3">{anim_wordmark()}<small>Hồng phấn · mạng xã hội</small></div>
  <div class="tile t4">{anim_wordmark()}<small>Neon · cửa hàng ban đêm</small></div>
 </div>
 <div class="sys">
  <div class="colors"><div style="background:var(--ch);color:var(--kem)">Cherry<small>#B5121B</small></div><div style="background:#fff;border:1px solid #EED9C8">Kem<small>#FFF4E8</small></div><div style="background:var(--den);color:var(--kem)">Đen<small>#1B1B1B</small></div><div style="background:var(--hong)">Hồng phấn<small>#F7CFC6</small></div><div style="background:var(--bo)">Vàng bơ<small>#FFD37A</small></div></div>
  <div class="typo"><span class="big">âêô</span><div class="row"><span style="font-weight:800">Đậm</span><span>Thường</span><span style="font-family:var(--nd)">Nét Đứt</span><span style="font-family:var(--dn)">Đốm Nướng</span></div><small style="opacity:.7">Font riêng An Tâm Sans · mọi dấu mũ là chiếc bánh</small></div>
 </div>
</div></section>

<section class="float"><div class="w">
 <p class="lab" style="color:var(--ch)">Ứng dụng</p><div class="bigline">cầm lên là<br>biết an tâm.</div>
 <div class="stage3">{cards}</div>
</div></section>

<section class="bgs"><div class="w"><p class="lab" style="color:var(--bo)">Nền thương hiệu</p><h2 class="h" style="margin-top:18px">Tám nền, <span>chạy không ngừng</span></h2></div>
 <div class="belt">{belt}{belt}</div>
</section>

<footer class="end"><div class="w">
 <div class="huge">ăn là<br><span>an tâm.</span></div>
 <div class="meta"><span>0348.635.222 · antamfoods.com</span><span>Sản Phẩm Tận Tâm - Phát Triển Xứng Tầm</span></div>
 <p style="margin-top:18px">Bản đề xuất trình diễn, chờ công ty duyệt. Hệ logo, màu, font và nền dùng chung với bộ nhận diện tổng thể.</p>
</div></footer>
"""
    return h.replace("px Lexend", "px 'An Tam Sans'")


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())
