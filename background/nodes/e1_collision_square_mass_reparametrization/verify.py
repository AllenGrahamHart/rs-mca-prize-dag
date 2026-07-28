#!/usr/bin/env python3
"""Verify the corrected E1 square-mass reparametrization."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NODE = "e1_collision_square_mass_reparametrization"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def class_vector_witness(h: int, ell: int, a: int, b: int):
    """Construct two valid class vectors and a common full-pair set."""
    assert b % 2 == 0
    t0 = a + b // 2
    r = (ell - t0) % 2
    t = t0 + r
    u = (ell - t) // 2

    x = [0] * h
    y = [0] * h
    cursor = 0
    for _ in range(a):
        x[cursor], y[cursor] = 1, -1
        cursor += 1
    for _ in range(b // 2):
        x[cursor] = 1
        cursor += 1
    for _ in range(b // 2):
        y[cursor] = 1
        cursor += 1
    for _ in range(r):
        x[cursor] = y[cursor] = 1
        cursor += 1

    full_pairs = tuple(range(cursor, cursor + u))
    assert cursor + u <= h
    return x, y, full_pairs


def first_not_excluded(exponent: int, even: bool) -> int:
    candidates = range(2 if even else 1, 400, 2 if even else 1)
    return next(v for v in candidates if v**exponent >= 2**250)


def main() -> None:
    checks = 0

    params = ((256, 128, 65, 260), (256, 128, 33, 132),
              (512, 256, 33, 132))
    for _N, h, ell, expected_max in params:
        T = min(ell, 2 * h - ell)
        assert 4 * T == expected_max
        for t in range(ell % 2, T + 1, 2):
            u = (ell - t) // 2
            assert 0 <= u <= h - t
            checks += 1
        checks += 1

    # Exact norm floors, with no floating-point logarithms.
    assert first_not_excluded(64, even=True) == 16
    assert first_not_excluded(64, even=False) == 15
    assert first_not_excluded(128, even=True) == 4
    assert first_not_excluded(128, even=False) == 4
    checks += 4

    splits = ((3, 4), (2, 8), (1, 12), (0, 16))
    for ell in (33, 65):
        for a, b in splits:
            x, y, full_pairs = class_vector_witness(128, ell, a, b)
            tx = sum(v != 0 for v in x)
            ty = sum(v != 0 for v in y)
            u = len(full_pairs)
            assert tx == ty and tx + 2 * u == ell
            assert u <= 128 - tx
            diff = [vx - vy for vx, vy in zip(x, y)]
            assert sum(abs(v) == 2 for v in diff) == a
            assert sum(abs(v) == 1 for v in diff) == b
            assert sum(v * v for v in diff) == 16
            assert sum(abs(v) for v in diff) == 2 * a + b
            assert x != y
            checks += 9

    # The all-even S=16 split is below the divided norm threshold.
    assert 4**64 < 2**250
    assert 16**64 > 2**250
    checks += 2

    pins = json.loads((Path(__file__).with_name("source_pin.json")).read_text())
    for file_key, hash_key in (
        ("dependency_statement_file", "dependency_statement_sha256"),
        ("dependency_proof_file", "dependency_proof_sha256"),
        ("class_count_proof_file", "class_count_proof_sha256"),
    ):
        assert sha256(ROOT / pins[file_key]) == pins[hash_key]
        checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"])
             for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in ("acl_count", "e1_prime_field_l2_norm_collision_radius"):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    for consumer in ("e1_official_prime_exception_control",
                     "unsafe_crossing_family_instantiation"):
        assert (NODE, consumer, "ev") in edges
        assert (NODE, consumer, "req") not in edges
        checks += 2

    print(
        "E1_COLLISION_SQUARE_MASS_REPARAMETRIZATION_PASS "
        f"S16_splits={splits} official_params={len(params)} checks={checks}"
    )


if __name__ == "__main__":
    main()
