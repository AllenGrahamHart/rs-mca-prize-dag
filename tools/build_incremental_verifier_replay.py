#!/usr/bin/env python3
"""Replay only verifiers not covered by an unchanged pinned baseline."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tools" / "verifier_manifest.json"
BASELINE = ROOT / "experiments" / "prize_resolution" / "modal_verifier_replay.json"
OUTPUT = ROOT / "experiments" / "prize_resolution" / "incremental_verifier_replay.json"

sys.path.insert(0, str(ROOT / "tools"))

from run_all_verifiers import run_one, validate_manifest  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def indexed_pass_rows(replay: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if replay.get("complete") is not True or replay.get("match") != "":
        raise AssertionError("baseline replay is partial or filtered")
    rows = replay.get("results")
    if not isinstance(rows, list):
        raise AssertionError("baseline replay results are not a list")
    indexed: dict[str, dict[str, Any]] = {}
    for row in rows:
        rel = row.get("script")
        if not isinstance(rel, str) or rel in indexed:
            raise AssertionError(f"invalid or duplicate baseline row: {rel!r}")
        if row.get("status") != "PASS" or row.get("returncode") != 0:
            raise AssertionError(f"baseline row did not pass: {rel}")
        indexed[rel] = row
    counts = replay.get("counts", {})
    if counts.get("PASS") != len(indexed):
        raise AssertionError("baseline PASS count does not match its rows")
    for status in ("FAIL", "TIMEOUT", "HASH_MISMATCH", "REMOTE_ERROR"):
        if counts.get(status, 0) != 0:
            raise AssertionError(f"baseline reports {status}")
    return indexed


def write_certificate(payload: dict[str, Any]) -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--max-delta",
        type=int,
        required=True,
        help="refuse before execution if more scripts need replay",
    )
    parser.add_argument("--timeout", type=float, default=30.0)
    args = parser.parse_args()
    if args.max_delta < 0 or args.timeout <= 0:
        parser.error("limits must be positive")

    manifest = json.loads(MANIFEST.read_text())
    errors = validate_manifest(ROOT, manifest)
    if errors:
        raise AssertionError(errors)
    baseline = json.loads(BASELINE.read_text())
    baseline_rows = indexed_pass_rows(baseline)
    current = manifest["scripts"]

    unchanged = {
        rel
        for rel, expected_hash in current.items()
        if rel in baseline_rows and baseline_rows[rel].get("sha256") == expected_hash
    }
    delta = sorted(set(current) - unchanged)
    retired = sorted(set(baseline_rows) - set(current))
    changed = sorted(set(delta) & set(baseline_rows))
    if len(delta) > args.max_delta:
        raise AssertionError(
            f"delta has {len(delta)} scripts, exceeding --max-delta={args.max_delta}"
        )

    payload: dict[str, Any] = {
        "schema": "prize-verifier-composed-replay-v1",
        "complete": False,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "current_manifest_sha256": digest(MANIFEST),
        "baseline": {
            "path": BASELINE.relative_to(ROOT).as_posix(),
            "replay_sha256": digest(BASELINE),
            "manifest_sha256": baseline.get("manifest_sha256"),
            "historical_pass_count": len(baseline_rows),
            "unchanged_current_count": len(unchanged),
            "retired_scripts": retired,
        },
        "delta": {
            "execution": "local via tools/ramguard tiny",
            "timeout_seconds_per_script": args.timeout,
            "changed_baseline_scripts": changed,
            "expected_scripts": delta,
            "results": [],
        },
    }
    write_certificate(payload)

    print(
        "COMPOSED_REPLAY_PLAN "
        f"baseline_unchanged={len(unchanged)} delta={len(delta)} retired={len(retired)}"
    )
    rows: list[dict[str, Any]] = []
    for rel in delta:
        row = run_one(ROOT, rel, args.timeout)
        row["sha256"] = digest(ROOT / rel)
        rows.append(row)
        payload["delta"]["results"] = rows
        write_certificate(payload)
        print(f"{row['status']:7} {row['seconds']:8.3f}s  {rel}", flush=True)
        if row["status"] != "PASS":
            return 1

    payload["complete"] = True
    write_certificate(payload)
    print(
        "COMPOSED_REPLAY_PASS "
        f"baseline_unchanged={len(unchanged)} delta={len(rows)} "
        f"current_total={len(current)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
