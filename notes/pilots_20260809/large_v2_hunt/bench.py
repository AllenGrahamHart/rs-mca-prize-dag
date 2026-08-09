#!/usr/bin/env python3
"""Throughput benchmark: how many h=64 box norms per second, and what the
gate (v_2(Norm-1) >= 8) costs vs the full strip_small+BPSW pipeline."""
import random
import sys
import time
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K  # noqa: E402

H = 64
rng = random.Random(20260809)

for name, gen in (("FAM-B", lambda: K.fam_B(H, rng)),
                  ("FAM-C3", lambda: K.fam_C(H, rng, 3)),
                  ("FAM-A", lambda: K.fam_A(H, rng))):
    ws = [gen() for _ in range(400)]
    t = time.time()
    ns = [abs(K.tower_norm(w)) for w in ws]
    dt = time.time() - t
    odd = sum(1 for n in ns if n % 2)
    law = sum(1 for n in ns if n % 2 and n % 128 == 1)
    bits = sorted(n.bit_length() for n in ns if n % 2)
    print("%-7s norm rate %7.0f/s   odd %3d/400  NORMLAW(=1 mod 128) %3d/%d"
          % (name, len(ws) / dt, odd, law, odd), end="")
    if bits:
        print("   LOGNORM med %d  max %d" % (bits[len(bits) // 2], bits[-1]))
    else:
        print()

ws = [K.fam_B(H, rng) for _ in range(200)]
ns = [abs(K.tower_norm(w)) for w in ws]
t = time.time()
for n in ns:
    K.strip_small(n)
print("strip_small rate  %7.0f/s" % (len(ns) / (time.time() - t)))
t = time.time()
for n in ns:
    K.is_probable_prime(n)
print("BPSW rate         %7.0f/s" % (len(ns) / (time.time() - t)))
t = time.time()
for n in ns:
    ((n - 1) & -(n - 1)).bit_length()
print("gate rate         %7.0f/s" % (len(ns) / (time.time() - t)))
