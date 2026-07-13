#!/usr/bin/env python3
"""bsr_check — verifier for the BRANCH-SPLIT RE-POSE packet (bsr_*).

P1  Lemma COL (the gate's column form as a support-count theorem) replayed on
    all 372 banked census cells, every band tag, every profile cell.
P2  The g1a falsification instances FIT the column form (and violate the old
    n^6 form — the falsification is reproduced, exact bigint).
P3  The odd-lift aperiodic population (catch #145): fresh complete
    enumerations; wide-vs-floor band arithmetic; official lift semantics
    end-to-end; brute official cross-check at (16,8).
P4  Clause (ii) DD-atlas census vs the column at the enumerated cells; banked
    member pins 3/63/47 reproduced; #137 nonemptiness.
P5  Consumer arithmetic: 719 allowance at the four official maximal rows;
    first-scale dominance of the M<=t profile extension; clause-(ii) trivial
    ratios and the gate COL cap over the official grid; K4 package ledger.
P6  Mutation controls MC1-MC4 (all must TRIP).

Run: tools/ramguard tiny -- python3 <scratchpad>/bsr_check.py
"""
from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from math import comb, lgamma, log2

PRIZE = "/home/u2470931/smooth-read-solomin/prize"
JSON_PATH = PRIZE + "/critical/nodes/petal_growth/notes/cg_petal_census_results.json"
LN2 = 0.6931471805599453

FAILS = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)


def lg_frac(fr):
    """log2 of a positive Fraction, huge-safe."""
    return fr.numerator.bit_length() - fr.denominator.bit_length()


# ---------------------------------------------------------------- field utils
def is_prime(m):
    if m < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if m % p == 0:
            return m == p
    d, s = m - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(s - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def order_n_domain(p, n):
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


def interpolate(xs, ys, k, p):
    poly = [0] * k
    for i in range(k):
        num = [1]
        den = 1
        xi = xs[i]
        for j in range(k):
            if j == i:
                continue
            r = xs[j]
            new = [0] * (len(num) + 1)
            for d2, c in enumerate(num):
                new[d2] = (new[d2] - r * c) % p
                new[d2 + 1] = (new[d2 + 1] + c) % p
            num = new
            den = den * (xi - r) % p
        coef = ys[i] * pow(den, -1, p) % p
        for d2, c in enumerate(num):
            poly[d2] = (poly[d2] + coef * c) % p
    return tuple(poly)


def stab_order(S, n):
    c, M = 1, 2
    while M <= n:
        s = n // M
        if all(((x + s) % n) in S for x in S):
            c = M
        else:
            break
        M *= 2
    return c


def own_A(k, M):
    """P1-OWN profile size at scale M: smallest multiple of M that is >= k+1."""
    return M * (-(-(k + 1) // M))


# =========================================================================
# P1 — Lemma COL replay on the 372 banked cells
# =========================================================================
print("=" * 72)
print("P1: Lemma COL on the banked 372-cell census (all tags, all profiles)")
print("=" * 72)
records = json.load(open(JSON_PATH))
check("banked record count == 372", len(records) == 372, f"got {len(records)}")

TAGS = ["fp0_edge", "fp0_own", "fp0_all", "fp1_edge", "fp1_own", "fp1_all"]
ncells = 0
max_ratio_Q = Fraction(0)
max_ratio_sup = Fraction(0)
col_viol = viol719 = ident_viol = mult_viol = q0 = 0
mc1_trips = mc2_trips = 0
for r in records:
    n = r["n"]
    for tag in TAGS:
        for cellkey, v in r[tag].items():
            M, A = (int(x) for x in cellkey.split(","))
            h = A // M
            npr = n // M
            cls = v["classes"]
            ncells += 1
            Q = comb(npr - 1, h) if h <= npr - 1 else 0
            if Q != v["Q"]:
                ident_viol += 1
            sup = comb(npr, h)
            if cls > sup:
                col_viol += 1
            if A < n and Fraction(sup) != Fraction(Q) * Fraction(n, n - A):
                ident_viol += 1
            if cls > 719 * Q:
                viol719 += 1
            if Q == 0:
                q0 += 1
            else:
                max_ratio_Q = max(max_ratio_Q, Fraction(cls, Q))
                max_ratio_sup = max(max_ratio_sup, Fraction(cls, sup))
            if v["codewords"] != cls:
                mult_viol += 1
            if cls > Q:                       # MC1: C_col = 1
                mc1_trips += 1
            Qm = comb(npr - 1, h + 2) if h + 2 <= npr - 1 else 0
            if cls > 719 * Qm:                # MC2: shifted column
                mc2_trips += 1

check("P1 profile cells swept >= 500", ncells >= 500, f"{ncells} cells")
check("P1 COL support cap classes <= C(n/M, A/M) at EVERY cell", col_viol == 0)
check("P1 rational identity C(n/M,h) == Q * n/(n-A) at every cell", ident_viol == 0)
check("P1 banked 719 line: zero excesses (replay)", viol719 == 0)
check("P1 multiplicity 1 everywhere (codewords == classes)", mult_viol == 0)
check("P1 no degenerate Q=0 cell realized", q0 == 0)
check("P1 max classes/Q == 4/3 (banked tightest cell)",
      max_ratio_Q == Fraction(4, 3), f"max = {max_ratio_Q}")
print(f"     max classes / C(n/M,A/M) (support saturation) = {max_ratio_sup}"
      f" ~ {float(max_ratio_sup):.3f}")

# =========================================================================
# P2 — g1a instances vs the column form
# =========================================================================
print("=" * 72)
print("P2: g1a instances — old n^6 form violated, column form fits")
print("=" * 72)


def smallest_prime_1mod(m, lo):
    q = lo + (m - (lo - 1) % m) % m
    while not is_prime(q):
        q += m
    return q


q_s13 = smallest_prime_1mod(8192, 2 * 4096 * 4096)
print(f"     s=13 instance field: q = {q_s13} (~2^{log2(q_s13):.1f}, = 1 mod 8192)")

INSTANCES = [
    ("official (256,128,65537)  ", 128, 64, 65537),
    ("s=13 primary (8192,4096)  ", 4096, 2048, q_s13),
    ("prize 2^128 (512,256)     ", 256, 128, 2**128),
    ("prize 2^256 (1024,512)    ", 512, 256, 2**256),
]
for name, npr, kpr, q in INSTANCES:
    n = 2 * npr
    Bfloor = comb(npr - 1, kpr) // (4 * q * (kpr + 1))
    old_budget = Fraction(121, 128) * n**6
    old_violated = 3 * Bfloor > old_budget
    Q1 = comb(npr - 1, kpr + 1)   # Q_2(k+2), parent-row profile column
    Q2c = comb(npr - 1, kpr + 2)  # Q_2(k+4)
    fits = Bfloor <= 719 * Q1
    cap1 = comb(npr - 1, kpr) <= 719 * Q1
    cap2 = comb(npr - 1, kpr + 1) <= 719 * Q2c
    margin = lg_frac(Fraction(719 * Q1, Bfloor)) if Bfloor else 10**9
    check(f"P2 {name} OLD form violated (falsification reproduced)",
          old_violated,
          f"3B ~ 2^{3 * Bfloor and (3 * Bfloor).bit_length()} vs budget "
          f"2^{lg_frac(old_budget)}")
    check(f"P2 {name} column form fits (+ per-profile caps)",
          fits and cap1 and cap2, f"margin ~ {margin} bits")

# =========================================================================
# P3/P4 — odd-lift census + DD-atlas at 3 cells
# =========================================================================
print("=" * 72)
print("P3/P4: odd-lift aperiodic mass, DD-atlas, banked member pins")
print("=" * 72)


def build_cell(n, k, p, smode):
    """Fiber-aligned sigma=1 chart word (cg conventions), k even."""
    assert k % 2 == 0
    dom = order_n_domain(p, n)
    half = n // 2
    nf = k // 2 - 1
    core = []
    for j in range(nf):
        core.extend([j, j + half])
    core.append(nf)
    petals = [[j, j + half] for j in range(nf + 1, half)]
    t = len(petals)
    if smode == "geom5":
        scal, v = [], 1
        for _ in range(t):
            scal.append(v)
            v = v * 5 % p
    elif smode == "consec":
        scal = [(i + 1) % p for i in range(t)]
    else:
        raise ValueError(smode)
    loc = locator([dom[j] for j in core], p)
    values = [0] * n
    for c_i, petal in zip(scal, petals):
        for j in petal:
            values[j] = c_i * ev(loc, dom[j], p) % p
    return dom, core, petals, scal, values


def odd_lift_census(n, k, p, smode, corrupt=False):
    npr, kpr = n // 2, k // 2
    nf = kpr - 1
    dom, core, petals, scal, values = build_cell(n, k, p, smode)
    # quotient word u1 (WORD normalization, #133/#137)
    domq = [dom[j] * dom[j] % p for j in range(npr)]
    Zq = [domq[j] for j in range(nf)]
    locq = locator(Zq, p)
    u1 = [0] * npr
    for i, j in enumerate(range(nf + 1, npr)):
        u1[j] = scal[i] * ev(locq, domq[j], p) % p
    if corrupt:
        u1[nf + 1] = (u1[nf + 1] + 1) % p
    # S2 structure identity U(x) = (x - x_nf) u1(x^2), x_j^2 = domq[j mod n']
    xnf = dom[nf]
    s2_ok = all(values[j] == (dom[j] - xnf) * u1[j % npr] % p for j in range(n))
    # complete census of deg<k' polys with |agr(g,u1)| >= k'
    seen = {}
    for sub in itertools.combinations(range(npr), kpr):
        xs = [domq[j] for j in sub]
        ys = [u1[j] for j in sub]
        g = interpolate(xs, ys, kpr, p)
        if g in seen:
            continue
        agr = frozenset(j for j in range(npr) if ev(g, domq[j], p) == u1[j])
        if len(agr) >= kpr:
            seen[g] = agr
    ynf = domq[nf]
    cnt = {"odd_exact_k": 0, "odd_kp1": 0, "scale2_members": 0}
    odd_wide = []
    band_classes = {}
    for g, agr in seen.items():
        gy = ev(g, ynf, p)
        if gy == 0:
            if len(agr) >= kpr + 1:
                cnt["scale2_members"] += 1
                if len(agr) in (kpr + 1, kpr + 2):
                    band_classes[agr] = g
        else:
            if len(agr) == kpr:
                cnt["odd_exact_k"] += 1
                odd_wide.append((g, agr))
            elif len(agr) == kpr + 1:
                cnt["odd_kp1"] += 1
                odd_wide.append((g, agr))
    # official end-to-end verification + band tallies
    petal_sets = [frozenset(P) for P in petals]
    t_ch = len(petals)
    wide_ok = True
    n_floor = 0
    for g, agr in odd_wide:
        S = frozenset(j for j in range(n)
                      if (dom[j] - xnf) * ev(g, domq[j % npr], p) % p == values[j])
        if len(S) != 1 + 2 * len(agr) or stab_order(S, n) != 1:
            wide_ok = False
        if any((S & P) not in (frozenset(), P) for P in petal_sets):
            wide_ok = False
        d = sum(1 for j in core if j not in S)
        m = sum(1 for P in petal_sets if P <= S)
        if d < 2 * (m - 2):
            wide_ok = False           # wide band must ALWAYS hold
        if d >= 2 * (t_ch - 2):
            n_floor += 1              # floor-band membership
    return {"cnt": cnt, "odd_wide": len(odd_wide), "n_floor": n_floor,
            "wide_ok": wide_ok, "s2_ok": s2_ok, "band_classes": band_classes,
            "npr": npr, "kpr": kpr, "t_ch": t_ch, "domq": domq, "u1": u1,
            "ynf": ynf, "p": p}


def dd_atlas_census(cell):
    """N_DD per profile a' in {k'+1, k'+2}: DD-consistent a'-supports
    containing y_nf (interpolant through k' of the points fits the rest)."""
    npr, kpr, p = cell["npr"], cell["kpr"], cell["p"]
    domq, u1 = cell["domq"], cell["u1"]
    nf_idx = kpr - 1
    others = [j for j in range(npr) if j != nf_idx]
    out = {}
    for ap in (kpr + 1, kpr + 2):
        n_dd = 0
        for sub in itertools.combinations(others, ap - 1):
            pts = (nf_idx,) + sub
            xs = [domq[j] for j in pts]
            ys = [u1[j] for j in pts]
            g = interpolate(xs[:kpr], ys[:kpr], kpr, p)
            if all(ev(g, x, p) == y for x, y in zip(xs[kpr:], ys[kpr:])):
                n_dd += 1
        out[ap] = n_dd
    return out


CELLS = [(16, 8, 97, "consec", 3), (32, 16, 97, "geom5", 63),
         (32, 12, 97, "geom5", 47)]
for (n, k, p, smode, pin) in CELLS:
    cell = odd_lift_census(n, k, p, smode)
    npr, kpr, t_ch = cell["npr"], cell["kpr"], cell["t_ch"]
    c = cell["cnt"]
    wide_total = cell["odd_wide"]
    check(f"P3 ({n},{k},{p},{smode}) S2 structure identity", cell["s2_ok"])
    check(f"P3 ({n},{k},{p},{smode}) scale>=2 member pin == {pin}",
          c["scale2_members"] == pin, f"got {c['scale2_members']}")
    check(f"P3 ({n},{k},{p},{smode}) odd lifts verified end-to-end "
          f"(|S|=2|agr|+1, aperiodic, full-petal, wide band)", cell["wide_ok"])
    supply = comb(npr - 1, kpr)
    z0 = (kpr - 1) - (t_ch - 2)
    floor_cap = (sum(comb(kpr - 1, z) * comb(t_ch, kpr - z)
                     for z in range(z0 + 1)) if z0 >= 0 else 0)
    check(f"P3 ({n},{k},{p},{smode}) wide-band aperiodic mass binomial-scale "
          f"(> supply/4)", wide_total > supply / 4,
          f"realized {wide_total} (= {c['odd_exact_k']} at |S|=k+1 + "
          f"{c['odd_kp1']} at |S|=k+3) vs supply C({npr - 1},{kpr}) = {supply}")
    check(f"P3 ({n},{k},{p},{smode}) floor-band count <= cap {floor_cap}"
          f" (z0 = {z0})", cell["n_floor"] <= floor_cap,
          f"realized floor-band aperiodic = {cell['n_floor']}")
    check(f"P4 ({n},{k},{p},{smode}) census nonempty (#137)",
          c["scale2_members"] + wide_total > 0)
    dd = dd_atlas_census(cell)
    ok = True
    detail = []
    for ap in (kpr + 1, kpr + 2):
        n_band = sum(1 for S in cell["band_classes"] if len(S) == ap)
        triv = comb(npr - 1, ap - 1)
        col = comb(npr - 1, ap)
        okc = n_band <= dd[ap] <= triv <= 719 * col
        ok = ok and okc
        detail.append(f"a'={ap}: B={n_band} <= N_DD={dd[ap]} <= "
                      f"C(n'-1,a'-1)={triv} <= 719*Q={719 * col}")
    check(f"P4 ({n},{k},{p},{smode}) clause-(ii) chain "
          f"B <= N_DD <= trivial <= 719*column", ok)
    for dline in detail:
        print("     " + dline)
    core_q = set(range(kpr))
    charts = set()
    dup = False
    for S in cell["band_classes"]:
        WP = (frozenset(S & core_q), frozenset(S - core_q))
        if WP in charts:
            dup = True
        charts.add(WP)
    check(f"P4 ({n},{k},{p},{smode}) minimal charts distinct per class", not dup)

# (16,8,97) brute official cross-check
n, k, p = 16, 8, 97
dom, core, petals, scal, values = build_cell(n, k, p, "consec")
petal_sets = [frozenset(P) for P in petals]
brute = {}
for idxs in itertools.combinations(range(n), k + 1):
    xs = [dom[j] for j in idxs]
    ys = [values[j] for j in idxs]
    poly = interpolate(xs[:k], ys[:k], k, p)
    if poly in brute:
        continue
    if any(ev(poly, x, p) != y for x, y in zip(xs[k:], ys[k:])):
        continue
    S = frozenset(j for j in range(n) if ev(poly, dom[j], p) == values[j])
    if len(S) >= k + 1:
        brute[poly] = S
ap_fp = sum(1 for poly, S in brute.items()
            if stab_order(S, n) == 1 and len(S) <= k + 4
            and all((S & P) in (frozenset(), P) for P in petal_sets))
cell168 = odd_lift_census(n, k, p, "consec")
check("P3 (16,8,97) brute official aperiodic top-band full-petal >= odd-lift "
      "count", ap_fp >= cell168["odd_wide"],
      f"brute {ap_fp} vs lifts {cell168['odd_wide']} "
      f"(non-lift = {ap_fp - cell168['odd_wide']})")

# headline #145 arithmetic
lhs = comb(63, 32)
rhs = Fraction(121, 128) * 128**6
check("P3 #145: C(63,32) > (121/128)*128^6 — wide-band clause (i) "
      "pre-falsified at (128,64), ANY q", lhs > rhs,
      f"2^{log2(lhs):.1f} vs 2^{lg_frac(rhs)}")
t128 = (128 - 63) // 2
z0 = 31 - (t128 - 2)
fcap = (sum(comb(31, z) * comb(t128, 32 - z) for z in range(z0 + 1))
        if z0 >= 0 else 0)
check("P3 #145: floor-band cap at (128,64) is poly (< n^2)",
      0 <= fcap < 128**2, f"cap = {fcap} (t_ch = {t128}, z0 = {z0})")

# =========================================================================
# P5 — consumer arithmetic at official shapes
# =========================================================================
print("=" * 72)
print("P5: consumer arithmetic (719 allowance, dominance, ratios, ledger)")
print("=" * 72)
ok719 = all(719 == (2**s) ** 6 // comb(2**s + 6, 6) for s in (41, 42, 43, 44))
check("P5 719 == floor(n^6/C(n+6,6)) at the four official maximal rows", ok719)

worst = Fraction(0)
for s in range(13, 21):
    nn = 2**s
    for rd in (2, 4, 8, 16):
        kk = nn // rd
        t = (nn - kk) // 2
        q2 = comb(nn // 2 - 1, kk // 2 + 1)
        tot = Fraction(0)
        M = 2
        while M <= t:
            A = own_A(kk, M)
            h = A // M
            if h <= nn // M - 1:
                tot += comb(nn // M - 1, h)
            M *= 2
        worst = max(worst, tot / q2)
excess = worst - 1
check("P5 dominance: sum_{M<=t} Q_M(A_own) <= (1 + 2^-10) Q_2(k+2), s=13..20 "
      "all rates", worst <= 1 + Fraction(1, 1024),
      f"max excess ~ 2^{lg_frac(excess) if excess > 0 else '-inf'}")


def log2comb(a, b):
    return (lgamma(a + 1) - lgamma(b + 1) - lgamma(a - b + 1)) / LN2


dom_max = max(log2comb(2**s // 4 - 1, 2**40 // 4 + 1)
              - log2comb(2**s // 2 - 1, 2**40 // 2 + 1) for s in (41, 42, 43, 44))
check("P5 dominance at maximal rows: log2(Q_4/Q_2) < -2^30", dom_max < -(2**30),
      f"max log2 ratio = {dom_max:.3e}")

max_r1 = max_r2 = max_gate = Fraction(0)
for s in range(13, 45):
    nn = 2**s
    for rd in (2, 4, 8, 16):
        kk = nn // rd
        npr, kpr = nn // 2, kk // 2
        max_r1 = max(max_r1, Fraction(kpr + 1, npr - 1 - kpr))
        max_r2 = max(max_r2, Fraction(kpr + 2, npr - 2 - kpr))
        t = (nn - kk) // 2
        M = 2
        while M <= t:
            A = own_A(kk, M)
            if A < nn:
                max_gate = max(max_gate, Fraction(nn, nn - A))
            M *= 2
check("P5 clause-(ii) trivial per-profile ratios <= 1.01 (hence << 719) over "
      "the official grid",
      max_r1 <= Fraction(101, 100) and max_r2 <= Fraction(101, 100),
      f"max r1 = {float(max_r1):.6f}, r2 = {float(max_r2):.6f}")
check("P5 gate COL cap n/(n-A_own) <= 4 over official grid, M <= t",
      max_gate <= 4, f"max = {float(max_gate):.4f}")
check("P5 K4 package: 121/128 < 1 primitive-only; (64/63)(121/128) == 121/126 "
      "(old line reproduced, 64/63 now retired)",
      Fraction(121, 128) < 1
      and Fraction(64, 63) * Fraction(121, 128) == Fraction(121, 126))

# =========================================================================
# P6 — mutation controls
# =========================================================================
print("=" * 72)
print("P6: mutation controls (all must TRIP)")
print("=" * 72)
check("MC1 TRIPS: C_col = 1 line violated on banked data", mc1_trips > 0,
      f"{mc1_trips} trips")
check("MC2 TRIPS: shifted column C(n/M-1, h+2) line violated on banked data",
      mc2_trips > 0, f"{mc2_trips} trips")
mut = odd_lift_census(32, 16, 97, "geom5", corrupt=True)
check("MC3 TRIPS: corrupted u1 breaks the S2 identity", not mut["s2_ok"])
check("MC3b TRIPS: corrupted u1 breaks the banked 63-member pin",
      mut["cnt"]["scale2_members"] != 63,
      f"corrupted census = {mut['cnt']['scale2_members']}")
print("MC4 == P2 rows above: the OLD (121/128)n^6 line FAILS at every g1a "
      "instance while the column line PASSES — the check separates the forms.")

print("=" * 72)
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURES:")
    for f in FAILS:
        print("  -", f)
    sys.exit(1)
print("RESULT: ALL CHECKS PASS")
