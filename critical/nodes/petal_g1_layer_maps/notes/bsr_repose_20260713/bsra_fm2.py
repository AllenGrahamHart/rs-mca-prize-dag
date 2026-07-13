#!/usr/bin/env python3
"""FM2 (repaired): synthesized band charts with m' = d'+2 at (32,16,193,consec).
Relaxed (deg <= k') member count must exceed 1 on some chart (margin exactly 1);
UNRELAXED (deg <= k'-1) member count must be <= 1 on EVERY chart (U0 in vivo)."""
import itertools
from math import comb

def order_n_domain(p,n):
    a=2
    while True:
        g0=pow(a,(p-1)//n,p)
        if pow(g0,n//2,p)!=1: break
        a+=1
    return [pow(g0,j,p) for j in range(n)]
def locator(roots,p):
    loc=[1]
    for r in roots:
        new=[0]*(len(loc)+1)
        for i,c in enumerate(loc):
            new[i]=(new[i]-r*c)%p; new[i+1]=(new[i+1]+c)%p
        loc=new
    return loc
def ev(poly,x,p):
    v=0
    for c in reversed(poly): v=(v*x+c)%p
    return v
def interpolate(xs,ys,k,p):
    poly=[0]*k
    for i in range(k):
        num=[1]; den=1; xi=xs[i]
        for j in range(k):
            if j==i: continue
            r=xs[j]; new=[0]*(len(num)+1)
            for d2,c in enumerate(num):
                new[d2]=(new[d2]-r*c)%p; new[d2+1]=(new[d2+1]+c)%p
            num=new; den=den*(xi-r)%p
        coef=ys[i]*pow(den,-1,p)%p
        for d2,c in enumerate(num):
            poly[d2]=(poly[d2]+coef*c)%p
    return tuple(poly)

n,k,p,smode = 32,16,193,"consec"
dom=order_n_domain(p,n); half=n//2; npr,kpr=half,k//2; nf=kpr-1
core=[]
for j in range(nf): core+=[j,j+half]
core.append(nf)
petals=[[j,j+half] for j in range(nf+1,half)]
scal=[(i+1)%p for i in range(len(petals))]
loc=locator([dom[j] for j in core],p)
values=[0]*n
for c_i,P in zip(scal,petals):
    for j in P: values[j]=c_i*ev(loc,dom[j],p)%p
domq=[dom[j]*dom[j]%p for j in range(npr)]
ynf=domq[nf]; locq=locator(domq[:nf],p)
u1=[0]*npr
for i,j in enumerate(range(nf+1,npr)):
    u1[j]=scal[i]*ev(locq,domq[j],p)%p

corepts=list(range(kpr))          # core'' indices (y_nf = index nf = k'-1)
petalpts=list(range(kpr,npr))     # petal-point indices
relax_trip=0; unrelax_bad=0; scanned=0
for z in (kpr-2, kpr-3):          # d' = 2 or 3; m' = d'+2 = 4 or 5
    dpr=kpr-z; mpr=dpr+2
    for Wrest in itertools.combinations([c for c in corepts if c!=nf], z-1):
        W=sorted((nf,)+Wrest)
        locW=locator([domq[j] for j in W],p)
        for P in itertools.combinations(petalpts, mpr):
            scanned+=1
            rel=set(); unrel=set()
            # relaxed: g = L_W*h, deg h <= d'  (deg g <= k')
            for sub in itertools.combinations(P,dpr+1):
                xs=[domq[j] for j in sub]
                ys=[u1[j]*pow(ev(locW,domq[j],p),-1,p)%p for j in sub]
                h=interpolate(xs,ys,dpr+1,p)
                nag=sum(1 for j in P if ev(h,domq[j],p)*ev(locW,domq[j],p)%p==u1[j])
                if nag>=dpr+1: rel.add(h)
            # unrelaxed: deg h <= d'-1 (deg g <= k'-1), members need >= d'+1 agr
            for sub in itertools.combinations(P,dpr):
                xs=[domq[j] for j in sub]
                ys=[u1[j]*pow(ev(locW,domq[j],p),-1,p)%p for j in sub]
                h=interpolate(xs,ys,dpr,p)
                nag=sum(1 for j in P if ev(h,domq[j],p)*ev(locW,domq[j],p)%p==u1[j])
                if nag>=dpr+1: unrel.add(h)
            if len(rel)>=2: relax_trip+=1
            if len(unrel)>1: unrelax_bad+=1
            if scanned>=4000: break
        if scanned>=4000: break
    if scanned>=4000: break
print(f"charts scanned {scanned}; relaxed >=2 members on {relax_trip}; "
      f"unrelaxed >1 member on {unrelax_bad}")
ok1 = relax_trip>0; ok2 = unrelax_bad==0
print(f"[{'PASS' if ok1 else 'FAIL'}] FM2 TRIPS: one-unit degree relaxation admits multi-member charts")
print(f"[{'PASS' if ok2 else 'FAIL'}] U0 in vivo: unrelaxed band charts hold <= 1 member on all scanned charts")
raise SystemExit(0 if (ok1 and ok2) else 1)
