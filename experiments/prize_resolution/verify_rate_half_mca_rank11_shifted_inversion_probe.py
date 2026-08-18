#!/usr/bin/env python3
"""Verify the bounded shifted-inversion Modal probe artifact."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "rate_half_mca_rank11_shifted_inversion_probe.cpp"
DISPATCHER = HERE / "rate_half_mca_rank11_shifted_inversion_probe_modal.py"
PREREGISTRATION = HERE / "rate_half_mca_rank11_shifted_inversion_probe_preregistration.md"
RESULT = HERE / "rate_half_mca_rank11_shifted_inversion_probe_result.json"
ROWS = HERE / "rate_half_mca_rank11_shifted_inversion_probe_rows.jsonl"
EXPECTED_HASHES = {
    "source": "2b4b73c5a9f828e0a669f338d225bd5365bd225f6e47adf61da76c78476f3f51",
    "dispatcher": "576a4d48040081e2a305f422eaa5483387e6237f2b9bb0c0dc3d483ff87652de",
    "preregistration": "cbd266ba908776a3c9345fc68f2e8b2eec8c57dafdefc11c00a92df66fd98763",
    "result": "48a6f15eca4cdbef6a6f545789ce3d3281c0a2d98e7783ada60f1db48a3a1170",
    "rows": "fc9d74d492b260ded5a9ac4501348db4ec7624655caba5987693b61ba0e690e8",
}


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_rows() -> list[list[object]]:
    return [json.loads(line) for line in ROWS.read_text().splitlines()]


def validate(summary: object, rows: object) -> dict[str, int]:
    require(isinstance(summary, dict) and isinstance(rows, list), "objects")
    require(
        summary.get("schema") == "rate-half-mca-rank11-shifted-inversion-probe-result-v1",
        "schema",
    )
    require(summary.get("status") == "COMPLETE" and summary.get("failures") == [], "complete")
    require((summary.get("p"), summary.get("domain_order")) == (2130706433, 2**21), "field")
    require(
        (
            summary.get("tau_shards_planned"),
            summary.get("parameters_per_shard"),
            summary.get("planned_parameter_count"),
            summary.get("completed_shards"),
            summary.get("completed_parameter_count"),
        )
        == (96, 64, 6144, 96, 6144),
        "coverage",
    )
    require(summary.get("threshold") == 8740, "threshold")
    require(
        summary.get("row_columns")
        == [
            "tau_index",
            "tau",
            "parameter_index",
            "kind",
            "kappa",
            "total_points",
            "fixed_points",
            "nonfixed_points",
        ],
        "columns",
    )
    require(summary.get("rows_file") == ROWS.name, "rows file")
    require(summary.get("rows_sha256") == EXPECTED_HASHES["rows"], "rows hash")
    require(len(rows) == 6144, "row count")

    p = 2130706433
    grouped: dict[int, list[list[object]]] = {index: [] for index in range(96)}
    counts: list[int] = []
    decoded = []
    for row in rows:
        require(isinstance(row, list) and len(row) == 8, "row shape")
        tau_index, tau, parameter_index, kind, kappa, total, fixed, nonfixed = row
        require(
            all(
                isinstance(value, int)
                for value in (tau_index, tau, parameter_index, kappa, total, fixed, nonfixed)
            ),
            "row integers",
        )
        require(0 <= tau_index < 96 and 0 <= parameter_index < 64, "row index")
        require(tau == pow(3, tau_index, p), "tau representative")
        require(kind == ("random" if parameter_index < 32 else "planted"), "kind")
        require(1 <= kappa < p, "kappa")
        require(0 <= fixed <= 2 and total == fixed + nonfixed, "point split")
        require(nonfixed >= 0 and nonfixed % 2 == 0, "orbit parity")
        grouped[tau_index].append(row)
        counts.append(nonfixed)
        decoded.append(
            {
                "tau_index": tau_index,
                "tau": tau,
                "parameter_index": parameter_index,
                "kind": kind,
                "kappa": kappa,
                "total_points": total,
                "fixed_points": fixed,
                "nonfixed_points": nonfixed,
            }
        )
    for tau_index, shard in grouped.items():
        require([row[2] for row in shard] == list(range(64)), f"parameter coverage {tau_index}")
        require(len({row[4] for row in shard}) == 64, f"kappa uniqueness {tau_index}")

    ordered = sorted(counts)
    maximum = max(ordered)
    maximizers = [row for row in decoded if row["nonfixed_points"] == maximum]
    quantiles = {
        label: ordered[((len(ordered) - 1) * numerator) // 100]
        for label, numerator in (("q50", 50), ("q90", 90), ("q99", 99))
    }
    require(maximum == summary.get("maximum_nonfixed_points") == 2336, "maximum")
    require(maximizers == summary.get("maximizing_rows"), "maximizers")
    require(
        quantiles
        == summary.get("quantiles")
        == {"q50": 2066, "q90": 2150, "q99": 2218},
        "quantiles",
    )
    require(not summary.get("candidate_cap_falsified") and maximum < 8740, "verdict")
    require("heuristic evidence" in str(summary.get("nonclaim")).lower(), "nonclaim")

    metrics = summary.get("shard_metrics")
    require(isinstance(metrics, list) and len(metrics) == 96, "metrics")
    require(all(row.get("event") == "SHARD_RESULT" for row in metrics), "metric events")
    require([row.get("tau_index") for row in metrics] == list(range(96)), "metric coverage")
    maximum_rss = 0
    for row in metrics:
        stderr = str(row.get("stderr"))
        require("RSS_KB=" in stderr and "WALL=" in stderr, "resource metric")
        maximum_rss = max(maximum_rss, int(stderr.split("RSS_KB=")[1].split()[0]))
        require(float(row.get("seconds")) < 60, "shard timeout")
    return {"maximum": maximum, "gap": 8740 - maximum, "maximum_rss_kb": maximum_rss}


def tamper_selftest(summary: dict[str, object], rows: list[list[object]]) -> int:
    mutations = (
        lambda s, r: s.__setitem__("completed_shards", 95),
        lambda s, r: s.__setitem__("threshold", 2336),
        lambda s, r: s.__setitem__("maximum_nonfixed_points", 2338),
        lambda s, r: s.__setitem__("candidate_cap_falsified", True),
        lambda s, r: s["quantiles"].__setitem__("q99", 2220),
        lambda s, r: r[0].__setitem__(7, r[0][7] + 1),
        lambda s, r: r[32].__setitem__(3, "random"),
        lambda s, r: s.__setitem__("nonclaim", "uniform theorem proved"),
    )
    caught = 0
    for mutate in mutations:
        altered_summary = copy.deepcopy(summary)
        altered_rows = copy.deepcopy(rows)
        mutate(altered_summary, altered_rows)
        try:
            validate(altered_summary, altered_rows)
        except (Reject, KeyError, TypeError, ValueError):
            caught += 1
    require(caught == len(mutations), "mutations")
    return caught


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tamper-selftest", action="store_true")
    args = parser.parse_args()
    paths = {
        "source": SOURCE,
        "dispatcher": DISPATCHER,
        "preregistration": PREREGISTRATION,
        "result": RESULT,
        "rows": ROWS,
    }
    require(
        all(sha256(path) == EXPECTED_HASHES[name] for name, path in paths.items()),
        "artifact hashes",
    )
    summary = json.loads(RESULT.read_text())
    require(summary.get("source_sha256") == EXPECTED_HASHES["source"], "source pin")
    require(summary.get("dispatcher_sha256") == EXPECTED_HASHES["dispatcher"], "dispatcher pin")
    require(
        summary.get("preregistration_sha256") == EXPECTED_HASHES["preregistration"],
        "preregistration pin",
    )
    rows = load_rows()
    checked = validate(summary, rows)
    if args.tamper_selftest:
        print(f"SHIFTED_INVERSION_PROBE_TAMPER_PASS mutations={tamper_selftest(summary, rows)}/8")
        return
    print(
        "SHIFTED_INVERSION_PROBE_PASS "
        f"maximum={checked['maximum']} threshold_gap={checked['gap']} "
        f"maximum_rss_kb={checked['maximum_rss_kb']}"
    )


if __name__ == "__main__":
    main()
