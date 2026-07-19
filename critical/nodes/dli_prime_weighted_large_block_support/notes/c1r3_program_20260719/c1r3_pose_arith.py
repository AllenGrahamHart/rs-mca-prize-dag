# c1r3 pose-instantiation arithmetic (exact integers only; sanctioned by the
# mandate: "the downstream-assembly consequence ... with explicit arithmetic").
import math
a = 41**34
b = 2**202
print("41^34 =", a)
print("2^202 =", b)
print("41^34 < 2^202 :", a < b)
print("slack bits = log2(2^202/41^34) = %.4f" % (202 - math.log2(a)))
# allowance headroom: largest integer-friendly allowance A with (1+A*33/32)^34 < 2^100
for A in (4, 5, 6, 7):
    lhs_num = (32 + 33*A)**34          # (1 + 33A/32)^34 < 2^100  <=>  (32+33A)^34 < 32^34 * 2^100
    lhs_ok = lhs_num < 32**34 * 2**100
    print(f"allowance {A}: (1+{A}*33/32)^34 < 2^100 : {lhs_ok}")
# killer-row v_2 facts (from the kill record; re-verified as PC2 in-round)
for q in (63361, 65921, 204353):
    v = (q-1); k = 0
    while v % 2 == 0: v //= 2; k += 1
    print(f"v_2({q}-1) = {k}")
# Newton emptiness of the extended window at scheduled levels: L+7 <= 2L iff L>=7
print("extended window Newton-empty for scheduled ell >= 8:", all(l+7 <= 2*l for l in (8, 16, 32)))
