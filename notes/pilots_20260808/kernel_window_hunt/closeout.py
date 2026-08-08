#!/usr/bin/env python3
"""Closeout: FAM-A baseline at h=64, the registered FAM-F lift probe, and the
total coverage accounting across every run in state/."""
import glob
import itertools
import json
import random
import sys
import time
sys.path.insert(0, "notes/pilots_20260808/kernel_window_hunt")
import klib as K

H, ORDER = 64, 128

# ---------------------------------------------------- FAM-A baseline at h=64
rng = random.Random(65537)
t0 = time.time()
bits, hits, odd = [], 0, 0
while time.time() - t0 < 60:
    for _ in range(300):
        w = K.fam_A(H, rng)
        n = K.tower_norm(w)
        if n == 0:
            continue
        n = abs(n)
        bits.append(n.bit_length())
        if n % 2:
            odd += 1
        rough, _ = K.strip_small(n)
        if (rough > K.W_ADM_LO and rough <= K.CEIL253 and rough % ORDER == 1
                and K.is_probable_prime(rough)):
            hits += 1
m = sum(bits) / len(bits)
v = sum((b - m) ** 2 for b in bits) / len(bits)
print("FAM-A h=64: %d samples, LOGNORM mean %.2f sd %.2f max %d; odd-norm frac %.3f"
      % (len(bits), m, v ** 0.5, max(bits), odd / len(bits)))
print("FAM-A BANDFRAC(244) = %.5f ; W_ADM hit rate = %.4f"
      % (sum(1 for b in bits if b >= 244) / len(bits), hits / len(bits)))

# ------------------------------------------- FAM-F: the h=8 maximiser lift
best, bw = 0, None
for u in itertools.product((-2, -1, 0, 1, 2), repeat=8):
    n = abs(K.tower_norm(list(u)))
    if n % 2 and n > best:
        best, bw = n, u
print("\nFAM-F: h=8 max ODD norm %d at u=%s (S=%d, nodd=%d)"
      % (best, bw, K.sq(list(bw)), K.nodd(list(bw))))
lift = [0] * 64
for i, t in enumerate(bw):
    lift[8 * i] = t
nl = abs(K.tower_norm(lift))
print("FAM-F lift w(x)=u(x^8): Norm = %d^8 ? %s ; log2 = %.1f (largest possible"
      " prime factor <= 2^%.1f)"
      % (best, nl == best ** 8, nl.bit_length() - 1, (best.bit_length() - 1)))
print("   -> as registered, USELESS for the window: a perfect 8th power.")
# tiling lift with odd-parity repair
til = list(bw) * 8
til[0] = 1 if til[0] % 2 == 0 else til[0]
nt = abs(K.tower_norm(til))
print("FAM-F tiling lift (parity-repaired): log2|Norm| = %.1f, odd = %s"
      % (nt.bit_length() - 1, nt % 2 == 1))

# ------------------------------------------------------ coverage accounting
cov = {}
for f in sorted(glob.glob("notes/pilots_20260808/kernel_window_hunt/state/*.json")):
    st = json.load(open(f))
    name = f.split("/")[-1]
    if "probe64" in name:
        cov[name] = ("FAM-B h=64 samples", st["n"], st.get("adm", 0))
    elif "probe256" in name:
        cov[name] = ("FAM-S h=128 samples", st["n"], len(st.get("hits", [])))
    elif "v2hunt" in name:
        cov[name] = ("FAM-B h=64 samples", st["n"], st.get("hits", 0))
    elif "proofhunt" in name:
        cov[name] = ("FAM-B h=64 samples", st["n"], st.get("hits", 0))
    elif "climb64" in name:
        cov[name] = ("FAM-D/E in-band distinct norms", st.get("processed", 0),
                     len(st.get("hits", [])))
    elif "climbproof" in name:
        cov[name] = ("FAM-D/E in-band vectors", st.get("inband", 0), st.get("top", 0))
tot_s = {}
tot_h = {}
for k, (lab, n, h) in cov.items():
    tot_s[lab] = tot_s.get(lab, 0) + n
    tot_h[lab] = tot_h.get(lab, 0) + h
print("\nCOVERAGE (distinct box vectors / norms fully processed):")
for lab in tot_s:
    print("   %-34s %10d   accepted %d" % (lab, tot_s[lab], tot_h[lab]))
print("   %-34s %10d" % ("GRAND TOTAL norms processed", sum(tot_s.values())))
print("   box size 5^64 = 2^148.6, so coverage = 2^%.1f of the box"
      % (sum(tot_s.values()).bit_length() - 1))
