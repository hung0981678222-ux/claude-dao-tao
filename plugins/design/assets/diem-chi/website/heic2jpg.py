import struct,sys,os,subprocess,tempfile,shutil
def boxes(d,s,e):
    while s<e:
        sz,t=struct.unpack('>I4s',d[s:s+8]);h=8
        if sz==1: sz=struct.unpack('>Q',d[s+8:s+16])[0];h=16
        elif sz==0: sz=e-s
        yield t.decode('latin1'),s+h,s+sz; s+=sz
def find(d,s,e,t):
    for bt,a,b in boxes(d,s,e):
        if bt==t: return a,b
def rd(d,p,n):
    return 0 if n==0 else int.from_bytes(d[p:p+n],'big')
def convert(src,dst):
    d=open(src,'rb').read()
    ms,me=find(d,0,len(d),'meta'); ms+=4
    ps,_=find(d,ms,me,'pitm'); v=d[ps]; pitm=rd(d,ps+4,2 if v==0 else 4)
    # iinf
    s,e=find(d,ms,me,'iinf'); v=d[s]; p=s+4+(2 if v==0 else 4)
    types={}
    for bt,a,b in boxes(d,p,e):
        if bt!='infe': continue
        v=d[a]; q=a+4
        iid=rd(d,q,2 if v<3 else 4); q+=(2 if v<3 else 4)+2
        types[iid]=d[q:q+4].decode('latin1')
    # iloc
    s,e=find(d,ms,me,'iloc'); v=d[s]; p=s+4
    os_,ls=d[p]>>4,d[p]&15; bs,isz=d[p+1]>>4,(d[p+1]&15 if v in(1,2) else 0); p+=2
    n=rd(d,p,2 if v<2 else 4); p+=(2 if v<2 else 4); loc={}
    for _ in range(n):
        iid=rd(d,p,2 if v<2 else 4); p+=(2 if v<2 else 4)
        cm=0
        if v in(1,2): cm=rd(d,p,2)&15; p+=2
        p+=2; base=rd(d,p,bs); p+=bs
        ec=rd(d,p,2); p+=2; ex=[]
        for _ in range(ec):
            p+=isz; o=rd(d,p,os_); p+=os_; l=rd(d,p,ls); p+=ls; ex.append((base+o,l))
        loc[iid]=(cm,ex)
    idat=find(d,ms,me,'idat')
    def data(iid):
        cm,ex=loc[iid]; off=idat[0] if cm==1 else 0
        return b''.join(d[off+o:off+o+l] for o,l in ex)
    # iref
    refs={}
    r=find(d,ms,me,'iref')
    if r:
        v=d[r[0]]; w=2 if v==0 else 4
        for bt,a,b in boxes(d,r[0]+4,r[1]):
            fr=rd(d,a,w); c=rd(d,a+w,2); refs.setdefault(bt,{})[fr]=[rd(d,a+w+2+i*w,w) for i in range(c)]
    # iprp
    s,e=find(d,ms,me,'iprp'); cs,ce=find(d,s,e,'ipco')
    props=[(bt,a,b) for bt,a,b in boxes(d,cs,ce)]
    ps,pe=find(d,s,e,'ipma'); v=d[ps]; fl=rd(d,ps+1,3); p=ps+4
    cnt=rd(d,p,4); p+=4; assoc={}
    for _ in range(cnt):
        iid=rd(d,p,2 if v<1 else 4); p+=(2 if v<1 else 4); k=d[p]; p+=1; L=[]
        for _ in range(k):
            if fl&1: x=rd(d,p,2)&0x7fff; p+=2
            else: x=d[p]&0x7f; p+=1
            if x: L.append(props[x-1])
        assoc[iid]=L
    def prop(iid,t):
        for bt,a,b in assoc.get(iid,[]):
            if bt==t: return a,b
    def hevc(iid):
        a,b=prop(iid,'hvcC'); ln=(d[a+21]&3)+1; na=d[a+22]; q=a+23; out=b''
        for _ in range(na):
            q+=1; nn=rd(d,q,2); q+=2
            for _ in range(nn):
                l=rd(d,q,2); q+=2; out+=b'\0\0\0\1'+d[q:q+l]; q+=l
        x=data(iid); i=0
        while i<len(x):
            l=rd(x,i,ln); i+=ln; out+=b'\0\0\0\1'+x[i:i+l]; i+=l
        return out
    tmp=tempfile.mkdtemp()
    try:
        if types[pitm]=='grid':
            g=data(pitm); big=g[1]&1; R=g[2]+1; C=g[3]+1
            W=rd(g,4,4 if big else 2); H=rd(g,4+(4 if big else 2),4 if big else 2)
            tiles=refs['dimg'][pitm]
            for i,t in enumerate(tiles):
                open(f'{tmp}/t.hevc','wb').write(hevc(t))
                subprocess.run(['ffmpeg','-v','error','-y','-f','hevc','-i',f'{tmp}/t.hevc','-frames:v','1',f'{tmp}/t{i:03d}.png'],check=True)
            subprocess.run(['montage']+[f'{tmp}/t{i:03d}.png' for i in range(len(tiles))]+['-tile',f'{C}x{R}','-geometry','+0+0',f'{tmp}/m.png'],check=True)
            subprocess.run(['convert',f'{tmp}/m.png','-crop',f'{W}x{H}+0+0','+repage',f'{tmp}/f.png'],check=True)
        else:
            open(f'{tmp}/t.hevc','wb').write(hevc(pitm))
            subprocess.run(['ffmpeg','-v','error','-y','-f','hevc','-i',f'{tmp}/t.hevc','-frames:v','1',f'{tmp}/f.png'],check=True)
        ops=[]
        ir=prop(pitm,'irot')
        if ir: ang=d[ir[0]]&3; ops+=['-rotate',str(-90*ang)] if ang else []
        im=prop(pitm,'imir')
        if im: ops+=['-flop' if d[im[0]]&1 else '-flip']
        subprocess.run(['convert',f'{tmp}/f.png']+ops+['-quality','90',dst],check=True)
    finally: shutil.rmtree(tmp)
if __name__=='__main__':
    for s in sys.argv[1:]:
        out=os.path.splitext(s)[0]+'.jpg'
        try: convert(s,out); print('OK',out)
        except Exception as ex: print('LOI',s,repr(ex))
