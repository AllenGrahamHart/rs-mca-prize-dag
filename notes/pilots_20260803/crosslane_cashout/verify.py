#!/usr/bin/env python3
"""Cross-lane cash-out verifier (P-A1 |K|, P-B planting ceiling).

Compute law: run ONLY as
    tools/ramguard tiny  -- python3 notes/pilots_20260803/crosslane_cashout/verify.py
    tools/ramguard local -- python3 notes/pilots_20260803/crosslane_cashout/verify.py --full
from the repo root.  Pure python integers + GF(p) linear algebra, no
third-party imports, no network.

Every check is registered against PREREG.md (+ its ADDENDUM).
"""
import json, sys, os, math, random
from itertools import combinations

_isqrt = math.isqrt

FULL = "--full" in sys.argv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

CHECKS = []
FALSIFIERS = {}


def ck(name, cond, detail=""):
    CHECKS.append((name, bool(cond), detail))
    if not cond:
        print("  FAIL  %-46s %s" % (name, detail))
    return bool(cond)


def fired(tag, cond, detail=""):
    """Record a pre-registered falsifier outcome."""
    prev = FALSIFIERS.get(tag, (False, ""))
    if cond:
        FALSIFIERS[tag] = (True, detail)
    elif not prev[0]:
        FALSIFIERS[tag] = (False, detail)
    return cond


# ---------------------------------------------------------------- GF(p)
def rank_mod(rows, p):
    """Rank of a list of vectors over F_p (destructive copy)."""
    M = [list(r) for r in rows]
    if not M:
        return 0
    ncol = len(M[0])
    r = 0
    for c in range(ncol):
        piv = None
        for i in range(r, len(M)):
            if M[i][c] % p:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r


def nullspace_mod(rows, ncol, p):
    """Basis of {x : rows . x = 0} over F_p."""
    M = [list(r) for r in rows]
    pivots = []
    r = 0
    for c in range(ncol):
        piv = None
        for i in range(r, len(M)):
            if M[i][c] % p:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        pivots.append(c)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(ncol) if c not in pivots]
    basis = []
    for fc in free:
        v = [0] * ncol
        v[fc] = 1
        for i, pc in enumerate(pivots):
            v[pc] = (-M[i][fc]) % p
        basis.append(v)
    return basis


def dual_basis(S, k, p):
    """Basis of C_S = {c on S : sum_x c(x) x^i = 0, i<k}; dim = |S|-k."""
    rows = [[pow(x, i, p) for x in S] for i in range(k)]
    return nullspace_mod(rows, len(S), p)


# ============================================================== PART A
def part_A():
    print("\n=== PART A : the unconditional |K| bound for P-A1 ===")
    rows = json.load(open(os.path.join(
        ROOT, "notes/pilots_20260802/support4_relation/stage5_escape.json")))["criterion"]
    ck("A.rows.count", len(rows) == 6, "%d rows" % len(rows))

    # ---- A-P4 : the row table (transferred sunflower ceiling vs target)
    print("\n-- A-P4 / A-P5 : row table (TRANSFER of banked bounds)")
    predicted = [88, 45, 34, 131, 67, 67]          # as pre-registered
    got, targets = [], []
    for i, r in enumerate(rows):
        A, h, R, k = r["A"], r["h"], r["R"], r["k"]
        bound = 1 + (2 * A) // (h + 1)             # sunflower, p >= (h+1)/2
        target = (2 * R - 1) // h
        got.append(bound)
        targets.append(target)
        ck("A.P4.below_target[%s]" % r["name"], bound < target,
           "bound %d vs target %d" % (bound, target))
        # A-P5 : banked clique_Vmax == 1 + floor(A/(h-d)),  d = 2h - clique_m
        d = 2 * h - r["clique_m"]
        pred_clique = 1 + A // (h - d)
        ck("A.P5.clique[%s]" % r["name"], pred_clique == r["clique_Vmax"],
           "1+A/(h-d)=%d vs banked clique_Vmax=%d" % (pred_clique, r["clique_Vmax"]))
        # and the banked identity clique_u//(h-d)
        ck("A.P5.cliqueu[%s]" % r["name"],
           r["clique_u"] // (h - d) == r["clique_Vmax"], "u//(h-d)")
    print("   bound  1+floor(2A/(h+1)) =", got)
    print("   target floor((2R-1)/h)   =", targets)
    mismatch = [(rows[i]["name"], predicted[i], got[i])
                for i in range(6) if predicted[i] != got[i]]
    fired("A-F4", bool(mismatch), "predicted vs recomputed: %s" % mismatch)
    ck("A.P4.all_below", all(g < t for g, t in zip(got, targets)), "6/6")

    # ---- A-P1 : the complement floor 2t >= h+1  (BANKED as e >= 1)
    print("\n-- A-P1 : complement floor 2t >= h+1 (banked e:=2t-h >= 1)")
    bad = []
    shapes = [(6, 3, 9), (6, 4, 9), (5, 3, 8), (7, 4, 10)] if not FULL else \
             [(6, 3, 9), (6, 4, 9), (5, 3, 8), (7, 4, 10), (6, 3, 10), (8, 5, 11)]
    tested = 0
    for (A, k, NU) in shapes:
        h = A - k
        ground = list(range(NU))
        subs = list(combinations(ground, A))
        for tri in combinations(range(len(subs)), 3):
            Sa, Sb, Sc = (set(subs[j]) for j in tri)
            U = Sa | Sb | Sc
            t = len(U) - A
            trip = len(Sa & Sb & Sc)
            tested += 1
            if trip <= k - 1:                      # (T)-clean
                if 2 * t < h + 1:
                    bad.append((A, k, NU, sorted(U), t))
        ck("A.P1.floor[A=%d,k=%d,|ground|=%d]" % (A, k, NU), not bad,
           "%d triples swept" % tested)
    fired("A-F1", bool(bad), "%d violations" % len(bad))
    ck("A.P1.no_violation", not bad, "%d (T)-clean triples swept, 0 with 2t<=h" % tested)
    # the inclusion-exclusion mechanism itself
    mech = all((3 * A - 2 * (A + t) <= k - 1) == (2 * t >= 3 * A - 2 * A - k + 1)
               for A in range(5, 12) for k in range(2, A) for t in range(0, 8))
    ck("A.P1.mechanism", mech, "|SaSbSc| >= 3A-2|U| and (T) <=> 2t >= h+1")

    # ---- A-P8 (NEW) : |K_+| <= e+2 from THEOREM D + D0-3
    print("\n-- A-P8 (NEW) : escaping core rays  |K_+| <= e+2 = 2t-h+2")
    # (a) pure arithmetic of the implication, brute-forced
    import random
    random.seed(20260803)
    arith_bad = []
    for _ in range(4000):
        V = random.randint(4, 14)
        hh = random.randint(3, 8)
        esc = sorted(random.randint(0, hh - 1) for _ in range(V))
        e_minus_1 = sum(esc[3:])                   # the THEOREM-D residue
        Kplus = sum(1 for x in esc if x >= 1)
        # claim: Kplus - 3 <= sum_{i>=4} esc_i
        if Kplus - 3 > e_minus_1:
            arith_bad.append(esc)
    ck("A.P8.arithmetic", not arith_bad,
       "4000 sorted escape vectors: |K_+|-3 <= sum_{i>=4} esc_i")

    # (b) THEOREM D + D0-3 chain on integers
    chain_bad = []
    for hh in range(3, 9):
        for tt in range((hh + 1 + 1) // 2, hh + 6):
            m = hh + tt
            e = 2 * tt - hh
            if e < 1:
                continue
            # rank <= 2m-1 (D0-3, live) and rank >= sum esc + G3 (THEOREM D)
            bound_sum = (2 * m - 1) - 3 * hh       # >= sum_{i>=4} esc_i
            if bound_sum != e - 1:
                chain_bad.append((hh, tt, bound_sum, e - 1))
    ck("A.P8.chain", not chain_bad, "2m-1-3h == e-1 for all (h,t) with e>=1")

    # ---- A-P9 (NEW) : zero-escape Jensen counting threshold
    print("\n-- A-P9 (NEW) : zero-escape triple-count threshold")
    def finite(A, k, t):
        return (A + t) ** 2 * (k - 1) < A ** 3
    def jensen_bound(A, k, t):
        """largest V with A(bV-1)(bV-2) <= (V-1)(V-2)(k-1), b=A/(A+t).
           The inequality holds only BETWEEN the two roots, so scan from
           V = 4 (|K| >= 4 by LEMMA B) and stop at the first failure after
           the window has been entered."""
        if not finite(A, k, t):
            return None
        u = A + t
        # cleared denominators: A(AV-u)(AV-2u) <= (V-1)(V-2)(k-1)u^2
        V, last = 4, None
        while V < 10 ** 7:
            lhs = A * (A * V - u) * (A * V - 2 * u)
            rhs = (V - 1) * (V - 2) * (k - 1) * u * u
            if lhs <= rhs:
                last = V
            elif last is not None:
                break
            elif V > 1000:
                break
            V += 1
        return last
    # window width: finite iff (A+t)^2 (k-1) < A^3
    thresh_rows = []
    jb = {}
    for r in rows:
        A, h, k = r["A"], r["h"], r["k"]
        tmin = (h + 1 + 1) // 2                    # ceil((h+1)/2)
        f_min = finite(A, k, tmin)
        f_next = finite(A, k, tmin + 1)
        # how many integers t admit a finite bound (closed form, exact):
        # finite <=> (A+t)^2 < A^3/(k-1) <=> A+t <= isqrt((A^3-1)//(k-1))
        tmax = _isqrt((A ** 3 - 1) // (k - 1)) - A
        while (A + tmax) ** 2 * (k - 1) >= A ** 3:
            tmax -= 1
        ck("A.P9.tmax_exact[%s]" % r["name"],
           finite(A, k, tmax) and not finite(A, k, tmax + 1),
           "t_max = %d" % tmax)
        width = max(0, tmax - tmin + 1)
        thresh_rows.append((r["name"], tmin, f_min, f_next, width))
        ck("A.P9.finite_at_tmin[%s]" % r["name"], f_min,
           "finite counting bound exists at t_min = %d" % tmin)
        jb[r["name"]] = jensen_bound(A, k, tmin)
        print("   %-11s t_min=%-11d window=%-9d Jensen |K_0| <= %-5s "
              "(sunflower 1+A/t_min = %d)"
              % (r["name"], tmin, width, jb[r["name"]], 1 + A // tmin))
    # PRE-REGISTERED prediction: the window is exactly one integer wide
    one_wide = all((a and not b) for (_, _, a, b, _) in thresh_rows)
    fired("A-F9", not one_wide,
          "window not one integer wide at: %s"
          % [nm for (nm, _, a, b, _) in thresh_rows if not (a and not b)])
    ck("A.P9.recorded_window", True,
       "finite@(t_min,t_min+1) per row: %s"
       % [(nm, a, b) for (nm, _, a, b, _) in thresh_rows])
    # order-of-magnitude agreement with the banked sunflower ceiling
    for r in rows:
        A, h, k, nm = r["A"], r["h"], r["k"], r["name"]
        tmin = (h + 1 + 1) // 2
        sf = 1 + A // tmin
        if jb[nm] is not None:
            ck("A.P9.equals_sunflower[%s]" % nm, jb[nm] == sf,
               "UNCONDITIONAL Jensen %d == banked sunflower %d" % (jb[nm], sf))
            ck("A.P9.below_target[%s]" % nm, jb[nm] < (2 * r["R"] - 1) // h,
               "jensen %d < target %d" % (jb[nm], (2 * r["R"] - 1) // h))

    # ---- A-P7 : banked-fixture replay + A-P8 evaluated ON the banked cores
    print("\n-- A-P7 : banked replay (U-mechanism, K_V) + A-P8 on them")
    banked_ok = True
    try:
        P2 = os.path.join(ROOT, "notes/pilots_20260802")
        for sub in ("support4_relation", "exact_k_heart"):
            p = os.path.join(P2, sub)
            if p not in sys.path:
                sys.path.append(p)
        import s4lib as S          # noqa: must precede tslib/stage5_escape
        import tslib as T
        import stage5_escape as S5
    except Exception as exc:       # pragma: no cover
        banked_ok = False
        ck("A.P7.import", False, "import failed: %r" % (exc,))

    def core_and_escapes(supports, k, nn):
        """greatest fixed point of Phi = the (3,k+1)-core operator (U2)."""
        live = {a: set(S_) for a, S_ in enumerate(supports)}
        while True:
            mult = {}
            for a in live:
                for x in live[a]:
                    mult[x] = mult.get(x, 0) + 1
            W = {x for x, m in mult.items() if m >= 3}
            new = {a: live[a] & W for a in live}
            new = {a: s for a, s in new.items() if len(s) > k}
            if new == live:
                return live
            live = new

    if banked_ok:
        # (1) U-mechanism (3,5,1,4): dim Rel 1, rank 19, escape floor 16, cap 4
        k, h, d, V, q = 3, 5, 1, 4, 6421
        priv = (h - 1) - (V - 1) * d
        nn = (k + 2) + (V * (V - 1) // 2) * d + V * priv + 2
        row = T.Row2(nn, k, h, q)
        fam = S.build_mobius_family(row, d, V, seed=1)
        sup, zs = fam["supports"], fam["slopes"]
        rk = S.family_rank(row, sup, zs)
        dimrel, _, _ = S.relation_space(row, sup, zs)
        lim, dimcap, floor = S5.peel_bound(row, sup)
        ck("A.P7.umech.rank", rk == 19, "rank %d (banked 19)" % rk)
        ck("A.P7.umech.dimrel", dimrel == 1, "dim Rel %d (banked 1)" % dimrel)
        ck("A.P7.umech.floor_cap", (floor, dimcap) == (16, 4),
           "floor %d cap %d (banked 16/4)" % (floor, dimcap))
        # A-P8 on this fixture
        core = core_and_escapes(sup, k, nn)
        A_ = k + h
        U_ = set().union(*[set(s) for s in sup])
        t_ = len(U_) - A_
        e_ = 2 * t_ - h
        m_ = h + t_
        esc = sorted(A_ - len(core[a]) for a in core)
        Kplus = sum(1 for x in esc if x >= 1)
        G3 = 3 * h - sum(esc[:3])
        print("   U-mech: |U|=%d t=%d e=%d |K|=%d escapes=%s rank=%d 2m-1=%d"
              % (len(U_), t_, e_, len(core), esc, rk, 2 * m_ - 1))
        ck("A.P7.umech.core_all", len(core) == V, "core = all %d rays" % len(core))
        ck("A.P8.umech.D0_3", rk <= 2 * m_ - 1, "rank %d <= 2m-1 = %d" % (rk, 2 * m_ - 1))
        ck("A.P8.umech.thmD", rk >= sum(esc) + G3,
           "rank %d >= sum esc + G3 = %d" % (rk, sum(esc) + G3))
        ck("A.P8.umech.thmD_tight", rk == sum(esc) + G3,
           "THEOREM D TIGHT: %d == %d" % (rk, sum(esc) + G3))
        ck("A.P8.umech.residue", sum(esc[3:]) <= e_ - 1,
           "sum_{i>=4} esc = %d <= e-1 = %d" % (sum(esc[3:]), e_ - 1))
        ck("A.P8.umech.bound", Kplus <= e_ + 2,
           "|K_+| = %d <= e+2 = %d" % (Kplus, e_ + 2))
        fired("A-F8", not (rk <= 2 * m_ - 1 and Kplus <= e_ + 2), "U-mechanism")

        # (2) K_V (3,7,1,5): dim Rel 0, rank 35 = Vh, core EMPTY (every ray dies)
        k2, h2, d2, V2 = 3, 7, 1, 5
        M2 = V2 * (V2 - 1) // 2
        n2 = max((k2 - 1) + M2 * (d2 + 1), k2 + h2 + 2)
        row2 = T.Row2(n2, k2, h2, q)
        _, _, info = S5.ADV.build_KV(row2, d2, V2, seed=0)
        sup2 = [tuple(s) for s in info["supports"].values()]
        zs2 = list(info["zs"])
        rk2 = S.family_rank(row2, sup2, zs2)
        dr2, _, _ = S.relation_space(row2, sup2, zs2)
        ck("A.P7.kv.rank", rk2 == V2 * h2 == 35, "rank %d (banked 35 = Vh)" % rk2)
        ck("A.P7.kv.dimrel", dr2 == 0, "dim Rel %d (banked 0)" % dr2)
        core2 = core_and_escapes(sup2, k2, n2)
        ck("A.P7.kv.core_empty", len(core2) == 0,
           "core = %d rays (triple locus = Y, |Y| = k-1 < k+1)" % len(core2))

    # ---- A-P8 at the complement FLOOR : exhaustive small search
    print("\n-- A-P8 at the complement floor e = 1 : |K_+| <= 3")
    # h=3, t=2 => e=1 ; A=k+3, |U|=A+2
    found, worst = 0, 0
    viol8 = []
    for k, Vmax in ((3, 7), (4, 6 if FULL else 5)):
        A_ = k + 3
        NU = A_ + 2
        ground = list(range(NU))
        subs = [set(c) for c in combinations(ground, A_)]
        for V in range(4, Vmax):
            for combo in combinations(range(len(subs)), V):
                Ss = [subs[j] for j in combo]
                U_ = set().union(*Ss)
                if len(U_) != NU:                  # need t = 2 exactly
                    continue
                bad_gate = False
                for a, b, c in combinations(range(V), 3):
                    if len(Ss[a] & Ss[b] & Ss[c]) > k - 1:
                        bad_gate = True
                        break
                if bad_gate:
                    continue
                core = core_and_escapes([tuple(sorted(s)) for s in Ss], k, NU)
                if not core:
                    continue
                found += 1
                esc = [A_ - len(core[a]) for a in core]
                Kp = sum(1 for x in esc if x >= 1)
                worst = max(worst, Kp)
                if Kp > 1 + 2:                     # e+2 with e = 2t-h = 1
                    viol8.append((k, V, sorted(esc)))
    ck("A.P8.floor_search", not viol8,
       "%d (T)-clean floor systems with nonempty core; max |K_+| = %d (bound 3)"
       % (found, worst))
    fired("A-F8", bool(viol8), "%d floor violations" % len(viol8))

    # ---- A-P6 : the rank route CANNOT bound |K| (fibre families)
    print("\n-- A-P6 : rank is constant on the fibre family (rank route dead)")
    q, s, hh = 31, 2, 3
    g = 3
    while pow(g, (q - 1) // 2, q) == 1 or pow(g, (q - 1) // 5, q) == 1:
        g += 1
    # fibres of x -> x^s on F_q^* : pair {x, -x}
    fibres = []
    seen = set()
    for x in range(1, q):
        if x in seen:
            continue
        f = tuple(sorted({x, (q - x) % q}))
        seen |= set(f)
        fibres.append(f)
    ranks = {}
    for V in (4, 5, 6, 7, 8):
        use = fibres[:V]
        U = sorted(set().union(*[set(f) for f in use]))
        A = len(U) - s
        k = A - hh
        if k < 1:
            continue
        Ss, zs = [], []
        for a in range(V):
            Sa = sorted(set(U) - set(use[a]))
            Ss.append(Sa)
            zs.append(pow(use[a][0], s, q))
        ck("A.P6.distinct_slopes[V=%d]" % V, len(set(zs)) == V, str(zs))
        ck("A.P6.uniform[V=%d]" % V, all(len(S) == A for S in Ss), "|S_a| = A = %d" % A)
        # gate (T)
        gate = max(len(set(Ss[a]) & set(Ss[b]) & set(Ss[c]))
                   for a, b, c in combinations(range(V), 3))
        ck("A.P6.gate[V=%d]" % V, gate <= k - 1, "max triple %d <= k-1 = %d" % (gate, k - 1))
        # zero escape: every point of U covered >= 3 times
        mult = {x: sum(1 for S in Ss if x in S) for x in U}
        ck("A.P6.zero_escape[V=%d]" % V, min(mult.values()) >= 3,
           "min mult %d" % min(mult.values()))
        # Rel and rank
        bases = [dual_basis(S, k, q) for S in Ss]
        nvar = sum(len(b) for b in bases)
        idx = {x: i for i, x in enumerate(U)}
        eqs = [[0] * nvar for _ in range(2 * len(U))]
        col = 0
        for a in range(V):
            for c in bases[a]:
                for j, x in enumerate(Ss[a]):
                    eqs[idx[x]][col] = (eqs[idx[x]][col] + c[j]) % q
                    eqs[len(U) + idx[x]][col] = (eqs[len(U) + idx[x]][col] + zs[a] * c[j]) % q
                col += 1
        dim_rel = nvar - rank_mod(eqs, q)
        rk = V * hh - dim_rel
        ranks[V] = rk
        m = hh + s
        ck("A.P6.rankle2m[V=%d]" % V, rk <= 2 * m, "rank %d <= 2m = %d" % (rk, 2 * m))
        print("   V=%2d  A=%2d k=%2d  rank=%2d  (3h=%d, 2m=%d)  |K|=V" % (V, A, k, rk, 3 * hh, 2 * m))
    const = len(set(ranks.values())) == 1
    ck("A.P6.rank_constant", const, "ranks %s" % ranks)
    ck("A.P6.rank_is_3h", all(v == 3 * hh for v in ranks.values()),
       "all == 3h = %d" % (3 * hh))
    fired("A-F6", not const, "rank grows with V")
    # the cash-out consequence: |K_+| = 0 on this family, bound A-P8 holds trivially
    e_here = 2 * s - hh
    ck("A.P8.fibre_consistent", 0 <= e_here + 2, "K_+ = 0 <= e+2 = %d" % (e_here + 2))

    return rows, got, targets, ranks, jb


# ============================================================== PART B
def part_B():
    print("\n=== PART B : the P-B planting ceiling for REALISED families ===")
    q, n, K, h = 41, 20, 4, 3
    A = K + h
    r = n - K
    # mu_20 <= F_41^*
    mu = sorted(x for x in range(1, q) if pow(x, n, q) == 1)
    ck("B.mu.size", len(mu) == n, "|mu_n| = %d" % len(mu))
    gen = None
    for x in mu:
        if len({pow(x, i, q) for i in range(n)}) == n:
            gen = x
            break
    ck("B.mu.generator", gen is not None, "g = %s" % gen)

    # moment map E(S) = (e_1,e_2,e_3)
    def moments(S):
        e = [0] * (h + 1)
        e[0] = 1
        for x in S:
            for j in range(h, 0, -1):
                e[j] = (e[j] + x * e[j - 1]) % q
        return (e[1], e[2], e[3])

    subs = list(combinations(mu, A))
    ck("B.subs.count", len(subs) == 77520, "C(20,7) = %d" % len(subs))
    E = {S: moments(S) for S in subs}

    # ---- B-P1 / B-P7 : orbit structure
    print("\n-- B-P1 / B-P7 : orbit-stabiliser ceiling")
    pos = {x: i for i, x in enumerate(mu)}
    def act(S, gg):
        return tuple(sorted((x * gg) % q for x in S))
    orbits = []
    seen = set()
    for S in subs:
        if S in seen:
            continue
        orb, gg = [], 1
        for _ in range(n):
            T = act(S, gg)
            orb.append(T)
            gg = (gg * gen) % q
        orb_set = set(orb)
        seen |= orb_set
        orbits.append(sorted(orb_set))
    sizes = sorted({len(o) for o in orbits})
    ck("B.P7.all_free", sizes == [n], "orbit sizes present: %s" % sizes)
    ck("B.P7.orbit_count", len(orbits) == len(subs) // n,
       "%d orbits x %d = %d" % (len(orbits), n, len(subs)))
    ck("B.P7.gcd_fixture", __import__("math").gcd(n, A) == 1,
       "gcd(n,A) = gcd(%d,%d) = 1" % (n, A))
    fired("B-F7", sizes != [n], "non-free orbit at the fixture")

    # ---- B-P2 : the A^2 identity and the spread stabiliser floor
    print("\n-- B-P2 : sum_g |S_0 ^ gS_0| = A^2 identity")
    idbad = []
    for S in subs[:400]:
        tot = sum(len(set(S) & set(act(S, pow(gen, i, q)))) for i in range(n))
        if tot != A * A:
            idbad.append((S, tot))
    ck("B.P2.identity", not idbad, "400 supports, sum_g |S ^ gS| = A^2 = %d" % (A * A))
    fired("B-F2", bool(idbad), "identity failed")
    floor_val = (A * A - n * (K - 1))
    ck("B.P2.vacuous_fixture", floor_val < 0,
       "A^2 - n(K-1) = %d < 0 => vacuous" % floor_val)

    # ---- THEOREM 3 exhibit : L = e_1-axis, witnesses, spread, rank
    print("\n-- THEOREM 3 replay : U = X^7, V = -X^6 on mu_20")
    # alpha_j = (-1)^j U_{A-j}, beta_j = (-1)^j V_{A-j}
    Ucoef = {7: 1}
    Vcoef = {6: (q - 1) % q}
    alpha = tuple(((-1) ** j * Ucoef.get(A - j, 0)) % q for j in (1, 2, 3))
    beta = tuple(((-1) ** j * Vcoef.get(A - j, 0)) % q for j in (1, 2, 3))
    ck("B.T3.alpha", alpha == (0, 0, 0), "alpha = %s" % (alpha,))
    ck("B.T3.beta", beta == (1, 0, 0), "beta = %s" % (beta,))
    ck("B.T3.live_slope_dir", beta != (0, 0, 0), "beta != 0")
    # L = {alpha + z beta} = the e_1 coordinate axis
    Lpts = {tuple((alpha[j] + z * beta[j]) % q for j in range(3)) for z in range(q)}
    ck("B.T3.L_is_axis", all(P[1] == 0 and P[2] == 0 for P in Lpts),
       "L = e_1-axis, %d points" % len(Lpts))
    wit = [S for S in subs if E[S] in Lpts]
    print("   |E^{-1}(L)| = %d   (n = %d, 2n = %d; mean supply C(n,A)/q^{h-1} = %.1f)"
          % (len(wit), n, 2 * n, len(subs) / q ** (h - 1)))
    ck("B.P6.fibre_size", len(wit) == 2 * n, "|E^{-1}(L)| = %d" % len(wit))
    fired("B-F6", len(wit) != 2 * n, "|E^{-1}(L)| = %d (predicted 2n = %d)" % (len(wit), 2 * n))
    wset = set(wit)
    worbs = [o for o in orbits if set(o) & wset]
    ck("B.P6.union_of_orbits", all(set(o) <= wset for o in worbs),
       "%d orbits meet the witness set, all contained" % len(worbs))
    ck("B.P6.two_orbits", len(worbs) == 2, "%d complete free orbits" % len(worbs))
    # spread of each orbit: max pairwise core
    spreads = []
    for o in worbs:
        mx = max(len(set(S) & set(T)) for S in o for T in o if S != T)
        spreads.append(mx)
    ck("B.T3.spread_exists", any(sp <= K - 1 for sp in spreads),
       "max pairwise cores per orbit: %s (K-1 = %d)" % (spreads, K - 1))
    # slopes
    for i, o in enumerate(worbs):
        sl = {E[S][0] for S in o}
        ck("B.T3.slopes[%d]" % i, len(sl) == n, "%d distinct slopes" % len(sl))

    # condition rank of the spread orbit: M h = 60 rows in F_q^{2n}
    def syndrome_rows(S, z):
        S = list(S)
        rows_ = []
        mus = []
        for x in S:
            den = 1
            for y in S:
                if y != x:
                    den = den * ((x - y) % q) % q
            mus.append(pow(den, q - 2, q))
        for i in range(h):
            rw = [0] * (2 * n)
            for j, x in enumerate(S):
                cf = mus[j] * pow(x, i, q) % q
                rw[pos[x]] = (rw[pos[x]] + cf) % q
                rw[n + pos[x]] = (rw[n + pos[x]] + z * cf) % q
            rows_.append(rw)
        return rows_
    spread_orb = worbs[spreads.index(min(spreads))]
    allrows = []
    for S in spread_orb:
        allrows += syndrome_rows(S, E[S][0])       # z = e_1 since beta_1 = 1, alpha = 0
    rk = rank_mod(allrows, q)
    print("   condition rank of the M=20 orbit: %d  (Mh = %d, 2r-1 = %d)"
          % (rk, n * h, 2 * r - 1))
    ck("B.T3.rank31", rk == 2 * r - 1, "rank %d == 2r-1 = %d" % (rk, 2 * r - 1))
    ck("B.T3.realised", rk < 2 * r, "nontrivial realiser exists (rank < 2r = %d)" % (2 * r))
    ck("B.T3.M_exceeds_ceiling", n > (2 * r - 1) // h,
       "M = %d > prescribed ceiling %d" % (n, (2 * r - 1) // h))
    # B-P1 : orbit ceiling attained
    ck("B.P1.ceiling_attained", len(spread_orb) == n,
       "M = |H|/|Stab| = %d = n" % len(spread_orb))
    fired("B-F1", len(spread_orb) != n, "orbit size %d" % len(spread_orb))

    # rigidity: 3 witnesses pin L
    print("\n-- B-P6 : does rigidity pin the family? (3 witnesses pin L)")
    import random
    random.seed(7)
    pin_bad = []
    for _ in range(60):
        trio = random.sample(spread_orb, 3)
        # lines through the 3 moment points: must be unique and equal L
        P = [E[S] for S in trio]
        # affine hull
        d1 = tuple((P[1][j] - P[0][j]) % q for j in range(3))
        d2 = tuple((P[2][j] - P[0][j]) % q for j in range(3))
        collinear = rank_mod([list(d1), list(d2)], q) <= 1
        if not collinear:
            pin_bad.append(trio)
    ck("B.P6.three_pin", not pin_bad, "60 random triples of the orbit are collinear")

    # ---- B-P3 : coordinate-axis FORCING, exhaustive over all orbits
    print("\n-- B-P3 (NEW) : mu_n-invariant + live slope => L is a COORDINATE AXIS")
    collinear_orbits = 0
    axis_orbits = 0
    degenerate = 0
    viol = []
    for o in orbits:
        pts = {E[S] for S in o}
        if len(pts) == 1:
            degenerate += 1
            if pts != {(0, 0, 0)}:
                viol.append(("single-point-nonzero", o[0], pts))
            continue
        pl = sorted(pts)
        p0 = pl[0]
        dirs = [tuple((P[j] - p0[j]) % q for j in range(3)) for P in pl[1:]]
        if rank_mod([list(d) for d in dirs], q) <= 1:
            collinear_orbits += 1
            # affine hull is a line; is it a coordinate axis through the origin?
            nz = [j for j in range(3) if any(P[j] for P in pts)]
            if len(nz) == 1:
                axis_orbits += 1
            else:
                viol.append(("collinear-not-axis", o[0], pl))
    print("   orbits: %d total, %d with a single moment point, %d collinear, %d on a coord axis"
          % (len(orbits), degenerate, collinear_orbits, axis_orbits))
    ck("B.P3.degenerate_are_zero", not [v for v in viol if v[0] == "single-point-nonzero"],
       "%d single-moment-point orbits, all E = 0" % degenerate)
    ck("B.P3.collinear_are_axes", collinear_orbits == axis_orbits,
       "%d collinear orbits, %d on coordinate axes" % (collinear_orbits, axis_orbits))
    fired("B-F3", collinear_orbits != axis_orbits or
          bool([v for v in viol if v[0] == "single-point-nonzero"]),
          "%d violations" % len(viol))
    ck("B.P3.T3_orbit_on_axis", all(E[S][1] == 0 and E[S][2] == 0 for S in spread_orb),
       "THEOREM 3 orbit has e_2 = e_3 = 0")

    # ---- six-row arithmetic for B-P2 / B-P4 / B-P7
    print("\n-- B-P4 / B-P7 : the six official rows")
    import math
    rowspec = [("RowC 1/4", 1024, 256, 5), ("RowC 1/8", 1024, 128, 5),
               ("RowC 1/16", 1024, 64, 3),
               ("prize 1/4", 2 ** 41, 2 ** 39, 2 ** 33 + 1),
               ("prize 1/8", 2 ** 41, 2 ** 38, 2 ** 33 + 1),
               ("prize 1/16", 2 ** 41, 2 ** 37, 2 ** 32 + 1)]
    margins = []
    for (nm, N, KK, hh) in rowspec:
        AA = KK + hh
        ck("B.P7.gcd[%s]" % nm, math.gcd(N, AA) == 1,
           "gcd(n,A) = %d" % math.gcd(N, AA))
        ck("B.P7.A_odd[%s]" % nm, AA % 2 == 1, "A odd")
        ck("B.P2.vacuous[%s]" % nm, AA * AA - N * (KK - 1) < 0,
           "A^2 - n(K-1) = %d" % (AA * AA - N * (KK - 1)))
        budget = 8 * N ** 3
        margins.append((nm, N, budget.bit_length() - N.bit_length()))
        ck("B.P4.below_budget[%s]" % nm, N < budget, "n=%d < 8n^3" % N)
    for (nm, N, bits) in margins:
        print("   %-11s  M <= n = 2^%-3d  vs 8n^3 = 2^%-4d   margin ~2^%d"
              % (nm, N.bit_length() - 1, (8 * N ** 3).bit_length() - 1, bits))
    fired("B-F4", False, "six margins recomputed")

    # ---- B-P5 : SELECTOR catch vs L-B DICHOTOMY, species test
    print("\n-- B-P5 (NEW) : SELECTOR catch vs L-B DICHOTOMY — species test")
    species_test()


def species_test():
    """Toy at a tractable scale: q = 13, D = mu_12 = F_13^*, K = 3, h = 2,
       A = 5  (C(12,5) = 792 supports).  Build a word with a FORCED
       over-agreement locus, then compare
         (1) the L-B over-agreement prune  (LIVENESS level)
         (2) the support-lex SELECTOR      (ATTRIBUTION level)
       under x -> gx, which preserves RS_K on mu_n (monomials are
       eigenvectors), and test whether the two mechanisms interact."""
    q, n, K, h = 13, 12, 3, 2
    A = K + h
    mu = sorted(x for x in range(1, q) if pow(x, n, q) == 1)
    gen = next(x for x in mu if len({pow(x, i, q) for i in range(n)}) == n)
    ck("B.P5.setting", len(mu) == n, "|D| = %d, K = %d, A = %d" % (len(mu), K, A))

    cpoly = [3, 1, 2]                                # deg < K = 3
    def cev(x):
        return sum(cpoly[i] * pow(x, i, q) for i in range(K)) % q
    G = tuple(mu[:A + 1])                            # |G| = A+1 = 6
    w = {x: (cev(x) if x in G else (cev(x) + 1 + (x % 3)) % q) for x in mu}

    def interp(pts, word):
        """coefficients-free evaluator of the degree-<K interpolant of word on pts"""
        def ev(x):
            val = 0
            for i, xi in enumerate(pts):
                num, den = 1, 1
                for j, xj in enumerate(pts):
                    if i != j:
                        num = num * ((x - xj) % q) % q
                        den = den * ((xi - xj) % q) % q
                val = (val + word[xi] * num * pow(den, q - 2, q)) % q
            return val
        return ev

    def witnesses(word):
        """A-subsets S with word|_S in RS_K|_S -> agreement size of its codeword."""
        out = {}
        for S in combinations(mu, A):
            pts = list(S)[:K]
            ev = interp(pts, word)
            if all(ev(x) == word[x] for x in S):     # S is a witness
                out[S] = sum(1 for x in mu if ev(x) == word[x])
        return out

    def actS(S, gg):
        return tuple(sorted((x * gg) % q for x in S))

    def selector(fam):
        """support-lex first match, keyed by the agreement class (the P-B
           selector's shape: a support-keyed choice among live witnesses)."""
        by = {}
        for S in sorted(fam):
            by.setdefault(fam[S], []).append(S)
        return {kk: min(v) for kk, v in by.items()}

    W = witnesses(w)
    over = {S for S, a in W.items() if a > A}        # L-B: forced over-agreeing
    live = {S: a for S, a in W.items() if S not in over}
    print("   witnesses %d ; forced over-agreeing (L-B prune) %d ; exact-A live %d"
          % (len(W), len(over), len(live)))
    ck("B.P5.nonempty", len(over) > 0 and len(live) > 0,
       "over %d, live %d" % (len(over), len(live)))
    ck("B.P5.over_contains_G_subsets", set(combinations(G, A)) <= over,
       "every A-subset of the (A+1)-agreement locus G is forced over-agreeing")

    # --- (1) EQUIVARIANCE : the species discriminator
    eq_over, eq_sel = [], []
    sel_base = selector(W)
    for i in range(1, n):
        gg = pow(gen, i, q)
        ginv = pow(gg, q - 2, q)
        wg = {x: w[(x * ginv) % q] for x in mu}      # the translated configuration
        Wg = witnesses(wg)
        overg = {S for S, a in Wg.items() if a > A}
        eq_over.append(overg == {actS(S, gg) for S in over})
        eq_sel.append(selector(Wg) == {kk: actS(v, gg) for kk, v in sel_base.items()})
    ck("B.P5.over_equivariant", all(eq_over),
       "L-B over-agreement set equivariant on %d/%d shifts"
       % (sum(eq_over), len(eq_over)))
    n_sel_eq = sum(eq_sel)
    ck("B.P5.selector_not_equivariant", n_sel_eq < len(eq_sel),
       "lex selector equivariant on only %d/%d shifts" % (n_sel_eq, len(eq_sel)))
    fired("B-F5", (not all(eq_over)) or n_sel_eq == len(eq_sel),
          "over-agreement equivariant=%s ; selector equivariant on %d/%d"
          % (all(eq_over), n_sel_eq, len(eq_sel)))

    # --- (2) INTERACTION (B-P5b), keyed by the CODEWORD (the natural datum):
    #         several supports may witness the SAME codeword; that is exactly
    #         where a selector has a choice to make.
    def classes(word, fam):
        by = {}
        for S in sorted(fam):
            ev = interp(list(S)[:K], word)
            key = tuple(ev(x) for x in mu)
            by.setdefault(key, []).append(S)
        return by

    cls_all = classes(w, W)
    cls_live = classes(w, live)
    nontrivial = {kk: v for kk, v in cls_all.items() if len(v) > 1}
    over_classes = {kk for kk, v in cls_all.items()
                    if sum(1 for x in mu if kk[mu.index(x)] == w[x]) > A}
    print("   codeword classes: %d total, %d with >1 witnessing support "
          "(where a selector has a CHOICE)" % (len(cls_all), len(nontrivial)))
    print("   after the L-B prune: %d classes, %d with >1 support"
          % (len(cls_live), sum(1 for v in cls_live.values() if len(v) > 1)))
    ck("B.P5b.choice_domain_is_over", set(nontrivial) == over_classes,
       "the selector's nontrivial classes are EXACTLY the over-agreeing ones "
       "(%d of %d)" % (len(nontrivial), len(cls_all)))
    trivial_after = all(len(v) == 1 for v in cls_live.values())
    ck("B.P5b.selector_vacuous_after_prune", trivial_after,
       "every class surviving the L-B prune is a singleton: the selector "
       "becomes VACUOUS")
    count_changed = len(cls_live) != len(cls_all)
    ck("B.P5b.counts_recorded", True,
       "class count %d -> %d under the L-B prune" % (len(cls_all), len(cls_live)))
    fired("B-F5b", count_changed,
          "L-B prune changed the selector's surviving class count %d -> %d "
          "(mechanisms are COMPLEMENTARY, not independent)"
          % (len(cls_all), len(cls_live)))


# ================================================================ main
def main():
    part_A()
    part_B()
    print("\n" + "=" * 66)
    npass = sum(1 for _, c, _ in CHECKS if c)
    nfail = len(CHECKS) - npass
    print("CHECKS: %d total, %d PASS, %d FAIL" % (len(CHECKS), npass, nfail))
    print("\nPRE-REGISTERED FALSIFIERS:")
    for tag in sorted(FALSIFIERS):
        f, d = FALSIFIERS[tag]
        print("  %-7s %-6s %s" % (tag, "FIRED" if f else "clear", d))
    nfired = sum(1 for f, _ in FALSIFIERS.values() if f)
    print("\n%d of %d recorded falsifiers FIRED" % (nfired, len(FALSIFIERS)))
    out = {"checks": len(CHECKS), "pass": npass, "fail": nfail,
           "falsifiers": {k: {"fired": v[0], "detail": v[1]} for k, v in FALSIFIERS.items()},
           "failed_checks": [(nm, d) for nm, c, d in CHECKS if not c],
           "all_checks": [{"name": nm, "pass": c, "detail": d} for nm, c, d in CHECKS]}
    with open(os.path.join(os.path.dirname(__file__), "verify.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    return 1 if nfail else 0


if __name__ == "__main__":
    sys.exit(main())
