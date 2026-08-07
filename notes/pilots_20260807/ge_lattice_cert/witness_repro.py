#!/usr/bin/env python3
"""STANDALONE WITNESS REPRODUCTION (PREREG P6 step 3), exercised on the
PLANT-C control -- the only cell in this pilot that produced a witness.

Imports nothing from this pilot's library.  It regenerates the control's
lattice from the REGISTERED seed alone, then verifies the recovered vector
exactly.  If a real prize row had produced a witness, this is the shape the
report would have carried for it (with the pinned rho in place of the
co-cyclic functional).

Run:  tools/ramguard tiny -- python3 \
        notes/pilots_20260807/ge_lattice_cert/witness_repro.py
"""
import json
import os
import random

# background/nodes/e1_pocklington_250bit_exhibit_field/statement.md:11-12
P = 904625697166646869347790708689937759412227977745095982970820953353127723009
SEED = 20260807          # registered in PREREG.md P4 / runcell.py PLANT_SEED
H = 64

rnd = random.Random(SEED)
v = [rnd.randint(-2, 2) for _ in range(H)]
while not any(v):
    v = [rnd.randint(-2, 2) for _ in range(H)]
c = [1] + [rnd.randrange(P) for _ in range(H - 1)]
t = max(range(H), key=lambda j: (abs(v[j]), j))
rest = sum(v[j] * c[j] for j in range(H) if j != t)
c[t] = (-rest * pow(v[t], P - 2, P)) % P
if t == 0:
    inv = pow(c[0], P - 2, P)
    c = [(x * inv) % P for x in c]

print("== PLANT-C witness reproduction, from the registered seed alone ==")
print("   p          = %d" % P)
print("   seed       = %d ; pivot index t = %d ; c[0] = %d" % (SEED, t, c[0]))
print("   planted v  = %s" % v)
s = sum(v[j] * c[j] for j in range(H))
print("   sum_j v_j c_j mod p = %d          -> v IS in the lattice: %s"
      % (s % P, s % P == 0))
print("   ||v||_inf = %d (<= 2: %s) ; ||v||_1 = %d ; ||v||_2^2 = %d (<= R^2=256: %s)"
      % (max(abs(a) for a in v), max(abs(a) for a in v) <= 2,
         sum(abs(a) for a in v), sum(a * a for a in v),
         sum(a * a for a in v) <= 256))

cert = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "state", "PLANT-64.cert.json")
if os.path.exists(cert):
    d = json.load(open(cert))
    got = [tuple(w) for w in d["found"]]
    print("\n   enumeration reported %d witness(es), FPNODES = %d"
          % (len(got), d["nodes"]))
    print("   planted v recovered by the enumeration : %s"
          % (tuple(v) in got))
    print("   the other witness is -v                : %s"
          % (tuple(-a for a in v) in got))
    print("   every reported witness re-verified     : %s"
          % all(sum(w[j] * c[j] for j in range(H)) % P == 0 and
                max(abs(a) for a in w) <= 2 for w in got))
print("\n   => the fail-closed control is reproducible from the seed and the")
print("      literal prime, with no dependence on the pilot's library.")
