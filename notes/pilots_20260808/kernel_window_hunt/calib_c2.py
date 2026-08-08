#!/usr/bin/env python3
"""C2/C3/C4 — the SAMPLING pipeline at h=8 against the C1 exhaustive truth."""
import json
import math
import random
import sys
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K
from hunt import process, verify_hit

H, ORDER = 8, 16
GT = json.load(open("notes/pilots_20260808/kernel_window_hunt/state/c1_h8.json"))
BAD = set(GT["bad"])
BANDLO = int(2 ** 18.5620)
BANDHI = (4 * (H - 1) + 1) ** (H // 2)          # 29^4, the odd-case ceiling
TRUE_RATE = GT["band_vecs"] / GT["nvec"]
print("ground truth: band primes %s, per-vector rate %.4e"
      % (GT["band_primes"], TRUE_RATE))

FAIL = []


def ck(name, cond, extra=""):
    print(("PASS " if cond else "FAIL ") + name + ("  " + extra if extra else ""))
    if not cond:
        FAIL.append(name)


# ---- C2a  uniform FAM-A sampling, the identical process() core
rng = random.Random(20260808)
M = 200000
found, hits, nbits = {}, 0, []
for i in range(M):
    w = K.fam_A(H, rng)
    b, hs = process(w, ORDER, BANDLO, BANDHI)
    nbits.append(b)
    for p in hs:
        found[p] = found.get(p, 0) + 1
        hits += 1
rate = hits / M
exp = TRUE_RATE * M
lo = exp - 1.96 * math.sqrt(exp)
hi = exp + 1.96 * math.sqrt(exp)
print("C2a: samples %d, band hits %d (expected %.1f, 95%% [%.1f, %.1f]), primes %s"
      % (M, hits, exp, lo, hi, sorted(found)))
ck("C2a zero false positives (every reported prime is exhaustively bad)",
   all(p in BAD for p in found), str([p for p in found if p not in BAD]))
ck("C2a recall inside the Poisson 95%% interval", lo <= hits <= hi)
ck("C2a recovers the known top-band prime 463249", 463249 in found)
ck("C3 rate agreement within a factor of 2",
   0.5 * TRUE_RATE <= rate <= 2 * TRUE_RATE,
   "sampled %.4e vs exhaustive %.4e" % (rate, TRUE_RATE))

# ---- C2b  the FAM-B (odd-extremal) enrichment, same core
rng2 = random.Random(1729)
MB = 60000
hb, fb = 0, {}
for i in range(MB):
    w = K.fam_B(H, rng2)
    b, hs = process(w, ORDER, BANDLO, BANDHI)
    for p in hs:
        fb[p] = fb.get(p, 0) + 1
        hb += 1
print("C2b: FAM-B samples %d, band hits %d, rate %.4e (enrichment x%.1f), %s"
      % (MB, hb, hb / MB, (hb / MB) / rate if rate else float('nan'), sorted(fb)))
ck("C2b zero false positives", all(p in BAD for p in fb))

# ---- C4  planted fail-closed control
wit = None
for w in __import__("itertools").product((-2, -1, 0, 1, 2), repeat=H):
    if abs(K.tower_norm(list(w))) % 463249 == 0:
        wit = list(w)
        break
b, hs = process(wit, ORDER, BANDLO, BANDHI)
ck("C4 planted witness detected", 463249 in hs, "w=%s bits=%d" % (wit, b))
rep = verify_hit(wit, 463249, ORDER)
ck("C4 planted witness passes full verification", rep["ok"], str(rep))
# corrupted: same vector, wrong prime
rep2 = verify_hit(wit, 463247, ORDER)
ck("C4 corrupted prime rejected", not rep2["ok"])
# corrupted: zero vector
rep3 = verify_hit([0] * H, 463249, ORDER)
ck("C4 zero vector rejected", not rep3["ok"])

# ---- LOGNORM distribution at h=8 (for the model check)
nbits.sort()
mean = sum(nbits) / len(nbits)
var = sum((x - mean) ** 2 for x in nbits) / len(nbits)
print("h=8 FAM-A LOGNORM: mean %.2f sd %.2f max %d" % (mean, var ** 0.5, nbits[-1]))

print("CALIB %s (%d failures)" % ("PASS" if not FAIL else "FAIL", len(FAIL)))
