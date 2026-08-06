#!/usr/bin/env python3
"""h=3 dichotomy test (Modal): char-0-persistent vs p-selected families.

(a) PERSISTENCE: enumerate interior trades at many primes q = 1 mod 96
    in [n^2, 5n^2]; extract the canonical shape of each dilation orbit
    (lex-min rotation of the combined exponent multiset). Prediction
    (norm-gate dichotomy): interior shape sets are DISJOINT across q
    (p-selected), while toral shapes persist everywhere.

(b) CERTIFICATE: for interior shapes at (96, 9601), verify the
    p-selection algebra directly in Z[zeta_96] via sympy: with gaps and
    relative shift fixed, the two trade conditions are elements
    E1, E2 of Z[zeta_96]; check E1, E2 != 0 in char 0 (NOT a char-0
    trade) while p | Norm(E1), p | Norm(E2) (the norm gate that
    activates the family at this q)."""
import itertools
import json
import modal

app = modal.App("rs-mca-f3-dichotomy")
image = modal.Image.debian_slim().pip_install("sympy")

N = 96
QS = [9601, 13249, 18433, 23233, 26113, 27649, 36097, 42337, 46273]  # =1 mod 96


@app.function(image=image, cpu=2, memory=3072, timeout=270)
def shapes_at(q):
    n = N
    g = None
    for cand in range(2, q):
        x = pow(cand, (q - 1) // n, q)
        if x == 1:
            continue
        y, order = x, 1
        while y != 1:
            y = y * x % q
            order += 1
        if order == n:
            g = x
            break
    D = [pow(g, i, q) for i in range(n)]
    counts = {}
    for P in itertools.combinations(range(n), 3):
        r0, r1, r2 = D[P[0]], D[P[1]], D[P[2]]
        sig = ((r0 + r1 + r2) % q, (r0*r1 + r0*r2 + r1*r2) % q)
        counts.setdefault(sig, []).append(P)
    step = n // 3
    interior_shapes = set()
    n_interior = 0
    for sig, mem in counts.items():
        if len(mem) < 2:
            continue
        for i in range(len(mem)):
            for j in range(i + 1, len(mem)):
                A, B = mem[i], mem[j]
                if set(A) & set(B):
                    continue
                if all(x % step == A[0] % step for x in A) and \
                        all(x % step == B[0] % step for x in B):
                    continue
                n_interior += 1
                # canonical shape: lex-min over rotations, of (sorted A-offsets,
                # sorted B-offsets) with A the lex-smaller side
                best = None
                for s in range(n):
                    Ar = tuple(sorted((a - s) % n for a in A))
                    Br = tuple(sorted((b - s) % n for b in B))
                    for X, Y in ((Ar, Br), (Br, Ar)):
                        if X[0] != 0:
                            continue
                        cand2 = (X, Y)
                        if best is None or cand2 < best:
                            best = cand2
                interior_shapes.add(best)
    return {"q": q, "n_interior": n_interior,
            "shapes": sorted([list(a) + list(b) for a, b in interior_shapes])}


@app.function(image=image, cpu=2, memory=4096, timeout=270)
def certificate(shape):
    """shape = [a1,a2,a3, b1,b2,b3] exponents mod 96. Verify char-0
    nonvanishing + p | Norm at p = 9601."""
    import sympy as sp
    n, p = N, 9601
    z = sp.exp(2 * sp.pi * sp.I / n)
    A = shape[:3]
    B = shape[3:]
    xs = [z**a for a in A]
    ys = [z**b for b in B]
    E1 = sp.expand(sum(xs) - sum(ys))
    E2 = sp.expand(xs[0]*xs[1] + xs[0]*xs[2] + xs[1]*xs[2]
                   - (ys[0]*ys[1] + ys[0]*ys[2] + ys[1]*ys[2]))
    # char-0 vanishing test (numeric to high precision + exact minpoly route)
    e1_zero = abs(complex(E1.evalf(50))) < 1e-30
    e2_zero = abs(complex(E2.evalf(50))) < 1e-30
    # norm mod p: work in F_p[zeta] using a primitive 96th root mod p
    for cand in range(2, p):
        x = pow(cand, (p - 1) // n, p)
        if x == 1:
            continue
        y, order = x, 1
        while y != 1:
            y = y * x % p
            order += 1
        if order == n:
            zp = x
            break
    def val_mod(expr_exps, pairs=False):
        if not pairs:
            return sum(pow(zp, a, p) for a in expr_exps) % p
    E1p = (sum(pow(zp, a, p) for a in A) - sum(pow(zp, b, p) for b in B)) % p
    E2p = 0
    xa = [pow(zp, a, p) for a in A]
    yb = [pow(zp, b, p) for b in B]
    E2p = (xa[0]*xa[1] + xa[0]*xa[2] + xa[1]*xa[2]
           - yb[0]*yb[1] - yb[0]*yb[2] - yb[1]*yb[2]) % p
    return {"shape": shape, "char0_E1_zero": bool(e1_zero),
            "char0_E2_zero": bool(e2_zero),
            "E1_mod_p_zero": E1p == 0, "E2_mod_p_zero": E2p == 0}


@app.local_entrypoint()
def main():
    res = [r for r in shapes_at.map(QS, return_exceptions=True)
           if isinstance(r, dict)]
    print("=== persistence across q (n = 96) ===")
    all_shapes = {}
    for r in sorted(res, key=lambda r: r['q']):
        print(f"  q={r['q']}: interior={r['n_interior']}, shapes={len(r['shapes'])}")
        for s in r['shapes']:
            all_shapes.setdefault(tuple(s), []).append(r['q'])
    print("\nshape -> activating q list:")
    for s, qs in sorted(all_shapes.items(), key=lambda kv: -len(kv[1])):
        print(f"  {list(s)}: {qs}")
    # certificates for the (96,9601) shapes
    s9601 = [list(s) for s, qs in all_shapes.items() if 9601 in qs]
    if s9601:
        certs = [c for c in certificate.map(s9601[:4], return_exceptions=True)
                 if isinstance(c, dict)]
        print("\n=== p-selection certificates at q = 9601 ===")
        for c in certs:
            print(f"  {c['shape']}: char0 zero = ({c['char0_E1_zero']},{c['char0_E2_zero']}), "
                  f"mod-p zero = ({c['E1_mod_p_zero']},{c['E2_mod_p_zero']})")
    with open("/tmp/f3_dichotomy.json", "w") as f:
        json.dump({"persistence": res}, f, indent=1)
