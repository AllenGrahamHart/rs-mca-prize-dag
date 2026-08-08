#!/usr/bin/env python3
"""h=64 (N'=128) probe: measured LOGNORM distribution + window scan.
Same process() core as the h=8 calibration.  Checkpointed, soft wall 230 s."""
import json
import os
import random
import sys
import time
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K
from hunt import process

H, ORDER = 64, 128
SOFT = 230.0
FAM = sys.argv[1] if len(sys.argv) > 1 else "B"
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 20260808
OUT = "notes/pilots_20260808/kernel_window_hunt/state/probe64_%s_%d.json" % (FAM, SEED)

BANDS = [230, 235, 240, 244, 248, 252, 255]
rng = random.Random(SEED)
st = {"fam": FAM, "seed": SEED, "n": 0, "bits": {}, "hits": [],
      "rough_prime": 0, "adm": 0, "dep": 0, "top": 0}
if os.path.exists(OUT):
    st = json.load(open(OUT))
    rng = random.Random(SEED + st["n"])

t0 = time.time()
mk = {"A": K.fam_A, "B": K.fam_B, "C": K.fam_C}[FAM]
while time.time() - t0 < SOFT:
    for _ in range(500):
        w = mk(H, rng)
        n = K.tower_norm(w)
        if n == 0:
            continue
        n = abs(n)
        b = n.bit_length()
        st["bits"][str(b)] = st["bits"].get(str(b), 0) + 1
        st["n"] += 1
        rough, fac = K.strip_small(n)
        if rough > 1 and K.is_probable_prime(rough):
            st["rough_prime"] += 1
            if rough % ORDER == 1 and rough <= K.CEIL253:
                if rough > K.W_ADM_LO:
                    st["adm"] += 1
                    rec = {"w": w, "p": str(rough), "pbits": rough.bit_length(),
                           "nbits": b, "cof": str(n // rough)}
                    if rough >= K.W_TOP_LO:
                        st["top"] += 1
                        st["hits"].append(rec)
                    elif rough >= K.W_DEP_LO:
                        st["dep"] += 1
                        if len([x for x in st["hits"] if x["pbits"] < 244]) < 40:
                            st["hits"].append(rec)

json.dump(st, open(OUT, "w"))
tot = st["n"]
print("FAM-%s seed %d: samples %d in %.0fs" % (FAM, SEED, tot, time.time() - t0))
bl = sorted((int(k), v) for k, v in st["bits"].items())
mean = sum(k * v for k, v in bl) / tot
var = sum((k - mean) ** 2 * v for k, v in bl) / tot
print("LOGNORM mean %.2f sd %.2f min %d max %d" % (mean, var ** 0.5, bl[0][0], bl[-1][0]))
for t in BANDS:
    c = sum(v for k, v in bl if k >= t)
    print("BANDFRAC(%d) = %d/%d = %.5f" % (t, c, tot, c / tot))
print("rough-part-prime %d (%.4f), W_ADM %d, W_DEP %d, W_TOP %d"
      % (st["rough_prime"], st["rough_prime"] / tot, st["adm"], st["dep"], st["top"]))
for rec in st["hits"][:6]:
    print("HIT pbits=%d nbits=%d cof=%s p=%s" %
          (rec["pbits"], rec["nbits"], rec["cof"], rec["p"]))
