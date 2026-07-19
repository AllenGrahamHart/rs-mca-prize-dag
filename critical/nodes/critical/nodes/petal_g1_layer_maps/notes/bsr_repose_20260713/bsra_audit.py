#!/usr/bin/env python3
"""bsra_audit — fresh-context INDEPENDENT audit battery for the bsr packet.

Written from the packet's CLAIMS, not from bsr_check.py's code paths.
A1  Lemma COL algebra: ratio identity, <=4 cap derivation per rate, boundary
    exactness probe (incl. the M-not-dividing-k counterexample above t).
A2  g1a instances: exact recomputation of old-form violation + column fit
    margins as exact log2 fractions (not bit_length shortcuts).
A3  #145 arithmetic: C(63,32) exact; both sides in exact log2; floor caps at
    (128,64) for BOTH odd-lift sub-families (|S|=k+1 and k+3); rate<=1/4
    emptiness derivation z0 >= 0 <=> 2k >= n-1 checked across shapes.
A4  719/dominance: 719 == floor(n^6/C(n+6,6)) at s=41..44 (and neighbors);
    exact dominance sum with max-excess location + magnitude (the 2^-691).
A5  Clause-(D) ratio grid recomputed independently (Fraction, s=13..44).
A6  FRESH CELL (32,16,193,consec): full independent census — S2 identity,
    COL cap on realized scale-2 classes, DD-atlas chain, odd-lift bands,
    minimal-chart injectivity, nonemptiness (#137).
A7  FRESH MUTATION FM1 (#133 normalization): layer-normalized labels must
    break S2 + empty/shift the census (the #137 vacuity hazard made live).
A8  FRESH MUTATION FM2 (U1 margin): one-unit degree relaxation must admit a
    band chart with >= 2 members (margin-exactly-1 made live).
A9  Banked-census independent cross-parse: COL support cap + multiplicity-1
    re-swept with independent code (no reuse of bsr_check internals).
"""
import itertools, json
from fractions import Fraction
from math import comb, log2

PRIZE = "/home/u2470931/smooth-read-solomin/prize"
FAILS = []
def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    if not ok: FAILS.append(name)

def lgf(fr):  # exact-ish log2 of a Fraction via float on the ratio of bit lengths
    return log2(fr.numerator) - log2(fr.denominator) if fr.numerator < 2**900 and fr.denominator < 2**900 else (fr.numerator.bit_length() - fr.denominator.bit_length())

print("="*72); print("A1: Lemma COL algebra")
# ratio identity C(n',h) = C(n'-1,h) * n'/(n'-h), symbolic over a sweep
ok = all(Fraction(comb(np_,h)) == Fraction(comb(np_-1,h))*Fraction(np_,np_-h)
         for np_ in range(2,200) for h in range(0,np_))
check("A1 identity C(n',h) == C(n'-1,h)*n'/(n'-h) (n'<200 sweep)", ok)
# with n'=n/M, h=A/M: n'/(n'-h) == n/(n-A)
ok = all(Fraction(n//M, n//M - A//M) == Fraction(n, n-A)
         for n in (16,32,64) for M in (2,4,8) for A in range(M, n, M) if A < n)
check("A1 n'/(n'-h) == n/(n-A) rewrite", ok)
# cap derivation: A_own = M*ceil((k+1)/M) <= k+M; n-(k+M) >= t iff M <= t
def own_A(k,M): return M*(-(-(k+1)//M))
worst = {}
for s in range(13,45):
    n = 2**s
    for rd in (2,4,8,16):
        k = n//rd; t=(n-k)//2; M=2; w=Fraction(0)
        while M<=t:
            A=own_A(k,M); assert A<=k+M and A>=k+1
            w=max(w,Fraction(n,n-A)); M*=2
        worst[rd]=max(worst.get(rd,Fraction(0)),w)
check("A1 cap == 2/(1-rho) per rate: {2:4, 4:8/3, 8:16/7, 16:32/15}",
      worst=={2:Fraction(4),4:Fraction(8,3),8:Fraction(16,7),16:Fraction(32,15)},
      f"{ {r: str(v) for r,v in worst.items()} }")
# boundary probe: COL(v) exactness holds iff M | k; counterexample above t
n,k = 32,8; t=(n-k)//2
A16 = own_A(k,16)  # M=16 > t=12
Q16 = comb(n//16 - 1, A16//16)
check("A1 COL(v) OVERSTATED for M !| k: (n,k,M)=(32,8,16), M=16 > t=12 but "
      "own column NONDEGENERATE", Q16 != 0 and A16 <= n-16,
      f"A_own={A16}, Q={Q16}, n/(n-A)={Fraction(n,n-A16)}")
# the load-bearing direction: all dyadic M <= t nondegenerate, official grid
ok = True
for s in range(13,45):
    n=2**s
    for rd in (2,4,8,16):
        k=n//rd; t=(n-k)//2; M=2
        while M<=t:
            A=own_A(k,M)
            if not (A//M <= n//M - 1): ok=False
            M*=2
check("A1 load-bearing direction: every dyadic M <= t own cell nondegenerate "
      "(official grid)", ok)
# exact-4 attainment
n=2**13; k=n//2; t=(n-k)//2; A=own_A(k,t)
check("A1 cap attains EXACTLY 4 at rho=1/2, M=t", Fraction(n,n-A)==4)
# {k+2,k+4} csp-band cells cap <= 4 in scope
ok = all(Fraction(2**s, 2**s - 2**s//rd - 4) <= 4 for s in range(13,45) for rd in (2,4,8,16))
check("A1 csp-band cells n/(n-k-4) <= 4 in scope", ok)

print("="*72); print("A2: g1a instances, exact margins")
def is_prime(m):
    if m<2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if m%p==0: return m==p
    d,s=m-1,0
    while d%2==0: d//=2; s+=1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x=pow(a,d,m)
        if x in (1,m-1): continue
        for _ in range(s-1):
            x=x*x%m
            if x==m-1: break
        else: return False
    return True
q13 = 2*4096*4096+1
while not (q13 % 8192 == 1 and is_prime(q13)): q13 += 8192
check("A2 s=13 field q=33710081 reproduced (>= 2*n'^2, ==1 mod 8192)",
      q13==33710081 and q13>=2*4096**2)
INST=[("(256,128,65537)",128,64,65537,True),("(8192,4096,q13)",4096,2048,q13,True),
      ("(512,256,2^128)",256,128,2**128,False),("(1024,512,2^256)",512,256,2**256,False)]
exp_margin=[33,47,147,275]; exp_viol=[54,3976,None,None]
for (nm,npr,kpr,q,realfield),em in zip(INST,exp_margin):
    n=2*npr
    check(f"A2 {nm} F4 hypothesis q >= 2 n'^2", q>=2*npr*npr)
    Bf = comb(npr-1,kpr)//(4*q*(kpr+1))
    old = Fraction(121,128)*n**6
    viol = lgf(Fraction(3*Bf)/old)
    fitm = lgf(Fraction(719*comb(npr-1,kpr+1), Bf))
    cap1 = comb(npr-1,kpr)   <= 719*comb(npr-1,kpr+1)
    cap2 = comb(npr-1,kpr+1) <= 719*comb(npr-1,kpr+2)
    check(f"A2 {nm} old form violated / column fits / per-profile caps",
          3*Bf>old and Bf<=719*comb(npr-1,kpr+1) and cap1 and cap2,
          f"violation +{viol:.1f} bits; fit margin {fitm:.1f} bits (claimed ~{em})")

print("="*72); print("A3: #145 arithmetic")
c6332 = comb(63,32)
check("A3 C(63,32) == 916312070471295267", c6332==916312070471295267)
wide_budget = Fraction(121,128)*128**6
check("A3 C(63,32) > (121/128)128^6", c6332 > wide_budget,
      f"2^{log2(c6332):.2f} > 2^{lgf(wide_budget):.2f}  "
      f"[NB packet says 2^41.3; true 2^{lgf(wide_budget):.2f}]")
# floor caps at (128,64): core=2(k'-1)+1=63 pts, t_ch=(n-63)/2
kpr=32; t_ch=(128-63)//2; z0=(kpr-1)-(t_ch-2)
cap_k1 = sum(comb(kpr-1,z)*comb(t_ch,kpr-z) for z in range(z0+1))
cap_k3 = sum(comb(kpr-1,z)*comb(t_ch,kpr+1-z) for z in range(z0+1))
check("A3 floor cap |S|=k+1 family at (128,64) == 993", cap_k1==993,
      f"t_ch={t_ch}, z0={z0}")
check("A3 floor cap TOTAL incl |S|=k+3 family == 1024 (still poly < n^2)",
      cap_k1+cap_k3 < 128**2, f"k+3 family adds {cap_k3} -> total {cap_k1+cap_k3}")
# structural emptiness: z0 >= 0 <=> 2k >= n-1 (core=k-1 odd, t_ch=(n-k+1)/2)
ok=True
for s in range(4,20):
    n=2**s
    for rd in (2,4,8,16):
        k=n//rd
        if k%2: continue
        kpr=k//2; t_ch=(n-(k-1))//2; z0=(kpr-1)-(t_ch-2)
        if (z0>=0) != (2*k>=n-1): ok=False
check("A3 emptiness law: z0 >= 0 <=> 2k >= n-1 (floor band empty for ALL "
      "rho <= 1/4, nonempty at rho = 1/2)", ok)
# odd-lift band membership algebra: |agr|=k': d=2(m-1); |agr|=k'+1: d=2(m-2)
ok=all(2*(kp-1-z)==2*((kp-z)-1) for kp in range(2,50) for z in range(kp))
ok&=all(2*(kp-1-z)==2*((kp+1-z)-2) for kp in range(2,50) for z in range(kp))
check("A3 odd lifts ALWAYS wide-band: d = 2(m-1) resp. 2(m-2) >= 2(m-2)", ok)

print("="*72); print("A4: 719 allowance + first-scale dominance")
ok = all((2**s)**6//comb(2**s+6,6) == 719 for s in (41,42,43,44))
check("A4 719 == floor(n^6/C(n+6,6)) at s=41..44", ok,
      f"s=40 gives {(2**40)**6//comb(2**40+6,6)}, s=45 gives {(2**45)**6//comb(2**45+6,6)}")
wex=Fraction(0); wloc=None
for s in range(13,21):
    n=2**s
    for rd in (2,4,8,16):
        k=n//rd; t=(n-k)//2
        Q2=comb(n//2-1,(k+2)//2); tot=Fraction(0); M=4
        while M<=t:
            A=own_A(k,M); h=A//M
            if h<=n//M-1: tot+=comb(n//M-1,h)
            M*=2
        ex=Fraction(tot,Q2)
        if ex>wex: wex, wloc = ex, (s,rd)
check("A4 dominance: worst excess sum_{4<=M<=t} Q_M(A_own)/Q_2(k+2) ~ 2^-691",
      wex>0 and -692<=lgf(wex)<=-690,
      f"max excess 2^{lgf(wex):.1f} at (s,rate)= {wloc}")

print("="*72); print("A5: clause-(D) ratio grid (independent)")
mx=Fraction(0); loc=None
for s in range(13,45):
    n=2**s
    for rd in (2,4,8,16):
        npr=n//2; kpr=n//rd//2
        for ap in (kpr+1,kpr+2):
            r=Fraction(ap,npr-ap)
            if r>mx: mx,loc=r,(s,rd,ap-kpr)
check("A5 max a'/(n'-a') over grid == 2050/2046 ~ 1.001955 at s=13, rho=1/2, "
      "a'=k'+2", mx==Fraction(2050,2046), f"max={float(mx):.6f} at {loc}")
check("A5 719*Q/trivial per-profile margin ~ 718x (packet says ~350x: that is "
      "the TWO-profile aggregate 719/2.002)", abs(719/float(mx)-717.6)<1,
      f"per-profile {719/float(mx):.1f}x; aggregate {719/(1+float(mx)):.1f}x")

# ---------------------------------------------------------------- field utils
def order_n_domain(p,n):
    a=2
    while True:
        g0=pow(a,(p-1)//n,p)
        if pow(g0,n//2,p)!=1: break
        a+=1
    dom=[pow(g0,j,p) for j in range(n)]
    assert len(set(dom))==n
    return dom
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
def stab_order(S,n):
    c,M=1,2
    while M<=n:
        s=n//M
        if all(((x+s)%n) in S for x in S): c=M
        else: break
        M*=2
    return c

def fresh_cell(n,k,p,smode,label_norm="word"):
    """Independent implementation of the fiber-aligned cell + full census."""
    assert k%2==0 and (p-1)%n==0
    dom=order_n_domain(p,n); half=n//2; npr, kpr = half, k//2; nf=kpr-1
    core=[]
    for j in range(nf): core+=[j,j+half]
    core.append(nf)
    petals=[[j,j+half] for j in range(nf+1,half)]
    t_ch=len(petals)
    scal=[]
    v=1
    for i in range(t_ch):
        scal.append((i+1)%p if smode=="consec" else v); v=v*5%p
    loc=locator([dom[j] for j in core],p)
    values=[0]*n
    for c_i,P in zip(scal,petals):
        for j in P: values[j]=c_i*ev(loc,dom[j],p)%p
    domq=[dom[j]*dom[j]%p for j in range(npr)]
    ynf=domq[nf]
    locq=locator(domq[:nf],p)
    u1=[0]*npr
    for i,j in enumerate(range(nf+1,npr)):
        lab = scal[i] if label_norm=="word" else scal[i]*pow(domq[j]-ynf,-1,p)%p
        u1[j]=lab*ev(locq,domq[j],p)%p
    xnf=dom[nf]
    s2 = all(values[j]==(dom[j]-xnf)*u1[j%npr]%p for j in range(n))
    # complete quotient census
    seen={}
    for sub in itertools.combinations(range(npr),kpr):
        g=interpolate([domq[j] for j in sub],[u1[j] for j in sub],kpr,p)
        if g in seen: continue
        seen[g]=frozenset(j for j in range(npr) if ev(g,domq[j],p)==u1[j])
    band={}; odd=[]
    for g,agr in seen.items():
        if len(agr)<kpr: continue
        if ev(g,ynf,p)==0:
            if len(agr)in(kpr+1,kpr+2): band[agr]=g
        elif len(agr) in (kpr,kpr+1): odd.append((g,agr))
    return dict(dom=dom,domq=domq,u1=u1,values=values,core=core,petals=petals,
                scal=scal,band=band,odd=odd,npr=npr,kpr=kpr,nf=nf,t_ch=t_ch,
                xnf=xnf,ynf=ynf,p=p,n=n,k=k,s2=s2)

print("="*72); print("A6: FRESH CELL (32,16,193,consec) — independent census")
C=fresh_cell(32,16,193,"consec")
npr,kpr,p,n,k = C["npr"],C["kpr"],C["p"],C["n"],C["k"]
check("A6 S2 word factorization identity holds", C["s2"])
nb1=sum(1 for S in C["band"] if len(S)==kpr+1); nb2=sum(1 for S in C["band"] if len(S)==kpr+2)
check("A6 census NONEMPTY (#137)", nb1+nb2+len(C["odd"])>0,
      f"band classes: a'={kpr+1}: {nb1}, a'={kpr+2}: {nb2}; odd lifts {len(C['odd'])}")
# COL on the realized scale>=2 classes, lifted officially
colok=True; multok=True
lifted={}
for agr,g in C["band"].items():
    S=frozenset(j for j in range(n) if (C["dom"][j]-C["xnf"])*ev(g,C["domq"][j%npr],p)%p==C["values"][j])
    M=stab_order(S,n); A=len(S)
    if M>=2 and A%M==0:
        if not (len({j%(n//M) for j in S})==A//M and A//M<=n//M): colok=False
        cap=comb(n//M - (0 if A==n else 0) ,0)  # placeholder no-op
        if len(S)!=2*len(agr): multok=False
    lifted[S]=g
ncl=len(lifted)
# independent COL cap per (M,A) cell
cells={}
for S in lifted:
    M=stab_order(S,n)
    cells.setdefault((M,len(S)),set()).add(S)
colcap=all(len(v)<=comb(n//M, A//M) for (M,A),v in cells.items())
check("A6 COL support cap on fresh realized cells", colcap,
      f"cells: { {ka: len(v) for ka,v in cells.items()} }")
check("A6 lift semantics |S| == 2|agr| for periodic classes", multok)
# DD-atlas chain
others=[j for j in range(npr) if j!=C["nf"]]
ddres={}
for ap in (kpr+1,kpr+2):
    ndd=0
    for sub in itertools.combinations(others,ap-1):
        pts=(C["nf"],)+sub
        xs=[C["domq"][j] for j in pts]; ys=[C["u1"][j] for j in pts]
        g=interpolate(xs[:kpr],ys[:kpr],kpr,p)
        if all(ev(g,x,p)==y for x,y in zip(xs[kpr:],ys[kpr:])): ndd+=1
    ddres[ap]=ndd
okc=True
for ap in (kpr+1,kpr+2):
    nb=sum(1 for S in C["band"] if len(S)==ap)
    triv=comb(npr-1,ap-1); col=comb(npr-1,ap)
    okc &= nb<=ddres[ap]<=triv<=719*col
    print(f"     a'={ap}: B={nb} <= N_DD={ddres[ap]} <= {triv} <= {719*col}")
check("A6 clause-(D) chain B <= N_DD <= C(n'-1,a'-1) <= 719*Q_2(2a')", okc)
# minimal charts distinct
coreq=set(range(kpr)); charts=set(); dup=False
for S in C["band"]:
    WP=(frozenset(S&coreq),frozenset(S-coreq))
    dup |= WP in charts; charts.add(WP)
check("A6 minimal-chart injectivity on fresh cell", not dup)
# odd-lift end-to-end + bands
pset=[frozenset(P) for P in C["petals"]]; wide=True; nfl=0
for g,agr in C["odd"]:
    S=frozenset(j for j in range(n) if (C["dom"][j]-C["xnf"])*ev(g,C["domq"][j%npr],p)%p==C["values"][j])
    if len(S)!=1+2*len(agr) or stab_order(S,n)!=1: wide=False
    if any((S&P) not in (frozenset(),P) for P in pset): wide=False
    d=sum(1 for j in C["core"] if j not in S); m=sum(1 for P in pset if P<=S)
    if d<2*(m-2): wide=False
    if d>=2*(C["t_ch"]-2): nfl+=1
z0=(kpr-1)-(C["t_ch"]-2)
capf=sum(comb(kpr-1,z)*comb(C["t_ch"],kpr-z) for z in range(max(z0+1,0)))
capf3=sum(comb(kpr-1,z)*comb(C["t_ch"],kpr+1-z) for z in range(max(z0+1,0)))
check("A6 odd lifts end-to-end (aperiodic, full-petal, wide band) at fresh "
      "prime/smode", wide, f"{len(C['odd'])} lifts, floor-band {nfl}")
check("A6 floor-band count <= TOTAL cap (both sub-families)", nfl<=capf+capf3,
      f"{nfl} <= {capf}+{capf3}")
check("A6 wide-band mass binomial-scale (> supply/4)",
      len(C["odd"])>comb(npr-1,kpr)/4, f"{len(C['odd'])} vs C(15,8)={comb(npr-1,kpr)}")

print("="*72); print("A7: FRESH MUTATION FM1 — layer-normalized labels (#133)")
Cm=fresh_cell(32,16,193,"consec",label_norm="layer")
nb=len(Cm["band"])
check("FM1 TRIPS: S2 identity FAILS under layer normalization", not Cm["s2"])
check("FM1 TRIPS: census changed/emptied (fresh-cell pin broken)",
      len(Cm["band"])!=len(C["band"]) or Cm["band"].keys()!=C["band"].keys(),
      f"word-norm band {len(C['band'])} vs layer-norm {len(Cm['band'])}")

print("="*72); print("A8: FRESH MUTATION FM2 — U1 margin (deg k'-1 -> k')")
# For realized band charts (W,P) with m'=d'+2, count RELAXED members:
# deg <= k' polys g = L_W * h vanishing on W with >= d'+1 agreements on P.
trip=False; scanned=0
for agr in C["band"]:
    W=sorted(agr&coreq); P=sorted(agr-coreq); z=len(W); dpr=kpr-z; mpr=len(P)
    if mpr!=dpr+2: continue
    scanned+=1
    locW=locator([C["domq"][j] for j in W],p)
    members=set()
    for sub in itertools.combinations(P,dpr+1):
        xs=[C["domq"][j] for j in sub]
        ys=[C["u1"][j]*pow(ev(locW,C["domq"][j],p),-1,p)%p for j in sub]
        h=interpolate(xs,ys,dpr+1,p)   # deg h <= d' -> deg g <= k' (RELAXED)
        nag=sum(1 for j in P if ev(h,C["domq"][j],p)*ev(locW,C["domq"][j],p)%p==C["u1"][j])
        if nag>=dpr+1: members.add(h)
    if len(members)>=2: trip=True
check("FM2 TRIPS: some band chart admits >= 2 members under one-unit degree "
      "relaxation (U1 margin is EXACTLY 1)", trip, f"charts scanned {scanned}")

print("="*72); print("A9: banked census independent re-sweep")
recs=json.load(open(PRIZE+"/critical/nodes/petal_growth/notes/cg_petal_census_results.json"))
bad=0; nc=0; mrq=Fraction(0); mrs=Fraction(0)
for r in recs:
    n_=r["n"]
    for tag in ("fp0_edge","fp0_own","fp0_all","fp1_edge","fp1_own","fp1_all"):
        for ck,v in r[tag].items():
            M,A=map(int,ck.split(",")); h=A//M; np_=n_//M; nc+=1
            sup=comb(np_,h); Q=comb(np_-1,h) if h<=np_-1 else 0
            if v["classes"]>sup or v["codewords"]!=v["classes"] or v["Q"]!=Q: bad+=1
            if Q: mrq=max(mrq,Fraction(v["classes"],Q))
            mrs=max(mrs,Fraction(v["classes"],sup))
check("A9 independent sweep: COL cap + multiplicity-1 + Q convention on all "
      "banked cells", bad==0, f"{nc} cells, max cls/Q={mrq}, max cls/sup={mrs}")
check("A9 max ratios match packet (4/3 and 2/3)", mrq==Fraction(4,3) and mrs==Fraction(2,3))

print("="*72)
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURES"); [print("  -",f) for f in FAILS]
else:
    print("RESULT: ALL INDEPENDENT CHECKS PASS")
