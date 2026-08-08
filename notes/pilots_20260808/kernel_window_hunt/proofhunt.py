#!/usr/bin/env python3
"""Same FAM-B sampling law (PREREG P3); additional recorded functional
PM1FRAC(p) = log2(factored part of p-1 from primes < 10^5)/log2 p.
Keeps witnesses whose p-1 is factored enough for a Brillhart-Lehmer-Selfridge
PROOF (needs F > p^(1/3))."""
import json
import os
import random
import sys
import time
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K

H, ORDER, SOFT = 64, 128, 230.0
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 1
OUT = "notes/pilots_20260808/kernel_window_hunt/state/proofhunt_%d.json" % SEED
TD = [q for q in K.SMALL_PRIMES if q < 10 ** 5]

rng = random.Random(SEED)
st = {"seed": SEED, "n": 0, "hits": 0, "best": 0.0, "rec": None, "top": []}
if os.path.exists(OUT):
    st = json.load(open(OUT))
    rng = random.Random(SEED * 97 + st["n"])

t0 = time.time()
while time.time() - t0 < SOFT:
    for _ in range(300):
        w = K.fam_B(H, rng)
        n = K.tower_norm(w)
        if n == 0:
            continue
        n = abs(n)
        st["n"] += 1
        rough, _ = K.strip_small(n)
        if rough <= K.W_ADM_LO or rough > K.CEIL253 or rough % ORDER != 1:
            continue
        if not K.is_probable_prime(rough):
            continue
        st["hits"] += 1
        m = rough - 1
        F = 1
        for q in TD:
            if m % q == 0:
                while m % q == 0:
                    m //= q
                    F *= q
        frac = (F.bit_length() - 1) / rough.bit_length()
        st["top"].append(round(frac, 4))
        if frac > st["best"]:
            st["best"] = frac
            st["rec"] = {"w": w, "p": str(rough), "frac": frac,
                         "pbits": rough.bit_length(), "F": str(F)}

st["top"] = sorted(st["top"])[-25:]
json.dump(st, open(OUT, "w"))
print("seed %d: samples %d, hits %d, best PM1FRAC %.4f (need > 0.3333)"
      % (SEED, st["n"], st["hits"], st["best"]))
print("top PM1FRAC values:", st["top"][-10:])
