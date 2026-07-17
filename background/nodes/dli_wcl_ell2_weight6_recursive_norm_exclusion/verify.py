#!/usr/bin/env python3
"""Verify the complete weight-six recursive-norm and prime certificates."""

from __future__ import annotations

import gzip
import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LEDGER = ROOT / (
    "experiments/prize_resolution/"
    "dli_wcl_ell2_weight6_recursive_norm_full_result.json"
)
PRIMES = ROOT / (
    "experiments/prize_resolution/"
    "dli_wcl_ell2_weight6_recursive_norm_prime_cert_result.json.gz"
)
SOURCE = ROOT / (
    "experiments/prize_resolution/"
    "dli_wcl_ell2_weight6_recursive_norm_full_modal.py"
)


class Reject(ValueError):
    pass


def exact_trial_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def check_hex_digest(value: object) -> None:
    if (
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in "0123456789abcdef" for character in value)
    ):
        raise Reject("digest")


def verify(data: dict[str, object], cert: dict[str, object]) -> tuple[int, int]:
    expected_top = {
        "aggregate_candidate_digest",
        "aggregate_factor_digest",
        "batch_size",
        "batches",
        "candidate_metadata",
        "covered_rows",
        "distinct_primes",
        "errors",
        "high_gate_cases",
        "max_batch_seconds",
        "max_gcd_bits",
        "max_v2_prime_minus_1",
        "nonunit_gcds",
        "requested_rows",
        "schema",
        "scope",
        "source_sha256",
        "status",
        "structural_zero_cases",
    }
    if not isinstance(data, dict) or set(data) != expected_top:
        raise Reject("ledger schema")
    if (
        data["schema"] != "dli-wcl-ell2-weight6-recursive-norm-full-v1"
        or data["scope"] != "complete"
        or data["status"] != "COMPLETE"
        or data["requested_rows"] != 404_740
        or data["covered_rows"] != 404_740
        or data["batch_size"] != 128
        or data["errors"] != []
        or data["high_gate_cases"] != []
        or data["nonunit_gcds"] != 404_230
        or data["max_gcd_bits"] != 16_986
        or data["max_v2_prime_minus_1"] != 18
    ):
        raise Reject("ledger header")
    check_hex_digest(data["aggregate_candidate_digest"])
    check_hex_digest(data["aggregate_factor_digest"])
    if data["source_sha256"] != hashlib.sha256(SOURCE.read_bytes()).hexdigest():
        raise Reject("source hash")

    metadata = data["candidate_metadata"]
    expected_metadata = {
        "binary_sha256",
        "candidate_orbits",
        "legal_pairs",
        "order",
        "pair_orbit_size_histogram",
        "pair_orbits",
        "presentation_multiplicity_histogram",
        "representative_digest",
        "router_presentations",
        "schema",
        "status",
    }
    if not isinstance(metadata, dict) or set(metadata) != expected_metadata:
        raise Reject("metadata schema")
    if (
        metadata["schema"] != "dli-wcl-ell2-weight6-candidate-file-v1"
        or metadata["status"] != "COMPLETE"
        or metadata["order"] != 1024
        or metadata["legal_pairs"] != 521_220
        or metadata["pair_orbits"] != 1_514
        or metadata["router_presentations"] != 1_550_336
        or metadata["candidate_orbits"] != 404_740
        or metadata["pair_orbit_size_histogram"]
        != {
            "2": 2,
            "4": 4,
            "8": 10,
            "16": 22,
            "32": 46,
            "64": 94,
            "128": 190,
            "256": 382,
            "512": 764,
        }
        or metadata["presentation_multiplicity_histogram"]
        != {
            "2": 32,
            "3": 345_440,
            "4": 2_024,
            "6": 42_672,
            "8": 508,
            "12": 10_416,
            "16": 252,
            "24": 2_480,
            "32": 124,
            "48": 560,
            "64": 60,
            "96": 112,
            "128": 28,
            "192": 16,
            "256": 12,
            "512": 4,
        }
        or metadata["representative_digest"]
        != "677871a774e3463b5f74b8c63578f9e075637745355599d682d7f9e0312747f2"
    ):
        raise Reject("metadata")
    check_hex_digest(metadata["binary_sha256"])

    batches = data["batches"]
    if not isinstance(batches, list) or len(batches) != 3_163:
        raise Reject("batch count")
    expected_batch = {
        "candidate_digest",
        "distinct_nonunit_gcds",
        "distinct_primes",
        "end",
        "factor_digest",
        "high_gate_cases",
        "max_gcd_bits",
        "max_v2_cases",
        "max_v2_prime_minus_1",
        "nonunit_gcds",
        "rows",
        "schema",
        "seconds",
        "start",
        "status",
        "structural_zero_cases",
    }
    cursor = 0
    batch_candidate_digests = []
    batch_factor_digests = []
    batch_primes = set()
    structural_cases = []
    nonunit_total = 0
    max_gcd_bits = 0
    max_v2 = -1
    max_seconds = 0.0
    for row in batches:
        if not isinstance(row, dict) or set(row) != expected_batch:
            raise Reject("batch schema")
        start = row["start"]
        end = row["end"]
        if (
            row["schema"] != "dli-wcl-ell2-weight6-recursive-norm-batch-v1"
            or row["status"] != "COMPLETE"
            or not isinstance(start, int)
            or not isinstance(end, int)
            or start != cursor
            or end <= start
            or end - start != row["rows"]
            or row["high_gate_cases"] != []
        ):
            raise Reject("batch coverage")
        cursor = end
        check_hex_digest(row["candidate_digest"])
        check_hex_digest(row["factor_digest"])
        batch_candidate_digests.append(row["candidate_digest"])
        batch_factor_digests.append(row["factor_digest"])
        batch_primes.update(row["distinct_primes"])
        structural_cases.extend(row["structural_zero_cases"])
        nonunit_total += row["nonunit_gcds"]
        max_gcd_bits = max(max_gcd_bits, row["max_gcd_bits"])
        max_v2 = max(max_v2, row["max_v2_prime_minus_1"])
        max_seconds = max(max_seconds, row["seconds"])
    if cursor != 404_740:
        raise Reject("coverage end")
    if hashlib.sha256("\n".join(batch_candidate_digests).encode()).hexdigest() != data[
        "aggregate_candidate_digest"
    ]:
        raise Reject("candidate aggregate")
    if hashlib.sha256("\n".join(batch_factor_digests).encode()).hexdigest() != data[
        "aggregate_factor_digest"
    ]:
        raise Reject("factor aggregate")
    if (
        nonunit_total != data["nonunit_gcds"]
        or max_gcd_bits != data["max_gcd_bits"]
        or max_v2 != data["max_v2_prime_minus_1"]
        or max_seconds != data["max_batch_seconds"]
    ):
        raise Reject("batch aggregate")

    top_primes = data["distinct_primes"]
    if (
        not isinstance(top_primes, list)
        or len(top_primes) != 443
        or top_primes != sorted(set(top_primes), key=int)
        or batch_primes != set(top_primes)
    ):
        raise Reject("prime roots")
    computed_v2 = max(
        ((int(prime) - 1 & -(int(prime) - 1)).bit_length() - 1)
        for prime in top_primes
    )
    if computed_v2 != 18:
        raise Reject("valuation")

    top_structural = data["structural_zero_cases"]
    if top_structural != structural_cases or len(top_structural) != 510:
        raise Reject("structural cases")
    seen_candidates = set()
    for case in top_structural:
        if not isinstance(case, dict) or set(case) != {
            "candidate",
            "first_zero",
            "second_zero",
        }:
            raise Reject("structural schema")
        candidate = tuple(case["candidate"])
        if (
            len(candidate) != 3
            or candidate in seen_candidates
            or not case["first_zero"]
            or not case["second_zero"]
        ):
            raise Reject("structural case")
        seen_candidates.add(candidate)
    if nonunit_total + len(top_structural) != 404_740:
        raise Reject("branch exhaustion")

    if not isinstance(cert, dict) or set(cert) != {
        "nodes",
        "roots",
        "schema",
        "status",
        "worker_errors",
    }:
        raise Reject("prime certificate schema")
    if (
        cert["schema"]
        != "dli-wcl-ell2-weight6-recursive-norm-prime-cert-v1"
        or cert["status"] != "COMPLETE"
        or cert["worker_errors"] != []
        or cert["roots"] != top_primes
        or len(cert["nodes"]) != 626
    ):
        raise Reject("prime certificate header")

    nodes = cert["nodes"]
    validated = set()
    active = set()

    def validate_prime(prime_text: str) -> None:
        if prime_text in validated:
            return
        if prime_text in active or prime_text not in nodes:
            raise Reject("prime dependency")
        active.add(prime_text)
        candidate = int(prime_text)
        node = nodes[prime_text]
        if not isinstance(node, dict) or node.get("method") not in {
            "trial",
            "pocklington",
        }:
            raise Reject("prime node")
        if node["method"] == "trial":
            if set(node) != {"method"} or candidate >= 10_000 or not exact_trial_prime(
                candidate
            ):
                raise Reject("trial prime")
        else:
            if set(node) != {"method", "minus_one_factors", "witnesses"}:
                raise Reject("Pocklington schema")
            factors = node["minus_one_factors"]
            witnesses = node["witnesses"]
            if (
                not isinstance(factors, list)
                or not factors
                or not isinstance(witnesses, dict)
            ):
                raise Reject("Pocklington payload")
            product = 1
            factor_roots = []
            for factor in factors:
                if (
                    not isinstance(factor, list)
                    or len(factor) != 2
                    or not isinstance(factor[0], str)
                    or not isinstance(factor[1], int)
                    or factor[1] <= 0
                ):
                    raise Reject("Pocklington factor")
                validate_prime(factor[0])
                factor_roots.append(factor[0])
                product *= int(factor[0]) ** factor[1]
            if product != candidate - 1 or set(witnesses) != set(factor_roots):
                raise Reject("Pocklington factorization")
            for factor_text in factor_roots:
                base = witnesses[factor_text]
                factor = int(factor_text)
                if (
                    not isinstance(base, int)
                    or not 2 <= base < candidate
                    or pow(base, candidate - 1, candidate) != 1
                    or math.gcd(
                        pow(base, (candidate - 1) // factor, candidate) - 1,
                        candidate,
                    )
                    != 1
                ):
                    raise Reject("Pocklington witness")
        active.remove(prime_text)
        validated.add(prime_text)

    for root in top_primes:
        validate_prime(root)
    if set(nodes) != validated:
        raise Reject("unused prime nodes")
    return len(top_structural), len(validated)


def expect_reject(data: dict[str, object], cert: dict[str, object], mutate, restore) -> None:
    mutate()
    try:
        verify(data, cert)
    except Reject:
        pass
    else:
        raise AssertionError("mutation survived")
    finally:
        restore()


def main() -> None:
    data = json.loads(LEDGER.read_text())
    with gzip.open(PRIMES, "rt", encoding="utf-8") as handle:
        cert = json.load(handle)
    structural, prime_nodes = verify(data, cert)

    old_status = data["status"]
    expect_reject(
        data,
        cert,
        lambda: data.__setitem__("status", "INCOMPLETE"),
        lambda: data.__setitem__("status", old_status),
    )
    old_start = data["batches"][1]["start"]
    expect_reject(
        data,
        cert,
        lambda: data["batches"][1].__setitem__("start", old_start + 1),
        lambda: data["batches"][1].__setitem__("start", old_start),
    )
    expect_reject(
        data,
        cert,
        lambda: data["high_gate_cases"].append({"candidate": [0, 1, 2]}),
        lambda: data["high_gate_cases"].pop(),
    )
    old_second = data["structural_zero_cases"][0]["second_zero"]
    expect_reject(
        data,
        cert,
        lambda: data["structural_zero_cases"][0].__setitem__("second_zero", False),
        lambda: data["structural_zero_cases"][0].__setitem__(
            "second_zero", old_second
        ),
    )
    removed_root = cert["roots"].pop()
    expect_reject(
        data,
        cert,
        lambda: None,
        lambda: cert["roots"].append(removed_root),
    )
    pocklington_key = next(
        key for key, node in cert["nodes"].items() if node["method"] == "pocklington"
    )
    witness_key = next(iter(cert["nodes"][pocklington_key]["witnesses"]))
    old_witness = cert["nodes"][pocklington_key]["witnesses"][witness_key]
    expect_reject(
        data,
        cert,
        lambda: cert["nodes"][pocklington_key]["witnesses"].__setitem__(
            witness_key, 1
        ),
        lambda: cert["nodes"][pocklington_key]["witnesses"].__setitem__(
            witness_key, old_witness
        ),
    )

    print(
        "DLI_WCL_ELL2_WEIGHT6_RECURSIVE_NORM_EXCLUSION_PASS "
        f"candidates=404740 batches=3163 primes=443 prime_nodes={prime_nodes} "
        f"double_zero={structural} max_v2=18 mutations=6/6"
    )


if __name__ == "__main__":
    main()
