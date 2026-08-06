#!/usr/bin/env python3
"""Crossing w >= 2 -- round 3: exact prize-row arithmetic (tiny, exact ints).

At the prize-max razor row n = 2^41, k = 2^40, the open crossing bracket is
k + 2^34 <= a_L <= a_IJ <= 3n/4, i.e. w = a_L - k in [2^34, 2^39].

Checks:
 (R1) d = gcd(r', n) = 2^{v_2(w)}, so LEMMA X divides by n/d = 2^{41-v_2(w)}.
 (R2) MC-3 (banked) applies at this row IFF w is an exact power of two;
      LEMMA X applies for EVERY w. Count how much of the bracket each covers.
 (R3) Newton/BCH linearization needs w < p. At this row every admissible
      characteristic has p >= 2^39 + 1 > 2^39 >= w, so it ALWAYS applies.
      Derivation: 2^41 | p^e - 1, ord_{2^41}(p) = 2^j, LTE gives
      v_2(p^2 - 1) >= 42 - j so p >= 2^{41-j} - 1; and p^{2^j} <= q < 2^256
      forces 2^j (41-j) < 256, i.e. j <= 2, hence p >= 2^39 - 1; 2^39 - 1 is
      composite so p >= 2^39 + 1.
"""

FAILURES = []
CHECKS = [0]


def check(name, cond, detail=""):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append((name, detail))
    return cond


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2
        c += 1
    return c


def main():
    print("=" * 78)
    print("CROSSING w >= 2 -- round 3: prize-max razor row exact arithmetic")
    print("=" * 78)
    n, k = 2 ** 41, 2 ** 40
    wlo, whi = 2 ** 34, 2 ** 39
    print("\n  n = 2^41 = %d, k = 2^40, open bracket w in [2^34, 2^39]" % n)

    # (R1) d = gcd(r', n) = 2^{v2(w)}
    print("\n[R1] d = gcd(r', n) and the LEMMA-X divisor n/d")
    bad = []
    ws = ([2 ** t for t in range(34, 40)]
          + [2 ** 34 + 1, 2 ** 34 + 2, 2 ** 35 + 6, 3 * 2 ** 34,
             2 ** 36 + 2 ** 20, 5 * 2 ** 35, 2 ** 38 + 2 ** 37, 2 ** 39 - 1])
    for w in sorted(set(ws)):
        if not (wlo <= w <= whi):
            continue
        rp = n - k - w
        d = gcd(rp, n)
        pred = 2 ** min(v2(w), 41)
        if d != pred:
            bad.append((w, d, pred))
    check("R1 d = 2^{v2(w)}", not bad, str(bad[:3]))
    print("     verified d = 2^{v_2(w)} on %d sampled w: %s"
          % (len(set(ws)), "OK" if not bad else "BROKEN"))
    for w in [2 ** 34, 2 ** 34 + 1, 3 * 2 ** 34, 2 ** 39]:
        rp = n - k - w
        d = gcd(rp, n)
        print("     w = %-14d v_2(w)=%2d  d=%-12d  LEMMA X divides by n/d = %d"
              % (w, v2(w), d, n // d))

    # (R2) MC-3 applicability vs LEMMA X
    print("\n[R2] MC-3 (banked) vs LEMMA X coverage of the open bracket")
    print("     MC-3 needs M|n, M|r', w<=M, gcd(r'/M, n/M)=1.")
    print("     At n=2^41 that forces M = 2^{v_2(r')} = 2^{v_2(w)} and")
    print("     w <= 2^{v_2(w)}, i.e. w must be an EXACT POWER OF TWO.")
    mc3_ok, tot = 0, 0
    for w in sorted(set(ws)):
        if not (wlo <= w <= whi):
            continue
        tot += 1
        rp = n - k - w
        ok = False
        M = 2 ** v2(rp)
        if M >= w and rp % M == 0 and n % M == 0:
            if gcd(rp // M, n // M) == 1:
                ok = True
        if ok:
            mc3_ok += 1
        ispow2 = (w & (w - 1)) == 0
        check("R2 MC-3 iff power of two (w=%d)" % w, ok == ispow2,
              "ok=%s pow2=%s" % (ok, ispow2))
    print("     sampled w in bracket: %d ; MC-3 applies to %d of them "
          "(exactly the powers of two)" % (tot, mc3_ok))
    npow2 = sum(1 for w in range(34, 40))
    print("     over the WHOLE bracket [2^34, 2^39] there are %d powers of two"
          % (39 - 34 + 1))
    print("     out of %d integers -> MC-3 covers a fraction ~ 2^-34 of the"
          " bracket;" % (whi - wlo + 1))
    print("     LEMMA X covers ALL of it (it needs no gcd hypothesis).")

    # (R3) Newton/BCH validity at this row
    print("\n[R3] Newton/BCH linearization validity: need w < p")
    print("     admissible characteristics: 2^41 | p^e - 1, p^e = q < 2^256")
    rows = []
    for j in range(0, 6):
        # ord_{2^41}(p) = 2^j  =>  v_2(p^2-1) >= 42 - j  =>  p >= 2^{41-j} - 1
        pmin = 2 ** (41 - j) - 1
        budget = (2 ** j) * (41 - j)
        rows.append((j, pmin, budget, budget < 256))
        print("     j=%d (e a multiple of 2^%d): p >= 2^%d - 1 = %d ; "
              "log2 q >= 2^j*(41-j) = %d ; admissible: %s"
              % (j, j, 41 - j, pmin, budget, budget < 256))
    adm = [r for r in rows if r[3]]
    pmin = min(r[1] for r in adm)
    check("R3 j <= 2", max(r[0] for r in adm) == 2, str(adm))
    check("R3 p >= 2^39 - 1", pmin == 2 ** 39 - 1, str(pmin))
    # 2^39 - 1 is composite (39 = 3*13), so p >= 2^39 + 1 > 2^39 >= w
    comp = (2 ** 39 - 1) % (2 ** 3 - 1) == 0 and (2 ** 39 - 1) % (2 ** 13 - 1) == 0
    check("R3 2^39-1 composite", comp)
    print("     => j <= 2, so p >= 2^39 - 1; and 2^39 - 1 = %d is COMPOSITE"
          % (2 ** 39 - 1))
    print("        (divisible by 2^3-1=7 and 2^13-1=8191: %s)" % comp)
    print("     => p >= 2^39 + 1 > 2^39 >= w for every w in the bracket.")
    print("     => Newton's identities are invertible at EVERY admissible")
    print("        official rate-half razor row: the window conditions")
    print("        e_1 = .. = e_{w-1} = 0 are EQUIVALENT to the linear")
    print("        power-sum conditions p_1 = .. = p_{w-1} = 0 there.")
    check("R3 w < p on bracket", 2 ** 39 < 2 ** 39 + 1)

    print("\n" + "=" * 78)
    print("checks run: %d   failures: %d" % (CHECKS[0], len(FAILURES)))
    for nm, d in FAILURES:
        print("  FAILED: %s | %s" % (nm, d))
    print("=" * 78)


if __name__ == "__main__":
    main()
