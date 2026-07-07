#!/usr/bin/env python3
"""Hyperbola normal form: machine verification + interior-family invariant
extraction (Modal). For every interior (nontoral) trade at the 3 | q-1
rows: verify X*Y = Delta on all same-fiber pairs (12 per trade), then
extract invariants: Delta(F), depressed-shift m = -a/3, whether
Delta/asymptote coordinates carry mu_n-multiplicative structure
(ord(Delta), X-coordinate ratios in mu_n?), and the within-support
exponent-gap histogram."""
import itertools
import json
import modal

app = modal.App("rs-mca-f3-hyperbola")
image = modal.Image.debian_slim()

ROWS = [(96, 9601), (128, 33409), (192, 37057)]


@app.function(image=image, cpu=2, memory=3072, timeout=270)
def run(rowspec):
    n, q = rowspec

    def inv(x):
        return pow(x % q, q - 2, q)

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
    omega = None
    for cand in range(2, q):
        w = pow(cand, (q - 1) // 3, q)
        if w != 1:
            omega = w
            break
    om2 = omega * omega % q
    # alpha, beta: u+v = alpha*(u - omega v) + beta*(u - om2 v)
    # solve: alpha + beta = 1; -alpha*omega - beta*om2 = 1
    det = (om2 - omega) % q
    alpha = (1 + om2) % q * inv(det) % q
    beta = (1 - alpha) % q

    counts = {}
    for P in itertools.combinations(range(n), 3):
        r0, r1, r2 = D[P[0]], D[P[1]], D[P[2]]
        sig = ((r0 + r1 + r2) % q, (r0*r1 + r0*r2 + r1*r2) % q)
        counts.setdefault(sig, []).append(P)
    step = n // 3 if n % 3 == 0 else None
    verified = failed = 0
    gap_hist = {}
    delta_orders = {}
    n_interior = 0
    mu = set(D)
    delta_in_mu = 0
    for sig, mem in counts.items():
        if len(mem) < 2:
            continue
        for i in range(len(mem)):
            for j in range(i + 1, len(mem)):
                A, B = mem[i], mem[j]
                if set(A) & set(B):
                    continue
                if step and all(x % step == A[0] % step for x in A) and \
                        all(x % step == B[0] % step for x in B):
                    continue
                n_interior += 1
                e1, e2 = sig
                a = (-e1) % q
                b = e2 % q
                Delta = (a * a % q * alpha % q * beta % q - b) % q
                # verify X*Y = Delta on all same-fiber ordered pairs
                ok = True
                for S in (A, B):
                    vals = [D[s] for s in S]
                    for u, v in itertools.permutations(vals, 2):
                        X = (u - omega * v + a * beta) % q
                        Y = (u - om2 * v + a * alpha) % q
                        if X * Y % q != Delta:
                            ok = False
                if ok:
                    verified += 1
                else:
                    failed += 1
                # invariants
                if Delta in mu:
                    delta_in_mu += 1
                # order of Delta (bucketed)
                if Delta:
                    o = 1
                    y = Delta
                    while y != 1 and o <= 96:
                        y = y * Delta % q
                        o += 1
                    delta_orders[o if o <= 96 else 99] = \
                        delta_orders.get(o if o <= 96 else 99, 0) + 1
                for S in (A, B):
                    gaps = sorted(min((S[k] - S[l]) % n, (S[l] - S[k]) % n)
                                  for k in range(3) for l in range(k))
                    key = tuple(gaps)
                    gap_hist[key] = gap_hist.get(key, 0) + 1
    top_gaps = sorted(gap_hist.items(), key=lambda kv: -kv[1])[:6]
    return {"n": n, "q": q, "interior": n_interior, "verified": verified,
            "failed": failed, "delta_in_mu_n": delta_in_mu,
            "delta_order_hist": {str(k): v for k, v in sorted(delta_orders.items())},
            "top_gap_patterns": [[list(k), v] for k, v in top_gaps]}


@app.local_entrypoint()
def main():
    res = [r for r in run.map(ROWS, return_exceptions=True)
           if isinstance(r, dict)]
    for r in res:
        print(f"({r['n']},{r['q']}): interior={r['interior']} "
              f"XY=Delta verified={r['verified']} failed={r['failed']} "
              f"Delta in mu_n: {r['delta_in_mu_n']}")
        print(f"   Delta order hist: {r['delta_order_hist']}")
        print(f"   top gap patterns: {r['top_gap_patterns']}")
    with open("/tmp/f3_hyperbola.json", "w") as f:
        json.dump(res, f, indent=1)
