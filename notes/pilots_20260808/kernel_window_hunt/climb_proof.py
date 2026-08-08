#!/usr/bin/env python3
"""FAM-D/FAM-E climb into W_TOP, keeping only witnesses whose prime admits a
BLS n-1 PROOF.  Target: a PROVEN prime witness at ~2^250, the scale of the
E1-128 exhibit field."""
import json
import os
import random
import sys
import time
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K
from bls import bls_prove, factor_part

H, ORDER, SOFT, T = 64, 128, 230.0, 244
SEED = int(sys.argv[1]) if len(sys.argv) > 1 else 1
OUT = "notes/pilots_20260808/kernel_window_hunt/state/climbproof_%d.json" % SEED

rng = random.Random(SEED)
st = {"seed": SEED, "inband": 0, "top": 0, "tried": 0, "proven": [], "bestfrac": 0.0}
if os.path.exists(OUT):
    st = json.load(open(OUT))
    rng = random.Random(SEED * 131 + st["inband"])

t0 = time.time()
seen = set()
while time.time() - t0 < SOFT:
    w0 = K.fam_B(H, rng)
    w, cur, start, ev = K.climb(w0, rng, T, max_evals=6000)
    if cur.bit_length() < T:
        continue
    base = list(w)
    for _ in range(600):
        if time.time() - t0 > SOFT:
            break
        v = list(base)
        v[rng.randrange(H)] *= -1
        n = abs(K.tower_norm(v))
        if n.bit_length() < T or n in seen:
            continue
        seen.add(n)
        st["inband"] += 1
        rough, _ = K.strip_small(n)
        if rough < K.W_TOP_LO or rough > K.CEIL253 or rough % ORDER != 1:
            if rng.random() < 0.35:
                base = v
            continue
        if not K.is_probable_prime(rough):
            if rng.random() < 0.35:
                base = v
            continue
        st["top"] += 1
        F, R, fac = factor_part(rough - 1)
        frac = (F.bit_length() - 1) / rough.bit_length()
        st["bestfrac"] = max(st["bestfrac"], frac)
        if frac <= 0.3334:
            if rng.random() < 0.35:
                base = v
            continue
        st["tried"] += 1
        ok, cert = bls_prove(rough)
        if ok:
            st["proven"].append({"w": v, "p": str(rough),
                                 "pbits": rough.bit_length(),
                                 "nbits": n.bit_length(),
                                 "cof": str(n // rough), "frac": frac})
            print("PROVEN W_TOP WITNESS pbits=%d frac=%.3f branch=%s"
                  % (rough.bit_length(), frac, cert["branch"]))
        if rng.random() < 0.35:
            base = v

json.dump(st, open(OUT, "w"))
print("seed %d: in-band %d, W_TOP PRP %d, BLS attempts %d, PROVEN %d, best frac %.4f"
      % (SEED, st["inband"], st["top"], st["tried"], len(st["proven"]), st["bestfrac"]))
