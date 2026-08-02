# Replay of background/nodes/xr_nondeep_tangent_supportwise_payment/refutation.md
# read through the xr_pencil_cascade lens: is the cascade pair "paid"?
from itertools import combinations
p = 17
D = [1,2,4,8,16,15,13,9]
n = len(D); K = 2; A = 3
u = [0,0,0,0,0,0,1,1]
v = [0,0,0,0,0,0,1,2]

def interp_deg_lt(vals, idx, deg):
    """return coeffs of unique poly of degree<deg through (D[i],vals[i]) for i in idx,
       or None if |idx|>deg and no consistent poly."""
    # solve Vandermonde least system exactly over F_p by Lagrange on first deg points
    pts = [(D[i], vals[i]) for i in idx]
    if len(pts) < deg:
        return "underdet"
    base = pts[:deg]
    # Lagrange interpolation on base
    coeffs = [0]*deg
    for j,(xj,yj) in enumerate(base):
        # basis poly
        num = [1]
        den = 1
        for m,(xm,_) in enumerate(base):
            if m==j: continue
            num = [ (num[i-1] if i>0 else 0) - xm*(num[i] if i<len(num) else 0) for i in range(len(num)+1)]
            num = [c % p for c in num]
            den = den*(xj-xm) % p
        inv = pow(den, p-2, p)
        for i,c in enumerate(num):
            if i < deg:
                coeffs[i] = (coeffs[i] + yj*c%p*inv) % p
    def ev(x):
        return sum(coeffs[i]*pow(x,i,p) for i in range(deg)) % p
    for (xx,yy) in pts:
        if ev(xx) != yy % p:
            return None
    return coeffs

def ev(coeffs, x):
    return sum(coeffs[i]*pow(x,i,p) for i in range(len(coeffs))) % p

supports = list(combinations(range(n), A))
bad = {}
for z in range(p):
    w = [(u[i] + z*v[i]) % p for i in range(n)]
    for S in supports:
        c = interp_deg_lt(w, S, K)
        if c is None:
            continue
        # joint explanation on S?
        c0 = interp_deg_lt(u, S, K); c1 = interp_deg_lt(v, S, K)
        joint = (c0 is not None) and (c1 is not None)
        if not joint:
            bad.setdefault(z, []).append((S, tuple(c)))
print("bad slopes:", sorted(bad))
print("count:", len(bad), " slot r+1 = n-A+1 =", n-A+1)
# lex-first support per slope
for z in sorted(bad):
    S, c = bad[z][0]
    print(f"  z={z:2d} lexfirst support {S} explaining codeword coeffs {c}  recovered-line(c==0)? {c==(0,0)}")
# maximal joint core: where u,v both equal (0,0) pencil
T = [i for i in range(n) if u[i]%p or v[i]%p]
print("max joint core = complement of T; T =", T, "|T| =", len(T), " n-A =", n-A)
# pairwise cores between lex-first selected supports
sel = {z: bad[z][0][0] for z in sorted(bad)}
zs = sorted(sel)
print("pairwise cores of lex-first selected supports (>= A-1 = %d flagged):" % (A-1))
for a,b in combinations(zs,2):
    c = len(set(sel[a]) & set(sel[b]))
    if c >= A-1:
        print(f"   z={a},z={b}: core {c}  supports {sel[a]} {sel[b]}")

print()
print("=== PENCIL DECOMPOSITION ===")
# forced pencil from slopes z1,z2 with codewords c1,c2 on a shared core
def pencil_from(z1,c1,z2,c2):
    inv = pow((z1-z2) % p, p-2, p)
    g = tuple(((c1[i]-c2[i])*inv) % p for i in range(K))
    f = tuple((c1[i] - z1*g[i]) % p for i in range(K))
    return f,g
# enumerate all (pencil -> set of slopes it explains) using every bad slope's every bad support
from collections import defaultdict
pen = defaultdict(set)
for z in sorted(bad):
    for S,c in bad[z]:
        # slope z is a recovered-line slope for pencil (f,g) iff c = f + z g
        pass
# build candidate pencils from all distinct-slope pairs sharing core >= A-1
cands = set()
for a,b in combinations(sorted(bad),2):
    for Sa,ca in bad[a]:
        for Sb,cb in bad[b]:
            if len(set(Sa)&set(Sb)) >= A-1:
                cands.add(pencil_from(a,ca,b,cb))
# also the global zero pencil
cands.add(((0,0),(0,0)))
for (f,g) in sorted(cands):
    T2 = [i for i in range(n) if ev(f,D[i]) != u[i]%p or ev(g,D[i]) != v[i]%p]
    slopes = []
    for z in sorted(bad):
        for S,c in bad[z]:
            if all((f[i] + z*g[i]) % p == c[i] for i in range(K)):
                slopes.append(z); break
    if slopes:
        print(f" pencil f={f} g={g}  core=n-|T|={n-len(T2)}  |T|={len(T2)}  recovered-line slopes {slopes} (count {len(slopes)} <= |T|={len(T2)})")
