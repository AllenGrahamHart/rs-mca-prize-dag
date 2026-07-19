#!/usr/bin/env python3
"""Verify the complete weight-5 norm-gcd and primality certificate."""

from __future__ import annotations

import copy
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LEDGER = ROOT / (
    "experiments/prize_resolution/"
    "dli_wcl_ell2_weight5_norm_gcd_certificate_result.json"
)
CERT = ROOT / (
    "experiments/prize_resolution/"
    "dli_wcl_ell2_weight5_norm_gcd_prime_cert_result.json.gz"
)
REPLAY = ROOT / (
    "experiments/prize_resolution/"
    "dli_wcl_ell2_weight5_norm_gcd_replay_result.json"
)
GENERATOR = ROOT / (
    "experiments/prize_resolution/dli_wcl_pair_norm_gcd_probe_modal.py"
)
ORDER = 1024
HALF = ORDER // 2
ORBIT_COUNT = 1_514
GCD_COUNT = 507
ROOT_COUNT = 168
NODE_COUNT = 282


class Reject(ValueError):
    pass


def valuation_two(value: int) -> int:
    return (value & -value).bit_length() - 1 if value else 0


def trial_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, math.isqrt(value) + 1, 2))


def legal_pairs() -> list[tuple[int, int]]:
    available = [exponent for exponent in range(1, ORDER) if exponent != HALF]
    return [
        pair
        for pair in itertools.combinations(available, 2)
        if (pair[1] - pair[0]) % ORDER != HALF
    ]


def representatives() -> list[tuple[int, int]]:
    unseen = set(legal_pairs())
    output = []
    while unseen:
        pair = min(unseen)
        orbit = {
            tuple(
                sorted(
                    ((unit * pair[0]) % ORDER, (unit * pair[1]) % ORDER)
                )
            )
            for unit in range(1, ORDER, 2)
        }
        unseen.difference_update(orbit)
        output.append(pair)
    return output


def exact_row_digest(rows: list[dict[str, object]]) -> str:
    fields = (
        "order",
        "pair",
        "status",
        "coefficient_bits",
        "first_norm_bits",
        "second_norm_bits",
        "gcd",
        "gcd_bits",
    )
    projection = [{field: row[field] for field in fields} for row in rows]
    encoded = json.dumps(projection, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()


def verify_ledger() -> tuple[list[str], int, int]:
    data = json.loads(LEDGER.read_text())
    if not isinstance(data, dict) or set(data) != {
        "eligible_factors",
        "factor_rows",
        "factor_status",
        "orbit_counts",
        "rows",
        "schema",
        "scope",
        "status",
    }:
        raise Reject("ledger schema")
    if (
        data["schema"] != "dli-wcl-pair-norm-gcd-probe-v1"
        or data["scope"] != "complete M=1024 odd-dilation orbit certificate"
        or data["status"] != "COMPLETE"
        or data["factor_status"] != "COMPLETE"
        or data["orbit_counts"] != {"1024": ORBIT_COUNT}
        or data["eligible_factors"] != []
    ):
        raise Reject("ledger header")

    rows = data["rows"]
    expected_pairs = representatives()
    if len(expected_pairs) != ORBIT_COUNT or len(rows) != ORBIT_COUNT:
        raise Reject("orbit count")
    row_fields = {
        "coefficient_bits",
        "first_norm_bits",
        "first_seconds",
        "gcd",
        "gcd_bits",
        "order",
        "pair",
        "second_norm_bits",
        "second_seconds",
        "seconds",
        "status",
    }
    for row, pair in zip(rows, expected_pairs):
        if not isinstance(row, dict) or set(row) != row_fields:
            raise Reject("row schema")
        common = int(row["gcd"])
        if (
            row["order"] != ORDER
            or row["pair"] != list(pair)
            or row["status"] != "COMPLETE"
            or common < 1
            or str(common) != row["gcd"]
            or row["gcd_bits"] != common.bit_length()
            or not 0 < row["coefficient_bits"]
            or not 0 < row["first_norm_bits"]
            or not 0 < row["second_norm_bits"]
        ):
            raise Reject("row")

    distinct = {row["gcd"] for row in rows if int(row["gcd"]) > 1}
    factor_rows = data["factor_rows"]
    if len(distinct) != GCD_COUNT or len(factor_rows) != GCD_COUNT:
        raise Reject("gcd count")
    roots = set()
    max_v2 = 0
    seen = set()
    for row in factor_rows:
        if not isinstance(row, dict) or set(row) != {
            "factors", "gcd", "seconds", "status"
        }:
            raise Reject("factor row schema")
        gcd_text = row["gcd"]
        if row["status"] != "COMPLETE" or gcd_text in seen or gcd_text not in distinct:
            raise Reject("factor row")
        seen.add(gcd_text)
        product = 1
        row_roots = set()
        for factor in row["factors"]:
            if not isinstance(factor, dict) or set(factor) != {
                "exponent", "prime", "prime_bits", "v2_prime_minus_1"
            }:
                raise Reject("factor schema")
            prime = int(factor["prime"])
            exponent = factor["exponent"]
            if (
                str(prime) != factor["prime"]
                or prime in row_roots
                or not isinstance(exponent, int)
                or isinstance(exponent, bool)
                or exponent <= 0
                or factor["prime_bits"] != prime.bit_length()
                or factor["v2_prime_minus_1"] != valuation_two(prime - 1)
            ):
                raise Reject("factor")
            product *= prime**exponent
            row_roots.add(prime)
            roots.add(factor["prime"])
            max_v2 = max(max_v2, factor["v2_prime_minus_1"])
        if product != int(gcd_text):
            raise Reject("factor product")
    if seen != distinct or len(roots) != ROOT_COUNT or max_v2 != 18:
        raise Reject("factor summary")

    replay = json.loads(REPLAY.read_text())
    digest = exact_row_digest(rows)
    if not isinstance(replay, dict) or set(replay) != {
        "actual_digest",
        "expected_digest",
        "orbit_counts",
        "rows",
        "schema",
        "source_sha256",
        "status",
    }:
        raise Reject("replay schema")
    if (
        replay["schema"] != "dli-wcl-ell2-weight5-norm-gcd-replay-v1"
        or replay["status"] != "COMPLETE"
        or replay["orbit_counts"] != {"1024": ORBIT_COUNT}
        or replay["rows"] != ORBIT_COUNT
        or replay["expected_digest"] != digest
        or replay["actual_digest"] != digest
        or replay["source_sha256"] != hashlib.sha256(GENERATOR.read_bytes()).hexdigest()
    ):
        raise Reject("replay")
    return sorted(roots, key=int), max_v2, max(int(row["gcd_bits"]) for row in rows)


def verify_tree(roots: list[str], nodes: dict[str, object], require_all: bool = True) -> int:
    verified: set[int] = set()

    def visit(value: int) -> None:
        if value in verified:
            return
        node = nodes.get(str(value))
        if not isinstance(node, dict):
            raise Reject("missing prime node")
        if node == {"method": "trial"}:
            if value >= 10_000 or not trial_prime(value):
                raise Reject("trial prime")
            verified.add(value)
            return
        if set(node) != {"method", "minus_one_factors", "witnesses"}:
            raise Reject("Pocklington schema")
        if node["method"] != "pocklington":
            raise Reject("Pocklington method")
        factors = node["minus_one_factors"]
        witnesses = node["witnesses"]
        if not isinstance(factors, list) or not isinstance(witnesses, dict):
            raise Reject("Pocklington payload")
        product = 1
        primes = set()
        for pair in factors:
            if not isinstance(pair, list) or len(pair) != 2:
                raise Reject("factor pair")
            prime = int(pair[0])
            exponent = pair[1]
            if (
                str(prime) != pair[0]
                or prime in primes
                or not isinstance(exponent, int)
                or isinstance(exponent, bool)
                or exponent <= 0
            ):
                raise Reject("Pocklington factor")
            visit(prime)
            primes.add(prime)
            product *= prime**exponent
        if product != value - 1 or product <= math.isqrt(value):
            raise Reject("incomplete minus-one factorization")
        if set(witnesses) != {str(prime) for prime in primes}:
            raise Reject("witness set")
        for prime in primes:
            base = witnesses[str(prime)]
            if not isinstance(base, int) or isinstance(base, bool):
                raise Reject("witness type")
            if pow(base, value - 1, value) != 1:
                raise Reject("Fermat condition")
            if math.gcd(pow(base, (value - 1) // prime, value) - 1, value) != 1:
                raise Reject("gcd condition")
        verified.add(value)

    for root in roots:
        visit(int(root))
    if require_all and {str(value) for value in verified} != set(nodes):
        raise Reject("orphan prime node")
    return len(verified)


def main() -> None:
    roots, max_v2, max_gcd_bits = verify_ledger()
    with gzip.open(CERT, "rt", encoding="utf-8") as handle:
        certificate = json.load(handle)
    if not isinstance(certificate, dict) or set(certificate) != {
        "nodes", "roots", "schema", "status", "worker_errors"
    }:
        raise Reject("certificate schema")
    if (
        certificate["schema"] != "dli-wcl-ell2-weight5-prime-cert-v1"
        or certificate["status"] != "COMPLETE"
        or certificate["worker_errors"] != []
        or certificate["roots"] != roots
        or len(roots) != ROOT_COUNT
        or not isinstance(certificate["nodes"], dict)
        or len(certificate["nodes"]) != NODE_COUNT
    ):
        raise Reject("certificate header")
    nodes = certificate["nodes"]
    verified = verify_tree(roots, nodes)

    root = next(root for root in roots if nodes[root].get("method") == "pocklington")
    controls = 0
    mutations = (
        lambda item: item[root]["witnesses"].__setitem__(
            next(iter(item[root]["witnesses"])), 1
        ),
        lambda item: item[root]["minus_one_factors"][0].__setitem__(
            1, item[root]["minus_one_factors"][0][1] + 1
        ),
        lambda item: item.__setitem__("2", {"method": "trial-bad"}),
    )
    for mutate in mutations:
        altered = copy.deepcopy(nodes)
        mutate(altered)
        try:
            verify_tree([root], altered, require_all=False)
        except (Reject, KeyError, TypeError, ValueError):
            controls += 1
    if controls != len(mutations):
        raise AssertionError(f"negative controls caught {controls}/{len(mutations)}")
    print(
        "DLI_WCL_ELL2_WEIGHT5_NORM_GCD_EXCLUSION_PASS "
        f"orbits={ORBIT_COUNT} gcds={GCD_COUNT} roots={len(roots)} "
        f"prime_nodes={verified} max_v2={max_v2} max_gcd_bits={max_gcd_bits} "
        f"negative_controls={controls}/{len(mutations)}"
    )


if __name__ == "__main__":
    main()
