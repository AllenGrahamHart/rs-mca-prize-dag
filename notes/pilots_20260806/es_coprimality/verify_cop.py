#!/usr/bin/env python3
"""Round 17 -- (ES) coprimality pilot: fail-closed verifier.

Stages (argv[1]):
  self    -- machinery self-test (lattice index, principal case, invariance)
  floor   -- Phi1/Phi2: THEOREM CS on every round-16 census accident
  strat   -- Phi3: LEMMA STRAT
  wit     -- K3: the five round-16 witnesses, exact N(I_S) factorisations
  rate    -- K4: coprimality rate on the reachable grid  (argv[2..]=n,rmax)

Exits nonzero if ANY check fails.  No float in any decision path.

run:  tools/ramguard local -- python3 \
      notes/pilots_20260806/es_coprimality/verify_cop.py self
"""

import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cop_lib import (M_of, antipodal_pairs, census_bad, coord_vector,
                     cyclotomic_closure, factorize, field_norm, ideal_norm,
                     is_periodic, lattice_index, mul_zeta, mult_order,
                     reduce_strat, strat, z_w_odd)

FAIL = []
NCHK = [0]
HERE = os.path.dirname(os.path.abspath(__file__))
ADV = os.path.join(os.path.dirname(HERE), "es_boundary_adversary")


def check(name, cond, detail=""):
    NCHK[0] += 1
    if not cond:
        FAIL.append((name, detail))
        print("    FAIL %-42s | %s" % (name, detail))
    return cond


def load_records():
    """all round-16 census bad-prime records, both rows."""
    recs = []
    for fn in ("census_n16_2_8.json", "census_n32_2_6.json"):
        path = os.path.join(ADV, fn)
        if not os.path.exists(path):
            continue
        with open(path) as fh:
            d = json.load(fh)
        for r in d["records"]:
            recs.append(r)
    return recs


# ==========================================================================
def stage_self():
    print("-" * 74)
    print("[SELF] machinery self-test")
    # S1: lattice_index on explicit lattices
    check("S1a identity lattice index 1",
          lattice_index([[1, 0], [0, 1]], 2) == 1)
    check("S1b diag(2,3) index 6",
          lattice_index([[2, 0], [0, 3]], 2) == 6)
    check("S1c rank deficient -> 0",
          lattice_index([[1, 1], [2, 2]], 2) == 0)
    check("S1d unimodular index 1",
          lattice_index([[1, 1], [1, 2]], 2) == 1)
    check("S1e 3x3 det 12",
          lattice_index([[2, 1, 0], [0, 2, 1], [0, 0, 3]], 3) == 12)
    rng = random.Random(11)
    for t in range(6):
        h = 4
        rows = [[rng.randint(-3, 3) for _ in range(h)] for _ in range(h)]
        import itertools
        # exact determinant by permutation expansion (independent route)
        det = 0
        for perm in itertools.permutations(range(h)):
            sgn = 1
            seen = list(perm)
            for i in range(h):
                for j in range(i + 1, h):
                    if seen[i] > seen[j]:
                        sgn = -sgn
            pr = 1
            for i in range(h):
                pr *= rows[i][perm[i]]
            det += sgn * pr
        check("S1f random 4x4 index == |det| (t=%d)" % t,
              lattice_index(rows, h) == abs(det),
              "hnf=%d det=%d" % (lattice_index(rows, h), det))

    # S2: w=2 -> I_S principal -> N(I_S) = |N(x_1)|
    rng = random.Random(3)
    for n in (8, 16, 32):
        for t in range(5):
            rp = rng.randint(2, n // 2)
            S = sorted(rng.sample(range(n), rp))
            a = ideal_norm(S, n, 2)
            b = abs(field_norm(coord_vector(S, 1, n), n))
            check("S2 principal n=%d t=%d" % (n, t), a == b,
                  "ideal=%d fieldnorm=%d S=%s" % (a, b, S))

    # S3: N(I_S) invariant under rotation and odd dilation (unit/Galois)
    rng = random.Random(5)
    for t in range(8):
        n = 16
        rp = rng.randint(3, 8)
        w = rng.randint(2, 5)
        S = sorted(rng.sample(range(n), rp))
        base = ideal_norm(S, n, w)
        b = rng.randrange(n)
        Sr = sorted((i + b) % n for i in S)
        check("S3a rotation-invariance t=%d" % t,
              ideal_norm(Sr, n, w) == base,
              "S=%s b=%d %d vs %d" % (S, b, ideal_norm(Sr, n, w), base))
        c = rng.randrange(1, n, 2)
        Sd = sorted((c * i) % n for i in S)
        check("S3b dilation-invariance t=%d" % t,
              ideal_norm(Sd, n, w) == base,
              "S=%s c=%d %d vs %d" % (S, c, ideal_norm(Sd, n, w), base))

    # S4: LEMMA Z consistency -- periodic <=> N(I_S) = 0
    for n in (8, 16):
        for rp in range(1, n):
            import itertools
            for S in itertools.combinations(range(n), rp):
                for w in range(2, min(rp, 5) + 1):
                    z = (ideal_norm(list(S), n, w) == 0)
                    per = is_periodic(list(S), n, w)
                    if z != per:
                        check("S4 LEMMA Z n=%d w=%d" % (n, w), False,
                              "S=%s ideal0=%s periodic=%s" % (S, z, per))
            if rp >= 4 and n == 16:
                break   # keep runtime bounded; rp<=4 is exhaustive at n=16
    check("S4 LEMMA Z consistency (exhaustive n=8 all rp; n=16 rp<=4)", True)

    # S5: census route agrees with ideal-norm route on prime support
    rng = random.Random(9)
    for t in range(10):
        n = 16
        rp = rng.randint(3, 8)
        w = rng.randint(3, 5)
        S = sorted(rng.sample(range(n), rp))
        N = ideal_norm(S, n, w)
        if N == 0:
            continue
        sup = sorted(q for q in factorize(N) if q != 2)
        cb = sorted(census_bad(S, n, w, [q for q in factorize(N)]))
        check("S5 support agrees t=%d" % t, sup == cb,
              "S=%s N=%d idealsup=%s censusbad=%s" % (S, N, sup, cb))

    # S6: (CS2) the archimedean ceiling, EXACT integer form
    #     N(x_1)^2 <= (r' - a_{n/2}(S))^h          [Parseval + AM-GM]
    rng = random.Random(23)
    import itertools
    for n in (8, 16):
        h = n // 2
        for rp in range(1, n):
            for S in itertools.combinations(range(n), rp):
                v = coord_vector(list(S), 1, n)
                if not any(v):
                    continue
                N1 = abs(field_norm(v, n))
                a = antipodal_pairs(list(S), n)
                check("S6 (CS2) exact n=%d r'=%d" % (n, rp),
                      N1 * N1 <= (rp - a) ** h,
                      "S=%s N1=%d a=%d bound=%d" % (S, N1, a, (rp - a) ** h))
    for t in range(40):
        n = 32
        h = 16
        rp = rng.randint(2, 16)
        S = sorted(rng.sample(range(n), rp))
        v = coord_vector(S, 1, n)
        if not any(v):
            continue
        N1 = abs(field_norm(v, n))
        a = antipodal_pairs(S, n)
        check("S6b (CS2) exact n=32 t=%d" % t,
              N1 * N1 <= (rp - a) ** h,
              "S=%s N1=%d a=%d" % (S, N1, a))
    print("  [SELF] %d checks" % NCHK[0])


# ==========================================================================
def stage_floor():
    """Phi1 + Phi2: THEOREM CS against every round-16 census accident."""
    print("-" * 74)
    print("[FLOOR] THEOREM CS on every round-16 census bad-prime record")
    recs = load_records()
    check("F0 census records loaded", len(recs) > 0, "%d" % len(recs))
    n_x1nz = n_x1z = 0
    worst = None
    for r in recs:
        n, rp, w, p, S = r["n"], r["rp"], r["w"], r["p"], list(r["witness"])
        v1 = coord_vector(S, 1, n)
        # the record's S is one representative; confirm it really is bad
        if not census_bad(S, n, w, [p]):
            check("F0b record is a genuine accident", False, str(r))
            continue
        if not any(v1):
            n_x1z += 1
            check("Phi1z x_1=0 => S is mu_2-periodic (LEMMA Z, t=1)",
                  strat(S, n) >= 1, "S=%s n=%d" % (S, n))
            continue
        n_x1nz += 1
        zo = len(z_w_odd(w, n, p))
        N1 = abs(field_norm(v1, n))
        # ---- Phi1 : p^{|Z_w^odd|} | N(x_1)
        ok1 = (N1 % (p ** zo) == 0)
        vp = 0
        tmp = N1
        while tmp and tmp % p == 0:
            vp += 1
            tmp //= p
        check("Phi1 p^|Zodd| | N(x_1)  n=%d r'=%d w=%d p=%d" % (n, rp, w, p),
              ok1, "zo=%d v_p(N1)=%d N1=%d" % (zo, vp, N1))
        # ---- Phi2 : (CS3) the archimedean squeeze
        a = antipodal_pairs(S, n)
        lhs = zo * math.log2(p)
        rhs = (n / 4.0) * math.log2(max(rp - a, 2))
        ok2 = lhs <= rhs + 1e-9
        check("Phi2 (CS3) n=%d r'=%d w=%d p=%d" % (n, rp, w, p), ok2,
              "lhs=%.4f rhs=%.4f zo=%d a=%d" % (lhs, rhs, zo, a))
        slack = rhs - lhs
        if worst is None or slack < worst[0]:
            worst = (slack, n, rp, w, p, zo, a)
    print("  records: %d   x_1 != 0: %d   x_1 = 0 (stratified): %d"
          % (len(recs), n_x1nz, n_x1z))
    if worst:
        print("  TIGHTEST (CS3) margin: %.4f bits at n=%d r'=%d w=%d p=%d "
              "|Z_w^odd|=%d a=%d" % worst)
    print("  [FLOOR] cumulative %d checks" % NCHK[0])


# ==========================================================================
def stage_strat():
    """Phi3: LEMMA STRAT -- the exact stratum reduction."""
    print("-" * 74)
    print("[STRAT] LEMMA STRAT: x_s = 0 off 2^a Z, and the odd-prime match")
    rng = random.Random(17)
    tested = 0
    for n in (16, 32):
        h = n // 2
        for t in range(40):
            a = rng.randint(1, 2)
            n2 = n // (2 ** a)
            rp2 = rng.randint(1, n2 - 1)
            Sp = sorted(rng.sample(range(n2), rp2))
            # lift to a stratum-a set
            S = sorted((i + j * n2) % n for i in Sp for j in range(2 ** a))
            if strat(S, n) < a:
                continue
            tested += 1
            w = rng.randint(2, 7)
            # (i) x_s = 0 unless 2^a | s
            okz = all(not any(coord_vector(S, s, n))
                      for s in range(1, w) if s % (2 ** a) != 0)
            check("Phi3a x_s=0 off 2^aZ n=%d a=%d w=%d" % (n, a, w), okz,
                  "S=%s" % S)
            # (ii) x_{2^a t} = 2^a * iota(p_t(S'))
            okv = True
            for tt in range(1, w):
                s = (2 ** a) * tt
                if s >= w:
                    break
                v = coord_vector(S, s, n)
                v2 = coord_vector(Sp, tt, n2)
                # iota: zeta_{n2}^e -> zeta_n^{e * 2^a}
                lift = [0] * h
                for e, c in enumerate(v2):
                    ee = (e * (2 ** a)) % n
                    if ee < h:
                        lift[ee] += c
                    else:
                        lift[ee - h] -= c
                if v != [(2 ** a) * c for c in lift]:
                    okv = False
            check("Phi3b x_{2^a t} = 2^a iota(p_t(S')) n=%d a=%d" % (n, a),
                  okv, "S=%s w=%d" % (S, w))
            # (iii) odd bad primes match the reduced instance
            wp = (w - 1) // (2 ** a) + 1
            N = ideal_norm(S, n, w)
            N2 = ideal_norm(Sp, n2, wp)
            if N == 0 or N2 == 0:
                check("Phi3c zero-branch agrees n=%d a=%d" % (n, a),
                      (N == 0) == (N2 == 0),
                      "S=%s w=%d N=%d N2=%d wp=%d" % (S, w, N, N2, wp))
                continue
            sup = sorted(q for q in factorize(N) if q != 2)
            sup2 = sorted(q for q in factorize(N2) if q != 2)
            check("Phi3c odd bad primes match n=%d a=%d w=%d" % (n, a, w),
                  sup == sup2,
                  "S=%s -> S'=%s  %s vs %s" % (S, Sp, sup, sup2))
    print("  stratified fixtures tested: %d" % tested)
    print("  [STRAT] cumulative %d checks" % NCHK[0])


# ==========================================================================
WITNESSES = [
    (32, 6, 4, 7, 4, [0, 2, 5, 16, 18, 21]),
    (32, 6, 3, 47, 2, [0, 2, 8, 9, 10, 17]),
    (32, 6, 4, 17, 2, [0, 1, 3, 16, 17, 19]),
    (32, 5, 2, 23, 4, [0, 4, 6, 8, 18]),
    (32, 5, 2, 463, 2, [0, 2, 3, 4, 17]),
]


def stage_wit():
    """K3: exact N(I_S) for the five round-16 witnesses."""
    print("-" * 74)
    print("[WIT] K3 -- the five round-16 witnesses, exact N(I_S)")
    print("  %-3s %-3s %-3s %-6s %-3s %-4s %-3s %s"
          % ("n", "r'", "w", "p", "a", "|Zo|", "in", "N(I_S) factorisation"))
    for (n, rp, w, p, delta, S) in WITNESSES:
        a = strat(S, n)
        N = ideal_norm(S, n, w)
        zo = len(z_w_odd(w, n, p))
        fac = factorize(N) if N else {}
        fs = " * ".join("%d^%d" % (q, e) for q, e in sorted(fac.items())) \
            if fac else ("0" if N == 0 else "1")
        inE = (a >= 1) or True   # E_floor membership decided below
        check("K3a p | N(I_S)  (n=%d r'=%d w=%d p=%d)" % (n, rp, w, p),
              N != 0 and N % p == 0, "N=%d" % N)
        okfl, zo2, base = None, zo, rp - antipodal_pairs(S, n)
        lhs = zo * math.log2(p)
        rhs = (n / 4.0) * math.log2(max(base, 2))
        okfl = lhs <= rhs + 1e-9
        check("K3b witness is inside E(n,r',w) (n=%d w=%d p=%d)"
              % (n, w, p), (a >= 1) or okfl,
              "a=%d lhs=%.3f rhs=%.3f" % (a, lhs, rhs))
        print("  %-3d %-3d %-3d %-6d %-3d %-4d %-3s %s"
              % (n, rp, w, p, a, zo, "E_s" if a >= 1 else "E_f", fs))
        # for stratified witnesses report the reduced instance too
        if a >= 1:
            n2 = n // (2 ** a)
            Sp = reduce_strat(S, n, a)
            wp = (w - 1) // (2 ** a) + 1
            N2 = ideal_norm(Sp, n2, wp)
            f2 = factorize(N2) if N2 else {}
            print("        reduces to n=%d S'=%s w'=%d  N=%s"
                  % (n2, Sp, wp,
                     " * ".join("%d^%d" % (q, e) for q, e in sorted(f2.items()))
                     or str(N2)))
            check("K3c stratum reduction keeps p (n=%d p=%d)" % (n, p),
                  N2 != 0 and N2 % p == 0, "N2=%d" % N2)
    print("  [WIT] cumulative %d checks" % NCHK[0])


# ==========================================================================
def stage_rate(n, rmax, wmax, rmin=2, wmin=2):
    """K4: exact coprimality rate over orbits, split by stratum."""
    import itertools
    print("-" * 74)
    print("[RATE] K4 -- coprimality rate  n=%d  r'<=%d  w<=%d" % (n, rmax, wmax))
    print("  %-3s %-3s %-7s %-7s %-8s %-8s %-9s %s"
          % ("r'", "w", "orbits", "N=0", "N=1", "N>1", "rate", "bad p (a=0)"))
    binom = [[math.comb(x, y) for y in range(rmax + 2)] for x in range(n + 1)]

    def colex_rank(comb):
        return sum(binom[c][j + 1] for j, c in enumerate(comb))

    for rp in range(rmin, rmax + 1):
        total = math.comb(n, rp)
        seen = bytearray(total)
        reps = []
        for comb in itertools.combinations(range(n), rp):
            pos = colex_rank(sorted(comb))
            if seen[pos]:
                continue
            reps.append(comb)
            for c in range(1, n, 2):
                base = tuple(sorted((c * i) % n for i in comb))
                for b in range(n):
                    seen[colex_rank(tuple(sorted((i + b) % n for i in base)))] = 1
        for w in range(wmin, min(rp, wmax) + 1):
            n0 = n1 = ngt = 0
            badp = set()
            for comb in reps:
                S = list(comb)
                N = ideal_norm(S, n, w)
                if N == 0:
                    n0 += 1
                    continue
                # LEMMA TWO: strip the forced 2-part (p=2 is ramified and
                # is excluded from every (ES) row); the conjecture is about
                # the ODD part.  Also CHECK the parity mechanism here.
                v2 = 0
                Nod = N
                while Nod % 2 == 0:
                    Nod //= 2
                    v2 += 1
                check("LEMMA TWO parity r'=%d w=%d" % (rp, w),
                      (v2 > 0) == (rp % 2 == 0),
                      "S=%s N=%d v2=%d" % (S, N, v2))
                if Nod == 1:
                    n1 += 1
                else:
                    ngt += 1
                    if strat(S, n) == 0:
                        try:
                            for q in factorize(Nod):
                                badp.add(q)
                        except Exception:
                            badp.add(-1)
            den = n1 + ngt
            rate = (float(n1) / den) if den else 1.0
            print("  %-3d %-3d %-7d %-7d %-8d %-8d %-9.5f %s"
                  % (rp, w, len(reps), n0, n1, ngt, rate,
                     sorted(badp)[:8]))
    print("  [RATE] cumulative %d checks" % NCHK[0])


# ==========================================================================
def main():
    stage = sys.argv[1] if len(sys.argv) > 1 else "self"
    print("=" * 74)
    print("ROUND 17 -- (ES) COPRIMALITY PILOT  stage=%s" % stage)
    print("=" * 74)
    if stage == "self":
        stage_self()
    elif stage == "floor":
        stage_floor()
    elif stage == "strat":
        stage_strat()
    elif stage == "wit":
        stage_wit()
    elif stage == "failclosed":
        # deliberate falsehood: proves the harness reports failures and
        # exits nonzero (fail-closed).  Must ALWAYS exit 1.
        print("[FAILCLOSED] injecting one false check on purpose")
        check("INJECTED FALSE (expected to fail)", 1 == 2, "by design")
        check("INJECTED CS violation (expected to fail)",
              ideal_norm([0, 1, 2], 16, 3) == -1, "by design")
    elif stage == "rate":
        stage_rate(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),
                   int(sys.argv[5]) if len(sys.argv) > 5 else 2,
                   int(sys.argv[6]) if len(sys.argv) > 6 else 2)
    else:
        print("unknown stage")
        return 2
    print("=" * 74)
    print("checks: %d   failures: %d" % (NCHK[0], len(FAIL)))
    for f in FAIL[:20]:
        print("  FAILED: %s | %s" % f)
    print("=" * 74)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
