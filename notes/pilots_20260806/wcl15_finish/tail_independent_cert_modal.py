#!/usr/bin/env python3
"""Independently certify the 193 completed WCL `(1,5)` hard tails."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import modal


INPUT = Path(
    "experiments/prize_resolution/"
    "dli_wcl_weight5_recursive_norm_tail_factor_only_result.json"
)
INPUT_SHA256 = "026fbd0d5665bc855bfcdd56f54b33bbea2b2a563aa98c79daf6e4f042ac0f4b"
REMOTE_INPUT = "/input/tail_factor_only_result.json"
OUTPUT = Path(__file__).with_name("tail_independent_cert.json")
TAIL_RUN_ID = "weight5-recursive-norm-tail-v1"
MANIFEST_DIGEST = "aa7fa74e79bb80f660ac6e5c6b9e03c85419630bef834076e1d1fe1380bf1ab8"
PRIME_DIGEST = "4180c683ce53c2df9181656ac8afb9fab287288bdab549f0a08326a31c800cbb"
CAP = 2**256
AMBIENT_V2 = 41

app = modal.App("rs-mca-wcl15-independent-hard-tail-cert")
image = (
    modal.Image.debian_slim()
    .pip_install("python-flint")
    .add_local_file(str(INPUT), REMOTE_INPUT, copy=True)
)


def valuation_two(value: int) -> int:
    return (value & -value).bit_length() - 1


@app.function(image=image, cpu=1, memory=1024, timeout=120)
def certify() -> dict[str, object]:
    import time

    from flint import fmpz

    started = time.monotonic()
    raw = Path(REMOTE_INPUT).read_bytes()
    source_sha256 = hashlib.sha256(raw).hexdigest()
    if source_sha256 != INPUT_SHA256:
        raise AssertionError(("source SHA-256", source_sha256))
    packet = json.loads(raw)
    if (
        packet.get("schema")
        != "dli-wcl-weight5-recursive-norm-tail-factor-only-v1"
        or packet.get("status") != "PARTIAL"
        or packet.get("tail_run_id") != TAIL_RUN_ID
    ):
        raise AssertionError("outer packet custody")

    manifest = packet["manifest"]
    if (
        manifest.get("schema")
        != "dli-wcl-weight5-recursive-norm-tail-manifest-v1"
        or manifest.get("status") != "COMPLETE"
        or manifest.get("tail_run_id") != TAIL_RUN_ID
        or manifest.get("distinct_tail_norms") != 194
        or manifest.get("easy_unresolved_cases") != 194
    ):
        raise AssertionError("manifest custody")
    manifest_rows = manifest["rows"]
    if len(manifest_rows) != 194:
        raise AssertionError("manifest length")

    manifest_hash = hashlib.sha256()
    manifest_by_index = {}
    norms = set()
    class_indices = set()
    for expected_index, row in enumerate(manifest_rows):
        if row.get("tail_index") != expected_index:
            raise AssertionError((expected_index, "tail index"))
        norm_text = row["norm"]
        if str(int(norm_text)) != norm_text or int(norm_text).bit_length() != row["norm_bits"]:
            raise AssertionError((expected_index, "norm custody"))
        if norm_text in norms:
            raise AssertionError((expected_index, "duplicate norm"))
        norms.add(norm_text)
        classes = sorted(
            row["classes"], key=lambda case: (case["class_index"], case["key"])
        )
        class_text = ",".join(
            f"{case['class_index']}:{case['key']}:{case['reason']}"
            for case in classes
        )
        manifest_hash.update(f"{norm_text}:{class_text}\n".encode())
        for case in classes:
            class_index = int(case["class_index"])
            if class_index in class_indices:
                raise AssertionError((expected_index, "duplicate class"))
            class_indices.add(class_index)
        manifest_by_index[expected_index] = row
    if manifest_hash.hexdigest() != MANIFEST_DIGEST:
        raise AssertionError(("manifest digest", manifest_hash.hexdigest()))
    if manifest.get("manifest_digest") != MANIFEST_DIGEST:
        raise AssertionError("printed manifest digest")

    factor_results = packet["factor_results"]
    if len(factor_results) != 193:
        raise AssertionError("factor result length")
    factors_by_index = {}
    prime_set = set()
    primality_checks = 0
    for result in factor_results:
        tail_index = int(result["tail_index"])
        if tail_index in factors_by_index or tail_index == 191:
            raise AssertionError((tail_index, "factor index"))
        manifest_row = manifest_by_index[tail_index]
        if (
            result.get("schema")
            != "dli-wcl-weight5-recursive-norm-tail-factor-v1"
            or result.get("status") != "COMPLETE"
            or result.get("tail_run_id") != TAIL_RUN_ID
            or result.get("norm") != manifest_row["norm"]
        ):
            raise AssertionError((tail_index, "factor custody"))
        factors = [(int(prime), int(exponent)) for prime, exponent in result["factors"]]
        if factors != sorted(factors) or len({prime for prime, _ in factors}) != len(factors):
            raise AssertionError((tail_index, "factor order"))
        if any(prime <= 1 or exponent <= 0 for prime, exponent in factors):
            raise AssertionError((tail_index, "factor sign"))
        if math.prod(prime**exponent for prime, exponent in factors) != int(result["norm"]):
            raise AssertionError((tail_index, "factor product"))
        composites = [prime for prime, _ in factors if not bool(fmpz(prime).is_prime())]
        primality_checks += len(factors)
        if composites:
            raise AssertionError((tail_index, "composite factors", composites))
        row_max_bits = max((prime.bit_length() for prime, _ in factors), default=0)
        row_max_v2 = max((valuation_two(prime - 1) for prime, _ in factors), default=-1)
        row_high = [
            {
                "prime": str(prime),
                "exponent": exponent,
                "v2_prime_minus_1": valuation_two(prime - 1),
            }
            for prime, exponent in factors
            if prime < CAP and valuation_two(prime - 1) >= AMBIENT_V2
        ]
        if (
            result.get("max_prime_bits") != row_max_bits
            or result.get("max_v2_prime_minus_1") != row_max_v2
            or result.get("high_gate_factors") != row_high
        ):
            raise AssertionError((tail_index, "factor metadata"))
        prime_set.update(prime for prime, _ in factors)
        factors_by_index[tail_index] = factors

    if sorted(set(range(194)) - set(factors_by_index)) != [191]:
        raise AssertionError("residual index")
    if packet.get("missing") != [{"error": "FACTOR_TIMEOUT_300S", "tail_index": 191}]:
        raise AssertionError("printed residual")
    prime_text = "".join(f"{prime}\n" for prime in sorted(prime_set))
    prime_digest = hashlib.sha256(prime_text.encode()).hexdigest()
    high_gate_factors = [
        str(prime)
        for prime in sorted(prime_set)
        if prime < CAP and valuation_two(prime - 1) >= AMBIENT_V2
    ]
    max_v2 = max((valuation_two(prime - 1) for prime in prime_set), default=-1)
    max_v2_below_cap = max(
        (valuation_two(prime - 1) for prime in prime_set if prime < CAP),
        default=-1,
    )
    if (
        len(prime_set) != 399
        or packet.get("tail_distinct_primes") != 399
        or prime_digest != PRIME_DIGEST
        or packet.get("tail_prime_digest") != PRIME_DIGEST
        or max_v2 != 17
        or packet.get("max_v2_prime_minus_1") != 17
        or max_v2_below_cap != 17
        or packet.get("max_v2_below_cap") != 17
        or high_gate_factors
        or packet.get("high_gate_cases")
    ):
        raise AssertionError("aggregate factor metadata")

    result = {
        "schema": "wcl15-independent-hard-tail-cert-v1",
        "status": "COMPLETE_193_PENDING_191",
        "source_sha256": source_sha256,
        "manifest_rows": len(manifest_rows),
        "manifest_digest": manifest_hash.hexdigest(),
        "certified_tail_rows": len(factors_by_index),
        "pending_tail_indices": [191],
        "primality_checks": primality_checks,
        "distinct_primes": len(prime_set),
        "prime_digest": prime_digest,
        "maximum_v2_prime_minus_1": max_v2,
        "high_gate_factors": high_gate_factors,
        "seconds": round(time.monotonic() - started, 6),
    }
    result["certificate_digest"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return result


@app.local_entrypoint()
def main() -> None:
    result = certify.remote()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("WCL15_TAIL_CERT " + json.dumps(result, sort_keys=True))
