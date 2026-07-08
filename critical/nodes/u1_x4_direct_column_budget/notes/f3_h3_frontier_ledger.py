#!/usr/bin/env python3
"""Compile the current h=3 frontier for the F3 flip attempt.

This ledger imports existing compilers and records the current proof surface.
It proves no new rank theorem and no new geometric batching theorem.
"""

from __future__ import annotations

from dataclasses import dataclass

from f3_h3_activation_bound_compiler import (
    first_n_below_floor,
    load_summary,
    prime_activation_counts,
)
from f3_h3_l2_levelset_bridge_compiler import (
    check_ledger,
    synthetic_ledgers,
)
from f3_h3_nondiagonal_highrow_budget import EXPECTED_ROWS as HIGH_ROWS
from f3_h3_nondiagonal_lowrow_budget import EXPECTED_ROWS as LOW_ROWS
from f3_h3_private_linear_lowrow_budget import EXPECTED_ROWS as PRIVATE_ROWS
from f3_h3_private_linear_official_separation_guard import (
    separation_summary as private_separation_summary,
)
from f3_h3_rank_effective_bridge import EXPECTED_CAPACITIES, PINNED_RANKS, rank_capacity
from f3_h3_repeat_frontier_ledger import strict_frontier_gates


@dataclass(frozen=True)
class H3FrontierGate:
    name: str
    status: str
    evidence: str
    residual: str


def activation_summary() -> dict[str, int]:
    data = load_summary()
    counts = prime_activation_counts(data)
    max_prime, max_count = max(counts.items(), key=lambda item: (item[1], -item[0]))
    if data["activation_exception_count"] != 720:
        raise AssertionError(data["activation_exception_count"])
    if max_count != 92 or max_prime != 37633:
        raise AssertionError((max_prime, max_count))
    if first_n_below_floor(16) != 17:
        raise AssertionError(first_n_below_floor(16))
    return {
        "n": data["n"],
        "oriented_activations": data["activation_exception_count"],
        "activation_primes": len(counts),
        "max_prime": max_prime,
        "max_count": max_count,
        "c16_threshold": 17,
    }


def official_budget_summary() -> dict[str, int]:
    rows = (*LOW_ROWS, *HIGH_ROWS)
    private = tuple(PRIVATE_ROWS)
    exponents = [row.s for row in rows]
    private_exponents = [row.s for row in private]
    expected = list(range(13, 42))
    if exponents != expected:
        raise AssertionError(exponents)
    if private_exponents != expected:
        raise AssertionError(private_exponents)
    return {
        "first_s": 13,
        "last_s": 41,
        "z_budget_min": min(row.z for row in rows),
        "z_budget_max": max(row.z for row in rows),
        "z_private_min": min(row.z for row in private),
        "z_private_max": max(row.z for row in private),
        "private_separation_margin": private_separation_summary()["min_pass_margin"],
    }


def rank_capacity_summary() -> dict[str, int]:
    actual = {name: rank_capacity(rank) for name, rank in PINNED_RANKS.items()}
    if actual != EXPECTED_CAPACITIES:
        raise AssertionError(actual)
    return {
        "collapsed_capacity": actual["constant-ratio collapsed"],
        "private_capacity": actual["private-divisor rational"],
        "random_capacity": actual["repaired random full-rank"],
    }


def l2_bridge_summary() -> dict[str, int]:
    rows = [check_ledger(name, n, r_values) for name, n, r_values in synthetic_ledgers()]
    boundary = rows[2]
    if boundary["pairs"] != 1024 or boundary["exact_numer"] != 73728:
        raise AssertionError(boundary)
    return {
        "target_multiplier": 1152,
        "pair_target_multiplier": 16,
        "synthetic_ledgers": len(rows),
        "boundary_pairs": boundary["pairs"],
    }


def repeat_frontier_summary() -> dict[str, tuple[int, int]]:
    expected = {
        "H3-VALUE-GEN-INJECTIVE": (14, 10),
        "H3-VALUE-SCALE-INJECTIVE": (6, 3),
        "H3-SLOPE-GG-HIT": (14, 41),
        "H3-SLOPE-MIXED-HIT": (10, 27),
        "LOOSE-GEN-RANK/NV": (15, 0),
        "LOOSE-A-RANK/NV": (22, 0),
        "LOOSE-B-RANK/NV": (24, 0),
    }
    actual = {
        gate.name: (gate.membership_total, gate.extra_total)
        for gate in strict_frontier_gates()
    }
    if actual != expected:
        raise AssertionError(actual)
    return actual


def frontier_gates(
    activation: dict[str, int],
    budgets: dict[str, int],
    capacity: dict[str, int],
    l2: dict[str, int],
    repeat: dict[str, tuple[int, int]],
) -> tuple[H3FrontierGate, ...]:
    return (
        H3FrontierGate(
            "H3-ACT-COMPILER",
            "REPLAYED/CONDITIONAL",
            (
                f"C=16 gives T3<n^3 from n>={activation['c16_threshold']}; "
                f"n=96 evidence has max {activation['max_count']} oriented activations"
            ),
            "prove H3-ACT(16), or replace with official-row activation certificates",
        ),
        H3FrontierGate(
            "F3-RANK-AVOID / RC-NV",
            "OPEN",
            (
                f"non-diagonal official budgets cover s={budgets['first_s']}..{budgets['last_s']} "
                f"with Z={budgets['z_budget_min']}..{budgets['z_budget_max']}"
            ),
            "prove finite-row rank-good minor nonvanishing on repaired degree-2 signature-curve images",
        ),
        H3FrontierGate(
            "H3-BRIDGE-RANKCAP",
            "OPEN",
            (
                f"rank-effective capacities are pinned: collapsed={capacity['collapsed_capacity']}, "
                f"private={capacity['private_capacity']}, random={capacity['random_capacity']}; "
                f"L2 target is sum R_z(R_z-6)<={l2['target_multiplier']}n"
            ),
            "assign activated non-toral shape pairs to repaired chart images with total rank capacity within the official budget",
        ),
        H3FrontierGate(
            "F3-PRIVATE-LINEAR-RANK-AVOID",
            "OPEN/ALTERNATE",
            (
                f"private-linear budgets cover s={budgets['first_s']}..{budgets['last_s']} "
                f"with Z={budgets['z_private_min']}..{budgets['z_private_max']}; "
                f"official separation margin={budgets['private_separation_margin']}"
            ),
            "prove finite-row minor nonvanishing on the three-parameter private-linear normal-form image, plus the matching bridge",
        ),
        H3FrontierGate(
            "H3-REPEAT-BOUNDARY-STAR",
            "OPEN FRONTIER",
            f"{len(repeat)} strict branch gates replayed in the repeat frontier ledger",
            "prove or replace the strict same-lambda, slope, and loose-triangle branch gates needed by the star route",
        ),
    )


def main() -> None:
    activation = activation_summary()
    budgets = official_budget_summary()
    capacity = rank_capacity_summary()
    l2 = l2_bridge_summary()
    repeat = repeat_frontier_summary()
    gates = frontier_gates(activation, budgets, capacity, l2, repeat)

    print("F3 h=3 frontier ledger")
    print(
        f"activation evidence: n={activation['n']} "
        f"oriented={activation['oriented_activations']} "
        f"primes={activation['activation_primes']} "
        f"max={activation['max_count']} at p={activation['max_prime']}"
    )
    print(
        "official rank-capacity budgets: "
        f"Z_budget={budgets['z_budget_min']}..{budgets['z_budget_max']} "
        f"Z_private={budgets['z_private_min']}..{budgets['z_private_max']} "
        f"private_sep_margin={budgets['private_separation_margin']}"
    )
    print(
        "rank-effective capacities: "
        f"collapsed={capacity['collapsed_capacity']} "
        f"private={capacity['private_capacity']} random={capacity['random_capacity']}"
    )
    print(
        "L2 bridge target: "
        f"sum R_z(R_z-6) <= {l2['target_multiplier']} n "
        f"equiv P_total <= {l2['pair_target_multiplier']} n"
    )
    print("repeat-boundary strict gates:")
    for name, (membership, extra) in repeat.items():
        print(f"  {name}: membership_total={membership} extra_total={extra}")
    print("frontier gates:")
    for gate in gates:
        print(f"{gate.name}: {gate.status}")
        print(f"  evidence: {gate.evidence}")
        print(f"  residual: {gate.residual}")
    print("H3_FRONTIER_LEDGER_PASS")


if __name__ == "__main__":
    main()
