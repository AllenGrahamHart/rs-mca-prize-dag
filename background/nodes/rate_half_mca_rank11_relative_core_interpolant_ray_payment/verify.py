#!/usr/bin/env python3
"""Verify the relative core-interpolant and one-ray payment."""

from __future__ import annotations

import copy
import hashlib
import json
from math import comb
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "3b4b70627535065aeae69d5dfcf0bea11f067557e3512f23571a11eb41b04454"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def eval_poly(coefficients: list[int], value: int, field: int) -> int:
    out = 0
    for coefficient in reversed(coefficients):
        out = (out * value + coefficient) % field
    return out


def validate(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    require(
        data.get("schema")
        == "rate-half-mca-rank11-relative-core-interpolant-ray-payment-v1",
        "schema",
    )
    require(
        data.get("dependencies")
        == ["rate_half_mca_rank11_global_core_rankdrop_highcomplexity_router"],
        "dependencies",
    )
    row = data.get("official")
    residual = data.get("residual_range")
    ray = data.get("ray")
    require(all(isinstance(x, dict) for x in (row, residual, ray)), "sections")
    require(
        tuple(row.get(key) for key in ("n", "K", "m", "R", "d", "t"))
        == (2097152, 1048576, 1116048, 1048576, 67472, 981104),
        "row",
    )
    require(row["n"] == row["R"] + row["K"], "n")
    require(row["m"] == row["d"] + row["K"], "m")
    require(row["t"] == row["R"] - row["d"], "t")
    k_min = residual.get("K_min")
    require((k_min, residual.get("K_max")) == (10, row["K"]), "range")
    n_min, m_min = row["R"] + k_min, row["d"] + k_min
    require((residual.get("n_at_min"), residual.get("m_at_min")) == (n_min, m_min), "minimum row")
    core = 31 * n_min // m_min
    extra = (31 * n_min - 32 * m_min) // m_min
    require(core == residual.get("core_compatible_cap") == 481, "core cap")
    require(extra == residual.get("extra_core_compatible_cap") == 449, "extra cap")

    affine_block = row["t"] + 1
    affine_charge = row["n"] * affine_block
    pair_charge = 31 * comb(row["n"], 2)
    ray_cap = affine_charge + pair_charge
    require(ray.get("slope_degree") == 31, "degree")
    require(ray.get("affine_block_cap") == affine_block == 981105, "affine block")
    require(ray.get("uniform_affine_block_count_cap") == row["n"], "block count")
    require(ray.get("uniform_affine_charge") == affine_charge, "affine charge")
    require(ray.get("uniform_heterogeneous_pair_charge") == pair_charge, "pair charge")
    require(ray.get("uniform_ray_cap") == ray_cap == 70227214729216, "ray cap")
    require(ray.get("core_plus_ray") == core + ray_cap == 70227214729697, "combined")
    require(ray.get("slack") == row["budget"] - core - ray_cap > 0, "slack")

    toy = data.get("toy")
    require(isinstance(toy, dict) and toy.get("field") == 17, "toy")
    polynomials = toy.get("different_clone_polynomials")
    require(polynomials == [[1, 1], [2, 1]], "toy polynomials")
    roots = sum(
        eval_poly(polynomials[0], x, 17) == eval_poly(polynomials[1], x, 17)
        for x in range(17)
    )
    require(roots == toy.get("collision_roots") == 0, "toy roots")
    require(toy.get("maximum_degree") == 31, "toy degree")
    require("No union-of-rays" in str(data.get("nonclaim")), "nonclaim")
    return {"core": core, "ray": ray_cap, "slack": ray["slack"]}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["residual_range"].__setitem__("K_min", 9),
        lambda item: item["residual_range"].__setitem__("core_compatible_cap", 480),
        lambda item: item["ray"].__setitem__("uniform_affine_block_count_cap", 2),
        lambda item: item["ray"].__setitem__("uniform_ray_cap", 1),
        lambda item: item["ray"].__setitem__("slack", 1),
        lambda item: item["toy"].__setitem__("collision_roots", 1),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_RELATIVE_CORE_INTERPOLANT_RAY_PAYMENT_PASS "
        f"core={result['core']} ray={result['ray']} slack={result['slack']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
