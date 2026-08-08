#!/usr/bin/env python3
"""FAM-D / FAM-E: threshold climb into W_TOP at h=64, then level-set walk.
Every in-band vector is run through the SAME process() core.  Checkpointed."""
import json
import os
import random
import sys
import time
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K

H, ORDER = 64, 128
SOFT = 230.0
T = int(sys.argv[1]) if len(sys.argv) > 1 else 244
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 20260808
OUT = "notes/pilots_20260808/kernel_window_hunt/state/climb64_T%d_%d.json" % (T, SEED)

rng = random.Random(SEED)
st = {"T": T, "seed": SEED, "climbs": 0, "reached": 0, "inband": 0,
      "processed": 0, "hits": [], "gains": [], "norms_seen": 0,
      "distinct": 0, "maxbits": 0}
seen = set()
if os.path.exists(OUT):
    st = json.load(open(OUT))
    rng = random.Random(SEED * 7919 + st["processed"])

t0 = time.time()
while time.time() - t0 < SOFT:
    w0 = K.fam_B(H, rng)
    w, cur, start, evals = K.climb(w0, rng, T, max_evals=6000)
    st["climbs"] += 1
    st["gains"].append(cur.bit_length() - start.bit_length())
    st["maxbits"] = max(st["maxbits"], cur.bit_length())
    if cur.bit_length() < T:
        continue
    st["reached"] += 1
    # FAM-E level-set walk around the climbed vector
    base = list(w)
    for step in range(400):
        if time.time() - t0 > SOFT:
            break
        v = list(base)
        j = rng.randrange(H)
        v[j] = -v[j]
        if step % 3 == 2:                      # occasional 2-flip
            v[rng.randrange(H)] *= -1
        n = abs(K.tower_norm(v))
        if n.bit_length() < T:
            continue
        st["inband"] += 1
        if n in seen:
            continue
        seen.add(n)
        st["processed"] += 1
        rough, fac = K.strip_small(n)
        if rough > 1 and rough >= K.W_TOP_LO and rough <= K.CEIL253 \
                and rough % ORDER == 1 and K.is_probable_prime(rough):
            st["hits"].append({"w": v, "p": str(rough), "pbits": rough.bit_length(),
                               "nbits": n.bit_length(), "cof": str(n // rough)})
            print("W_TOP HIT pbits=%d nbits=%d cof=%s" %
                  (rough.bit_length(), n.bit_length(), n // rough))
        if rng.random() < 0.35:
            base = v                            # random-walk the base

st["distinct"] = len(seen)
json.dump(st, open(OUT, "w"))
g = st["gains"]
print("climbs %d, reached T=%d: %d (%.3f), in-band vectors %d, distinct norms %d"
      % (st["climbs"], T, st["reached"], st["reached"] / max(1, st["climbs"]),
         st["inband"], st["processed"]))
print("CLIMBGAIN mean %.2f max %d ; maxbits reached %d ; ceiling log2(253^32)=255.45"
      % (sum(g) / max(1, len(g)), max(g) if g else 0, st["maxbits"]))
print("W_TOP HITS: %d" % len(st["hits"]))
for r in st["hits"][:5]:
    print("  pbits=%d nbits=%d cof=%s" % (r["pbits"], r["nbits"], r["cof"]))
