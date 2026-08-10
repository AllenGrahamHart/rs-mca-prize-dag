"""k3_chain_seams exhibit (attack A4, quantifier narrowing): admissible
n = 2^41 rate-1/2 rows whose q is NOT prime.

Why: rate_half_band_crossing_location is the ONLY child of
rate_half_band_closure that owns the located crossing, and its pose of
record reads "n = 2^41, k = 2^40, q prime, q = 1 mod n, 2^167 < q < 2^256"
(statement.md:11-12, node.json statement). The repo's admissibility
descriptor (notes/BAND_LANE_DEFINITIONS.md item 13) is
"q = p^e, n = 2^s, k = rho*n under q < 2^256, k <= 2^40, n | q-1" — e is
NOT restricted to 1. The consumers quantify over "each admissible row"
(adjacency_closing/statement.md:9, mca_grand/statement.md:9).

This script exhibits explicit rows inside the parent's quantifier and
outside the child's pose: q = p^2 (so q is not prime), n = 2^41 | q-1,
k = 2^40, q < 2^256, including one inside the razor slice
(2^255.9 < q < 2^256) — the hard corner itself.

All range decisions are EXACT INTEGER comparisons. A first draft of this
script used math.log2 and silently reported log2 q = 256.0 for every
candidate (float rounds 2^256 - 2^170 to 2^256); that miss is recorded in
REPORT.md. The 2^255.9 threshold is the integer 10th root of 2^2559.

Stdlib only.
"""

_SPRP = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]


def is_probable_prime(n):
    if n < 2:
        return False
    for p in _SPRP:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in _SPRP:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def iroot(x, k):
    """floor(x**(1/k)) by integer Newton"""
    if x < 0:
        raise ValueError
    if x == 0:
        return 0
    hi = 1 << ((x.bit_length() + k - 1) // k + 1)
    lo = 0
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** k <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo


def v2(x):
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


T_2559 = None  # floor(2^255.9), set in main


def report(p, label, e=2):
    q = p ** e
    n = 1 << 41
    print("--- " + label)
    print("  p                    = %d" % p)
    print("  p prime (MR-20)      = %s" % is_probable_prime(p))
    print("  e                    = %d   (q = p^e, so q is NOT prime)" % e)
    print("  q bit_length         = %d" % q.bit_length())
    print("  n = 2^41 divides q-1 = %s   (v_2(q-1) = %d)" % ((q - 1) % n == 0, v2(q - 1)))
    print("  k = 2^40, rate 1/2, k <= 2^40 = True")
    print("  q < 2^256            = %s" % (q < (1 << 256)))
    print("  q > 2^167            = %s" % (q > (1 << 167)))
    print("  q > 2^255.9          = %s   [EXACT: vs floor(2^255.9)]" % (q > T_2559))
    print("  B* = floor(q/2^128)  = %d" % (q >> 128))
    print("  B* bit_length        = %d" % (q >> 128).bit_length())


def main():
    global T_2559
    T_2559 = iroot(1 << 2559, 10)          # floor(2^255.9), exact
    assert T_2559.bit_length() == 256
    print("floor(2^255.9) has bit_length %d" % T_2559.bit_length())
    print("floor(2^255.9) = %d" % T_2559)
    print()

    n = 1 << 41

    # EXHIBIT 1: q = p^2 ~ 2^200, comfortably inside the child's widened q-range
    c = (1 << 100) // n
    while True:
        p = c * n + 1
        if is_probable_prime(p):
            break
        c += 1
    report(p, "EXHIBIT 1: admissible n=2^41 rate-1/2 row, q = p^2, 2^167 < q < 2^256")
    print()

    # EXHIBIT 2: q = p^2 inside the RAZOR SLICE (2^255.9, 2^256)
    hi = (1 << 128) - 1
    c = hi // n
    found = None
    while c > 0:
        p = c * n + 1
        if p <= hi and is_probable_prime(p):
            q = p * p
            if T_2559 < q < (1 << 256):
                found = p
                break
        c -= 1
    if found is None:
        print("EXHIBIT 2: NOT FOUND in the scanned window -> ZERO-POWER for exhibit 2")
    else:
        report(found, "EXHIBIT 2: admissible RAZOR-SLICE row, q = p^2 in (2^255.9, 2^256)")
    print()

    # CONTROL: the KoalaBear K3 lane row is NOT an n = 2^41 row
    kb = 2130706433
    q6 = kb ** 6
    print("--- CONTROL: the K3 lane's KoalaBear row")
    print("  p                    = %d" % kb)
    print("  v_2(p-1)             = %d" % v2(kb - 1))
    print("  q = p^6 bit_length   = %d" % q6.bit_length())
    print("  v_2(q-1)             = %d" % v2(q6 - 1))
    print("  2^41 | q-1 ?         = %s   <- the KB row is NOT an n = 2^41 row" % (v2(q6 - 1) >= 41))
    print("  2^21 | q-1 ?         = %s   <- it IS an n = 2^21 row" % (v2(q6 - 1) >= 21))
    print("  B* = floor(q/2^128)  = %d (bit_length %d)" % (q6 >> 128, (q6 >> 128).bit_length()))
    print("  band_closure QUALITY.md gate 1 requires n=2^41,k=2^40,2^128<q<2^256,n|(q-1)")
    print("  -> KB row fails gate 1 on n (2^21) and on n|(q-1) at n=2^41.")

    # CONTROL 2: the KB adjacent-pair datum's row size, from U_paid = n - a
    a = 1116048
    u_paid = 981104
    print()
    print("--- CONTROL 2: KB deployed candidate arithmetic (attack_sections/00, lines 10-16)")
    print("  a = %d, U_paid = n - a = %d  ->  n = %d = 2^%d"
          % (a, u_paid, a + u_paid, (a + u_paid).bit_length() - 1))


if __name__ == "__main__":
    main()
