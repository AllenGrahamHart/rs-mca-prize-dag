#!/usr/bin/env python3
"""Verify the exceptional quadratic-moment pin."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_ca_hankel_a1_core_one_exceptional_only_quadratic_moment_pin"
DEPENDENCY = (
    "rate_half_ca_hankel_a1_core_one_exceptional_only_kernel_plane_transversality"
)
CONSUMER = "rate_half_band_closure"


def moments(points: list[int], weights: list[int], count: int, p: int) -> list[int]:
    return [
        sum(weight * pow(point, degree, p) for point, weight in zip(points, weights)) % p
        for degree in range(count)
    ]


def square_coefficients(coefficients: list[int], p: int) -> list[int]:
    result = [0] * (2 * len(coefficients) - 1)
    for i, left in enumerate(coefficients):
        for j, right in enumerate(coefficients):
            result[i + j] = (result[i + j] + left * right) % p
    return result


def theta_from_convolution(
    coefficients: list[int], sequence: list[int], shift: int, p: int
) -> int:
    square = square_coefficients(coefficients, p)
    return sum(value * sequence[index + shift] for index, value in enumerate(square)) % p


def evaluate(coefficients: list[int], point: int, p: int) -> int:
    return sum(value * pow(point, degree, p) for degree, value in enumerate(coefficients)) % p


def profile_check() -> None:
    profiles = 0
    for e in range(3, 256):
        r = 2 * e + 1
        largest_index = 2 * (r - 1) + 2
        assert largest_index == 2 * r
        assert largest_index == (r + r)
        profiles += 1
    assert profiles == 253


def source_fixture() -> None:
    p = 101
    # A(X)=X; the source at x=0 is killed by A(X)^2.
    coefficients = [0, 1]
    points = [0, 1, 2, 3]
    weights = [77, 18, -9, 2]
    sequence = moments(points, weights, 5, p)

    theta = [theta_from_convolution(coefficients, sequence, shift, p) for shift in range(3)]
    assert theta == [0, 0, 36]

    source_theta = [
        sum(
            weight * pow(point, shift, p) * pow(evaluate(coefficients, point, p), 2, p)
            for point, weight in zip(points, weights)
        )
        % p
        for shift in range(3)
    ]
    assert source_theta == theta

    without_roots = [(point, weight) for point, weight in zip(points, weights) if point != 0]
    deleted_theta = [
        sum(
            weight * pow(point, shift, p) * pow(evaluate(coefficients, point, p), 2, p)
            for point, weight in without_roots
        )
        % p
        for shift in range(3)
    ]
    assert deleted_theta == theta

    broken_weights = weights[:]
    broken_weights[1] += 1
    broken_sequence = moments(points, broken_weights, 5, p)
    assert theta_from_convolution(coefficients, broken_sequence, 0, p) != 0


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[DEPENDENCY]["status"] == "PROVED"
    assert (DEPENDENCY, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges

    here = ROOT / "background" / "nodes" / NODE
    statement = (here / "statement.md").read_text()
    proof = (here / "proof.md").read_text()
    for marker in (
        "Theta_0=0",
        "Theta_2!=0",
        "omega_x x^s A(x)^2",
        "not asserted to equal the original error values",
    ):
        assert marker in statement
    for marker in (
        "largest moment index used is `2r`",
        "Contracting by the fixed core factor",
        "valid in every characteristic",
    ):
        assert marker in proof


def main() -> None:
    profile_check()
    source_fixture()
    packet_check()
    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_EXCEPTIONAL_ONLY_QUADRATIC_MOMENT_PIN_PASS "
        "profiles=253 theta=0,0,36 source=1 root_delete=1 mutation=1"
    )


if __name__ == "__main__":
    main()
