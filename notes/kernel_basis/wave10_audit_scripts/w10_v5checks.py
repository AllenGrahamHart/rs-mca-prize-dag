import math
from math import comb, isqrt
n = 1 << 41; k = 1 << 40
# new cyclic floor instantiation c=2^33, N=256, d=1, s=c-1
c = 1 << 33; N = n // c; assert N == 256
d = 1; s = c - 1; m = N // 2 + d; assert m == 129
assert k % c == 0 and 0 < s < c and 1 <= d <= N // 2 - 1
excess = d * c + s
assert excess == (1 << 34) - 1 == 17_179_869_183
L = -(-comb(N - 1, m) // N)  # ceil, d=1 => q-free
assert L > 1 << 238, math.log2(L)
print("list_bits=%.3f" % math.log2(L), "excess=2^34-1 OK; field-independent (d=1)")
# margin vs max budget B* < 2^128
assert L > 1 << 128
# old vs new reach
print("reach doubled:", 17_179_869_183 / 8_594_128_895)
# MCA conversion at the new list: E = L(q-n)/(q(q-n+kL)) > 2^-128 for all n<q<2^256?
for qb in (129, 167, 200, 256):
    q = (1 << qb) + 1  # generic
    E_num = L * (q - n); E_den = q * (q - n + k * L)
    assert E_num * (1 << 128) > E_den, qb   # E > 2^-128
    # also E > 2^-41-ish
    assert E_num * (1 << 42) > E_den, qb
print("pole conversion E>2^-128 (and >2^-42) at q~2^{129,167,200,256} OK")
# integer Johnson anchor at B=1,2,3 exact at 3n/4; fails at 3n/4-1 (B=1)
def johnson_pass(B, a):
    ell = B + 1; t = ell * a; dd, r = divmod(t, n)
    return n * comb(dd, 2) + r * dd > comb(ell, 2) * (k - 1)
a34 = 3 * n // 4
assert johnson_pass(1, a34) and not johnson_pass(1, a34 - 1)
assert johnson_pass(2, a34) and not johnson_pass(2, a34 - 1)
assert johnson_pass(3, a34) and not johnson_pass(3, a34 - 1)
print("a_IJ = 3n/4 exact for B=1,2,3 (two-sided) OK")
# unbounded-list threshold constant: B* >= 332114441762 => a_IJ = floor(sqrt(n(k-1)))+1
aj = isqrt(n * (k - 1)) + 1
B_big = 332_114_441_762
assert johnson_pass(B_big, aj)
assert not johnson_pass(B_big - 1, aj), "threshold not tight below"
print("sqrt anchor a_IJ =", aj, "tight at B*=332114441762 OK")
# feasibility slack for the unsafe pair construction at 3n/4-1 (B=1)
assert 2 * (a34 - 1) <= n + (k - 1)
print("W10_V5_CHECKS_PASS")
