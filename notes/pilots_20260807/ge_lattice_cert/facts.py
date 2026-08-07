#!/usr/bin/env python3
"""Exact arithmetic checks on every literal constant in the row list."""
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cells as C                                        # noqa: E402
import latlib as LL                                      # noqa: E402


def isprime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def v2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


HI = 253 ** 32
print("HIGH-FIELD THRESHOLD 253^32 = 2^%.4f  "
      "(integer_code_distance_high_field_folded_box_exclusion)"
      % math.log2(HI))
print("AM-GM CEILING (4h)^{h/2} at h=64 = 2^256 (rigorous, no witness above it)")
print()
print("%-14s %-9s %-6s %-7s %-9s %-11s %-9s"
      % ("cell", "log2 p", "prime", "v2(p-1)", "p=1mod128", "vs 253^32",
         "order-128 root"))


def show(tag, p):
    r = LL.zeta_of_order(128, p) if (p - 1) % 128 == 0 else None
    ok = r is not None and pow(r, 128, p) == 1 and pow(r, 64, p) == p - 1
    print("%-14s %-9.3f %-6s %-7d %-9s %-11s %-9s"
          % (tag, math.log2(p), isprime(p), v2(p - 1), (p - 1) % 128 == 0,
             "ABOVE (free)" if p > HI else "below", ok))


show("E1 p250", C.P250)
for c in C.EXTENSION:
    show(c["cid"], c["p"])
show("corridor q", C.QCORR)
print()

print("-- the pinned roots (e1_pocklington_250bit_exhibit_field:23-27) --")
p = C.P250
print("   rho_128 = 3^((p-1)/128) mod p ? %s ; exact order 128 ? %s"
      % (pow(3, (p - 1) // 128, p) == C.RHO128,
         pow(C.RHO128, 128, p) == 1 and pow(C.RHO128, 64, p) == p - 1))
print("   rho_256 = 3^((p-1)/256) mod p ? %s ; exact order 256 ? %s"
      % (pow(3, (p - 1) // 256, p) == C.RHO256,
         pow(C.RHO256, 256, p) == 1 and pow(C.RHO256, 128, p) == p - 1))
print("   p = 562949953421383 * 2^200 + 1 ? %s ; bitlen %d ; p < 2^256 ? %s"
      % (p == 562949953421383 * 2 ** 200 + 1, p.bit_length(), p < 2 ** 256))
print()

print("-- the four deployed Proth rows "
      "(mca_quadratic_prize_rows/statement.md:31-34) --")
for (r, n, pp, B) in C.PROTH:
    u = (pp - 1) >> v2(pp - 1)
    s = v2(pp - 1)
    print("   rate %-5s n=2^%-3d p = %d*2^%d+1  bitlen=%d  "
          "B=floor(p/2^128)=%d matches table: %s"
          % (r, int(math.log2(n)), u, s, pp.bit_length(),
             pp // 2 ** 128, pp // 2 ** 128 == B))
    print("        bits below 253^32: %.2f" % (math.log2(HI) - math.log2(pp)))
print()

print("-- the corridor literal prime "
      "(corridor_ledger/verify_corridor_literal_prime.py:22-26) --")
q = C.QCORR
P_AUX = 309485010219174763933204481
S_MULT = 158747337183671499011314909792715251078
print("   q = 2^41 * P_AUX * S_MULT + 1 ? %s"
      % (q == 2 ** 41 * P_AUX * S_MULT + 1))
print("   bitlen %d ; q = 1 mod 1024 ? %s ; q > 253^32 ? %s "
      "-> already FREE by the proved high-field branch"
      % (q.bit_length(), (q - 1) % 1024 == 0, q > HI))
print()

print("-- BOXCOUNT sanity: 5^h and the l1-restricted counts --")
for (h, L) in [(64, 128), (128, 256), (128, 130), (128, 66), (256, 66)]:
    bc = LL.boxcount(h, L)
    full = 5 ** h
    print("   h=%-4d 2l'=%-4d BOXCOUNT = 2^%-9.3f   (5^h = 2^%-9.3f, "
          "fraction 2^%.2f)"
          % (h, L, math.log2(bc), math.log2(full),
             math.log2(bc) - math.log2(full)))
