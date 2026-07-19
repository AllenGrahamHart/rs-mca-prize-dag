#!/usr/bin/env python3
"""F7-A1b (floor campaign, Modal): the 17 heavy census cells, sharded.

Completes F7's first attack family: the heavy structured cells that hit
the 60 s cap in F7-A1 are re-run with BOTH internal loops sharded (the
full-petal scan by touched-combo index, the two-petal pencil by pair
index), findings merged and classified client-side with the census's own
classify_pattern. Alarm = any UNCLASSIFIED record (third-class).
"""
import itertools
import json
import re
from pathlib import Path

import modal

app = modal.App("rs-mca-f7a1b-heavy")
image = modal.Image.debian_slim().pip_install("numpy")

HERE = Path('/home/u2470931/smooth-read-solomin/prize/critical/nodes/'
            'worst_word_challenger_pricing/notes')
NSHARDS = 24


def _sources():
    core = (HERE / 'e22_core.py').read_text()
    census = (HERE / 'e22_census_modal.py').read_text()
    census = re.sub(r'^import modal\s*$', '', census, flags=re.M)
    census = re.sub(r'^app = modal\.App.*$', '', census, flags=re.M)
    census = re.sub(r'^image = .*$', '', census, flags=re.M)
    census = re.sub(r'^@app\.\w+\(.*\)\s*$', '', census, flags=re.M)
    return core, census


def _load(core_src, census_src):
    import sys
    import types
    ns = {"__name__": "e22_core", "__file__": "/tmp/a/b/e22_core.py"}
    exec(core_src, ns)
    mod = types.ModuleType("e22_core")
    mod.__dict__.update(ns)
    sys.modules["e22_core"] = mod
    ns2 = {"__name__": "e22_census", "__file__": "/tmp/a/b/e22_census.py"}
    exec(census_src, ns2)
    return ns2


@app.function(image=image, cpu=2, memory=3072, timeout=60)
def heavy_shard(payload):
    import itertools as it
    import math
    core_src, census_src, spec, shard, nshards = payload
    ns = _load(core_src, census_src)
    n, k, sigma, layout, scalar_mode = spec
    word = ns["sunflower_word"](n, k, sigma, layout, scalar_mode)
    P = ns["P"] if "P" in ns else __import__("e22_core").P
    core, petals, ell = word["core"], word["petals"], word["ell"]
    domain = word["domain"]
    found = {}
    max_excess = 2
    # (a) full-petal scan, sharded by touched-combo counter
    dmax = min(len(core), ell + max_excess)
    est = (2 ** len(petals)) * math.comb(len(core), dmax) if len(core) else 0
    counter = 0
    if est <= 200_000_000:
        for excess in range(max_excess + 1):
            d = ell + excess
            if d > len(core):
                continue
            for tc in range(2, len(petals) + 1):
                if d > (tc - 1) * ell:
                    continue
                for touched in it.combinations(range(len(petals)), tc):
                    counter += 1
                    if counter % nshards != shard:
                        continue
                    pts = sorted(pt for pi in touched for pt in petals[pi])
                    for mc in it.combinations(core, d):
                        agreement = sorted((set(core) - set(mc)) | set(pts))
                        if len(agreement) < word["s"]:
                            continue
                        poly = ns["polynomial_through"](agreement, domain,
                                                        word["values"], word["k"])
                        if poly is None or poly in word["planted_polynomials"]:
                            continue
                        rec = ns["pattern"](poly, word)
                        if rec["agreement"] >= word["s"]:
                            found[poly] = rec
    # (b) pencil, sharded by pair index
    if len(core) >= ell:
        petal_locators = [ns["locator"]([domain[i] for i in petal], P)
                          for petal in petals]
        mcls = [(mc, ns["locator"]([domain[i] for i in mc], P))
                for mc in it.combinations(core, ell)]
        for idx, (i, j) in enumerate(it.combinations(range(len(petals)), 2)):
            if idx % nshards != shard:
                continue
            left, right = petal_locators[i], petal_locators[j]
            pencil = {ns["poly_add"](ns["poly_scale"](left, 1 + b, P),
                                     ns["poly_scale"](right, -b, P), P): b
                      for b in range(P)}
            for mc, ld in mcls:
                if ld in pencil:
                    b = pencil[ld]
                    cand = ns["poly_add"](ns["poly_scale"](left, 1 + b, P),
                                          ns["poly_scale"](right, -b, P), P)
                    if len(cand) <= word["k"] and cand not in word["planted_polynomials"]:
                        rec = ns["pattern"](cand, word)
                        if rec["agreement"] >= word["s"]:
                            found[cand] = rec
    return {"spec": list(spec), "shard": shard, "ell": ell,
            "found": [[list(p), r] for p, r in found.items()]}


@app.local_entrypoint()
def main():
    core, census = _sources()
    ns = _load(core, census)
    plan = [tuple(s) for s in ns["build_plan"]()]
    done = json.loads((HERE / 'f7a1_census_results.json').read_text())["completed"]
    done_keys = set()
    for c in done:
        if isinstance(c, dict) and all(x in c for x in ("n", "k", "sigma")):
            done_keys.add((c["n"], c["k"], c["sigma"],
                           c.get("layout"), c.get("scalar_mode")))
    heavy = [s for s in plan if s not in done_keys]
    print(f"heavy cells to shard: {len(heavy)} of plan {len(plan)}")
    payloads = [(core, census, s, sh, NSHARDS) for s in heavy for sh in range(NSHARDS)]
    print(f"{len(payloads)} shard jobs")
    results = [r for r in heavy_shard.map(payloads, return_exceptions=True)
               if isinstance(r, dict)]
    # merge per spec
    merged = {}
    for r in results:
        key = tuple(r["spec"])
        m = merged.setdefault(key, {"ell": r["ell"], "found": {}, "shards": 0})
        m["shards"] += 1
        for poly, rec in r["found"]:
            m["found"][tuple(poly)] = rec
    total_unclassified = 0
    for key, m in sorted(merged.items()):
        classes = {}
        for rec in m["found"].values():
            c = ns["classify_pattern"](rec, m["ell"])
            classes[c] = classes.get(c, 0) + 1
        unc = sum(classes.get(c, 0) for c in ns["UNCLASSIFIED_CLASSES"])
        total_unclassified += unc
        flag = "  <-- THIRD-CLASS ALARM" if unc else ""
        print(f"{key}: shards {m['shards']}/{NSHARDS} hits={len(m['found'])} "
              f"classes={classes}{flag}")
    print(f"\nTOTAL UNCLASSIFIED across heavy cells: {total_unclassified}")
    with open("/tmp/f7a1b_results.json", "w") as f:
        json.dump({str(k): {"classes": {c: v for c, v in
                   [(ns['classify_pattern'](rec, m['ell']), 1) for rec in m['found'].values()] } ,
                   "hits": len(m["found"]), "shards": m["shards"]}
                   for k, m in merged.items()}, f, indent=1, default=str)
