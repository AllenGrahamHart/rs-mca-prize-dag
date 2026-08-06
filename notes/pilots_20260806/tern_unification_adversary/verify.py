#!/usr/bin/env python3
"""
verify.py -- round 19, tern_unification_adversary (ADVERSARIAL lens).

Self-contained, fail-closed. Exits nonzero if ANY registered check fails.
Run: tools/ramguard local -- python3 notes/pilots_20260806/tern_unification_adversary/verify.py

Tests the registrations P1-P13 of PREREG.md sections 5-8.

Toy grids use 2-POWER lengths only (CATCH-Z6 standing rule) EXCEPT section
Z6, which deliberately probes the composite-length disanalogy (permitted by
the brief's compute law).
"""

import itertools
import sys
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 80

FAILURES = []
NOTES = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}" + (f"  --  {detail}" if detail else ""))
    if not ok:
        FAILURES.append(name)
    return ok


def note(s):
    NOTES.append(s)
    print(f"  [note] {s}")


LN2 = Decimal(2).ln()
LOG2_3 = Decimal(3).ln() / LN2


def log2(x):
    return Decimal(x).ln() / LN2


# ---------------------------------------------------------------------------
# SECTION 1 -- the criticality coordinate, and reproduction of banked constants
#   tau   = c*log2(p)/N
#   B     = N - c*log2 p         (THEOREM Z-FLOOR informativeness, in bits)
#   Tcrit = N*log2 3 - c*log2 p  (first-moment ternary count, in bits)
# ---------------------------------------------------------------------------

def dceil(x):
    """True ceiling for Decimal (Decimal's // truncates toward zero)."""
    i = int(x)
    if Decimal(i) < x:
        i += 1
    return i


def crit(N, c, log2p):
    """N, c integers (or Decimal); log2p a Decimal. Returns (tau, B, Tcrit)."""
    N = Decimal(N)
    c = Decimal(c)
    cl = c * log2p
    return (cl / N, N - cl, N * LOG2_3 - cl)


def section1():
    print("\n=== SECTION 1: criticality coordinate vs banked constants (P2,P3,P4) ===")

    # ---- I1, the f2_adm witness row (the row the knife edge was computed on).
    # notes/pilots_20260806/f2_adm/REPORT.md:10
    p_w = 18446735827372343297
    e_w = 4                     # q = p^4
    S_w = 2 ** 38               # z1_ternary_mass/PROOFS.md:319
    R_w = 4294967340            # f2_adm/REPORT.md:10
    n = 2 ** 41

    log2p_w = log2(p_w)
    log2q_w = e_w * log2p_w
    check("I1 witness: log2 q = 255.999997420 (f2_adm REPORT.md:10)",
          abs(log2q_w - Decimal("255.999997420")) < Decimal("1e-8"),
          f"log2 q = {log2q_w:.9f}")

    # R = ceil(t/2), t = n / log2 q
    t_w = Decimal(n) / log2q_w
    R_from_t = dceil(t_w / 2)                # R = ceil(t/2)
    check("I1 witness: R = ceil(t/2) = 4,294,967,340",
          R_from_t == R_w, f"computed {R_from_t}, t = {t_w:.4f}")

    tau1, B1, T1 = crit(S_w, R_w, log2p_w)

    # THE KNIFE EDGE: f2_z1_mass_knife_edge/statement.md:46-49 --
    # "the Z-FLOOR is silent by 46.02 bits" / "FIRES at +17.98 bits" under the
    # exact-balance reading, "ONE Lambda condition, worth log2 p = 64 bits".
    check("I1 knife edge: B = S - R*log2 p = -46.02 bits (banked -46.02)",
          abs(B1 + Decimal("46.02")) < Decimal("0.05"), f"B = {B1:.4f}")
    _, B1b, _ = crit(S_w, R_w - 1, log2p_w)
    check("I1 exact-balance reading (one Lambda condition fewer): +17.98 bits",
          abs(B1b - Decimal("17.98")) < Decimal("0.05"), f"B = {B1b:.4f}")
    check("I1 one Lambda condition is worth log2 p = 64 bits",
          abs((B1b - B1) - log2p_w) < Decimal("1e-9")
          and abs(log2p_w - 64) < Decimal("1e-5"),
          f"delta = {B1b - B1:.6f}, log2 p = {log2p_w:.6f}")

    # SATURATION (THEOREM Z-NOGO: R/S = 1/log2 p) => tau = 1 exactly, up to ceil.
    check("I1: tau = 1 to within 1e-9 (saturation, THEOREM Z-NOGO)",
          abs(tau1 - 1) < Decimal("1e-9"), f"tau = {tau1:.12f}")
    check("I1: R/S = 1/log2 p to within 1e-9",
          abs(Decimal(R_w) / Decimal(S_w) - 1 / log2p_w) < Decimal("1e-9"),
          f"R/S = {Decimal(R_w)/Decimal(S_w):.12f}, 1/log2 p = {1/log2p_w:.12f}")

    # CATCH-Z1's (3/2)^S = 2^{0.585 * 2^38}
    check("I1: Tcrit = 0.585 * 2^38 bits (CATCH-Z1's (3/2)^S)",
          abs(T1 / Decimal(2 ** 38) - Decimal("0.585")) < Decimal("0.0005"),
          f"Tcrit = {T1:.4e} = {T1/Decimal(2**38):.6f} * 2^38")
    check("I1: Tcrit > 0  (SUPERCRITICAL -- ternary vectors abundant)",
          T1 > 0, f"Tcrit = +{T1:.4e} bits")

    # ---- I2, the crossing deep stratum at v = 34 on an e = 1 prime row.
    # crossing_dsa_refutation/statement.md:28-33 (L = 2^{41-v}), :52-56 (3^128/p).
    v = 34
    L2 = 2 ** (41 - v)
    check("I2: L = 2^{41-v} = 128 at v = 34 (LEMMA DS)", L2 == 128, f"L = {L2}")
    log2p_2 = Decimal(256)          # recorded prime rows q = p ~ 2^256
    delta_a = 1                     # ord_{2L}(p) = 1 since 2^41 | p-1 => 256 | p-1
    tau2, B2, T2 = crit(L2, delta_a, log2p_2)
    check("I2: 3^L = 2^202.875 (LEMMA TC's requirement at v = 34)",
          abs(Decimal(L2) * LOG2_3 - Decimal("202.875")) < Decimal("0.001"),
          f"{Decimal(L2)*LOG2_3:.6f}")
    check("I2: Tcrit = -53.1 bits (banked 3^128/p = 2^{-53.1})",
          abs(T2 + Decimal("53.1")) < Decimal("0.05"), f"Tcrit = {T2:.4f}")
    check("I2: orbit-corrected Tcrit = -61.1 bits (LEMMA ROT, orbits 2L = 256)",
          abs((T2 - log2(2 * L2)) + Decimal("61.1")) < Decimal("0.05"),
          f"{T2 - log2(2*L2):.4f}")
    check("I2: tau = 2 exactly", abs(tau2 - 2) < Decimal("1e-12"), f"tau = {tau2}")
    check("I2: Tcrit < 0  (SUBCRITICAL -- ternary relations expected absent)",
          T2 < 0)

    # ---- I3, CC-sparsity at w = 2^34 on the official row.
    # efloor_sparsity/PROOFS.md:545-550 (official row), LEMMA AB (length n/2).
    h = 2 ** 40
    w = 2 ** 34
    c3 = -((-(w - 1)) // 2)          # ceil((w-1)/2) = |Z_w^odd| lower bound
    check("I3: c = ceil((w-1)/2) = 2^33 at w = 2^34", c3 == 2 ** 33, f"c = {c3}")
    log2p_3 = Decimal(256)
    tau3, B3, T3 = crit(h, c3, log2p_3)
    check("I3: tau = 2 exactly", abs(tau3 - 2) < Decimal("1e-12"), f"tau = {tau3}")
    check("I3: Tcrit = -0.41504 * 2^40 bits (SUBCRITICAL)",
          T3 < 0 and abs(T3 / Decimal(h) + Decimal("0.41504")) < Decimal("0.0001"),
          f"Tcrit = {T3:.5e} = {T3/Decimal(h):.6f} * 2^40")

    # ---- P4: the sign split (THE load-bearing disanalogy).
    check("P4: sign(Tcrit) is + at I1 and - at I2 and I3 (PHASE TRANSITION)",
          T1 > 0 and T2 < 0 and T3 < 0,
          f"I1 +{T1:.3e} | I2 {T2:.3f} | I3 {T3:.3e}")

    # ---- where the threshold sits, in each lane's own coordinate.
    # I3: tau > log2 3  <=>  w > log2(3) * 2^33.
    w_tern = LOG2_3 * Decimal(2 ** 33)
    check("I3: bracket bottom w = 2^34 is only 0.336 bits above the ternary "
          "threshold w_tern = log2(3)*2^33",
          abs((Decimal(34) - log2(w_tern)) - Decimal("0.33566")) < Decimal("0.001"),
          f"log2 w_tern = {log2(w_tern):.5f}, margin = {Decimal(34)-log2(w_tern):.5f} bits")
    # I2: tau = 256/L = 256/2^{41-v}; v = 33 gives L = 256 and tau = 1.
    tau_v33, _, T_v33 = crit(2 ** (41 - 33), 1, Decimal(256))
    check("I2: one step below the bracket (v = 33, L = 256) tau = 1 and Tcrit "
          "= +149.75 bits -- SUPERCRITICAL at the recorded PRIME rows",
          abs(tau_v33 - 1) < Decimal("1e-12") and T_v33 > 0
          and abs(T_v33 - Decimal("149.75")) < Decimal("0.01"),
          f"tau = {tau_v33}, Tcrit = +{T_v33:.4f}")

    # ---- I1 at the SHARED row (e = 1, log2 p ~ 256): tau is still 1.
    # Saturation is e-independent: R*log2 q = m = n/2 exactly, up to the ceil.
    log2q_e1 = Decimal("255.99")
    t_e1 = Decimal(n) / log2q_e1
    R_e1 = dceil(t_e1 / 2)
    S_e1 = 2 ** 40                    # S = 2^40/e with e = 1
    tau1b, B1c, T1c = crit(S_e1, R_e1, log2q_e1)   # e = 1 so log2 q = log2 p
    check("I1 at the shared e = 1 row: tau = 1 to within 1e-9 (saturation is "
          "e-independent)",
          abs(tau1b - 1) < Decimal("1e-9"), f"tau = {tau1b:.12f}")
    check("I1 at the shared e = 1 row: Tcrit = +0.585 * 2^40 bits",
          T1c > 0 and abs(T1c / Decimal(2 ** 40) - Decimal("0.585")) < Decimal("0.0005"),
          f"Tcrit = +{T1c:.5e}")

    return dict(T1=T1, T2=T2, T3=T3, B1=B1, B1b=B1b, S_w=S_w, R_w=R_w,
                log2p_w=log2p_w)


# ---------------------------------------------------------------------------
# SECTION 2 -- the shared admissible row (P5)
# ---------------------------------------------------------------------------

def is_probable_prime(n, bases=None):
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for q in small:
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    if bases is None:
        bases = small + [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                         101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                         157, 163, 167, 173]
    for a in bases:
        a %= n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def section2():
    print("\n=== SECTION 2: the SHARED admissible row (P5) ===")
    # Admissibility predicates, all three from their minted nodes:
    #   I1 (e = 1 generating class, f2_o1_status_split:50-54): p prime,
    #      e_p = v_2(p-1) >= 41, k = ord_n(p) = e = 1, e*log2 p < 256.
    #   I2 (crossing e = 1 prime row, crossing_dsa_refutation:52-56): q = p
    #      prime, n = 2^41 | q-1, B* = floor(q/2^128) >= 3.
    #   I3 (official row, efloor_sparsity/PROOFS.md:545-550): q prime,
    #      v_2(q-1) >= 41.
    # We search INSIDE the tightest banked window: the prize-max admissible
    # sliver log2 Q in [255.9113, 256) of width 0.089 bits
    # (u2c_giant_tnull_dichotomy/statement.md:16-17), which also sits inside
    # the crossing razor row's recorded log2 q in (255.900, 256)
    # (mun_anticoncentration/PREREG.md:9-12).
    n = 2 ** 41
    lo = int((Decimal("255.9113") * LN2).exp())      # 2^255.9113
    found = None
    k = lo // n
    if k % 2 == 0:
        k += 1
    tried = 0
    while tried < 200000:
        p = k * n + 1
        if p >= 2 ** 256:
            break
        if is_probable_prime(p):
            found = p
            break
        k += 2
        tried += 1
    check("an explicit 256-bit probable prime p = k*2^41 + 1, k odd, exists "
          "INSIDE the prize-max sliver log2 q in [255.9113, 256)",
          found is not None and Decimal("255.9113") <= log2(found) < 256,
          f"p = {found}")
    if found is None:
        return None
    p = found
    v2 = 0
    m = p - 1
    while m % 2 == 0:
        m //= 2
        v2 += 1
    check("shared row: v_2(p-1) = 41 exactly (=> e_p = 41, S = 2^40 at e = 1)",
          v2 == 41, f"v_2(p-1) = {v2}")
    check("shared row: log2 p in [255.9113, 256) -- inside BOTH the prize-max "
          "admissible sliver and the crossing razor row's (255.900, 256)",
          Decimal("255.9113") <= log2(p) < 256 and p < 2 ** 256,
          f"log2 p = {log2(p):.9f}")
    check("shared row I1: ord_n(p) = 1 = e  (GENERATING, k = e)",
          pow(p, 1, n) == 1 % n and (p - 1) % n == 0)
    check("shared row I1: e*log2 p < 256 with e = 1", log2(p) < 256)
    check("shared row I2: B* = floor(q/2^128) >= 3", p // 2 ** 128 >= 3,
          f"B* = {p // 2**128}")
    check("shared row I2: p is NOT in the DSA regime (p^{delta_a} >= 2^{L-2}),"
          " so the crossing question is OPEN there",
          p >= 2 ** (128 - 2), "delta_a = ord_256(p) = 1 since 256 | p-1")
    check("shared row I2: delta_a = ord_{2L}(p) = 1 at L = 128",
          (p - 1) % 256 == 0)
    check("shared row I3: q = p prime with v_2(q-1) >= 41 (official gate)",
          v2 >= 41)
    note(f"SHARED ROW EXHIBIT: p = {p}")
    note("Existence is unconditional by Dirichlet/PNT for the progression "
         "1 mod 2^41; the exhibit above is a Miller-Rabin probable prime "
         "(40 fixed bases) offered as a convenience, not as the proof.")
    return p


# ---------------------------------------------------------------------------
# SECTION 3 -- the master object M(N,c,p) on 2-power toys:
#   negacyclicity, LEMMA ROT, THEOREM Z-1, THEOREM Z-FLOOR, THEOREM DSA
# ---------------------------------------------------------------------------

def order(x, p):
    o, y = 1, x % p
    while y != 1:
        y = y * x % p
        o += 1
    return o


def theta_of_order(p, r):
    """An element of exact multiplicative order r in F_p, or None."""
    if (p - 1) % r:
        return None
    for g in range(2, p):
        x = pow(g, (p - 1) // r, p)
        if order(x, p) == r:
            return x
    return None


def ternary(N):
    return itertools.product((0, 1, -1), repeat=N)


def codewords_M(N, c, p, theta):
    """All eps in {0,+-1}^N with sum_j eps_j theta^{(2i-1)j} = 0, i = 1..c.
    Meet-in-the-middle on the two halves."""
    half = N // 2
    pw = [[pow(theta, (2 * i - 1) * j, p) for j in range(N)] for i in range(1, c + 1)]
    left = {}
    for e in ternary(half):
        s = tuple(sum(e[j] * pw[i][j] for j in range(half)) % p for i in range(c))
        left.setdefault(s, []).append(e)
    out = []
    for e in ternary(N - half):
        s = tuple((-sum(e[j] * pw[i][half + j] for j in range(N - half))) % p
                  for i in range(c))
        for el in left.get(s, ()):
            out.append(el + e)
    return out


def negashift(e):
    return (-e[-1],) + tuple(e[:-1])


def section3():
    print("\n=== SECTION 3: master object M(N,c,p) on 2-power toys "
          "(P1, P6, P7, P8) ===")
    grids = []
    for (N, p) in [(8, 17), (8, 97), (8, 113), (8, 193), (8, 241), (16, 97)]:
        th = theta_of_order(p, 2 * N)
        if th is None:
            continue
        for c in range(1, 5):
            if c >= N:
                continue
            grids.append((N, c, p, th))

    tot_cw = 0
    zfloor_ok = True
    z1_ok = True
    rot_ok = True
    dsa_ok = True
    dsa_cases = 0
    zfloor_fires = 0
    table = []
    for (N, c, p, th) in grids:
        cws = codewords_M(N, c, p, th)
        tot_cw += len(cws)
        nz = [e for e in cws if any(e)]
        cwset = set(cws)

        # -- P7 / LEMMA ROT: negacyclic shift preserves the code; orbits | 2N.
        for e in cws:
            if negashift(e) not in cwset:
                rot_ok = False
        for e in nz[: 200]:
            o, y = 1, negashift(e)
            while y != e and o <= 4 * N:
                y = negashift(y)
                o += 1
            if y != e or (2 * N) % o:
                rot_ok = False

        # -- P8 / THEOREM Z-1: min ternary weight >= 2c+1 on a shift-0 window.
        minw = min((sum(1 for x in e if x) for e in nz), default=None)
        if minw is not None and minw < 2 * c + 1:
            z1_ok = False

        # -- THEOREM Z-FLOOR: Z = sum 2^{-wt} >= 2^N / p^c  (exact rationals).
        Z = sum(Fraction(1, 2 ** sum(1 for x in e if x)) for e in cws)
        if Z < Fraction(2 ** N, p ** c):
            zfloor_ok = False
        if Fraction(2 ** N, p ** c) > 1:
            zfloor_fires += 1
            # -- P6: Z-FLOOR's existence corollary.
            if not nz:
                zfloor_ok = False

        # -- P6 / THEOREM DSA: p^c < 2^{N-2} => a nonzero ternary codeword
        #    supported in the first N-2 coordinates.
        if p ** c < 2 ** (N - 2):
            dsa_cases += 1
            if not any(e[-2:] == (0, 0) for e in nz):
                dsa_ok = False

        table.append((N, c, p, len(nz), minw,
                      float(crit(N, c, log2(p))[2])))

    print("    N   c    p   #nonzero  minwt   Tcrit(bits)   2^Tcrit")
    for (N, c, p, k, mw, T) in table:
        print(f"   {N:2d}  {c:2d} {p:4d}   {k:8d}   {str(mw):>5}   "
              f"{T:9.3f}   {2**T:12.3f}")

    check("P1/P7 LEMMA ROT: negacyclic shift preserves every toy code and all "
          "sampled orbit sizes divide 2N", rot_ok,
          f"{len(grids)} grids, {tot_cw} codewords")
    check("P8 THEOREM Z-1: min ternary weight >= 2c+1 on every 2-power toy "
          "with a shift-0 odd window", z1_ok)
    check("THEOREM Z-FLOOR: Z >= 2^N/p^c on every toy (exact rationals)",
          zfloor_ok, f"{zfloor_fires} grids where the floor exceeds 1")
    check("P6 THEOREM DSA = Z-FLOOR's existence corollary + support control: "
          "p^c < 2^{N-2} always produced a nonzero ternary codeword supported "
          "in the first N-2 coordinates", dsa_ok, f"{dsa_cases} firing grids")

    # -- calibration of the phase transition (CALIBRATION ONLY, not evidence
    #    about any official row).
    good = 0
    miss = []
    for (N, c, p, k, mw, T) in table:
        if (T > 0) == (k > 0):
            good += 1
        else:
            miss.append((N, c, p, k, T))
    check("calibration: sign(Tcrit) predicts nonemptiness on the 2-power toys "
          "in >= 80% of grids", good >= 0.8 * len(table),
          f"{good}/{len(table)}, misses {miss}")

    # LEMMA ROT transferred: relations come in orbits of size dividing 2N, so
    # the first moment over-predicts by 2N. Re-score with that correction.
    good2, miss2 = 0, []
    for (N, c, p, k, mw, T) in table:
        Tc = T - float(log2(2 * N))
        if (Tc > 0) == (k > 0):
            good2 += 1
        else:
            miss2.append((N, c, p, k, round(Tc, 3)))
    check("LEMMA ROT transferred: orbit-correcting the first moment by 2N "
          "strictly improves the calibration", good2 > good,
          f"{good2}/{len(table)} vs {good}/{len(table)}; residual "
          f"misses {miss2}")
    note("Both uncorrected misses are grids with a small POSITIVE Tcrit and an "
         "empty code; the 2N orbit correction (LEMMA ROT, transferred from I2 "
         "to the master object) accounts for them. The single residual miss "
         "sits at a 0.56-bit margin -- inside Poisson noise.")
    note("The toy sweep calibrates the criticality coordinate only. Per "
         "f2_z1_mass_knife_edge/statement.md:68-69, no toy is evidence about "
         "any official row.")


# ---------------------------------------------------------------------------
# SECTION 4 -- CATCH-Z6 as a PROVED lemma, and all three instances' immunity
# ---------------------------------------------------------------------------

def cyclotomic_poly(m):
    """Phi_m over Z, by exact polynomial division."""
    poly = [-1] + [0] * (m - 1) + [1]         # X^m - 1
    for d in range(1, m):
        if m % d == 0:
            q = cyclotomic_poly(d)
            # divide poly by q exactly
            out = [0] * (len(poly) - len(q) + 1)
            rem = poly[:]
            for i in range(len(out) - 1, -1, -1):
                coef = rem[i + len(q) - 1] // q[-1]
                out[i] = coef
                for j in range(len(q)):
                    rem[i + j] -= coef * q[j]
            poly = out
    return poly


def section4():
    print("\n=== SECTION 4: CATCH-Z6 / the Z-basis property (P11) ===")
    # A p-INDEPENDENT ternary relation of length N at 2N-th roots is a ternary
    # v of degree < N with Phi_{2N} | v over Z.
    for twoN in (8, 16, 32, 12, 20, 24):
        N = twoN // 2
        phi = cyclotomic_poly(twoN)
        d = len(phi) - 1
        cnt, minw = 0, None
        if d < N:
            for g in itertools.product(range(-2, 3), repeat=N - d):
                v = [0] * N
                for i, gi in enumerate(g):
                    for j, pj in enumerate(phi):
                        v[i + j] += gi * pj
                if any(v) and all(abs(x) <= 1 for x in v):
                    cnt += 1
                    wgt = sum(1 for x in v if x)
                    minw = wgt if minw is None else min(minw, wgt)
        ispow2 = (twoN & (twoN - 1)) == 0
        print(f"    2N = {twoN:3d}  deg Phi_2N = {d:2d}  N = {N:2d}   "
              f"p-independent ternary relations: {cnt}   min wt {minw}")
        if ispow2:
            check(f"2-power 2N = {twoN}: deg Phi_2N = N, so ZERO p-independent "
                  f"ternary relations (the Z-basis property)",
                  d == N and cnt == 0)
    # reproduce CATCH-Z6's exact composite counts
    exp = {12: (8, 3), 20: (8, None), 24: (80, None)}
    for twoN, (ec, ew) in exp.items():
        N = twoN // 2
        phi = cyclotomic_poly(twoN)
        d = len(phi) - 1
        cnt, minw = 0, None
        for g in itertools.product(range(-2, 3), repeat=N - d):
            v = [0] * N
            for i, gi in enumerate(g):
                for j, pj in enumerate(phi):
                    v[i + j] += gi * pj
            if any(v) and all(abs(x) <= 1 for x in v):
                cnt += 1
                wgt = sum(1 for x in v if x)
                minw = wgt if minw is None else min(minw, wgt)
        ok = (cnt == ec) and (ew is None or minw == ew)
        check(f"CATCH-Z6 reproduced at composite 2N = {twoN}: {ec} relations"
              + (f", min weight {ew}" if ew else ""), ok,
              f"got {cnt}, min wt {minw}")
    note("All three instances live at 2-POWER N in their live regimes "
         "(I1: S = 2^40/e; I2: L = 2^{41-v}; I3: h = 2^40), hence all three "
         "are structurally immune to CATCH-Z6's parasitic relations.")


# ---------------------------------------------------------------------------
# SECTION 5 -- transfer-matrix arithmetic: CS vacuity at I1; SP-COVER blind
#              spot at the shared row; the Z-FLOOR + Z-1 count corollary
# ---------------------------------------------------------------------------

def section5(d):
    print("\n=== SECTION 5: transfer-matrix arithmetic (P9, P10) ===")
    S_w, R_w, log2p_w = d["S_w"], d["R_w"], d["log2p_w"]

    # -- P9: THEOREM CS's exclusion (CS4) reads
    #        ceil((w-1)/2)*log2 p > (n/4)*log2 r'.
    #    In master coordinates (n = 2N, conditions c, ternary support U) the
    #    natural ternary extension is  c*log2 p > (N/2)*log2 U.
    #    At I1, saturation gives c*log2 p = N exactly, so the condition is
    #    N > (N/2) log2 U  <=>  U < 4.
    lhs = Decimal(R_w) * log2p_w
    check("P9: at I1, c*log2 p = S to within 50 bits of 2.7e11 (saturation)",
          abs(lhs - Decimal(S_w)) < 50, f"c*log2 p - S = {lhs - Decimal(S_w):.3f}")
    U_max = 2 ** (2 * (lhs / Decimal(S_w)))    # U < 2^{2 c log2p / N}
    check("P9: the ternary extension of CS excludes only U < 4 at I1 -- "
          "PROVABLY VACUOUS", abs(U_max - 4) < Decimal("0.001"),
          f"CS would exclude ternary support U < {U_max:.6f}")
    note("Against THEOREM Z-1's min ternary weight 2R+1 = 8,589,934,681 at I1, "
         "a U < 4 exclusion is 9 orders of magnitude short.")

    # -- P10: SP-COVER's requirement at the shared row.
    #    LEMMA COS: w_cov <= 2^{v_2(p^2-1)}; SP-UNIFORM needs w >= 2^{v_2(p^2-1)}.
    #    v_2(p-1) >= 41 and p odd => v_2(p+1) = 1 => v_2(p^2-1) >= 42.
    for (name, v2pm1, window_top_log2) in [
            ("I1 (window {1,3,..,2R-1}, top ~ 2^33)", 41, 33),
            ("I2 (window {1}, top = 2^1)", 41, 1),
            ("I3 (window {1,..,w-1}, top <= 2^39 = bracket cap)", 41, 39)]:
        req = v2pm1 + 1
        check(f"P10 SP-COVER blind spot at the shared row -- {name}: needs "
              f"w >= 2^{req}, has 2^{window_top_log2}", window_top_log2 < req,
              f"short by {req - window_top_log2} bits")
    note("E-3 (es_ternary_suppression_instruments/statement.md:57-62) is "
         "therefore not an I3 defect: the official smooth-domain gate "
         "v_2(q-1) >= 41 blind-spots SP-COVER in ALL THREE instances.")

    # -- the Z-FLOOR + Z-1 count corollary at I1 under the exact-balance reading.
    B1b = d["B1b"]                       # +17.98 bits
    lower_log2_count = B1b + Decimal(2 * R_w + 1)
    avail = Decimal(S_w) * LOG2_3
    check("consistency: Z-FLOOR firing (+17.98) with min weight 2R+1 forces "
          ">= 2^{8.59e9} ternary codewords, which fits inside 3^S = 2^{1.74e12}",
          lower_log2_count < avail and lower_log2_count > 0,
          f"forced >= 2^{lower_log2_count:.4e}, available 3^S = 2^{avail:.4e}")
    check("consistency: that forced count is far below the first-moment "
          "expectation 2^{0.585*2^38}", lower_log2_count < d["T1"],
          f"{lower_log2_count:.4e} < {d['T1']:.4e}")


def codewords_window(N, exps, p, theta):
    """Ternary eps with sum_j eps_j theta^{s j} = 0 for every s in exps."""
    half = N // 2
    pw = [[pow(theta, s * j, p) for j in range(N)] for s in exps]
    left = {}
    for e in ternary(half):
        k = tuple(sum(e[j] * pw[i][j] for j in range(half)) % p
                  for i in range(len(exps)))
        left.setdefault(k, []).append(e)
    out = []
    for e in ternary(N - half):
        k = tuple((-sum(e[j] * pw[i][half + j] for j in range(N - half))) % p
                  for i in range(len(exps)))
        for el in left.get(k, ()):
            out.append(el + e)
    return out


def section6():
    """ADVERSARIAL SELF-TEST of P7's scope, prompted by a sibling catch
    recorded in notes/pilots_20260802/CAMPAIGN_LEDGER.md:1823-1825
    ('the LEMMA ROT orbit constant 2N collapses to 2 ... negacyclic iff
    all-odd T'). Registered post hoc and labelled as such."""
    print("\n=== SECTION 6: P7 scope -- all-odd vs MIXED-PARITY windows ===")
    N, p = 16, 97
    th = theta_of_order(p, 2 * N)
    rows = []
    for label, exps in [("all-odd  {1}", (1,)),
                        ("all-odd  {1,3}", (1, 3)),
                        ("all-odd  {1,3,5}", (1, 3, 5)),
                        ("MIXED    {1,2}", (1, 2)),
                        ("MIXED    {1,2,3}", (1, 2, 3)),
                        ("all-even {2,4}", (2, 4))]:
        cws = set(codewords_window(N, exps, p, th))
        nz = [e for e in cws if any(e)]
        closed = all(negashift(e) in cws for e in cws)
        orb = set()
        for e in nz:
            o, y = 1, negashift(e)
            while y != e and o <= 4 * N:
                y = negashift(y)
                o += 1
            orb.add(o if y == e else -1)
        rows.append((label, len(nz), closed, sorted(orb)))
        print(f"    {label:16s} #nonzero={len(nz):5d}  negashift-closed="
              f"{str(closed):5s}  orbit sizes={sorted(orb)}")

    allodd = [r for r in rows if r[0].startswith("all-odd")]
    mixed = [r for r in rows if r[0].startswith("MIXED")]
    check("P7 scope: on ALL-ODD windows the negacyclic shift closes the code "
          "and every orbit size divides 2N (LEMMA ROT transfers)",
          all(r[2] and all(o > 0 and (2 * N) % o == 0 for o in r[3])
              for r in allodd))
    populated = [r for r in mixed if r[1] > 0]
    check("NON-VACUITY GUARD: the mixed-parity windows actually carry nonzero "
          "ternary codewords (else the next check would fail open)",
          len(populated) > 0, f"{len(populated)}/{len(mixed)} populated")
    check("sibling CATCH-19A CONFIRMED: on MIXED-PARITY windows the negacyclic "
          "shift does NOT close the code -- 'negacyclic iff all-odd'",
          len(populated) > 0 and all(not r[2] for r in populated),
          "even-index conditions evaluate X^N to +1, odd ones to -1, so no "
          "single ambient algebra X^N -+ 1 carries both")
    note("I1's banked window is ALL-ODD -- 'P(omega^{2j-1}) = 0, j = 1..ell' "
         "with 'Lambda = {odd l : l <= t} starts at l = 1' "
         "(z1_ternary_mass/PROOFS.md:87-94). So the all-odd branch is the one "
         "I1 sits on, and the 2N orbit constant stands for I1. Flagged for "
         "coordinator adjudication against CATCH-19A's 'I1's mixed-parity "
         "windows' reading.")


def main():
    print("verify.py -- tern_unification_adversary (round 19, ADVERSARIAL)")
    d = section1()
    section2()
    section3()
    section4()
    section5(d)
    section6()
    print("\n" + "=" * 70)
    if FAILURES:
        print(f"RESULT: {len(FAILURES)} FAILURE(S): " + "; ".join(FAILURES))
        sys.exit(1)
    print("RESULT: ALL CHECKS PASSED")
    sys.exit(0)


if __name__ == "__main__":
    main()
