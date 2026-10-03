// Chụp PNG 1080x1350 từ các mẫu HTML. Chạy: cd mau && node chup.js
const {chromium}=require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs'),path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const f of fs.readdirSync(__dirname).filter(x=>/^[a-z]-.*\.html$/.test(x))){
 await p.goto('file://'+path.join(__dirname,f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 const n=f.replace('.html','.png');await p.locator('#s').screenshot({path:path.join(__dirname,n)});
 const r=await p.evaluate(()=>{const s=document.getElementById('s').getBoundingClientRect();
  const fonts=['400','600','800'].map(w=>document.fonts.check(w+' 20px "An Tam Tron Banh"'));
  const imgs=[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src);
  const bad=[...document.querySelectorAll('#s *')].filter(e=>{if(!e.children.length&&!e.textContent.trim())return false;const c=e.getBoundingClientRect();return c.right>s.right-60||c.bottom>s.bottom||c.left<s.left+60&&e.tagName!=='DIV'&&false||(e.scrollWidth>e.clientWidth+2&&getComputedStyle(e).display!=='inline')}).map(e=>e.className+'|'+e.textContent.slice(0,25));
  return {fonts,imgs,bad}});
 console.log(n,JSON.stringify(r));}
await b.close()})();
