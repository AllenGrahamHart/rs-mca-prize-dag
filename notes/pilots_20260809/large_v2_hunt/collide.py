#!/usr/bin/env python3
"""COLLISION AUDIT - the denominator of the CSTAR count.

At h = 8 the naive estimator #bad = INCIDENCE / (2h^2) over-predicts by 7.1x
because 390624 box vectors carry only 1450 distinct norms.  At h = 64 the
same estimator is only safe if distinct sampled vectors carry distinct norms.
Measured here: COLLFRAC = 1 - (#distinct |Norm|)/(#sampled), and the same for
the admissible primes actually accepted.
"""
import random
import sys
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K  # noqa: E402

H, ORDER = 64, 128
rng = random.Random(31337)
for fam, gen in (("FAM-B", lambda: K.fam_B(H, rng)),
                 ("FAM-A", lambda: K.fam_A(H, rng))):
    norms, primes = [], []
    N = 12000
    for _ in range(N):
        w = gen()
        n = K.tower_norm(w)
        if n == 0:
            continue
        n = abs(n)
        if n % 2:
            norms.append(n)
    for n in norms[:4000]:
        rough, _ = K.strip_small(n)
        if K.W_ADM_LO < rough <= K.CEIL253 and rough % ORDER == 1 \
                and K.is_probable_prime(rough):
            primes.append(rough)
    print("%s: odd-norm samples %d, distinct |Norm| %d (COLLFRAC %.2e); "
          "admissible primes %d, distinct %d"
          % (fam, len(norms), len(set(norms)),
             1 - len(set(norms)) / len(norms), len(primes), len(set(primes))))

# h = 8 control: the measured degeneracy that breaks the estimator at the toy
import itertools
sys.path.insert(0, "notes/pilots_20260807/ge_floor_falsifier")
from gelib import tower_norm as tn8  # noqa: E402
ns = [abs(tn8(list(w))) for w in itertools.product((-2, -1, 0, 1, 2), repeat=8)]
ns = [n for n in ns if n]
print("h=8 control: %d nonzero norms, %d distinct -> %.1f vectors per norm "
      "(orbit 2h^2 = 128)" % (len(ns), len(set(ns)), len(ns) / len(set(ns))))
