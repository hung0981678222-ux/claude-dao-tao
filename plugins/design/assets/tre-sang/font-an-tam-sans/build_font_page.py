"""Trang giới thiệu font An Tâm Sans. Chạy: python3 build_font_page.py OUT.html"""
import base64
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MH = "/home/user/claude-dao-tao/plugins/design/assets/minh-hoa"
RG = {
    "vietnamese": "U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB",
    "latin": "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD",
}


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()


def ill(n):
    return b64(f"{MH}/{n}.svg", "image/svg+xml")


def faces():
    out = []
    for style, w in (("ExtraBold", 800), ("Regular", 400)):
        for sub, rg in RG.items():
            out.append(f"@font-face{{font-family:'An Tam Sans';font-weight:{w};font-display:swap;src:url({b64(os.path.join(HERE, f'AnTamSans-{style}-{sub}.woff2'), 'font/woff2')}) format('woff2');unicode-range:{rg}}}")
    return "\n".join(out)


CSS = """
/* Bố cục: trang mẫu chữ (type specimen); nền kem, chữ cherry; font được trình diễn bằng chữ thật, gõ được. */
:root{--ch:#B5121B;--ch2:#7D0A10;--kem:#FFF4E8;--hong:#F7CFC6;--bo:#FFD37A;--den:#1B1B1B;--xam:#6B5A57;--line:#EED9C8;
--f:'An Tam Sans',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;color-scheme:light}
*{box-sizing:border-box;margin:0}
body{background:var(--kem);color:var(--den);font:400 17px/1.6 var(--f);-webkit-font-smoothing:antialiased;overflow-x:hidden}
.w{max-width:1240px;margin:0 auto;padding-inline:40px}
section{padding-block:96px;border-top:1px solid var(--line)}
.lab{display:inline-flex;gap:8px;align-items:center;font:800 12px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;padding:9px 14px;border-radius:999px;background:var(--den);color:var(--kem)}
.lab i{width:8px;height:8px;border-radius:50%;background:var(--bo)}
h2{font:800 clamp(40px,6vw,80px)/.98 var(--f);letter-spacing:-.05em;margin-top:18px;text-wrap:balance}
h2 span{color:var(--ch)}
.lead{color:var(--xam);max-width:58ch;margin-top:16px;font-size:18px}
.hero{background:var(--ch);color:var(--kem);padding-block:28px 0;overflow:hidden;border:0}
.hero .top{display:flex;justify-content:space-between;font:800 12px/1 var(--f);letter-spacing:.14em}
.hero .big{font:800 clamp(110px,22vw,320px)/.86 var(--f);letter-spacing:-.06em;margin-top:56px;white-space:nowrap}
.hero .big span{color:var(--bo)}
.hero .sub{display:grid;grid-template-columns:1fr 1fr;gap:40px;padding-block:36px 48px;font-size:18px;opacity:.95}
.hero .sub b{font-weight:800;font-size:22px;display:block;margin-bottom:6px}
.traits{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:48px}
.trait{background:#fff;border:1px solid var(--line);border-radius:32px;padding:36px;display:flex;flex-direction:column;gap:12px}
.trait .z{font:800 220px/.9 var(--f);letter-spacing:-.06em;color:var(--ch);display:flex;gap:24px;align-items:flex-end;overflow:hidden}
.trait b{font:800 26px/1.1 var(--f);letter-spacing:-.03em}
.trait p{color:var(--xam);font-size:15px}
.set{margin-top:40px;display:grid;gap:12px}
.set div{font:800 clamp(30px,4vw,54px)/1.2 var(--f);letter-spacing:-.02em;word-break:break-all}
.set div.r{font-weight:400}
.set div.vn{color:var(--ch)}
.tester{margin-top:40px;background:#fff;border:1px solid var(--line);border-radius:32px;padding:28px}
.tester .ctl{display:flex;gap:16px;align-items:center;flex-wrap:wrap;font:800 13px/1 var(--f)}
.tester .ctl button{font:800 13px/1 var(--f);border:1px solid var(--den);background:transparent;padding:10px 14px;border-radius:999px;cursor:pointer}
.tester .ctl button[aria-pressed="true"]{background:var(--den);color:var(--kem)}
.tester .ctl button:focus-visible,.tester textarea:focus-visible{outline:2px solid var(--ch);outline-offset:3px}
.tester input[type=range]{accent-color:var(--ch);width:200px}
.tester textarea{margin-top:18px;width:100%;min-height:200px;border:0;background:transparent;resize:vertical;font-family:var(--f);font-weight:800;font-size:72px;line-height:1.1;letter-spacing:-.03em;color:var(--ch)}
.uses{display:grid;grid-template-columns:repeat(12,1fr);gap:16px;margin-top:48px}
.use{border-radius:32px;overflow:hidden;position:relative;padding:36px;min-height:380px;display:flex;flex-direction:column}
.u7{grid-column:span 7}.u5{grid-column:span 5}.u4{grid-column:span 4}.u8{grid-column:span 8}.u6{grid-column:span 6}
.use .cap{font:800 11px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;opacity:.7}
.poster{background:var(--ch);color:var(--kem)}
.poster h3{font:800 clamp(56px,7vw,110px)/.9 var(--f);letter-spacing:-.06em;margin-top:auto}
.poster h3 span{color:var(--bo)}
.poster img{position:absolute;right:-30px;top:20px;width:52%;filter:drop-shadow(0 20px 20px rgba(0,0,0,.3))}
.menu{background:var(--den);color:var(--kem)}
.menu h3{font:800 54px/1 var(--f);letter-spacing:-.04em;color:var(--bo);margin-top:14px}
.menu ul{list-style:none;padding:0;margin-top:18px;display:grid;gap:10px}
.menu li{display:flex;gap:10px;align-items:baseline;font:800 24px/1.2 var(--f);letter-spacing:-.02em}
.menu li i{flex:1;border-bottom:2px dotted rgba(255,244,232,.35)}
.menu li em{font-style:normal;font-weight:400;font-size:16px;color:var(--bo)}
.pack{background:var(--hong)}
.pack .box{margin:auto;background:var(--kem);border-radius:18px;padding:30px 26px;width:min(100%,320px);box-shadow:0 30px 40px -24px rgba(80,0,0,.45);text-align:center}
.pack .box b{display:block;font:800 64px/.9 var(--f);letter-spacing:-.05em;color:var(--ch)}
.pack .box span{display:block;font:800 14px/1.2 var(--f);letter-spacing:.12em;margin-top:12px}
.pack .box small{display:block;font:400 12px/1.4 var(--f);color:var(--xam);margin-top:10px}
.chat{background:var(--bo)}
.bub{background:#fff;border-radius:22px 22px 22px 6px;padding:16px 18px;font:400 18px/1.45 var(--f);max-width:90%;margin-top:14px}
.bub.me{align-self:flex-end;background:var(--ch);color:var(--kem);border-radius:22px 22px 6px 22px}
.rules{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px}
.rules div{border-top:2px solid var(--den);padding-top:12px;font-size:15px;color:var(--xam)}
.rules b{display:block;color:var(--den);font-weight:800;font-size:18px;margin-bottom:4px}
footer{background:var(--den);color:var(--kem);padding-block:64px 44px}
footer .w{display:grid;grid-template-columns:1fr auto;gap:40px;align-items:end}
footer .big{font:800 96px/.9 var(--f);letter-spacing:-.06em}
footer p{font-size:13px;opacity:.7;margin-top:18px;max-width:64ch}
footer .ct{font:800 20px/1.6 var(--f);text-align:right}
@media (max-width:900px){.w{padding-inline:18px}section{padding-block:64px}.hero .sub,.traits,.rules{grid-template-columns:1fr}
 .u7,.u5,.u4,.u8,.u6{grid-column:1/-1}.trait .z{font-size:140px}.tester textarea{font-size:44px}footer .w{grid-template-columns:1fr}footer .ct{text-align:left}}
"""

JS = """
<script>
(function(){
 const ta=document.getElementById('thu'),sz=document.getElementById('co');
 const set=(k,v)=>{try{localStorage.setItem(k,v)}catch(e){}};
 const get=k=>{try{return localStorage.getItem(k)}catch(e){return null}};
 const v=get('ats-text');if(v)ta.value=v;
 ta.addEventListener('input',()=>set('ats-text',ta.value));
 sz.addEventListener('input',()=>{ta.style.fontSize=sz.value+'px';document.getElementById('cov').textContent=sz.value+' px'});
 document.querySelectorAll('[data-w]').forEach(b=>b.addEventListener('click',()=>{
   document.querySelectorAll('[data-w]').forEach(x=>x.setAttribute('aria-pressed','false'));
   b.setAttribute('aria-pressed','true');ta.style.fontWeight=b.dataset.w}));
})();
</script>"""


def page():
    return f"""<title>An Tâm Sans</title>
<style>{faces()}
{CSS}</style>
<header class="hero"><div class="w">
 <div class="top"><span>AN TÂM SANS</span><span>FONT THƯƠNG HIỆU · 2 ĐỘ ĐẬM</span></div>
 <div class="big">an t<span>â</span>m</div>
 <div class="sub"><div><b>Font riêng của Ẩm Thực An Tâm</b>Gõ được trên máy tính như font bình thường: Word, Canva, PowerPoint. Đủ dấu tiếng Việt. Mọi dấu mũ là chiếc bánh.</div>
 <div><b>Hai độ đậm</b>Đậm (ExtraBold) cho tên, tiêu đề, biển hiệu. Thường (Regular) cho nội dung, menu, tin nhắn.</div></div>
</div></header>

<section><div class="w">
 <span class="lab"><i></i>Nét riêng</span>
 <h2>Hai dấu hiệu <span>chỉ An Tâm có</span></h2>
 <p class="lead">Hai chi tiết lặp lại ở mọi chữ, nên dù viết câu nào cũng nhận ra chữ của An Tâm.</p>
 <div class="traits">
  <div class="trait"><div class="z">âêô</div><b>Mũ bánh</b><p>Mọi dấu mũ trong tiếng Việt (â, ê, ô, ấ, ầ, ẩ, ẫ, ậ, ế, ố…) là chiếc bánh tortilla gập đôi có ba đốm nướng. Tiếng Việt có rất nhiều dấu mũ, nên đoạn văn nào cũng có bánh.</p></div>
  <div class="trait"><div class="z">ndl</div><b>Nhát dao</b><p>Góc trên bên trái mỗi chữ cắt chéo, góc dưới bên phải khía một vết nhỏ, như nhát dao thái thịt doner. Nhìn gần thấy sắc, nhìn xa vẫn tròn và thân thiện.</p></div>
 </div>
</div></section>

<section style="background:#fff"><div class="w">
 <span class="lab"><i></i>Bộ chữ</span>
 <h2>Đủ chữ, <span>đủ dấu</span></h2>
 <div class="set">
  <div>ABCDEFGHIJKLMNOPQRSTUVWXYZ</div>
  <div>abcdefghijklmnopqrstuvwxyz</div>
  <div class="vn">ĂÂĐÊÔƠƯ ăâđêôơư ấầẩẫậ ắằẳẵặ ếềểễệ ốồổỗộ ớờởỡợ ứừửữự</div>
  <div class="r">0123456789 · & ! ? , . : ; ( ) % đ ₫</div>
 </div>
</div></section>

<section><div class="w">
 <span class="lab"><i></i>Gõ thử</span>
 <h2>Gõ câu <span>của anh chị</span></h2>
 <div class="tester">
  <div class="ctl"><button type="button" data-w="800" aria-pressed="true">Đậm</button><button type="button" data-w="400" aria-pressed="false">Thường</button>
   <label for="co">Cỡ chữ</label><input id="co" type="range" min="24" max="140" value="72"><span id="cov">72 px</span></div>
  <textarea id="thu" spellcheck="false" aria-label="Gõ thử font An Tâm Sans">Bánh nóng mỗi sáng, ăn là an tâm.</textarea>
 </div>
</div></section>

<section style="background:#fff"><div class="w">
 <span class="lab"><i></i>Ứng dụng</span>
 <h2>Font trên <span>mọi ấn phẩm</span></h2>
 <div class="uses">
  <div class="use u7 poster"><span class="cap">Poster</span><img src="{ill('doner-cuon')}" alt=""><h3>cuộn chặt,<br><span>ăn an tâm.</span></h3></div>
  <div class="use u5 menu"><span class="cap">Thực đơn</span><h3>thực đơn</h3>
   <ul><li>Bánh tortillas<i></i><em>[giá]</em></li><li>Taco gập đôi<i></i><em>[giá]</em></li><li>Doner kebab<i></i><em>[giá]</em></li><li>Doner cuộn<i></i><em>[giá]</em></li></ul></div>
  <div class="use u5 pack"><span class="cap">Bao bì</span><div class="box"><b>an tâm</b><span>BÁNH TORTILLAS</span><small>[Cần điền: khối lượng, hạn dùng]</small></div></div>
  <div class="use u7 chat"><span class="cap">Tin nhắn Zalo</span>
   <div class="bub me">Cho mình 30 phần doner cuộn lúc 15h nhé.</div>
   <div class="bub">Dạ An Tâm đã nhận đơn ạ. Bánh nóng sẽ tới văn phòng anh chị đúng giờ.</div>
   <div class="bub me">Cảm ơn, ăn là an tâm!</div></div>
 </div>
 <div class="rules">
  <div><b>Logo vẫn là file vẽ</b>Logo "an tâm" dùng file SVG đã chốt. Font dùng cho mọi chữ còn lại.</div>
  <div><b>Đậm cho tiêu đề</b>Chữ thường, khít chữ −3 đến −6%. Không viết hoa cả đoạn dài.</div>
  <div><b>Thường cho nội dung</b>Từ 14 px trở lên. Giãn dòng 1,5.</div>
 </div>
</div></section>

<footer><div class="w"><div><div class="big">an tâm sans</div>
<p>Font dựng từ Lexend (giấy phép SIL Open Font License 1.1), đổi tên và thêm nét riêng. Được dùng tự do cho thương mại, không được bán lại font riêng lẻ. File cài đặt: AnTamSans-ExtraBold.ttf, AnTamSans-Regular.ttf.</p></div>
<div class="ct">0348.635.222<br>antamfoods.com</div></div></footer>
{JS}
"""


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())
