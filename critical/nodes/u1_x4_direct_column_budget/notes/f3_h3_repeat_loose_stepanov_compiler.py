#!/usr/bin/env python3
"""Conditional Stepanov arithmetic for the loose-triangle targets."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LooseTarget:
    name: str
    parameter_blocks: int
    maps: int
    subgroup_order: int
    family_size: int
    param_degree: int
    source_degree: int
    subgroup_degree: int
    multiplicity: int
    parameter_sum_total: int


@dataclass(frozen=True)
class LooseCompilerRow:
    target: LooseTarget
    coefficients: int
    conditions: int
    x_degree: int
    point_bound_num: int
    point_bound_den: int
    ls_slack: int
    rank_capacity_slack: int
    cleared_total_degree: int


def target_coefficients(target: LooseTarget) -> int:
    return (
        target.param_degree**target.parameter_blocks
        * target.source_degree
        * target.subgroup_degree**target.maps
    )


def reduced_conditions(target: LooseTarget) -> int:
    # For fixed parameters, logarithmic X-jets are over-imposed by a polynomial
    # in X of degree < C + kD, with k membership maps.
    return (
        target.multiplicity
        * (target.source_degree + target.maps * target.multiplicity)
        * target.family_size
    )


def x_degree_bound(target: LooseTarget) -> int:
    return (target.source_degree - 1) + target.maps * target.subgroup_order * (
        target.subgroup_degree - 1
    )


def cleared_total_degree(target: LooseTarget) -> int:
    parameter_source = target.parameter_blocks * (target.param_degree - 1)
    return (
        parameter_source
        + (target.source_degree - 1)
        + target.subgroup_order
        * (target.subgroup_degree - 1)
        * target.parameter_sum_total
    )


def compile_row(target: LooseTarget) -> LooseCompilerRow:
    coefficients = target_coefficients(target)
    conditions = reduced_conditions(target)
    if conditions >= coefficients:
        raise AssertionError((target, coefficients, conditions, "linear system not underdetermined"))
    x_degree = x_degree_bound(target)
    return LooseCompilerRow(
        target=target,
        coefficients=coefficients,
        conditions=conditions,
        x_degree=x_degree,
        point_bound_num=target.family_size * x_degree,
        point_bound_den=target.multiplicity,
        ls_slack=coefficients - conditions,
        rank_capacity_slack=target.family_size * (x_degree + 1) - conditions,
        cleared_total_degree=cleared_total_degree(target),
    )


def sample_targets() -> tuple[LooseTarget, ...]:
    return (
        LooseTarget(
            name="generic",
            parameter_blocks=2,
            maps=9,
            subgroup_order=32,
            family_size=1,
            param_degree=16,
            source_degree=512,
            subgroup_degree=4,
            multiplicity=2,
            parameter_sum_total=15,
        ),
        LooseTarget(
            name="branch_A",
            parameter_blocks=1,
            maps=8,
            subgroup_order=32,
            family_size=1,
            param_degree=16,
            source_degree=512,
            subgroup_degree=4,
            multiplicity=2,
            parameter_sum_total=22,
        ),
        LooseTarget(
            name="branch_B",
            parameter_blocks=1,
            maps=8,
            subgroup_order=32,
            family_size=1,
            param_degree=16,
            source_degree=512,
            subgroup_degree=4,
            multiplicity=2,
            parameter_sum_total=24,
        ),
    )


def main() -> None:
    print("h=3 repeat loose conditional Stepanov compiler")
    print("reduced conditions: D * (C + kD) * |Z|")
    print("coefficients: P^m * C * B^k")
    print("x-degree: C-1 + k n (B-1)")
    print("missing gates: LOOSE-GEN-RANK/NV, LOOSE-A-RANK/NV, LOOSE-B-RANK/NV")
    print(
        " target     k m |Z|   P    C   B   D       coeffs   conditions"
        "      Lx    bound    rank_slack  total_deg"
    )
    for target in sample_targets():
        row = compile_row(target)
        print(
            f"{target.name:9s} {target.maps:2d} {target.parameter_blocks:1d}"
            f" {target.family_size:3d} {target.param_degree:3d}"
            f" {target.source_degree:4d} {target.subgroup_degree:3d}"
            f" {target.multiplicity:3d} {row.coefficients:12d}"
            f" {row.conditions:12d} {row.x_degree:7d}"
            f" {row.point_bound_num:6d}/{row.point_bound_den:<3d}"
            f" {row.rank_capacity_slack:11d} {row.cleared_total_degree:10d}"
        )
        expected_x_degree = (target.source_degree - 1) + target.maps * target.subgroup_order * (
            target.subgroup_degree - 1
        )
        if row.x_degree != expected_x_degree:
            raise AssertionError((target, row.x_degree))
        if row.rank_capacity_slack <= 0:
            raise AssertionError((target, row.rank_capacity_slack, "sample rank route has no capacity"))
    print("H3_REPEAT_LOOSE_STEPANOV_COMPILER_PASS")


if __name__ == "__main__":
    main()
