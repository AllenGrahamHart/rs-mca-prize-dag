#!/usr/bin/env python3
"""Resolve every retained hard-tail norm from the weight-five easy pass."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


CLASS_COUNT = 2_296_920
BATCH_SIZE = 64
AMBIENT_V2 = 41
CAP = 2**256
EASY_RUN_ID = "weight5-recursive-norm-full-v2"
TAIL_RUN_ID = "weight5-recursive-norm-tail-v1"
EASY_ROOT = f"/classes/{EASY_RUN_ID}"
EASY_BATCH_ROOT = f"{EASY_ROOT}/batch_summaries"
EASY_PRIME_FILE = f"{EASY_ROOT}/distinct_primes.txt"
TAIL_ROOT = f"/classes/{TAIL_RUN_ID}"
TAIL_MANIFEST_FILE = f"{TAIL_ROOT}/manifest.json"
TAIL_FACTOR_ROOT = f"{TAIL_ROOT}/factors"
TAIL_PRIME_FILE = f"{TAIL_ROOT}/combined_distinct_primes.txt"
TAIL_RESULT_FILE = f"{TAIL_ROOT}/result.json"
OUTPUT = Path(__file__).with_name(
    "dli_wcl_weight5_recursive_norm_tail_result.json"
)

app = modal.App("rs-mca-dli-wcl-weight5-recursive-norm-tail")
volume = modal.Volume.from_name("rs-mca-dli-wcl-weight5-affine-classes-v1")
image = modal.Image.debian_slim().apt_install("pari-gp")


def valuation_two(value: int) -> int:
    return (value & -value).bit_length() - 1


@app.function(
    image=image,
    cpu=2,
    memory=4096,
    timeout=900,
    volumes={"/classes": volume},
)
def compile_tail_manifest() -> dict[str, object]:
    import time

    started = time.monotonic()
    volume.reload()
    expected_batches = (CLASS_COUNT + BATCH_SIZE - 1) // BATCH_SIZE
    by_norm: dict[str, dict[str, object]] = {}
    easy_unresolved = 0
    for batch_index in range(expected_batches):
        start = batch_index * BATCH_SIZE
        end = min(start + BATCH_SIZE, CLASS_COUNT)
        path = f"{EASY_BATCH_ROOT}/part_{batch_index:05d}.json"
        with open(path) as handle:
            batch = json.load(handle)
        expected = {
            "schema": "dli-wcl-weight5-recursive-norm-batch-v2",
            "run_id": EASY_RUN_ID,
            "status": "COMPLETE",
            "batch_index": batch_index,
            "start": start,
            "end": end,
            "rows": end - start,
        }
        if any(batch.get(key) != value for key, value in expected.items()):
            raise AssertionError((batch_index, "easy checkpoint"))
        for case in batch["unresolved_cases"]:
            easy_unresolved += 1
            norm = case["norm"]
            if str(int(norm)) != norm or int(norm).bit_length() != case["norm_bits"]:
                raise AssertionError((batch_index, "tail norm"))
            row = by_norm.setdefault(
                norm,
                {
                    "norm": norm,
                    "norm_bits": case["norm_bits"],
                    "classes": [],
                },
            )
            if row["norm_bits"] != case["norm_bits"]:
                raise AssertionError((norm, "norm bits"))
            row["classes"].append(
                {
                    "class_index": case["class_index"],
                    "key": case["key"],
                    "reason": case["reason"],
                }
            )

    rows = sorted(by_norm.values(), key=lambda row: int(row["norm"]))
    digest = hashlib.sha256()
    for tail_index, row in enumerate(rows):
        row["tail_index"] = tail_index
        row["classes"].sort(key=lambda case: (case["class_index"], case["key"]))
        class_text = ",".join(
            f"{case['class_index']}:{case['key']}:{case['reason']}"
            for case in row["classes"]
        )
        digest.update(f"{row['norm']}:{class_text}\n".encode())
    manifest = {
        "schema": "dli-wcl-weight5-recursive-norm-tail-manifest-v1",
        "status": "COMPLETE",
        "easy_run_id": EASY_RUN_ID,
        "tail_run_id": TAIL_RUN_ID,
        "easy_batches": expected_batches,
        "easy_unresolved_cases": easy_unresolved,
        "distinct_tail_norms": len(rows),
        "manifest_digest": digest.hexdigest(),
        "rows": rows,
        "seconds": round(time.monotonic() - started, 6),
    }
    Path(TAIL_ROOT).mkdir(parents=True, exist_ok=True)
    temporary = TAIL_MANIFEST_FILE + ".tmp"
    Path(temporary).write_text(json.dumps(manifest, sort_keys=True) + "\n")
    Path(temporary).replace(TAIL_MANIFEST_FILE)
    volume.commit()
    return manifest


@app.function(
    image=image,
    cpu=1,
    memory=2048,
    timeout=420,
    max_containers=100,
    volumes={"/classes": volume},
)
def factor_tail(payload: tuple[int, str]) -> dict[str, object]:
    import math
    import re
    import subprocess
    import time

    tail_index, norm_text = payload
    norm = int(norm_text)
    if tail_index < 0 or norm <= 0 or str(norm) != norm_text:
        raise AssertionError("tail payload")
    path = f"{TAIL_FACTOR_ROOT}/part_{tail_index:05d}.json"
    volume.reload()
    try:
        with open(path) as handle:
            checkpoint = json.load(handle)
        if (
            checkpoint.get("schema")
            == "dli-wcl-weight5-recursive-norm-tail-factor-v1"
            and checkpoint.get("tail_run_id") == TAIL_RUN_ID
            and checkpoint.get("tail_index") == tail_index
            and checkpoint.get("norm") == norm_text
            and checkpoint.get("status") == "COMPLETE"
        ):
            checkpoint["cache_hit"] = True
            return checkpoint
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    started = time.monotonic()
    program = (
        f"n={norm};f=factor(n);"
        "for(j=1,matsize(f)[1],if(!isprime(f[j,1]),error(\"nonprime factor\"));"
        "print(f[j,1],\":\",f[j,2]));quit()\n"
    )
    factors = []
    factors_by_index = {}
    error = None
    try:
        completed = subprocess.run(
            ["gp", "-q", "-s", "1073741824"],
            input=program,
            text=True,
            capture_output=True,
            timeout=300,
            check=True,
        )
        for line in completed.stdout.splitlines():
            match = re.fullmatch(r"\s*(\d+)\s*:\s*(\d+)\s*", line)
            if match:
                factors.append([match.group(1), int(match.group(2))])
        if not factors or math.prod(
            int(prime) ** exponent for prime, exponent in factors
        ) != norm:
            raise AssertionError("incomplete tail factorization")
    except subprocess.TimeoutExpired:
        error = "FACTOR_TIMEOUT_300S"
    except (subprocess.CalledProcessError, AssertionError) as exc:
        error = f"FACTOR_ERROR:{type(exc).__name__}:{exc}"

    high_gate_factors = []
    max_v2 = -1
    max_prime_bits = 0
    for prime_text, exponent in factors:
        prime = int(prime_text)
        valuation = valuation_two(prime - 1)
        max_v2 = max(max_v2, valuation)
        max_prime_bits = max(max_prime_bits, prime.bit_length())
        if prime < CAP and valuation >= AMBIENT_V2:
            high_gate_factors.append(
                {
                    "prime": prime_text,
                    "exponent": exponent,
                    "v2_prime_minus_1": valuation,
                }
            )
    result = {
        "schema": "dli-wcl-weight5-recursive-norm-tail-factor-v1",
        "tail_run_id": TAIL_RUN_ID,
        "status": "COMPLETE" if error is None else "PARTIAL",
        "tail_index": tail_index,
        "norm": norm_text,
        "norm_bits": norm.bit_length(),
        "factors": factors,
        "max_prime_bits": max_prime_bits,
        "max_v2_prime_minus_1": max_v2,
        "high_gate_factors": high_gate_factors,
        "error": error,
        "seconds": round(time.monotonic() - started, 6),
        "cache_hit": False,
    }
    Path(TAIL_FACTOR_ROOT).mkdir(parents=True, exist_ok=True)
    temporary = path + ".tmp"
    Path(temporary).write_text(json.dumps(result, sort_keys=True) + "\n")
    Path(temporary).replace(path)
    volume.commit()
    return result


@app.function(
    image=image,
    cpu=2,
    memory=4096,
    timeout=900,
    volumes={"/classes": volume},
)
def aggregate_tail() -> dict[str, object]:
    import time

    started = time.monotonic()
    volume.reload()
    with open(TAIL_MANIFEST_FILE) as handle:
        manifest = json.load(handle)
    if (
        manifest.get("schema")
        != "dli-wcl-weight5-recursive-norm-tail-manifest-v1"
        or manifest.get("status") != "COMPLETE"
        or manifest.get("tail_run_id") != TAIL_RUN_ID
    ):
        raise AssertionError("tail manifest")

    factors = []
    missing = []
    for row in manifest["rows"]:
        tail_index = row["tail_index"]
        path = f"{TAIL_FACTOR_ROOT}/part_{tail_index:05d}.json"
        try:
            with open(path) as handle:
                factor = json.load(handle)
        except (FileNotFoundError, json.JSONDecodeError) as exc:
            missing.append({"tail_index": tail_index, "error": repr(exc)})
            continue
        if (
            factor.get("schema")
            != "dli-wcl-weight5-recursive-norm-tail-factor-v1"
            or factor.get("tail_run_id") != TAIL_RUN_ID
            or factor.get("tail_index") != tail_index
            or factor.get("norm") != row["norm"]
        ):
            raise AssertionError((tail_index, "tail checkpoint"))
        factors.append(factor)
        factors_by_index[tail_index] = factor
        if factor["status"] != "COMPLETE":
            missing.append(
                {"tail_index": tail_index, "error": factor.get("error")}
            )

    prime_set = set()
    with open(EASY_PRIME_FILE) as handle:
        prime_set.update(int(line) for line in handle if line.strip())
    for factor in factors:
        if factor["status"] == "COMPLETE":
            prime_set.update(int(row[0]) for row in factor["factors"])
    Path(TAIL_ROOT).mkdir(parents=True, exist_ok=True)
    with open(TAIL_PRIME_FILE, "w") as handle:
        for prime in sorted(prime_set):
            handle.write(f"{prime}\n")

    high_gate_cases = []
    for row in manifest["rows"]:
        factor = factors_by_index.get(row["tail_index"])
        if factor is None:
            continue
        for candidate in factor["high_gate_factors"]:
            high_gate_cases.append(
                {
                    "tail_index": row["tail_index"],
                    "norm": row["norm"],
                    "classes": row["classes"],
                    **candidate,
                }
            )
    prime_digest = hashlib.sha256(
        "".join(f"{prime}\n" for prime in sorted(prime_set)).encode()
    ).hexdigest()
    result = {
        "schema": "dli-wcl-weight5-recursive-norm-tail-result-v1",
        "status": "COMPLETE" if not missing else "PARTIAL",
        "easy_run_id": EASY_RUN_ID,
        "tail_run_id": TAIL_RUN_ID,
        "manifest": manifest,
        "factor_results": factors,
        "missing": missing,
        "combined_distinct_primes": len(prime_set),
        "combined_prime_digest": prime_digest,
        "max_v2_prime_minus_1": max(
            (valuation_two(prime - 1) for prime in prime_set), default=-1
        ),
        "max_v2_below_cap": max(
            (valuation_two(prime - 1) for prime in prime_set if prime < CAP),
            default=-1,
        ),
        "high_gate_cases": high_gate_cases,
        "max_tail_seconds": max(
            (float(row["seconds"]) for row in factors), default=0.0
        ),
        "seconds": round(time.monotonic() - started, 6),
    }
    temporary = TAIL_RESULT_FILE + ".tmp"
    Path(temporary).write_text(json.dumps(result, sort_keys=True) + "\n")
    Path(temporary).replace(TAIL_RESULT_FILE)
    volume.commit()
    return result


@app.local_entrypoint()
def main() -> None:
    manifest = compile_tail_manifest.remote()
    payloads = [
        (int(row["tail_index"]), str(row["norm"])) for row in manifest["rows"]
    ]
    completed = 0
    cache_hits = 0
    client_errors = []
    remote_rows = factor_tail.map(
        payloads,
        order_outputs=False,
        return_exceptions=True,
    )
    for row in remote_rows:
        if isinstance(row, BaseException):
            client_errors.append({"error": repr(row)})
        else:
            completed += int(row["status"] == "COMPLETE")
            cache_hits += int(bool(row.get("cache_hit")))
    result = aggregate_tail.remote()
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["client_errors"] = client_errors
    result["cache_hits"] = cache_hits
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_WEIGHT5_RECURSIVE_NORM_TAIL "
        + json.dumps(
            {
                "status": result["status"],
                "tail_cases": manifest["easy_unresolved_cases"],
                "distinct_tail_norms": manifest["distinct_tail_norms"],
                "completed": completed,
                "cache_hits": cache_hits,
                "client_errors": len(client_errors),
                "missing": len(result["missing"]),
                "distinct_primes": result["combined_distinct_primes"],
                "max_v2_below_cap": result["max_v2_below_cap"],
                "eligible": len(result["high_gate_cases"]),
            },
            sort_keys=True,
        )
    )
