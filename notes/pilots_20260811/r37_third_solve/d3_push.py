"""D2b/D3 - bespoke push past T=3 with an EXACT double prescription, and the
(OV4) pairwise-overlap law measured on every T>=3 object. r37_third_solve.
Self-contained. Appends to d3_results.txt.
"""
import random, time

def trim(a):
    while a and a[-1]==0: a.pop()
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
def lagrange(X,Y,p):
    res=[]
    for i,xi in enumerate(X):
        num=[1]; den=1
        for j,xj in enumerate(X):
            if i!=j: num=pmul(num,[(-xj)%p,1],p); den=den*(xi-xj)%p
        res=padd(res,pscal(num,Y[i]*pow(den,p-2,p)%p,p),p)
    return res
def redmod(a,fm,p):
    r=a[:]
    for i in range(len(r)-1,3,-1):
        c=r[i]
        if c:
            r[i]=0
            for j in range(4): r[i-4+j]=(r[i-4+j]-c*fm[j])%p
    r=r+[0]*(4-len(r))
    return [x%p for x in r[:4]]
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
def rinv(a,fm,p):
    r0=fm[:]+[1]; r1=trim(a[:])
    if not r1: return None
    s0=[]; s1=[1]
    while r1:
        q,r=pdivmod(r0,r1,p)
        s0,s1=s1,psub(s0,pmul(q,s1,p),p)
        r0,r1=r1,r
    if len(r0)!=1: return None
    v=pscal(s0,pow(r0[0],p-2,p),p); v=v+[0]*(4-len(v))
    return v[:4]

def tables(p):
    sq={}
    for a in range(p): sq.setdefault(a*a%p,a)
    return sq

def build(p,rng,SQ):
    """exact double prescription over a bespoke domain: Q_0 and Q_2 both split."""
    ell=rng.randrange(p)
    L=[(-ell)%p,1]
    S0=rng.sample([x for x in range(p) if x!=ell],7)
    Q0=[1]
    for a in S0: Q0=pmul(Q0,[(-a)%p,1],p)
    LQ0=pmul(L,Q0,p)
    cand=[x for x in range(p) if x!=ell and peval(Q0,x,p)!=0 and peval(LQ0,x,p) in SQ]
    if len(cand)<4: return None
    R=rng.sample(cand,4)
    g=[1]
    for r in R: g=pmul(g,[(-r)%p,1],p)
    vals=[]
    for r in R:
        s=SQ[peval(LQ0,r,p)]
        vals.append(s if rng.randrange(2) else (-s)%p)
    f=padd(lagrange(R,vals,p),pscal(g,rng.randrange(p),p),p)
    if len(f)!=5: return None
    if peval(f,ell,p)==0 or peval(g,ell,p)==0: return None
    k,rem=pdivmod(psub(pmul(f,f,p),LQ0,p),g,p)
    if rem: return None
    c=pow(f[4],p-2,p); fm=[(x*c)%p for x in f[:4]]
    Li=rinv([L[0],L[1],0,0],fm,p)
    if Li is None: return None
    tau=rmul(redmod(pmul(g,g,p),fm,p),Li,fm,p)      # target: prod(x-b) ~ tau
    B4=rng.sample([x for x in range(p) if x!=ell],4)
    U=[1,0,0,0]
    for b in B4: U=rmul(U,[(-b)%p,1,0,0],fm,p)
    Ui=rinv(U,fm,p)
    if Ui is None: return None
    V=rmul(tau,Ui,fm,p)
    order=list(range(p)); rng.shuffle(order)
    for b5 in order:
        if b5==ell or b5 in B4: continue
        li=rinv([(-b5)%p,1,0,0],fm,p)
        if li is None: continue
        Z=rmul(V,li,fm,p)
        if Z[3]!=0 or Z[2]==0: continue
        iv=pow(Z[2],p-2,p)
        s1=(-Z[1])*iv%p; s2=Z[0]*iv%p
        disc=(s1*s1-4*s2)%p
        if disc not in SQ: continue
        sd=SQ[disc]; i2=pow(2,p-2,p)
        b6=(s1+sd)*i2%p; b7=(s1-sd)*i2%p
        Bs=B4+[b5,b6,b7]
        if len(set(Bs))!=7 or ell in Bs: continue
        P2=[1]
        for b in Bs: P2=pmul(P2,[(-b)%p,1],p)
        u=redmod(pmul(L,P2,p),fm,p); v=redmod(pmul(g,g,p),fm,p)
        idx=next((i for i in range(4) if u[i]),None)
        if idx is None: continue
        gam=v[idx]*pow(u[idx],p-2,p)%p
        if gam==0 or [x*gam%p for x in u]!=v: continue
        Q2=pscal(P2,gam,p)
        h,r2=pdivmod(psub(pmul(L,Q2,p),pmul(g,g,p),p),f,p)
        if r2 or len(h)>5: continue
        Q1,r3=pdivmod(padd(pmul(f,g,p),pmul(h,k,p),p),L,p)
        if r3: continue
        if len(Q0)!=8 or len(Q1)!=8 or len(Q2)!=8: continue
        if len(pgcd(pgcd(Q0,Q1,p),Q2,p))-1!=0: continue
        return f,g,h,k,L,ell,Q0,Q1,Q2,sorted(S0),sorted(Bs)
    return None

def tally(Q0,Q1,Q2,p,SQ):
    """slope -> set of x in F_q with q_x(slope)=0 (finite slopes only)"""
    d={}
    i2=pow(2,p-2,p)
    for x in range(p):
        a0=peval(Q0,x,p); a1=peval(Q1,x,p); a2=peval(Q2,x,p)
        if a2==0:
            if a1: d.setdefault((-a0)*pow(a1,p-2,p)%p,set()).add(x)
            continue
        disc=(a1*a1-4*a0*a2)%p
        if disc==0:
            d.setdefault((-a1)*pow(2*a2%p,p-2,p)%p,set()).add(x)
        elif disc in SQ:
            sd=SQ[disc]; ia=pow(2*a2%p,p-2,p)
            d.setdefault((-a1+sd)*ia%p,set()).add(x)
            d.setdefault((-a1-sd)*ia%p,set()).add(x)
    return d

def run(p,out,rng,budget):
    SQ=tables(p)
    t0=time.time(); nobj=0; Tdist={}; best=0; bestrec=None; ov_viol=0; ov_obs={}
    unions=[]
    while time.time()-t0<budget:
        o=build(p,rng,SQ)
        if o is None: continue
        f,g,h,k,L,ell,Q0,Q1,Q2,S0,S2=o
        nobj+=1
        d=tally(Q0,Q1,Q2,p,SQ)
        sup={z:s for z,s in d.items() if len(s)==7}
        T=len(sup)+1   # +1 for z = infinity (Q_2 splits by construction)
        Tdist[T]=Tdist.get(T,0)+1
        if T>=3:
            supp=dict(sup); supp['inf']=set(S2)
            U=set()
            for s in supp.values(): U|=s
            unions.append((T,len(U)))
            keys=list(supp)
            e={}
            for i in range(len(keys)):
                for j in range(i+1,len(keys)):
                    e[(i,j)]=len(supp[keys[i]]&supp[keys[j]])
            def ee(a,b): return e[(min(a,b),max(a,b))]
            worst=0
            for a in range(len(keys)):
                for b in range(len(keys)):
                    for c in range(len(keys)):
                        if len({a,b,c})==3: worst=max(worst,ee(a,b)+ee(a,c))
            ov_obs[worst]=ov_obs.get(worst,0)+1
            if worst>4: ov_viol+=1
            if T>best:
                best=T
                bestrec=(T,len(U),worst,sorted(e.values()),
                         [f,g,h,k,L],[Q0,Q1,Q2],sorted(S0),sorted(S2),sorted(sup))
    out.append("q=%d bespoke objects (Q_0 AND Q_2 both prescribed split, EXACT) = %d in %.0f s"
               %(p,nobj,time.time()-t0))
    out.append("q=%d T distribution over P^1 (F_q-split members) = %s"%(p,sorted(Tdist.items())))
    out.append("q=%d T>=3 objects: |union of supported root sets| samples = %s"
               %(p,sorted(set(unions))))
    out.append("q=%d (OV4) worst-case e(k,i)+e(k,j) over T>=3 objects: histogram %s ; violations of <=4 : %d"
               %(p,sorted(ov_obs.items()),ov_viol))
    if bestrec:
        T,U,worst,ev,B,Q,S0,S2,sl=bestrec
        out.append("q=%d RECORD T=%d |union|=%d OV4worst=%d pairwise-overlaps=%s"
                   %(p,T,U,worst,ev))
        out.append("q=%d RECORD f=%s g=%s h=%s k=%s L=%s"%(p,B[0],B[1],B[2],B[3],B[4]))
        out.append("q=%d RECORD Q0=%s Q1=%s Q2=%s"%(p,Q[0],Q[1],Q[2]))
        out.append("q=%d RECORD S0=%s S_inf=%s finite supported slopes=%s"%(p,S0,S2,sl))
    return bestrec

def main():
    rng=random.Random(99371)
    out=["","=== RUN d3_push %s ==="%time.strftime("%Y-%m-%dT%H:%M:%S")]
    for p in (97,193):
        run(p,out,rng,125)
    with open("notes/pilots_20260811/r37_third_solve/d3_results.txt","a") as fh:
        fh.write("\n".join(out)+"\n")
    print("\n".join(out))

main()
