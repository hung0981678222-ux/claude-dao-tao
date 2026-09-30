"""Thế giới thương hiệu Ẩm Thực An Tâm: tính cách, giọng nói, linh vật Bé Cuộn,
bộ sticker, poster chiến dịch, ứng dụng. Chạy: python3 the_gioi.py OUT.html"""
import sys

import build_nl2  # noqa: F401  (nạp logo mới vào NL.OUT)
import build_nl as B
import logo_nl as NL
import logo2 as L2
from mascot4 import be_cuon

DO, DO2, VANG, KEM, MUC, BO = L2.DO, L2.DO2, L2.VANG, L2.KEM, L2.MUC, L2.BO
OUT = NL.OUT


def m(u, mat, tay, n=0, chan="dung", cls=""):
    return be_cuon(u, mat, tay, n, chan=chan).replace("<svg ", f'<svg class="bc {cls}" ', 1)


def lg(k, cls=""):
    return OUT[k].replace("<svg ", f'<svg class="lg {cls}" ', 1)


TRAITS = [
    ("tt", "mat_tim", "tim", 0, "dung", "Tận tâm", "Làm bánh như làm cho người nhà ăn. Bột, nhân, giờ giao đều chăm chút."),
    ("nn", "cuoi", "chay", -10, "chay", "Nhanh nhẹn", "Đơn tới là chạy. Giao đúng hẹn, bánh tới tay còn nóng."),
    ("vv", "nhay", "like", 0, "dung", "Vui vẻ", "Nói chuyện gần gũi, có chút duyên, như người quen trong xóm."),
    ("rr", "cuoi", "om_tui", 0, "dung", "Rõ ràng", "Bếp sạch, giá rõ, nói được làm được. Không hứa suông."),
]

VOICE = [
    ("Bánh vừa ra lò, anh chị đặt liền nha.", "Sản phẩm chất lượng số 1 thị trường."),
    ("Đơn của anh chị đang trên đường, 15 phút nữa tới.", "Chúng tôi sẽ cố gắng giao sớm nhất có thể."),
    ("Nhân viên đói bụng giữa chiều? Có Bé Cuộn lo.", "Giải pháp ẩm thực đỉnh cao cho doanh nghiệp."),
    ("Giá rõ ràng, gửi báo giá trong ngày.", "Liên hệ để nhận ưu đãi khủng."),
]

STICKERS = [
    ("s1", "cuoi", "chao", "CHÀO ANH CHỊ!"), ("s2", "nhay", "like", "ĐÃ NHẬN ĐƠN"),
    ("s3", "cuoi", "chay", "ĐANG GIAO NÈ"), ("s4", "le", "cam", "NGON HÔNG?"),
    ("s5", "mat_tim", "tim", "CẢM ƠN NHIỀU!"), ("s6", "cuoi", "hai_tay", "AN TÂM NHA"),
    ("s7", "ngac", "om_tui", "BÁNH NÓNG ĐÂY"), ("s8", "nham", "tim", "HẸN GẶP LẠI"),
]

CSS = """
/* Bố cục: trang "thế giới thương hiệu" nhiều năng lượng, mảng màu lớn, linh vật là nhân vật chính. */
:root{--do:#D7150E;--do2:#A90F09;--vang:#FFC53D;--kem:#FFF6E6;--muc:#3A1410;--bo:#FFE3A3;--xam:#6D5049;
--ten:'Fraunces AT',Georgia,serif;--hep:'Anton','Arial Narrow',sans-serif;--noi:'Be Vietnam Pro',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--kem);color:var(--muc);font:400 17px/1.6 var(--noi);-webkit-font-smoothing:antialiased;overflow-x:hidden}
svg{max-width:100%}
svg.lg,svg.bc{display:block;width:100%;height:auto}
.w{max-width:1200px;margin:0 auto;padding-inline:40px}
section{padding-block:96px}
.kick{font:400 18px/1 var(--hep);letter-spacing:.08em;color:var(--do);display:flex;gap:12px;align-items:center}
.kick::before{content:"";width:34px;height:3px;background:currentColor}
h2{font:900 clamp(44px,6.4vw,88px)/.95 var(--ten);letter-spacing:-.025em;margin-top:14px;text-wrap:balance}
h2 span{color:var(--do)}
.on-do{background:var(--do);color:var(--kem)}.on-do .kick,.on-do h2 span{color:var(--vang)}
.on-vang{background:var(--vang)}.on-muc{background:var(--muc);color:var(--kem)}.on-muc .kick,.on-muc h2 span{color:var(--vang)}
.lead{max-width:58ch;margin-top:18px;font-size:18px;opacity:.9}

/* chuyển động */
@media (prefers-reduced-motion:no-preference){
 .song .nhun{animation:nhun 2.6s ease-in-out infinite}
 .song .vay{animation:vay 1.4s ease-in-out infinite}
 .song .vay2{animation:vay2 1.4s ease-in-out infinite}
 @keyframes nhun{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
 @keyframes vay{0%,100%{transform:rotate(0)}50%{transform:rotate(-16deg)}}
 @keyframes vay2{0%,100%{transform:rotate(0)}50%{transform:rotate(16deg)}}
 .khoi path{animation:khoi 2.2s ease-in-out infinite}
 @keyframes khoi{0%,100%{opacity:.25;transform:translateY(6px)}50%{opacity:.9;transform:translateY(-4px)}}
}

/* đầu trang */
.hero{background:var(--vang);position:relative;overflow:hidden}
.hero .w{display:grid;grid-template-columns:1.15fr .85fr;align-items:center;gap:24px;padding-block:48px 0;position:relative;z-index:1}
.hero .lg{max-width:600px}
.hero h1{font:400 clamp(48px,7vw,104px)/.92 var(--hep);color:var(--do);text-transform:uppercase;margin-top:28px;letter-spacing:.005em}
.hero h1 span{color:var(--muc)}
.hero p{font-size:18px;margin-top:16px;max-width:40ch}
.hero .bc{max-width:420px;justify-self:center;filter:drop-shadow(0 30px 30px rgba(120,40,0,.25))}
.hero .burst{position:absolute;right:-8%;top:-20%;width:62%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle,#FFE08A 0 38%,transparent 38.5%),repeating-conic-gradient(#FFB82E 0 7.5deg,#FFC53D 7.5deg 15deg);opacity:.9}
.strip{background:var(--do);color:var(--kem);overflow:hidden;white-space:nowrap;padding-block:16px;font:400 28px/1 var(--hep);letter-spacing:.04em;position:relative;z-index:2}
.strip span{display:inline-block;padding-inline:22px}
.strip i{font-style:normal;color:var(--vang)}
@media (prefers-reduced-motion:no-preference){.strip div{display:inline-block;animation:chay 26s linear infinite}@keyframes chay{to{transform:translateX(-50%)}}}

/* tính cách */
.traits{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:48px}
.trait{border-radius:28px;padding:22px 22px 26px;display:flex;flex-direction:column;gap:6px;background:#fff;border:2px solid #F0DCC0}
.trait:nth-child(1){background:var(--do);color:var(--kem);border:0}
.trait:nth-child(2){background:var(--vang);border:0}
.trait:nth-child(3){background:var(--muc);color:var(--kem);border:0}
.trait .bc{max-width:200px;align-self:center}
.trait b{font:400 34px/1 var(--hep);text-transform:uppercase;margin-top:8px}
.trait p{font-size:15px;opacity:.9}

/* giọng nói */
.voice{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:40px}
.voice div{border-radius:24px;padding:24px 28px}
.voice .yes{background:#fff;border:2px solid #F0DCC0}.voice .no{background:transparent;border:2px dashed #D9BFA0}
.voice h3{font:400 24px/1 var(--hep);text-transform:uppercase;margin-bottom:12px}
.voice .yes h3{color:#2F7D24}.voice .no h3{color:var(--do)}
.voice ul{list-style:none;padding:0;display:grid;gap:10px}
.voice li{font-size:17px;padding-left:28px;position:relative}
.voice .yes li::before{content:"✓";position:absolute;left:0;color:#2F7D24;font-weight:700}
.voice .no li{color:var(--xam);text-decoration:line-through;text-decoration-color:rgba(215,21,14,.5)}
.voice .no li::before{content:"✕";position:absolute;left:0;color:var(--do);font-weight:700}

/* hồ sơ Bé Cuộn */
.bio{display:grid;grid-template-columns:.9fr 1.1fr;gap:40px;align-items:center;margin-top:24px}
.bio .bc{max-width:440px;justify-self:center}
.card{background:var(--kem);color:var(--muc);border-radius:28px;padding:34px;box-shadow:0 30px 60px -30px rgba(0,0,0,.5);transform:rotate(1.5deg)}
.card h3{font:900 54px/1 var(--ten);color:var(--do)}
.card dl{display:grid;grid-template-columns:auto 1fr;gap:10px 18px;margin-top:20px}
.card dt{font:400 18px/1.4 var(--hep);color:var(--do);text-transform:uppercase}
.card dd{font-size:16px}
.quote{font:900 30px/1.1 var(--ten);margin-top:22px;padding-top:18px;border-top:3px dashed #E8C9A0}

/* sticker */
.stickers{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:48px}
.stk{display:flex;flex-direction:column;align-items:center;gap:0;position:relative}
.stk .bc{width:78%;filter:url(#vien)}
.stk b{font:400 22px/1 var(--hep);background:var(--muc);color:var(--kem);padding:10px 14px;border-radius:14px;margin-top:-14px;position:relative;box-shadow:0 0 0 5px #fff;transform:rotate(-3deg)}
.stk:nth-child(2n) b{background:var(--do);transform:rotate(3deg)}
.phone{margin:40px auto 0;max-width:360px;background:#111;border-radius:40px;padding:12px}
.chat{background:#E8F0FB;border-radius:30px;padding:18px 14px;display:grid;gap:10px;font-size:14px}
.chat .me{justify-self:end;background:#0068FF;color:#fff;border-radius:18px 18px 4px 18px;padding:10px 14px;max-width:80%}
.chat .them{justify-self:start;background:#fff;border-radius:18px 18px 18px 4px;padding:10px 14px;max-width:80%}
.chat .st{justify-self:start;width:120px}
.chat .st .bc{filter:url(#vien)}
.chat small{text-align:center;color:#6b7a90;font-size:11px}

/* poster */
.posters{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:48px}
.poster{border-radius:24px;aspect-ratio:4/5;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:26px}
.poster .lg.top{width:44%}
.poster .st{position:absolute;inset:18% 0 0 0;display:grid;place-items:center}
.poster .st svg{width:88%;height:auto}
.poster .foot{margin-top:auto;font:400 15px/1.2 var(--hep);letter-spacing:.06em;position:relative}
.poster h4{font:400 clamp(40px,4.4vw,64px)/.92 var(--hep);text-transform:uppercase;margin-top:18px;position:relative}

/* ứng dụng */
.apps{display:grid;grid-template-columns:repeat(12,1fr);gap:16px;margin-top:48px}
.app{border-radius:28px;overflow:hidden;position:relative;min-height:320px}
.app .cap{position:absolute;left:16px;top:14px;z-index:3;font:400 14px/1 var(--hep);letter-spacing:.06em;background:var(--kem);color:var(--muc);padding:8px 12px;border-radius:999px}
.a7{grid-column:span 7}.a5{grid-column:span 5}.a4{grid-column:span 4}.a8{grid-column:span 8}.a6{grid-column:span 6}
.mk{display:block;width:100%;height:auto}
footer{background:var(--muc);color:var(--kem);padding-block:64px 40px}
footer .w{display:grid;grid-template-columns:auto 1fr auto;gap:36px;align-items:center}
footer .lg{width:260px}
footer p{font-size:14px;opacity:.72;max-width:60ch}
footer .ct{font:400 22px/1.4 var(--hep);text-align:right}
@media (max-width:900px){.w{padding-inline:18px}section{padding-block:64px}
 .hero .w{grid-template-columns:1fr}.hero .bc{max-width:280px}.hero .burst{width:120%;right:-50%;top:30%}
 .traits,.stickers{grid-template-columns:1fr 1fr}.voice,.bio{grid-template-columns:1fr}.posters{grid-template-columns:1fr}
 .a7,.a5,.a4,.a8,.a6{grid-column:1/-1}
 footer .w{grid-template-columns:1fr}footer .ct{text-align:left}}
"""


def xe_giao():
    """Xe máy giao hàng có thùng in linh vật."""
    return f"""<svg class="mk" viewBox="0 0 700 420" role="img" aria-label="Xe giao hàng">
<rect width="700" height="420" fill="#FCE9C4"/><rect y="340" width="700" height="80" fill="#E9D0A4"/>
<ellipse cx="360" cy="352" rx="250" ry="14" fill="#000" opacity=".15"/>
<circle cx="200" cy="320" r="46" fill="#2A1512"/><circle cx="200" cy="320" r="20" fill="#9A8A80"/>
<circle cx="520" cy="320" r="46" fill="#2A1512"/><circle cx="520" cy="320" r="20" fill="#9A8A80"/>
<path d="M200,320 L300,250 H470 L520,320" fill="none" stroke="#2A1512" stroke-width="14" stroke-linejoin="round"/>
<path d="M440,250 L500,160 H540" fill="none" stroke="#2A1512" stroke-width="12" stroke-linecap="round"/>
<path d="M300,250 Q380,212 470,250 Z" fill="{DO}"/>
<rect x="150" y="96" width="210" height="170" rx="16" fill="{DO}"/>
<rect x="150" y="96" width="210" height="28" rx="14" fill="{DO2}"/>
<g transform="translate(166 132)">{OUT['wm_do'].replace('<svg ', '<svg width="180" height="72" ', 1)}</g>
<g transform="translate(372 96)">{be_cuon('xg', 'cuoi', 'chao').replace('<svg ', '<svg width="130" height="148" ', 1)}</g>
<text x="176" y="250" fill="{VANG}" style="font:400 17px Anton">GIAO TẬN NƠI · 0348.635.222</text>
</svg>"""


def ao():
    return f"""<svg class="mk" viewBox="0 0 500 420" role="img" aria-label="Áo nhân viên">
<rect width="500" height="420" fill="{BO}"/>
<path d="M150,70 L200,50 Q250,80 300,50 L350,70 L420,130 L380,180 L350,160 V380 H150 V160 L120,180 L80,130 Z" fill="{DO}"/>
<path d="M200,50 Q250,86 300,50" fill="none" stroke="{VANG}" stroke-width="8"/>
<g transform="translate(270 110)">{OUT['mark_vang'].replace('<svg ', '<svg width="56" height="56" ', 1)}</g>
<g transform="translate(160 190)">{OUT['wm_do'].replace('<svg ', '<svg width="180" height="72" ', 1)}</g>
<text x="250" y="330" text-anchor="middle" fill="{KEM}" style="font:400 22px Anton;letter-spacing:.06em">ĂN LÀ AN TÂM</text>
</svg>"""


def ly():
    return f"""<svg class="mk" viewBox="0 0 500 420" role="img" aria-label="Ly nước và hộp giấy">
<rect width="500" height="420" fill="{MUC}"/>
<ellipse cx="170" cy="372" rx="80" ry="12" fill="#000" opacity=".4"/>
<path d="M104,110 H236 L220,370 H120 Z" fill="{KEM}"/>
<rect x="96" y="92" width="148" height="24" rx="8" fill="{DO}"/>
<g transform="translate(118 160)">{OUT['mark_do'].replace('<svg ', '<svg width="104" height="104" ', 1)}</g>
<text x="170" y="320" text-anchor="middle" fill="{DO}" style="font:400 18px Anton;letter-spacing:.06em">AN TÂM NHA</text>
<ellipse cx="350" cy="372" rx="100" ry="12" fill="#000" opacity=".4"/>
<path d="M260,200 L350,170 L440,200 L440,360 L350,390 L260,360 Z" fill="{VANG}"/>
<path d="M260,200 L350,230 L440,200 L350,170 Z" fill="#FFD875"/><path d="M350,230 V390" stroke="#D99A1E" stroke-width="2"/>
<g transform="translate(270 250)">{be_cuon('hp', 'nhay', 'like').replace('<svg ', '<svg width="72" height="82" ', 1)}</g>
<g transform="translate(355 250) skewY(-18)">{OUT['wm_kem'].replace('<svg ', '<svg width="80" height="34" ', 1)}</g>
</svg>"""


def page():
    traits = "".join(f'<div class="trait">{m(u, a, t, n, c)}<b>{name}</b><p>{p}</p></div>' for u, a, t, n, c, name, p in TRAITS)
    yes = "".join(f"<li>{a}</li>" for a, _ in VOICE)
    no = "".join(f"<li>{b}</li>" for _, b in VOICE)
    stickers = "".join(f'<div class="stk">{m(u, a, t, -10 if t == "chay" else 0, "chay" if t == "chay" else "dung")}<b>{txt}</b></div>' for u, a, t, txt in STICKERS)
    stair = NL.stairs(["ĂN LÀ", "AN TÂM"], VANG, hi=KEM, hi_idx=(1,), D=120, H=150)
    stair2 = NL.stairs(["BỮA", "NHẸ", "VĂN", "PHÒNG"], DO, hi=MUC, hi_idx=(3,))
    strip_items = "".join(f"<span>{t}</span><i>✦</i>" for t in ["ĂN LÀ AN TÂM", "BÁNH TORTILLAS", "DONER KEBAB", "GIAO TẬN VĂN PHÒNG", "NHƯỢNG QUYỀN CỬA HÀNG"] * 2)
    return f"""<title>An Tâm Thế Giới Bé Cuộn</title>
<style>{B.fontfaces()}
{CSS}</style>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><filter id="vien" x="-20%" y="-20%" width="140%" height="140%">
<feMorphology in="SourceAlpha" operator="dilate" radius="7" result="d"/><feFlood flood-color="#fff"/><feComposite in2="d" operator="in" result="w"/>
<feDropShadow in="w" dx="0" dy="6" stdDeviation="5" flood-opacity=".25" result="s"/><feMerge><feMergeNode in="s"/><feMergeNode in="SourceGraphic"/></feMerge></filter></svg>

<header class="hero"><div class="burst"></div><div class="w">
 <div>{OUT['wm_kem'].replace('<svg ', '<svg class="lg" ', 1)}
  <h1>Ăn là <span>an tâm.</span></h1>
  <p>Gặp Bé Cuộn, chiếc bánh cuộn tận tâm của Sài Gòn. Bánh tortillas và doner kebab cho văn phòng, cửa hàng, và đối tác nhượng quyền.</p></div>
 {m('hero', 'cuoi', 'chao', cls='song')}
</div><div class="strip"><div>{strip_items}</div></div></header>

<section><div class="w">
 <p class="kick">TÍNH CÁCH THƯƠNG HIỆU</p>
 <h2>Bốn nét <span>làm nên An Tâm</span></h2>
 <p class="lead">Mọi thứ An Tâm làm, từ chữ trên hộp tới câu trả lời tin nhắn, đều mang bốn nét này. Bé Cuộn là người thể hiện chúng.</p>
 <div class="traits">{traits}</div>
</div></section>

<section class="on-vang"><div class="w">
 <p class="kick">GIỌNG NÓI</p>
 <h2>Nói như <span>người quen</span></h2>
 <p class="lead">Xưng "An Tâm", gọi khách là "anh chị". Câu ngắn, cụ thể, có chút duyên. Không khoe khoang, không hứa điều chưa chắc.</p>
 <div class="voice"><div class="yes"><h3>Nói thế này</h3><ul>{yes}</ul></div><div class="no"><h3>Không nói thế này</h3><ul>{no}</ul></div></div>
</div></section>

<section class="on-do"><div class="w">
 <p class="kick">LINH VẬT</p>
 <h2>Đây là <span>Bé Cuộn</span></h2>
 <div class="bio">{m('bio', 'le', 'cam', cls='song')}
  <div class="card"><h3>Bé Cuộn</h3>
   <dl><dt>Quê</dt><dd>Bếp An Tâm, TP.HCM</dd><dt>Tuổi</dt><dd>Mới ra lò sáng nay</dd><dt>Nghề</dt><dd>Giao bánh, giữ lời hứa</dd>
   <dt>Thích</dt><dd>Bánh nóng, khách cười, giao đúng giờ</dd><dt>Ghét</dt><dd>Bánh nguội, đơn trễ, giá mập mờ</dd></dl>
   <p class="quote">"Có Bé Cuộn lo, anh chị cứ an tâm nha!"</p></div></div>
</div></section>

<section><div class="w">
 <p class="kick">BỘ STICKER ZALO</p>
 <h2>Tám câu <span>Bé Cuộn hay nói</span></h2>
 <p class="lead">Dùng khi nhắn tin với khách trên Zalo, Messenger: xác nhận đơn, báo đang giao, cảm ơn. Khách nhớ mặt, nhớ tên.</p>
 <div class="stickers">{stickers}</div>
 <div class="phone"><div class="chat"><small>Zalo · Ẩm Thực An Tâm</small>
  <div class="me">Cho mình 30 phần doner cuộn lúc 15h nhé</div>
  <div class="st">{m('c1', 'nhay', 'like')}</div>
  <div class="them">Dạ An Tâm đã nhận đơn 30 phần, giao lúc 15h tại văn phòng anh chị ạ.</div>
  <div class="st">{m('c2', 'cuoi', 'chay', -10, 'chay')}</div></div></div>
</div></section>

<section class="on-muc"><div class="w">
 <p class="kick">POSTER CHIẾN DỊCH</p>
 <h2>Chữ bậc thang <span>và Bé Cuộn</span></h2>
 <div class="posters">
  <div class="poster" style="background:var(--do);color:var(--kem)">{lg('wm_do', 'top')}<div class="st" style="inset:16% 24% 18% 0">{stair}</div>
   <div style="position:absolute;right:3%;bottom:9%;width:34%">{m('p1', 'cuoi', 'chay', -10, 'chay')}</div>
   <p class="foot">ANTAMFOODS.COM · 0348.635.222</p></div>
  <div class="poster" style="background:var(--vang);color:var(--muc)">{lg('wm_bo', 'top')}<div class="st" style="inset:14% 0 16% 30%">{stair2}</div>
   <div style="position:absolute;left:3%;bottom:9%;width:34%">{m('p2', 'ngac', 'om_tui')}</div>
   <p class="foot" style="text-align:right">GIAO TẬN VĂN PHÒNG</p></div>
  <div class="poster" style="background:var(--kem);color:var(--muc)">{lg('wm_kem', 'top')}<h4 style="color:var(--do)">Nóng hổi<br><span style="color:var(--muc)">vừa ra lò</span></h4>
   <div style="position:absolute;right:-4%;bottom:-2%;width:58%">{m('p3', 'le', 'cam')}</div>
   <p class="foot" style="max-width:44%">BÁNH TORTILLAS<br>DONER KEBAB</p></div>
 </div>
</div></section>

<section><div class="w">
 <p class="kick">ỨNG DỤNG</p>
 <h2>Bé Cuộn <span>đi khắp nơi</span></h2>
 <div class="apps">
  <div class="app a7"><span class="cap">THÙNG XE GIAO HÀNG</span>{xe_giao()}</div>
  <div class="app a5"><span class="cap">ÁO NHÂN VIÊN</span>{ao()}</div>
  <div class="app a6"><span class="cap">LY VÀ HỘP</span>{ly()}</div>
  <div class="app a6" style="background:var(--do);display:grid;place-items:center;padding:40px"><span class="cap">LOGO</span>
   <div style="width:min(100%,460px)">{lg('wm_do')}</div></div>
 </div>
</div></section>

<footer><div class="w">
 {lg('wm_muc')}
 <p>Sản Phẩm Tận Tâm - Phát Triển Xứng Tầm. Bản đề xuất, chờ công ty duyệt. Câu "Ăn là an tâm", hồ sơ Bé Cuộn và các câu thoại là đề xuất sáng tạo, sửa được.</p>
 <div class="ct">0348.635.222<br>ANTAMFOODS.COM</div>
</div></footer>
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())
