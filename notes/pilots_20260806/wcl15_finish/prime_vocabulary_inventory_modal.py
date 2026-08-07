#!/usr/bin/env python3
"""Independently inventory the easy-factor vocabulary for WCL `(1,5)`."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


CLASS_COUNT = 2_296_920
BATCH_SIZE = 64
EXPECTED_BATCHES = (CLASS_COUNT + BATCH_SIZE - 1) // BATCH_SIZE
AMBIENT_V2 = 41
CAP = 2**256
RUN_ID = "weight5-recursive-norm-full-v2"
AUDIT_RUN_ID = "weight5-recursive-norm-audit-v1"
REPRESENTATIVE_SHA256 = (
    "9ac0ca650e704a13514180fe2d8bcea94943c771f125b3942888a6aba8c87f00"
)
BATCH_ROOT = Path(f"/classes/{RUN_ID}/batch_summaries")
PRIME_ROOT = Path(f"/classes/{RUN_ID}/prime_shards")
AUDIT_ROOT = Path(f"/classes/{AUDIT_RUN_ID}")
VOCABULARY_FILE = AUDIT_ROOT / "easy_distinct_primes.txt"
REMOTE_RESULT_FILE = AUDIT_ROOT / "prime_vocabulary_inventory.json"
OUTPUT = Path(__file__).with_name("prime_vocabulary_inventory.json")

app = modal.App("rs-mca-wcl15-prime-vocabulary-audit")
volume = modal.Volume.from_name("rs-mca-dli-wcl-weight5-affine-classes-v1")
image = modal.Image.debian_slim()


def valuation_two(value: int) -> int:
    return (value & -value).bit_length() - 1


@app.function(
    image=image,
    cpu=2,
    memory=8192,
    timeout=900,
    max_containers=1,
    volumes={"/classes": volume},
)
def inventory_prime_vocabulary() -> dict[str, object]:
    import concurrent.futures
    import time

    started = time.monotonic()
    volume.reload()

    def read_pair(index: int) -> tuple[int, dict[str, object], list[int], str]:
        batch_path = BATCH_ROOT / f"part_{index:05d}.json"
        prime_path = PRIME_ROOT / f"part_{index:05d}.txt"
        batch_raw = batch_path.read_bytes()
        prime_raw = prime_path.read_bytes()
        batch = json.loads(batch_raw)
        if not prime_raw.endswith(b"\n"):
            raise AssertionError((index, "prime shard missing final newline"))
        lines = prime_raw.splitlines()
        primes = []
        previous = 0
        for line in lines:
            text = line.decode("ascii")
            if not text.isdigit() or (len(text) > 1 and text.startswith("0")):
                raise AssertionError((index, "noncanonical prime", text))
            prime = int(text)
            if prime <= previous:
                raise AssertionError((index, "unsorted or duplicate prime", prime))
            primes.append(prime)
            previous = prime
        return index, batch, primes, hashlib.sha256(prime_raw).hexdigest()

    global_primes: set[int] = set()
    custody = hashlib.sha256()
    total_factor_records = 0
    total_shard_records = 0
    maximum_prime_bits = 0
    maximum_v2 = -1
    high_gate_factors: list[dict[str, object]] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=96) as executor:
        rows = executor.map(read_pair, range(EXPECTED_BATCHES))
        for index, batch, primes, shard_digest in rows:
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
                key: [batch.get(key), value]
                for key, value in expected.items()
                if batch.get(key) != value
            }
            if mismatches:
                raise AssertionError((index, "batch custody", mismatches))
            if batch.get("batch_distinct_primes") != len(primes):
                raise AssertionError((index, "shard count"))

            shard_max_bits = max((prime.bit_length() for prime in primes), default=0)
            shard_max_v2 = max((valuation_two(prime - 1) for prime in primes), default=-1)
            if batch.get("max_prime_bits") != shard_max_bits:
                raise AssertionError((index, "maximum prime bits"))
            if batch.get("max_v2_prime_minus_1") != shard_max_v2:
                raise AssertionError((index, "maximum v2"))

            shard_high = [
                {
                    "batch_index": index,
                    "prime": str(prime),
                    "v2_prime_minus_1": valuation_two(prime - 1),
                }
                for prime in primes
                if prime < CAP and valuation_two(prime - 1) >= AMBIENT_V2
            ]
            if bool(shard_high) != bool(batch.get("high_gate_cases")):
                raise AssertionError((index, "high-gate summary disagreement"))
            high_gate_factors.extend(shard_high)
            global_primes.update(primes)
            total_factor_records += int(batch["factor_records"])
            total_shard_records += len(primes)
            maximum_prime_bits = max(maximum_prime_bits, shard_max_bits)
            maximum_v2 = max(maximum_v2, shard_max_v2)
            custody.update(f"{index}:{shard_digest}:{len(primes)}\n".encode())
            if (index + 1) % 2000 == 0:
                print(
                    f"vocabulary_progress batches={index + 1}/{EXPECTED_BATCHES} "
                    f"distinct={len(global_primes)}",
                    flush=True,
                )

    AUDIT_ROOT.mkdir(parents=True, exist_ok=True)
    vocabulary_digest = hashlib.sha256()
    vocabulary_temporary = Path(str(VOCABULARY_FILE) + ".tmp")
    with vocabulary_temporary.open("w") as handle:
        for prime in sorted(global_primes):
            line = f"{prime}\n"
            handle.write(line)
            vocabulary_digest.update(line.encode())
    vocabulary_temporary.replace(VOCABULARY_FILE)

    result = {
        "schema": "wcl15-prime-vocabulary-inventory-v1",
        "status": "COMPLETE",
        "source_run_id": RUN_ID,
        "audit_run_id": AUDIT_RUN_ID,
        "representative_sha256": REPRESENTATIVE_SHA256,
        "class_count": CLASS_COUNT,
        "batch_size": BATCH_SIZE,
        "validated_batches": EXPECTED_BATCHES,
        "factor_records": total_factor_records,
        "shard_prime_records": total_shard_records,
        "distinct_easy_primes": len(global_primes),
        "maximum_prime_bits": maximum_prime_bits,
        "maximum_v2_prime_minus_1": maximum_v2,
        "high_gate_factors": high_gate_factors,
        "shard_custody_digest": custody.hexdigest(),
        "vocabulary_sha256": vocabulary_digest.hexdigest(),
        "seconds": round(time.monotonic() - started, 6),
    }
    result["result_digest"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    result_temporary = Path(str(REMOTE_RESULT_FILE) + ".tmp")
    result_temporary.write_text(json.dumps(result, sort_keys=True) + "\n")
    result_temporary.replace(REMOTE_RESULT_FILE)
    volume.commit()
    return result


@app.local_entrypoint()
def main() -> None:
    result = inventory_prime_vocabulary.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "WCL15_PRIME_VOCABULARY "
        + json.dumps(
            {
                key: result[key]
                for key in (
                    "status",
                    "validated_batches",
                    "factor_records",
                    "shard_prime_records",
                    "distinct_easy_primes",
                    "maximum_prime_bits",
                    "maximum_v2_prime_minus_1",
                    "high_gate_factors",
                    "vocabulary_sha256",
                    "seconds",
                )
            },
            sort_keys=True,
        )
    )
