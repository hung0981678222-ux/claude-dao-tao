const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const src=process.argv[2],dst=process.argv[3];fs.mkdirSync(dst,{recursive:true});
for(const f of fs.readdirSync(src).filter(f=>f.endsWith('.svg'))){const s=fs.readFileSync(src+'/'+f,'utf8');const m=s.match(/viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"/);
const r=m[3]/m[4];const W=r>=1?2000:Math.round(2000*r),H=r>=1?Math.round(2000/r):2000;
await p.setViewportSize({width:W,height:H});await p.setContent('<style>html,body{margin:0;background:transparent}body>svg{display:block;width:'+W+'px;height:'+H+'px}</style>'+s);
await p.screenshot({path:dst+'/'+f.replace('.svg','.png'),omitBackground:true});console.log(f,W,H)}await b.close()})();
