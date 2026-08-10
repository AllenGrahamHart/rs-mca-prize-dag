#!/usr/bin/env python3
"""Pay exceptional finite fibers of the uncolored generic-rank atlas."""

from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
GENERIC = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_uncolored_generic_rank_result.json"
)
ROOTS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_uncolored_guard_roots_result.json"
)
LIFTS = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_guard_lifts_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcminus_uncolored_exceptional_fibers_result.json"
)
SHARD_RESULTS = {
    record: DIRECTORY / (
        "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
        f"bcminus_uncolored_exceptional_{record.replace('+', 'plus')}_result.json"
    )
    for record in ("DE+", "DF+", "EF")
}
REMOTE_GENERIC = "/root/generic.json"
REMOTE_ROOTS = "/root/roots.json"
REMOTE_LIFTS = "/root/lifts.json"
PRIME = 2130706433
IOTA = 16711679
GLOBAL_RECORDS = ("BE", "CF", "DE+", "DE-", "DF+", "DF-", "EF")

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcminus-uncolored-exceptional")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(GENERIC, REMOTE_GENERIC)
    .add_local_file(ROOTS, REMOTE_ROOTS)
    .add_local_file(LIFTS, REMOTE_LIFTS)
)


def canonical_matchings(items):
    if not items:
        return ((),)
    output = []
    for index in range(1, len(items)):
        for tail in canonical_matchings(items[1:index]+items[index+1:]):
            output.append(((items[0], items[index]),)+tail)
    return tuple(output)


MATCHINGS = canonical_matchings(tuple(range(6)))


@app.function(image=image, cpu=1.0, memory=1536, timeout=180, max_containers=100)
def pay(case):
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    epsilon_1, epsilon_2, missing_record, sigma_o, pairing_index = case
    generic_payload = json.loads(Path(REMOTE_GENERIC).read_text())
    root_payload = json.loads(Path(REMOTE_ROOTS).read_text())
    lift_payload = json.loads(Path(REMOTE_LIFTS).read_text())
    generic_row = next(
        row for row in generic_payload["rows"]
        if row["epsilon"] == [epsilon_1, epsilon_2]
        and row["missing_record"] == missing_record
        and row["sigma_o"] == sigma_o
        and row["pairing_index"] == pairing_index
    )
    roots_by_hash = {row["sha256"]: row["roots"] for row in root_payload["rows"]}
    q_values = sorted({
        value for digest in generic_row["guard_hashes"]
        for value in roots_by_hash[digest]
    })
    lifts_by_q = {row["q"]: row for row in lift_payload["rows"]}

    context = fmpz_mod_poly_ctx(PRIME)
    variable = context([0, 1])

    def field_roots(polynomial):
        if polynomial.is_zero():
            return None
        if int(polynomial.degree()) == 0:
            return []
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

    def determinant(matrix):
        matrix = [[value % PRIME for value in row] for row in matrix]
        output = 1
        for column in range(len(matrix)):
            pivot = next(
                (row for row in range(column, len(matrix))
                 if matrix[row][column]),
                None,
            )
            if pivot is None:
                return 0
            if pivot != column:
                matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
                output = -output
            pivot_value = matrix[column][column]
            output = output*pivot_value % PRIME
            inverse = pow(pivot_value, -1, PRIME)
            for row in range(column+1, len(matrix)):
                factor = matrix[row][column]*inverse % PRIME
                for index in range(column, len(matrix)):
                    matrix[row][index] = (
                        matrix[row][index]-factor*matrix[column][index]
                    ) % PRIME
        return output % PRIME

    def polynomial_value(coefficients, value):
        return sum(coefficient*pow(value, index, PRIME)
                   for index, coefficient in enumerate(coefficients)) % PRIME

    def paired(a_values, b_values, left, right):
        p0, p1, p2 = (
            context([b_value])-left*a_value
            for a_value, b_value in zip(a_values, b_values)
        )
        q0 = context([b_values[0]])-right*a_values[0]
        q1 = context([-b_values[1]])+right*a_values[1]
        q2 = context([b_values[2]])-right*a_values[2]
        return (p2*q0-p0*q2)**2-(p2*q1-p1*q2)*(p1*q0-p0*q1)

    matching = MATCHINGS[pairing_index]
    residual_names = tuple(name for name in GLOBAL_RECORDS if name != missing_record)
    fibers = []
    status_counts = Counter()
    survivors = []
    unresolved = []
    for lift_row in (lifts_by_q[value] for value in q_values):
        point_rows = [
            (y_row, point)
            for y_row in lift_row.get("sign_rows", [])
            if y_row["status"] == "LIFTED"
            for sign_row in y_row["sign_rows"]
            if sign_row["epsilon"] == [epsilon_1, epsilon_2]
            for point in sign_row["points"]
            if point["status"] == "GUARDED"
        ]
        for y_row, point in point_rows:
            base_q = lift_row["q"]
            curve_y = y_row["y"]
            b_value = y_row["b"]
            c_value = y_row["c"]
            r_value = point["r"]
            fiber = {"base_q": base_q, "curve_y": curve_y, "r": r_value}
            r2, r4 = r_value*r_value % PRIME, pow(r_value, 4, PRIME)
            labels = (1, r4, PRIME-1, r2, -r2 % PRIME)
            products = (PRIME-1, b_value, c_value,
                        b_value*c_value % PRIME, b_value*c_value % PRIME)
            matrix = [
                [-product % PRIME, -product*label % PRIME,
                 -product*label*label % PRIME, 1, label,
                 label*label % PRIME]
                for product, label in zip(products, labels)
            ]
            cofactors = []
            for column in range(6):
                minor = [row[:column]+row[column+1:] for row in matrix]
                cofactors.append(((-1)**column*determinant(minor)) % PRIME)
            scale = r4*(1-r4) % PRIME
            kernel = [scale*value % PRIME for value in cofactors]
            a_values, b_values = kernel[:3], kernel[3:]
            a_pivot = sum(cofactors[index]*pow(r4, index, PRIME)
                          for index in range(3)) % PRIME
            beta_0 = (
                -epsilon_1*epsilon_2*r2*(1+b_value)*a_pivot
            ) % PRIME
            beta_1 = -beta_0 % PRIME
            missing_label = -r4 % PRIME
            a_missing = polynomial_value(a_values, missing_label)
            b_missing = polynomial_value(b_values, missing_label)
            beta_missing = (beta_0+beta_1*missing_label) % PRIME
            if a_missing == 0:
                fiber["status"] = (
                    "MISSING_PRODUCT_FREE" if b_missing == 0
                    else "MISSING_PRODUCT_INCONSISTENT"
                )
                if b_missing == 0:
                    unresolved.append({
                        "base_q": base_q, "curve_y": curve_y, "r": r_value,
                        "reason": fiber["status"],
                    })
                status_counts[fiber["status"]] += 1
                fibers.append(fiber)
                continue
            q_value = b_missing*pow(a_missing, -1, PRIME) % PRIME
            sum_squared = (
                missing_label*beta_missing*beta_missing
                * pow(a_missing, -2, PRIME)
            ) % PRIME
            fiber["q"] = q_value
            fiber["sum_squared"] = sum_squared
            if q_value == 0:
                fiber["status"] = "ZERO_MISSING_PRODUCT_BOUNDARY"
                status_counts[fiber["status"]] += 1
                fibers.append(fiber)
                continue
            endpoint_polynomial = context([
                q_value*q_value, 0, 2*q_value-sum_squared, 0, 1,
            ])
            endpoint_roots = field_roots(endpoint_polynomial)
            fiber["endpoint_roots"] = endpoint_roots
            if endpoint_roots is None:
                unresolved.append({
                    "base_q": base_q, "curve_y": curve_y, "r": r_value,
                    "reason": "ZERO_ENDPOINT_QUARTIC",
                })
                fiber["status"] = "ZERO_ENDPOINT_QUARTIC"
                status_counts[fiber["status"]] += 1
                fibers.append(fiber)
                continue
            endpoint_rows = []
            for endpoint in endpoint_roots:
                other = q_value*pow(endpoint, -1, PRIME) % PRIME
                if pow(endpoint+other, 2, PRIME) != sum_squared:
                    raise ValueError("endpoint reconstruction")
                if missing_record == "DE+":
                    records = {
                        "BE": context([b_value*other]),
                        "CF": context([0, c_value]),
                        "DE-": context([-q_value]),
                        "DF+": context([0, endpoint]),
                        "DF-": context([0, -endpoint]),
                        "EF": context([0, sigma_o*other]),
                    }
                elif missing_record == "DF+":
                    records = {
                        "BE": context([0, b_value]),
                        "CF": context([c_value*other]),
                        "DE+": context([0, endpoint]),
                        "DE-": context([0, -endpoint]),
                        "DF-": context([-q_value]),
                        "EF": context([0, sigma_o*other]),
                    }
                else:
                    f_value = sigma_o*other % PRIME
                    records = {
                        "BE": context([b_value*endpoint]),
                        "CF": context([c_value*f_value]),
                        "DE+": context([0, endpoint]),
                        "DE-": context([0, -endpoint]),
                        "DF+": context([0, f_value]),
                        "DF-": context([0, -f_value]),
                    }
                residual = tuple(records[name] for name in residual_names)
                equations = [
                    paired(a_values, b_values, residual[left], residual[right])
                    for left, right in matching
                ]
                common = equations[0]
                for equation in equations[1:]:
                    common = common.gcd(equation)
                y_roots = field_roots(common)
                endpoint_row = {
                    "endpoint": endpoint, "other": other,
                    "gcd_degree": int(common.degree()),
                    "y_roots": y_roots,
                }
                if y_roots is None:
                    endpoint_row["status"] = "FREE_RESIDUAL_COORDINATE"
                    unresolved.append({
                        "base_q": base_q, "curve_y": curve_y,
                        "r": r_value, "endpoint": endpoint,
                        "reason": endpoint_row["status"],
                    })
                    endpoint_rows.append(endpoint_row)
                    continue
                for y_value in y_roots:
                    if missing_record == "DE+":
                        coordinates = (1, b_value, c_value,
                                       endpoint, other, y_value)
                    elif missing_record == "DF+":
                        coordinates = (1, b_value, c_value,
                                       endpoint, y_value, other)
                    else:
                        coordinates = (1, b_value, c_value,
                                       y_value, endpoint, sigma_o*other % PRIME)
                    guarded = (
                        all(coordinates)
                        and all((coordinates[left]-coordinates[right]) % PRIME
                                and (coordinates[left]+coordinates[right]) % PRIME
                                for left, right in itertools.combinations(range(6), 2))
                    )
                    if guarded:
                        survivors.append({
                            "base_q": base_q, "curve_y": curve_y,
                            "r": r_value,
                            "endpoint": endpoint, "other": other,
                            "y": y_value, "coordinates": coordinates,
                        })
                endpoint_row["status"] = (
                    "CANDIDATE" if y_roots else "EMPTY_RESIDUAL_GCD"
                )
                endpoint_rows.append(endpoint_row)
            fiber["endpoint_rows"] = endpoint_rows
            fiber["status"] = (
                "CANDIDATE" if any(row["y_roots"] for row in endpoint_rows)
                else "EMPTY_ENDPOINT_FIBERS"
            )
            status_counts[fiber["status"]] += 1
            fibers.append(fiber)
    return {
        "epsilon": [epsilon_1, epsilon_2],
        "missing_record": missing_record,
        "sigma_o": sigma_o,
        "pairing_index": pairing_index,
        "q_values": q_values,
        "fiber_count": len(fibers),
        "status_counts": dict(sorted(status_counts.items())),
        "survivor_count": len(survivors),
        "survivors": survivors,
        "unresolved": unresolved,
        "fibers": fibers,
        "seconds": time.perf_counter()-started,
    }


@app.local_entrypoint()
def main(limit: int = 0):
    generic_payload = json.loads(GENERIC.read_text())
    cases = tuple(
        (row["epsilon"][0], row["epsilon"][1], row["missing_record"],
         row["sigma_o"], row["pairing_index"])
        for row in generic_payload["rows"]
    )
    if limit:
        cases = cases[:limit]
    raw = list(pay.map(cases, order_outputs=True, return_exceptions=True))
    rows = []
    for case, row in zip(cases, raw):
        if isinstance(row, BaseException):
            rows.append({
                "epsilon": list(case[:2]), "missing_record": case[2],
                "sigma_o": case[3], "pairing_index": case[4],
                "status": "REMOTE_ERROR", "error": repr(row),
            })
        else:
            rows.append({"status": "COMPLETE", **row})
    source_hashes = {
        "generic": hashlib.sha256(GENERIC.read_bytes()).hexdigest(),
        "roots": hashlib.sha256(ROOTS.read_bytes()).hexdigest(),
        "lifts": hashlib.sha256(LIFTS.read_bytes()).hexdigest(),
    }
    shards = {}
    for record, path in SHARD_RESULTS.items():
        shard_rows = [row for row in rows if row["missing_record"] == record]
        shard = {
            "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-uncolored-exceptional-shard-v1",
            "missing_record": record,
            "source_hashes": source_hashes,
            "case_count": len(shard_rows),
            "status_counts": dict(sorted(Counter(
                row["status"] for row in shard_rows
            ).items())),
            "fiber_count": sum(row.get("fiber_count", 0) for row in shard_rows),
            "survivor_count": sum(row.get("survivor_count", 0)
                                  for row in shard_rows),
            "unresolved_count": sum(len(row.get("unresolved", []))
                                    for row in shard_rows),
            "rows": shard_rows,
        }
        path.write_text(json.dumps(shard, indent=2, sort_keys=True)+"\n")
        shards[record] = {
            "file": path.name,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "case_count": len(shard_rows),
            "fiber_count": shard["fiber_count"],
        }

    compact_rows = []
    for row in rows:
        fibers = row.get("fibers", [])
        endpoint_rows = [endpoint for fiber in fibers
                         for endpoint in fiber.get("endpoint_rows", [])]
        compact_rows.append({
            "epsilon": row["epsilon"],
            "missing_record": row["missing_record"],
            "sigma_o": row["sigma_o"],
            "pairing_index": row["pairing_index"],
            "status": row["status"],
            "q_count": len(row.get("q_values", [])),
            "q_sha256": hashlib.sha256(json.dumps(
                row.get("q_values", []), separators=(",", ":")
            ).encode()).hexdigest(),
            "fiber_count": row.get("fiber_count", 0),
            "fiber_status_counts": dict(sorted(Counter(
                fiber["status"] for fiber in fibers
            ).items())),
            "endpoint_status_counts": dict(sorted(Counter(
                endpoint["status"] for endpoint in endpoint_rows
            ).items())),
            "endpoint_root_count": sum(
                len(fiber.get("endpoint_roots") or []) for fiber in fibers
            ),
            "residual_root_count": sum(
                len(endpoint.get("y_roots") or []) for endpoint in endpoint_rows
            ),
            "survivor_count": row.get("survivor_count", 0),
            "unresolved_count": len(row.get("unresolved", [])),
            "seconds": row.get("seconds", 0),
        })
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcminus-uncolored-exceptional-v1",
        "scope": (
            "Direct finite replay over every deployed-field root of each "
            "generic-rank guard, including missing-product quartics and "
            "residual paired-product gcds."
        ),
        "source_generic_sha256": source_hashes["generic"],
        "source_roots_sha256": source_hashes["roots"],
        "source_lifts_sha256": source_hashes["lifts"],
        "case_count": len(rows),
        "status_counts": dict(sorted(Counter(row["status"] for row in rows).items())),
        "survivor_count": sum(row.get("survivor_count", 0) for row in rows),
        "unresolved_count": sum(len(row.get("unresolved", [])) for row in rows),
        "shards": shards,
        "rows": compact_rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "case_count": len(rows),
        "status_counts": output["status_counts"],
        "survivor_count": output["survivor_count"],
        "unresolved_count": output["unresolved_count"],
        "fiber_count": sum(row.get("fiber_count", 0) for row in rows),
        "q_incidence_count": sum(len(row.get("q_values", [])) for row in rows),
        "maximum_seconds": max(
            (row.get("seconds", 0) for row in rows), default=0
        ),
        "shards": shards,
    }, sort_keys=True))
