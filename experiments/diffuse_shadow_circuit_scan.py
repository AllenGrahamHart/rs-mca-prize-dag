#!/usr/bin/env python3
"""Small finite-field stress tests for the diffuse triple-shadow premise.

This is not a verifier for ``diffuse_triple_shadow``.  It is an adversarial
small-model search for the failure mode that would damage the amber implication

    diffuse_triple_shadow -> hankel_slope_large_sieve.

Model tested:

* H = mu_n in F_p.
* A degree-j locator is the error set E; its agreement set is H \\ E.
* A slope/support incidence (Z, E) contributes the t Hankel equations
  M_Z ell_E = 0, where M_Z = Z0 M_u + Z1 M_v.
* A "first stagnating" certificate is modeled as a minimal family of m
  incidences whose t*m rows are linearly dependent before the ambient cap.

For every minimal dependent family found, the script checks the triple-covered
agreement shadow.  A family with triple-shadow size < k+1 is recorded as a
potential falsifier of the Vandermonde/triple-shadow reduction.  Families with
some triple core of size >= k+1 are tangent-core controls; m >= 4 families
with no such core but triple shadow >= k+1 are the diffuse residue.

The script is deterministic, pure Python, and checkpointed after each block so
partial results survive a timeout.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import time
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "experiments" / "amber_stress" / "diffuse_shadow_circuit_results.json"


CONFIGS = [
    {"name": "F13_mu12_t3_j4", "p": 13, "n": 12, "t": 3, "j": 4, "trials": 25000, "m_values": [3, 4]},
    {"name": "F17_mu8_t2_j3", "p": 17, "n": 8, "t": 2, "j": 3, "trials": 25000, "m_values": [3, 4, 5]},
    {"name": "F17_mu16_t3_j5", "p": 17, "n": 16, "t": 3, "j": 5, "trials": 12000, "m_values": [3, 4, 5]},
]


def inv_mod(a: int, p: int) -> int:
    return pow(a % p, p - 2, p)


def rank_mod(rows: list[list[int]], p: int) -> int:
    mat = [row[:] for row in rows if any(x % p for x in row)]
    if not mat:
        return 0
    n_rows = len(mat)
    n_cols = len(mat[0])
    rank = 0
    for col in range(n_cols):
        piv = None
        for r in range(rank, n_rows):
            if mat[r][col] % p:
                piv = r
                break
        if piv is None:
            continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        scale = inv_mod(mat[rank][col], p)
        mat[rank] = [(x * scale) % p for x in mat[rank]]
        for r in range(n_rows):
            if r != rank and mat[r][col] % p:
                factor = mat[r][col]
                mat[r] = [(a - factor * b) % p for a, b in zip(mat[r], mat[rank])]
        rank += 1
        if rank == n_rows:
            break
    return rank


def subgroup_generator(p: int, n: int) -> int:
    for g in range(2, p):
        seen = {pow(g, i, p) for i in range(n)}
        if len(seen) == n and pow(g, n, p) == 1:
            return g
    raise ValueError(f"no order-{n} generator found in F_{p}")


def poly_mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai % p == 0:
            continue
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return out


def locator_coeffs(error_set: tuple[int, ...], H: list[int], p: int) -> list[int]:
    poly = [1]
    for idx in error_set:
        poly = poly_mul(poly, [(-H[idx]) % p, 1], p)
    return poly


class CircuitModel:
    def __init__(self, p: int, n: int, t: int, j: int):
        self.p = p
        self.n = n
        self.t = t
        self.j = j
        self.k = n - j - t
        self.A = n - j
        self.window = t + j
        if self.k <= 0:
            raise ValueError("requires k = n - j - t > 0")
        gen = subgroup_generator(p, n)
        self.H = [pow(gen, i, p) for i in range(n)]
        self.error_sets = list(itertools.combinations(range(n), j))
        self.locators = [locator_coeffs(E, self.H, p) for E in self.error_sets]
        self.slopes = [(1, z) for z in range(p)] + [(0, 1)]
        self._row_cache: dict[tuple[int, int], list[list[int]]] = {}

    def rows_for(self, slope_idx: int, error_idx: int) -> list[list[int]]:
        key = (slope_idx, error_idx)
        cached = self._row_cache.get(key)
        if cached is not None:
            return cached
        z0, z1 = self.slopes[slope_idx]
        ell = self.locators[error_idx]
        rows: list[list[int]] = []
        for i in range(self.t):
            row = [0] * (2 * self.window)
            for c, coef in enumerate(ell):
                row[i + c] = (row[i + c] + z0 * coef) % self.p
                row[self.window + i + c] = (row[self.window + i + c] + z1 * coef) % self.p
            rows.append(row)
        self._row_cache[key] = rows
        return rows

    def family_rank(self, family: list[tuple[int, int]]) -> int:
        rows: list[list[int]] = []
        for slope_idx, error_idx in family:
            rows.extend(self.rows_for(slope_idx, error_idx))
        return rank_mod(rows, self.p)

    def is_minimal_dependent(self, family: list[tuple[int, int]]) -> tuple[bool, int]:
        m = len(family)
        full = m * self.t
        if full > 2 * self.window:
            return False, self.family_rank(family)
        rank = self.family_rank(family)
        if rank >= full:
            return False, rank
        for subset in itertools.combinations(range(m), m - 1):
            subfamily = [family[i] for i in subset]
            if self.family_rank(subfamily) < (m - 1) * self.t:
                return False, rank
        return True, rank

    def agreement_set(self, error_idx: int) -> set[int]:
        return set(range(self.n)) - set(self.error_sets[error_idx])

    def classify(self, family: list[tuple[int, int]]) -> dict:
        agreements = [self.agreement_set(error_idx) for _, error_idx in family]
        cover_counts = [
            sum(point in agreement for agreement in agreements)
            for point in range(self.n)
        ]
        triple_shadow = {idx for idx, count in enumerate(cover_counts) if count >= 3}
        max_triple_core = 0
        for a, b, c in itertools.combinations(range(len(agreements)), 3):
            max_triple_core = max(max_triple_core, len(agreements[a] & agreements[b] & agreements[c]))
        return {
            "triple_shadow_size": len(triple_shadow),
            "max_triple_core": max_triple_core,
            "kind": (
                "shadow_violation"
                if len(triple_shadow) < self.k + 1
                else "tangent_core"
                if max_triple_core >= self.k + 1
                else "diffuse"
            ),
        }

    def serialise_family(self, family: list[tuple[int, int]]) -> list[dict]:
        out = []
        for slope_idx, error_idx in family:
            z0, z1 = self.slopes[slope_idx]
            errors = list(self.error_sets[error_idx])
            agreement = sorted(set(range(self.n)) - set(errors))
            out.append(
                {
                    "slope": [z0, z1],
                    "error_indices": errors,
                    "agreement_indices": agreement,
                }
            )
        return out

    def tangent_core_control(self, m: int) -> dict:
        core = set(range(self.k + 1))
        outside = [idx for idx in range(self.n) if idx not in core]
        candidate_errors = [tuple(c) for c in itertools.combinations(outside, self.j)]
        if len(candidate_errors) < m or len(self.slopes) < m:
            return {"available": False}
        error_index = {E: i for i, E in enumerate(self.error_sets)}
        family = [(i, error_index[candidate_errors[i]]) for i in range(m)]
        minimal, rank = self.is_minimal_dependent(family)
        cls = self.classify(family)
        return {
            "available": True,
            "minimal_dependent": minimal,
            "rank": rank,
            "full_rank": m * self.t,
            "classification": cls,
            "family": self.serialise_family(family),
        }


def checkpoint(payload: dict) -> None:
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def scan_config(config: dict, seed: int, deadline: float) -> dict:
    model = CircuitModel(config["p"], config["n"], config["t"], config["j"])
    rng = random.Random(seed)
    result = {
        "config": config,
        "field": f"F_{model.p}",
        "n": model.n,
        "k": model.k,
        "t": model.t,
        "j": model.j,
        "agreement_size": model.A,
        "k_plus_1": model.k + 1,
        "num_error_sets": len(model.error_sets),
        "num_projective_slopes": len(model.slopes),
        "m_results": [],
    }

    for m in config["m_values"]:
        block = {
            "m": m,
            "trials_requested": config["trials"],
            "trials_completed": 0,
            "minimal_dependencies": 0,
            "shadow_violations": 0,
            "tangent_core": 0,
            "diffuse": 0,
            "rank_deficient_not_minimal": 0,
            "examples": {},
            "tangent_core_control": model.tangent_core_control(m),
        }
        if m * model.t > 2 * model.window:
            block["skipped"] = "ambient dimension cap makes every family dependent"
            result["m_results"].append(block)
            continue
        for trial in range(config["trials"]):
            if time.monotonic() >= deadline:
                block["stopped_by_time_guard"] = True
                break
            slope_idxs = rng.sample(range(len(model.slopes)), m)
            family = [
                (slope_idxs[i], rng.randrange(len(model.error_sets)))
                for i in range(m)
            ]
            minimal, rank = model.is_minimal_dependent(family)
            block["trials_completed"] += 1
            if not minimal:
                if rank < m * model.t:
                    block["rank_deficient_not_minimal"] += 1
                continue
            block["minimal_dependencies"] += 1
            cls = model.classify(family)
            kind = cls["kind"]
            block[kind] += 1
            block["examples"].setdefault(
                kind,
                {
                    "rank": rank,
                    "full_rank": m * model.t,
                    "classification": cls,
                    "family": model.serialise_family(family),
                },
            )
            if kind == "shadow_violation":
                break
        result["m_results"].append(block)
        if block["shadow_violations"]:
            break
    return result


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=55.0)
    parser.add_argument("--seed", type=int, default=20260706)
    args = parser.parse_args(list(argv) if argv is not None else None)

    started = time.monotonic()
    deadline = started + args.time_limit
    payload = {
        "started_at_unix": time.time(),
        "time_limit_seconds": args.time_limit,
        "seed": args.seed,
        "configs": [],
        "summary": {
            "configs_completed": 0,
            "minimal_dependencies": 0,
            "shadow_violations": 0,
            "tangent_core": 0,
            "diffuse": 0,
        },
    }
    checkpoint(payload)

    for idx, config in enumerate(CONFIGS):
        if time.monotonic() >= deadline:
            payload["stopped_by_time_guard"] = True
            break
        result = scan_config(config, args.seed + 1009 * idx, deadline)
        payload["configs"].append(result)
        payload["summary"]["configs_completed"] += 1
        for block in result["m_results"]:
            payload["summary"]["minimal_dependencies"] += block.get("minimal_dependencies", 0)
            payload["summary"]["shadow_violations"] += block.get("shadow_violations", 0)
            payload["summary"]["tangent_core"] += block.get("tangent_core", 0)
            payload["summary"]["diffuse"] += block.get("diffuse", 0)
        checkpoint(payload)
        if payload["summary"]["shadow_violations"]:
            break

    payload["finished_at_unix"] = time.time()
    payload["wall_seconds"] = round(time.monotonic() - started, 6)
    checkpoint(payload)
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 1 if payload["summary"]["shadow_violations"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
