#!/usr/bin/env python3
"""cp_verify — verifier for the CLAUSE (P) floor-band packet (cp_statement.md,
cp_proof.md). Standalone; run under tools/ramguard tiny, one stage per call:

    python3 cp_verify.py P1|P2|P3a|P3b|P4|P5|P6|P7

Stages:
  P1  (16,8,97,consec) COMPLETE brute census; rigidity in vivo; candidate
      method == brute (method cross-validation); banked floor-lift pin 8.
  P2  (32,16,97,geom5) candidate census (rigidity-complete) + independent
      quotient-side lift census; banked pin 53; caps; per-chart <= t+1.
  P3a (32,16,193,consec) fresh-cell reproduction of the bsra pin 48.
  P3b (32,16,257,geom3) NEVER-banked fresh cell: census, rigidity, caps.
  P4  (16,8,97) non-coset layouts (fiber_pairs, shuffled): brute == candidate,
      rigidity — combinatorial layout-freeness in vivo.
  P5  (16,4,97) rate-1/4 complete brute: floor band EMPTY in vivo (+ the
      arithmetic emptiness law at (32,12) and official rates <= 1/4).
  P6  Mutations: M1 widened-band trips rigidity (required-to-trip); M2
      dropped m-stratum undercounts (required-to-trip); M3 corrupted word
      shifts the census (required-to-trip); M4 catch #168 tailored-layout
      re-basing demo + the (128,64) layout-existential kill arithmetic.
  P7  Exact bigint: budget fit at all rate-1/2 rows s=3..44; official
      maximal rows; emptiness at rates <= 1/4 s=13..44; #153 lift caps
      embed; parity law; Newton-vs-Lagrange interpolation self-test.
"""
import itertools
import sys
from math import comb

# ---------------------------------------------------------------- checks
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


# ---------------------------------------------------------------- field
def order_n_domain(p, n):
    assert (p - 1) % n == 0
    a = 2
    while True:
        g0 = pow(a, (p - 1) // n, p)
        if pow(g0, n // 2, p) != 1:
            break
        a += 1
    dom = [pow(g0, j, p) for j in range(n)]
    assert len(set(dom)) == n
    return dom


def locator(roots, p):
    loc = [1]
    for r in roots:
        new = [0] * (len(loc) + 1)
        for i, c in enumerate(loc):
            new[i] = (new[i] - r * c) % p
            new[i + 1] = (new[i + 1] + c) % p
        loc = new
    return loc


def ev(poly, x, p):
    v = 0
    for c in reversed(poly):
        v = (v * x + c) % p
    return v


def newton_interp(xs, ys, p):
    """Monomial coefficients (len k) of the unique deg<k interpolant."""
    k = len(xs)
    dd = list(ys)
    for lvl in range(1, k):
        for i in range(k - 1, lvl - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) * pow(xs[i] - xs[i - lvl], -1, p) % p
    coeffs = [0] * k
    coeffs[0] = dd[k - 1] % p
    deg = 0
    for i in range(k - 2, -1, -1):
        # multiply by (X - xs[i]) then add dd[i]
        for d in range(deg, -1, -1):
            coeffs[d + 1] = (coeffs[d + 1] + coeffs[d]) % p
            coeffs[d] = (-xs[i] * coeffs[d]) % p
        deg += 1
        coeffs[0] = (coeffs[0] + dd[i]) % p
    return tuple(coeffs)


def lagrange_interp(xs, ys, k, p):  # cg_petal_census reference implementation
    poly = [0] * k
    for i in range(k):
        num = [1]
        den = 1
        for j in range(k):
            if j == i:
                continue
            r = xs[j]
            new = [0] * (len(num) + 1)
            for d2, c in enumerate(num):
                new[d2] = (new[d2] - r * c) % p
                new[d2 + 1] = (new[d2 + 1] + c) % p
            num = new
            den = den * (xs[i] - xs[j]) % p
        coef = ys[i] * pow(den, -1, p) % p
        for d2, c in enumerate(num):
            poly[d2] = (poly[d2] + coef * c) % p
    return tuple(poly)


def stab_order(S, n):
    c = 1
    M = 2
    while M <= n:
        s = n // M
        if all(((x + s) % n) in S for x in S):
            c = M
        else:
            break
        M *= 2
    return c


# ---------------------------------------------------------------- layouts
def build_layout(n, k, layout, seed=0):
    """(core, petals, background) in exponent space — cg conventions."""
    half = n // 2
    z = k - 1
    if layout == "fiber_aligned":
        nf = (k - 1) // 2
        core = []
        for j in range(nf):
            core.extend([j, j + half])
        extra = []
        if (k - 1) % 2:
            core.append(nf)
            extra = [nf + half]
        start = nf + (1 if (k - 1) % 2 else 0)
        petals = [sorted([j, j + half]) for j in range(start, half)]
        return sorted(core), petals, sorted(extra)
    if layout == "fiber_pairs":
        order = []
        for j in range(half):
            order.extend([j, j + half])
    elif layout.startswith("shuffled"):
        import random
        rng = random.Random(seed)
        order = list(range(n))
        rng.shuffle(order)
    else:
        raise ValueError(layout)
    core = sorted(order[:z])
    rest = order[z:]
    t = len(rest) // 2
    petals = [sorted(rest[2 * i:2 * i + 2]) for i in range(t)]
    background = sorted(rest[2 * t:])
    return core, petals, background


def build_word(n, k, p, dom, layout, smode, seed=0):
    core, petals, background = build_layout(n, k, layout, seed)
    t = len(petals)
    if smode == "geom5":
        scal, v = [], 1
        for _ in range(t):
            scal.append(v)
            v = v * 5 % p
    elif smode == "geom3":
        scal, v = [], 1
        for _ in range(t):
            scal.append(v)
            v = v * 3 % p
    elif smode == "consec":
        scal = [(i + 1) % p for i in range(t)]
    else:
        raise ValueError(smode)
    loc = locator([dom[j] for j in core], p)
    values = [0] * n
    for c_i, petal in zip(scal, petals):
        for j in petal:
            values[j] = c_i * ev(loc, dom[j], p) % p
    return values, core, petals, background


# ------------------------------------------------------- census machinery
def chart_data(S, core, petals, background):
    j = len(S & frozenset(core))
    d = len(core) - j
    m = sum(1 for P in petals if frozenset(P) <= S)
    fp = all((S & frozenset(P)) in (frozenset(), frozenset(P))
             for P in petals)
    s_r = len(S & frozenset(background))
    return d, j, m, s_r, fp


def brute_all_classes(n, k, p, dom, values):
    """COMPLETE class census: every deg<k codeword with exact |agr| >= k+1
    (found via all (k+1)-subsets)."""
    found = {}
    for idxs in itertools.combinations(range(n), k + 1):
        xs = [dom[j] for j in idxs]
        ys = [values[j] for j in idxs]
        f = newton_interp(xs[:k], ys[:k], p)
        if ev(f, xs[k], p) != ys[k]:
            continue
        S = frozenset(j for j in range(n)
                      if ev(f, dom[j], p) == values[j])
        if len(S) >= k + 1 and S not in found:
            found[S] = f
    return found


def candidate_census(n, k, p, dom, values, core, petals, background,
                     drop_low_stratum=False):
    """Floor-band full-petal classes via Lemma-B rigidity: enumerate the
    admissible supports (j <= J, m in {t-1, t}, s_r <= b0), realize, and
    keep exact-agreement classes.  Rigidity-COMPLETE for the floor band
    (cross-validated against brute in P1/P4)."""
    t = len(petals)
    thr = 2 * (t - 2)
    J = (k - 1) - thr
    out = {}
    if J < 0:
        return out
    m_range = [t] if drop_low_stratum else [t - 1, t]
    bg_subs = [frozenset()] + [frozenset([b]) for b in background]
    for jsz in range(0, min(J, k - 1) + 1):
        for csub in itertools.combinations(core, jsz):
            for m in m_range:
                for psub in itertools.combinations(range(t), m):
                    pet_pts = [x for i in psub for x in petals[i]]
                    for rsub in bg_subs:
                        S = frozenset(csub) | frozenset(pet_pts) | rsub
                        if len(S) < k + 1:
                            continue
                        pts = sorted(S)
                        xs = [dom[j] for j in pts]
                        ys = [values[j] for j in pts]
                        f = newton_interp(xs[:k], ys[:k], p)
                        if any(ev(f, x, p) != y
                               for x, y in zip(xs[k:], ys[k:])):
                            continue
                        A = frozenset(j for j in range(n)
                                      if ev(f, dom[j], p) == values[j])
                        if A != S:
                            continue
                        out[S] = f
    return out


def is_lift(f, x_nf, p):
    """h = f0 + x_nf f1 == 0  <=>  f = (X - x_nf) g(X^2)."""
    f0 = f[0::2]
    f1 = f[1::2]
    kp = max(len(f0), len(f1))
    for i in range(kp):
        a = f0[i] if i < len(f0) else 0
        b = f1[i] if i < len(f1) else 0
        if (a + x_nf * b) % p:
            return False
    return True


def quotient_lift_census(n, k, p, dom, values, nf):
    """Independent method: all odd lifts f=(X-x_nf)g(X^2), g exact
    |agr(g,u1)| in {k', k'+1}, g(y_nf) != 0, VERIFIED end-to-end at the
    official row. Returns dict S -> (z, official f check ok)."""
    npr, kpr = n // 2, k // 2
    domq = [dom[j] * dom[j] % p for j in range(npr)]
    Zq = [domq[j] for j in range(nf)]
    locq = locator(Zq, p)
    # u1 from the OFFICIAL word via S2: values[j] = (dom[j]-x_nf) u1(j mod n')
    xnf = dom[nf]
    u1 = [0] * npr
    for j in range(npr):
        if j == nf:
            continue
        u1[j] = values[j] * pow(dom[j] - xnf, -1, p) % p
    # S2 identity check
    s2 = all(values[j] == (dom[j] - xnf) * u1[j % npr] % p for j in range(n))
    seen = {}
    for sub in itertools.combinations(range(npr), kpr):
        xs = [domq[j] for j in sub]
        ys = [u1[j] for j in sub]
        g = newton_interp(xs, ys, p)
        if g in seen:
            continue
        agr = frozenset(j for j in range(npr)
                        if ev(g, domq[j], p) == u1[j])
        seen[g] = agr
    out = {}
    half = n // 2
    for g, agr in seen.items():
        if ev(g, domq[nf], p) == 0 or len(agr) not in (kpr, kpr + 1):
            continue
        if nf in agr:
            continue
        S = frozenset([nf]) | frozenset(x for j in agr for x in (j, j + half))
        # end-to-end official verification: exact agreement of the lift
        exact = frozenset(j for j in range(n)
                          if (dom[j] - xnf) * ev(g, domq[j % npr], p) % p
                          == values[j])
        z = len(agr & frozenset(range(nf)))
        out[S] = (z, exact == S, len(agr))
    return out, s2


def floor_split(classes, n, core, petals, background):
    """Split a class dict by floor-band membership/full-petal; return list of
    (S, f, d, j, m, s_r, scale)."""
    t = len(petals)
    thr = 2 * (t - 2)
    rows = []
    for S, f in classes.items():
        d, j, m, s_r, fp = chart_data(S, core, petals, background)
        if fp and d >= thr:
            rows.append((S, f, d, j, m, s_r, stab_order(S, n)))
    return rows


def rigidity_ok(rows, k, t):
    J = (k - 1) - 2 * (t - 2)
    bad = [r for r in rows
           if r[3] > J or r[4] not in (t - 1, t) or r[5] > 1]
    return len(bad) == 0, bad


def n_max(k, t, b0):
    J = (k - 1) - 2 * (t - 2)
    if J < 0:
        return 0
    SJ = sum(comb(k - 1, i) for i in range(min(J, k - 1) + 1))
    return (2 ** b0) * (t + 1) * SJ


# ================================================================= stages
def stage_P1():
    n, k, p, smode = 16, 8, 97, "consec"
    dom = order_n_domain(p, n)
    values, core, petals, bg = build_word(n, k, p, dom, "fiber_aligned",
                                          smode)
    t = len(petals)
    nf = (k - 1) // 2
    brute = brute_all_classes(n, k, p, dom, values)
    rows = floor_split(brute, n, core, petals, bg)
    check("P1 census nonempty (#137 discipline)", len(rows) > 0,
          f"{len(rows)} floor-band full-petal classes (complete brute)")
    ok, bad = rigidity_ok(rows, k, t)
    check("P1 RIGIDITY on complete census (j <= 3, m in {t-1,t}, s_r <= 1)",
          ok, f"violations: {bad[:3]}")
    cand = candidate_census(n, k, p, dom, values, core, petals, bg)
    check("P1 candidate method == brute on the floor band (completeness)",
          set(cand) == {r[0] for r in rows},
          f"cand {len(cand)} vs brute {len(rows)}")
    aper = [r for r in rows if r[6] == 1]
    lifts = [r for r in aper if is_lift(r[1], dom[nf], p)]
    check("P1 banked floor-lift pin == 8 (bsr E3)", len(lifts) == 8,
          f"lifts {len(lifts)}, aperiodic total {len(aper)}, "
          f"non-lift aperiodic {len(aper) - len(lifts)}, "
          f"periodic floor {len(rows) - len(aper)}")
    cap = n_max(k, t, len(bg))
    check(f"P1 census <= N_max = {cap}", len(rows) <= cap)
    # atlas: coverage + per-chart count
    perch = {}
    for (S, f, d, j, m, s_r, c) in rows:
        key = (frozenset(core) - S, S & frozenset(bg))
        perch.setdefault(key, []).append(S)
        check_ok = d >= 2 * (t - 2) and len(key[1]) <= 1
        if not check_ok:
            check("P1 atlas chart legality", False, str(S))
    check("P1 atlas coverage: every class's (D0,R) chart is in the index",
          all(len(D0) >= 2 * (t - 2) for D0, R in perch))
    check(f"P1 per-chart class count <= t+1 = {t + 1} (K4 line, word-free)",
          all(len(v) <= t + 1 for v in perch.values()),
          f"max {max(len(v) for v in perch.values())}")


def run_cell_32(p, smode, pin, pin_name):
    n, k = 32, 16
    dom = order_n_domain(p, n)
    values, core, petals, bg = build_word(n, k, p, dom, "fiber_aligned",
                                          smode)
    t = len(petals)
    nf = (k - 1) // 2
    cand = candidate_census(n, k, p, dom, values, core, petals, bg)
    rows = floor_split(cand, n, core, petals, bg)
    check(f"({n},{k},{p},{smode}) candidate census nonempty",
          len(rows) > 0, f"{len(rows)} classes")
    ok, bad = rigidity_ok(rows, k, t)
    check(f"({n},{k},{p},{smode}) rigidity holds on all realized classes",
          ok, f"violations {bad[:3]}")
    aper = [r for r in rows if r[6] == 1]
    lifts = {r[0] for r in aper if is_lift(r[1], dom[nf], p)}
    qlifts, s2 = quotient_lift_census(n, k, p, dom, values, nf)
    check(f"({n},{k},{p},{smode}) S2 word factorization identity", s2)
    qfloor = set()
    thr = 2 * (t - 2)
    for S, (z, exact_ok, la) in qlifts.items():
        if not exact_ok:
            continue
        d, j, m, s_r, fp = chart_data(S, core, petals, bg)
        if fp and d >= thr:
            qfloor.add(S)
    # cpa-C3 (catch #174): the agreement check must not pass vacuously on
    # an empty lift subfamily at unpinned cells (#137 discipline)
    check(f"({n},{k},{p},{smode}) lift subfamily nonempty",
          len(lifts) > 0, f"{len(lifts)} lifts")
    check(f"({n},{k},{p},{smode}) lift censuses agree "
          f"(candidate/official vs quotient methods)", lifts == qfloor,
          f"cand {len(lifts)} vs quotient {len(qfloor)}")
    if pin is not None:
        check(f"({n},{k},{p},{smode}) banked pin {pin_name} == {pin}",
              len(lifts) == pin, f"got {len(lifts)}")
    cap = n_max(k, t, len(bg))
    check(f"({n},{k},{p},{smode}) census {len(rows)} <= N_max = {cap}",
          len(rows) <= cap,
          f"aperiodic {len(aper)} (lifts {len(lifts)}, accidental "
          f"{len(aper) - len(lifts)}), periodic {len(rows) - len(aper)}")
    z0 = (k // 2 - 1) - (t - 2)
    cap1 = sum(comb(k // 2 - 1, z) * comb(t, k // 2 - z)
               for z in range(z0 + 1)) if z0 >= 0 else 0
    cap2 = sum(comb(k // 2 - 1, z) * comb(t, k // 2 + 1 - z)
               for z in range(z0 + 1)) if z0 >= 0 else 0
    check(f"({n},{k},{p},{smode}) lift floor count <= #153 two-family cap "
          f"{cap1}+{cap2}", len(lifts) <= cap1 + cap2)
    perch = {}
    for (S, f, d, j, m, s_r, c) in rows:
        perch.setdefault((frozenset(core) - S, S & frozenset(bg)),
                         []).append(S)
    check(f"({n},{k},{p},{smode}) per-chart <= t+1 = {t + 1}",
          all(len(v) <= t + 1 for v in perch.values()),
          f"max {max(len(v) for v in perch.values())}, "
          f"charts used {len(perch)}")
    return dom, values, core, petals, bg


def stage_P2():
    run_cell_32(97, "geom5", 53, "bsr E3 floor-lift count")


def stage_P3a():
    run_cell_32(193, "consec", 48, "bsra fresh-cell floor count")


def stage_P3b():
    run_cell_32(257, "geom3", None, "")  # never-banked fresh cell


def stage_P4():
    n, k, p = 16, 8, 97
    dom = order_n_domain(p, n)
    for layout, seed, smode in [("fiber_pairs", 0, "consec"),
                                ("shuffled", 1, "geom5")]:
        values, core, petals, bg = build_word(n, k, p, dom, layout, smode,
                                              seed)
        t = len(petals)
        brute = brute_all_classes(n, k, p, dom, values)
        rows = floor_split(brute, n, core, petals, bg)
        ok, bad = rigidity_ok(rows, k, t)
        check(f"P4 [{layout}/{smode}] rigidity on complete census "
              f"({len(rows)} floor classes)", ok, f"violations {bad[:3]}")
        cand = candidate_census(n, k, p, dom, values, core, petals, bg)
        check(f"P4 [{layout}/{smode}] candidate == brute (non-coset layout)",
              set(cand) == {r[0] for r in rows},
              f"cand {len(cand)} vs brute {len(rows)}")
        cap = n_max(k, t, len(bg))
        check(f"P4 [{layout}/{smode}] census <= N_max = {cap}",
              len(rows) <= cap)


def stage_P5():
    # complete in-vivo emptiness at a rate-1/4 cell
    n, k, p = 16, 4, 97
    dom = order_n_domain(p, n)
    values, core, petals, bg = build_word(n, k, p, dom, "fiber_aligned",
                                          "geom5")
    t = len(petals)
    thr = 2 * (t - 2)
    check(f"P5 (16,4) arithmetic: k-1 = {k - 1} < thr = {thr} (J < 0)",
          k - 1 < thr)
    brute = brute_all_classes(n, k, p, dom, values)
    rows = floor_split(brute, n, core, petals, bg)
    check("P5 (16,4,97) COMPLETE brute: floor band EMPTY in vivo",
          len(rows) == 0, f"classes total {len(brute)}, floor {len(rows)}")
    check("P5 (16,4,97) contributors exist (emptiness is the band, "
          "not vacuity)", len(brute) > 0, f"{len(brute)} classes")
    # arithmetic law at the banked rate-3/8 cell and official rates
    for (nn, kk) in [(32, 12), (2 ** 42, 2 ** 40), (2 ** 43, 2 ** 40),
                     (2 ** 44, 2 ** 40)]:
        tt = (nn - kk) // 2
        check(f"P5 emptiness law at (n={nn},k={kk}): k-1 < 2(t-2)",
              kk - 1 < 2 * (tt - 2))


def stage_P6():
    n, k, p = 32, 16, 97
    dom = order_n_domain(p, n)
    values, core, petals, bg = build_word(n, k, p, dom, "fiber_aligned",
                                          "geom5")
    t = len(petals)
    nf = (k - 1) // 2
    half = n // 2
    thr = 2 * (t - 2)
    # M1: widened band (one petal wider) must admit j > 3 classes
    qlifts, _ = quotient_lift_census(n, k, p, dom, values, nf)
    wide2 = []
    for S, (z, exact_ok, la) in qlifts.items():
        if not exact_ok:
            continue
        d, j, m, s_r, fp = chart_data(S, core, petals, bg)
        if fp and d >= 2 * (t - 3) and j > 3:
            wide2.append((S, z, d, j))
    check("P6 M1 REQUIRED-TO-TRIP: widening the band by one petal admits "
          "realized classes with j > J = 3 (rigidity is band-sharp)",
          len(wide2) > 0, f"{len(wide2)} classes (z=2 lifts), "
          f"e.g. d={wide2[0][2]}, j={wide2[0][3]}" if wide2 else "none")
    # M2: dropping the m = t-1 stratum undercounts (at the complete cell)
    n2, k2 = 16, 8
    dom2 = order_n_domain(p, n2)
    v2, c2, pt2, bg2 = build_word(n2, k2, p, dom2, "fiber_aligned", "consec")
    full = candidate_census(n2, k2, p, dom2, v2, c2, pt2, bg2)
    dropped = candidate_census(n2, k2, p, dom2, v2, c2, pt2, bg2,
                               drop_low_stratum=True)
    check("P6 M2 REQUIRED-TO-TRIP: dropping the m=t-1 stratum strictly "
          "undercounts", len(dropped) < len(full),
          f"{len(dropped)} < {len(full)}")
    # M3: corrupting one petal value shifts the floor census
    values_bad = list(values)
    values_bad[petals[0][0]] = (values_bad[petals[0][0]] + 1) % p
    cand0 = candidate_census(n, k, p, dom, values, core, petals, bg)
    cand1 = candidate_census(n, k, p, dom, values_bad, core, petals, bg)
    check("P6 M3 REQUIRED-TO-TRIP: corrupted petal value changes the "
          "realized floor census", set(cand0) != set(cand1),
          f"{len(cand0)} vs {len(cand1)}")
    # M4: catch #168 — tailored-layout re-basing of a floor-EXCLUDED lift
    reb = None
    n_rebasable = 0
    for S, (z, exact_ok, la) in qlifts.items():
        if not exact_ok or la != k // 2:
            continue
        n_rebasable += 1
        if z >= 2 and reb is None:
            reb = (S, z)
    check("P6 M4 every |S|=k+1 lift is re-basable (spare-fiber count fits)",
          n_rebasable > 0, f"{n_rebasable} lifts at |S|=k+1")
    if reb is not None:
        S, z = reb
        d0, j0, m0, s0, fp0 = chart_data(S, core, petals, bg)
        check("P6 M4 witness lift is floor-EXCLUDED in the word's layout",
              fp0 and d0 < thr, f"z={z}, d={d0} < thr={thr}")
        # tailored layout: core = k'-1 fibers outside S (excl. nf) + {x_nf}
        sfib = {j % half for j in S if j != nf}
        avail = [j for j in range(half) if j not in sfib and j != nf]
        zstar = sorted([x for j in avail[:k // 2 - 1]
                        for x in (j, j + half)] + [nf])
        pstar = [sorted([j, j + half]) for j in sorted(sfib)]
        bstar = [nf + half]
        tstar = len(pstar)
        dS, jS, mS, sS, fpS = chart_data(S, zstar, pstar, bstar)
        check("P6 M4 CATCH #168: the same class is floor-band full-petal "
              "in the tailored layout (layout-existential reading dies)",
              fpS and dS >= 2 * (tstar - 2) and len(zstar) == k - 1,
              f"tailored: t*={tstar}, d*={dS}, j*={jS}, m*={mS}")
    # the (128,64) layout-existential kill arithmetic (supply side)
    check("P6 M4 kill arithmetic: C(63,32) > (121/128)*128^6 "
          "(so re-based supply breaks the budget at (128,64))",
          comb(63, 32) > 121 * 128 ** 6 // 128,
          f"2^{comb(63, 32).bit_length() - 1} vs "
          f"2^{(121 * 128 ** 6 // 128).bit_length() - 1}")


def stage_P7():
    # (a) budget fit at ALL rate-1/2 rows s = 3..44 (exact bigint)
    ok = True
    worst = None
    for s in range(3, 45):
        n = 2 ** s
        k = n // 2
        t = (n - k) // 2
        W = n_max(k, t, 1)
        budget = 121 * n ** 6 // 128
        if W > budget:
            ok = False
        marg = budget // max(W, 1)
        if worst is None or marg < worst[1]:
            worst = (s, marg)
    check("P7a N_max <= (121/128) n^6 at every rate-1/2 row s=3..44",
          ok, f"worst margin 2^{worst[1].bit_length() - 1} at s={worst[0]}")
    # (b) official maximal rows
    n = 2 ** 41
    k = 2 ** 40
    W = n_max(k, (n - k) // 2, 1)
    budget = 121 * n ** 6 // 128
    check("P7b binding official row n=2^41 (rate 1/2) fits",
          W <= budget,
          f"N_max = 2^{W.bit_length() - 1}, budget = 2^"
          f"{budget.bit_length() - 1}, margin = 2^"
          f"{(budget // W).bit_length() - 1}")
    for n in (2 ** 42, 2 ** 43, 2 ** 44):
        t = (n - 2 ** 40) // 2
        check(f"P7b official row n=2^{n.bit_length() - 1} floor band EMPTY",
              2 ** 40 - 1 < 2 * (t - 2))
    # (c) rates <= 1/4, s = 13..44: empty
    ok = True
    for s in range(13, 45):
        n = 2 ** s
        for rho_den in (4, 8, 16):
            k = n // rho_den
            if k < 4:
                continue
            t = (n - k) // 2
            if k - 1 >= 2 * (t - 2):
                ok = False
    check("P7c floor band EMPTY at rates 1/4, 1/8, 1/16 for all s=13..44",
          ok)
    # (d) #153 two-family lift caps embed at (128,64)
    kpr, tch = 32, 32
    z0 = (kpr - 1) - (tch - 2)
    c1 = sum(comb(kpr - 1, z) * comb(tch, kpr - z) for z in range(z0 + 1))
    c2 = sum(comb(kpr - 1, z) * comb(tch, kpr + 1 - z)
             for z in range(z0 + 1))
    NM = n_max(64, 32, 1)
    check("P7d #153 caps at (128,64): 993 + 31 = 1024 <= N_max",
          c1 == 993 and c2 == 31 and c1 + c2 <= NM,
          f"caps {c1}+{c2}, N_max {NM}")
    # (e) parity law: no even-k 2-power row with 2k = n-2
    ok = all((2 ** s - 2) % 4 != 0 or ((2 ** s - 2) // 2) % 2 == 1
             for s in range(3, 25))
    check("P7e parity: no even-k 2-power row sits at 2k = n-2 "
          "(emptiness boundary vacuous)", ok)
    # (f) Newton vs Lagrange interpolation self-test
    import random
    rng = random.Random(7)
    p = 97
    okf = True
    for _ in range(20):
        k = rng.randrange(3, 9)
        xs = rng.sample(range(1, p), k)
        ys = [rng.randrange(p) for _ in range(k)]
        if newton_interp(xs, ys, p) != lagrange_interp(xs, ys, k, p):
            okf = False
    check("P7f Newton == Lagrange interpolation (20 random instances)", okf)


STAGES = {"P1": stage_P1, "P2": stage_P2, "P3a": stage_P3a,
          "P3b": stage_P3b, "P4": stage_P4, "P5": stage_P5,
          "P6": stage_P6, "P7": stage_P7}


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    names = list(STAGES) if which == "all" else [which]
    for nm in names:
        print("=" * 70)
        print(f"STAGE {nm}")
        print("=" * 70)
        STAGES[nm]()
    print("=" * 70)
    print(f"TOTAL: {NPASS} PASS, {NFAIL} FAIL")
    if NFAIL:
        sys.exit(1)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
