#!/usr/bin/env python3
"""Shared-core Stepanov/rank target for h=3 loose special branches."""

from __future__ import annotations

from f3_h3_repeat_loose_rank_minor_compiler import minor_degree_row
from f3_h3_repeat_loose_shared_core_degree import loose_shared_core_summary
from f3_h3_repeat_loose_stepanov_compiler import LooseTarget, compile_row


def shared_core_target() -> LooseTarget:
    shared = loose_shared_core_summary()
    return LooseTarget(
        name="shared_core",
        parameter_blocks=1,
        maps=shared["shared_maps"],
        subgroup_order=32,
        family_size=1,
        param_degree=16,
        source_degree=512,
        subgroup_degree=4,
        multiplicity=2,
        parameter_sum_total=shared["shared_sum_total"],
    )


def shared_core_rank_summary() -> dict[str, int]:
    target = shared_core_target()
    compiled = compile_row(target)
    minor = minor_degree_row(target)
    return {
        "maps": target.maps,
        "parameter_blocks": target.parameter_blocks,
        "parameter_sum_total": target.parameter_sum_total,
        "coefficients": compiled.coefficients,
        "conditions": compiled.conditions,
        "x_degree": compiled.x_degree,
        "point_bound_num": compiled.point_bound_num,
        "point_bound_den": compiled.point_bound_den,
        "rank_capacity_slack": compiled.rank_capacity_slack,
        "cleared_total_degree": compiled.cleared_total_degree,
        "rank_target": minor.rank_target,
        "entry_parameter_degree": minor.entry_parameter_degree,
        "minor_total_degree": minor.minor_total_degree,
    }


def main() -> None:
    print("h=3 repeat loose shared-core rank target")
    summary = shared_core_rank_summary()
    expected = {
        "maps": 6,
        "parameter_blocks": 1,
        "parameter_sum_total": 14,
        "coefficients": 33_554_432,
        "conditions": 1048,
        "x_degree": 1087,
        "point_bound_num": 1087,
        "point_bound_den": 2,
        "rank_capacity_slack": 40,
        "cleared_total_degree": 1870,
        "rank_target": 1049,
        "entry_parameter_degree": 1359,
        "minor_total_degree": 1_425_591,
    }
    if summary != expected:
        raise AssertionError(summary)
    print(
        "shared_core_stepanov: "
        f"maps={summary['maps']} "
        f"parameter_blocks={summary['parameter_blocks']} "
        f"S_total={summary['parameter_sum_total']} "
        f"coefficients={summary['coefficients']} "
        f"conditions={summary['conditions']} "
        f"x_degree={summary['x_degree']} "
        f"point_bound={summary['point_bound_num']}/{summary['point_bound_den']} "
        f"rank_capacity_slack={summary['rank_capacity_slack']} "
        f"cleared_total_degree={summary['cleared_total_degree']}"
    )
    print(
        "shared_core_minor_target: "
        f"rank_target={summary['rank_target']} "
        f"entry_degree={summary['entry_parameter_degree']} "
        f"minor_degree<={summary['minor_total_degree']}"
    )
    print("H3_REPEAT_LOOSE_SHARED_CORE_RANK_TARGET_PASS")


if __name__ == "__main__":
    main()
