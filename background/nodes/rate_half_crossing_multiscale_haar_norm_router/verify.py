#!/usr/bin/env python3
"""Replay the crossing multiscale Haar identities and exact route fence."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "rate_half_crossing_multiscale_haar_norm_router"
SUPPLIER = "rate_half_crossing_ideal_galois_multiplicity_exclusion"
CONSUMER = "rate_half_list_adjacent_crossing"


def folds(bits: tuple[int, ...]) -> list[int]:
    current = list(bits)
    energies: list[int] = []
    while len(current) > 1:
        half = len(current) // 2
        energies.append(sum((current[i] - current[i + half]) ** 2 for i in range(half)))
        current = [current[i] + current[i + half] for i in range(half)]
    return energies


def check_haar() -> int:
    checks = 0
    for n in (4, 8, 16):
        for bits in itertools.product((0, 1), repeat=n):
            r = sum(bits)
            lhs = sum(Fraction(e, 2 ** (j + 1)) for j, e in enumerate(folds(bits)))
            assert lhs == Fraction(r * (n - r), n)
            checks += 1
    return checks


def check_window_partition() -> int:
    checks = 0
    for v in range(1, 10):
        w = 2**v
        seen: set[int] = set()
        total = 0
        for j in range(v):
            odd = [t for t in range(1, w) if t % 2 and 2**j * t < w]
            assert len(odd) == 2 ** (v - j - 1)
            block = {2**j * t for t in odd}
            assert not seen.intersection(block)
            seen.update(block)
            total += len(block)
        assert seen == set(range(1, w))
        assert total == w - 1
        checks += 1
    return checks


def all_active_gate(n: int, w: int, p_cap: int) -> bool:
    assert n % (2 * w) == 0
    r = n // 2 - w
    energy = Fraction(r * (n - r), n)
    base = energy / Fraction(w - 1, w)
    d = n // (2 * w)
    return p_cap * base.denominator**d > base.numerator**d


def check_prize_fence() -> int:
    n = 2**41
    cap = 2**256
    verdicts = {}
    for v in range(34, 40):
        verdicts[v] = all_active_gate(n, 2**v, cap)
    assert verdicts == {
        34: False,
        35: False,
        36: False,
        37: False,
        38: True,
        39: True,
    }

    w = 2**37
    r = n // 2 - w
    energy = r * (n - r) // n
    d = n // (2 * w)
    assert d == 8
    assert cap * (w - 1) ** d <= (energy * w) ** d
    w = 2**38
    r = n // 2 - w
    energy = r * (n - r) // n
    d = n // (2 * w)
    assert d == 4
    assert cap * (w - 1) ** d > (energy * w) ** d
    return len(verdicts) + 4


def check_dag() -> int:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    assert nodes[SUPPLIER]["status"] == "PROVED"
    assert nodes[CONSUMER]["status"] == "TARGET"
    assert (SUPPLIER, NODE, "req") in edges
    assert (NODE, CONSUMER, "ev") in edges
    return 5


def main() -> None:
    haar = check_haar()
    windows = check_window_partition()
    fence = check_prize_fence()
    dag = check_dag()
    print(
        "RATE_HALF_CROSSING_MULTISCALE_HAAR_NORM_ROUTER_PASS "
        f"haar={haar} windows={windows} fence={fence} dag={dag}"
    )


if __name__ == "__main__":
    main()
