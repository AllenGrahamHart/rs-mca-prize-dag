#!/usr/bin/env python3
"""Bounded parallel Modal probe for guarded rational FPC5 Hankel cells."""

from __future__ import annotations

import json

import modal


app = modal.App("rs-mca-fpc5-hankel-guard-probe")
image = modal.Image.debian_slim()


SPECS = (
    {"id": "t4e2", "q": 23, "M": 5, "t": 4, "ell": 2, "b": 1, "u": 1, "d": 7, "N": 11, "configs": 64},
    {"id": "t5e2", "q": 29, "M": 6, "t": 5, "ell": 2, "b": 1, "u": 1, "d": 9, "N": 13, "configs": 48},
    {"id": "t4e3", "q": 37, "M": 5, "t": 4, "ell": 3, "b": 2, "u": 1, "d": 10, "N": 15, "configs": 64},
    {"id": "t5e3", "q": 41, "M": 6, "t": 5, "ell": 3, "b": 2, "u": 1, "d": 13, "N": 18, "configs": 48},
    {"id": "t4e4", "q": 43, "M": 5, "t": 4, "ell": 4, "b": 3, "u": 1, "d": 13, "N": 19, "configs": 32},
    {"id": "t5e4", "q": 53, "M": 6, "t": 5, "ell": 4, "b": 3, "u": 1, "d": 17, "N": 22, "configs": 24},
)


@app.function(image=image, cpu=1.0, memory=512, timeout=60)
def run_job(job: dict) -> dict:
    import random
    import time
    from itertools import combinations
    from math import comb

    spec = job["spec"]
    q = spec["q"]
    rng = random.Random(job["seed"])
    deadline = time.monotonic() + 54.0

    def peval(poly, x):
        value = 0
        for coefficient in reversed(poly):
            value = (value * x + coefficient) % q
        return value

    def locator(points):
        poly = [1]
        for root in points:
            out = [0] * (len(poly) + 1)
            for index, coefficient in enumerate(poly):
                out[index] = (out[index] - root * coefficient) % q
                out[index + 1] = (out[index + 1] + coefficient) % q
            poly = out
        return poly

    def quotient_root(poly, root):
        degree = len(poly) - 1
        out = [0] * degree
        carry = poly[-1]
        out[-1] = carry
        for index in range(degree - 1, 0, -1):
            carry = (poly[index] + root * carry) % q
            out[index - 1] = carry
        if (poly[0] + root * carry) % q:
            raise AssertionError("failed synthetic division")
        return out

    def matrix_rank(matrix):
        work = [row[:] for row in matrix]
        rank = 0
        columns = len(work[0]) if work else 0
        for column in range(columns):
            pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
            if pivot is None:
                continue
            work[rank], work[pivot] = work[pivot], work[rank]
            inverse = pow(work[rank][column], -1, q)
            work[rank] = [(x * inverse) % q for x in work[rank]]
            for i in range(len(work)):
                if i == rank or not work[i][column]:
                    continue
                factor = work[i][column]
                work[i] = [(x - factor * y) % q for x, y in zip(work[i], work[rank])]
            rank += 1
            if rank == len(work):
                break
        return rank

    def random_full_rank_moments(d, rows):
        while True:
            mu = [rng.randrange(q) for _ in range(d + rows)]
            matrix = [[mu[j + a] for a in range(d + 1)] for j in range(rows)]
            if matrix_rank(matrix) == rows:
                return mu

    def rational_moments(nodes, labels, length):
        weighted = []
        for i, z in enumerate(nodes):
            derivative = 1
            for j, y in enumerate(nodes):
                if i != j:
                    derivative = derivative * (z - y) % q
            weighted.append(labels[i] * pow(derivative, -1, q) % q)
        mu = []
        powers = [1] * len(nodes)
        for _ in range(length):
            mu.append(sum(w * power for w, power in zip(weighted, powers)) % q)
            powers = [power * z % q for power, z in zip(powers, nodes)]
        return mu, weighted

    def kernel_and_primitive(poly, roots, mu, rows):
        for j in range(rows):
            if sum(poly[a] * mu[j + a] for a in range(len(poly))) % q:
                return False, False
        for root in roots:
            quotient = quotient_root(poly, root)
            if sum(quotient[a] * mu[a] for a in range(len(quotient))) % q == 0:
                return True, False
        return True, True

    def one_config():
        M, t, ell = spec["M"], spec["t"], spec["ell"]
        b, u, d, N = spec["b"], spec["u"], spec["d"], spec["N"]
        total = N + b + M * ell
        pool = list(range(1, q))
        rng.shuffle(pool)
        if total > len(pool):
            raise AssertionError("field too small")
        core = sorted(pool[:N])
        bg = pool[N : N + b]
        petals = [
            pool[N + b + i * ell : N + b + (i + 1) * ell]
            for i in range(M)
        ]
        source_labels = rng.sample(range(1, q), M)
        touched = [z for petal in petals[:t] for z in petal]
        untouched = petals[t:]
        rows = ell - 1
        all_split = set()
        all_primitive = set()
        all_guarded = set()
        fixed = []

        for required in combinations(bg, u):
            nodes = touched + list(required)
            labels = [source_labels[i] for i in range(t) for _ in petals[i]] + [0] * u
            mu, weights = rational_moments(nodes, labels, d + rows)
            random_mu = random_full_rank_moments(d, rows)
            split = primitive = guarded = 0
            random_split = random_primitive = 0
            for roots in combinations(core, d):
                poly = locator(roots)
                in_kernel, is_primitive = kernel_and_primitive(poly, roots, mu, rows)
                random_in_kernel, random_is_primitive = kernel_and_primitive(
                    poly, roots, random_mu, rows
                )
                random_split += random_in_kernel
                random_primitive += random_in_kernel and random_is_primitive
                if not in_kernel:
                    continue
                split += 1
                all_split.add(roots)
                if not is_primitive:
                    continue
                primitive += 1
                all_primitive.add(roots)
                touched_values = [peval(poly, z) for z in nodes]

                def numerator_at(y):
                    parent = 1
                    cauchy = 0
                    for z, weight, value in zip(nodes, weights, touched_values):
                        parent = parent * (y - z) % q
                        if weight:
                            cauchy += weight * value * pow(y - z, -1, q)
                    return parent * cauchy % q

                bad = False
                for petal_index, petal in enumerate(untouched, start=t):
                    label = source_labels[petal_index]
                    for y in petal:
                        if (numerator_at(y) - label * peval(poly, y)) % q == 0:
                            bad = True
                            break
                    if bad:
                        break
                if bad:
                    continue
                guarded += 1
                all_guarded.add(roots)
            fixed.append({
                "required": list(required),
                "split": split,
                "primitive": primitive,
                "guarded": guarded,
                "random_split": random_split,
                "random_primitive": random_primitive,
            })

        return {
            "union_split": len(all_split),
            "union_primitive": len(all_primitive),
            "union_guarded": len(all_guarded),
            "fixed": fixed,
        }

    records = []
    requested = job["requested"]
    while len(records) < requested and time.monotonic() < deadline:
        records.append(one_config())
    mean = comb(spec["N"], spec["d"]) / (q ** (spec["ell"] - 1))

    def union_values(key):
        return [record[key] for record in records]

    return {
        "id": spec["id"],
        "worker": job["worker"],
        "requested": requested,
        "completed": len(records),
        "mean_ambient": mean,
        "records": records,
        "union_max": {key: max(union_values(key), default=0) for key in (
            "union_split", "union_primitive", "union_guarded"
        )},
    }


@app.local_entrypoint()
def main() -> None:
    jobs = []
    for spec_index, spec in enumerate(SPECS):
        for worker in range(2):
            jobs.append(
                {
                    "spec": spec,
                    "worker": worker,
                    "seed": 20260810 + 1000 * spec_index + worker,
                    "requested": (spec["configs"] + 1) // 2,
                }
            )
    results = list(run_job.map(jobs, order_outputs=False))
    by_id = {}
    for result in results:
        cell = by_id.setdefault(
            result["id"],
            {"workers": 0, "requested": 0, "completed": 0, "records": [], "mean_ambient": result["mean_ambient"]},
        )
        cell["workers"] += 1
        cell["requested"] += result["requested"]
        cell["completed"] += result["completed"]
        cell["records"].extend(result["records"])

    for spec in SPECS:
        cell = by_id[spec["id"]]
        records = cell["records"]
        fixed_records = [
            chart
            for record in records
            for chart in record["fixed"]
        ]
        cell["parameters"] = spec
        cell["fixed_charts"] = len(fixed_records)
        cell["fixed_max"] = {
            key: max((chart[key] for chart in fixed_records), default=0)
            for key in ("split", "primitive", "guarded", "random_split", "random_primitive")
        }
        cell["fixed_mean"] = {
            key: (sum(chart[key] for chart in fixed_records) / len(fixed_records) if fixed_records else None)
            for key in ("split", "primitive", "guarded", "random_split", "random_primitive")
        }
        cell["union_max"] = {
            key: max((record[key] for record in records), default=0)
            for key in ("union_split", "union_primitive", "union_guarded")
        }
        cell["union_mean"] = {
            key: (sum(record[key] for record in records) / len(records) if records else None)
            for key in ("union_split", "union_primitive", "union_guarded")
        }
        denominator = 1.0 + cell["mean_ambient"]
        cell["excess_max"] = {
            "actual": cell["fixed_max"]["primitive"] / denominator,
            "guarded": cell["fixed_max"]["guarded"] / denominator,
            "random": cell["fixed_max"]["random_primitive"] / denominator,
        }
        ratios = [
            chart["guarded"] / chart["primitive"]
            for chart in fixed_records
            if chart["primitive"]
        ]
        ratios.sort()
        cell["median_guard_fraction"] = ratios[len(ratios) // 2] if ratios else None

    print("FPC5_HANKEL_GUARD_RESULT=" + json.dumps({
        "schema": "fpc5-hankel-guard-probe-v1",
        "cells": by_id,
    }, sort_keys=True))
