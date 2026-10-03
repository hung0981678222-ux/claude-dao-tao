const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
const jobs={'a-carousel-ham-banh':['s1','s2','s3','s4','s5'],'b-the-cong-thuc-wrap-ga':['b'],'c-bai-ban-hang':['c']};
for(const [f,ids] of Object.entries(jobs)){await p.goto('file://'+process.cwd()+'/'+f+'.html');await p.waitForTimeout(300);
 for(const [i,id] of ids.entries()){const n=ids.length>1?`${f}-${i+1}.png`:`${f}.png`;await p.locator('#'+id).screenshot({path:n});
  const o=await p.evaluate(id=>{const s=document.getElementById(id);return [...s.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+2&&getComputedStyle(e).display!='inline').map(e=>e.className+':'+e.textContent.slice(0,20));},id);if(o.length)console.log(n,'overflow?',o);}}
await b.close()})();
