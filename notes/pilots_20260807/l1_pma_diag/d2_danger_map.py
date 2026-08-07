#!/usr/bin/env python3
"""D2/D3: the floor-band BOX as a function of petal size ell -- the danger map.

Hand derivation (then machine-checked against the N10 census at ell=2):

Maximal-source chart family (pma_arbitrary_petal_source_realizability,
statement.md:9-28 + H5): L = n points, core C with |C| = k-1, petals
T_1..T_t of size ell, background B with |B| = b < ell, and
    t = floor((n-k+1)/ell),   b = (n-k+1) - t*ell.
At rate 1/2 (n = 2k) this is t*ell + b = k+1.

Floor band (petal_growth/proof.md:8-13, catch #168): core defect
d = |C \\ S| >= ell(t-2), i.e. a := |C n S| <= A_max := |C| - ell(t-2).
Agreement: |S| >= k+1, i.e. omitted petal points
om <= a + b' + t*ell - k - 1, maximised at
    OM_max = A_max + b + t*ell - k - 1 = k - ell(t-2) - 1.

Substituting t*ell = k+1-b and |C| = k-1 gives the identity
    A_max = OM_max = 2*ell + b - 2 =: Lambda            (the BAND SLACK)
so the number of floor-band supports is
    BOX(ell) = sum_{a<=Lambda, b'<=b, om<=a+b'+t*ell-k-1}
               C(k-1,a) C(b,b') C(t*ell, om)  =  Theta(n^{2*Lambda}).
Exponent 2*Lambda = 4*ell + 2*b - 4.  At ell=2, b=1: n^6.
"""
from math import comb, log2

BANKED_BOX = {16: 5096, 32: 386640, 64: 27152032}


def chart(n, ell):
    k = n // 2
    t = (n - k + 1) // ell
    b = (n - k + 1) - t * ell
    C = k - 1
    assert C + t * ell + b == n, (C, t, ell, b, n)
    return k, C, t, b


def box(n, ell, mixed_only=False):
    """Exact count of floor-band supports with agreement >= k+1."""
    k, C, t, b = chart(n, ell)
    band = ell * (t - 2)
    A_max = C - band
    if A_max < 0:
        return 0, 0, 0
    total = 0
    for a in range(0, A_max + 1):
        for bp in range(0, b + 1):
            om_max = a + bp + t * ell - k - 1
            for om in range(0, min(t * ell, om_max) + 1):
                if mixed_only and om == 0:
                    continue
                total += comb(C, a) * comb(b, bp) * comb(t * ell, om)
    return total, A_max, k - band - 1


print("=" * 78)
print("CHECK: does the derived box formula reproduce the N10 census box?")
print("=" * 78)
print("(N10 additionally requires om >= 1 AND some petal met in exactly 1 pt;")
print(" the derived BOX is the superset -- it must DOMINATE, and match in order)")
for n in (16, 32, 64):
    tot, A_max, Lam = box(n, 2)
    tot_m, _, _ = box(n, 2, mixed_only=True)
    k, C, t, b = chart(n, 2)
    print(f"n={n:3d}: ell=2 t={t:2d} b={b} |C|={C:2d}  Lambda = 2*ell+b-2 = "
          f"{2*2+b-2} (derived) vs A_max={A_max}, OM_max={Lam} (computed)")
    print(f"        BOX = {tot:,}   BOX(om>=1) = {tot_m:,}   "
          f"N10 candidates = {BANKED_BOX[n]:,}   "
          f"ratio N10/BOX = {BANKED_BOX[n]/tot:.3f}")

print()
print("=" * 78)
print("THE DANGER MAP: floor-band box exponent vs petal size ell (rate 1/2)")
print("=" * 78)
print(f"{'ell':>4} {'t':>6} {'b':>3} {'Lambda':>7} {'pred exp':>9} "
      f"{'log_n BOX n=2^10':>17} {'log_n BOX n=2^14':>17}")
for ell in (2, 3, 4, 5, 6, 8, 12, 16):
    rows = []
    for e in (10, 14):
        n = 2 ** e
        tot, A_max, _ = box(n, ell)
        rows.append(log2(tot) / e if tot else float("nan"))
    k, C, t, b = chart(2 ** 14, ell)
    lam = 2 * ell + b - 2
    print(f"{ell:>4} {t:>6} {b:>3} {lam:>7} {4*ell+2*b-4:>9} "
          f"{rows[0]:>17.3f} {rows[1]:>17.3f}")

print()
print("=" * 78)
print("GROWING ell: where the box stops being polynomial")
print("=" * 78)
print("official-row scale n = 2^41, k = 2^40; ell grows with n:")
n = 2 ** 41
k = n // 2
for name, ell in (("ell = 2 (the N10 census)", 2),
                  ("ell = log2 n", 41),
                  ("ell = sqrt(n)", 2 ** 20),
                  ("ell = n / log2(n)^2", n // (41 * 41)),
                  ("ell = n / log2(n)^2  [rich-fiber fence]", n // (41 * 41))):
    kk, C, t, b = chart(n, ell)
    if t < 3:
        print(f"   {name:42s}: t = {t} < 3, band vacuous")
        continue
    lam = 2 * ell + b - 2
    # log2 of the dominant binomial C(k-1, Lambda)*C(t*ell, Lambda)
    lg = 0.0
    for i in range(1, min(lam, 60) + 1):
        lg += log2((C - i + 1) / i) + log2((t * ell - i + 1) / i)
    tag = "poly" if lam <= 8 else "SUPER-POLYNOMIAL"
    print(f"   {name:42s}: ell={ell:,} t={t:,} Lambda={lam:,} "
          f"exponent 2*Lambda={2*lam:,} -> {tag}")
print()
print("The banked structural fence petal_reserve_rich_fiber_reduction says a")
print("counterexample needs an Omega(n/log^2 n) source-coupled value fiber in")
print("ONE petal -- i.e. ell = Omega(n/log^2 n).  That is exactly the row where")
print("Lambda = 2*ell+b-2 is Omega(n/log^2 n) and the box exponent 2*Lambda is")
print("super-polynomial.  The N10 census sits at ell = 2, Lambda = 3.")
