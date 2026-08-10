#!/usr/bin/env python3
"""D2 - is the measured K = 0.73 a property of BAD PRIMES or of the ACCEPTANCE
RULE?  LAW 2 pins v_2(Norm-1) = 7 on FAM-B, so every COFACTOR-1 acceptance is
FORCED to v_2(p-1) = 7.  Split the ladder by cofactor and find out."""
import random
import sys
from collections import Counter
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K  # noqa: E402

H, ORDER = 64, 128
rng = random.Random(4242)
c1 = Counter()
cg = Counter()
n = 0
import time
t0 = time.time()
while time.time() - t0 < 200:
    for _ in range(200):
        w = K.fam_B(H, rng)
        m = K.tower_norm(w)
        if m == 0:
            continue
        m = abs(m)
        if m % 2 == 0:
            continue
        n += 1
        rough, _f = K.strip_small(m)
        if rough <= K.W_ADM_LO or rough > K.CEIL253 or rough % ORDER != 1:
            continue
        if not K.is_probable_prime(rough):
            continue
        v = ((rough - 1) & -(rough - 1)).bit_length() - 1
        (c1 if m // rough == 1 else cg)[v] += 1


def show(name, c):
    t = sum(c.values())
    if not t:
        return
    print("\n%s  (%d hits)" % (name, t))
    print("  v   count   P(>=v)     K = P(>=v)*2^(v-7)")
    s = 0
    tl = {}
    for v in sorted(c, reverse=True):
        s += c[v]
        tl[v] = s
    for v in sorted(c):
        if tl[v] < 8:
            break
        print("%3d %7d   %.5f     %.4f" % (v, c[v], tl[v] / t, tl[v] / t * 2 ** (v - 7)))


print("FAM-B, %d odd-norm samples" % n)
show("COFACTOR = 1  (LAW 2 forces v_2(p-1) = v_2(Norm-1) = 7)", c1)
show("COFACTOR > 1  (v_2(p-1) unconstrained)", cg)
tot = Counter(c1) + Counter(cg)
show("POOLED (what the ladder reports)", tot)
print("\ncofactor-1 share of hits: %.4f" % (sum(c1.values()) /
                                           max(1, sum(tot.values()))))
