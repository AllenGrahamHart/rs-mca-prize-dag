#!/usr/bin/env python3
"""Bounded Modal probe for joint-owner multiplicity in small FPC5 cells."""

from __future__ import annotations

import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve()
ROOT = HERE.parents[2] if len(HERE.parents) >= 3 else HERE.parent
FPC5 = ROOT / "notes/pilots_20260807/fpc5_diag/rh_m4t2_census.py"
BUCKET = ROOT / "notes/pilots_20260807/mf_wall_adversary/rh_bucket.py"
ARM = ROOT / "notes/pilots_20260809/m7_complement_repose/d2_arm_a.py"
HUNT = ROOT / "notes/pilots_20260809/m7_falsifier_hunt/d2_hunt.py"

REMOTE_ROOT = "/home/u2470931/smooth-read-solomin/prize"
image = (
    modal.Image.debian_slim()
    .add_local_file(
        FPC5, REMOTE_ROOT + "/notes/pilots_20260807/fpc5_diag/rh_m4t2_census.py"
    )
    .add_local_file(
        BUCKET, REMOTE_ROOT + "/notes/pilots_20260807/mf_wall_adversary/rh_bucket.py"
    )
    .add_local_file(
        ARM, REMOTE_ROOT + "/notes/pilots_20260809/m7_complement_repose/d2_arm_a.py"
    )
    .add_local_file(
        HUNT, REMOTE_ROOT + "/notes/pilots_20260809/m7_falsifier_hunt/d2_hunt.py"
    )
)

app = modal.App("rs-mca-fpc5-joint-owner-probe")


@app.function(image=image, cpu=1.0, memory=1024, timeout=60)
def probe() -> dict:
    import random
    import sys
    import time
    from collections import Counter
    from itertools import combinations
    from math import comb

    sys.path.insert(0, REMOTE_ROOT + "/notes/pilots_20260807/fpc5_diag")
    sys.path.insert(0, REMOTE_ROOT + "/notes/pilots_20260807/mf_wall_adversary")
    sys.path.insert(0, REMOTE_ROOT + "/notes/pilots_20260809/m7_complement_repose")
    sys.path.insert(0, REMOTE_ROOT + "/notes/pilots_20260809/m7_falsifier_hunt")

    from d2_hunt import SPECS, build_flat_general
    from rh_bucket import enumerate_split, monic_chart, rref_kernel
    from rh_m4t2_census import domain, peval, pgcd, pdegree, pmul, prem

    def one_config(rng, spec):
        q = spec["q"]
        M, t, ell = spec["M"], spec["t"], spec["ell"]
        b, u, d, N, n = spec["b"], spec["u"], spec["d"], spec["N"], spec["n"]
        points, _ = domain(n, q)
        rng.shuffle(points)
        core = sorted(points[:N])
        bg = points[N : N + b]
        petals = [
            points[N + b + i * ell : N + b + (i + 1) * ell]
            for i in range(M)
        ]
        labels = rng.sample(range(1, q), M)
        touched = tuple(range(t))
        untouched = range(t, M)
        candidates = {}

        for chosen in combinations(bg, u):
            matrix, product_poly, crt_poly, rows = build_flat_general(
                list(chosen), petals, labels, touched, q, d
            )
            if rows != ell - 1:
                raise AssertionError("unexpected guarded codimension")
            basis = rref_kernel(matrix, d + 1, q)
            base, directions = monic_chart(basis, d, q)
            if base is None:
                continue
            common = base[:]
            for direction in directions:
                common = pgcd(common, direction, q)
            if max(pdegree(common), 0) > 0:
                raise AssertionError("flat-wide common locator factor")
            found, _ = enumerate_split(base, directions, core, d, q)
            for root_tuple, coefficients in found.items():
                locator_poly = base[:]
                for coefficient, direction in zip(coefficients, directions):
                    if coefficient:
                        locator_poly = [
                            (x + coefficient * y) % q
                            for x, y in zip(locator_poly, direction)
                        ]
                numerator = prem(pmul(locator_poly, crt_poly, q), product_poly, q)
                if any(peval(numerator, x, q) == 0 for x in root_tuple):
                    continue
                if any(
                    (peval(numerator, x, q) - labels[i] * peval(locator_poly, x, q))
                    % q
                    == 0
                    for i in untouched
                    for x in petals[i]
                ):
                    continue
                bg_roots = frozenset(x for x in bg if peval(numerator, x, q) == 0)
                key = frozenset(root_tuple)
                previous = candidates.setdefault(key, bg_roots)
                if previous != bg_roots:
                    raise AssertionError("background roots depend on chosen certificate")

        marked = [(roots, roots | candidates[roots]) for roots in candidates]
        r = spec["r_J"]
        v = max(0, u)
        result = {
            "members": len(marked),
            "anchors": len(marked) if len(marked) >= 2 else 0,
            "owner_groups": 0,
            "owner_collisions": 0,
            "injective_anchors": 0,
            "co_def": Counter(),
            "multiplicity": Counter(),
            "packing_violations": 0,
            "max_owner_multiplicity": 0,
            "witness": None,
        }
        if len(marked) < 2:
            return result

        for anchor_index, (anchor_roots, anchor_marked) in enumerate(marked):
            owners = {}
            for candidate_index, (candidate_roots, candidate_marked) in enumerate(marked):
                if candidate_index == anchor_index:
                    continue
                defect_owner = tuple(sorted(anchor_roots & candidate_roots))
                background_owner = tuple(
                    sorted(candidates[anchor_roots] & candidates[candidate_roots])
                )
                owner = (defect_owner, background_owner)
                owners.setdefault(owner, []).append(candidate_index)
            result["owner_groups"] += len(owners)
            result["owner_collisions"] += (len(marked) - 1) - len(owners)
            result["injective_anchors"] += len(owners) == len(marked) - 1
            for owner, indices in owners.items():
                q_owner = len(owner[0]) + len(owner[1])
                if not 0 <= q_owner <= r:
                    raise AssertionError("joint owner exceeds determinant degree")
                c = r - q_owner
                result["co_def"][c] += len(indices)
                result["multiplicity"][len(indices)] += 1
                s = c + 1
                bound = comb(N + b - q_owner, s) // comb(d + v - q_owner, s)
                if len(indices) > bound:
                    result["packing_violations"] += 1
                if len(indices) > result["max_owner_multiplicity"]:
                    result["max_owner_multiplicity"] = len(indices)
                    result["witness"] = {
                        "members": len(marked),
                        "owner_degree": q_owner,
                        "co_deficiency": c,
                        "owner_multiplicity": len(indices),
                        "packing_bound": bound,
                    }
        return result

    schedule = [("T1", 256), ("T2", 64), ("C8", 128)]
    deadline = time.monotonic() + 54.0
    output = {"schema": "fpc5-joint-owner-probe-v1", "cells": {}}
    for offset, (cell, requested) in enumerate(schedule):
        rng = random.Random(20260810 + offset)
        records = []
        for _ in range(requested):
            if time.monotonic() >= deadline:
                break
            records.append(one_config(rng, SPECS[cell]))
        aggregate = {
            "requested": requested,
            "completed": len(records),
            "member_hist": Counter(record["members"] for record in records),
            "anchors_total": sum(record["anchors"] for record in records),
            "owner_groups": sum(record["owner_groups"] for record in records),
            "owner_collisions": sum(record["owner_collisions"] for record in records),
            "injective_anchors": sum(record["injective_anchors"] for record in records),
            "co_def": Counter(),
            "multiplicity": Counter(),
            "packing_violations": sum(record["packing_violations"] for record in records),
            "max_owner_multiplicity": max(
                (record["max_owner_multiplicity"] for record in records), default=0
            ),
            "witness": max(
                (record["witness"] for record in records if record["witness"]),
                key=lambda item: item["owner_multiplicity"],
                default=None,
            ),
        }
        for record in records:
            aggregate["co_def"].update(record["co_def"])
            aggregate["multiplicity"].update(record["multiplicity"])
        output["cells"][cell] = aggregate
    output["elapsed_seconds"] = round(54.0 - max(0.0, deadline - time.monotonic()), 3)
    return output


@app.local_entrypoint()
def main() -> None:
    print(json.dumps(probe.remote(), indent=2, sort_keys=True))
