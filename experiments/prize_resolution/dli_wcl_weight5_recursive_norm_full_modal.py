#!/usr/bin/env python3
"""Exhaust terminal weight-five norms and their official split factors."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


ORDER = 512
DEGREE = 256
CLASS_COUNT = 2_296_920
BATCH_SIZE = 64
MERGE_GROUP_SIZE = 100
RUN_ID = "weight5-recursive-norm-full-v2"
REPRESENTATIVE_SHA256 = (
    "9ac0ca650e704a13514180fe2d8bcea94943c771f125b3942888a6aba8c87f00"
)
REPRESENTATIVE_FILE = "/classes/weight5_affine_representatives.bin"
REPRESENTATIVE_METADATA_FILE = "/classes/weight5_affine_representatives.json"
RUN_ROOT = f"/classes/{RUN_ID}"
BATCH_ROOT = f"{RUN_ROOT}/batch_summaries"
PRIME_SHARD_ROOT = f"{RUN_ROOT}/prime_shards"
PRIME_GROUP_ROOT = f"{RUN_ROOT}/prime_groups"
PRIME_FILE = f"{RUN_ROOT}/distinct_primes.txt"
REMOTE_RESULT_FILE = f"{RUN_ROOT}/result.json"
OUTPUT = Path(__file__).with_name("dli_wcl_weight5_recursive_norm_full_result.json")

app = modal.App("rs-mca-dli-wcl-weight5-recursive-norm-full")
volume = modal.Volume.from_name("rs-mca-dli-wcl-weight5-affine-classes-v1")
image = modal.Image.debian_slim().pip_install("python-flint").apt_install("pari-gp")


@app.function(
    image=image,
    cpu=2,
    memory=4096,
    timeout=2100,
    max_containers=500,
    volumes={"/classes": volume},
)
def process_batch(payload: tuple[int, int, int]) -> dict[str, object]:
    import concurrent.futures
    import hashlib
    import math
    import struct
    import subprocess
    import sys
    import time

    from flint import fmpz_poly

    sys.set_int_max_str_digits(0)
    batch_index, start, end = payload
    if not 0 <= start < end <= CLASS_COUNT or end - start > BATCH_SIZE:
        raise AssertionError("batch bounds")
    checkpoint_path = f"{BATCH_ROOT}/part_{batch_index:05d}.json"
    prime_path = f"{PRIME_SHARD_ROOT}/part_{batch_index:05d}.txt"
    volume.reload()
    try:
        with open(checkpoint_path) as handle:
            checkpoint = json.load(handle)
        if (
            checkpoint.get("schema") == "dli-wcl-weight5-recursive-norm-batch-v2"
            and checkpoint.get("run_id") == RUN_ID
            and checkpoint.get("representative_sha256") == REPRESENTATIVE_SHA256
            and checkpoint.get("batch_index") == batch_index
            and checkpoint.get("start") == start
            and checkpoint.get("end") == end
            and checkpoint.get("rows") == end - start
            and checkpoint.get("status") == "COMPLETE"
            and Path(prime_path).is_file()
        ):
            checkpoint["cache_hit"] = True
            return checkpoint
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    started = time.monotonic()
    with open(REPRESENTATIVE_METADATA_FILE) as handle:
        representative_metadata = json.load(handle)
    if (
        representative_metadata.get("status") != "COMPLETE"
        or representative_metadata.get("class_count") != CLASS_COUNT
        or representative_metadata.get("representative_digest")
        != REPRESENTATIVE_SHA256
    ):
        raise AssertionError("representative metadata")
    with open(REPRESENTATIVE_FILE, "rb") as handle:
        handle.seek(8 * start)
        raw = handle.read(8 * (end - start))
    keys = [row[0] for row in struct.iter_unpack("<Q", raw)]
    if len(keys) != end - start:
        raise AssertionError("representative read")

    def recursive_norm(value: fmpz_poly) -> int:
        width = DEGREE
        current = value
        while width > 1:
            next_width = width // 2
            even = fmpz_poly(
                [int(current[2 * index]) for index in range(next_width)]
            )
            odd = fmpz_poly(
                [int(current[2 * index + 1]) for index in range(next_width)]
            )
            paired = even * even - fmpz_poly([0, 1]) * odd * odd
            coefficients = [int(paired[index]) for index in range(width)]
            for index in range(next_width, width):
                coefficients[index - next_width] -= coefficients[index]
            current = fmpz_poly(coefficients[:next_width])
            width = next_width
        return abs(int(current[0]))

    norms = []
    candidate_digest = hashlib.sha256()
    for key in keys:
        terms = tuple((key >> (9 * index)) & 0x1FF for index in range(5))
        if len({term & 0xFF for term in terms}) != 5:
            raise AssertionError("antipodal collision")
        coefficients = [0] * DEGREE
        for term in terms:
            coefficients[term & 0xFF] += -1 if term & 0x100 else 1
        norm = recursive_norm(fmpz_poly(coefficients))
        if norm == 0:
            raise AssertionError((key, "characteristic-zero vanisher"))
        norms.append(norm)
        candidate_digest.update(f"{key}:{norm}\n".encode())

    factor_started = time.monotonic()
    factors_by_index: dict[int, list[tuple[int, int]]] = {}
    unresolved_cases = []

    def factor_one(
        item: tuple[int, tuple[int, int]],
    ) -> tuple[int, list[tuple[int, int]] | None, dict[str, object] | None]:
        offset, (key, norm) = item
        program = (
            f"n={norm};f=factor(n);"
            "for(j=1,matsize(f)[1],if(!isprime(f[j,1]),error(\"nonprime factor\"));"
            "print(f[j,1],\":\",f[j,2]));quit()\n"
        )
        try:
            completed = subprocess.run(
                ["gp", "-q", "-s", "536870912"],
                input=program,
                text=True,
                capture_output=True,
                timeout=60,
                check=True,
            )
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as exc:
            return (
                offset,
                None,
                {
                    "class_index": start + offset - 1,
                    "key": key,
                    "norm": str(norm),
                    "norm_bits": norm.bit_length(),
                    "reason": (
                        "FACTOR_TIMEOUT_60S"
                        if isinstance(exc, subprocess.TimeoutExpired)
                        else "FACTOR_PROCESS_ERROR"
                    ),
                },
            )
        factors = []
        for line in completed.stdout.splitlines():
            if ":" in line:
                prime_text, exponent_text = line.split(":", 1)
                factors.append((int(prime_text), int(exponent_text)))
        return offset, factors, None

    work = list(enumerate(zip(keys, norms), 1))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for offset, factors, unresolved in executor.map(factor_one, work):
            if unresolved is not None:
                unresolved_cases.append(unresolved)
            elif factors is not None:
                factors_by_index[offset] = factors
    factor_seconds = time.monotonic() - factor_started

    factor_digest = hashlib.sha256()
    prime_set = set()
    max_v2 = -1
    max_prime_bits = 0
    high_gate_cases = []
    factor_records = 0
    for offset, (key, norm) in enumerate(zip(keys, norms), 1):
        if offset not in factors_by_index:
            factor_digest.update(f"{key}:{norm}:TIMEOUT\n".encode())
            continue
        factors = factors_by_index[offset]
        if math.prod(prime**exponent for prime, exponent in factors) != norm:
            raise AssertionError((offset, "incomplete factorization"))
        factor_text = ",".join(f"{prime}^{exponent}" for prime, exponent in factors)
        factor_digest.update(f"{key}:{norm}:{factor_text}\n".encode())
        for prime, exponent in factors:
            factor_records += 1
            prime_set.add(prime)
            valuation = (prime - 1 & -(prime - 1)).bit_length() - 1
            max_v2 = max(max_v2, valuation)
            max_prime_bits = max(max_prime_bits, prime.bit_length())
            if prime < 2**256 and valuation >= 41:
                high_gate_cases.append(
                    {
                        "class_index": start + offset - 1,
                        "key": key,
                        "prime": str(prime),
                        "exponent": exponent,
                        "v2_prime_minus_1": valuation,
                    }
                )

    Path(PRIME_SHARD_ROOT).mkdir(parents=True, exist_ok=True)
    prime_temporary = prime_path + ".tmp"
    with open(prime_temporary, "w") as handle:
        for prime in sorted(prime_set):
            handle.write(f"{prime}\n")
    Path(prime_temporary).replace(prime_path)
    result = {
        "schema": "dli-wcl-weight5-recursive-norm-batch-v2",
        "run_id": RUN_ID,
        "representative_sha256": REPRESENTATIVE_SHA256,
        "status": "COMPLETE",
        "batch_index": batch_index,
        "start": start,
        "end": end,
        "rows": len(keys),
        "candidate_digest": candidate_digest.hexdigest(),
        "factor_digest": factor_digest.hexdigest(),
        "factor_records": factor_records,
        "resolved_rows": len(keys) - len(unresolved_cases),
        "unresolved_cases": unresolved_cases,
        "batch_distinct_primes": len(prime_set),
        "max_norm_bits": max(norm.bit_length() for norm in norms),
        "max_prime_bits": max_prime_bits,
        "max_v2_prime_minus_1": max_v2,
        "high_gate_cases": high_gate_cases,
        "factor_seconds": round(factor_seconds, 6),
        "seconds": round(time.monotonic() - started, 6),
        "cache_hit": False,
    }
    Path(BATCH_ROOT).mkdir(parents=True, exist_ok=True)
    checkpoint_temporary = checkpoint_path + ".tmp"
    Path(checkpoint_temporary).write_text(json.dumps(result, sort_keys=True) + "\n")
    Path(checkpoint_temporary).replace(checkpoint_path)
    volume.commit()
    return result


def merge_sorted_text(inputs: list[str], output: str) -> tuple[int, str]:
    import hashlib
    import heapq

    handles = []

    def rows(handle):
        for line in handle:
            yield int(line)

    digest = hashlib.sha256()
    count = 0
    previous = None
    try:
        iterators = []
        for path in inputs:
            handle = open(path)
            handles.append(handle)
            iterators.append(rows(handle))
        with open(output, "w") as target:
            for prime in heapq.merge(*iterators):
                if prime == previous:
                    continue
                target.write(f"{prime}\n")
                digest.update(f"{prime}\n".encode())
                previous = prime
                count += 1
    finally:
        for handle in handles:
            handle.close()
    return count, digest.hexdigest()


@app.function(
    image=image,
    cpu=1,
    memory=1024,
    timeout=300,
    max_containers=100,
    volumes={"/classes": volume},
)
def merge_prime_group(payload: tuple[int, list[int]]) -> dict[str, object]:
    import time

    group_index, batch_indices = payload
    started = time.monotonic()
    volume.reload()
    Path(PRIME_GROUP_ROOT).mkdir(parents=True, exist_ok=True)
    inputs = [f"{PRIME_SHARD_ROOT}/part_{index:05d}.txt" for index in batch_indices]
    output = f"{PRIME_GROUP_ROOT}/group_{group_index:03d}.txt"
    count, digest = merge_sorted_text(inputs, output)
    volume.commit()
    return {
        "group_index": group_index,
        "batch_indices": batch_indices,
        "prime_count": count,
        "digest": digest,
        "seconds": round(time.monotonic() - started, 6),
        "status": "COMPLETE",
    }


@app.function(
    image=image,
    cpu=1,
    memory=1024,
    timeout=300,
    volumes={"/classes": volume},
)
def merge_prime_groups(groups: list[dict[str, object]]) -> dict[str, object]:
    import time

    started = time.monotonic()
    volume.reload()
    groups = sorted(groups, key=lambda row: int(row["group_index"]))
    if any(row["status"] != "COMPLETE" for row in groups):
        raise AssertionError("prime group")
    inputs = [f"{PRIME_GROUP_ROOT}/group_{int(row['group_index']):03d}.txt" for row in groups]
    count, digest = merge_sorted_text(inputs, PRIME_FILE)
    max_prime_bits = 0
    max_v2 = -1
    with open(PRIME_FILE) as handle:
        for line in handle:
            prime = int(line)
            max_prime_bits = max(max_prime_bits, prime.bit_length())
            max_v2 = max(max_v2, (prime - 1 & -(prime - 1)).bit_length() - 1)
    volume.commit()
    return {
        "schema": "dli-wcl-weight5-recursive-norm-prime-vocabulary-v1",
        "status": "COMPLETE",
        "group_count": len(groups),
        "distinct_primes": count,
        "prime_digest": digest,
        "max_prime_bits": max_prime_bits,
        "max_v2_prime_minus_1": max_v2,
        "seconds": round(time.monotonic() - started, 6),
    }


@app.function(
    image=image,
    cpu=2,
    memory=4096,
    timeout=900,
    volumes={"/classes": volume},
)
def aggregate_checkpoints(
    row_count: int,
    groups: list[dict[str, object]],
    prime_vocabulary: dict[str, object] | None,
) -> dict[str, object]:
    import time

    started = time.monotonic()
    volume.reload()
    bounds = [
        (index, start, min(start + BATCH_SIZE, row_count))
        for index, start in enumerate(range(0, row_count, BATCH_SIZE))
    ]
    batches = []
    errors = []
    for batch_index, start, end in bounds:
        path = f"{BATCH_ROOT}/part_{batch_index:05d}.json"
        try:
            with open(path) as handle:
                row = json.load(handle)
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            errors.append(
                {
                    "batch_index": batch_index,
                    "bounds": [start, end],
                    "error": repr(exc),
                }
            )
            continue
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
            key: [row.get(key), value]
            for key, value in expected.items()
            if row.get(key) != value
        }
        if mismatches:
            errors.append(
                {
                    "batch_index": batch_index,
                    "bounds": [start, end],
                    "error": "CHECKPOINT_MISMATCH",
                    "mismatches": mismatches,
                }
            )
            continue
        batches.append(row)

    covered = sum(int(row["rows"]) for row in batches)
    unresolved_cases = [
        case for row in batches for case in row["unresolved_cases"]
    ]
    high_gate_cases = [
        case for row in batches for case in row["high_gate_cases"]
    ]
    result = {
        "schema": "dli-wcl-weight5-recursive-norm-full-v2",
        "run_id": RUN_ID,
        "scope": "complete" if row_count == CLASS_COUNT else "prefix test",
        "status": (
            "COMPLETE"
            if not errors
            and covered == row_count
            and prime_vocabulary
            and not unresolved_cases
            else "PARTIAL"
        ),
        "representative_sha256": REPRESENTATIVE_SHA256,
        "requested_rows": row_count,
        "covered_rows": covered,
        "batch_size": BATCH_SIZE,
        "batch_count": len(batches),
        "batches": batches,
        "errors": errors,
        "aggregate_candidate_digest": hashlib.sha256(
            "\n".join(str(row["candidate_digest"]) for row in batches).encode()
        ).hexdigest(),
        "aggregate_factor_digest": hashlib.sha256(
            "\n".join(str(row["factor_digest"]) for row in batches).encode()
        ).hexdigest(),
        "factor_records": sum(int(row["factor_records"]) for row in batches),
        "resolved_rows": sum(int(row["resolved_rows"]) for row in batches),
        "unresolved_cases": unresolved_cases,
        "max_norm_bits": max(
            (int(row["max_norm_bits"]) for row in batches), default=0
        ),
        "max_prime_bits": max(
            (int(row["max_prime_bits"]) for row in batches), default=0
        ),
        "max_v2_prime_minus_1": max(
            (int(row["max_v2_prime_minus_1"]) for row in batches), default=-1
        ),
        "high_gate_cases": high_gate_cases,
        "max_batch_seconds": max(
            (float(row["seconds"]) for row in batches), default=0.0
        ),
        "max_factor_seconds": max(
            (float(row["factor_seconds"]) for row in batches), default=0.0
        ),
        "prime_groups": groups,
        "prime_vocabulary": prime_vocabulary,
        "aggregate_seconds": round(time.monotonic() - started, 6),
    }
    Path(RUN_ROOT).mkdir(parents=True, exist_ok=True)
    temporary = REMOTE_RESULT_FILE + ".tmp"
    Path(temporary).write_text(json.dumps(result, sort_keys=True) + "\n")
    Path(temporary).replace(REMOTE_RESULT_FILE)
    volume.commit()
    return result


@app.function(
    image=image,
    cpu=1,
    memory=1024,
    timeout=300,
    volumes={"/classes": volume},
)
def checkpoint_progress() -> dict[str, object]:
    volume.reload()
    root = Path(BATCH_ROOT)
    if not root.is_dir():
        return {
            "run_id": RUN_ID,
            "batch_count": 0,
            "covered_rows": 0,
            "resolved_rows": 0,
            "unresolved_cases": 0,
            "high_gate_cases": 0,
        }
    rows = []
    for path in root.glob("part_*.json"):
        try:
            row = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        if (
            row.get("schema") == "dli-wcl-weight5-recursive-norm-batch-v2"
            and row.get("run_id") == RUN_ID
            and row.get("status") == "COMPLETE"
        ):
            rows.append(row)
    return {
        "run_id": RUN_ID,
        "batch_count": len(rows),
        "expected_batches": (CLASS_COUNT + BATCH_SIZE - 1) // BATCH_SIZE,
        "covered_rows": sum(int(row["rows"]) for row in rows),
        "resolved_rows": sum(int(row["resolved_rows"]) for row in rows),
        "unresolved_cases": sum(len(row["unresolved_cases"]) for row in rows),
        "high_gate_cases": sum(len(row["high_gate_cases"]) for row in rows),
        "max_v2_prime_minus_1": max(
            (int(row["max_v2_prime_minus_1"]) for row in rows), default=-1
        ),
        "max_norm_bits": max(
            (int(row["max_norm_bits"]) for row in rows), default=0
        ),
    }


@app.local_entrypoint()
def main(limit: int = 0) -> None:
    row_count = CLASS_COUNT if limit <= 0 else min(limit, CLASS_COUNT)
    bounds = [
        (index, start, min(start + BATCH_SIZE, row_count))
        for index, start in enumerate(range(0, row_count, BATCH_SIZE))
    ]
    completed = 0
    cache_hits = 0
    errors = []
    remote_rows = process_batch.map(
        bounds,
        order_outputs=False,
        return_exceptions=True,
    )
    for row in remote_rows:
        if isinstance(row, BaseException):
            errors.append({"error": repr(row)})
        else:
            completed += 1
            cache_hits += int(bool(row.get("cache_hit")))

    prime_vocabulary = None
    prime_groups = []
    if not errors and completed == len(bounds):
        group_payloads = [
            (group_index, list(range(start, min(start + MERGE_GROUP_SIZE, len(bounds)))))
            for group_index, start in enumerate(range(0, len(bounds), MERGE_GROUP_SIZE))
        ]
        merged_rows = list(merge_prime_group.map(group_payloads, return_exceptions=True))
        merge_errors = [repr(row) for row in merged_rows if isinstance(row, BaseException)]
        if merge_errors:
            errors.extend({"prime_merge_error": error} for error in merge_errors)
        else:
            prime_groups = merged_rows
            prime_vocabulary = merge_prime_groups.remote(prime_groups)

    result = aggregate_checkpoints.remote(row_count, prime_groups, prime_vocabulary)
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["client_errors"] = errors
    result["cache_hits"] = cache_hits
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_WEIGHT5_RECURSIVE_NORM_FULL "
        + json.dumps(
            {
                "scope": result["scope"],
                "status": result["status"],
                "covered": result["covered_rows"],
                "batches": result["batch_count"],
                "errors": len(errors),
                "cache_hits": cache_hits,
                "factor_records": result["factor_records"],
                "resolved": result["resolved_rows"],
                "unresolved": len(result["unresolved_cases"]),
                "distinct_primes": (
                    prime_vocabulary["distinct_primes"] if prime_vocabulary else None
                ),
                "max_norm_bits": result["max_norm_bits"],
                "max_prime_bits": result["max_prime_bits"],
                "max_v2": result["max_v2_prime_minus_1"],
                "eligible": len(result["high_gate_cases"]),
                "max_batch_seconds": result["max_batch_seconds"],
            },
            sort_keys=True,
        )
    )
