const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const src=process.argv[2];
for(const f of fs.readdirSync(src).filter(f=>f.endsWith('.svg'))){const s=fs.readFileSync(src+'/'+f,'utf8');const m=s.match(/viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"/);
const W=Math.round(+m[3]),H=Math.round(+m[4]);await p.setViewportSize({width:W,height:H});
await p.setContent('<style>html,body{margin:0;background:transparent}body>svg{display:block;width:'+W+'px;height:'+H+'px}</style>'+s);await p.waitForTimeout(100);
await p.screenshot({path:src+'/'+f.replace('.svg','.png'),omitBackground:true})}await b.close()})();
