# Dựng bộ ảnh thay thế cho antamfoods.com (/client/images/) theo Điểm Chỉ v1.1.
# Sinh HTML -> render PNG bằng Playwright (render.js) -> nén bằng ImageMagick.
# Cách chạy: python3 dung_anh.py <thu_muc_anh_that>  (cần src_kho.jpg, src_kho2.jpg, src_cat.jpg, src_gia.jpg)
import os,sys,json,subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
DC=os.path.abspath(os.path.join(HERE,'..','..'))          # .../diem-chi
SRC=os.path.abspath(sys.argv[1]); WORK=os.path.join(SRC,'..','html'); os.makedirs(WORK,exist_ok=True)
U=lambda p:'file://'+p
FONT=''.join(f'@font-face{{font-family:T;src:url("{U(DC)}/font-an-tam-tron-banh/AnTamTronBanh-{n}.woff2");font-weight:{w}}}' for n,w in [('Regular',400),('SemiBold',600),('ExtraBold',800)])
BASE=f'<style>{FONT}*{{margin:0;padding:0;box-sizing:border-box}}html,body{{background:transparent;font-family:T}}</style>'
LOGO=U(DC+'/logo/logo-ngang.svg'); LOGO_DO=U(DC+'/logo/logo-ngang-nen-do.svg'); VAN=U(DC+'/hoa-tiet/nen-duong-van.svg')
jobs=[]
def page(name,w,h,body,transparent=False):
    p=os.path.join(WORK,name+'.html'); open(p,'w').write(f'<!doctype html><meta charset=utf-8>{BASE}<body style="width:{w}px;height:{h}px;overflow:hidden">{body}</body>')
    jobs.append(dict(html=p,w=w,h=h,out=os.path.join(WORK,name+'.png'),transparent=transparent))
# logo 780x155: logo ngang, trái, cao 155
page('logo',780,155,f'<img src="{LOGO}" style="height:155px;display:block">',True)
# phone 550x550: tròn đỏ + tay nghe kem
CALL='M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z'
page('phone-call-icon',550,550,f'<svg width="550" height="550" viewBox="0 0 550 550"><circle cx="275" cy="275" r="275" fill="#D2141E"/><g transform="translate(130 130) scale(12.1)"><path d="{CALL}" fill="#FFF6EA"/></g></svg>',True)
# icon
for n,s,f in [('favicon-16x16',16,'website/favicon.svg'),('favicon-32x32',32,'website/favicon.svg'),('favicon-48',48,'website/favicon.svg'),('apple-touch-icon',180,'website/app-icon.svg')]:
    page(n,s,s,f'<img src="{U(DC+"/"+f)}" style="width:{s}px;height:{s}px;display:block">',True)
# hero-food-banner 4000x2060: ảnh thật kho, không chữ (trang gốc đặt nút play / thẻ trắng lên ảnh)
page('hero-food-banner',4000,2060,f'<div style="width:4000px;height:2060px;background:url({U(SRC)}/src_kho.jpg) center 55%/cover"></div>')
# bìa video 1376x768: trái đỏ + chữ, phải ảnh thật; giữa trống cho nút play, góc dưới trái trống cho nhãn thời lượng
def bia(name,kick,t1,t2,img,pos):
    page(name,1376,768,f'''<div style="position:relative;width:1376px;height:768px;background:#D2141E;overflow:hidden">
<div style="position:absolute;inset:0;background:url({VAN}) center/900px;opacity:.10"></div>
<div style="position:absolute;right:0;top:0;width:640px;height:768px;background:url({U(SRC)}/{img}) {pos}/cover"></div>
<div style="position:absolute;right:16px;bottom:16px;background:#FFF6EA;color:#231716;font-weight:600;font-size:20px;padding:6px 16px;border-radius:99px">Ảnh thật tại xưởng An Tâm</div>
<img src="{LOGO_DO}" style="position:absolute;left:64px;top:56px;height:96px">
<div style="position:absolute;left:64px;top:208px;width:600px;color:#FFF6EA">
<div style="font-weight:600;font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:#F5B82E">{kick}</div>
<div style="font-weight:800;font-size:68px;line-height:1.1;margin-top:14px">{t1}</div>
<div style="font-weight:400;font-size:28px;line-height:1.4;margin-top:20px;opacity:.95;width:520px">{t2}</div></div></div>''')
bia('franchise-hero','Hợp tác &amp; nhượng quyền','Cùng An Tâm<br>mở quán','Tư vấn mô hình ki-ốt, cửa hàng – nguồn bánh ổn định mỗi ngày.','src_gia.jpg','center 45%')
bia('training-hero','Đào tạo nghề','Học làm bánh<br>từ A đến Z','Hướng dẫn vận hành, công thức và cách nướng bánh chuẩn vị.','src_cat.jpg','center 50%')
# delivery-truck 1750x1020: đồ hoạ giao hàng + ảnh thật kho đóng túi
page('delivery-truck',1750,1020,f'''<div style="position:relative;width:1750px;height:1020px;background:#FFF6EA;border-radius:64px;overflow:hidden">
<div style="position:absolute;left:0;top:0;width:900px;height:1020px;background:#D2141E"></div>
<div style="position:absolute;left:0;top:0;width:900px;height:1020px;background:url({VAN}) center/900px;opacity:.10"></div>
<img src="{LOGO_DO}" style="position:absolute;left:80px;top:72px;height:120px">
<div style="position:absolute;left:80px;top:270px;width:760px;color:#FFF6EA">
<div style="font-weight:600;font-size:34px;letter-spacing:.14em;color:#F5B82E">GIAO HOẢ TỐC</div>
<div style="font-weight:800;font-size:220px;line-height:.95">2H</div>
<div style="font-weight:600;font-size:46px;margin-top:18px">Gửi xe toàn quốc</div>
<div style="margin-top:56px;display:inline-block;background:#FFF6EA;color:#D2141E;border-radius:99px;padding:22px 44px">
<div style="font-weight:600;font-size:26px;letter-spacing:.12em;color:#231716">HOTLINE / ZALO</div>
<div style="font-weight:800;font-size:76px;line-height:1">0398 431 300</div></div></div>
<div style="position:absolute;left:960px;top:80px;width:710px;height:860px;border-radius:44px;background:url({U(SRC)}/src_kho2.jpg) 50% 50%/cover"></div>
<div style="position:absolute;left:990px;bottom:110px;background:#FFF6EA;color:#231716;font-weight:600;font-size:26px;padding:8px 22px;border-radius:99px">Ảnh thật tại kho An Tâm</div>
</div>''',True)
json.dump(jobs,open(os.path.join(WORK,'jobs.json'),'w'))
subprocess.run(['node',os.path.join(HERE,'render.js'),os.path.join(WORK,'jobs.json')],check=True,env=dict(os.environ,NODE_PATH=subprocess.check_output(['npm','root','-g'],text=True).strip()))
