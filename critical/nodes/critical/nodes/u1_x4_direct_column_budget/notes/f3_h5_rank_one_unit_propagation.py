#!/usr/bin/env python3
"""Abstract unit propagation for the h=5 rank-one reciprocal charts."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


SLOTS = range(1, 6)
A = {index: sp.Symbol(f"A{index}") for index in SLOTS}
B = {index: sp.Symbol(f"B{index}") for index in SLOTS}
ABAR = {index: sp.Symbol(f"bar_A{index}") for index in SLOTS}
BBAR = {index: sp.Symbol(f"bar_B{index}") for index in SLOTS}


@dataclass(frozen=True)
class UnitPropagationSyzygy:
    source_chart: int
    target_slot: int
    source_unit: str
    target_unit: str
    oriented_minor: str
    conjugate_minor: str


def oriented_minor(source: int, target: int) -> sp.Expr:
    return B[target] * A[source] - B[source] * A[target]


def conjugate_minor(source: int, target: int) -> sp.Expr:
    return BBAR[target] * ABAR[source] - BBAR[source] * ABAR[target]


def unit_row(index: int) -> sp.Expr:
    return A[index] * ABAR[index] - B[index] * BBAR[index]


def unit_propagation_syzygies() -> tuple[UnitPropagationSyzygy, ...]:
    rows: list[UnitPropagationSyzygy] = []
    for source in SLOTS:
        for target in SLOTS:
            if source == target:
                continue
            c_st = oriented_minor(source, target)
            cbar_st = conjugate_minor(source, target)
            identity = sp.expand(
                B[source] * BBAR[source] * unit_row(target)
                - B[target] * BBAR[target] * unit_row(source)
                + BBAR[source] * ABAR[target] * c_st
                + B[target] * A[source] * cbar_st
            )
            if identity != 0:
                raise AssertionError((source, target, sp.factor(identity)))
            rows.append(
                UnitPropagationSyzygy(
                    source_chart=source,
                    target_slot=target,
                    source_unit=f"N{source}",
                    target_unit=f"N{target}",
                    oriented_minor=f"C{source}->{target}",
                    conjugate_minor=f"conj(C{source}->{target})",
                )
            )
    return tuple(rows)


def unit_propagation_summary() -> dict[str, int]:
    syzygies = unit_propagation_syzygies()
    by_source = {source: 0 for source in SLOTS}
    for row in syzygies:
        by_source[row.source_chart] += 1
    expected = {source: 4 for source in SLOTS}
    if by_source != expected:
        raise AssertionError(by_source)
    return {
        "charts": len(tuple(SLOTS)),
        "ordered_syzygies": len(syzygies),
        "targets_per_chart": min(by_source.values()),
    }


def main() -> None:
    summary = unit_propagation_summary()
    print("h=5 rank-one unit propagation")
    print(
        "identity: B_i*bar_B_i*N_j - B_j*bar_B_j*N_i "
        "in <C_ij,conj(C_ij)>"
    )
    print(
        "summary: "
        f"charts={summary['charts']} "
        f"ordered_syzygies={summary['ordered_syzygies']} "
        f"targets_per_chart={summary['targets_per_chart']}"
    )
    print("H5_RANK_ONE_UNIT_PROPAGATION_PASS")


if __name__ == "__main__":
    main()
