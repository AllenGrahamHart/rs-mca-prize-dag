#!/usr/bin/env python3
"""C1: the registered closed form (PREREG R1) + the cell cost map.

Emits, for every declared cell (PREREG R0.4):
  Lambda, t, b, the shell profile N_{k+r}, BOX = sum_r N_{k+r},
  RETPRED (the random-word law), and the predicted RATIOBOX / RATIOSHELL.

Nothing here touches a received word: BOX and N_{k+r} are pure
combinatorics of (n, ell) and are therefore layout-independent.
"""
from math import comb

Q = 97


def cells(n, ell):
    k = n // 2
    t = (n - k + 1) // ell
    b = (n - k + 1) - t * ell
    C = k - 1
    assert C + t * ell + b == n
    return k, t, b, C, 2 * ell + b - 2


def shells(n, ell, mixed=True, band=True, a_cap=None):
    """PREREG R1 closed form.  Returns {r: N_{k+r}}."""
    k, t, b, C, Lam = cells(n, ell)
    tl = t * ell
    cap = C if a_cap is None else a_cap
    if band:
        cap = min(cap, Lam)
    N = {}
    om_lo = 1 if mixed else 0
    for a in range(0, cap + 1):
        for nb in range(0, b + 1):
            hi = min(tl, a + nb - b)
            for om in range(om_lo, hi + 1):
                if mixed:
                    m = comb(tl, om)
                    if om % ell == 0:
                        m -= comb(t, om // ell)
                else:
                    m = comb(tl, om)
                if m <= 0:
                    continue
                r = a + nb - b - om + 1
                N[r] = N.get(r, 0) + comb(C, a) * comb(b, nb) * m
    return N


def retpred(n, N, q=Q):
    k = n // 2
    return sum(v * q ** (-r) * (1 - 1.0 / q) ** (n - k - r)
               for r, v in N.items())


if __name__ == "__main__":
    GRID = [(16, [2, 3]), (24, [2, 3, 4, 5, 6]), (32, [2, 3, 4, 5, 6, 8])]

    print("=" * 96)
    print("C1  registered closed form (PREREG R1) over the declared grid, q = 97")
    print("=" * 96)
    print(f"{'n':>3} {'ell':>4} {'t':>3} {'b':>3} {'Lam':>4} {'|C|':>4} {'t*ell':>6} "
          f"{'BOX':>16} {'N_k+1':>16} {'RETPRED':>12} {'BOX/q':>12} "
          f"{'RATIOBOX':>9} {'band':>7}")
    ALL = {}
    for n, ells in GRID:
        for ell in ells:
            k, t, b, C, Lam = cells(n, ell)
            if t < 1 or b >= ell:
                print(f"{n:>3} {ell:>4}  --- illegal chart (b={b} >= ell={ell}) ---")
                continue
            N = shells(n, ell)
            box = sum(N.values())
            rp = retpred(n, N)
            ALL[(n, ell)] = (N, box, rp)
            print(f"{n:>3} {ell:>4} {t:>3} {b:>3} {Lam:>4} {C:>4} {t*ell:>6} "
                  f"{box:>16,} {N.get(1,0):>16,} {rp:>12.2f} {box/Q:>12.1f} "
                  f"{rp/(box/Q):>9.4f} {'VACUOUS' if t < 3 else 'proper':>7}")

    print()
    print("=" * 96)
    print("C2  shell profile N_{k+r} (the reason RATIOBOX must fall in ell)")
    print("=" * 96)
    for (n, ell), (N, box, rp) in sorted(ALL.items()):
        prof = "  ".join(f"r={r}:{N[r]:,}" for r in sorted(N)[:6])
        print(f"n={n:>3} ell={ell}: N_k+1/BOX = {N.get(1,0)/box:.5f}   {prof}"
              + ("  ..." if len(N) > 6 else ""))

    print()
    print("=" * 96)
    print("C3  cost map: matmul flops ~ BOX*t*ell, filter survivors ~ sum_r N/q^r")
    print("=" * 96)
    print(f"{'n':>3} {'ell':>4} {'BOX':>16} {'flops/word':>14} {'s0 surv':>12} "
          f"{'all-r surv':>12} {'verdict':>28}")
    for (n, ell), (N, box, rp) in sorted(ALL.items()):
        k, t, b, C, Lam = cells(n, ell)
        tl = t * ell
        s0 = box / Q
        allr = sum(v * Q ** (-r) for r, v in N.items())
        fl = box * tl
        if box <= 6e8:
            v = "LOCAL (ramguard local)"
        elif box <= 5e9:
            v = "MODAL (spec it)"
        else:
            v = "MODAL, large"
        print(f"{n:>3} {ell:>4} {box:>16,} {fl:>14.3e} {s0:>12,.0f} "
              f"{allr:>12,.1f} {v:>28}")

    print()
    print("=" * 96)
    print("C4  the UNRESTRICTED mixed family (no floor band) -- the P4 scope test")
    print("=" * 96)
    for n, ell in ((16, 2), (16, 3), (24, 2), (24, 3), (32, 2)):
        k, t, b, C, Lam = cells(n, ell)
        Nb = shells(n, ell, band=True)
        Nf = shells(n, ell, band=False)
        print(f"n={n} ell={ell}: floor-band BOX {sum(Nb.values()):,}  "
              f"UNRESTRICTED mixed BOX {sum(Nf.values()):,}  "
              f"(ratio {sum(Nf.values())/sum(Nb.values()):.1f}x)  "
              f"max r in band {max(Nb)} = Lambda={Lam}?{max(Nb)==Lam}  "
              f"max r unrestricted {max(Nf)}")
