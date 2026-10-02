const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const d=process.cwd()+'/'+(process.argv[2]||'fp2')+'/';
for(const f of fs.readdirSync(d).filter(f=>f.endsWith('.svg'))){const s=fs.readFileSync(d+f,'utf8');const m=s.match(/viewBox="0 0 (\d+) (\d+)"/);
await p.setViewportSize({width:+m[1],height:+m[2]});await p.setContent('<style>html,body{background:transparent;margin:0}body>svg{display:block}</style>'+s);
await p.screenshot({path:d+f.replace('.svg','.png'),omitBackground:true})}
await b.close()})();
