#!/usr/bin/env python3
"""Replay every WCL `(1,5)` easy norm/factor batch independently."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


CLASS_COUNT = 2_296_920
BATCH_SIZE = 64
EXPECTED_BATCHES = (CLASS_COUNT + BATCH_SIZE - 1) // BATCH_SIZE
DEGREE = 256
GROUP_COUNT = 100
CHECKPOINT_BATCHES = 64
RUN_ID = "weight5-recursive-norm-full-v2"
AUDIT_RUN_ID = "weight5-recursive-norm-audit-v1"
FULL_RUN_ID = "full-batch-replay-v1"
REPRESENTATIVE_SHA256 = (
    "9ac0ca650e704a13514180fe2d8bcea94943c771f125b3942888a6aba8c87f00"
)
REPRESENTATIVE_FILE = Path("/classes/weight5_affine_representatives.bin")
REPRESENTATIVE_METADATA_FILE = Path("/classes/weight5_affine_representatives.json")
BATCH_ROOT = Path(f"/classes/{RUN_ID}/batch_summaries")
PRIME_ROOT = Path(f"/classes/{RUN_ID}/prime_shards")
FULL_ROOT = Path(f"/classes/{AUDIT_RUN_ID}/{FULL_RUN_ID}")
GROUP_ROOT = FULL_ROOT / "groups"
REMOTE_RESULT_FILE = FULL_ROOT / "result.json"
OUTPUT = Path(__file__).with_name("full_batch_replay.json")

app = modal.App("rs-mca-wcl15-full-independent-batch-replay")
volume = modal.Volume.from_name("rs-mca-dli-wcl-weight5-affine-classes-v1")
image = modal.Image.debian_slim().pip_install("python-flint")


def group_bounds(group_index: int) -> tuple[int, int]:
    return (
        group_index * EXPECTED_BATCHES // GROUP_COUNT,
        (group_index + 1) * EXPECTED_BATCHES // GROUP_COUNT,
    )


GROUP_BOUNDS = tuple(group_bounds(index) for index in range(GROUP_COUNT))
PARTITION_DIGEST = hashlib.sha256(
    "".join(f"{index}:{start}:{end}\n" for index, (start, end) in enumerate(GROUP_BOUNDS)).encode()
).hexdigest()


def checkpoint_path(group_index: int) -> Path:
    return GROUP_ROOT / f"part_{group_index:03d}.json"


def summarize_records(records: list[dict[str, object]]) -> dict[str, int | str]:
    custody = hashlib.sha256()
    for record in records:
        custody.update(
            f"{record['batch_index']}:{record['candidate_digest']}:"
            f"{record['factor_digest']}\n".encode()
        )
    return {
        "checked_batches": len(records),
        "checked_rows": sum(int(record["rows"]) for record in records),
        "checked_primes": sum(int(record["primes"]) for record in records),
        "checked_factor_records": sum(
            int(record["factor_records"]) for record in records
        ),
        "unresolved_rows": sum(
            int(record["unresolved_rows"]) for record in records
        ),
        "custody_digest": custody.hexdigest(),
    }


@app.function(
    image=image,
    cpu=1,
    memory=2048,
    timeout=420,
    max_containers=100,
    volumes={"/classes": volume},
)
def replay_group(group_index: int) -> dict[str, object]:
    import struct
    import time

    from flint import fmpz, fmpz_poly

    started = time.monotonic()
    volume.reload()
    start_batch, end_batch = GROUP_BOUNDS[group_index]
    path = checkpoint_path(group_index)
    records: list[dict[str, object]] = []
    norm_seconds = primality_seconds = division_seconds = 0.0
    prior_worker_seconds = 0.0
    try:
        cached = json.loads(path.read_text())
        if (
            cached.get("schema") == "wcl15-full-batch-replay-group-v1"
            and cached.get("source_run_id") == RUN_ID
            and cached.get("full_run_id") == FULL_RUN_ID
            and cached.get("partition_digest") == PARTITION_DIGEST
            and cached.get("group_index") == group_index
            and cached.get("start_batch") == start_batch
            and cached.get("end_batch") == end_batch
        ):
            if cached.get("status") == "COMPLETE":
                cached["cache_hit"] = True
                return cached
            if cached.get("status") == "PARTIAL":
                records = list(cached.get("records", []))
                expected_prefix = list(range(start_batch, start_batch + len(records)))
                if [record.get("batch_index") for record in records] != expected_prefix:
                    raise AssertionError((group_index, "partial prefix custody"))
                norm_seconds = float(cached.get("norm_seconds", 0.0))
                primality_seconds = float(cached.get("primality_seconds", 0.0))
                division_seconds = float(cached.get("division_seconds", 0.0))
                prior_worker_seconds = float(cached.get("seconds", 0.0))
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    with REPRESENTATIVE_METADATA_FILE.open() as handle:
        representative_metadata = json.load(handle)
    if (
        representative_metadata.get("status") != "COMPLETE"
        or representative_metadata.get("class_count") != CLASS_COUNT
        or representative_metadata.get("representative_digest")
        != REPRESENTATIVE_SHA256
    ):
        raise AssertionError("representative metadata")
    cyclotomic = fmpz_poly([1] + [0] * (DEGREE - 1) + [1])

    def write_checkpoint(status: str, error: str | None) -> dict[str, object]:
        summary = summarize_records(records)
        result = {
            "schema": "wcl15-full-batch-replay-group-v1",
            "status": status,
            "source_run_id": RUN_ID,
            "full_run_id": FULL_RUN_ID,
            "partition_digest": PARTITION_DIGEST,
            "group_index": group_index,
            "start_batch": start_batch,
            "end_batch": end_batch,
            **summary,
            "records": records,
            "norm_seconds": round(norm_seconds, 6),
            "primality_seconds": round(primality_seconds, 6),
            "division_seconds": round(division_seconds, 6),
            "error": error,
            "seconds": round(prior_worker_seconds + time.monotonic() - started, 6),
            "cache_hit": False,
        }
        GROUP_ROOT.mkdir(parents=True, exist_ok=True)
        temporary = Path(str(path) + ".tmp")
        temporary.write_text(json.dumps(result, sort_keys=True) + "\n")
        temporary.replace(path)
        volume.commit()
        return result

    try:
        for batch_index in range(start_batch + len(records), end_batch):
            start = batch_index * BATCH_SIZE
            end = min(start + BATCH_SIZE, CLASS_COUNT)
            batch = json.loads(
                (BATCH_ROOT / f"part_{batch_index:05d}.json").read_text()
            )
            expected = {
                "schema": "dli-wcl-weight5-recursive-norm-batch-v2",
                "run_id": RUN_ID,
                "representative_sha256": REPRESENTATIVE_SHA256,
                "status": "COMPLETE",
                "batch_index": batch_index,
                "start": start,
                "end": end,
                "rows": end - start,
            }
            mismatches = {
                key: [batch.get(key), value]
                for key, value in expected.items()
                if batch.get(key) != value
            }
            if mismatches:
                raise AssertionError((batch_index, "batch custody", mismatches))

            prime_lines = (
                PRIME_ROOT / f"part_{batch_index:05d}.txt"
            ).read_text().splitlines()
            primes = [int(line) for line in prime_lines]
            if any(
                str(prime) != line or prime <= 1
                for prime, line in zip(primes, prime_lines)
            ):
                raise AssertionError((batch_index, "noncanonical prime shard"))
            if primes != sorted(set(primes)):
                raise AssertionError((batch_index, "unsorted prime shard"))
            if len(primes) != batch["batch_distinct_primes"]:
                raise AssertionError((batch_index, "prime shard count"))

            prime_started = time.monotonic()
            composite = [prime for prime in primes if not bool(fmpz(prime).is_prime())]
            primality_seconds += time.monotonic() - prime_started
            if composite:
                raise AssertionError((batch_index, "composite shard entries", composite[:4]))

            with REPRESENTATIVE_FILE.open("rb") as handle:
                handle.seek(8 * start)
                raw = handle.read(8 * (end - start))
            keys = [row[0] for row in struct.iter_unpack("<Q", raw)]
            if len(keys) != end - start:
                raise AssertionError((batch_index, "representative read"))

            norms = []
            candidate_digest = hashlib.sha256()
            norm_started = time.monotonic()
            for key in keys:
                terms = tuple((key >> (9 * index)) & 0x1FF for index in range(5))
                if len({term & 0xFF for term in terms}) != 5:
                    raise AssertionError((batch_index, key, "antipodal collision"))
                coefficients = [0] * DEGREE
                for term in terms:
                    coefficients[term & 0xFF] += -1 if term & 0x100 else 1
                norm = abs(int(cyclotomic.resultant(fmpz_poly(coefficients))))
                if norm == 0:
                    raise AssertionError((batch_index, key, "zero norm"))
                norms.append(norm)
                candidate_digest.update(f"{key}:{norm}\n".encode())
            norm_seconds += time.monotonic() - norm_started
            if candidate_digest.hexdigest() != batch["candidate_digest"]:
                raise AssertionError((batch_index, "candidate digest"))

            unresolved = {
                int(case["class_index"]): case
                for case in batch.get("unresolved_cases", [])
            }
            factor_digest = hashlib.sha256()
            batch_factor_records = 0
            division_started = time.monotonic()
            for offset, (key, norm) in enumerate(zip(keys, norms)):
                class_index = start + offset
                if class_index in unresolved:
                    case = unresolved[class_index]
                    if case.get("key") != key or int(case.get("norm", 0)) != norm:
                        raise AssertionError((batch_index, class_index, "timeout custody"))
                    factor_digest.update(f"{key}:{norm}:TIMEOUT\n".encode())
                    continue

                remaining = norm
                factors = []
                for prime in primes:
                    if remaining % prime:
                        continue
                    exponent = 0
                    while remaining % prime == 0:
                        remaining //= prime
                        exponent += 1
                    factors.append((prime, exponent))
                if remaining != 1:
                    raise AssertionError(
                        (batch_index, class_index, "unexplained remainder", str(remaining))
                    )
                factor_text = ",".join(
                    f"{prime}^{exponent}" for prime, exponent in factors
                )
                factor_digest.update(f"{key}:{norm}:{factor_text}\n".encode())
                batch_factor_records += len(factors)
            division_seconds += time.monotonic() - division_started

            if factor_digest.hexdigest() != batch["factor_digest"]:
                raise AssertionError((batch_index, "factor digest"))
            if batch_factor_records != batch["factor_records"]:
                raise AssertionError((batch_index, "factor record count"))
            if end - start - len(unresolved) != batch["resolved_rows"]:
                raise AssertionError((batch_index, "resolved row count"))
            records.append(
                {
                    "batch_index": batch_index,
                    "rows": end - start,
                    "primes": len(primes),
                    "factor_records": batch_factor_records,
                    "unresolved_rows": len(unresolved),
                    "candidate_digest": batch["candidate_digest"],
                    "factor_digest": batch["factor_digest"],
                }
            )

            if len(records) % CHECKPOINT_BATCHES == 0:
                write_checkpoint("PARTIAL", None)
            if time.monotonic() - started > 380:
                return write_checkpoint("PARTIAL", "VOLUNTARY_TIME_CAP_380S")
    except Exception as exc:  # fail closed and retain the exact verified prefix
        return write_checkpoint("FAIL", f"{type(exc).__name__}:{exc}")

    return write_checkpoint("COMPLETE", None)


@app.function(
    image=modal.Image.debian_slim(),
    cpu=1,
    memory=1024,
    timeout=180,
    max_containers=1,
    volumes={"/classes": volume},
)
def aggregate_full_replay() -> dict[str, object]:
    import time

    started = time.monotonic()
    volume.reload()
    groups = []
    missing = []
    failures = []
    all_records = []
    for group_index, (start_batch, end_batch) in enumerate(GROUP_BOUNDS):
        path = checkpoint_path(group_index)
        try:
            row = json.loads(path.read_text())
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            missing.append({"group_index": group_index, "error": repr(exc)})
            continue
        expected = {
            "schema": "wcl15-full-batch-replay-group-v1",
            "source_run_id": RUN_ID,
            "full_run_id": FULL_RUN_ID,
            "partition_digest": PARTITION_DIGEST,
            "group_index": group_index,
            "start_batch": start_batch,
            "end_batch": end_batch,
        }
        if any(row.get(key) != value for key, value in expected.items()):
            raise AssertionError((group_index, "group custody"))
        records = list(row.get("records", []))
        expected_prefix = list(range(start_batch, start_batch + len(records)))
        if [record.get("batch_index") for record in records] != expected_prefix:
            raise AssertionError((group_index, "record prefix"))
        if summarize_records(records)["custody_digest"] != row.get("custody_digest"):
            raise AssertionError((group_index, "group digest"))
        all_records.extend(records)
        groups.append(
            {
                key: row[key]
                for key in (
                    "group_index",
                    "start_batch",
                    "end_batch",
                    "status",
                    "checked_batches",
                    "checked_rows",
                    "checked_primes",
                    "checked_factor_records",
                    "unresolved_rows",
                    "custody_digest",
                    "norm_seconds",
                    "primality_seconds",
                    "division_seconds",
                    "seconds",
                    "error",
                )
            }
        )
        if row["status"] != "COMPLETE":
            failures.append(
                {
                    "group_index": group_index,
                    "status": row["status"],
                    "error": row["error"],
                    "checked_batches": row["checked_batches"],
                }
            )

    indices = [record["batch_index"] for record in all_records]
    duplicate_batches = len(indices) - len(set(indices))
    covered = set(indices)
    missing_batches = sorted(set(range(EXPECTED_BATCHES)) - covered)
    status = (
        "COMPLETE"
        if not missing
        and not failures
        and not missing_batches
        and duplicate_batches == 0
        else "PARTIAL"
    )
    summary = summarize_records(all_records)
    if status == "COMPLETE":
        expected_summary = {
            "checked_batches": EXPECTED_BATCHES,
            "checked_rows": CLASS_COUNT,
            "checked_primes": 6_177_403,
            "checked_factor_records": 6_528_119,
            "unresolved_rows": 194,
        }
        mismatches = {
            key: [summary[key], value]
            for key, value in expected_summary.items()
            if summary[key] != value
        }
        if mismatches:
            raise AssertionError(("complete aggregate counts", mismatches))

    result = {
        "schema": "wcl15-full-batch-replay-v1",
        "status": status,
        "source_run_id": RUN_ID,
        "full_run_id": FULL_RUN_ID,
        "partition_digest": PARTITION_DIGEST,
        **summary,
        "expected_groups": GROUP_COUNT,
        "present_groups": len(groups),
        "complete_groups": sum(group["status"] == "COMPLETE" for group in groups),
        "missing_groups": missing,
        "incomplete_groups": failures,
        "missing_batches": len(missing_batches),
        "missing_batch_prefix": missing_batches[:100],
        "duplicate_batches": duplicate_batches,
        "groups": groups,
        "norm_seconds": round(sum(float(group["norm_seconds"]) for group in groups), 6),
        "primality_seconds": round(
            sum(float(group["primality_seconds"]) for group in groups), 6
        ),
        "division_seconds": round(
            sum(float(group["division_seconds"]) for group in groups), 6
        ),
        "worker_seconds": round(sum(float(group["seconds"]) for group in groups), 6),
        "maximum_group_seconds": max(
            (float(group["seconds"]) for group in groups), default=0.0
        ),
        "aggregate_seconds": round(time.monotonic() - started, 6),
    }
    result["result_digest"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    FULL_ROOT.mkdir(parents=True, exist_ok=True)
    temporary = Path(str(REMOTE_RESULT_FILE) + ".tmp")
    temporary.write_text(json.dumps(result, sort_keys=True) + "\n")
    temporary.replace(REMOTE_RESULT_FILE)
    volume.commit()
    return result


@app.local_entrypoint()
def main(aggregate_only: bool = False) -> None:
    if not aggregate_only:
        returned = list(
            replay_group.map(
                range(GROUP_COUNT), order_outputs=False, return_exceptions=True
            )
        )
        print(
            "WCL15_FULL_REPLAY_GROUPS "
            + json.dumps(
                {
                    "returned": len(returned),
                    "exceptions": sum(isinstance(row, Exception) for row in returned),
                },
                sort_keys=True,
            )
        )
    result = aggregate_full_replay.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "WCL15_FULL_REPLAY "
        + json.dumps(
            {
                key: result[key]
                for key in (
                    "status",
                    "partition_digest",
                    "complete_groups",
                    "checked_batches",
                    "checked_rows",
                    "checked_primes",
                    "checked_factor_records",
                    "unresolved_rows",
                    "missing_batches",
                    "incomplete_groups",
                    "worker_seconds",
                    "maximum_group_seconds",
                    "custody_digest",
                )
            },
            sort_keys=True,
        )
    )
