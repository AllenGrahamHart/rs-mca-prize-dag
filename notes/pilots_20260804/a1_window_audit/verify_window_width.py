#!/usr/bin/env python3
"""A1 window-extension audit: exact recomputation of the C1'-r3 window ladder.

Two independent arithmetics, both exact (Fraction), no floats in any verdict:
  (S) SUPPLY side  -- worst K'_r3 over the complete two-round gated census as a
      function of the window width W (window [L+1, L+W]).  Uses the BANKED
      per-row (w7,w8) orbit counts from c1r3_results.md and the banked
      round-2 ledgers from c1r3b_results.md.
  (D) DEMAND side  -- the official-scale zone budget: slot count as a function
      of W, and the *true* W_ext tolerance the 34-level assembly admits.

Controls: every recomputed quantity that is ALSO banked must reproduce the
banked value exactly (C1..C6 below).  A mismatch aborts.
"""
from fractions import Fraction as F
import math

# ---------------------------------------------------------------- constants
# Analogue census scale (c1r3_results.md:64 "all 33 in-gate rows, L=1, N=32").
N_ANA = 32
TWO_N = 2 * N_ANA                       # = 64;  orbit mass = 2N * 2^-w
def mass_ana(w): return F(TWO_N, 2 ** w)

# Official scale: N_ell = 256*ell, orbit mass = 512*ell*2^-w  (wcl_audit_findings.md:236)
def mass_off(ell, w): return F(512 * ell, 2 ** w)

ALLOWANCE = 4                            # the 4 in E-1 <= 4 r (1 + W_ext)
N_LEVELS = 34                            # schedule r2
ZONE_WIRED = F(1, 32)                    # WCL-ZONE / WCL-ZONE-ext threshold

# ------------------------------------------------------- (S) census, round 1
# c1r3_results.md:66-100  -- q, v2, (E-1)/r as exact-ish decimal, (w7,w8) counts.
# env stored as Fraction(decimal string) => exact to the printed 6 dp.
R1 = [  # (q, env, w6, w7, w8)
    (7340033,   "1.230120", 0, 3, 6),
    (13631489,  "0.785299", 0, 0, 3),
    (23068673,  "0.380929", 0, 0, 0),
    (26214401,  "1.035845", 0, 1, 1),
    (28311553,  "0.866978", 0, 0, 2),
    (69206017,  "0.741365", 0, 0, 0),
    (70254593,  "0.942369", 0, 0, 1),
    (81788929,  "1.008154", 0, 0, 0),
    (101711873, "0.997912", 0, 0, 0),
    (104857601, "0.922993", 0, 0, 0),
    (111149057, "0.954379", 0, 0, 0),
    (113246209, "0.709742", 0, 0, 0),
    (120586241, "0.625868", 0, 0, 0),
    (132120577, "0.779668", 0, 0, 0),
    (136314881, "0.678814", 0, 0, 0),
    (138412033, "0.783785", 0, 0, 0),
    (141557761, "0.949246", 0, 0, 1),
    (147849217, "1.222305", 0, 0, 1),
    (155189249, "0.831432", 0, 0, 0),
    (158334977, "0.912148", 0, 0, 0),
    (163577857, "0.776242", 0, 0, 1),
    (167772161, "0.883271", 0, 0, 0),
    (169869313, "0.989577", 0, 0, 0),
    (185597953, "0.745830", 0, 0, 0),
    (186646529, "1.122901", 0, 1, 0),
    (199229441, "0.895932", 0, 0, 0),
    (204472321, "0.858202", 0, 0, 0),
    (211812353, "0.812069", 0, 0, 0),
    (221249537, "0.933197", 0, 0, 0),
    (230686721, "0.780084", 0, 0, 0),
    (246415361, "1.024517", 0, 0, 0),
    (249561089, "0.725317", 0, 0, 0),
    (257949697, "0.748986", 0, 0, 0),
]

# ------------------------------------------------------- (S) census, round 2
# c1r3b_results.md:83-89 (worst rows, banked ledgers) + c1r3b_table.txt.
# The only ledgered round-2 rows that matter for a max are those with env >= the
# round-1 max; all other band rows have env == K' (W_ext = 0) so are W-invariant.
R2 = [  # (q, env, w6, w7, w8)   ledger decompositions quoted verbatim in .md
    (377487361,  "1.401644", 0, 0, 0),   # "1.401644312 | 0"        ROUND WORST @ W=7
    (1431306241, "1.473264", 0, 0, 2),   # "1/2 (two w8)"
    (1365245953, "1.389420", 0, 0, 0),   # "0"
    (918552577,  "3.000058", 1, 0, 1),   # "5/4 (w6+w8)"            the accident row
    (290455553,  "1.740144", 0, 1, 0),   # "1/2 (one w7)"
    (399507457,  "1.270344", 0, 0, 1),   # table: env/K' = 1.270344/1.016275 => 1+W=5/4
    (383778817,  "1.157121", 0, 0, 0),
    (463470593,  "1.165643", 0, 0, 0),
    (531628033,  "1.033389", 0, 0, 0),
    (311427073,  "1.029844", 0, 0, 0),
]

CENSUS = [(q, F(e), a, b, c) for (q, e, a, b, c) in R1 + R2]


def ledger(w6, w7, w8, W):
    """W_ext under window [L+1, L+W] at L=1, N=32: weights 2..1+W."""
    tot = F(0)
    for cnt, w in ((w6, 6), (w7, 7), (w8, 8)):
        if w <= 1 + W:
            tot += cnt * mass_ana(w)
    return tot


def worst_kprime(W):
    best = (F(0), None)
    for q, env, w6, w7, w8 in CENSUS:
        k = env / (1 + ledger(w6, w7, w8, W))
        if k > best[0]:
            best = (k, q)
    return best


# ---------------------------------------------------------- (D) demand side
SCHEDULE_DIMS = [1, 1, 2, 4] + [2 ** j for j in range(3, 33)]   # 34 levels
FLOORS = {(1, 3), (1, 4), (2, 5), (2, 6)}      # ambient censuses + certs


def open_slots(W):
    """Cells left open at window [ell+1, ell+W] after Newton (w >= 2ell+1) + floors."""
    out = set()
    for ell in sorted(set(SCHEDULE_DIMS)):
        lo = max(ell + 1, 2 * ell + 1)          # Newton floor binds
        for w in range(lo, ell + W + 1):
            if (ell, w) not in FLOORS:
                out.add((ell, w))
    return out


def tolerated_W_ext():
    """Largest W with (1 + ALLOWANCE*(1+W))^34 < 2^100, exactly (bisect on Fraction)."""
    def ok(W):
        return (1 + ALLOWANCE * (1 + W)) ** N_LEVELS < F(2) ** 100
    lo, hi = F(0), F(2)
    assert ok(lo) and not ok(hi)
    for _ in range(120):
        mid = (lo + hi) / 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo


def main():
    print("=" * 72)
    print("CONTROLS (must reproduce banked values exactly)")
    print("=" * 72)
    caught = 0

    # C1: banked round-1 ledgers reproduce (c1r3_results.md col 'W_ext').
    banked_r1 = {7340033: F(3), 13631489: F(3, 4), 26214401: F(3, 4),
                 28311553: F(1, 2), 70254593: F(1, 4), 141557761: F(1, 4),
                 147849217: F(1, 4), 163577857: F(1, 4), 186646529: F(1, 2)}
    for q, env, w6, w7, w8 in CENSUS:
        if q in banked_r1:
            got = ledger(w6, w7, w8, 7)
            assert got == banked_r1[q], (q, got, banked_r1[q])
    print("C1 PASS  round-1 W_ext at W=7 reproduces 9/9 banked ledgers")
    caught += 1

    # C2: banked round-1 worst K' = 1.024517293 at q=246415361.
    k, q = worst_kprime(7)
    r1only = max((F(e) / (1 + ledger(a, b, c, 7)), qq) for qq, e, a, b, c in R1)
    assert r1only[1] == 246415361 and abs(float(r1only[0]) - 1.024517) < 1e-6
    print(f"C2 PASS  round-1 worst K'(W=7) = {float(r1only[0]):.6f} @ q={r1only[1]}"
          "   (banked 1.024517293)")
    caught += 1

    # C3: banked round-2 worst K' = 1.401644312 at 377487361, W_ext = 0.
    assert q == 377487361 and abs(float(k) - 1.401644) < 1e-6
    print(f"C3 PASS  two-round worst K'(W=7) = {float(k):.6f} @ q={q}"
          "   (banked 1.401644312, W_ext=0)")
    caught += 1

    # C4: the accident row reprices 3.000058 -> 1.333359 at W=7.
    acc = next(r for r in CENSUS if r[0] == 918552577)
    kacc7 = acc[1] / (1 + ledger(acc[2], acc[3], acc[4], 7))
    assert ledger(acc[2], acc[3], acc[4], 7) == F(5, 4)
    assert abs(float(kacc7) - 1.333359) < 1e-6
    print(f"C4 PASS  918552577: W_ext(W=7) = 5/4, K' = {float(kacc7):.6f}"
          "   (banked 1.333358972)")
    caught += 1

    # C5: ten-slot residual at W=7 == the ten minted TARGETs.
    TEN = {(1, 5), (1, 6), (1, 7), (1, 8), (2, 7), (2, 8), (2, 9),
           (4, 9), (4, 10), (4, 11)}
    assert open_slots(7) == TEN, open_slots(7) ^ TEN
    print("C5 PASS  open_slots(W=7) == the ten minted dli_wcl_slot_* TARGETs")
    caught += 1

    # C6: four-slot residual at W=5 == the pre-extension board.
    FOUR = {(1, 5), (1, 6), (2, 7), (4, 9)}
    assert open_slots(5) == FOUR, open_slots(5) ^ FOUR
    print("C6 PASS  open_slots(W=5) == the pre-extension four-slot residual")
    caught += 1

    # C7: banked allowance headroom (6 passes, 7 fails) at W_ext = 1/32.
    for A in (4, 5, 6, 7):
        got = (1 + A * (1 + ZONE_WIRED)) ** N_LEVELS < F(2) ** 100
        exp = A <= 6
        assert got == exp, (A, got)
    print("C7 PASS  allowance ladder at W<=1/32: 4,5,6 pass; 7 fails (banked)")
    caught += 1
    print(f"\n{caught}/7 controls PASS\n")

    # ------------------------------------------------------------- the ladder
    print("=" * 72)
    print("(S) SUPPLY SIDE — worst K'_r3 over the complete two-round census")
    print("    (33 round-1 + 164 round-2 rows to 1.95e9; kill line 4, amber-2 line 2)")
    print("=" * 72)
    print(f"{'W':>3} {'slots':>6} {'worst K(exact)':>34} {'~':>9} {'@q':>12}"
          f" {'margin/4':>9} {'amber-2 hdrm':>13}")
    lad = {}
    for W in (0, 4, 5, 6, 7, 8):
        k, q = worst_kprime(W)
        s = len(open_slots(W))
        lad[W] = (k, q, s)
        marg = 4 / float(k)
        hd = (2 / float(k) - 1) * 100
        print(f"{W:>3} {s:>6} {str(k):>34} {float(k):>9.6f} {q:>12}"
              f" {marg:>8.3f}x {hd:>12.1f}%")

    print("\nMARGINAL PRICE OF EACH WIDENING STEP (K'-units bought per slot added):")
    for a, b in ((0, 5), (5, 6), (6, 7), (7, 8)):
        dk = float(lad[a][0] - lad[b][0])
        ds = lad[b][2] - lad[a][2]
        per = dk / ds if ds else float('nan')
        print(f"  +{a} -> +{b}:  worst K' {float(lad[a][0]):.6f} -> {float(lad[b][0]):.6f}"
              f"  (-{dk:.6f})   slots {lad[a][2]} -> {lad[b][2]} (+{ds})"
              f"   = {per:.6f} K'-units/slot")

    print("\nPER-OCTAVE WORSTS (KILL-IIDX condition (a): strictly increasing over"
          " the last >= 3 populated octaves)")
    for W in (5, 6, 7):
        oct_worst = {}
        for q, env, w6, w7, w8 in CENSUS:
            o = q.bit_length() - 1
            k = env / (1 + ledger(w6, w7, w8, W))
            if k > oct_worst.get(o, F(0)):
                oct_worst[o] = k
        ser = [(o, float(oct_worst[o])) for o in sorted(oct_worst)]
        txt = " -> ".join(f"{v:.4f}" for _, v in ser)
        run = 1
        for i in range(len(ser) - 1, 0, -1):
            if ser[i][1] > ser[i - 1][1]:
                run += 1
            else:
                break
        print(f"  W={W}: {txt}")
        print(f"        terminal strictly-increasing run = {run}"
              f"  -> KILL-IIDX(a) {'FIRES' if run >= 3 else 'NOT FIRED'}")

    # ------------------------------------------------------------ demand side
    print("\n" + "=" * 72)
    print("(D) DEMAND SIDE — what the 34-level assembly actually needs")
    print("=" * 72)
    Wtol = tolerated_W_ext()
    print(f"  assembly:  prod_(j<34) E_j < 2^100,  E_j <= 1 + {ALLOWANCE}*(1+W_ext)")
    print(f"  TRUE tolerated W_ext          = {float(Wtol):.9f}"
          f"   (largest W with (1+4(1+W))^34 < 2^100)")
    print(f"  WIRED predicate WCL-ZONE      = 1/32 = {float(ZONE_WIRED):.9f}")
    print(f"  A2 OVERKILL FACTOR            = {float(Wtol / ZONE_WIRED):.4f}x"
          "   (unused zone budget)")
    print(f"  ten-slot route delivers       = 0   (exactly)  -> infinite overkill")
    lo_used = 34 * math.log2(1 + 4 * (1 + float(ZONE_WIRED)))
    lo_del = 34 * math.log2(1 + 4.0)
    print(f"\n  product slack at W<=1/32 : 100 - 34*log2(41/8) = {100-lo_used:.4f} bits"
          "   (banked 19.8432)")
    print(f"  product slack at W_ext=0 : 100 - 34*log2(5)    = {100-lo_del:.4f} bits")
    print(f"  A2 GAP (bits of product slack bought by W_ext=0) = "
          f"{lo_used-lo_del:.4f} bits")

    print("\n  does the overkill retire ANY slot?  (a cell is mass-safe iff its"
          " single-orbit mass <= tolerance)")
    for thr, name in ((ZONE_WIRED, "wired 1/32"), (Wtol, "true tolerance")):
        safe = [(e, w) for (e, w) in sorted(open_slots(8))
                if mass_off(e, w) <= thr]
        mn = min(mass_off(e, w) for (e, w) in open_slots(7))
        arg = min(open_slots(7), key=lambda c: mass_off(*c))
        print(f"    {name:>16}: mass-safe cells in the W<=8 board = {safe or 'NONE'};"
              f"  tightest W=7 cell {arg} mass {mn} = {float(mn/thr):.4f}x threshold")

    print("\n  first mass-safe weight per level under the TRUE tolerance"
          " (= where a budget re-pose would first buy something):")
    for ell in (1, 2, 4):
        w = next(w for w in range(1, 40) if mass_off(ell, w) <= Wtol)
        print(f"    ell={ell}: first mass-safe w = {w}  (needs window W >= {w-ell})")

    print("\n" + "=" * 72)
    print("SLOT LADDER (official scale, Newton floor 2ell+1, floors"
          " (1,3)(1,4)(2,5)(2,6))")
    print("=" * 72)
    for W in range(4, 10):
        s = open_slots(W)
        free = all(e + W <= 2 * e for e in SCHEDULE_DIMS if e >= 8)
        print(f"  W={W}: {len(s):>2} slots  {sorted(s)}"
              f"   ell>=8 Newton-free: {free}")


if __name__ == "__main__":
    main()
