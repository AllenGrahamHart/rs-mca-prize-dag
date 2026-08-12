"""D2a - reproduce the exact T=2 solve over mu_32 and test the s!=0 criterion.
r37_third_solve. Self-contained. Appends to d2_results.txt.
"""
import random, time, itertools

def trim(a):
    while a and a[-1] == 0: a.pop()
    return a
def padd(a,b,p):
    n=max(len(a),len(b)); r=[0]*n
    for i in range(n): r[i]=((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p
    return trim(r)
def psub(a,b,p):
    n=max(len(a),len(b)); r=[0]*n
    for i in range(n): r[i]=((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0))%p
    return trim(r)
def pmul(a,b,p):
    if not a or not b: return []
    r=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b): r[i+j]=(r[i+j]+ai*bj)%p
    return trim(r)
def pscal(a,c,p): return trim([(x*c)%p for x in a])
def pdivmod(a,b,p):
    a=a[:]; db=len(b)-1; inv=pow(b[-1],p-2,p); q=[0]*max(0,len(a)-db)
    for i in range(len(a)-1,db-1,-1):
        c=(a[i]*inv)%p
        if c:
            q[i-db]=c
            for j in range(db+1): a[i-db+j]=(a[i-db+j]-c*b[j])%p
    return trim(q),trim(a)
def pgcd(a,b,p):
    a=a[:];b=b[:]
    while b: a,b=b,pdivmod(a,b,p)[1]
    return pscal(a,pow(a[-1],p-2,p),p) if a else []
def peval(a,x,p):
    r=0
    for c in reversed(a): r=(r*x+c)%p
    return r
def mu_set(p,N):
    g=2
    while True:
        ok=True
        for d in (2,3,5,7,11):
            if (p-1)%d==0 and pow(g,(p-1)//d,p)==1: ok=False;break
        if ok: break
        g+=1
    h=pow(g,(p-1)//N,p); S=set(); v=1
    for _ in range(N): S.add(v); v=v*h%p
    return sorted(S)

# ---- ring F_q[x]/(fm), fm monic degree 4 ----
def rmul(a,b,fm,p):
    r=[0]*7
    for i in range(4):
        if a[i]:
            for j in range(4): r[i+j]=(r[i+j]+a[i]*b[j])%p
    for i in (6,5,4):
        c=r[i]
        if c:
            r[i]=0
            for j in range(4): r[i-4+j]=(r[i-4+j]-c*fm[j])%p
    return r[:4]
def redmod(a,fm,p):
    """reduce any poly mod monic fm of degree 4 -> 4-vector"""
    r=a[:]
    for i in range(len(r)-1,3,-1):
        c=r[i]
        if c:
            r[i]=0
            for j in range(4): r[i-4+j]=(r[i-4+j]-c*fm[j])%p
    r=r+[0]*(4-len(r))
    return [x%p for x in r[:4]]
def rinv(a,fm,p):
    r0=fm[:]+[1]; r1=trim(a[:])
    if not r1: return None
    s0=[]; s1=[1]
    while r1:
        q,r=pdivmod(r0,r1,p)
        s0,s1=s1,psub(s0,pmul(q,s1,p),p)
        r0,r1=r1,r
    if len(r0)!=1: return None
    c=pow(r0[0],p-2,p)
    v=pscal(s0,c,p); v=v+[0]*(4-len(v))
    return v[:4]
def nrm(a,p):
    for i in range(4):
        if a[i]:
            c=pow(a[i],p-2,p); return tuple((x*c)%p for x in a)
    return None

def config(p,D,rng,S0):
    """Route A: Q_0 = prod(S0) split over mu_32; returns (f,g,k,L,ell,Q0) or None"""
    Q0=[1]
    for a in S0: Q0=pmul(Q0,[(-a)%p,1],p)
    for _ in range(40):
        ell=rng.randrange(p)
        if peval(Q0,ell,p)==0: continue
        L=[(-ell)%p,1]
        LQ0=pmul(L,Q0,p)
        cand=[x for x in range(p) if x!=ell and peval(Q0,x,p)!=0
              and pow(peval(LQ0,x,p),(p-1)//2,p)==1]
        if len(cand)<4: continue
        R=rng.sample(cand,4)
        g=[1]
        for r in R: g=pmul(g,[(-r)%p,1],p)
        # f0: interpolate +-sqrt(L Q0) at R
        vals=[]
        for r in R:
            v=peval(LQ0,r,p); sq=pow(v,(p+1)//4,p) if p%4==3 else tonelli(v,p)
            if sq*sq%p!=v: return None
            vals.append(sq if rng.randrange(2) else (-sq)%p)
        f0=lagrange(R,vals,p)
        c=rng.randrange(p)
        f=padd(f0,pscal(g,c,p),p)
        if len(f)!=5: continue
        if peval(f,ell,p)==0 or peval(g,ell,p)==0: continue
        num=psub(pmul(f,f,p),LQ0,p)
        k,rem=pdivmod(num,g,p)
        if rem: continue
        return f,g,k,L,ell,Q0
    return None
def tonelli(n,p):
    if n==0: return 0
    if p%4==3: return pow(n,(p+1)//4,p)
    q=p-1; s=0
    while q%2==0: q//=2; s+=1
    z=2
    while pow(z,(p-1)//2,p)!=p-1: z+=1
    m=s; c=pow(z,q,p); t=pow(n,q,p); r=pow(n,(q+1)//2,p)
    while t!=1:
        i=0; tt=t
        while tt!=1: tt=tt*tt%p; i+=1
        b=pow(c,1<<(m-i-1),p); m=i; c=b*b%p; t=t*c%p; r=r*b%p
    return r
def lagrange(X,Y,p):
    res=[]
    for i,xi in enumerate(X):
        num=[1]; den=1
        for j,xj in enumerate(X):
            if i!=j:
                num=pmul(num,[(-xj)%p,1],p); den=den*(xi-xj)%p
        res=padd(res,pscal(num,Y[i]*pow(den,p-2,p)%p,p),p)
    return res

def enum_side(pts,fm,p,maxsz,invert):
    """dict size -> list of (nrm(u) or nrm(u^-1), frozenset)"""
    out={j:[] for j in range(maxsz+1)}
    lin=[[(-a)%p,1,0,0] for a in pts]
    def rec(i,cur,sz,chosen):
        out[sz].append((cur,chosen))
        if sz==maxsz or i==len(pts): return
        for j in range(i,len(pts)):
            rec(j+1,rmul(cur,lin[j],fm,p),sz+1,chosen+(pts[j],))
    rec(0,[1,0,0,0],0,())
    res={}
    for j in range(maxsz+1):
        lst=[]
        for u,ch in out[j]:
            if invert:
                v=rinv(u,fm,p)
                if v is None: continue
                lst.append((nrm(v,p),ch))
            else:
                lst.append((nrm(u,p),ch))
        res[j]=lst
    return res

def solve_S2(f,g,L,p,D):
    """all S2 subset mu_32, |S2|=7, with g^2 == gamma*L*P_{S2} (mod f)"""
    if len(f)!=5: return []
    c=pow(f[4],p-2,p); fm=[(x*c)%p for x in f[:4]]
    G2=redmod(pmul(g,g,p),fm,p)
    Lr=[L[0],L[1],0,0]
    A=D[:16]; B=D[16:]
    tA=enum_side(A,fm,p,7,False)
    tB=enum_side(B,fm,p,7,False)
    G2i=rinv(G2,fm,p)
    if G2i is None: return []
    sols=[]
    for j in range(8):
        dd={}
        for key,ch in tA[j]:
            if key is not None: dd.setdefault(key,[]).append(ch)
        if not dd: continue
        for key2,ch2 in tB[7-j]:
            if key2 is None: continue
            # need nrm(L*uA*uB*G2^{-1}) == (1,0,0,0)  <=> nrm(uA) == nrm((L*uB*G2i)^{-1})
            v=rmul(rmul(Lr,[key2[0],key2[1],key2[2],key2[3]],fm,p),G2i,fm,p)
            w=rinv(v,fm,p)
            if w is None: continue
            kk=nrm(w,p)
            if kk in dd:
                for ch1 in dd[kk]: sols.append(tuple(sorted(ch1+ch2)))
    return sols

def run(p,nconf,out,rng,tbudget):
    D=mu_set(p,32)
    t0=time.time()
    nconfdone=0; nsol=0; scrit_ok=0; scrit_bad=0
    hist={}; sdist={}; Tdist={}; ovmaxes=[]
    for _ in range(nconf):
        if time.time()-t0>tbudget: break
        S0=tuple(sorted(rng.sample(D,7)))
        cfg=config(p,D,rng,S0)
        if cfg is None: continue
        f,g,k,L,ell,Q0=cfg
        nconfdone+=1
        for S2 in solve_S2(f,g,L,p,D):
            P2=[1]
            for b in S2: P2=pmul(P2,[(-b)%p,1],p)
            LP2=pmul(L,P2,p)
            # gamma from g^2 = gamma * L*P2 mod f
            cc=pow(f[4],p-2,p); fm=[(x*cc)%p for x in f[:4]]
            u=redmod(LP2,fm,p); v=redmod(pmul(g,g,p),fm,p)
            idx=None
            for i in range(4):
                if u[i]: idx=i;break
            if idx is None: continue
            gam=v[idx]*pow(u[idx],p-2,p)%p
            if gam==0: continue
            if [x*gam%p for x in u]!=v: continue
            Q2=pscal(P2,gam,p)
            hnum=psub(pmul(L,Q2,p),pmul(g,g,p),p)
            h,rem=pdivmod(hnum,f,p)
            if rem: continue
            N1=padd(pmul(f,g,p),pmul(h,k,p),p)
            Q1,rem1=pdivmod(N1,L,p)
            if rem1: continue
            nsol+=1
            ov=len(set(S0)&set(S2))
            s=len(pgcd(pgcd(Q0,Q1,p),Q2,p))-1
            hist[(ov,s)]=hist.get((ov,s),0)+1
            sdist[s]=sdist.get(s,0)+1
            dfg=len(pgcd(f,g,p))-1
            if s==ov: scrit_ok+=1
            else: scrit_bad+=1
            if s==0 and len(Q0)==8 and len(Q1)==8 and len(Q2)==8:
                # T over mu_32 via the vote/quadratic structure
                cnt={}
                for x in D:
                    a0=peval(Q0,x,p); a1=peval(Q1,x,p); a2=peval(Q2,x,p)
                    if a2==0:
                        if a1: cnt[(-a0)*pow(a1,p-2,p)%p]=cnt.get((-a0)*pow(a1,p-2,p)%p,0)+1
                        cnt['inf']=cnt.get('inf',0)+1
                    else:
                        disc=(a1*a1-4*a0*a2)%p
                        if disc==0:
                            z=(-a1)*pow(2*a2%p,p-2,p)%p; cnt[z]=cnt.get(z,0)+1
                        elif pow(disc,(p-1)//2,p)==1:
                            sq=tonelli(disc,p); i2=pow(2*a2%p,p-2,p)
                            for sgn in (sq,(-sq)%p):
                                z=(-a1+sgn)*i2%p; cnt[z]=cnt.get(z,0)+1
                T=sum(1 for z,c in cnt.items() if c==7)
                Tdist[T]=Tdist.get(T,0)+1
                # OV4: max_z |roots(Q_z) cap (S0 u S2)|
                U=sorted(set(S0)|set(S2)); mx=0
                for z in range(1,p):
                    fzg=padd(f,pscal(g,z,p),p)
                    mx=max(mx,sum(1 for x in U if peval(fzg,x,p)==0))
                ovmaxes.append((mx,dfg))
    out.append("q=%d configs=%d exact_S2_solutions=%d  per-config=%.2f (predicted C(32,7)/q^3=%.2f)"
               %(p,nconfdone,nsol,nsol/max(1,nconfdone),3365856/p**3))
    out.append("q=%d (|S0 cap S2|, s) joint histogram = %s"%(p,sorted(hist.items())))
    out.append("q=%d SCRIT s==|S0 cap S2| : %d agree / %d disagree"%(p,scrit_ok,scrit_bad))
    out.append("q=%d s-distribution = %s ; s=0 fraction = %.4f (predicted C(25,7)/C(32,7)=0.1428)"
               %(p,sorted(sdist.items()),sdist.get(0,0)/max(1,nsol)))
    out.append("q=%d T over mu_32 on the s=0 certified objects: %s"%(p,sorted(Tdist.items())))
    out.append("q=%d OV4 (max_z |roots(f+zg) cap (S0 u S2)|, deg gcd(f,g)) = %s"%(p,sorted(set(ovmaxes))))

def main():
    rng=random.Random(370211)
    out=["","=== RUN d2_scrit %s ==="%time.strftime("%Y-%m-%dT%H:%M:%S")]
    run(97,60,out,rng,110)
    run(193,120,out,rng,120)
    with open("notes/pilots_20260811/r37_third_solve/d2_results.txt","a") as fh:
        fh.write("\n".join(out)+"\n")
    print("\n".join(out))

main()
