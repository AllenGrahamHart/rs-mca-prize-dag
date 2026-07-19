#!/usr/bin/env python3
"""E2b: robust confirmation of the pair-engineering result without the
integer-echelon ideal norm (whose coefficient explosion forced 7/250 trial
skips in E2).

Sound over-approximation chain: a two-orbit prime q (both P1, P2 vanish at a
COMMON order-n' embedding mod q) must divide both element norms, hence
q | g = gcd(|N(P1)|, |N(P2)|).  For every candidate admissible factor q of g
(q ≡ 1 mod n', q >= 97) we then check directly whether P1 and P2 share a
common root of order n' mod q.  No lattice echelon anywhere; resultants and
gcds only.  1000 pairs, fresh seed.
"""
import importlib.util
import json
import math
import random
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "rge", HERE / "resultant_gate_experiments.py")
rge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rge)

N, NPRIME = rge.N, rge.NPRIME
XN1 = [1] + [0] * (N - 1) + [1]

rng = random.Random(715)
TRIALS = 1000
gcd_hist = Counter()
candidates = 0
two_orbit = []
for i in range(TRIALS):
    s1, g1 = rge.random_ternary(rng, 5)
    s2, g2 = rge.random_ternary(rng, 5)
    if rge.census.orbit_key(s1, g1, N) == rge.census.orbit_key(s2, g2, N):
        continue
    P1, P2 = rge.poly_from(s1, g1), rge.poly_from(s2, g2)
    n1, n2 = abs(rge.resultant(XN1, P1)), abs(rge.resultant(XN1, P2))
    g = math.gcd(n1, n2)
    gcd_hist[g if g <= 64 else ">64"] += 1
    if g > 1:
        for q in rge.factorize(g, rng):
            if q % NPRIME == 1 and q >= 97:
                candidates += 1
                r1 = set(rge.order_np_roots(P1, q))
                r2 = set(rge.order_np_roots(P2, q))
                if r1 & r2:
                    two_orbit.append({"q": q, "P1": [s1, g1], "P2": [s2, g2]})
out = {
    "experiment": "E2b_pair_gcd_web",
    "pairs": TRIALS,
    "gcd_hist": {str(k): v for k, v in sorted(gcd_hist.items(), key=str)},
    "admissible_candidate_primes": candidates,
    "common_embedding_two_orbit_pairs": len(two_orbit),
    "examples": two_orbit[:5],
}
(HERE / "pair_gcd_web_results.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
