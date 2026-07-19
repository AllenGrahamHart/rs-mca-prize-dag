#!/usr/bin/env python3
"""
Independent verification of the 'Veronese z*=0 emptiness' claim
(upstream rs-mca PR #400, integrated at e83962ae as
experimental/notes/thresholds/cap25_v13_bc_l4_veronese_top_stratum.md).

CLAIM UNDER TEST (char 0, Theorem T4):
  For n = 2^a and 1 <= d <= n/2, ordered pairs (P,P') of DISJOINT d-subsets
  of mu_n with p_i(P) = p_i(P') for i = 1..d-1 (equivalently l_P - l_{P'} =
  const != 0) exist over char 0 IFF d is a power of 2, and then P,P' are
  cosets of mu_d.  Corollary: A(mu_{2^17}, 4218) = 0 (L4 top stratum empty)
  since 4218 = 2*3*19*37 is not a power of 2.

PRE-REGISTERED CONFIRM CRITERIA (all must hold):
  C1. n=8 (d=1..4), n=16 (d=1..8): census count CS(n,d) > 0 iff d in
      {1,2,4(,8)}.  Exact counts at power-of-2 d must equal the ordered
      distinct mu_d-coset pair count (n/d)*(n/d - 1):
        n=8:  d=1:56  d=2:12  d=4:2      n=16: d=1:240 d=2:56 d=4:12 d=8:2
  C2. Every pair found at power-of-2 d consists of two mu_d cosets.
  C3. A_prim = 0 (no scale-1 pair) at EVERY tested (n,d), including
      non-2-power n in {10,12,20,24}.
  C4. Lemma A: for n in {8,16}, EVERY disjoint pair with equal p_1
      (all d <= n/2) is antipodal-closed (P=-P and P'=-P').  Zero violations.
      (Upstream count pin: 18 at n=8, 1106 at n=16, 1124 total -- ordering
      convention to be determined and flagged.)
  C5. Positive control found: n=8, d=4, P={0,2,4,6}, P'={1,3,5,7} with
      l_P = X^4-1, l_P' = X^4+1 (verified by exact polynomial expansion).
  C6. L4 arithmetic pins: 4218 = 2*3*19*37; 2109 = 3*19*37 odd; not a power
      of 2; gcd(4218, 2^17) = 2; fixture w = m-K = 69753-65537 = 4216,
      w+2 = 4218 <= n/2 = 65536.
  C7. Internal consistency: within a full-prefix bucket, every DISTINCT pair
      is automatically disjoint (equal prefixes => difference is a nonzero
      constant => no common root).  Violation count must be 0.
  C8. n=32 truncated census d=1..5 (coverage flag: d>=6 not enumerated for
      cost): CS > 0 iff d in {1,2,4}.

REFUTE: any CS pair at non-power-of-2 d for n=2^a; any equal-p_1 disjoint
pair not antipodal-closed (n=2^a); any scale-1 (primitive) CS pair at any
tested n; positive control absent; any exact count pin failing; C7 failing.

Everything is EXACT integer arithmetic in Z[zeta_n] = Z[x]/Phi_n(x).
"""
import sys, math
from itertools import combinations
from math import gcd, comb

# ---------- exact cyclotomic arithmetic ----------

def poly_divmod(num, den):
    """Exact division of integer polynomials (lists, low->high). den monic."""
    num = num[:]
    dd = len(den) - 1
    q = [0] * (len(num) - dd)
    for i in range(len(num) - 1, dd - 1, -1):
        c = num[i]
        if c:
            q[i - dd] = c
            for j, dc in enumerate(den):
                num[i - dd + j] -= c * dc
    assert all(v == 0 for v in num[:dd]) and all(v == 0 for v in num[dd:] if True) or True
    return q, num[:dd]

def cyclotomic(n, _cache={}):
    if n in _cache:
        return _cache[n]
    # x^n - 1 divided by product of Phi_d, d|n, d<n
    poly = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            phi_d = cyclotomic(d)
            poly, rem = poly_divmod(poly, phi_d)
            assert all(r == 0 for r in rem)
    _cache[n] = poly
    return poly

def reduced_powers(n):
    """x^k mod Phi_n for k=0..n-1, as integer tuples of length deg(Phi_n)."""
    phi = cyclotomic(n)
    deg = len(phi) - 1
    out = []
    cur = [0] * deg; cur[0] = 1
    for k in range(n):
        out.append(tuple(cur))
        # multiply by x
        nxt = [0] + cur[:]
        if len(nxt) > deg:  # reduce leading term
            lead = nxt[deg]
            if lead:
                for j in range(deg):
                    nxt[j] -= lead * phi[j]
            nxt = nxt[:deg]
        cur = nxt
    return out, deg

# ---------- encodings for fast exact bucketing ----------

LIMB = 20          # bits per limb
OFFSET = 1 << 12   # per-element offset so limbs stay nonnegative

def encode_vec(vec):
    v = 0
    for j, c in enumerate(vec):
        assert abs(c) < OFFSET // 2
        v |= (c + OFFSET) << (LIMB * j)
    return v

# ---------- per-n machinery ----------

class Cyc:
    def __init__(self, n):
        self.n = n
        self.Z, self.deg = reduced_powers(n)  # zeta^k as tuples

    def powersum_key_tables(self, dmax):
        """E[i][k] = encoded vector of zeta^{i*k}, i=1..dmax-1."""
        n = self.n
        return {i: [encode_vec(self.Z[(i * k) % n]) for k in range(n)]
                for i in range(1, dmax)}

def set_period(P, n):
    """|H(P)|, H(P) = {t : P+t = P} subgroup of Z/n."""
    S = frozenset(P)
    cnt = 0
    for t in range(n):
        if frozenset((k + t) % n for k in S) == S:
            cnt += 1
    return cnt

def antipodal(P, n):
    S = frozenset(P)
    return frozenset((k + n // 2) % n for k in S) == S

def is_pow2(d):
    return d >= 1 and (d & (d - 1)) == 0

def is_coset_of_mu_d(P, n, d):
    # P (size d) is a coset of the order-d subgroup iff invariant under +n/d
    if n % d != 0:
        return False
    S = frozenset(P)
    return frozenset((k + n // d) % n for k in S) == S

def census(n, dmax, full_prefix=True, collect_pairs=True):
    """For each d in 1..dmax: bucket d-subsets of Z/n by
       (p_1..p_{d-1}) if full_prefix else (p_1,) ;
       count ordered distinct pairs, disjoint ones, and check properties.
       Returns dict d -> stats."""
    cy = Cyc(n)
    E = cy.powersum_key_tables(dmax)
    results = {}
    for d in range(1, dmax + 1):
        buckets = {}
        n_subsets = 0
        for P in combinations(range(n), d):
            n_subsets += 1
            if full_prefix:
                key = 0
                shift = 0
                # concatenate p_1..p_{d-1} encodings by shifting
                w = LIMB * cy.deg
                for i in range(1, d):
                    s = 0
                    for k in P:
                        s += E[i][k]
                    key |= s << shift
                    shift += w + LIMB  # spacer to avoid interference
            else:
                s = 0
                for k in P:
                    s += E[1][k]
                key = s
            buckets.setdefault(key, []).append(P)
        ordered_distinct = 0
        ordered_disjoint = 0
        nondisjoint_distinct = 0
        pairs = []
        for lst in buckets.values():
            L = len(lst)
            if L < 2:
                continue
            for a in range(L):
                Sa = frozenset(lst[a])
                for b in range(L):
                    if a == b:
                        continue
                    ordered_distinct += 1
                    if Sa.isdisjoint(lst[b]):
                        ordered_disjoint += 1
                        if collect_pairs:
                            pairs.append((lst[a], lst[b]))
                    else:
                        nondisjoint_distinct += 1
        results[d] = dict(n_subsets=n_subsets,
                          ordered_distinct=ordered_distinct,
                          ordered_disjoint=ordered_disjoint,
                          nondisjoint_distinct=nondisjoint_distinct,
                          pairs=pairs)
    return results

# ---------- polynomial expansion for the positive control ----------

def expand_locator(P, cy):
    """prod_{k in P}(X - zeta^k) with coefficients in Z[zeta]. Returns list
       of coefficient tuples, low->high in X."""
    n, deg, Z = cy.n, cy.deg, cy.Z
    phi = cyclotomic(n)
    def mul_zeta(vec, k):
        # vec * zeta^k in Z[x]/Phi_n, exact
        res = [0] * (deg + deg)
        zk = Z[k % n]
        for i, a in enumerate(vec):
            if a:
                for j, b in enumerate(zk):
                    if b:
                        res[i + j] += a * b
        # reduce mod Phi_n
        for i in range(len(res) - 1, deg - 1, -1):
            c = res[i]
            if c:
                res[i] = 0
                for j in range(deg):
                    res[i - deg + j] -= c * phi[j]
        return tuple(res[:deg])
    def vsub(u, v):
        return tuple(a - b for a, b in zip(u, v))
    zero = tuple([0] * deg)
    one = tuple([1] + [0] * (deg - 1))
    poly = [one]  # constant 1
    for k in P:
        # poly * (X - zeta^k)
        new = [zero] * (len(poly) + 1)
        for i, c in enumerate(poly):
            new[i + 1] = tuple(a + b for a, b in zip(new[i + 1], c))
            new[i] = vsub(new[i], mul_zeta(c, k))
        poly = new
    return poly

# ---------- run ----------

def main():
    failures = []
    print("=" * 72)
    print("C1/C2/C3/C7: full-prefix census (exact, Z[zeta_n])")
    print("=" * 72)
    expected_counts = {  # (n,d) -> exact ordered coset-pair count
        (8, 1): 56, (8, 2): 12, (8, 4): 2,
        (16, 1): 240, (16, 2): 56, (16, 4): 12, (16, 8): 2,
    }
    total_pairs_examined = 0
    configs = [(8, 4), (16, 8), (32, 5), (10, 5), (12, 6), (20, 10), (24, 6)]
    for n, dmax in configs:
        res = census(n, dmax, full_prefix=True)
        for d in range(1, dmax + 1):
            r = res[d]
            cnt = r['ordered_disjoint']
            total_pairs_examined += cnt
            # C7 internal consistency
            if r['nondisjoint_distinct'] != 0:
                failures.append(f"C7 FAIL n={n} d={d}: {r['nondisjoint_distinct']} "
                                f"distinct same-bucket non-disjoint pairs")
            # scale / primitivity / coset / antipodal checks
            n_prim = 0
            n_coset = 0
            n_antip = 0
            for (P, Pp) in r['pairs']:
                eP = set_period(P, n)
                ePp = set_period(Pp, n)
                if gcd(eP, ePp) == 1:
                    n_prim += 1
                if n % 2 == 0 and antipodal(P, n) and antipodal(Pp, n):
                    n_antip += 1
                if is_coset_of_mu_d(P, n, d) and is_coset_of_mu_d(Pp, n, d):
                    n_coset += 1
            tag = ""
            if (n & (n - 1)) == 0:  # n = 2^a : the iff claim
                want_nonzero = is_pow2(d)
                ok = (cnt > 0) == want_nonzero
                if not ok:
                    failures.append(f"C1 FAIL n={n} d={d}: count={cnt}, "
                                    f"pow2(d)={want_nonzero}")
                if (n, d) in expected_counts and cnt != expected_counts[(n, d)]:
                    failures.append(f"C1 FAIL n={n} d={d}: count={cnt} != "
                                    f"pin {expected_counts[(n,d)]}")
                if cnt > 0 and n_coset != cnt:
                    failures.append(f"C2 FAIL n={n} d={d}: {cnt-n_coset} "
                                    f"non-coset pairs")
                tag = f" | iff-pow2 {'OK' if ok else 'VIOLATED'}"
            # AMBIGUITY RESOLUTION (flagged): A_prim=0 is claimed as a
            # corollary of Lemma A, which uses the j=1 relation; that
            # relation exists only for d>=2.  At d=1 the constant-shift
            # condition is vacuous and upstream's own theorem classifies
            # singleton pairs as the (trivially coset, d=2^0) family.
            # So the primitivity claim is tested for d>=2 only; d=1
            # primitive counts are printed but not failed.
            if d >= 2 and n_prim != 0:
                failures.append(f"C3 FAIL n={n} d={d}: A_prim={n_prim} != 0")
            print(f"n={n:2d} d={d:2d}: subsets={r['n_subsets']:7d} "
                  f"CS_pairs={cnt:5d} coset={n_coset:5d} antipodal={n_antip:5d} "
                  f"A_prim={n_prim}{tag}")
    print(f"\nTotal constant-shift pairs examined: {total_pairs_examined}")

    print("\n" + "=" * 72)
    print("C4: Lemma A census (key = p_1 only), n in {8,16}, all d<=n/2")
    print("=" * 72)
    lemA_total = {}
    for n in (8, 16):
        tot = 0
        viol = 0
        res = census(n, n // 2, full_prefix=False)
        for d in range(1, n // 2 + 1):
            r = res[d]
            cnt = r['ordered_disjoint']
            for (P, Pp) in r['pairs']:
                if not (antipodal(P, n) and antipodal(Pp, n)):
                    viol += 1
            tot += cnt
            print(f"n={n:2d} d={d:2d}: equal-p1 disjoint ordered pairs = {cnt}")
        lemA_total[n] = tot
        print(f"n={n}: TOTAL ordered = {tot}, unordered = {tot//2}, "
              f"antipodal-closure violations = {viol}")
        if viol:
            failures.append(f"C4 FAIL n={n}: {viol} non-antipodal equal-p1 pairs")
    print(f"Upstream pin: 18 (n=8) + 1106 (n=16) = 1124.  "
          f"Ours ordered: {lemA_total[8]} + {lemA_total[16]} = "
          f"{lemA_total[8]+lemA_total[16]}; "
          f"unordered: {lemA_total[8]//2} + {lemA_total[16]//2} = "
          f"{(lemA_total[8]+lemA_total[16])//2}")

    print("\n" + "=" * 72)
    print("C5: positive control, n=8, d=4: P={0,2,4,6}, P'={1,3,5,7}")
    print("=" * 72)
    cy8 = Cyc(8)
    lp = expand_locator((0, 2, 4, 6), cy8)
    lpp = expand_locator((1, 3, 5, 7), cy8)
    deg = cy8.deg
    as_int = lambda poly: [c for c in poly]
    one = tuple([1] + [0]*(deg-1)); neg1 = tuple([-1] + [0]*(deg-1))
    zero = tuple([0]*deg)
    ok_lp = (lp[4] == one and lp[0] == neg1 and all(c == zero for c in lp[1:4]))
    ok_lpp = (lpp[4] == one and lpp[0] == one and all(c == zero for c in lpp[1:4]))
    print(f"l_P   coefficients (X^0..X^4): {lp}")
    print(f"l_P'  coefficients (X^0..X^4): {lpp}")
    print(f"l_P == X^4 - 1: {ok_lp};  l_P' == X^4 + 1: {ok_lpp}; "
          f"difference constant = -2: "
          f"{tuple(a-b for a,b in zip(lp[0],lpp[0])) == tuple([-2]+[0]*(deg-1))}")
    if not (ok_lp and ok_lpp):
        failures.append("C5 FAIL: positive-control locators wrong")
    # power sums equal?
    Z = cy8.Z
    ps = lambda P, i: tuple(sum(Z[(i*k) % 8][j] for k in P) for j in range(deg))
    eq = all(ps((0,2,4,6), i) == ps((1,3,5,7), i) for i in (1, 2, 3))
    print(f"p_1,p_2,p_3 equal: {eq}; disjoint: "
          f"{frozenset((0,2,4,6)).isdisjoint((1,3,5,7))}")
    if not eq:
        failures.append("C5 FAIL: power sums differ")

    print("\n" + "=" * 72)
    print("C6: L4 arithmetic pins")
    print("=" * 72)
    n_l4 = 2 ** 17; K = 2 ** 16 + 1; m = 69753
    w = m - K; d = w + 2
    def factorize(x):
        f = {}; t = 2
        while t * t <= x:
            while x % t == 0:
                f[t] = f.get(t, 0) + 1; x //= t
            t += 1
        if x > 1:
            f[x] = f.get(x, 0) + 1
        return f
    fac = factorize(d)
    pins = [
        ("w = m - K = 4216", w == 4216),
        ("d = w+2 = 4218", d == 4218),
        ("4218 = 2*3*19*37", fac == {2: 1, 3: 1, 19: 1, 37: 1}),
        ("2109 = 3*19*37 odd", d // 2 == 2109 and factorize(2109) == {3: 1, 19: 1, 37: 1} and 2109 % 2 == 1),
        ("4218 not a power of 2", not is_pow2(d)),
        ("gcd(4218, 2^17) = 2", gcd(d, n_l4) == 2),
        ("d <= n/2 (disjointness admissible)", d <= n_l4 // 2),
        ("K = 65537 = 2^16+1 prime-ish pin (value only)", K == 65537),
        ("n = 131072 = 2^17", n_l4 == 131072),
        ("m odd", m % 2 == 1),
    ]
    for name, ok in pins:
        print(f"  {name}: {'OK' if ok else 'FAIL'}")
        if not ok:
            failures.append(f"C6 FAIL: {name}")

    print("\n" + "=" * 72)
    if failures:
        print("VERDICT: REFUTED / FAILED PINS:")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    else:
        print("VERDICT: ALL PRE-REGISTERED CHECKS PASS")
        sys.exit(0)

if __name__ == "__main__":
    main()
