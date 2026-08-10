#!/usr/bin/env python3
"""Extract deployed-field roots of the uncolored generic-rank guards."""

from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import time

import modal


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_uncolored_generic_rank_result.json"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_"
    "bcplus_uncolored_guard_roots_result.json"
)
REMOTE_SOURCE = "/root/generic_rank.json"
PRIME = 2130706433

app = modal.App("rs-mca-positive-433-1b-o0b-cell3-bcplus-uncolored-guard-roots")
image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("python-flint==0.8.0")
    .add_local_file(SOURCE, REMOTE_SOURCE)
)


@app.function(image=image, cpu=1.0, memory=1024, timeout=120, max_containers=54)
def roots(digest):
    from flint import fmpz_mod_poly_ctx

    started = time.perf_counter()
    payload = json.loads(Path(REMOTE_SOURCE).read_text())
    coefficients = [int(value) for value in payload["guard_atlas"][digest].split(",")]
    context = fmpz_mod_poly_ctx(PRIME)
    polynomial = context(coefficients)
    variable = context([0, 1])
    field_part = polynomial.gcd(pow(variable, PRIME, polynomial)-variable)
    _, factors = field_part.factor()
    values = []
    for factor, multiplicity in factors:
        if int(factor.degree()) != 1:
            raise ValueError("field part contains nonlinear factor")
        value = -int(factor[0])*pow(int(factor[1]), -1, PRIME) % PRIME
        values.append(value)
        if int(multiplicity) != 1:
            raise ValueError("squarefree field part has multiplicity")
    values.sort()
    return {
        "sha256": digest,
        "degree": int(polynomial.degree()),
        "field_part_degree": int(field_part.degree()),
        "roots": values,
        "field_part_coefficients": [
            int(field_part[index]) % PRIME
            for index in range(int(field_part.degree())+1)
        ],
        "seconds": time.perf_counter()-started,
    }


@app.local_entrypoint()
def main():
    payload = json.loads(SOURCE.read_text())
    digests = sorted(payload["guard_atlas"])
    raw = list(roots.map(digests, order_outputs=True, return_exceptions=True))
    rows = []
    for digest, row in zip(digests, raw):
        if isinstance(row, BaseException):
            rows.append({"sha256": digest, "status": "REMOTE_ERROR",
                         "error": repr(row)})
        else:
            rows.append({"status": "COMPLETE", **row})
    incidence = defaultdict(list)
    for row in rows:
        for value in row.get("roots", []):
            incidence[value].append(row["sha256"])
    output = {
        "schema": "rate-half-kb-positive-433-1b-o0b-cell3-bcplus-uncolored-guard-roots-v1",
        "scope": (
            "Exact F_2130706433 roots of every generic-rank construction "
            "and determinant guard; torus lifts and exceptional fibers unpaid."
        ),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "guard_count": len(rows),
        "status_counts": dict(sorted(Counter(row["status"] for row in rows).items())),
        "root_union": sorted(incidence),
        "root_incidence": {
            str(value): sorted(digests) for value, digests in sorted(incidence.items())
        },
        "rows": rows,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps({
        "result": str(RESULT),
        "guard_count": len(rows),
        "status_counts": output["status_counts"],
        "root_union_count": len(incidence),
        "root_incidence_count": sum(len(values) for values in incidence.values()),
        "field_part_degree_histogram": dict(sorted(Counter(
            str(row.get("field_part_degree")) for row in rows
        ).items())),
        "maximum_seconds": max(
            (row.get("seconds", 0) for row in rows), default=0
        ),
    }, sort_keys=True))
