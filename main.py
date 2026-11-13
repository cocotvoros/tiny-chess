import json,os
from urllib.request import*
U=os.getenv("MAKEFUN_ENV_URL")
V=(0,100,320,330,500,900,0)
N=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
B=[(-1,-1),(-1,1),(1,-1),(1,1)];R=[(-1,0),(1,0),(0,-1),(0,1)];G=B+R;Q='abcdefgh'
Y=[0];Z=25000;H=[0]
X=Exception
def P(f):
 a=f.split();b=[0]*64;r=7
 for w in a[0].split('/'):
  x=0
  for c in w:
   if c>'9':b[r*8+x]=('pnbrqk'.index(c.lower())+1)*((c<'a')*2-1);x+=1
   else:x+=int(c)
  r-=1
 s=(a[1]=='w')*2-1;c=sum(1<<i for i,k in enumerate('KQkq')if k in a[2])
 return b,s,c,-1 if a[3]=='-' else ord(a[3][0])+8*int(a[3][1])-105
def F(b,s):return b.index(s*6)
def A(b,q,w):
 f,r=q%8,q//8;d=-w
 for z,t in((((-1,d),(1,d)),1),(N,2),(G,6)):
  for df,dr in z:
   x,y=f+df,r+dr
   if 0<=x<8 and 0<=y<8 and b[y*8+x]==w*t:return 1
 for z,t in((B,3),(R,4)):
  for df,dr in z:
   x,y=f+df,r+dr
   while 0<=x<8 and 0<=y<8:
    p=b[y*8+x]
    if p:
     if p in(w*t,w*5):return 1
     break
    x+=df;y+=dr
 return 0
def T(p,i):
 a=abs(p);f=i%8;r=i//8
 if p<0:r=7-r
 return (V[a]+(r*3,12-2*abs(f-3)-2*abs(r-3),0,6*(r==6),4-abs(f-3),12-6*r)[a-1])*p//abs(p)
def M(b,f,t,p,s,c,e):
 v=b[f];w=p*s if p else v;cs=t-8*s if abs(v)==1 and t==e else t;q=b[cs]
 d=T(w,t)-T(v,f)
 if q:d-=T(q,cs)
 b[f]=0;b[t]=w
 if cs!=t:b[cs]=0
 a=z=0
 if abs(v)==6 and abs(t-f)==2:a,z=(t+1,t-1)if t>f else(t-2,t+1);b[a]=0;b[z]=s*4;d+=T(s*4,z)-T(s*4,a)
 for k,m in((4,3),(60,12),(7,1),(0,2),(63,4),(56,8)):
  if k in(f,t):c&=~m
 H[0]+=d
 return (v,q,cs,d,a,z),c,(f+t)//2 if abs(v)==1 and abs(t-f)==16 else -1
def D(b,f,t,u):
 v,q,cs,d,a,z=u;H[0]-=d;b[f]=v;b[t]=0;b[cs]=q
 if z:b[a]=4*v//abs(v);b[z]=0
def L(b,s,c,e,q=0):
 m=[]
 for i,p in enumerate(b):
  if p*s<=0:continue
  f,r=i%8,i//8;t=abs(p)
  if t==1:
   d=8*s;y=r+s
   if 0<=y<8:
    for df in(0,-1,1):
     x=f+df;j=i+d+df
     if 0<=x<8 and (not b[j] if df==0 else b[j]*s<0 or j==e):
      if y in(0,7):m+=[(i,j,5),(i,j,2)]
      else:
       if not q or df:m.append((i,j,0))
       if not q and not df and r==(1 if s>0 else 6) and not b[j+d]:m.append((i,j+d,0))
  else:
   ds=N if t==2 else G if t>4 else B if t==3 else R
   for df,dr in ds:
    x,y=f+df,r+dr
    while 0<=x<8 and 0<=y<8:
     j=y*8+x
     if b[j]*s>0:break
     if b[j] or not q:m.append((i,j,0))
     if b[j] or t in(2,6):break
     x+=df;y+=dr
 if not q:
  for k,d,bit in((4,1,1),(4,-1,2),(60,1,4),(60,-1,8)):
   ro=k+3*d-(d<0);es=(k+d,k+2*d,k+3*d)[:2+(d<0)];ks=(k,k+d,k+2*d)
   if (s>0)==(k<32) and c&bit and b[k]==s*6 and b[ro]==s*4 and not any(b[x] for x in es) and not any(A(b,x,-s) for x in ks):m.append((k,k+2*d,0))
 o=[]
 for f,t,p in m:
  if abs(b[t])==6:continue
  u,_,_=M(b,f,t,p,s,c,e)
  if not A(b,F(b,s),-s):o.append((f,t,p))
  D(b,f,t,u)
 return o
def O(b,m):return 900+V[m[2]] if m[2] else V[abs(b[m[1]])]*10-V[abs(b[m[0]])]
def E(b,m,s,c,e,d,a,be,pl):
 f,t,p=m;u,c2,e2=M(b,f,t,p,s,c,e);x=-S(b,-s,c2,e2,d-1,-be,-a,pl+1);D(b,f,t,u);return x
def S(b,s,c,e,d,a,be,pl):
 Y[0]+=1
 if Y[0]>Z:raise X
 k0=F(b,s)
 if d<=0:
  if d<=-8:return H[0]*s
  v=H[0]*s
  if v>=be:return be
  if v>a:a=v
  ic=A(b,k0,-s);ms=L(b,s,c,e,not ic)
  if ic and not ms:return -20000+pl
 else:
  ic=1;ms=L(b,s,c,e,0)
  if not ms:return -20000+pl if A(b,k0,-s) else 0
 ms.sort(key=lambda m:-O(b,m));best=-30000
 for m in ms:
  x=E(b,m,s,c,e,d,a,be,pl)
  if x>best:best=x
  if best>a:a=best
  if a>=be:break
 return best if ic else max(a,best)
def W(m):return f'{Q[m[0]%8]}{m[0]//8+1}{Q[m[1]%8]}{m[1]//8+1}'+('qn'[m[2]==2] if m[2] else '')
def C(f,legal):
 b,s,c,e=P(f);H[0]=sum(T(p,i) for i,p in enumerate(b) if p);ms=L(b,s,c,e)
 ms=[m for m in ms if W(m) in legal] or ms
 best=ms[0]
 for d in range(1,7):
  Y[0]=0
  try:
   cur=None;bv=a=-30000
   for m in sorted(ms,key=lambda m:-O(b,m)):
    x=E(b,m,s,c,e,d-1,a,30000,1)
    if x>bv:bv=x;cur=m
    if x>a:a=x
   best=cur
  except X:break
 return W(best)
def h(p,y):
 with urlopen(Request(U+p,json.dumps(y).encode())) as z:return json.load(z)
while U:
 g=h('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':g=h('/move',{'game':g['game'],'move':C(g['fen'],g['legal_moves'])})
