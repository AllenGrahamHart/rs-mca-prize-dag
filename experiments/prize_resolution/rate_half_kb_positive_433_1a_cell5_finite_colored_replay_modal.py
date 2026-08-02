#!/usr/bin/env python3
"""Fresh finite-field colored-gcd replays on selected cell-5 fibers."""

import json
from pathlib import Path

import modal


DIRECTORY = Path(__file__).parent
FILES = (
    "probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_generic_guard_units.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization.py",
    "check_rate_half_kb_positive_433_1a_cell5_pair_localized_operator.py",
    "rate_half_kb_positive_433_1a_cell5_sparse_edge_probe.py",
    "rate_half_kb_positive_433_1a_cell5_lift_atlas_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_coordinate_map_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_coordinate_columns_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_localized_operator_merged_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients.bin",
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients_meta.json",
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_factorization_result.json",
    "rate_half_kb_positive_433_1a_cell5_pair_primitive_polynomial_result.json",
)
REMOTE_DIRECTORY = "/root/cell5_replay"

app = modal.App("rs-mca-positive-433-1a-cell5-finite-colored-replay")
image = modal.Image.debian_slim(python_version="3.12").pip_install("sympy==1.14.0")
for name in FILES:
    image = image.add_local_file(DIRECTORY / name, f"{REMOTE_DIRECTORY}/{name}")


@app.function(image=image, cpu=1.0, memory=2048, timeout=300)
def replay_batch(fibers, chart):
    import contextlib
    import hashlib
    import importlib
    import io
    import json
    import sys
    import time

    started = time.monotonic()
    if (
        not fibers
        or len(set(fibers)) != len(fibers)
        or any(not 0 <= fiber < 2130706433 for fiber in fibers)
        or chart not in range(2, 6)
    ):
        raise RuntimeError("finite replay parameter outside scope")
    sys.path.insert(0, REMOTE_DIRECTORY)
    probe = importlib.import_module(
        "probe_rate_half_kb_positive_433_1a_cell5_pair_colored_gcd_fiber"
    )
    guard = [[probe.P - 1], [0], [1]]
    one = [[1]]
    source_sha256 = {
        name: hashlib.sha256(Path(REMOTE_DIRECTORY, name).read_bytes()).hexdigest()
        for name in FILES
    }
    results = []
    for fiber in fibers:
        fiber_started = time.monotonic()
        probe.T = fiber
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            probe.main(chart_index=chart)
        result = json.loads(stream.getvalue())
        if result["status"] != "COMPLETE" or result["fiber"] != fiber:
            raise RuntimeError("finite probe did not complete")
        rows = [
            {
                "factor": row["factor"],
                "finite_factor": row["finite_factor"],
                "finite_factor_degree": row["finite_factor_degree"],
                "pair_degree": row["pair_degree"],
                "colored_degree": row["colored_degree"],
                "gcd_degree": row["gcd_degree"],
                "gcd_class": (
                    "e2_minus_1"
                    if row["gcd"] == guard
                    else "one"
                    if row["gcd"] == one
                    else "outside"
                ),
            }
            for row in result["rows"]
        ]
        excluded = rows and all(
            row["gcd_class"] in {"e2_minus_1", "one"} for row in rows
        )
        results.append(
            {
                "status": "COMPLETE",
                "fiber": fiber,
                "chart": chart,
                "classification": "EXCLUDED" if excluded else "SURVIVOR",
                "rows": rows,
                "source_sha256": source_sha256,
                "elapsed_seconds": round(time.monotonic() - fiber_started, 6),
                "scope": (
                    "fresh exact finite-field recomputation of the DE+/DE-/BE "
                    "necessary gcd on every specialized primitive subfactor; "
                    "no vertical-fiber, other-sign, cell, route, row, or Prize closure"
                ),
            }
        )
    return {
        "status": "COMPLETE",
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "results": results,
    }


@app.local_entrypoint()
def main(fibers: str, chart: int = 2, output: str = ""):
    selected = [int(value) for value in fibers.split(",") if value]
    if not selected or len(set(selected)) != len(selected):
        raise ValueError("fibers must be a nonempty distinct list")
    batch = replay_batch.remote(selected, chart)
    if batch["status"] != "COMPLETE":
        raise RuntimeError("remote replay batch did not complete")
    results = batch["results"]
    for result in results:
        compact = {key: value for key, value in result.items() if key not in {"rows", "source_sha256"}}
        compact["row_count"] = len(result["rows"])
        print(json.dumps(compact, sort_keys=True), flush=True)
    if output:
        Path(output).write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
