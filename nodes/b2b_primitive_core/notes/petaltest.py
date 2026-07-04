# validate Lemma 13: dim K_{I,d} <= d-ell+1 and r_{I,d} >= ell, on toy sunflowers.
def polmulmod(a,b,mod,q):
    r=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b): r[i+j]=(r[i+j]+ai*bj)%q
    return polmod(r,mod,q)
def polmod(a,mod,q):
    a=a[:]; dm=len(mod)-1
    inv=pow(mod[-1],q-2,q)
    for i in range(len(a)-1,dm-1,-1):
        c=(a[i]*inv)%q
        if c:
            for j in range(dm+1): a[i-dm+j]=(a[i-dm+j]-c*mod[j])%q
    while len(a)>dm: a.pop()
    while len(a)<dm: a.append(0)
    return a
def locator(pts,q):
    p=[1]
    for x in pts:
        p=polmulmod(p,[(-x)%q,1],[0]*99+[1] if False else None,q) if False else naive_mul(p,[(-x)%q,1],q)
    return p
def naive_mul(a,b,q):
    r=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b): r[i+j]=(r[i+j]+ai*bj)%q
    return r
def crt(residues,mods,q,total_deg):
    # reconstruct G deg<total_deg with G = residues[i] mod mods[i]; mods coprime
    # standard CRT via Bezout; do incremental
    G=[0]; M=[1]
    for res,mod in zip(residues,mods):
        # solve G' = G mod M, G'=res mod mod ; G'=G + M*t, choose t so (G+M t)=res mod mod
        # t = (res-G)*inv(M) mod mod
        diff=poladd(res,[(-x)%q for x in G],q)
        Mmod=polmod(M[:],mod,q)
        Minv=polinvmod(Mmod,mod,q)
        t=polmod(naive_mul(diff,Minv,q),mod,q)
        G=poladd(G,naive_mul(M,t,q),q)
        M=naive_mul(M,mod,q)
    G=G[:total_deg]+[0]*(total_deg-len(G))
    return [x%q for x in G][:total_deg]
def poladd(a,b,q):
    r=[0]*max(len(a),len(b))
    for i,x in enumerate(a): r[i]=(r[i]+x)%q
    for i,x in enumerate(b): r[i]=(r[i]+x)%q
    return r
def polinvmod(a,mod,q):
    # extended euclid for polynomials over F_q, invert a mod mod
    def norm(p):
        while len(p)>1 and p[-1]%q==0: p.pop()
        return p
    r0,r1=mod[:],norm(a[:]); s0,s1=[0],[1]
    while any(x%q for x in r1):
        # divide r0 by r1
        qd,rem=poldivmod(r0,r1,q)
        r0,r1=r1,rem
        s0,s1=s1,poladd(s0,[(-x)%q for x in naive_mul(qd,s1,q)],q)
    inv=pow(r0[-1] if r0 else 1,q-2,q)
    return polmod([(x*inv)%q for x in s0],mod,q)
def poldivmod(a,b,q):
    a=a[:]; b=b[:]
    while len(b)>1 and b[-1]%q==0: b.pop()
    db=len(b)-1; inv=pow(b[-1],q-2,q); quo=[0]*max(1,len(a)-db)
    for i in range(len(a)-1,db-1,-1):
        c=(a[i]*inv)%q
        quo[i-db]=c
        for j in range(db+1): a[i-db+j]=(a[i-db+j]-c*b[j])%q
    while len(a)>db: a.pop()
    return quo,a
def rank_mod(M,q):
    M=[row[:] for row in M]; rows=len(M); cols=len(M[0]) if rows else 0; r=0
    for c in range(cols):
        piv=None
        for i in range(r,rows):
            if M[i][c]%q: piv=i;break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        inv=pow(M[r][c],q-2,q)
        M[r]=[(x*inv)%q for x in M[r]]
        for i in range(rows):
            if i!=r and M[i][c]%q:
                f=M[i][c]
                M[i]=[(M[i][j]-f*M[r][j])%q for j in range(cols)]
        r+=1
    return r

def test(q,petals,c,d):
    t=len(petals); ell=len(petals[0])
    mods=[locator(P,q) for P in petals]      # L_{T_i}, degree ell
    tell=t*ell
    # R_{I,d}: F(deg<=d) -> G deg<tell with G = c_i F mod L_{T_i}; then pi_{>d}
    # build matrix cols = basis 1..X^d, rows = coeffs deg d+1..tell-1
    cols=[]
    for e in range(d+1):
        F=[0]*(e)+[1]
        residues=[polmod(naive_mul([c[i]],F,q),mods[i],q) for i in range(t)]
        G=crt(residues,mods,q,tell)
        col=[G[j] for j in range(d+1,tell)]
        cols.append(col)
    # matrix rows x cols
    R=len(cols[0]) if cols and cols[0] else 0
    Mat=[[cols[cc][rr] for cc in range(len(cols))] for rr in range(R)]
    r=rank_mod(Mat,q) if R>0 else 0
    dimK=(d+1)-r
    return dict(t=t,ell=ell,d=d,e=d-ell,r_Id=r,dimK=dimK,bound_e1=d-ell+1,
               lem13_ok=(dimK<=d-ell+1),floor_ok=(r>=ell))

q=13
for d in [2,3,4]:
    print(test(q,[[1,2],[3,4],[5,6]],[1,2,3],d))
q=101
for d in [3,4,5,6]:
    print(test(q,[[1,2,3],[4,5,6],[7,8,9]],[1,2,3],d))
