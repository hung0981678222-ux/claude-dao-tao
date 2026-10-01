"""Trang font An Tâm Sans, bản có 4 kiểu (Đậm, Thường, Nét Đứt, Đốm Nướng). Chạy: python3 build_font_page2.py OUT.html"""
import os
import sys

import build_font_page as P

HERE = P.HERE
ND, DN = "'An Tam Sans Net Dut'", "'An Tam Sans Dom Nuong'"


def faces2():
    return (f"@font-face{{font-family:{ND};font-display:swap;src:url({P.b64(os.path.join(HERE, 'AnTamSans-NetDut.woff2'), 'font/woff2')}) format('woff2')}}\n"
            f"@font-face{{font-family:{DN};font-display:swap;src:url({P.b64(os.path.join(HERE, 'AnTamSans-DomNuong.woff2'), 'font/woff2')}) format('woff2')}}")


CSS2 = f"""
.fam{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:48px}}
.fm{{border-radius:32px;padding:34px;display:flex;flex-direction:column;gap:10px;min-height:340px}}
.fm .s{{font-size:clamp(84px,10vw,150px);line-height:.95;letter-spacing:-.04em}}
.fm .t{{font-size:32px;line-height:1.2;margin-top:auto}}
.fm b{{font:800 14px/1 var(--f);letter-spacing:.14em;text-transform:uppercase;opacity:.75}}
.fm p{{font-size:14px;opacity:.85}}
.f-nd{{font-family:{ND},var(--f)}}.f-dn{{font-family:{DN},var(--f)}}
.zoomrow{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}}
.zoomrow div{{border-radius:32px;background:#fff;border:1px solid var(--line);display:grid;place-items:center;overflow:hidden;height:300px}}
.zoomrow span{{font-size:420px;line-height:.8;color:var(--ch)}}
@media (max-width:900px){{.fam,.zoomrow{{grid-template-columns:1fr}}.zoomrow span{{font-size:300px}}}}
"""


def page():
    h = P.page()
    h = h.replace("</style>", faces2() + CSS2 + "</style>", 1)
    fam = f"""<section style="background:#fff"><div class="w">
 <span class="lab"><i></i>Họ font · 4 kiểu</span>
 <h2>Thêm <span>nét đứt</span> và <span>đốm nướng</span></h2>
 <p class="lead">Hai kiểu hoạ tiết mới gõ được như font thường. Dùng cho chữ lớn: tiêu đề, bao bì, biển hiệu, từ 40 px trở lên. Chữ nhỏ dùng kiểu Đậm hoặc Thường.</p>
 <div class="fam">
  <div class="fm" style="background:var(--ch);color:var(--kem)"><b>Đậm · ExtraBold</b><div class="s" style="font-weight:800">an tâm</div><div class="t" style="font-weight:800">Bánh nóng mỗi sáng</div><p>Tên, tiêu đề, biển hiệu.</p></div>
  <div class="fm" style="background:var(--kem);border:1px solid var(--line)"><b>Thường · Regular</b><div class="s" style="font-weight:400">an tâm</div><div class="t" style="font-weight:400">Bánh nóng mỗi sáng</div><p>Nội dung, menu, tin nhắn.</p></div>
  <div class="fm f-nd" style="background:var(--bo)"><b style="font-family:var(--f)">Nét Đứt · Stitch</b><div class="s" style="color:var(--ch)">an tâm</div><div class="t">Bánh nóng mỗi sáng</div><p style="font-family:var(--f)">Đường chỉ khâu đứt quãng trong lòng nét, như đường may trên túi bánh, đường cắt trên tem.</p></div>
  <div class="fm f-dn" style="background:var(--den);color:var(--kem)"><b style="font-family:var(--f)">Đốm Nướng · Toast</b><div class="s" style="color:var(--bo)">an tâm</div><div class="t">Bánh nóng mỗi sáng</div><p style="font-family:var(--f)">Đốm cháy trong lòng chữ như mặt bánh tortilla vừa nướng trên chảo.</p></div>
 </div>
 <div class="zoomrow"><div><span class="f-nd">â</span></div><div><span class="f-dn">â</span></div></div>
</div></section>"""
    h = h.replace('<section style="background:#fff"><div class="w">\n <span class="lab"><i></i>Bộ chữ</span>', fam + '\n<section style="background:#fff"><div class="w">\n <span class="lab"><i></i>Bộ chữ</span>', 1)
    # nút chọn kiểu trong ô gõ thử
    h = h.replace('<button type="button" data-w="400" aria-pressed="false">Thường</button>',
                  '<button type="button" data-w="400" aria-pressed="false">Thường</button><button type="button" data-fam="nd" aria-pressed="false">Nét Đứt</button><button type="button" data-fam="dn" aria-pressed="false">Đốm Nướng</button>')
    h = h.replace("""   b.setAttribute('aria-pressed','true');ta.style.fontWeight=b.dataset.w}));""",
                  """   b.setAttribute('aria-pressed','true');ta.style.fontWeight=b.dataset.w;ta.style.fontFamily=''}));
 document.querySelectorAll('[data-fam]').forEach(b=>b.addEventListener('click',()=>{
   document.querySelectorAll('[data-w],[data-fam]').forEach(x=>x.setAttribute('aria-pressed','false'));
   b.setAttribute('aria-pressed','true');ta.style.fontFamily=b.dataset.fam==='nd'?"'An Tam Sans Net Dut'":"'An Tam Sans Dom Nuong'";ta.style.fontWeight='400'}));""")
    h = h.replace("document.querySelectorAll('[data-w]').forEach(x=>x.setAttribute('aria-pressed','false'));",
                  "document.querySelectorAll('[data-w],[data-fam]').forEach(x=>x.setAttribute('aria-pressed','false'));", 1)
    # ứng dụng: poster dùng Nét Đứt, bao bì dùng Đốm Nướng
    h = h.replace('<h3>cuộn chặt,<br><span>ăn an tâm.</span></h3>', f'<h3 style="font-family:{ND};font-weight:400">cuộn chặt,<br><span>ăn an tâm.</span></h3>')
    h = h.replace('<div class="box"><b>an tâm</b>', f'<div class="box"><b style="font-family:{DN};font-weight:400">an tâm</b>')
    h = h.replace('<div class="big">an t<span>â</span>m</div>', '<div class="big">an t<span class="f-dn" style="font-weight:400">â</span>m</div>')
    h = h.replace("FONT THƯƠNG HIỆU · 2 ĐỘ ĐẬM", "FONT THƯƠNG HIỆU · 4 KIỂU")
    h = h.replace("File cài đặt: AnTamSans-ExtraBold.ttf, AnTamSans-Regular.ttf.", "File cài đặt: AnTamSans-ExtraBold.ttf, AnTamSans-Regular.ttf, AnTamSans-NetDut.ttf, AnTamSans-DomNuong.ttf.")
    return h


if __name__ == "__main__":
    open(sys.argv[1], "w").write(page())
