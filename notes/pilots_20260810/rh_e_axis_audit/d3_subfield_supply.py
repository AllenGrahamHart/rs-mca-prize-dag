"""D3 - THE SUBFIELD SUPPLY QUESTION, measured exactly.

F_LMAX(n_s,K,q,a) = max_U #{c in C : agreement(U,c) >= a}
                  = max over cosets V of F[X]_{<K} in F[X]_{<n_s} of
                    #{f in V : f has >= a roots in D},
the exact max list profile at the scaled rate-1/2 RS row -- the same
object the round-29 list_profile_bound pilot measured (F_LMAX(8,4,5) = 7
at q = 17, 41, 97, reported there as a "q-INDEPENDENT ABSOLUTE
constant").  Every field in that measurement, and in every rounds-27..29
experiment in the repo, is PRIME; the banked field layer
notes/pilots_20260810/ssparse_endpoints/ffield.py cannot represent an
extension field at all (it inverts by pow(x,q-2,q)).  This script uses
the generic layer ffq.GF written for this pilot.

EXACT ALGORITHM (projective, cost ~ C(n_s,a) q^(n_s-a-1), no sampling).
Every f of degree < n_s with >= a roots in D factors UNIQUELY as
f = P_S * h with S its exact root set in D (|S| = j >= a) and h
nonvanishing on D\\S.  key(f) = coefficients of f in degrees K..n_s-1,
and h |-> key is linear and injective for fixed S.  The list size at a
key v is #{(S,h) : M_S h = v}, which is constant on the projective class
of v; and for fixed S each projective class [h] contributes to exactly
one projective class [M_S h].  So enumerating PROJECTIVE h once per S
and histogramming the projective key class computes every list size
exactly.  Cross-checked against exhaustive enumeration at q = 9, 17, 25.
"""
import sys
from math import isqrt
from itertools import combinations

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import ffq


def proj_canon(F, v):
    """canonical representative of the projective class of a nonzero vector"""
    for c in v:
        if c:
            iv = F.inv(c)
            return tuple(F.mul(x, iv) for x in v)
    return None


def proj_vectors(F, m):
    """one representative per projective class of F_q^m \\ {0}: leading 1"""
    q = F.q
    for lead in range(m):
        # coords 0..lead-1 are zero, coord lead is 1, rest free
        rest = m - lead - 1
        for code in range(q ** rest):
            v = [0] * lead + [1]
            t = code
            for _ in range(rest):
                v.append(t % q)
                t //= q
            yield v


def flmax(F, n_s, K, a, want_keys=False):
    """exact F_LMAX plus the histogram of list sizes over projective keys"""
    D = F.subgroup(n_s)
    R = n_s - K
    hist = {}
    for j in range(a, n_s):
        nh = n_s - j
        for S in combinations(range(n_s), j):
            PS = F.poly_from_roots([D[i] for i in S])
            out = [D[i] for i in range(n_s) if i not in S]
            for h in proj_vectors(F, nh):
                bad = False
                for x in out:
                    if F.poly_eval(h, x) == 0:
                        bad = True
                        break
                if bad:
                    continue
                key = [0] * R
                for i, c1 in enumerate(PS):
                    if c1:
                        for t2, c2 in enumerate(h):
                            if c2 and K <= i + t2 < n_s:
                                key[i + t2 - K] = F.add(key[i + t2 - K],
                                                        F.mul(c1, c2))
                if not any(key):
                    continue
                ck = proj_canon(F, key)
                hist[ck] = hist.get(ck, 0) + 1
    if not hist:
        return (0, {}) if want_keys else 0
    m = max(hist.values())
    return (m, hist) if want_keys else m


def flmax_direct(F, n_s, K, a):
    """exhaustive cross-check: enumerate every root-rich f once"""
    D = F.subgroup(n_s)
    q = F.q
    hist = {}
    for j in range(a, n_s):
        nh = n_s - j
        for S in combinations(range(n_s), j):
            PS = F.poly_from_roots([D[i] for i in S])
            out = [D[i] for i in range(n_s) if i not in S]
            for code in range(q ** nh):
                h, t = [], code
                for _ in range(nh):
                    h.append(t % q)
                    t //= q
                if not any(h):
                    continue
                if any(F.poly_eval(h, x) == 0 for x in out):
                    continue
                f = [0] * (n_s + 1)
                for i, c1 in enumerate(PS):
                    if c1:
                        for t2, c2 in enumerate(h):
                            if c2:
                                f[i + t2] = F.add(f[i + t2], F.mul(c1, c2))
                key = tuple(f[K:n_s])
                if not any(key):
                    continue
                hist[key] = hist.get(key, 0) + 1
    return max(hist.values()) if hist else 0


def domain_subfield(F, D):
    for d in range(1, F.e + 1):
        if F.e % d == 0 and all(F.in_subfield(x, d) for x in D):
            return d
    return F.e


def key_flags(F, key):
    if F.e == 1:
        return "-", "-"
    rat = all(F.in_subfield(c, 1) for c in key)
    fr = tuple(F.frob(c) for c in key)
    fixed = (fr == tuple(key))
    if not fixed:
        c0 = proj_canon(F, list(fr))
        fixed_proj = (c0 == proj_canon(F, list(key)))
    else:
        fixed_proj = True
    return ("rational" if rat else "irrational",
            "frob-fixed" if fixed else ("frob-proj-fixed" if fixed_proj
                                        else "frob-moved"))


if __name__ == "__main__":
    n_s, K = 8, 4
    print("=" * 100, flush=True)
    print("D3.0  VALIDATION: projective algorithm vs exhaustive enumeration", flush=True)
    print("=" * 100, flush=True)
    for q in (9, 17, 25):
        if (q - 1) % n_s:
            continue
        F = ffq.GF(q)
        for a in (5, 6, 7):
            d = flmax_direct(F, n_s, K, a)
            c = flmax(F, n_s, K, a)
            print(f"  q={q:<4} (p={F.p},e={F.e}) a={a}: exhaustive={d:<4} "
                  f"projective={c:<4} AGREE={d == c}", flush=True)

    LADDER = [9, 17, 25, 41, 49, 73, 81, 89, 97, 113, 121, 137, 169, 193,
              233, 241, 257, 281, 289, 337, 353, 361]
    print(flush=True)
    print("=" * 100, flush=True)
    print("D3.1  F_LMAX LADDER, n_s = 8, K = 4 (rate 1/2), PRIME vs EXTENSION",
          flush=True)
    print("=" * 100, flush=True)
    print(f"{'q':>5} {'p':>5} {'e':>2} {'type':>5} {'D<=F_p^d':>9} "
          f"{'B_s':>5} {'FL(5)':>6} {'FL(6)':>6} {'FL(7)':>6} {'sigma_L':>8} "
          f"{'#argmax(5)':>11} {'argmax flags':>28}", flush=True)
    table = {}
    for q in LADDER:
        if (q - 1) % n_s:
            continue
        pe = ffq.factor_pe(q)
        if pe is None:
            continue
        F = ffq.GF(q)
        D = F.subgroup(n_s)
        dsub = domain_subfield(F, D)
        vals, nargs, flags = {}, {}, {}
        for a in (5, 6, 7):
            m, hist = flmax(F, n_s, K, a, want_keys=True)
            vals[a] = m
            arg = [kk for kk, v in hist.items() if v == m]
            nargs[a] = len(arg)
            flags[a] = key_flags(F, list(arg[0])) if arg else ("-", "-")
        vals[8] = 1
        Bs = isqrt(q)
        sig = 0
        for a in range(K + 1, n_s + 1):
            if vals[a] > Bs:
                sig = a - K
        table[q] = (F.p, F.e, dsub, Bs, dict(vals), sig, nargs, flags)
        print(f"{q:>5} {F.p:>5} {F.e:>2} {('PRIME' if F.e == 1 else 'EXT'):>5} "
              f"{dsub:>9} {Bs:>5} {vals[5]:>6} {vals[6]:>6} {vals[7]:>6} "
              f"{sig:>8} {nargs[5]:>11} "
              f"{(flags[5][0] + '/' + flags[5][1]):>28}", flush=True)

    print(flush=True)
    print("=" * 100, flush=True)
    print("D3.2  VERDICT LINES", flush=True)
    print("=" * 100, flush=True)
    for a in (5, 6, 7):
        pr = sorted({(q, table[q][4][a]) for q in table if table[q][1] == 1})
        ex = sorted({(q, table[q][4][a]) for q in table if table[q][1] > 1})
        print(f"  a={a}  PRIME     : {pr}", flush=True)
        print(f"  a={a}  EXTENSION : {ex}", flush=True)
        pv = sorted({v for _, v in pr})
        ev = sorted({v for _, v in ex})
        print(f"  a={a}  value sets: prime {pv}  extension {ev}  "
              f"identical? {pv == ev}", flush=True)
        print(flush=True)

    print("  DOMAIN-LOCATION SPLIT (d = smallest subfield containing D):", flush=True)
    for dd in sorted({table[q][2] for q in table if table[q][1] > 1}):
        qs = [q for q in table if table[q][1] > 1 and table[q][2] == dd]
        print(f"    D inside F_(p^{dd}): q = {qs} -> "
              f"FL(5) = {[table[q][4][5] for q in qs]}", flush=True)

    print(flush=True)
    print("  q = 9 CONTROL: at q = 9 the order-8 domain IS the whole group F_9^*,", flush=True)
    print("  a degeneracy no prime field in the ladder shares (there D has index", flush=True)
    print("  (q-1)/8 >= 2).  Compare against the prime field where D = F_q^* is", flush=True)
    print("  impossible; the honest reading of q = 9 is stated in the report.", flush=True)

    print(flush=True)
    print("=" * 100, flush=True)
    print("D3.3  RATIONAL-KEY RESTRICTION (E3): max over F_p-rational keys only",
          flush=True)
    print("=" * 100, flush=True)
    print(f"{'q':>5} {'p':>5} {'e':>2} {'FL(5) global':>13} "
          f"{'FL(5) rational-key':>19} {'gap':>5}", flush=True)
    for q in LADDER:
        if (q - 1) % n_s:
            continue
        pe = ffq.factor_pe(q)
        if pe is None or pe[1] == 1 or q > 400:
            continue
        F = ffq.GF(q)
        m, hist = flmax(F, n_s, K, 5, want_keys=True)
        best_rat = 0
        # proj_canon normalises the first nonzero coordinate to 1, so the
        # class [kk] has an F_p-rational representative iff the canonical
        # representative is itself F_p-rational.
        for kk, v in hist.items():
            if v > best_rat and all(F.in_subfield(c, 1) for c in kk):
                best_rat = v
        print(f"{q:>5} {F.p:>5} {F.e:>2} {m:>13} {best_rat:>19} "
              f"{m - best_rat:>5}", flush=True)
    sys.stdout.flush()
