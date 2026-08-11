"""m=1 EXHAUSTIVE realizability test for (SAT3): T = rho+2 = 5.

Profile (SAT1) at m=1:  rho = 4m-1 = 3, N = 16m = 16, R = N/2 = 8, k = 8,
r = rho = 3 (strict row r = R/2-1), A = R+1-2rho = 3, e = m = 1, s = 0,
delta = rho-3e = 0.  (SAT2) forces O = 0, so every supported slope has a
FULL degree-rho split locator, and d_x <= e = 1 forces the T locator sets
to be PAIRWISE DISJOINT.

Reduction used (derived in-session, see REPORT D1):
  generic corank 1  =>  ker M(Z) = <Q_Z>,  Q_Z = Q_0 + Z Q_1  (deg_Z <= e = 1)
  supported slope gamma  <=>  Q_gamma splits into rho distinct D-roots
  => the supported locators are the totally-split members of a PENCIL of
     degree-rho polynomials, i.e. a LINE in P^rho = P^3.
Since T >= 2 forces two disjoint split triples, enumerating all unordered
pairs of disjoint triples of D enumerates EVERY candidate pencil.  For a
pair (S1,S2) the member through x is lam(x) = -P_{S1}(x)/P_{S2}(x), so the
whole fibre structure is the multiset {lam(x) : x in D} and
   T = #{lam in P^1 : multiplicity exactly rho}.
Because sum of multiplicities = |D| = 16, T <= floor(16/3) = 5 = rho+2.

Stdlib only.
"""
import sys
from itertools import combinations

INF = "INF"


def inv_table(q):
    t = [0] * q
    for a in range(1, q):
        t[a] = pow(a, q - 2, q)
    return t


def poly_from_roots(roots, q):
    c = [1]
    for r in roots:
        nc = [0] * (len(c) + 1)
        for i, ci in enumerate(c):
            nc[i] = (nc[i] - r * ci) % q
            nc[i + 1] = (nc[i + 1] + ci) % q
        c = nc
    return c


def peval(c, x, q):
    v = 0
    for co in reversed(c):
        v = (v * x + co) % q
    return v


def find_domain(q, size):
    """multiplicative subgroup of order `size` (needs size | q-1)"""
    assert (q - 1) % size == 0
    g = None
    for cand in range(2, q):
        seen, x, ok = set(), 1, True
        for _ in range(q - 1):
            x = x * cand % q
            if x in seen:
                ok = False
                break
            seen.add(x)
        if ok and len(seen) == q - 1:
            g = cand
            break
    h = pow(g, (q - 1) // size, q)
    D, x = [], 1
    for _ in range(size):
        D.append(x)
        x = x * h % q
    return sorted(D)


def scan(q, D, rho, label, out):
    n = len(D)
    inv = inv_table(q)
    idx = {x: i for i, x in enumerate(D)}
    triples = list(combinations(range(n), rho))
    Pv = []
    for t in triples:
        c = poly_from_roots([D[i] for i in t], q)
        Pv.append([peval(c, x, q) for x in D])
    tri_set = [set(t) for t in triples]

    best = 0
    hits = {}
    npairs = 0
    for i1, t1 in enumerate(triples):
        s1 = tri_set[i1]
        P1 = Pv[i1]
        for i2 in range(i1 + 1, len(triples)):
            if tri_set[i2] & s1:
                continue
            npairs += 1
            P2 = Pv[i2]
            vals = []
            for x in range(n):
                if x in s1:
                    vals.append(0)
                elif x in tri_set[i2]:
                    vals.append(INF)
                else:
                    vals.append((-P1[x] * inv[P2[x]]) % q)
            cnt = {}
            for v in vals:
                cnt[v] = cnt.get(v, 0) + 1
            T = sum(1 for v, c in cnt.items() if c == rho)
            if T > best:
                best = T
                hits = {}
            if T == best and T >= 4 and len(hits) < 40:
                hits[(t1, triples[i2])] = sorted(
                    (v for v, c in cnt.items() if c == rho), key=str)
    out(f"[{label}] q={q} |D|={n} rho={rho} disjoint-pairs={npairs} "
        f"MAX T = {best}   (rho+1={rho+1}, rho+2={rho+2})")
    return best, hits


def main():
    lines = []

    def out(s):
        print(s)
        lines.append(s)

    out("=== D1/D3: m=1 EXHAUSTIVE (SAT3) realizability scan ===")
    out("profile: rho=3 N=16 R=8 k=8 r=3 A=3 e=1 s=0 delta=0 ; target T=rho+2=5")
    out("cap from sum_x d_x <= N*e = 16 with d_x<=1 and u_gamma=rho=3:"
        " T <= floor(16/3) = 5  (so T=5 needs 15 of 16 points covered)")
    out("")
    cells = []
    for q in (17, 97, 113, 193, 241, 257):
        try:
            D = find_domain(q, 16)
        except AssertionError:
            continue
        cells.append((q, D, f"mu16/F_{q}"))
    # second domain family: an affine shift of mu16 (different D, same q)
    for q in (97, 193):
        D0 = find_domain(q, 16)
        D = sorted(set((x + 1) % q for x in D0))
        if len(D) == 16 and 0 not in D:
            cells.append((q, D, f"mu16+1/F_{q}"))
    results = {}
    for q, D, lab in cells:
        b, h = scan(q, D, 3, lab, out)
        results[lab] = (b, h)
        for k_, v in list(h.items())[:3]:
            out(f"    witness S1={[D[i] for i in k_[0]]} "
                f"S2={[D[i] for i in k_[1]]} split-slopes={v}")
    out("")
    out("=== SUMMARY (m=1) ===")
    for lab, (b, h) in results.items():
        out(f"  {lab}: max T = {b}")
    mx = max(b for b, _ in results.values())
    out(f"  GLOBAL max T over all cells = {mx}")
    out(f"  (SAT3) needs T = 5.  REALIZED at m=1? {'YES' if mx >= 5 else 'NO'}")
    out(f"  T = rho+1 = 4 realized in the A=3 branch? {'YES' if mx >= 4 else 'NO'}")
    with open(sys.argv[1], "w") as f:
        f.write("\n".join(lines) + "\n")


main()
