#!/usr/bin/env python3
"""ROUND S3 (self-tennis), REFUTE CHAIR on Modal: the DUAL-GEOMETRIC family.

CLAIM UNDER ATTACK (S2's DYADIC-K hypothesis, second half): "the top range
j < j1 carries no lambda at all (dual near-peak emptiness)".

ATTACK: rows whose embedding has a geometrically small orbit. If omega = 2
(q | Phi_{n'}(2), so ord(2) = n' exactly), then u_y = lambda*2^y mod q is
small for lambda in the 2-adic orbit, and T(lambda) = prod cos^2(pi u_y/q)
is MACROSCOPIC — the iid model predicts none.

Toy instance (exact): q = 6700417 (the large factor of F5 = 2^32+1 = 641 *
6700417), n' = 64, N = 32, L = 1, omega = 2 (2^32 ≡ -1 mod q). Controls:
(i) the SAME q with the PINNED embedding omega_pin = g^((q-1)/64) (is the
pinned row also contaminated? 2 = omega_pin^a for some odd a — dilation
scrambles the geometric structure); (ii) a random admissible prime of the
same size with its pinned embedding.

Modal outputs per row: exact E (full lambda-sum via D3), T(1), dyadic
near-peak counts #{lambda != 0 : T >= 2^-j} for j = 2..32, log2 E.
Shards of 1e6 lambda; every job << 60 s.
"""
import json
import math
import sys

import modal

app = modal.App("dli-s3-dual-geometric")
image = modal.Image.debian_slim().pip_install("numpy")

Q_GEO = 6_700_417          # F5 large factor; 2^32 ≡ -1 (mod q)
Q_CTRL = 6_700_609         # candidate control prime ≡ 1 (mod 64), verified below
NP, N = 64, 32
JS = list(range(2, 34, 2))


def spr_omega(q, nprime):
    n = q - 1
    fs = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    g = 2
    while any(pow(g, (q - 1) // p, q) == 1 for p in fs):
        g += 1
    return g, pow(g, (q - 1) // nprime, q)


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def scan_shard(payload):
    import numpy as np
    q, omega, lo, hi = payload
    xs = np.array([pow(omega, y, q) for y in range(N)], dtype=np.int64)
    lam = np.arange(lo, hi, dtype=np.int64)
    a = lam[:, None] * xs[None, :] % q
    lg = np.log2(np.cos(np.pi * a / q) ** 2 + 1e-300).sum(axis=1)
    counts = {j: int((lg >= -j).sum()) for j in JS}
    # E contribution: sum of T over the shard (log-sum-exp safe: T <= 1)
    e_contrib = float(np.exp2(lg).sum())
    top = sorted(lam[np.argsort(lg)[-3:]].tolist())
    return {"lo": lo, "counts": counts, "e": e_contrib,
            "top_lambda": top, "max_log2T": float(lg.max())}


@app.local_entrypoint()
def main():
    # exact local pre-checks (trivial arithmetic)
    assert (2**32 + 1) % Q_GEO == 0 and Q_GEO % NP == 1
    assert pow(2, 32, Q_GEO) == Q_GEO - 1          # ord(2) = 64 exactly
    # control prime: verified prime ≡ 1 mod 64 (Miller-Rabin via sympy-free)
    def is_prime(n):
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if n % p == 0:
                return n == p
        d, s = n - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            x = pow(a, d, n)
            if x in (1, n - 1):
                continue
            for _ in range(s - 1):
                x = x * x % n
                if x == n - 1:
                    break
            else:
                return False
        return True
    assert is_prime(Q_GEO) and is_prime(Q_CTRL) and Q_CTRL % NP == 1

    g_geo, om_pin_geo = spr_omega(Q_GEO, NP)
    g_c, om_pin_c = spr_omega(Q_CTRL, NP)
    rows = [("GEO omega=2", Q_GEO, 2),
            ("GEO pinned", Q_GEO, om_pin_geo),
            ("CTRL pinned", Q_CTRL, om_pin_c)]

    payloads = []
    for name, q, om in rows:
        assert pow(om, NP, q) == 1 and pow(om, N, q) == q - 1, (name, "order")
        step = 1_000_000
        for lo in range(1, q, step):
            payloads.append((q, om, lo, min(lo + step, q)))

    results = list(scan_shard.map(payloads, return_exceptions=True))
    out = {}
    for name, q, om in rows:
        shards = [r for r in results if not isinstance(r, Exception)
                  and isinstance(r, dict)]
        mine = [r for p, r in zip(payloads, results)
                if p[0] == q and p[1] == om and isinstance(r, dict)]
        counts = {j: sum(r["counts"][j] for r in mine) for j in JS}
        E = 1.0 + sum(r["e"] for r in mine)   # lambda = 0 contributes 1
        best = max(mine, key=lambda r: r["max_log2T"])
        out[name] = {"q": q, "omega": om, "E": E, "log2E": math.log2(E),
                     "near_peak_counts": counts,
                     "max_log2T_nonzero": best["max_log2T"],
                     "top_lambda": best["top_lambda"],
                     "n_shards": len(mine)}
        print(f"{name}: q={q} omega={om}  E={E:.6f}  log2E={math.log2(E):.4f}"
              f"  maxT=2^{best['max_log2T']:.2f}")
        print(f"   near-peak: {counts}")
    with open("/tmp/s3_result.json", "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))
