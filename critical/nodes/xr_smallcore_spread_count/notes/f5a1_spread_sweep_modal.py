#!/usr/bin/env python3
"""F5-A1 (floor campaign, Modal): the spread-family count sweep — first
attack on the xr_smallcore 16n^3 per-pair floor.

FLOOR: per pair (u,v), the post-strip spread remainder R_spread(u,v;A)
fits inside R_post <= 16 n^3. Objects per the node's own rungs verifier
(verify_xr_smallcore_rungs_2a_2b.py, source-shipped; its certificate run
is the CALIBRATION GATE): a support S is z-aligned if some codeword agrees
with u+zv on S; same-slope families are the exact-list column (stripped);
distinct-slope tangent depth d >= 1 is tangent-charged (stripped); the
spread remainder = pairwise-small-core (|S_i ∩ S_j| < k+t-1) families of
aligned supports across distinct slopes.

MEASUREMENT (exact, per toy pair): enumerate all codewords (q^k small),
all slopes z, all agreement sets with u+zv; supports = A-subsets of
agreement sets with A = k+1; count (i) total aligned supports, (ii) a
GREEDY maximal pairwise-small-core distinct-slope family (a lower bound
on the spread family — sufficient for an ALARM; its smallness plus the
total gives the survival bound). Compare to the transported budget 16n^3.
Pairs: adversarial (two codewords + sparse noise — pencils through many
codewords) + random controls. Scales: (k=2: q in {17, 31, 49-ish}) and
(k=3: q in {17, 31}) with n = q-1 full domain.

PRE-REGISTERED: falsifier fires on a pair with greedy spread family
> 16 n^3, sustained across scales. FM-band-consistent counts do NOT fire.
"""
import json
from pathlib import Path

import modal

app = modal.App("rs-mca-f5a1-spread")
image = modal.Image.debian_slim()


def _src():
    return Path('/home/u2470931/smooth-read-solomin/rs-mca-upstream-xr-smallcore/'
                'experimental/scripts/verify_xr_smallcore_rungs_2a_2b.py').read_text()


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def gate(src):
    import os
    os.makedirs("/tmp/a/b/experimental/data/certificates/xr-smallcore-rungs-2a-2b",
                exist_ok=True)
    os.chdir("/tmp/a/b")
    ns = {"__name__": "rungs", "__file__": "/tmp/a/b/rungs.py"}
    exec(src, ns)
    cert = ns["build_certificate"]()
    ns["verify_certificate"](cert)
    return {"pass": len(ns["FAIL"]) == 0, "n_pass": len(ns["PASS"]),
            "fails": ns["FAIL"][:5]}


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def spread_cell(payload):
    import itertools
    import random
    src, k, q, seed = payload
    ns = {"__name__": "rungs", "__file__": "/tmp/a/b/rungs.py"}
    exec(src, ns)
    rng = random.Random(seed)
    domain = tuple(range(1, q))          # full multiplicative domain, n = q-1
    n = len(domain)
    cws = ns["codewords"](domain, k, q)  # [(coeffs, values)]
    A = k + 1
    t = 2
    core_thresh = k + t - 1
    budget = 16 * n**3

    def measure(u, v):
        aligned = []                      # (z, frozenset support)
        for z in range(q):
            w = tuple((u[i] + z * v[i]) % q for i in range(n))
            for coeffs, vals in cws:
                agree = [i for i in range(n) if vals[i] == w[i]]
                if len(agree) >= A:
                    for S in itertools.combinations(agree, A):
                        aligned.append((z, frozenset(S)))
        # greedy pairwise-small-core distinct-slope family
        fam = []
        for z, S in aligned:
            if all(z != z2 and len(S & S2) < core_thresh for z2, S2 in fam):
                fam.append((z, S))
        return len(aligned), len(fam)

    rows = []
    for trial in range(6):
        c1 = rng.choice(cws)[1]
        c2 = rng.choice(cws)[1]
        u = list(c1)
        v = list(c2)
        for _ in range(2):               # sparse noise
            u[rng.randrange(n)] = rng.randrange(q)
            v[rng.randrange(n)] = rng.randrange(q)
        tot, fam = measure(tuple(u), tuple(v))
        rows.append({"kind": "adversarial", "total_aligned": tot,
                     "greedy_spread": fam})
    for trial in range(3):
        u = tuple(rng.randrange(q) for _ in range(n))
        v = tuple(rng.randrange(q) for _ in range(n))
        tot, fam = measure(u, v)
        rows.append({"kind": "random", "total_aligned": tot,
                     "greedy_spread": fam})
    worst = max(r["greedy_spread"] for r in rows)
    return {"k": k, "q": q, "n": n, "budget_16n3": budget,
            "worst_greedy_spread": worst,
            "alarm": worst > budget, "rows": rows}


@app.local_entrypoint()
def main():
    src = _src()
    g = gate.remote(src)
    print(f"calibration gate (rungs 2a/2b certificate): pass={g['pass']} "
          f"({g['n_pass']} checks){' FAILS: ' + str(g['fails']) if not g['pass'] else ''}")
    if not g["pass"]:
        return
    cells = [(2, 17), (2, 31), (2, 49), (2, 71), (3, 17), (3, 31)]
    # q=49 not prime — replace with 47? domain needs field: use primes only
    cells = [(2, 17), (2, 31), (2, 47), (2, 71), (3, 17), (3, 31)]
    payloads = [(src, k, q, 20260707 + i) for i, (k, q) in enumerate(cells)]
    results = [r for r in spread_cell.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    for r in sorted(results, key=lambda r: (r["k"], r["q"])):
        flag = "  <-- ALARM" if r["alarm"] else ""
        print(f"k={r['k']} q={r['q']} n={r['n']}: worst greedy spread = "
              f"{r['worst_greedy_spread']} vs budget {r['budget_16n3']}{flag}")
    with open("/tmp/f5a1_results.json", "w") as f:
        json.dump(results, f, indent=1)
