#!/usr/bin/env python3
"""Consequence of NORMLAW: a FAM-B witness prime has p = 129 mod 256 unless the
cofactor absorbs the 128.  v2(p-1) >= t therefore costs 2^-(t-7).  This hunt
maximises v2(p-1) so the witness sits on the largest smooth domain n = 2^v2
we can actually reach.  Same process() core."""
import json
import os
import random
import sys
import time
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K

H, ORDER = 64, 128
SOFT = 230.0
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 20260808
OUT = "notes/pilots_20260808/kernel_window_hunt/state/v2hunt_%d.json" % SEED

rng = random.Random(SEED)
st = {"seed": SEED, "n": 0, "hits": 0, "best": [], "v2hist": {}}
if os.path.exists(OUT):
    st = json.load(open(OUT))
    rng = random.Random(SEED * 31 + st["n"])

t0 = time.time()
while time.time() - t0 < SOFT:
    for _ in range(400):
        w = K.fam_B(H, rng)
        n = K.tower_norm(w)
        if n == 0:
            continue
        n = abs(n)
        st["n"] += 1
        rough, fac = K.strip_small(n)
        if rough <= K.W_ADM_LO or rough > K.CEIL253 or rough % ORDER != 1:
            continue
        if not K.is_probable_prime(rough):
            continue
        st["hits"] += 1
        v2 = ((rough - 1) & -(rough - 1)).bit_length() - 1
        st["v2hist"][str(v2)] = st["v2hist"].get(str(v2), 0) + 1
        if v2 >= 14:
            st["best"].append({"w": w, "p": str(rough), "v2": v2,
                               "pbits": rough.bit_length(),
                               "nbits": n.bit_length(), "cof": str(n // rough)})

st["best"].sort(key=lambda r: -r["v2"])
st["best"] = st["best"][:60]
json.dump(st, open(OUT, "w"))
print("seed %d: samples %d, admissible-window hits %d (%.4f)"
      % (SEED, st["n"], st["hits"], st["hits"] / st["n"]))
print("v2(p-1) histogram:", dict(sorted((int(k), v) for k, v in st["v2hist"].items())))
for r in st["best"][:5]:
    print("BEST v2=%d pbits=%d nbits=%d cof=%s" %
          (r["v2"], r["pbits"], r["nbits"], r["cof"]))
