#!/usr/bin/env python3
"""Price an independent replay of WCL `(1,5)` norm-factor batches."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


CLASS_COUNT = 2_296_920
BATCH_SIZE = 64
EXPECTED_BATCHES = (CLASS_COUNT + BATCH_SIZE - 1) // BATCH_SIZE
DEGREE = 256
SAMPLE_SIZE = 128
GROUP_SIZE = 8
RUN_ID = "weight5-recursive-norm-full-v2"
AUDIT_RUN_ID = "weight5-recursive-norm-audit-v1"
PILOT_RUN_ID = "batch-replay-pilot-v1"
REPRESENTATIVE_SHA256 = (
    "9ac0ca650e704a13514180fe2d8bcea94943c771f125b3942888a6aba8c87f00"
)
SEED = b"wcl15-independent-batch-replay-pilot-v1"
REPRESENTATIVE_FILE = Path("/classes/weight5_affine_representatives.bin")
REPRESENTATIVE_METADATA_FILE = Path("/classes/weight5_affine_representatives.json")
BATCH_ROOT = Path(f"/classes/{RUN_ID}/batch_summaries")
PRIME_ROOT = Path(f"/classes/{RUN_ID}/prime_shards")
PILOT_ROOT = Path(f"/classes/{AUDIT_RUN_ID}/{PILOT_RUN_ID}")
GROUP_ROOT = PILOT_ROOT / "groups"
REMOTE_RESULT_FILE = PILOT_ROOT / "result.json"
OUTPUT = Path(__file__).with_name("batch_replay_pilot.json")

app = modal.App("rs-mca-wcl15-independent-batch-replay-pilot")
volume = modal.Volume.from_name("rs-mca-dli-wcl-weight5-affine-classes-v1")
image = modal.Image.debian_slim().pip_install("python-flint")


def sample_indices() -> tuple[int, ...]:
    selected = {0, 1, 2, 24_924, 35_887, 35_888, 35_889}
    counter = 0
    while len(selected) < SAMPLE_SIZE:
        digest = hashlib.sha256(SEED + counter.to_bytes(8, "big")).digest()
        selected.add(int.from_bytes(digest[:8], "big") % EXPECTED_BATCHES)
        counter += 1
    return tuple(sorted(selected))


SAMPLE_INDICES = sample_indices()
SELECTOR_DIGEST = hashlib.sha256(
    (",".join(map(str, SAMPLE_INDICES)) + "\n").encode()
).hexdigest()
GROUPS = tuple(
    SAMPLE_INDICES[start : start + GROUP_SIZE]
    for start in range(0, len(SAMPLE_INDICES), GROUP_SIZE)
)


def checkpoint_path(group_index: int) -> Path:
    return GROUP_ROOT / f"part_{group_index:02d}.json"


@app.function(
    image=image,
    cpu=1,
    memory=2048,
    timeout=420,
    max_containers=16,
    volumes={"/classes": volume},
)
def audit_group(payload: tuple[int, tuple[int, ...]]) -> dict[str, object]:
    import struct
    import time

    from flint import fmpz, fmpz_poly

    group_index, indices = payload
    started = time.monotonic()
    volume.reload()
    path = checkpoint_path(group_index)
    try:
        cached = json.loads(path.read_text())
        if (
            cached.get("schema") == "wcl15-batch-replay-pilot-group-v1"
            and cached.get("status") == "COMPLETE"
            and cached.get("selector_digest") == SELECTOR_DIGEST
            and cached.get("group_index") == group_index
            and cached.get("batch_indices") == list(indices)
        ):
            cached["cache_hit"] = True
            return cached
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
    checked_rows = checked_primes = checked_factor_records = 0
    unresolved_rows = 0
    norm_seconds = primality_seconds = division_seconds = 0.0
    custody = hashlib.sha256()
    error = None

    try:
        for batch_index in indices:
            batch_path = BATCH_ROOT / f"part_{batch_index:05d}.json"
            prime_path = PRIME_ROOT / f"part_{batch_index:05d}.txt"
            batch = json.loads(batch_path.read_text())
            start = batch_index * BATCH_SIZE
            end = min(start + BATCH_SIZE, CLASS_COUNT)
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

            prime_lines = prime_path.read_text().splitlines()
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
            checked_primes += len(primes)

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
                    unresolved_rows += 1
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
            checked_rows += end - start
            checked_factor_records += batch_factor_records
            custody.update(
                f"{batch_index}:{batch['candidate_digest']}:{batch['factor_digest']}\n".encode()
            )
    except Exception as exc:  # fail closed while preserving the checkpoint
        error = f"{type(exc).__name__}:{exc}"

    result = {
        "schema": "wcl15-batch-replay-pilot-group-v1",
        "status": "COMPLETE" if error is None else "FAIL",
        "source_run_id": RUN_ID,
        "pilot_run_id": PILOT_RUN_ID,
        "selector_digest": SELECTOR_DIGEST,
        "group_index": group_index,
        "batch_indices": list(indices),
        "checked_batches": len(indices) if error is None else checked_rows // BATCH_SIZE,
        "checked_rows": checked_rows,
        "checked_primes": checked_primes,
        "checked_factor_records": checked_factor_records,
        "unresolved_rows": unresolved_rows,
        "norm_seconds": round(norm_seconds, 6),
        "primality_seconds": round(primality_seconds, 6),
        "division_seconds": round(division_seconds, 6),
        "custody_digest": custody.hexdigest(),
        "error": error,
        "seconds": round(time.monotonic() - started, 6),
        "cache_hit": False,
    }
    GROUP_ROOT.mkdir(parents=True, exist_ok=True)
    temporary = Path(str(path) + ".tmp")
    temporary.write_text(json.dumps(result, sort_keys=True) + "\n")
    temporary.replace(path)
    volume.commit()
    return result


@app.function(
    image=modal.Image.debian_slim(),
    cpu=1,
    memory=1024,
    timeout=120,
    max_containers=1,
    volumes={"/classes": volume},
)
def aggregate_pilot() -> dict[str, object]:
    import time

    started = time.monotonic()
    volume.reload()
    rows = []
    missing = []
    for group_index, indices in enumerate(GROUPS):
        path = checkpoint_path(group_index)
        try:
            row = json.loads(path.read_text())
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            missing.append({"group_index": group_index, "error": repr(exc)})
            continue
        if (
            row.get("schema") != "wcl15-batch-replay-pilot-group-v1"
            or row.get("selector_digest") != SELECTOR_DIGEST
            or row.get("group_index") != group_index
            or row.get("batch_indices") != list(indices)
        ):
            raise AssertionError((group_index, "group custody"))
        rows.append(row)

    failures = [
        {"group_index": row["group_index"], "error": row["error"]}
        for row in rows
        if row["status"] != "COMPLETE"
    ]
    checked_batches = sum(int(row["checked_batches"]) for row in rows)
    total_worker_seconds = sum(float(row["seconds"]) for row in rows)
    scale = EXPECTED_BATCHES / checked_batches if checked_batches else None
    projected_cpu_seconds = total_worker_seconds * scale if scale else None
    result = {
        "schema": "wcl15-batch-replay-pilot-v1",
        "status": (
            "COMPLETE"
            if not missing and not failures and checked_batches == SAMPLE_SIZE
            else "PARTIAL"
        ),
        "source_run_id": RUN_ID,
        "pilot_run_id": PILOT_RUN_ID,
        "selector_seed": SEED.decode(),
        "selector_digest": SELECTOR_DIGEST,
        "sample_indices": list(SAMPLE_INDICES),
        "expected_groups": len(GROUPS),
        "completed_groups": sum(row["status"] == "COMPLETE" for row in rows),
        "missing": missing,
        "failures": failures,
        "checked_batches": checked_batches,
        "checked_rows": sum(int(row["checked_rows"]) for row in rows),
        "checked_primes": sum(int(row["checked_primes"]) for row in rows),
        "checked_factor_records": sum(
            int(row["checked_factor_records"]) for row in rows
        ),
        "unresolved_rows": sum(int(row["unresolved_rows"]) for row in rows),
        "norm_seconds": round(sum(float(row["norm_seconds"]) for row in rows), 6),
        "primality_seconds": round(
            sum(float(row["primality_seconds"]) for row in rows), 6
        ),
        "division_seconds": round(
            sum(float(row["division_seconds"]) for row in rows), 6
        ),
        "worker_seconds": round(total_worker_seconds, 6),
        "maximum_group_seconds": max(
            (float(row["seconds"]) for row in rows), default=0.0
        ),
        "projected_full_cpu_seconds": (
            round(projected_cpu_seconds, 3) if projected_cpu_seconds else None
        ),
        "projected_100_container_wall_seconds": (
            round(projected_cpu_seconds / 100, 3) if projected_cpu_seconds else None
        ),
        "aggregate_seconds": round(time.monotonic() - started, 6),
    }
    result["result_digest"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    PILOT_ROOT.mkdir(parents=True, exist_ok=True)
    temporary = Path(str(REMOTE_RESULT_FILE) + ".tmp")
    temporary.write_text(json.dumps(result, sort_keys=True) + "\n")
    temporary.replace(REMOTE_RESULT_FILE)
    volume.commit()
    return result


@app.local_entrypoint()
def main(aggregate_only: bool = False) -> None:
    if not aggregate_only:
        payloads = tuple(enumerate(GROUPS))
        returned = list(
            audit_group.map(payloads, order_outputs=False, return_exceptions=True)
        )
        print(
            "WCL15_REPLAY_GROUPS "
            + json.dumps(
                {
                    "returned": len(returned),
                    "exceptions": sum(isinstance(row, Exception) for row in returned),
                },
                sort_keys=True,
            )
        )
    result = aggregate_pilot.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "WCL15_REPLAY_PILOT "
        + json.dumps(
            {
                key: result[key]
                for key in (
                    "status",
                    "selector_digest",
                    "completed_groups",
                    "checked_batches",
                    "checked_rows",
                    "checked_primes",
                    "failures",
                    "missing",
                    "worker_seconds",
                    "maximum_group_seconds",
                    "projected_full_cpu_seconds",
                    "projected_100_container_wall_seconds",
                )
            },
            sort_keys=True,
        )
    )
