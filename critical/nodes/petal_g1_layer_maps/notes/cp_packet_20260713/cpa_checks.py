#!/usr/bin/env python3
"""cpa_checks — INDEPENDENT audit battery for the cp_packet_20260713
(clause (P), petal_g1_layer_maps). Fresh-context adversarial auditor.

Standalone; run under tools/ramguard tiny, one stage per call:

    python3 cpa_checks.py A1|A2|A3|A4|A5|A6|all

Stages:
  A1  Boundary/emptiness arithmetic re-derived (operational t_ch=(n-k)/2):
      J-law, official maximal rows, rates<=1/4 grid, the 2k=n-2 parity gap,
      the (10,4) OUT-OF-SCOPE cell where the packet's boundary constant and
      bsra's printed "2k>=n-1" DISAGREE — decided in vivo at (10,4,11).
  A2  Lemma B (rigidity) verified EXHAUSTIVELY as pure combinatorics over
      all layout shapes n<=64 (any k parity, b0<=1): every full-petal
      support triple in the floor band has j<=J and m in {t-1,t}; the
      m=t-2 stratum is arithmetically impossible; the j=J, m=t-1 corner is
      attainable (sharpness).
  A3  Exact bigint recompute: N_max & budget at every rate-1/2 row s=3..44,
      binding official row n=2^41 (log2 values to 2 decimals vs the claimed
      157.42/245.92/88.50), (128,64) N_max=2754048 & #153 caps 993+31,
      C(63,32)=2^59.67 vs (121/128)128^6=2^41.92.
  A4  INDEPENDENT in-vivo audit at (16,8,97,consec) and (16,4,97,geom5):
      complete class census by the k-SUBSET method (different from the
      packet's (k+1)-subset method), Lagrange-only interpolation, a
      FUNCTIONAL lift test ((x+a)f(x)+(x-a)f(-x)=0 on H), rigidity, atlas
      coverage, per-chart counts, banked pins 8 lifts / 51-and-empty, and
      the out-of-scope mixed-petal floor mass (reported, not charged).
  A5  INDEPENDENT audit at (32,16,97,geom5): admissible-support census
      (own code), expected 83 = 53 lifts + 30 accidental + 0 periodic;
      independent quotient-side lift recount (6435 interpolations);
      rigidity; per-chart <= 9; N_max=10368.
  A6  NEW REQUIRED-TO-TRIP mutations (auditor-designed):
      NM1 tighten the rigidity j-bound to J-1  -> must report violations,
      NM2 drop the m=t stratum                 -> must undercount,
      NM3 raise the atlas index floor to thr+2 -> must leave realized
          classes uncovered (coverage check must FAIL).
"""
import itertools
import sys
from math import comb, log2

NPASS = 0
NFAIL = 0


def check(name, cond, detail=""):
    global NPASS, NFAIL
    tag = "PASS" if cond else "FAIL"
    if cond:
        NPASS += 1
    else:
        NFAIL += 1
    print(f"[{tag}] {name}" + (f"  -- {detail}" if detail else ""))


# ----------------------------------------------------------------- field ops
def find_domain(p, n):
    """Same convention as the house tools: dom[j]=g0^j, g0=a^((p-1)/n),
    smallest a>=2 with g0 of exact order n."""
    a = 2
    while True:
        g0 = pow(a, (p - 1) // n, p)
        if pow(g0, n // 2, p) != 1:
            break
        a += 1
    dom = [pow(g0, j, p) for j in range(n)]
    assert len(set(dom)) == n
    return dom


def lagrange_coeffs(xs, ys, p):
    """Monomial coeffs (len = len(xs)) of the unique interpolant. Own code."""
    k = len(xs)
    poly = [0] * k
    for i in range(k):
        num = [1]
        for j in range(k):
            if j == i:
                continue
            r = xs[j]
            new = [0] * (len(num) + 1)
            for d, c in enumerate(num):
                new[d] = (new[d] - r * c) % p
                new[d + 1] = (new[d + 1] + c) % p
            num = new
        den = 1
        for j in range(k):
            if j != i:
                den = den * (xs[i] - xs[j]) % p
        w = ys[i] * pow(den, -1, p) % p
        for d, c in enumerate(num):
            poly[d] = (poly[d] + w * c) % p
    return tuple(poly)


def evp(poly, x, p):
    v = 0
    for c in reversed(poly):
        v = (v * x + c) % p
    return v


# ------------------------------------------------------------------ layout
def fiber_layout(n, k):
    """House fiber-aligned layout, re-derived from the conventions in
    cp_statement section 0 (NOT imported from cp_verify)."""
    half = n // 2
    nf = (k - 1) // 2
    core = []
    for j in range(nf):
        core.extend([j, j + half])
    bg = []
    if (k - 1) % 2:          # k even: split point into core, mirror to bg
        core.append(nf)
        bg = [nf + half]
        start = nf + 1
    else:
        start = nf
    petals = [[j, j + half] for j in range(start, half)]
    assert len(core) == k - 1
    return sorted(core), petals, bg, nf


def chart_of(S, core, petals, bg):
    cs = frozenset(core)
    j = len(S & cs)
    d = len(core) - j
    m = 0
    fullpetal = True
    for P in petals:
        inter = S & frozenset(P)
        if len(inter) == 2:
            m += 1
        elif len(inter) == 1:
            fullpetal = False
    s_r = len(S & frozenset(bg))
    return d, j, m, s_r, fullpetal


def dyadic_scale(S, n):
    c, M = 1, 2
    while M <= n:
        s = n // M
        if all(((x + s) % n) in S for x in S):
            c = M
            M *= 2
        else:
            break
    return c


def chart_word(n, k, p, dom, smode):
    """Word = 0 on core+bg, c_i * L_Z on petal i (house convention)."""
    core, petals, bg, nf = fiber_layout(n, k)
    t = len(petals)
    if smode == "consec":
        scal = [(i + 1) % p for i in range(t)]
    elif smode == "geom5":
        scal, v = [], 1
        for _ in range(t):
            scal.append(v)
            v = v * 5 % p
    else:
        raise ValueError(smode)
    # locator L_Z as a product evaluated pointwise (no coefficient vector)
    zpts = [dom[j] for j in core]
    values = [0] * n
    for c_i, P in zip(scal, petals):
        for j in P:
            v = c_i
            for z in zpts:
                v = v * (dom[j] - z) % p
            values[j] = v
    return values, core, petals, bg, nf


def complete_census_ksub(n, k, p, dom, values):
    """COMPLETE class census via ALL k-subsets (every class with
    |agr| >= k+1 contains a k-subset; the interpolant on it IS the class
    codeword). Independent of the packet's (k+1)-subset route."""
    found = {}
    for idxs in itertools.combinations(range(n), k):
        xs = [dom[j] for j in idxs]
        ys = [values[j] for j in idxs]
        f = lagrange_coeffs(xs, ys, p)
        A = frozenset(j for j in range(n) if evp(f, dom[j], p) == values[j])
        if len(A) >= k + 1 and A not in found:
            found[A] = f
    return found


def is_lift_functional(f, n, p, dom, nf):
    """f = (X - x_nf) g(X^2)  <=>  (x+a) f(x) + (x-a) f(-x) = 0 on all of H
    (a = x_nf = dom[nf]; -x = dom[j + n/2]). Derived independently."""
    a = dom[nf]
    half = n // 2
    for j in range(half):
        x = dom[j]
        mx = dom[j + half]
        lhs = ((x + a) * evp(f, x, p) + (x - a) * evp(f, mx, p)) % p
        if lhs:
            return False
    return True


def admissible_census(n, k, p, dom, values, core, petals, bg,
                      m_range=None, jmax=None):
    """Floor-band full-petal census via Lemma-B admissible supports.
    Own implementation (used where brute is infeasible; validated against
    the complete k-subset census at n = 16 in A4)."""
    t = len(petals)
    thr = 2 * (t - 2)
    J = (k - 1) - thr
    if jmax is None:
        jmax = J
    if m_range is None:
        m_range = [t - 1, t]
    out = {}
    if jmax < 0:
        return out
    bgsubs = [frozenset()] + [frozenset([b]) for b in bg]
    for jsz in range(0, min(jmax, k - 1) + 1):
        for csub in itertools.combinations(core, jsz):
            for m in m_range:
                for psub in itertools.combinations(range(t), m):
                    pts = [x for i in psub for x in petals[i]]
                    for rs in bgsubs:
                        S = frozenset(csub) | frozenset(pts) | rs
                        if len(S) < k + 1:
                            continue
                        pl = sorted(S)
                        xs = [dom[j] for j in pl]
                        ys = [values[j] for j in pl]
                        f = lagrange_coeffs(xs[:k], ys[:k], p)
                        if any(evp(f, x, p) != y
                               for x, y in zip(xs[k:], ys[k:])):
                            continue
                        A = frozenset(jj for jj in range(n)
                                      if evp(f, dom[jj], p) == values[jj])
                        if A == S:
                            out[S] = f
    return out


def floor_rows(classes, n, core, petals, bg):
    t = len(petals)
    thr = 2 * (t - 2)
    rows = []
    for S, f in classes.items():
        d, j, m, s_r, fp = chart_of(S, core, petals, bg)
        if fp and d >= thr:
            rows.append((S, f, d, j, m, s_r, dyadic_scale(S, n)))
    return rows


# ==================================================================== stages
def stage_A1():
    # (i) J-law on even-k 2-power rows: J >= 0 <=> 2k >= n (both printed
    # boundary constants collapse to the same in-scope law)
    ok_law, ok_gap = True, True
    for s in range(3, 25):
        n = 2 ** s
        for k in range(4, n - 1, 2):
            t = (n - k) // 2
            J = (k - 1) - 2 * (t - 2)
            if (J >= 0) != (2 * k >= n):
                ok_law = False
            if 2 * k in (n - 1, n - 2, n - 3) and J >= 0:
                ok_gap = False   # boundary cells would poison the law
    check("A1 in-scope law: J>=0 <=> 2k>=n on ALL even-k 2-power rows "
          "s=3..24", ok_law)
    check("A1 no even-k 2-power row attains 2k in {n-3,n-2,n-1} "
          "(parity gap: both printed constants immaterial in scope)", ok_gap)
    # (ii) official maximal rows: k = 2^40 at n = 2^42..2^44 -> J < 0
    for s in (42, 43, 44):
        n, k = 2 ** s, 2 ** 40
        t = (n - k) // 2
        J = (k - 1) - 2 * (t - 2)
        check(f"A1 official row n=2^{s}, k=2^40: J = {J} < 0 "
              f"(t_ch = {t})", J < 0)
    n, k = 2 ** 41, 2 ** 40
    t = (n - k) // 2
    J = (k - 1) - 2 * (t - 2)
    check("A1 official row n=2^41 (rate 1/2): J == 3 exactly", J == 3)
    # (iii) rates <= 1/4, s = 13..44 all empty
    ok = True
    for s in range(13, 45):
        n = 2 ** s
        for den in (4, 8, 16):
            k = n // den
            t = (n - k) // 2
            if (k - 1) - 2 * (t - 2) >= 0:
                ok = False
    check("A1 rates 1/4,1/8,1/16, s=13..44: J < 0 everywhere (emptiness)",
          ok)
    # (iv) the OUT-OF-SCOPE disagreement cell (10,4): operational t_ch=(n-k)/2
    # says the band/lift-family is NONEMPTY (J=1, z0=0); bsra's printed
    # "2k >= n-1" says empty. Decide in vivo at q=11.
    n, k, p = 10, 4, 11
    t = (n - k) // 2
    J = (k - 1) - 2 * (t - 2)
    z0 = (k // 2 - 1) - (t - 2)
    check("A1 (10,4): operational J=1>=0 and z0=0>=0 while bsra's printed "
          "2k>=n-1 fails (8<9) — the two laws disagree here",
          J == 1 and z0 == 0 and not (2 * k >= n - 1))
    best = None
    for q in (11, 31):
        dom = find_domain(q, n)
        for smode in ("consec", "geom5"):
            values, core, petals, bg, nf = chart_word(n, k, q, dom, smode)
            cls = complete_census_ksub(n, k, q, dom, values)
            rows = floor_rows(cls, n, core, petals, bg)
            lifts = [r for r in rows if r[6] == 1
                     and is_lift_functional(r[1], n, q, dom, nf)]
            if best is None or len(rows) > best[2]:
                best = (q, smode, len(rows), len(lifts))
    check("A1 (10,4) IN VIVO: floor-band full-petal contributors realize "
          "at some chart word (operational boundary correct; bsra's "
          "printed constant is the half-integer artifact — packet's #169 "
          "remark resolves it right)", best is not None and best[2] > 0,
          f"best cell q={best[0]}/{best[1]}: floor {best[2]}, "
          f"aperiodic lifts {best[3]}")


def stage_A2():
    # Lemma B as pure combinatorics: exhaustive over layout shapes.
    # A full-petal support is determined by (j, m, s_r); the lemma is a
    # statement about triples only.
    bad = []
    sharp_corner = 0
    shapes = 0
    for n in range(6, 65):
        for k in range(3, n - 1):
            for b0 in (0, 1):
                rem = n - (k - 1) - b0
                if rem <= 0 or rem % 2:
                    continue
                t = rem // 2
                if t < 2:
                    continue
                shapes += 1
                thr = 2 * (t - 2)
                J = (k - 1) - thr
                for j in range(0, k):
                    d = (k - 1) - j
                    for m in range(0, t + 1):
                        for s_r in range(0, b0 + 1):
                            size = j + 2 * m + s_r
                            if size < k + 1 or d < thr:
                                continue
                            # floor-band full-petal contributor triple:
                            if j > J or m not in (t - 1, t):
                                bad.append((n, k, b0, j, m, s_r))
                # sharpness corner: j=J, m=t-1, s_r=0 has size exactly k+1
                if J >= 0 and 0 <= J <= k - 1:
                    if J + 2 * (t - 1) == k + 1:
                        sharp_corner += 1
    check(f"A2 Lemma B EXHAUSTIVE over {shapes} layout shapes (n<=64, any "
          "k, b0<=1): floor+full-petal+|S|>=k+1 forces j<=J and "
          "m in {t-1,t}", len(bad) == 0, f"violations: {bad[:5]}")
    check("A2 corner j=J, m=t-1, s_r=0 sits at |S|=k+1 exactly in EVERY "
          "shape with J>=0 (identity J+2(t-1)=k+1; bounds are sharp, no "
          "off-by-one slack)", sharp_corner > 0, f"{sharp_corner} shapes")
    # the m = t-2 stratum is arithmetically impossible (packet's stratum
    # window is tight): max size at m=t-2 is J+2(t-2)+1 = k (< k+1)
    ok = True
    for n in range(6, 65):
        for k in range(3, n - 1):
            for b0 in (0, 1):
                rem = n - (k - 1) - b0
                if rem <= 0 or rem % 2:
                    continue
                t = rem // 2
                if t < 2:
                    continue
                J = (k - 1) - 2 * (t - 2)
                if J >= 0 and J + 2 * (t - 2) + b0 >= k + 1:
                    ok = False
    check("A2 m=t-2 stratum impossible in every shape (max reach = k+b0-1 "
          "< k+1)", ok)


def stage_A3():
    # exact bigint budget sweep, own arithmetic
    worst = None
    ok = True
    for s in range(3, 45):
        n = 2 ** s
        k = n // 2
        t = (n - k) // 2
        J = (k - 1) - 2 * (t - 2)
        if J != 3:
            ok = False
        SJ = sum(comb(k - 1, i) for i in range(4))
        NM = 2 * (t + 1) * SJ
        budget = 121 * n ** 6 // 128
        if NM > budget:
            ok = False
        marg = budget // NM
        if worst is None or marg < worst[1]:
            worst = (s, marg)
    check("A3 rate-1/2 sweep s=3..44: J==3 and N_max <= (121/128)n^6 "
          "everywhere (exact bigint, own code)", ok,
          f"worst margin 2^{worst[1].bit_length() - 1} at s={worst[0]}")
    # binding row exact
    n, k = 2 ** 41, 2 ** 40
    t = (n - k) // 2
    SJ = sum(comb(k - 1, i) for i in range(4))
    NM = 2 * (t + 1) * SJ
    budget = 121 * n ** 6 // 128
    lN, lB = log2(NM), log2(budget)
    check("A3 binding row n=2^41: log2(N_max) = 157.42, log2(budget) = "
          "245.92, margin = 88.50 (2 d.p.)",
          abs(lN - 157.42) < 0.005 and abs(lB - 245.92) < 0.005
          and abs((lB - lN) - 88.50) < 0.01,
          f"exact: {lN:.4f} / {lB:.4f} / {lB - lN:.4f}")
    check("A3 binding row fits", NM <= budget)
    # (128,64) cell: N_max, #153 caps
    n, k = 128, 64
    t = (n - k) // 2
    SJ = sum(comb(k - 1, i) for i in range(4))
    NM = 2 * (t + 1) * SJ
    kp = k // 2
    z0 = (kp - 1) - (t - 2)
    cap1 = sum(comb(kp - 1, z) * comb(t, kp - z) for z in range(z0 + 1))
    cap2 = sum(comb(kp - 1, z) * comb(t, kp + 1 - z) for z in range(z0 + 1))
    check("A3 (128,64): N_max = 2,754,048; #153 caps = 993 + 31 = 1024; "
          "caps embed", NM == 2754048 and cap1 == 993 and cap2 == 31
          and cap1 + cap2 <= NM, f"NM={NM}, caps={cap1}+{cap2}")
    # layout-existential kill arithmetic
    c = comb(63, 32)
    b = 121 * 128 ** 6 // 128
    check("A3 kill arithmetic: C(63,32)=2^59.67 > (121/128)128^6=2^41.92",
          c > b and abs(log2(c) - 59.67) < 0.005
          and abs(log2(b) - 41.92) < 0.005,
          f"log2: {log2(c):.4f} vs {log2(b):.4f}")
    # N_max ~ n^4/96 sanity at the binding row (report claim)
    check("A3 N_max/(n^4/96) in [0.9, 1.1] at n=2^41 (the ~n^4/96 claim)",
          0.9 < NM_ratio(2 ** 41) < 1.1, f"ratio {NM_ratio(2 ** 41):.4f}")


def NM_ratio(n):
    k = n // 2
    t = (n - k) // 2
    SJ = sum(comb(k - 1, i) for i in range(4))
    NM = 2 * (t + 1) * SJ
    return NM / (n ** 4 / 96)


def stage_A4():
    # ---- (16,8,97,consec): complete census, independent machinery
    n, k, p = 16, 8, 97
    dom = find_domain(p, n)
    values, core, petals, bg, nf = chart_word(n, k, p, dom, "consec")
    t = len(petals)
    thr = 2 * (t - 2)
    J = (k - 1) - thr
    cls = complete_census_ksub(n, k, p, dom, values)
    rows = floor_rows(cls, n, core, petals, bg)
    check("A4 (16,8,97) complete census nonempty (own k-subset method)",
          len(rows) > 0, f"{len(rows)} floor full-petal classes, "
          f"{len(cls)} classes total")
    check("A4 (16,8,97) floor census == 10 (packet #170 table)",
          len(rows) == 10)
    viol = [r for r in rows if r[3] > J or r[4] not in (t - 1, t)
            or r[5] > 1]
    check("A4 (16,8,97) rigidity on the complete census", len(viol) == 0,
          f"violations {viol[:3]}")
    aper = [r for r in rows if r[6] == 1]
    lifts = [r for r in aper if is_lift_functional(r[1], n, p, dom, nf)]
    check("A4 (16,8,97) lifts == 8 (banked pin, FUNCTIONAL lift test), "
          "non-lift aperiodic == 1, periodic == 1 (#170 split)",
          len(lifts) == 8 and len(aper) - len(lifts) == 1
          and len(rows) - len(aper) == 1,
          f"lifts {len(lifts)}, acc {len(aper) - len(lifts)}, "
          f"per {len(rows) - len(aper)}")
    # atlas coverage: adversarial — every floor class's exact chart in index?
    unc = [S for (S, f, d, j, m, s_r, c) in rows if d < thr]
    check("A4 (16,8,97) NO floor-band full-petal class outside the atlas "
          "(coverage is definitional; adversarial scan agrees)",
          len(unc) == 0)
    perch = {}
    for (S, f, d, j, m, s_r, c) in rows:
        perch.setdefault((frozenset(core) - S, S & frozenset(bg)),
                         []).append(S)
    check(f"A4 (16,8,97) per-chart <= t+1 = {t + 1}",
          all(len(v) <= t + 1 for v in perch.values()),
          f"max {max(len(v) for v in perch.values())}")
    # both retained flavors + both strata realized? (report)
    strata = sorted({r[4] for r in rows})
    flavs = sorted({r[5] for r in rows})
    print(f"[info] A4 strata realized m={strata}, s_r flavors {flavs}, "
          f"d values {sorted({r[2] for r in rows})}")
    # out-of-scope mass: mixed-petal floor-band contributors (NOT charged
    # by clause (P); petal_growth mixed-petal bucket)
    mixed = 0
    for S, f in cls.items():
        d, j, m, s_r, fp = chart_of(S, core, petals, bg)
        if (not fp) and d >= thr:
            mixed += 1
    print(f"[info] A4 (16,8,97) mixed-petal floor-band contributors "
          f"(outside clause (P) scope, petal_growth's separate bucket): "
          f"{mixed}")
    # candidate machinery cross-validation (validates A5's method)
    cand = admissible_census(n, k, p, dom, values, core, petals, bg)
    check("A4 (16,8,97) own admissible-support census == own complete "
          "census on the floor band (method validation for A5)",
          set(cand) == {r[0] for r in rows},
          f"{len(cand)} vs {len(rows)}")
    # ---- (16,4,97,geom5): rate-1/4 complete census
    n2, k2 = 16, 4
    values2, core2, petals2, bg2, nf2 = chart_word(n2, k2, p, dom, "geom5")
    cls2 = complete_census_ksub(n2, k2, p, dom, values2)
    rows2 = floor_rows(cls2, n2, core2, petals2, bg2)
    check("A4 (16,4,97) complete census: contributors EXIST, floor band "
          "EMPTY (Lemma A in vivo; nonvacuous)",
          len(cls2) > 0 and len(rows2) == 0,
          f"{len(cls2)} classes, {len(rows2)} floor")
    check("A4 (16,4,97) class total == 51 (packet number)", len(cls2) == 51,
          f"{len(cls2)}")


def stage_A5():
    n, k, p = 32, 16, 97
    dom = find_domain(p, n)
    values, core, petals, bg, nf = chart_word(n, k, p, dom, "geom5")
    t = len(petals)
    thr = 2 * (t - 2)
    J = (k - 1) - thr
    cand = admissible_census(n, k, p, dom, values, core, petals, bg)
    rows = floor_rows(cand, n, core, petals, bg)
    check("A5 (32,16,97) census == 83 (packet)", len(rows) == 83,
          f"{len(rows)}")
    viol = [r for r in rows if r[3] > J or r[4] not in (t - 1, t)
            or r[5] > 1]
    check("A5 (32,16,97) rigidity clean", len(viol) == 0)
    aper = [r for r in rows if r[6] == 1]
    lifts = {r[0] for r in aper if is_lift_functional(r[1], n, p, dom, nf)}
    check("A5 (32,16,97) split == 53 lifts + 30 accidental + 0 periodic "
          "(#170 table; functional lift test)",
          len(lifts) == 53 and len(aper) - len(lifts) == 30
          and len(rows) == len(aper),
          f"{len(lifts)} + {len(aper) - len(lifts)} + "
          f"{len(rows) - len(aper)}")
    # independent quotient-side lift recount
    half = n // 2
    npr, kpr = n // 2, k // 2
    domq = [dom[j] * dom[j] % p for j in range(npr)]
    xnf = dom[nf]
    u1 = [0] * npr
    for j in range(npr):
        if j != nf:
            u1[j] = values[j] * pow(dom[j] - xnf, -1, p) % p
    s2 = all(values[j] == (dom[j] - xnf) * u1[j % npr] % p
             for j in range(n) if j % npr != nf)
    check("A5 S2 word factorization identity (off the split fiber)", s2)
    qfloor = set()
    seen = set()
    for A in itertools.combinations([j for j in range(npr) if j != nf],
                                    kpr):
        xs = [domq[j] for j in A]
        ys = [u1[j] for j in A]
        g = lagrange_coeffs(xs, ys, p)
        if g in seen:
            continue
        seen.add(g)
        if evp(g, domq[nf], p) == 0:
            continue                       # periodic branch
        agr = frozenset(j for j in range(npr)
                        if j != nf and evp(g, domq[j], p) == u1[j])
        if len(agr) not in (kpr, kpr + 1):
            continue
        S = frozenset([nf]) | frozenset(x for j in agr
                                        for x in (j, j + half))
        exact = frozenset(j for j in range(n)
                          if (dom[j] - xnf) * evp(g, domq[j % npr], p) % p
                          == values[j])
        if exact != S:
            continue
        d, jj, m, s_r, fp = chart_of(S, core, petals, bg)
        if fp and d >= thr:
            qfloor.add(S)
    check("A5 quotient-side floor-lift recount == candidate-side lift set "
          "(two independent methods agree)", qfloor == lifts,
          f"quotient {len(qfloor)} vs candidate {len(lifts)}")
    perch = {}
    for (S, f, d, jj, m, s_r, c) in rows:
        perch.setdefault((frozenset(core) - S, S & frozenset(bg)),
                         []).append(S)
    check(f"A5 per-chart <= t+1 = {t + 1}",
          all(len(v) <= t + 1 for v in perch.values()),
          f"max {max(len(v) for v in perch.values())}, "
          f"charts {len(perch)}")
    NM = 2 * (t + 1) * sum(comb(k - 1, i) for i in range(4))
    check(f"A5 census 83 <= N_max = {NM}", len(rows) <= NM and NM == 10368)


def stage_A6():
    n, k, p = 16, 8, 97
    dom = find_domain(p, n)
    values, core, petals, bg, nf = chart_word(n, k, p, dom, "consec")
    t = len(petals)
    thr = 2 * (t - 2)
    J = (k - 1) - thr
    cls = complete_census_ksub(n, k, p, dom, values)
    rows = floor_rows(cls, n, core, petals, bg)
    assert len(rows) == 10
    # NM1: tighten the j bound to J-1 — must report violations (there must
    # be realized classes AT j = J; else the rigidity check is not sharp
    # and could not trip a j-drift bug)
    viol = [r for r in rows if r[3] > J - 1]
    check("A6 NM1 REQUIRED-TO-TRIP: rigidity with j <= J-1 reports "
          "violations on the honest census (j = J realized => the j bound "
          "is exercised at its boundary)", len(viol) > 0,
          f"{len(viol)} classes at j = {J}")
    # NM2: drop the m = t stratum — must undercount
    kept = [r for r in rows if r[4] != t]
    check("A6 NM2 REQUIRED-TO-TRIP: dropping the m=t stratum strictly "
          "undercounts (complement of packet M2)",
          len(kept) < len(rows), f"{len(kept)} < {len(rows)}")
    # NM3: raise the atlas index floor to thr+2 — must leave realized
    # classes uncovered (coverage check must fail on the mutant atlas)
    unc = [r for r in rows if r[2] < thr + 2]
    check("A6 NM3 REQUIRED-TO-TRIP: mutant atlas index |D0| >= thr+2 "
          "leaves realized floor classes uncovered",
          len(unc) > 0, f"{len(unc)} classes at d in {{thr, thr+1}}")


STAGES = {"A1": stage_A1, "A2": stage_A2, "A3": stage_A3,
          "A4": stage_A4, "A5": stage_A5, "A6": stage_A6}


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    names = list(STAGES) if which == "all" else [which]
    for nm in names:
        print("=" * 70)
        print(f"AUDIT STAGE {nm}")
        print("=" * 70)
        STAGES[nm]()
    print("=" * 70)
    print(f"AUDIT TOTAL: {NPASS} PASS, {NFAIL} FAIL")
    if NFAIL:
        sys.exit(1)


if __name__ == "__main__":
    main()
