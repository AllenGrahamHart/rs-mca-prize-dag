#!/usr/bin/env python3
"""D2 TURBO - the FREE high-rung ladder test.

KEY IDENTITY (new here).  If N = Norm(w) = c*p with p = 1 mod 2^L and the
cofactor c < 2^L, then N = c mod 2^L, so c is DETERMINED: c = N mod 2^L.
Hence the whole rung-L test costs one mask and one divisibility check:

      r := N mod 2^L ;   hit-candidate iff r >= 1, r | N, and p := N/r
      lands in the admissible window.   Then p = 1 mod 2^L by construction.

No trial division and no primality test on the 99.999...% of samples that
fail, so a rung-L probe costs only the tower norm.  Rungs are the brief's
ladder L in {8,12,16,24,32,41} (CATCH-Z6: powers of two where mine to
choose; no rung at the trivial baseline 7, CATCH-19B).

Every SUBSAMPLE-th sample also runs the full round-24 pipeline so the
v_2(p-1) histogram keeps accumulating in the same run.

usage: tools/ramguard local -- python3 turbo.py SEED FAM
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
SUB = int(os.environ.get("TURBO_SUB", "4"))
SEED = int(sys.argv[1])
FAM = sys.argv[2] if len(sys.argv) > 2 else "B"
OUT = "notes/pilots_20260809/large_v2_hunt/state/turbo_%s_%d.json" % (FAM, SEED)
RUNGS = (8, 12, 16, 24, 32, 41)

GEN = {"B": lambda r: K.fam_B(H, r),
       "C3": lambda r: K.fam_C(H, r, 3),
       "C5": lambda r: K.fam_C(H, r, 5),
       "A": lambda r: K.fam_A(H, r)}[FAM]

from math import gcd  # noqa: E402
PB = [p for p in K.SMALL_PRIMES if p % ORDER == 1]
PBPROD = 1
for p in PB:
    PBPROD *= p

st = {"seed": SEED, "fam": FAM, "n": 0, "nsub": 0, "hits": 0,
      "rung": {}, "rungwin": {}, "rungprime": {}, "cofhist": {},
      "v2": {}, "v212": {}, "cof1": 0, "best": [], "wit": [], "smallp": {}}
if os.path.exists(OUT):
    st = json.load(open(OUT))
rng = random.Random(SEED * 1000003 + 7 + st["n"])


def v2(n):
    return (n & -n).bit_length() - 1


def bump(d, k, m=1):
    k = str(k)
    d[k] = d.get(k, 0) + m


MASK = {L: (1 << L) - 1 for L in RUNGS}
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
        # PER-PRIME control channel: every p = 1 mod 128 below B_TD dividing N.
        # The null is n * (1 - (1-1/p)^64); testing whether the RATIO depends
        # on v_2(p-1) is the V1 test at the real h (no model of the null needed
        # beyond the per-prime one).
        gg = gcd(n, PBPROD)
        if gg > 1:
            for p in PB:
                if gg % p == 0:
                    bump(st["smallp"], p)
                    gg //= p
                    if gg == 1:
                        break
        for L in RUNGS:
            r = n & MASK[L]
            if r == 0 or n % r:
                continue
            bump(st["rung"], L)                       # divisor congruence met
            p = n // r
            if p <= K.W_ADM_LO or p > K.CEIL253:
                continue
            bump(st["rungwin"], L)                    # ... and p in W_ADM
            bump(st["cofhist"], "%d:%d" % (L, r.bit_length()))
            if not K.is_probable_prime(p):
                continue
            bump(st["rungprime"], L)                  # ... and p PRIME
            st["wit"].append({"L": L, "w": w, "p": str(p), "cof": str(r),
                              "v2": v2(p - 1), "pbits": p.bit_length()})
        # ---- subsampled full pipeline: keeps the v_2(p-1) histogram growing
        if st["n"] % SUB == 0:
            st["nsub"] += 1
            rough, _f = K.strip_small(n)
            if rough <= K.W_ADM_LO or rough > K.CEIL253 or rough % ORDER != 1:
                continue
            if not K.is_probable_prime(rough):
                continue
            cof = n // rough
            v = v2(rough - 1)
            st["hits"] += 1
            bump(st["v2"], v)
            if cof == 1:
                st["cof1"] += 1
            if cof <= 4096:
                bump(st["v212"], v)
            if v >= 22:
                st["best"].append({"w": w, "p": str(rough), "v2": v,
                                   "pbits": rough.bit_length(),
                                   "cof": str(cof)})

st["best"].sort(key=lambda r: -r["v2"])
st["best"] = st["best"][:60]
st["wit"] = sorted(st["wit"], key=lambda r: -r["L"])[:60]
tmp = OUT + ".tmp"
json.dump(st, open(tmp, "w"))
os.replace(tmp, OUT)
print("%s/%d n=%d nsub=%d hits=%d rung=%s win=%s prime=%s maxv2=%s"
      % (FAM, SEED, st["n"], st["nsub"], st["hits"],
         {int(k): v for k, v in sorted(st["rung"].items(), key=lambda t: int(t[0]))},
         {int(k): v for k, v in sorted(st["rungwin"].items(), key=lambda t: int(t[0]))},
         {int(k): v for k, v in sorted(st["rungprime"].items(), key=lambda t: int(t[0]))},
         max((int(k) for k in st["v2"]), default=None)))
