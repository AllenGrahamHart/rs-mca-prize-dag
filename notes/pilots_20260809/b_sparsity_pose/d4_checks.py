"""D4 — LEM-1 at the prize dimension, and the consumer sub-family pricing.

(1) LEM-1 (energy ceiling, banked LN4) checked directly on h=64 box vectors:
    0 < Norm(w) <= E(w)^{32} <= 256^32 = 2^256, and the odd-norm refinement
    E <= 4h-3 => Norm <= 253^32.
(2) The proved sparsity bound evaluated on the sub-families a consumer might
    actually be handed: full admissible window, thin deployed band, the
    v_2 >= 92 stratum, and the Proth-form family the deployment uses.
"""
import random, math

random.seed(20260809)
L2 = math.log(2)


def negmul(a, b, h):
    c = [0] * h
    for i in range(h):
        ai = a[i]
        if not ai:
            continue
        for j in range(h):
            bj = b[j]
            if not bj:
                continue
            k = i + j
            if k < h:
                c[k] += ai * bj
            else:
                c[k - h] -= ai * bj
    return c


def tower_norm(w):
    w = list(w)
    h = len(w)
    while h > 1:
        wm = [w[i] if i % 2 == 0 else -w[i] for i in range(h)]
        p = negmul(w, wm, h)
        w = [p[2 * i] for i in range(h // 2)]
        h //= 2
    return w[0]


h = 64
bad = badodd = 0
mx = 0
mxodd = 0
n = 4000
for _ in range(n):
    w = [random.randint(-2, 2) for _ in range(h)]
    if not any(w):
        continue
    N = tower_norm(w)
    E = sum(x * x for x in w)
    if N <= 0 or N > E ** (h // 2) or N > (4 * h) ** (h // 2):
        bad += 1
    mx = max(mx, N)
    if sum(w) % 2:
        if N > (4 * h - 3) ** (h // 2):
            badodd += 1
        mxodd = max(mxodd, N)
print("LEM-1 at h=64 on %d random box vectors: violations %d (odd-norm refinement: %d)"
      % (n, bad, badodd))
print("  largest sampled norm 2^%.2f   (ceiling 2^256; odd-norm ceiling 2^255.46)"
      % math.log2(mx))

print()
print("=== consumer sub-family pricing (CLASSBOUND = 2^135.6034, RPRIME = 1) ===")
CB = 135.6034


def li(x2, K=12):
    lnx = x2 * L2
    return x2 - math.log2(lnx) + math.log2(sum(math.factorial(k) / lnx ** k
                                               for k in range(K)))


def pi_win(lo2, hi2, phi=64.0):
    return (hi2 + math.log2(1 - 2 ** (li(lo2) - li(hi2)))) - math.log2(lnx_(hi2)) \
        - math.log2(phi) if False else \
        (li(hi2) + math.log2(1 - 2 ** (li(lo2) - li(hi2)))) - math.log2(phi)


rows = [
    ("W_ADM  (2^128,2^256], any v_2", pi_win(128, 256), None),
    ("W_ADM, v_2 >= 92", pi_win(128, 256) - 85, None),
    ("W_ADM, v_2 >= 113", pi_win(128, 256) - 106, None),
    ("W_DEP  [2^166,2^172), any v_2", pi_win(166, 172), None),
    ("W_DEP, v_2 >= 92", pi_win(166, 172) - 85, None),
]
# Proth family in W_DEP with v_2 >= 92: p = k*2^v+1, k odd < 2^v
proth = math.log2(2 ** 79) + math.log2(2 / (172 * L2))
rows.append(("W_DEP Proth k*2^92+1 (k odd)", proth, None))
for lab, P, _ in rows:
    print("  %-34s PI = 2^%7.2f   proved bound 2^%+8.2f %s"
          % (lab, P, CB - P, "" if CB - P < 0 else "  <-- VACUOUS"))

print()
print("=== consistency with round-25's measured count ===")
print("  round-25 measured log2 BADCOUNT(W_ADM) = 132.0 ; proved ceiling = %.2f"
      % CB)
print("  headroom = %.2f bits  (a measured count ABOVE the ceiling would refute"
      " one of the two)" % (CB - 132.0))
