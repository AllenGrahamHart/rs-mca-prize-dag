#!/usr/bin/env python3
"""Verify the exact unsafe-cell fiber-layout scope counterexample."""

from __future__ import annotations

import json
from math import comb
from pathlib import Path


Q = 2266333732813281563300991037777987502081
N = 1 << 13
K = N // 4
B_STAR = 6
D = 256
PROTH_K = 1705
PROTH_EXP = 120
PROTH_BASE = 3
SELECTED_CLASSES = tuple(range(2, 8))
ROOT = Path(__file__).resolve().parents[3]
NODE_ID = "ww_spending_cell_fiber_layout_counterexample"
W3 = "ww_row_envelope_clause"
ADJACENCY = "list_adjacency_closing"
PLANTED_ARITHMETIC = "list_planted_arithmetic"


def fiber_indices(residue: int, d: int = D) -> set[int]:
    quotient_order = N // d
    return {residue + quotient_order * j for j in range(d)}


def evaluate(
    *,
    q: int = Q,
    d: int = D,
    selected_classes: tuple[int, ...] = SELECTED_CLASSES,
    background_class: int = 1,
    core_class: int = 0,
    proth_base: int = PROTH_BASE,
    rate_denominator: int = 4,
) -> dict[str, bool]:
    k = N // rate_denominator
    b_star = q // (1 << 128)
    proth_shape = q == PROTH_K * (1 << PROTH_EXP) + 1
    proth_hypotheses = PROTH_K % 2 == 1 and PROTH_K < (1 << PROTH_EXP)
    proth_witness = pow(proth_base, (q - 1) // 2, q) == q - 1

    subgroup_ok = (q - 1) % N == 0
    omega = pow(PROTH_BASE, (q - 1) // N, q) if subgroup_ok else 0
    omega_order = subgroup_ok and pow(omega, N, q) == 1 and pow(omega, N // 2, q) == q - 1

    quotient_order = rate_denominator
    while quotient_order <= N and comb(quotient_order - 1, quotient_order // rate_denominator) <= b_star:
        quotient_order *= 2
    first_scale = quotient_order == 8
    ell = N // quotient_order
    sigma = ell - 1
    petal_count = (N - k + 1) // ell
    background_size = (N - k + 1) % ell
    planted_crossing = (N - k + 1) // (b_star + 1) - 1
    staircase_crossing = ell - 1

    valid_d = d > 0 and N % d == 0
    if valid_d:
        core_fiber = fiber_indices(core_class, d)
        zero_fiber = fiber_indices(background_class, d)
        selected = [fiber_indices(item, d) for item in selected_classes]
    else:
        core_fiber, zero_fiber, selected = set(), set(), []

    reserved = [core_fiber, zero_fiber, *selected]
    disjoint_fibers = all(
        not reserved[i].intersection(reserved[j])
        for i in range(len(reserved))
        for j in range(i)
    )

    background = min(zero_fiber) if zero_fiber else -1
    blocked = set().union(*selected) if selected else set()
    blocked.add(background)
    core = set(core_fiber)
    for idx in range(N):
        if len(core) == k - 1:
            break
        if idx not in blocked and idx not in core:
            core.add(idx)

    noncore = set(range(N)) - core
    layout_possible = (
        len(core) == k - 1
        and background in noncore
        and all(points <= noncore - {background} for points in selected)
        and len(noncore - {background}) == petal_count * ell
    )

    petals: list[set[int]] = [set(points) for points in selected]
    if len(petals) == petal_count and layout_possible:
        used = set().union(*petals) if petals else set()
        pool = iter(sorted(noncore - {background} - used))
        for petal in petals:
            while len(petal) < ell:
                petal.add(next(pool))
    partition_ok = (
        len(petals) == petal_count
        and all(len(petal) == ell for petal in petals)
        and all(not petals[i].intersection(petals[j]) for i in range(len(petals)) for j in range(i))
        and set().union(*petals) == noncore - {background}
    ) if petals else False

    if omega_order and valid_d:
        values = [pow(omega, d * item, q) for item in (core_class, background_class, *selected_classes)]
        zc, z0, *zs = values
        try:
            labels = [((z - z0) * pow((z - zc) % q, -1, q)) % q for z in zs]
        except ValueError:
            labels = []
    else:
        zc = z0 = 0
        labels = []

    label_ok = (
        len(labels) == petal_count
        and len(set(labels)) == petal_count
        and all(label != 0 for label in labels)
        and zc != z0
    )

    agreement_lower = (k - 1 - d) + 1 + len(selected_classes) * d
    threshold = k + sigma
    legal_degree = (k - 1 - d) + d == k - 1 and d <= k - 1
    nonplant = label_ok and all(label != 1 for label in labels)
    strict_falsifier = petal_count + 1 > b_star

    return {
        "proth_shape": proth_shape,
        "proth_hypotheses": proth_hypotheses,
        "proth_witness": proth_witness,
        "field_cap": q < (1 << 256),
        "budget": b_star == B_STAR,
        "subgroup": subgroup_ok,
        "omega_order": omega_order,
        "rate": k == K,
        "first_spending_scale": first_scale,
        "spending_decider": staircase_crossing > planted_crossing,
        "cell_shape": ell == 1024 and sigma == 1023 and petal_count == 6 and background_size == 1,
        "valid_defect": valid_d and d <= ell,
        "fiber_capacity": valid_d and N // d >= petal_count + 2,
        "disjoint_fibers": disjoint_fibers,
        "layout_possible": layout_possible,
        "partition": partition_ok,
        "labels": label_ok,
        "legal_degree": legal_degree,
        "agreement": agreement_lower >= threshold,
        "nonplant": nonplant,
        "strict_falsifier": strict_falsifier,
    }


def evaluate_wiring(dag: dict[str, object]) -> dict[str, bool]:
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = dag["edges"]
    w3_statement = nodes.get(W3, {}).get("statement", "")
    counterexample_statement = nodes.get(NODE_ID, {}).get("statement", "")

    def kinds(source: str, target: str) -> list[str]:
        return [
            edge.get("kind", "")
            for edge in edges
            if edge["from"] == source and edge["to"] == target
        ]

    req_out: dict[str, set[str]] = {}
    for edge in edges:
        if edge.get("kind") == "req":
            req_out.setdefault(edge["from"], set()).add(edge["to"])

    reachable = {W3}
    frontier = [W3]
    while frontier:
        source = frontier.pop()
        for target in req_out.get(source, set()):
            if target not in reachable:
                reachable.add(target)
                frontier.append(target)

    return {
        "counterexample_proved": nodes.get(NODE_ID, {}).get("status") == "PROVED",
        "w3_retired_target": nodes.get(W3, {}).get("status") == "TARGET",
        "counterexample_ref_edge": kinds(NODE_ID, W3) == ["ref"],
        "safe_unsafe_scope_pinned": (
            "safe-side official-convention" in w3_statement
            and "globally unsafe spending cell" in w3_statement
            and "not this literal safe-side statement" in w3_statement
            and "but not W3's literal safe-side claim" in counterexample_statement
        ),
        "safe_required": kinds("list_safe", ADJACENCY) == ["req"],
        "unsafe_required": kinds("list_unsafe", ADJACENCY) == ["req"],
        "old_chain_evidence_only": kinds(PLANTED_ARITHMETIC, ADJACENCY) == ["ev"],
        "w3_off_required_prize_path": ADJACENCY not in reachable and "prize" not in reachable,
    }


def main() -> None:
    checks = evaluate()
    checks.update(evaluate_wiring(json.loads((ROOT / "dag.json").read_text())))
    failures = [name for name, passed in checks.items() if not passed]
    if failures:
        raise SystemExit("WW_SPENDING_CELL_FIBER_LAYOUT_COUNTEREXAMPLE_FAIL " + ",".join(failures))
    print(
        "WW_SPENDING_CELL_FIBER_LAYOUT_COUNTEREXAMPLE_PASS "
        f"checks={len(checks)} q={Q} n={N} k={K} B*=6 plants=6 list_lower=7"
    )


if __name__ == "__main__":
    main()
