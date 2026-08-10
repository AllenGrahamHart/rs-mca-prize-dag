#!/usr/bin/env python3
"""D2 - THE GRADED LADDER at h = 64 (N' = 128).   One shard, checkpointed.

usage:  tools/ramguard local -- python3 .../lad.py SEED FAM

Streams measured per sampled w (registered R2):
  GATEHIST[g]      : v_2(Norm(w) - 1)                      -- free, every sample
  SMALLBAD[v]      : incidences of prime factors p < 2^17, p = 1 mod 128,
                     counted by v_2(p-1)  (the HIGH-STATISTICS test of
                     conditional-badness independence, V1, at the real h)
  V2HIST[v]        : v_2(p-1) for accepted admissible-window prime hits
  V2HIST12[v]      : ditto restricted to the brief's COFAC <= 2^12
  COF256[c%256]    : cofactor residue of hits (tests the c = 129 mod 256 law)
Witnesses with v_2(p-1) >= 20 are stored in full.
"""
import json
import os
import random
import sys
import time

sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K  # noqa: E402

H, ORDER = 64, 128
SOFT = float(os.environ.get("LAD_SOFT", "235"))
SEED = int(sys.argv[1])
FAM = sys.argv[2] if len(sys.argv) > 2 else "B"
OUT = "notes/pilots_20260809/large_v2_hunt/state/lad_%s_%d.json" % (FAM, SEED)

# primes = 1 mod 128 below B_TD, and their product (cheap gcd instrument)
PB = [p for p in K.SMALL_PRIMES if p % ORDER == 1]
PBPROD = 1
for p in PB:
    PBPROD *= p
PBV2 = {p: ((p - 1) & -(p - 1)).bit_length() - 1 for p in PB}

GEN = {"B": lambda r: K.fam_B(H, r),
       "C3": lambda r: K.fam_C(H, r, 3),
       "C5": lambda r: K.fam_C(H, r, 5),
       "A": lambda r: K.fam_A(H, r)}[FAM]

st = {"seed": SEED, "fam": FAM, "n": 0, "hits": 0, "hits12": 0,
      "gate": {}, "small": {}, "v2": {}, "v212": {}, "cof256": {},
      "cof1": 0, "best": []}
if os.path.exists(OUT):
    st = json.load(open(OUT))
rng = random.Random(SEED * 1000003 + st["n"])


def v2(n):
    return (n & -n).bit_length() - 1


def bump(d, k):
    k = str(k)
    d[k] = d.get(k, 0) + 1


t0 = time.time()
while time.time() - t0 < SOFT:
    for _ in range(300):
        w = GEN(rng)
        n = K.tower_norm(w)
        if n == 0:
            continue
        n = abs(n)
        if n % 2 == 0:
            continue
        st["n"] += 1
        bump(st["gate"], v2(n - 1))
        g = K.gcd(n, PBPROD) if hasattr(K, "gcd") else __import__("math").gcd(n, PBPROD)
        if g > 1:
            for p in PB:
                if g % p == 0:
                    bump(st["small"], PBV2[p])
                    g //= p
                    if g == 1:
                        break
        rough, _fac = K.strip_small(n)
        if rough <= K.W_ADM_LO or rough > K.CEIL253 or rough % ORDER != 1:
            continue
        if not K.is_probable_prime(rough):
            continue
        cof = n // rough
        v = v2(rough - 1)
        st["hits"] += 1
        bump(st["v2"], v)
        bump(st["cof256"], cof % 256)
        if cof == 1:
            st["cof1"] += 1
        if cof <= 4096:
            st["hits12"] += 1
            bump(st["v212"], v)
        if v >= 20:
            st["best"].append({"w": w, "p": str(rough), "v2": v,
                               "pbits": rough.bit_length(),
                               "nbits": n.bit_length(), "cof": str(cof)})

st["best"].sort(key=lambda r: -r["v2"])
st["best"] = st["best"][:80]
tmp = OUT + ".tmp"
json.dump(st, open(tmp, "w"))
os.replace(tmp, OUT)
print("%s/%d n=%d hits=%d (%.4f) hits12=%d cof1=%d maxv2=%s"
      % (FAM, SEED, st["n"], st["hits"], st["hits"] / max(1, st["n"]),
         st["hits12"], st["cof1"],
         max((int(k) for k in st["v2"]), default=None)))
