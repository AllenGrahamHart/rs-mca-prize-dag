#!/usr/bin/env python3
"""Replay K'=83 carrier lanes with the stratified support-5/6 charge."""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import re
import tarfile
from functools import lru_cache
from math import comb
from pathlib import Path


ARCHIVES = list(Path(".").glob("*.tar.gz"))
ROOT = Path("repo") if ARCHIVES else Path(__file__).resolve().parents[2]
if ARCHIVES:
    for archive_path in ARCHIVES:
        with tarfile.open(archive_path, "r:gz") as archive:
            archive.extractall(ROOT, filter="data")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PROBE = load_module(
    "carrier_atlas_for_stratified56",
    ROOT
    / "experiments/prize_resolution/rate_half_mca_rank11_k72_two_step_probe.py",
)
K71 = PROBE.K71
SUPPORTS = K71.SUPPORTS


@lru_cache(maxsize=None)
def stratified56_weighted_cap(
    kprime: int, union: int, dimension: int
) -> int:
    """Bound the weighted support-5/6 incidence inside/outside every union."""
    assert dimension >= 6
    m = 67472 + kprime
    outside = m - union
    residual = kprime - union - dimension
    assert residual >= 0
    factor5 = comb(m - 5, 6)
    factor6 = comb(m - 6, 5)
    weight5 = K71.LEDGER.DEFICITS[5] * factor5
    weight6 = K71.LEDGER.DEFICITS[6] * factor6
    total = 0

    # For i=0..3, contract an i-set inside the fixed union and couple
    # support-(5-i) and support-(6-i) circuits on the outside restriction.
    for inside in range(4):
        choices = comb(union, inside)
        cap5 = (
            choices
            * residual
            * comb(outside, 4 - inside)
            // (5 - inside)
        )
        rhs6 = choices * residual * comb(outside, 5 - inside)
        coefficient = outside - residual - 4 + inside
        slope = (
            (6 - inside) * weight5 - coefficient * weight6
        )
        if slope >= 0:
            numerator = weight6 * rhs6 + slope * cap5
        else:
            numerator = weight6 * rhs6
        total += numerator // (6 - inside)

    # The remaining low-outside strata use completion exposure directly.
    count5 = comb(union, 4) * residual + comb(union, 5)
    count6 = (
        comb(union, 4) * residual * outside // 2
        + comb(union, 5) * residual
        + comb(union, 6)
    )
    return total + weight5 * count5 + weight6 * count6


def charged_case_rows(kprime: int, local: tuple[int, ...], cases: dict):
    """Deduplicate geometry routes while retaining both joint charges."""
    rows = {}
    for name, charges in cases.items():
        candidate = local
        joint45 = None
        joint56 = []
        for union, dimension in charges:
            candidate = K71.combine(
                candidate,
                PROBE.fixed_union_cap(kprime, union, dimension),
            )
            if dimension >= 5:
                coupled = PROBE.joint45_weighted_cap(
                    kprime, union, dimension
                )
                joint45 = (
                    coupled if joint45 is None else min(joint45, coupled)
                )
            if dimension >= 6 and kprime - union - dimension >= 0:
                joint56.append(
                    stratified56_weighted_cap(
                        kprime, union, dimension
                    )
                )
        rows.setdefault((candidate, joint45, tuple(joint56)), name)
    return rows


def priced(
    kprime: int,
    caps: tuple[int, ...],
    joint45: int | None,
    joint56: tuple[int, ...],
) -> int:
    value = K71.premium(caps)
    old456 = sum(
        K71.LEDGER.DEFICITS[support] * caps[support - 2]
        for support in (4, 5, 6)
    )
    options = [old456]
    if joint45 is not None:
        options.append(
            joint45 + K71.LEDGER.DEFICITS[6] * caps[6 - 2]
        )
    if joint56:
        m = 67472 + kprime
        factor4 = comb(m - 4, 7)
        normalized4 = caps[4 - 2] // factor4 * factor4
        options.extend(
            K71.LEDGER.DEFICITS[4] * normalized4 + bound
            for bound in joint56
        )
    return value - old456 + min(options)


@lru_cache(maxsize=None)
def adjacent_weighted_cap(
    kprime: int, union: int, dimension: int, support: int
) -> int:
    """Bound one adjacent support pair using the generic fixed-union theorem."""
    assert 2 <= support <= dimension - 1
    m = 67472 + kprime
    outside = m - union
    residual = kprime - union - dimension
    assert residual >= 0 and outside >= residual + support - 1
    weight = (
        K71.LEDGER.DEFICITS[support]
        * comb(m - support, 11 - support)
    )
    weight_next = (
        K71.LEDGER.DEFICITS[support + 1]
        * comb(m - support - 1, 10 - support)
    )
    total = 0
    for inside in range(support - 1):
        choices = comb(union, inside)
        cap = (
            choices
            * residual
            * comb(outside, support - 1 - inside)
            // (support - inside)
        )
        rhs = choices * residual * comb(outside, support - inside)
        coefficient = outside - residual - support + 1 + inside
        slope = (support + 1 - inside) * weight - coefficient * weight_next
        total += (
            weight_next * rhs + max(slope, 0) * cap
        ) // (support + 1 - inside)
    count = comb(union, support - 1) * residual + comb(union, support)
    count_next = (
        comb(union, support - 1) * residual * outside // 2
        + comb(union, support) * residual
        + comb(union, support + 1)
    )
    return total + weight * count + weight_next * count_next


def all_adjacent_caps(kprime: int, charges: list[tuple[int, int]]):
    """Return the strongest available weighted cap for each adjacent pair."""
    result = {}
    for union, dimension in charges:
        if kprime - union - dimension < 0:
            continue
        for support in range(4, min(dimension, 9)):
            value = adjacent_weighted_cap(
                kprime, union, dimension, support
            )
            if support == 4:
                value = min(
                    value,
                    PROBE.joint45_weighted_cap(
                        kprime, union, dimension
                    ),
                )
            if support == 5:
                value = min(
                    value,
                    stratified56_weighted_cap(
                        kprime, union, dimension
                    ),
                )
            result[support] = min(result.get(support, value), value)
    return tuple(sorted(result.items()))


def charged_case_rows_all_adjacent(
    kprime: int, local: tuple[int, ...], cases: dict
):
    """Deduplicate routes while retaining every adjacent-support charge."""
    rows = {}
    for name, charges in cases.items():
        candidate = local
        for union, dimension in charges:
            candidate = K71.combine(
                candidate,
                PROBE.fixed_union_cap(kprime, union, dimension),
            )
        adjacent = all_adjacent_caps(kprime, charges)
        rows.setdefault((candidate, adjacent), name)
    return rows


def priced_all_adjacent(
    kprime: int,
    caps: tuple[int, ...],
    adjacent: tuple[tuple[int, int], ...],
) -> int:
    """Optimize over support-disjoint adjacent-pair charges."""
    base = K71.premium(caps)
    edges = dict(adjacent)
    choices = [base]
    ordered = sorted(edges)
    for width in range(1, len(ordered) + 1):
        for selected in itertools.combinations(ordered, width):
            covered = {
                support
                for edge in selected
                for support in (edge, edge + 1)
            }
            if len(covered) != 2 * len(selected):
                continue
            old = sum(
                K71.LEDGER.DEFICITS[support] * caps[support - 2]
                for support in covered
            )
            choices.append(
                base - old + sum(edges[edge] for edge in selected)
            )
    return min(choices)


def lane_summary(kprime: int, selected: set[str]) -> dict[str, object]:
    q = kprime - 10
    m = 67472 + kprime
    baseline = K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(q, m)
    _, front23, steps, carrier32, _ = PROBE.position23_group(
        kprime, baseline
    )
    exact45, _, front45 = K71.exact45_rows(kprime, baseline)
    _, high = K71.PARENT.high_group(kprime, baseline)
    maximum = (-1, "")
    counts: dict[str, int] = {}

    def keep(lane: str, value: int, label: str) -> None:
        nonlocal maximum
        counts[lane] = counts.get(lane, 0) + 1
        maximum = max(maximum, (value, label))

    if "ordinary" in selected:
        for left, middle in itertools.product(front23, front45):
            defects = re.fullmatch(r"s2=(\d+)/s3=(\d+)/U23", left[0])
            m2 = q - int(defects.group(1)) if defects else 0
            m3 = q - int(defects.group(2)) if defects else 0
            prefix = f"{left[0]}/{middle[0]}"
            if defects and m2 > 0 and m3 > m2:
                s4_match = re.search(r"s4=(\d+)", middle[0])
                s5_match = re.search(r"s5=(\d+)", middle[0])
                assert s4_match and s5_match
                m4 = q - int(s4_match.group(1))
                m5 = q - int(s5_match.group(1))
                local = K71.combine(left[1], middle[1])
                cases = PROBE.mixed_cases(m2, m3 - m2, m4, m5)
                for (candidate, joint45, joint56), name in (
                    charged_case_rows(kprime, local, cases).items()
                ):
                    for high_name, high_vector in high:
                        caps = K71.combine(candidate, high_vector)
                        keep(
                            "ordinary_geom",
                            priced(kprime, caps, joint45, joint56),
                            f"{prefix}/{high_name}/ordinary_{name}",
                        )
                continue
            for high_name, high_vector in high:
                caps = K71.combine(left[1], middle[1], high_vector)
                keep(
                    "ordinary_plain",
                    K71.premium(caps),
                    f"{prefix}/{high_name}/ordinary_plain",
                )

    if "carrier32" in selected:
        for s2, s3, left in carrier32:
            m2 = q - s2
            offset = 30 - m2
            for s4, s5, middle in exact45:
                m4, m5 = q - s4, q - s5
                local = K71.combine(left, middle)
                prefix = f"s2={s2}/s3={s3}/s4={s4}/s5={s5}"
                cases = PROBE.mixed_cases(m2, offset, m4, m5)
                for (candidate, joint45, joint56), name in (
                    charged_case_rows(kprime, local, cases).items()
                ):
                    for high_name, high_vector in high:
                        caps = K71.combine(candidate, high_vector)
                        keep(
                            "carrier32_geom",
                            priced(kprime, caps, joint45, joint56),
                            f"{prefix}/{high_name}/carrier32_{name}",
                        )

    names = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
    }
    for offset, rows in steps.items():
        lane = names[offset]
        if lane not in selected:
            continue
        for s2, s3, left in rows:
            m2 = q - s2
            for s4, s5, middle in exact45:
                m4, m5 = q - s4, q - s5
                local = K71.combine(left, middle)
                prefix = f"s2={s2}/s3={s3}/s4={s4}/s5={s5}"
                if offset == 1 or m4 > m2:
                    cases = PROBE.mixed_cases(
                        m2, offset, m4, m5
                    )
                elif m4 == m2 + offset:
                    cases = PROBE.offset_cases(
                        m2,
                        offset,
                        include_support5=(m5 == m2 + offset),
                    )
                else:
                    cases = PROBE.mixed_cases(
                        m2, offset, m4, m5
                    )
                for (candidate, joint45, joint56), name in (
                    charged_case_rows(kprime, local, cases).items()
                ):
                    for high_name, high_vector in high:
                        caps = K71.combine(candidate, high_vector)
                        keep(
                            f"{lane}_geom",
                            priced(kprime, caps, joint45, joint56),
                            f"{prefix}/{high_name}/{lane}_{name}",
                        )

    return {
        "kprime": kprime,
        "selected": sorted(selected),
        "counts": counts,
        "maximum": maximum[0],
        "active_branch": maximum[1],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("kprime", type=int)
    parser.add_argument(
        "lanes",
        help="comma-separated ordinary,carrier32,one,...,six",
    )
    args = parser.parse_args()
    selected = set(args.lanes.split(","))
    allowed = {
        "ordinary", "carrier32", "one", "two", "three",
        "four", "five", "six",
    }
    assert selected and selected <= allowed
    print(json.dumps(lane_summary(args.kprime, selected), indent=2))


if __name__ == "__main__":
    main()
