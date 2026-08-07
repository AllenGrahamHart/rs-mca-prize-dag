#!/usr/bin/env python3
"""Bounded metadata inventory for the persisted WCL (1,5) census."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


CLASS_COUNT = 2_296_920
BATCH_SIZE = 64
EXPECTED_BATCHES = (CLASS_COUNT + BATCH_SIZE - 1) // BATCH_SIZE
RUN_ID = "weight5-recursive-norm-full-v2"
REPRESENTATIVE_SHA256 = (
    "9ac0ca650e704a13514180fe2d8bcea94943c771f125b3942888a6aba8c87f00"
)
BATCH_ROOT = Path(f"/classes/{RUN_ID}/batch_summaries")
PRIME_ROOT = Path(f"/classes/{RUN_ID}/prime_shards")
OUTPUT = Path(__file__).with_name("inventory.json")

app = modal.App("rs-mca-wcl15-finish-inventory")
volume = modal.Volume.from_name("rs-mca-dli-wcl-weight5-affine-classes-v1")
image = modal.Image.debian_slim()


def ranges(values: list[int]) -> list[list[int]]:
    if not values:
        return []
    out = []
    start = previous = values[0]
    for value in values[1:]:
        if value != previous + 1:
            out.append([start, previous])
            start = value
        previous = value
    out.append([start, previous])
    return out


@app.function(
    image=image,
    cpu=1,
    memory=1024,
    timeout=420,
    max_containers=1,
    volumes={"/classes": volume},
)
def inventory() -> dict[str, object]:
    import concurrent.futures
    import time

    started = time.monotonic()
    volume.reload()
    paths = sorted(BATCH_ROOT.glob("part_*.json"))
    prime_indices = {
        int(path.stem.removeprefix("part_"))
        for path in PRIME_ROOT.glob("part_*.txt")
    }
    valid_indices = set()
    invalid = []
    extras = []
    missing_prime_shards = []
    covered_rows = resolved_rows = unresolved_cases = 0
    unresolved_norms = set()
    high_gate_cases = []
    maximum_v2 = -1
    partial = False

    def read_one(path: Path) -> tuple[str, int | None, dict | None, str | None]:
        try:
            index = int(path.stem.removeprefix("part_"))
            row = json.loads(path.read_text())
        except (ValueError, OSError, json.JSONDecodeError) as error:
            return str(path), None, None, repr(error)
        return str(path), index, row, None

    scanned = 0
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=64)
    futures = [executor.submit(read_one, path) for path in paths]
    try:
        for future in concurrent.futures.as_completed(futures):
            if time.monotonic() - started > 390:
                partial = True
                break
            path_text, index, row, error = future.result()
            scanned += 1
            if error is not None or index is None or row is None:
                invalid.append({"path": path_text, "error": error})
                continue
            if not 0 <= index < EXPECTED_BATCHES:
                extras.append(index)
                continue
            start = index * BATCH_SIZE
            end = min(start + BATCH_SIZE, CLASS_COUNT)
            expected = {
                "schema": "dli-wcl-weight5-recursive-norm-batch-v2",
                "run_id": RUN_ID,
                "representative_sha256": REPRESENTATIVE_SHA256,
                "status": "COMPLETE",
                "batch_index": index,
                "start": start,
                "end": end,
                "rows": end - start,
            }
            mismatches = {
                key: [row.get(key), value]
                for key, value in expected.items()
                if row.get(key) != value
            }
            if mismatches or index in valid_indices:
                invalid.append(
                    {
                        "path": path_text,
                        "index": index,
                        "mismatches": mismatches,
                        "duplicate": index in valid_indices,
                    }
                )
                continue
            valid_indices.add(index)
            covered_rows += int(row["rows"])
            resolved_rows += int(row["resolved_rows"])
            cases = row.get("unresolved_cases", [])
            unresolved_cases += len(cases)
            unresolved_norms.update(str(case["norm"]) for case in cases)
            maximum_v2 = max(maximum_v2, int(row["max_v2_prime_minus_1"]))
            high_gate_cases.extend(row.get("high_gate_cases", []))
            if index not in prime_indices:
                missing_prime_shards.append(index)
            if scanned % 2000 == 0:
                print(
                    f"inventory_progress files={scanned}/{len(paths)} "
                    f"valid={len(valid_indices)} unresolved={unresolved_cases}",
                    flush=True,
                )
    finally:
        if partial:
            for future in futures:
                future.cancel()
        executor.shutdown(wait=not partial, cancel_futures=partial)

    missing = sorted(set(range(EXPECTED_BATCHES)) - valid_indices)
    payload = {
        "schema": "wcl15-finish-inventory-v1",
        "status": "PARTIAL" if partial else "COMPLETE",
        "run_id": RUN_ID,
        "representative_sha256": REPRESENTATIVE_SHA256,
        "class_count": CLASS_COUNT,
        "batch_size": BATCH_SIZE,
        "expected_batches": EXPECTED_BATCHES,
        "files_seen": len(paths),
        "files_scanned": scanned,
        "valid_batches": len(valid_indices),
        "covered_rows": covered_rows,
        "resolved_rows": resolved_rows,
        "unresolved_cases": unresolved_cases,
        "distinct_unresolved_norms": len(unresolved_norms),
        "maximum_v2_prime_minus_1": maximum_v2,
        "high_gate_cases": high_gate_cases,
        "invalid": invalid,
        "extra_indices": sorted(extras),
        "missing_prime_shards": sorted(missing_prime_shards),
        "missing_batches": len(missing),
        "missing_ranges": ranges(missing),
        "seconds": round(time.monotonic() - started, 6),
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["inventory_digest"] = hashlib.sha256(encoded.encode()).hexdigest()
    return payload


@app.local_entrypoint()
def main() -> None:
    result = inventory.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "WCL15_FINISH_INVENTORY "
        + json.dumps(
            {
                key: result[key]
                for key in (
                    "status",
                    "valid_batches",
                    "covered_rows",
                    "resolved_rows",
                    "unresolved_cases",
                    "distinct_unresolved_norms",
                    "missing_batches",
                    "maximum_v2_prime_minus_1",
                    "missing_prime_shards",
                    "invalid",
                    "seconds",
                )
            },
            sort_keys=True,
        )
    )
