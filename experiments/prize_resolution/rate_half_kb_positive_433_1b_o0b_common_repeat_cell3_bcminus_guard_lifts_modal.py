#!/usr/bin/env python3
"""Lift BC- generic-rank guard roots through the genus-two common tower."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
ROOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_uncolored_guard_roots_result.json"
)
TOWER = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_"
    "cell3_bcminus_tower_certificate_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_guard_lifts_result.json"
)
REMOTE_ROOTS = "/root/roots.json"
PRIME = 2130706433
IOTA = 16711679

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcminus-guard-lifts")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(ROOTS, REMOTE_ROOTS)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=60, max_containers=48)
def lift(q_value):
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    context = fmpz_mod_poly_ctx(PRIME)
    variable = context([0, 1])

    def field_roots(coefficients):
        polynomial = context([value % PRIME for value in coefficients])
        if polynomial.is_zero():
            return None
        field_part = polynomial.gcd(pow(variable, PRIME, polynomial)-variable)
        _, factors = field_part.factor()
        values = []
        for factor, _ in factors:
            if int(factor.degree()) != 1:
                raise ValueError("field part has nonlinear factor")
            values.append(
                -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
            )
        return sorted(set(values))

    q2 = q_value*q_value % PRIME
    q3 = q2*q_value % PRIME
    numerator = (q3+2*q2+q_value+4) % PRIME
    denominator = (q3+6*q2+q_value) % PRIME
    row = {
        "q": q_value, "numerator": numerator, "denominator": denominator,
        "sign_rows": [],
    }
    if denominator == 0:
        row["status"] = "PROJECTION_DENOMINATOR_BOUNDARY"
        row["seconds"] = time.perf_counter()-started
        return row
    y_square = numerator*pow(denominator, -1, PRIME) % PRIME
    y_values = field_roots([-y_square, 0, 1])
    row["y_square"] = y_square
    row["y_values"] = y_values
    if not y_values:
        row["status"] = "NO_BASE_FIELD_Y"
        row["seconds"] = time.perf_counter()-started
        return row

    guarded_y_count = 0
    point_count = 0
    for y_value in y_values:
        y_row = {"y": y_value, "sign_rows": []}
        if (y_value-1) % PRIME == 0 or (q_value*y_value-1) % PRIME == 0:
            y_row["status"] = "MOBIUS_DENOMINATOR_BOUNDARY"
            row["sign_rows"].append(y_row)
            continue
        b_value = (q_value*y_value+1)*pow(q_value*y_value-1, -1, PRIME) % PRIME
        c_value = (y_value+1)*pow(y_value-1, -1, PRIME) % PRIME
        y_row.update({"b": b_value, "c": c_value})
        target_guard = (
            b_value*c_value*(b_value-1)*(b_value+1)
            *(c_value-1)*(c_value+1)*(b_value-c_value)*(b_value+c_value)
        ) % PRIME
        if target_guard == 0 or (b_value*c_value-1) % PRIME == 0:
            y_row["status"] = "TARGET_GUARD_BOUNDARY"
            row["sign_rows"].append(y_row)
            continue
        guarded_y_count += 1
        projection = (
            b_value**3*c_value**3+b_value**2*c_value**4
            +3*b_value**2*c_value**3-2*b_value**2*c_value**2
            -2*b_value**2*c_value-b_value**2-b_value*c_value**4
            -2*b_value*c_value**3-2*b_value*c_value**2
            +3*b_value*c_value+b_value+c_value
        ) % PRIME
        if projection:
            raise ValueError("projection replay")
        ratio = (c_value-b_value)*pow(b_value*c_value-1, -1, PRIME) % PRIME
        for epsilon_1, epsilon_2 in itertools.product((-1, 1), repeat=2):
            alpha = epsilon_1*(IOTA+epsilon_2)*ratio % PRIME
            beta = -epsilon_2*IOTA % PRIME
            r_values = field_roots([-beta, -alpha, 1])
            sign_row = {
                "epsilon": [epsilon_1, epsilon_2],
                "alpha": alpha, "beta": beta, "r_values": r_values,
                "points": [],
            }
            for r_value in r_values or []:
                r2 = r_value*r_value % PRIME
                t_value = epsilon_1*epsilon_2*r2 % PRIME
                labels = (1, t_value*t_value % PRIME, PRIME-1, r2, -r2 % PRIME)
                common_guard = (
                    r_value*t_value
                    * pow(b_value*c_value*(b_value-1)*(b_value+1)
                          *(c_value-1)*(c_value+1)*(b_value-c_value)
                          *(b_value+c_value), 1, PRIME)
                ) % PRIME
                common_guard = common_guard and all(
                    (labels[left]-labels[right]) % PRIME
                    for left in range(5) for right in range(left+1, 5)
                )
                relation = (
                    (b_value*c_value-1)
                    *(epsilon_1*epsilon_2*r2+epsilon_1*IOTA)
                    -(epsilon_2*IOTA+1)*r_value*(c_value-b_value)
                ) % PRIME
                if relation:
                    raise ValueError("r relation replay")
                point = {"r": r_value, "t": t_value,
                         "status": "GUARDED" if common_guard else "COMMON_GUARD_BOUNDARY"}
                sign_row["points"].append(point)
                if common_guard:
                    point_count += 1
            y_row["sign_rows"].append(sign_row)
        y_row["status"] = "LIFTED"
        row["sign_rows"].append(y_row)
    row["guarded_y_count"] = guarded_y_count
    row["guarded_point_count"] = point_count
    row["status"] = "LIFTED" if point_count else "NO_GUARDED_COMMON_POINT"
    row["seconds"] = time.perf_counter()-started
    return row


@app.local_entrypoint()
def main():
    roots = json.loads(ROOTS.read_text())
    q_values = roots["root_union"]
    raw = list(lift.map(q_values, order_outputs=True, return_exceptions=True))
    rows = []
    for q_value, row in zip(q_values, raw):
        if isinstance(row, BaseException):
            rows.append({"q": q_value, "status": "REMOTE_ERROR",
                         "error": repr(row)})
        else:
            rows.append(row)
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-guard-lifts-v1",
        "scope": (
            "Exact deployed-field lifts of every generic-rank guard root "
            "through the genus-two projection and four root-sign quadratics."
        ),
        "source_roots_sha256": hashlib.sha256(ROOTS.read_bytes()).hexdigest(),
        "source_tower_sha256": hashlib.sha256(TOWER.read_bytes()).hexdigest(),
        "q_count": len(rows),
        "status_counts": dict(sorted(Counter(row["status"] for row in rows).items())),
        "guarded_point_count": sum(row.get("guarded_point_count", 0) for row in rows),
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "q_count": len(rows),
        "status_counts": output["status_counts"],
        "guarded_point_count": output["guarded_point_count"],
        "maximum_seconds": max((row.get("seconds", 0) for row in rows), default=0),
    }, sort_keys=True))
