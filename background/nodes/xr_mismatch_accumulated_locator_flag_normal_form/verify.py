#!/usr/bin/env python3
"""Verify the XR accumulated-locator flag normal form."""

from __future__ import annotations

import json
from pathlib import Path


P = 29
N = 20
K = 4
A = 5
H = A - K
ROOT = Path(__file__).resolve().parents[3]
NODE = "xr_mismatch_accumulated_locator_flag_normal_form"
PARENTS = {
    "xr_tangent_mismatch_full_external_zero_canonicalization",
    "xr_mismatch_chart_nongeneric_joint_support_equivalence",
    "xr_mismatch_nongeneric_invariant_excess_descent",
}
CONSUMER = "xr_tangent_support_mismatch_bridge"


def trim(poly: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    out = [coefficient % P for coefficient in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
            for index in range(size)
        ]
    )


def neg(poly: tuple[int, ...]) -> tuple[int, ...]:
    return trim([-coefficient for coefficient in poly])


def sub(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return add(left, neg(right))


def scale(scalar: int, poly: tuple[int, ...]) -> tuple[int, ...]:
    return trim([scalar * coefficient for coefficient in poly])


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    return trim(out)


def evaluate(poly: tuple[int, ...], x: int) -> int:
    return sum(c * pow(x, j, P) for j, c in enumerate(poly)) % P


def divide_exact(
    numerator: tuple[int, ...], denominator: tuple[int, ...]
) -> tuple[int, ...] | None:
    work = list(trim(numerator))
    denominator = trim(denominator)
    quotient = [0] * max(1, len(work) - len(denominator) + 1)
    inverse = pow(denominator[-1], P - 2, P)
    while len(work) >= len(denominator) and any(work):
        shift = len(work) - len(denominator)
        coefficient = work[-1] * inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            work[index + shift] = (work[index + shift] - coefficient * value) % P
        work = list(trim(work))
    return trim(quotient) if not any(work) else None


def locator(points: set[int]) -> tuple[int, ...]:
    result = (1,)
    for point in sorted(points):
        result = multiply(result, ((-point) % P, 1))
    return result


def line(pair: tuple[tuple[int, ...], tuple[int, ...]], slope: int) -> tuple[int, ...]:
    return add(pair[0], scale(slope, pair[1]))


def support_intersection_check(supports: list[set[int]]) -> None:
    assert all(len(support) == A for support in supports)
    for i in range(len(supports)):
        for j in range(i + 1, len(supports)):
            assert len(supports[i] & supports[j]) <= K - 1


def fixture(alpha: int, slope: int) -> None:
    domain = set(range(N))
    d1 = set(range(15))
    r0 = {0, 1, 2, 3}
    d2 = set(range(4, 15))
    r1 = {4, 5, 6}
    extra = 7
    z0 = {alpha}
    z1 = {0}
    assert z0 <= domain - d1
    assert z1 <= d1 - d2
    assert not z0 & z1

    p0 = locator(z0)
    p1 = locator(z1)
    l0 = (1,)
    l1 = p0
    l2 = multiply(p0, p1)
    assert l2 == locator(z0 | z1)

    base = ((2, 3), (5, 1))
    g00, g10 = (1,), (0,)
    g01, g11 = (1,), (0,)
    pair1 = (
        add(base[0], multiply(l1, g00)),
        add(base[1], multiply(l1, g10)),
    )
    pair2 = (
        add(pair1[0], multiply(l2, g01)),
        add(pair1[1], multiply(l2, g11)),
    )
    assert all(len(poly) - 1 < K for pair in (base, pair1, pair2) for poly in pair)

    q1 = multiply(p1, add(g01, scale(slope, g11)))
    q0 = multiply(p0, add(add(g00, scale(slope, g10)), q1))
    witness = add(line(base, slope), q0)
    assert sub(witness, line(pair1, slope)) == multiply(l1, q1)
    assert sub(witness, line(pair2, slope)) == (0,)
    assert divide_exact(sub(witness, line(pair1, slope)), l1) == q1
    assert divide_exact(sub(witness, line(pair2, slope)), l2) == (0,)

    # Build the normalized residual at stage one, then lift it to the root.
    residual1: dict[int, tuple[int, int]] = {}
    for x in d1:
        if x in r0:
            residual1[x] = (0, 0)
        elif x in r1:
            residual1[x] = (evaluate(p1, x), 0)
        elif x == extra:
            residual1[x] = ((x - slope) % P, 1)
        else:
            residual1[x] = ((x + 2) % P, 1)
    assert {x for x, value in residual1.items() if value != (0, 0)} == d2

    errors0: dict[int, tuple[int, int]] = {}
    for x in domain:
        if x not in d1:
            errors0[x] = (0, 0)
            continue
        factor = evaluate(p0, x)
        e0, e1 = residual1[x]
        errors0[x] = (factor * (1 + e0) % P, factor * e1 % P)
    assert {x for x, value in errors0.items() if value != (0, 0)} == d1

    received = {
        x: (
            (evaluate(base[0], x) + errors0[x][0]) % P,
            (evaluate(base[1], x) + errors0[x][1]) % P,
        )
        for x in domain
    }
    y0 = set(range(15, 20))
    y1 = z0 | r0
    y2 = z0 | z1 | r1
    supports = [y0, y1, y2]
    support_intersection_check(supports)
    for pair, support in zip((base, pair1, pair2), supports):
        assert all(
            (evaluate(pair[0], x), evaluate(pair[1], x)) == received[x]
            for x in support
        )

    # The selected witness has A agreements at both nonterminal stages.
    root_agreement = {
        x
        for x in domain
        if evaluate(witness, x)
        == (received[x][0] + slope * received[x][1]) % P
    }
    assert len(root_agreement) >= A
    assert z0 | r1 | {extra} <= root_agreement
    stage1_agreement = {
        x
        for x in d1
        if evaluate(q1, x)
        == (residual1[x][0] + slope * residual1[x][1]) % P
    }
    assert z1 | r1 <= stage1_agreement
    assert len(z1 | r1) == A - len(z0)

    # Full external zero sets and prefix divisibility are exact.
    assert {x for x in domain - d1 if evaluate(q0, x) == 0} == z0
    assert {x for x in d1 - d2 if evaluate(q1, x) == 0} == z1
    assert divide_exact(sub(pair1[0], base[0]), l1) is not None
    assert divide_exact(sub(pair2[0], base[0]), l1) is not None
    assert divide_exact(sub(pair2[0], pair1[0]), l2) is not None
    assert len(z0 | z1) <= K - 1

    # Puncturing the shared root prefix preserves the residual low-core cap.
    common_prefix = z0
    assert common_prefix <= y1 and common_prefix <= y2
    assert len((y1 - common_prefix) & (y2 - common_prefix)) <= K - len(common_prefix) - 1

    # Removing the new locator factor destroys the terminal witness identity.
    mutated_pair2 = (add(pair1[0], multiply(l1, g01)), pair1[1])
    assert sub(witness, line(mutated_pair2, slope)) != (0,)


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for parent in PARENTS:
        assert nodes[parent]["status"] == "PROVED"
        assert (parent, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    statement = "".join(
        (ROOT / "background" / "nodes" / NODE / "statement.md")
        .read_text()
        .split()
    )
    for marker in (
        "Omega_j=disjoint_union_(r<j)Z_r",
        "L_j=Lambda_(Omega_j)=product_(r<j)P_r",
        "K_j=K-delta_j",
        "C_i^(j+1)=C_i^j+L_jP_jg_i^j",
        "|Y_(j+1)|=A",
        "L_(s+1)dividesC_i^r-C_i^s",
        "delta_j<=K-1",
        "<=K_s-1",
        "doesnotboundthenumber",
    ):
        assert marker in statement


def main() -> None:
    fixtures = 0
    for alpha in range(15, 20):
        for slope in range(1, 6):
            fixture(alpha, slope)
            fixtures += 1
    packet_check()
    print(
        "XR_MISMATCH_ACCUMULATED_LOCATOR_FLAG_PASS "
        f"fixtures={fixtures} depth=2 mutation=terminal_factor"
    )


if __name__ == "__main__":
    main()
