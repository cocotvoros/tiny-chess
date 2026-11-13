import json,os
from urllib.request import*
U=os.getenv("MAKEFUN_ENV_URL")
V=(0,100,320,330,500,900,20000)
N=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
B=[(-1,-1),(-1,1),(1,-1),(1,1)];R=[(-1,0),(1,0),(0,-1),(0,1)];G=B+R;Q='abcdefgh'
Y=[0];Z=12000
X=Exception
def P(f):
 a=f.split();b=[0]*64;r=7
 for w in a[0].split('/'):
  x=0
  for c in w:
   if c.isdigit():x+=int(c)
   else:b[r*8+x]=('pnbrqk'.index(c.lower())+1)*(1 if c.isupper() else -1);x+=1
  r-=1
 s=1 if a[1]=='w' else -1;c=sum(1<<i for i,k in enumerate('KQkq')if k in a[2])
 return b,s,c,-1 if a[3]=='-' else Q.index(a[3][0])+(int(a[3][1])-1)*8
def A(b,q,w):
 f,r=q%8,q//8;d=-1 if w>0 else 1
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
     if p==w*t or p==w*5:return 1
     break
    x+=df;y+=dr
 return 0
def M(b,f,t,p,s,c,e):
 n=b[:];v=n[f];n[f]=0;n[t]=p*s if p else v
 if abs(v)==1 and t==e:n[t-8*s]=0
 if abs(v)==6 and abs(t-f)==2:
  a,z=(t+1,t-1)if t>f else(t-2,t+1);n[a]=0;n[z]=s*4
 for k,m in((4,3),(60,12),(7,1),(0,2),(63,4),(56,8)):
  if f==k or t==k:c&=~m
 return n,c,(f+t)//2 if abs(v)==1 and abs(t-f)==16 else -1
def L(b,s,c,e):
 m=[]
 for i,p in enumerate(b):
  if p*s<=0:continue
  f,r=i%8,i//8;t=abs(p)
  if t==1:
   d=8*s;y=r+s
   if 0<=y<8:
    j=i+d
    if not b[j]:
     if y in(0,7):m+=[(i,j,5),(i,j,2)]
     else:
      m.append((i,j,0))
      if r==(1 if s>0 else 6) and not b[j+d]:m.append((i,j+d,0))
    for df in(-1,1):
     x=f+df
     if 0<=x<8:
      j=i+d+df
      if b[j]*s<0 or j==e:
       if y in(0,7):m+=[(i,j,5),(i,j,2)]
       else:m.append((i,j,0))
  else:
   ds=N if t==2 else G if t>4 else B if t==3 else R
   for df,dr in ds:
    x,y=f+df,r+dr
    while 0<=x<8 and 0<=y<8:
     j=y*8+x
     if b[j]*s>0:break
     m.append((i,j,0))
     if b[j] or t in(2,6):break
     x+=df;y+=dr
 for k,ro,es,ks,t,bit in((4,7,(5,6),(4,5,6),6,1),(4,0,(1,2,3),(4,3,2),2,2),(60,63,(61,62),(60,61,62),62,4),(60,56,(57,58,59),(60,59,58),58,8)):
  if (s>0)==(k<32) and c&bit and b[k]==s*6 and b[ro]==s*4 and not any(b[x] for x in es) and not any(A(b,x,-s) for x in ks):m.append((k,t,0))
 o=[]
 for f,t,p in m:
  if abs(b[t])==6:continue
  n,_,_=M(b,f,t,p,s,c,e);k=[i for i,x in enumerate(n) if x==s*6]
  if k and not A(n,k[0],-s):o.append((f,t,p))
 return o
def E(b):
 s=0
 for i,p in enumerate(b):
  if p:
   a=abs(p);v=V[a];f=i%8;r=i//8
   if p<0:r=7-r
   v+=r*8+5-abs(f-3) if a==1 else (12-(abs(f-3)+abs(r-3))*4) if a==2 else 6 if a==3 else (2-r)*6
   s+=v if p>0 else -v
 return s
def O(b,m):return 900+V[m[2]] if m[2] else V[abs(b[m[1]])]*10-V[abs(b[m[0]])]
def S(b,s,c,e,d,a,be,pl):
 Y[0]+=1
 if Y[0]>Z:raise X
 k0=[i for i,x in enumerate(b) if x==s*6][0]
 if d<=0:
  v=E(b)*s
  if v>=be:return be
  if v>a:a=v
  ms=L(b,s,c,e)
  if not ms:return -20000+pl if A(b,k0,-s) else 0
  if not A(b,k0,-s):ms=[m for m in ms if b[m[1]] or m[1]==e or m[2]]
  if not ms:return a
 else:
  ms=L(b,s,c,e)
  if not ms:return -20000+pl if A(b,k0,-s) else 0
 ms.sort(key=lambda m:-O(b,m));best=-30000
 for m in ms:
  n,c2,e2=M(b,m[0],m[1],m[2],s,c,e);x=-S(n,-s,c2,e2,d-1,-be,-a,pl+1)
  if x>best:best=x
  if best>a:a=best
  if a>=be:break
 return best
def W(m):return f'{Q[m[0]%8]}{m[0]//8+1}{Q[m[1]%8]}{m[1]//8+1}'+('qn'[m[2]==2] if m[2] else '')
def C(f,legal):
 b,s,c,e=P(f);ms=L(b,s,c,e)
 if not ms:return legal[0]
 ms=[m for m in ms if W(m) in legal] or ms
 best=ms[0];Y[0]=0
 for d in range(1,6):
  try:
   cur=None;bv=-30000;a=-30000
   for m in sorted(ms,key=lambda m:-O(b,m)):
    n,c2,e2=M(b,m[0],m[1],m[2],s,c,e);x=-S(n,-s,c2,e2,d-1,-30000,-a,1)
    if x>bv:bv=x;cur=m
    if x>a:a=x
   best=cur
  except X:break
 return W(best)
def h(p,y):
 q=Request(U+p,json.dumps(y).encode())
 with urlopen(q) as z:return json.load(z)
if U:
 while True:
  g=h('/game',{})
  if g['status']=='done':break
  while g['status']=='your_move':g=h('/move',{'game':g['game'],'move':C(g['fen'],g['legal_moves'])})
