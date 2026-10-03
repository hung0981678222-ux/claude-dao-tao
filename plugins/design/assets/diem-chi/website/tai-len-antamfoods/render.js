const {chromium}=require('playwright');const jobs=require(process.argv[2]);
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});
for(const j of jobs){const p=await b.newPage({viewport:{width:j.w,height:j.h}});await p.goto('file://'+j.html);
await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
await p.screenshot({path:j.out,omitBackground:!!j.transparent,clip:{x:0,y:0,width:j.w,height:j.h}});await p.close();console.log('OK',j.out)}
await b.close()})()
