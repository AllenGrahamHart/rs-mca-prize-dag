#!/usr/bin/env python3
"""Sparse fixed-point skeleton for the h=8 chart-7 graph."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import sympy as sp

from f3_h8_reciprocal_compatibility_compiler import ALL_BARS, TOP, reciprocal_part
from f3_h8_x83_triangular_obstruction import LOCATOR


CHART = 7


@dataclass(frozen=True)
class SubstitutionProfile:
    bar: str
    denominator_p7_power: int
    numerator_terms: int
    numerator_total_degree: int


@dataclass(frozen=True)
class ConjugatePartProfile:
    slot: int
    denominator_p7_power: int
    pre_cancellation_terms: int
    numerator_degree_bound: int
    original_terms: int
    original_total_degree: int


@dataclass(frozen=True)
class FixedPointSkeletonRow:
    target_slot: int
    common_denominator_p7_power: int
    pre_cancellation_terms: int
    total_degree_bound: int


@lru_cache(maxsize=1)
def chart_parts() -> dict[int, sp.Expr]:
    parts = {index: reciprocal_part(index)[1] for index in range(1, 8)}
    parts[8] = LOCATOR[8]
    return parts


@lru_cache(maxsize=1)
def substitution_profiles() -> tuple[SubstitutionProfile, ...]:
    parts = chart_parts()
    rows: list[SubstitutionProfile] = []
    for bar in ALL_BARS:
        name = str(bar)
        if name == "bar_c9":
            rows.append(SubstitutionProfile(name, 0, 1, 1))
        elif name == "bar_c8":
            rows.append(SubstitutionProfile(name, 1, 1, 2))
        else:
            slot = 16 - int(name[5:])
            poly = sp.Poly(parts[slot], *TOP, domain=sp.ZZ)
            rows.append(
                SubstitutionProfile(
                    name,
                    1,
                    len(poly.terms()),
                    poly.total_degree() + 1,
                )
            )
    return tuple(rows)


@lru_cache(maxsize=None)
def conjugate_part_profile(slot: int) -> ConjugatePartProfile:
    parts = chart_parts()
    _, p7, _ = reciprocal_part(CHART)
    p7_poly = sp.Poly(p7, *TOP, domain=sp.ZZ)
    p7_terms = len(p7_poly.terms())
    p7_degree = p7_poly.total_degree()
    substitutions = substitution_profiles()
    poly = sp.Poly(parts[slot], *TOP, domain=sp.ZZ)

    monomial_profiles: list[tuple[int, int, int]] = []
    max_power = 0
    for monom, _ in poly.terms():
        denominator_power = sum(
            exponent * substitutions[index].denominator_p7_power
            for index, exponent in enumerate(monom)
        )
        term_bound = 1
        degree_bound = 0
        for index, exponent in enumerate(monom):
            if exponent == 0:
                continue
            term_bound *= substitutions[index].numerator_terms**exponent
            degree_bound += substitutions[index].numerator_total_degree * exponent
        monomial_profiles.append((denominator_power, term_bound, degree_bound))
        max_power = max(max_power, denominator_power)

    pre_cancellation_terms = 0
    numerator_degree_bound = 0
    for denominator_power, term_bound, degree_bound in monomial_profiles:
        padding_power = max_power - denominator_power
        pre_cancellation_terms += term_bound * (p7_terms**padding_power)
        numerator_degree_bound = max(
            numerator_degree_bound,
            degree_bound + padding_power * p7_degree,
        )

    return ConjugatePartProfile(
        slot=slot,
        denominator_p7_power=max_power,
        pre_cancellation_terms=pre_cancellation_terms,
        numerator_degree_bound=numerator_degree_bound,
        original_terms=len(poly.terms()),
        original_total_degree=poly.total_degree(),
    )


@lru_cache(maxsize=1)
def conjugate_part_profiles() -> tuple[ConjugatePartProfile, ...]:
    return tuple(conjugate_part_profile(slot) for slot in range(1, 9))


@lru_cache(maxsize=1)
def fixedpoint_skeleton_rows() -> tuple[FixedPointSkeletonRow, ...]:
    _, p7, _ = reciprocal_part(CHART)
    p7_poly = sp.Poly(p7, *TOP, domain=sp.ZZ)
    p7_terms = len(p7_poly.terms())
    p7_degree = p7_poly.total_degree()
    profiles = {row.slot: row for row in conjugate_part_profiles()}
    chart_profile = profiles[CHART]

    rows: list[FixedPointSkeletonRow] = []
    for target_slot in (1, 2, 3, 4, 5, 6, 8):
        target_profile = profiles[target_slot]
        common_power = max(
            chart_profile.denominator_p7_power,
            target_profile.denominator_p7_power,
        )
        chart_padding = common_power - chart_profile.denominator_p7_power
        target_padding = common_power - target_profile.denominator_p7_power
        pre_cancellation_terms = (
            chart_profile.pre_cancellation_terms * (p7_terms**chart_padding)
            + target_profile.pre_cancellation_terms * (p7_terms**target_padding)
        )
        total_degree_bound = max(
            1 + chart_profile.numerator_degree_bound + chart_padding * p7_degree,
            1 + target_profile.numerator_degree_bound + target_padding * p7_degree,
        )
        rows.append(
            FixedPointSkeletonRow(
                target_slot=target_slot,
                common_denominator_p7_power=common_power,
                pre_cancellation_terms=pre_cancellation_terms,
                total_degree_bound=total_degree_bound,
            )
        )
    return tuple(rows)


def fixedpoint_skeleton_summary() -> dict[str, int]:
    substitutions = substitution_profiles()
    profiles = conjugate_part_profiles()
    rows = fixedpoint_skeleton_rows()
    expected_substitutions = {
        "bar_c8": (1, 1, 2),
        "bar_c9": (0, 1, 1),
        "bar_c10": (1, 40, 11),
        "bar_c11": (1, 52, 12),
        "bar_c12": (1, 70, 13),
        "bar_c13": (1, 89, 14),
        "bar_c14": (1, 115, 15),
        "bar_c15": (1, 140, 16),
    }
    actual_substitutions = {
        row.bar: (
            row.denominator_p7_power,
            row.numerator_terms,
            row.numerator_total_degree,
        )
        for row in substitutions
    }
    if actual_substitutions != expected_substitutions:
        raise AssertionError(actual_substitutions)

    expected_profiles = {
        1: (15, 193_739_819_866_454_614_432_080_308_483_638, 240, 140, 15),
        2: (14, 1_383_854_668_464_947_616_708_824_390_613, 224, 115, 14),
        3: (13, 9_884_628_736_752_300_408_065_281_673, 208, 89, 13),
        4: (12, 70_604_136_603_528_584_030_836_299, 192, 70, 12),
        5: (11, 504_301_112_158_780_208_566_858, 176, 52, 11),
        6: (10, 3_602_046_985_214_881_055_420, 160, 40, 10),
        7: (9, 25_724_765_024_868_437_269, 144, 29, 9),
        8: (1, 1, 2, 1, 1),
    }
    actual_profiles = {
        row.slot: (
            row.denominator_p7_power,
            row.pre_cancellation_terms,
            row.numerator_degree_bound,
            row.original_terms,
            row.original_total_degree,
        )
        for row in profiles
    }
    if actual_profiles != expected_profiles:
        raise AssertionError(actual_profiles)

    expected_rows = {
        1: (15, 193_755_121_556_618_651_323_524_735_233_987, 241),
        2: (14, 1_384_382_312_953_362_681_931_046_002_694, 225),
        3: (13, 9_902_823_374_283_854_381_245_337_262, 209),
        4: (12, 71_231_537_897_720_100_347_389_940, 193),
        5: (11, 525_935_639_544_694_564_310_087, 177),
        6: (10, 4_348_065_170_936_065_736_221, 161),
        8: (9, 25_724_765_525_114_850_230, 145),
    }
    actual_rows = {
        row.target_slot: (
            row.common_denominator_p7_power,
            row.pre_cancellation_terms,
            row.total_degree_bound,
        )
        for row in rows
    }
    if actual_rows != expected_rows:
        raise AssertionError(actual_rows)

    return {
        "substitution_rows": len(substitutions),
        "conjugate_profiles": len(profiles),
        "fixedpoint_rows": len(rows),
        "max_common_denominator_p7_power": max(
            row.common_denominator_p7_power for row in rows
        ),
        "min_pre_cancellation_terms": min(row.pre_cancellation_terms for row in rows),
        "max_pre_cancellation_terms": max(row.pre_cancellation_terms for row in rows),
        "max_total_degree_bound": max(row.total_degree_bound for row in rows),
    }


def main() -> None:
    summary = fixedpoint_skeleton_summary()
    print("h=8 chart-7 fixed-point skeleton")
    print("profiles are sparse upper bounds; no expanded fixed-point numerators are formed")
    for row in conjugate_part_profiles():
        print(
            f"  Q{row.slot}: P7_denom_power={row.denominator_p7_power} "
            f"original_terms={row.original_terms} "
            f"pre_cancel_terms<={row.pre_cancellation_terms} "
            f"numerator_degree<={row.numerator_degree_bound}"
        )
    for row in fixedpoint_skeleton_rows():
        print(
            f"  F{row.target_slot}: common_P7_power={row.common_denominator_p7_power} "
            f"pre_cancel_terms<={row.pre_cancellation_terms} "
            f"total_degree<={row.total_degree_bound}"
        )
    print(
        "summary: "
        f"fixedpoint_rows={summary['fixedpoint_rows']} "
        f"P7_power<={summary['max_common_denominator_p7_power']} "
        f"pre_cancel_terms={summary['min_pre_cancellation_terms']}.."
        f"{summary['max_pre_cancellation_terms']} "
        f"max_total_degree={summary['max_total_degree_bound']}"
    )
    print("H8_CHART7_FIXEDPOINT_SKELETON_PASS")


if __name__ == "__main__":
    main()
