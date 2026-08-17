#!/usr/bin/env python3
"""Traverse one K'=88 raw-unsafe offset with raw-clipped pricing."""

from __future__ import annotations

import json


def scan(base, offset: int) -> dict[str, object]:
    assert 1 <= offset < base.Q
    baseline = base.K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(base.Q, base.M)
    middle = list(base.exact45_rows(baseline))
    _, high = base.K71.PARENT.high_group(base.KPRIME, baseline)
    high = sorted(high)
    units = unsafe_units = profiles_checked = 0

    for m2 in range(1, base.Q - offset + 1):
        m3 = m2 + offset
        s2, s3 = base.Q - m2, base.Q - m3
        left = base.K71.base23_vector(base.KPRIME, baseline, s2, s3)
        raw_cache = {}
        for s4, s5, middle_vector in middle:
            units += 1
            local_caps = base.K71.combine(left, middle_vector)
            raw = raw_cache.get(local_caps)
            if raw is None:
                raw = base.raw_maximum(local_caps, high)
                raw_cache[local_caps] = raw
            if raw[0] <= base.CEILING:
                continue
            unsafe_units += 1
            cases = base.PROBE.mixed_cases(
                m2, offset, base.Q - s4, base.Q - s5
            )
            for case, charges, fixed, adjacent in base.geometry_profiles(cases):
                candidate = base.K71.combine(local_caps, fixed)
                after = max(
                    (
                        base.clipped_price(
                            base.K71.combine(candidate, high_vector),
                            adjacent,
                            charges,
                        ),
                        high_name,
                    )
                    for high_name, high_vector in high
                )
                profiles_checked += 1
                if after[0] > base.LEADER:
                    return {
                        "event": "FALSIFIED",
                        "offset": offset,
                        "m2": m2,
                        "m3": m3,
                        "s2": s2,
                        "s3": s3,
                        "s4": s4,
                        "s5": s5,
                        "m4": base.Q - s4,
                        "m5": base.Q - s5,
                        "case": case,
                        "charges": charges,
                        "adjacent_edges": adjacent,
                        "raw_before": raw[0],
                        "raw_before_high": raw[1],
                        "clipped_after": after[0],
                        "clipped_high": after[1],
                        "leader": base.LEADER,
                        "excess_over_leader": after[0] - base.LEADER,
                        "units_checked": units,
                        "unsafe_units_checked": unsafe_units,
                        "profiles_checked": profiles_checked,
                        "complete": False,
                    }
        print(json.dumps({
            "event": "PROGRESS",
            "offset": offset,
            "m2": m2,
            "units_checked": units,
            "unsafe_units_checked": unsafe_units,
            "profiles_checked": profiles_checked,
        }, sort_keys=True), flush=True)
    return {
        "event": "SURVIVED",
        "offset": offset,
        "units_checked": units,
        "unsafe_units_checked": unsafe_units,
        "profiles_checked": profiles_checked,
        "leader": base.LEADER,
        "complete": True,
    }
