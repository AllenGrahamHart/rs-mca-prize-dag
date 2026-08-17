#!/usr/bin/env python3
"""Float route probe for a joint raw-clipped 4/5/6 K'=88 witness LP."""

from __future__ import annotations

import importlib.util
import json
from math import comb
from pathlib import Path

from scipy.optimize import linprog


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


DIRECTORY = Path(__file__).resolve().parent
K88 = load_module(
    "k88_joint456_raw_clipped_base",
    DIRECTORY / "rate_half_mca_rank11_k88_clipped_domination_falsifier_cached.py",
)
PAIR = load_module(
    "k88_joint456_raw_clipped_pair",
    DIRECTORY / "rate_half_mca_raw_clipped_adjacent_support.py",
)
BASE = K88.BASE
KPRIME, Q, M = BASE.KPRIME, BASE.Q, BASE.M
UNION, DIMENSION = 38, 6


def witness_caps():
    baseline = BASE.K71.PARENT.PARENT.PARENT.CAPS.baseline_caps(Q, M)
    left = BASE.K71.base23_vector(KPRIME, baseline, 46, 45)
    middle = next(
        vector
        for s4, s5, vector in BASE.exact45_rows(baseline)
        if (s4, s5) == (45, 44)
    )
    local = BASE.K71.combine(left, middle)
    cases = BASE.PROBE.mixed_cases(32, 1, 33, 34)
    profile = next(
        row for row in BASE.geometry_profiles(cases)
        if row[0] == "F23__N4_t0__N5_t2"
    )
    case, charges, fixed, adjacent = profile
    assert charges == [(UNION, DIMENSION), (UNION, DIMENSION)]
    candidate = BASE.K71.combine(local, fixed)
    _, high = BASE.K71.PARENT.high_group(KPRIME, baseline)
    raw, high_name, caps = max(
        (
            BASE.K71.premium(BASE.K71.combine(candidate, vector)),
            name,
            BASE.K71.combine(candidate, vector),
        )
        for name, vector in sorted(high)
    )
    assert high_name == "c6F/c7F/c8F/c9F"
    assert raw == 49355312964508839635000536009148053954853701245
    return case, charges, adjacent, raw, caps


def add_row(rows, rhs_values, coefficients, rhs):
    row = [0] * 14
    for index, value in coefficients.items():
        row[index] = value
    rows.append(row)
    rhs_values.append(rhs)


def build_lp(caps):
    # x_0..x_2 are support 4, y_0..y_3 support 5,
    # z_0..z_3 support 6, followed by direct 4/5/6 strata.
    pair45, direct4, _ = PAIR.pair_data(
        KPRIME, M, UNION, DIMENSION, 4
    )
    pair56, direct5, direct6 = PAIR.pair_data(
        KPRIME, M, UNION, DIMENSION, 5
    )
    rows, rhs_values = [], []
    bounds = [(0, None)] * 14
    for inside, a5, b4, rhs, cap4 in pair45:
        add_row(rows, rhs_values, {inside: b4, 3 + inside: a5}, rhs)
        bounds[inside] = (0, cap4)
    for inside, a6, b5, rhs, cap5 in pair56:
        add_row(rows, rhs_values, {3 + inside: b5, 7 + inside: a6}, rhs)
        bounds[3 + inside] = (0, cap5)
    bounds[11] = (0, direct4)
    bounds[12] = (0, direct5)
    bounds[13] = (0, direct6)

    raw = {}
    for support in (4, 5, 6):
        factor = comb(M - support, 11 - support)
        raw[support], _ = divmod(caps[support - 2], factor)
    add_row(rows, rhs_values, {0: 1, 1: 1, 2: 1, 11: 1}, raw[4])
    add_row(
        rows,
        rhs_values,
        {3: 1, 4: 1, 5: 1, 6: 1, 12: 1},
        raw[5],
    )
    add_row(
        rows,
        rhs_values,
        {7: 1, 8: 1, 9: 1, 10: 1, 13: 1},
        raw[6],
    )
    weights = {
        support: PAIR.DEFICITS[support] * comb(M - support, 11 - support)
        for support in (4, 5, 6)
    }
    objective = (
        [weights[4]] * 3
        + [weights[5]] * 4
        + [weights[6]] * 4
        + [weights[4], weights[5], weights[6]]
    )
    normalized_rows = [
        [coefficient / rhs for coefficient in row]
        for row, rhs in zip(rows, rhs_values)
    ]
    return normalized_rows, [1.0] * len(rows), bounds, objective, raw


def solve(method, rows, rhs, bounds, objective):
    scale = max(objective)
    result = linprog(
        [-coefficient / scale for coefficient in objective],
        A_ub=rows,
        b_ub=rhs,
        bounds=bounds,
        method=method,
        options={"presolve": True},
    )
    assert result.success, result.message
    optimum = sum(coefficient * value for coefficient, value in zip(objective, result.x))
    return {
        "method": method,
        "objective_estimate": int(round(optimum)),
        "minimum_normalized_slack": min(result.ineqlin.residual),
        "iterations": int(result.nit),
    }


def main() -> None:
    case, charges, adjacent, raw, caps = witness_caps()
    rows, rhs, bounds, objective, raw_caps = build_lp(caps)
    raw456 = sum(
        BASE.K71.LEDGER.DEFICITS[support] * caps[support - 2]
        for support in (4, 5, 6)
    )
    solves = [
        solve(method, rows, rhs, bounds, objective)
        for method in ("highs-ds", "highs-ipm")
    ]
    estimates = [row["objective_estimate"] for row in solves]
    repaired = raw - raw456 + max(estimates)
    print(json.dumps({
        "event": "HEURISTIC_ROUTE_PROBE",
        "case": case,
        "charges": charges,
        "adjacent_edges": adjacent,
        "union": UNION,
        "dimension": DIMENSION,
        "variables": 14,
        "inequalities": len(rows),
        "raw_caps": raw_caps,
        "raw": raw,
        "raw456": raw456,
        "solves": solves,
        "solver_disagreement": max(estimates) - min(estimates),
        "repaired_estimate": repaired,
        "leader": BASE.LEADER,
        "estimated_margin_to_leader": BASE.LEADER - repaired,
        "proof_status": "NONE_FLOAT_ROUTE_DECISION_ONLY",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
