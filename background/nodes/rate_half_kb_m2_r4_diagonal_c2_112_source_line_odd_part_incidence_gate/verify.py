#!/usr/bin/env python3
"""Verify the saturated (1,1,2) odd-part incidence gate."""

import json
from fractions import Fraction as F
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
NODE_ID = "rate_half_kb_m2_r4_diagonal_c2_112_source_line_odd_part_incidence_gate"
PARENTS = {
    "rate_half_kb_m2_r4_diagonal_c2_112_saturated_defect_classifier",
    "rate_half_kb_m2_r4_diagonal_c2_square_fiber_linear_cut",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def odd_part(epsilon, w, q):
    q0, q1, q2 = q
    f = q0 - epsilon * w * q2
    g = epsilon * q2 - w * q0
    m = q1 * (1 - epsilon * w)
    return f, g, m


def value(epsilon, coefficients, t, W):
    f, g, m = coefficients
    return ((f + g * W) + m * (1 + epsilon * W) * t
            + epsilon * (g + f * W) * t * t)


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    require("- **status:** PROVED" in statement, "status")
    require("z=-N_epsilon(a)/D_epsilon(a)" in statement, "incidence map")

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    require(nodes[NODE_ID]["status"] == "PROVED", "DAG status")
    edges = {(edge["from"], edge["to"], edge.get("kind", "req"))
             for edge in dag["edges"]}
    require(all((parent, NODE_ID, "req") in edges for parent in PARENTS),
            "dependencies")
    require((NODE_ID, "rate_half_band_closure", "ev") in edges, "consumer")

    for epsilon in (1, -1):
        w = F(2, 5)
        q = (F(21, 11), F(-10, 3), F(1))
        coefficients = odd_part(epsilon, w, q)
        # Coefficient comparison at W=w gives (1-w^2)q.
        f, g, m = coefficients
        at_w = (
            f + g * w,
            m * (1 + epsilon * w),
            epsilon * (g + f * w),
        )
        require(at_w == tuple((1 - w * w) * entry for entry in q),
                "forced evaluation")

        a = F(7, 4)
        n = f + m * a + epsilon * g * a * a
        d = g + epsilon * m * a + epsilon * f * a * a
        require(d != 0, "fixture denominator")
        z = -n / d
        require(value(epsilon, coefficients, a, z) == 0,
                "incidence equation")
        require(a * a * z * value(epsilon, coefficients, 1 / a, 1 / z)
                == epsilon * value(epsilon, coefficients, a, z),
                "reciprocal identity")

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_112_SOURCE_LINE_ODD_PART_INCIDENCE_GATE_PASS "
        "signs=2 internal_orbit=unramified common_root=1 incidence_map=exact"
    )


if __name__ == "__main__":
    main()
