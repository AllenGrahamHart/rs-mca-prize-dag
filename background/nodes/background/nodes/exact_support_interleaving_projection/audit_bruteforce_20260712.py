#!/usr/bin/env python3
"""w3 audit: independent brute-force of exact_support_interleaving_projection
(ESP), which codex's verify.py never brute-forced (arithmetic-only).

Model: C = RS[F_5, mu_4, 2] (deg<2 on the order-4 subgroup {1,2,4,3} of F_5*),
n=4, q=5, m=2. EXHAUSTIVE over all 5^4 x 5^4 = 390,625 interleaved words and
ALL 2^(2^4) support-properties is too many; we take: P_aper (trivial dyadic
stabilizer), P_all, and 200 random properties. For each property and each
agreement a in {2,3,4} (r=2,1,0 < q):
    L_P     = max over 625 words of #{c: |S_exact| >= a, S_exact in P}
    L_{2,P} = max over 390,625 word-pairs of #{(c1,c2): |S1&S2|>=a, S1&S2 in P}
Check: L_P=0 => L_{2,P}=0 ; else if D=(q-r)^2-L_P q>0:
       L_P <= L_{2,P} <= floor(L_P*q*(q-r-1)/D).
Also verify r=0 case against banked collapse bound floor(L(q-1)/(q-L)).
"""
import itertools, random
import numpy as np

q, n, k = 5, 4, 2
dom = [1, 2, 4, 3]          # 2^j mod 5, cyclic order
# 25 codewords, value vectors
cw = []
for a0 in range(q):
    for a1 in range(q):
        cw.append(tuple((a0 + a1 * x) % q for x in dom))
words = list(itertools.product(range(q), repeat=n))   # 625
# mask of exact agreement per (word, codeword)
wmask = np.zeros((len(words), len(cw)), dtype=np.int64)
for wi, w in enumerate(words):
    for ci, c in enumerate(cw):
        m = 0
        for j in range(n):
            if c[j] == w[j]: m |= 1 << j
        wmask[wi, ci] = m
# per-word histogram over the 16 masks
hist = np.zeros((len(words), 16), dtype=np.int64)
for wi in range(len(words)):
    np.add.at(hist[wi], wmask[wi], 1)

popc = np.array([bin(m).count("1") for m in range(16)])
def aper(m):
    S = {j for j in range(4) if m >> j & 1}
    if not S: return False   # empty support: c undefined; exclude
    for M in (2, 4):
        s = 4 // M
        if all(((x + s) % 4) in S for x in S): return False
    return True
P_aper = {m for m in range(16) if aper(m)}
P_all = set(range(16))
rng = random.Random(7)
props = [("P_aper", P_aper), ("P_all", P_all)] + \
        [(f"rand{i}", {m for m in range(16) if rng.random() < 0.5}) for i in range(200)]

# joint pair table: for each (maskA, maskB) the intersection mask
inter = np.array([[a & b for b in range(16)] for a in range(16)])
fails = checks = 0
for name, P in props:
    for a_thr in (2, 3, 4):
        r = n - a_thr
        qualify = np.array([1 if (popc[m] >= a_thr and m in P) else 0 for m in range(16)])
        LP = int((hist * qualify[None, :]).sum(axis=1).max())
        Qm = qualify[inter]                      # 16x16 0/1
        M_ = hist @ Qm @ hist.T                  # 625x625 pair list sizes
        L2P = int(M_.max())
        checks += 1
        if LP == 0:
            if L2P != 0: print("ESP FAIL zero-case", name, a_thr); fails += 1
            continue
        D = (q - r) ** 2 - LP * q
        if D <= 0: continue
        bound = (LP * q * (q - r - 1)) // D
        if not (LP <= L2P <= bound):
            print("ESP FAIL", name, a_thr, LP, L2P, bound); fails += 1
        if r == 0:
            collapse = (LP * (q - 1)) // (q - LP) if LP < q else None
            if collapse is not None and bound != collapse:
                print("r=0 mismatch vs collapse bound", name, LP, bound, collapse); fails += 1
print(f"ESP brute-force: {checks} (property,a) configs, fails={fails}")
print(f"  sample: P_aper a=3: LP={'/'.join('')}", end="")
# report the aperiodic numbers explicitly
for name, P in props[:2]:
    for a_thr in (2,3,4):
        r = n - a_thr
        qualify = np.array([1 if (popc[m] >= a_thr and m in P) else 0 for m in range(16)])
        LP = int((hist * qualify[None,:]).sum(axis=1).max())
        Qm = qualify[inter]; L2P = int((hist @ Qm @ hist.T).max())
        D = (q-r)**2 - LP*q
        b = (LP*q*(q-r-1))//D if (LP and D>0) else None
        print(f"\n  {name} a={a_thr}: L_P={LP} L_2P={L2P} D={D} bound={b}", end="")
print()
