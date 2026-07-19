#!/usr/bin/env python3
"""wclp_a_tranche_modal_v2.py -- hardened per-row sizing tranche for the
(1,5) weight-five sweep (v1 died when the heavyweight checkpoint scan hit the
280s function ceiling; the checkpoint tree turned out to hold ~16.7k batches).

Changes vs v1: no volume-wide scan (checkpoint state is analyzed locally from
a CLI download); 16-row shards; shard row budget 160s; per-row gp timeout
min(60, 250-elapsed); map-iteration failure containment.

READ-ONLY on the volume; cpu=1 so per-row wall == CPU.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import modal

ORDER = 512
DEGREE = 256
CLASS_COUNT = 2_296_920
REPRESENTATIVE_FILE = "/classes/weight5_affine_representatives.bin"
SHARD_SIZE = 16
ROW_BUDGET_SECONDS = 160.0
GP_TIMEOUT = 60
OUTPUT = Path(__file__).with_name("wclp_a_tranche_result.json")

app = modal.App("wclp-a-weight5-sizing-tranche-v2")
volume = modal.Volume.from_name("rs-mca-dli-wcl-weight5-affine-classes-v1")
image = modal.Image.debian_slim().pip_install("python-flint").apt_install("pari-gp")


@app.function(
    image=image,
    cpu=1,
    memory=2048,
    timeout=280,
    max_containers=40,
    volumes={"/classes": volume},
)
def measure_rows(payload: tuple[int, str, list[int]]) -> dict[str, object]:
    import struct
    import subprocess
    import sys
    import time as time_mod

    from flint import fmpz_poly

    sys.set_int_max_str_digits(0)
    shard_index, label, class_indices = payload
    shard_started = time_mod.monotonic()
    volume.reload()

    with open(REPRESENTATIVE_FILE, "rb") as handle:
        keys = []
        for class_index in class_indices:
            handle.seek(8 * class_index)
            packed = handle.read(8)
            if len(packed) != 8:
                raise AssertionError("representative read")
            keys.append(struct.unpack("<Q", packed)[0])

    def recursive_norm(value: fmpz_poly) -> int:
        width = DEGREE
        current = value
        while width > 1:
            next_width = width // 2
            even = fmpz_poly([int(current[2 * i]) for i in range(next_width)])
            odd = fmpz_poly([int(current[2 * i + 1]) for i in range(next_width)])
            paired = even * even - fmpz_poly([0, 1]) * odd * odd
            coefficients = [int(paired[i]) for i in range(width)]
            for i in range(next_width, width):
                coefficients[i - next_width] -= coefficients[i]
            current = fmpz_poly(coefficients[:next_width])
            width = next_width
        return abs(int(current[0]))

    records = []
    controls = 0
    for offset, (class_index, key) in enumerate(zip(class_indices, keys)):
        elapsed = time_mod.monotonic() - shard_started
        if elapsed > ROW_BUDGET_SECONDS:
            records.append({"class_index": class_index, "status": "SKIPPED_BUDGET"})
            continue
        terms = tuple((key >> (9 * index)) & 0x1FF for index in range(5))
        if len({term & 0xFF for term in terms}) != 5:
            raise AssertionError("antipodal collision")
        coefficients = [0] * DEGREE
        for term in terms:
            coefficients[term & 0xFF] += -1 if term & 0x100 else 1
        polynomial = fmpz_poly(coefficients)
        norm_started = time_mod.monotonic()
        norm = recursive_norm(polynomial)
        norm_seconds = time_mod.monotonic() - norm_started
        if norm == 0:
            raise AssertionError("characteristic-zero vanisher")
        if offset < 1:  # one exact generic-resultant control per shard
            cyclotomic = fmpz_poly([1] + [0] * (DEGREE - 1) + [1])
            if abs(int(cyclotomic.resultant(polynomial))) != norm:
                raise AssertionError("generic norm mismatch")
            controls += 1
        row_timeout = min(
            GP_TIMEOUT, max(5, int(250 - (time_mod.monotonic() - shard_started)))
        )
        program = (
            f"n={norm};f=factor(n);"
            "for(j=1,matsize(f)[1],if(!isprime(f[j,1]),error(\"nonprime\"));"
            "print(f[j,1],\":\",f[j,2]));quit()\n"
        )
        factor_started = time_mod.monotonic()
        timed_out = False
        factors: list[tuple[int, int]] = []
        try:
            completed = subprocess.run(
                ["gp", "-q", "-s", "536870912"],
                input=program,
                text=True,
                capture_output=True,
                timeout=row_timeout,
                check=True,
            )
            for line in completed.stdout.splitlines():
                if ":" in line:
                    prime_text, exponent_text = line.split(":", 1)
                    factors.append((int(prime_text), int(exponent_text)))
        except subprocess.TimeoutExpired:
            timed_out = True
        factor_seconds = time_mod.monotonic() - factor_started
        record: dict[str, object] = {
            "class_index": class_index,
            "key": key,
            "norm_bits": norm.bit_length(),
            "norm_seconds": round(norm_seconds, 6),
            "factor_seconds": round(factor_seconds, 6),
            "gp_timeout_used": row_timeout,
            "status": (
                ("TIMEOUT_60S" if row_timeout == GP_TIMEOUT else "TIMEOUT_SHORT")
                if timed_out
                else "COMPLETE"
            ),
        }
        if not timed_out:
            product = 1
            max_v2 = -1
            for prime, exponent in factors:
                product *= prime**exponent
                max_v2 = max(max_v2, ((prime - 1) & -(prime - 1)).bit_length() - 1)
            if product != norm:
                raise AssertionError("incomplete factorization")
            record["factor_count"] = len(factors)
            record["max_v2_prime_minus_1"] = max_v2
            record["max_prime_bits"] = max((p.bit_length() for p, _ in factors), default=0)
        records.append(record)
    return {
        "shard_index": shard_index,
        "label": label,
        "records": records,
        "generic_norm_controls": controls,
        "shard_seconds": round(time_mod.monotonic() - shard_started, 6),
    }


@app.local_entrypoint()
def main(frontier: int = 1_066_688) -> None:
    started = time.monotonic()
    contiguous = list(range(frontier, frontier + 128))
    remaining = CLASS_COUNT - frontier - 128
    stride = remaining // 384
    uniform = [frontier + 128 + 97 + j * stride for j in range(384)]
    assert max(uniform) < CLASS_COUNT

    payloads = []
    shard = 0
    for label, indices in (("contiguous", contiguous), ("uniform", uniform)):
        for start in range(0, len(indices), SHARD_SIZE):
            payloads.append((shard, label, indices[start : start + SHARD_SIZE]))
            shard += 1

    shards = []
    errors = []
    try:
        for row in measure_rows.map(
            payloads, order_outputs=False, return_exceptions=True
        ):
            if isinstance(row, BaseException):
                errors.append(repr(row))
            else:
                shards.append(row)
    except BaseException as exc:  # salvage partial results on infra raise
        errors.append(f"MAP_ABORT:{exc!r}")

    records = [
        {**record, "label": row["label"]}
        for row in shards
        for record in row["records"]
    ]
    result = {
        "schema": "wclp-a-weight5-sizing-tranche-v2",
        "scope": "sizing pilot only; no certificate claim",
        "class_count": CLASS_COUNT,
        "frontier_assumed": frontier,
        "gp_timeout_seconds": GP_TIMEOUT,
        "shards": len(shards),
        "shard_errors": errors,
        "records": records,
        "wall_seconds": round(time.monotonic() - started, 3),
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    measured = [r for r in records if r["status"].startswith(("COMPLETE", "TIMEOUT"))]
    print(
        "WCLP_A_TRANCHE_V2 "
        + json.dumps(
            {
                "shards": len(shards),
                "errors": len(errors),
                "measured_rows": len(measured),
                "timeouts_60s": sum(r["status"] == "TIMEOUT_60S" for r in measured),
                "timeouts_short": sum(r["status"] == "TIMEOUT_SHORT" for r in measured),
                "skipped": sum(r["status"] == "SKIPPED_BUDGET" for r in records),
            },
            sort_keys=True,
        )
    )
