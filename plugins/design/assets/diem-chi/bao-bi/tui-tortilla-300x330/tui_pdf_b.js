const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();const d=process.cwd()+'/tui-out/';
const pages=['tui-an-tam-mat-truoc','tui-an-tam-mat-sau'].map(n=>'<div class="pg">'+fs.readFileSync(d+n+'.svg','utf8')+'</div>').join('');
await p.setContent('<style>@page{size:306mm 336mm;margin:0}*{margin:0}.pg{width:306mm;height:336mm;page-break-after:always;overflow:hidden}.pg svg{display:block}</style>'+pages);
await p.pdf({path:d+'tui-an-tam-300x330-in.pdf',width:'306mm',height:'336mm',printBackground:true,preferCSSPageSize:true});
for(const [n,w] of [['mockup-an-tam',2280],['tui-an-tam-mat-truoc',1836]]){const s=fs.readFileSync(d+n+'.svg','utf8');const m=s.match(/viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"/);const h=Math.round(w*m[4]/m[3]);
await p.setViewportSize({width:w,height:h});await p.setContent('<style>*{margin:0}body>svg{display:block;width:'+w+'px;height:'+h+'px}</style>'+s);await p.screenshot({path:d+n+'.png'})}
await b.close()})();
