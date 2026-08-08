#!/usr/bin/env python3
"""D3 — N'=256 POSITIVE CONTROL at h=128, families FAM-S(s), s in {21,27,33,41}.
Same process() core.  Window: p = 1 mod 256, 2^128 < p < 2^256 (spec cap)."""
import json
import os
import random
import sys
import time
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K

H, ORDER = 128, 256
SOFT = 230.0
S = int(sys.argv[1]) if len(sys.argv) > 1 else 27
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 20260808
OUT = ("notes/pilots_20260808/kernel_window_hunt/state/probe256_s%d_%d.json"
       % (S, SEED))
CAP = 1 << 256

rng = random.Random(SEED)
st = {"s": S, "seed": SEED, "n": 0, "bits": {}, "hits": [], "rough_prime": 0}
if os.path.exists(OUT):
    st = json.load(open(OUT))
    rng = random.Random(SEED + st["n"])

t0 = time.time()
while time.time() - t0 < SOFT:
    for _ in range(200):
        w = K.fam_S(H, rng, S)
        n = K.tower_norm(w)
        if n == 0:
            continue
        n = abs(n)
        st["bits"][str(n.bit_length())] = st["bits"].get(str(n.bit_length()), 0) + 1
        st["n"] += 1
        rough, fac = K.strip_small(n)
        if rough > 1 and K.W_ADM_LO < rough < CAP and rough % ORDER == 1:
            if K.is_probable_prime(rough):
                st["rough_prime"] += 1
                st["hits"].append({"w": w, "p": str(rough),
                                   "pbits": rough.bit_length(),
                                   "nbits": n.bit_length(),
                                   "cof": str(n // rough)})

json.dump(st, open(OUT, "w"))
tot = st["n"]
bl = sorted((int(k), v) for k, v in st["bits"].items())
mean = sum(k * v for k, v in bl) / tot
var = sum((k - mean) ** 2 * v for k, v in bl) / tot
print("h=128 FAM-S(%d) seed %d: samples %d in %.0fs" % (S, SEED, tot, time.time() - t0))
print("LOGNORM mean %.2f sd %.2f min %d max %d  (predicted mean %.1f)"
      % (mean, var ** 0.5, bl[0][0], bl[-1][0], 64 * ((S).bit_length() - 1 - 0.8327)))
print("ADMISSIBLE-WINDOW HITS: %d  (rate %.4e)" % (len(st["hits"]), len(st["hits"]) / tot))
for rec in st["hits"][:5]:
    print("HIT pbits=%d nbits=%d cof=%s" % (rec["pbits"], rec["nbits"], rec["cof"]))
