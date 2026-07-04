import cmath, itertools, math
from collections import Counter
p=17; N=8; L=2
# omega of order 16: 3 has order 16 mod 17
omega=3; roots=[pow(omega,2*a+1,p) for a in range(N)]
def phi(d):
    return tuple(sum(di*pow(r,2*l-1,p) for di,r in zip(d,roots))%p for l in range(1,L+1))
def F(lam,doms):
    pr=1+0j
    for D,r in zip(doms,roots):
        a=sum(lam[l-1]*pow(r,2*l-1,p) for l in range(1,L+1))%p
        pr*=sum(cmath.exp(2j*math.pi*(a*u%p)/p) for u in D)/len(D)
    return pr
ok=True
for name,doms in [("signed",[[-1,1]]*N),("ternary",[[-2,0,2]]*N)]:
    U=math.prod(len(D) for D in doms)
    vecs=list(itertools.product(*doms))
    ic=Counter(phi(d) for d in vecs)
    B=ic[(0,)*L]; rho=(p**L)*B/U
    Fv={lam:F(lam,doms) for lam in itertools.product(range(p),repeat=L)}
    rhoF=sum(Fv.values())
    ok &= abs(rhoF-rho)<1e-8
    for m in (1,2):
        J=sum(abs(v)**(2*m) for lam,v in Fv.items() if any(lam))
        eta=math.log(1+(p**(L*(1-1/(2*m))))*(J**(1/(2*m))),p)
        ok &= rho <= p**eta+1e-9
    print(f"{name}: B={B} rho={rho:.6f} fourier={rhoF.real:.6f} holder-ok")
print("D3 reduction algebra:", "PASS" if ok else "FAIL")
