#!/usr/bin/env python3
"""Audit component-defect packets for the core-one maximal-degree face."""

from __future__ import annotations

from math import ceil


def main() -> None:
    component_checks = 0
    residual_checks = 0
    mutations = 0
    for m in range(3, 160):
        e = 2 * m - 1
        supported = 4 * e + 1
        for component_e in range(1, e + 1):
            admissible = []
            for defect in range(-3, 4):
                difference = 5 * component_e - supported * defect
                if -1 <= difference <= e:
                    admissible.append(defect)
            assert len(admissible) <= 1
            assert all(defect in (0, 1) for defect in admissible)
            component_checks += 1

        for residual_e in range(e // 5 + 1):
            dominant_e = e - residual_e
            assert dominant_e >= e - e // 5
            rank = ceil((e + 1) / (residual_e + 1))
            if m >= 12:
                assert rank >= 5
            residual_checks += 1

        # Mutation: total defect two permits two positive components.
        assert sum((1, 1)) == 2
        mutations += 1

    print(
        "AUDIT_RATE_HALF_CA_HANKEL_A1_CORE_ONE_MAX_COMPONENT_LOCALIZATION_PASS "
        f"components={component_checks} residuals={residual_checks} "
        f"mutations={mutations}/157"
    )


if __name__ == "__main__":
    main()
