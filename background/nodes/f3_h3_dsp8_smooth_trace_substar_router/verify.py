#!/usr/bin/env python3
"""Verify the DSP8 smooth-trace substar router."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_h3_dsp8_smooth_trace_substar_router"
DEPENDENCIES = {
    "f3_h3_dsp8_joint_star_depth_pareto_compiler",
    "f3_h3_dsp8_unit_trace_elliptic_curve_router",
}
CONSUMERS = {
    "f3_h3_dsp8_correlation_bound",
    "f3_h3_official_order_template_survivor",
}


def prime_factors(value: int) -> tuple[int, ...]:
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return tuple(factors)


def nodal_degree_check(prime: int, order: int) -> tuple[int, int]:
    primitive = next(
        candidate
        for candidate in range(2, prime)
        if all(
            pow(candidate, (prime - 1) // factor, prime) != 1
            for factor in prime_factors(prime - 1)
        )
    )
    generator = pow(primitive, (prime - 1) // order, prime)
    subgroup = [pow(generator, exponent, prime) for exponent in range(order)]
    fibers: dict[int, list[int]] = defaultdict(list)
    for left_index, left in enumerate(subgroup):
        if left == 1:
            continue
        for right in subgroup[left_index:]:
            if right == 1:
                continue
            target = (1 - left) * (1 - right) % prime
            fibers[target].append(left * right % prime)

    maximum = 0
    rich_maximum = 0
    for target, parameters in fibers.items():
        assert len(parameters) == len(set(parameters))
        degrees = {parameter: 0 for parameter in parameters}
        for index, left in enumerate(parameters):
            for right in parameters[index + 1 :]:
                trace = (1 + left + right - target) % prime
                if (trace**3 - 27 * left * right) % prime == 0:
                    degrees[left] += 1
                    degrees[right] += 1
        fiber_maximum = max(degrees.values(), default=0)
        maximum = max(maximum, fiber_maximum)
        if 2 * len(parameters) >= 25:
            rich_maximum = max(rich_maximum, fiber_maximum)
        assert fiber_maximum <= 3
    return maximum, rich_maximum


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes[NODE]["status"] == "PROVED"
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    for dependency in DEPENDENCIES:
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}


def main() -> None:
    # The two exact controls make the cubic degree bound sharp.
    controls = [nodal_degree_check(97, 32), nodal_degree_check(193, 64)]
    assert controls[0][0] == 3
    assert controls[1] == (3, 3)

    star_degrees = {
        10: (5, 3),
        11: (5, 3),
        12: (6, 4),
        13: (6, 4),
        14: (7, 5),
        15: (7, 5),
        16: (8, 6),
    }
    smooth = {key: tuple(max(value - 3, 0) for value in pair)
              for key, pair in star_degrees.items()}
    assert smooth[10] == (2, 0)
    assert smooth[12] == (3, 1)
    assert smooth[14] == (4, 2)
    assert smooth[16] == (5, 3)
    packet_check()
    print(
        "F3_H3_DSP8_SMOOTH_TRACE_SUBSTAR_ROUTER_PASS "
        "nodal_degree=3 smooth_corner=5/3 controls=2"
    )


if __name__ == "__main__":
    main()
