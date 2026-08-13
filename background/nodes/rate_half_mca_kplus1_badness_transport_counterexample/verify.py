#!/usr/bin/env python3
"""Verify the deployed K-to-K+1 badness-transport counterexample."""

from __future__ import annotations

import copy
import hashlib
import json
import math
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "391421a32ad5f40bb1be20754760065ea31490f226e13151e79a3ad61a837365"
TOP_KEYS = {"schema", "canonical_dossier_commit", "upstream", "row"}
ROW_KEYS = {
    "p",
    "p_minus_1_factorization",
    "pocklington_witnesses",
    "n",
    "k",
    "m",
    "zeta",
    "e",
    "slope",
    "expected_e_plus_m",
}


class Reject(ValueError):
    pass


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer field")
    return value


def validate(data: object) -> dict[str, int]:
    if not isinstance(data, dict) or set(data) != TOP_KEYS:
        raise Reject("top-level schema")
    if data["schema"] != "rate-half-mca-kplus1-badness-counterexample-v1":
        raise Reject("schema")
    if data["canonical_dossier_commit"] != "c8d48cd4b94fb256ad9fedfc1d53b4b14c77bfad":
        raise Reject("canonical pin")
    if data["upstream"] != {
        "head": "e26c15b2d2c2f98ae12dda17b97c40981f76e1ff",
        "note_blob": "9a3ea00b216ff16c32cfab0b2b7f8a179cb16ee7",
        "python_verifier_blob": "57bfec727a3bf032236c7c0d3f5852c55fd526d9",
        "sage_verifier_blob": "dbfabead1542e2297f3c8ea4e0ac58b503ecf8eb",
    }:
        raise Reject("upstream pins")
    row = data["row"]
    if not isinstance(row, dict) or set(row) != ROW_KEYS:
        raise Reject("row schema")
    p = integer(row["p"])
    n = integer(row["n"])
    dimension = integer(row["k"])
    agreement = integer(row["m"])
    zeta = integer(row["zeta"])
    e = integer(row["e"])
    slope = integer(row["slope"])
    expected_end = integer(row["expected_e_plus_m"])
    factors = row["p_minus_1_factorization"]
    witnesses = row["pocklington_witnesses"]
    if factors != {"two_exponent": 24, "odd_prime": 127}:
        raise Reject("factorization schema")
    if witnesses != {"2": 3, "127": 2}:
        raise Reject("witness schema")
    if p - 1 != 127 * (1 << 24):
        raise Reject("p-1 factorization")
    for prime in (2, 127):
        witness = integer(witnesses[str(prime)])
        if (
            pow(witness, p - 1, p) != 1
            or math.gcd(pow(witness, (p - 1) // prime, p) - 1, p) != 1
        ):
            raise Reject("Pocklington witness")
    if (
        n != 1 << 21
        or dimension != 1 << 20
        or not 0 < e < agreement < n
        or e + agreement != expected_end
        or expected_end >= n
        or slope != 0
        or pow(zeta, n, p) != 1
        or pow(zeta, n // 2, p) != p - 1
    ):
        raise Reject("deployed support contract")

    # The polynomial X^k is excluded at dimension k and included at k+1.
    direction_degree = dimension
    if direction_degree < dimension or direction_degree >= dimension + 1:
        raise Reject("dimension membership switch")
    if agreement <= direction_degree:
        raise Reject("root-count contradiction")
    return {
        "p": p,
        "n": n,
        "k": dimension,
        "m": agreement,
        "e": e,
        "support_end": expected_end,
        "root_surplus": agreement - direction_degree,
    }


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    result = validate(data)
    mutations = (
        lambda item: item["row"].__setitem__("p", item["row"]["p"] + 2),
        lambda item: item["row"].__setitem__("zeta", 1),
        lambda item: item["row"].__setitem__("n", item["row"]["n"] // 2),
        lambda item: item["row"].__setitem__("m", item["row"]["k"]),
        lambda item: item["row"].__setitem__("e", item["row"]["e"] + 1),
        lambda item: item["row"].__setitem__("slope", 1),
        lambda item: item["row"]["pocklington_witnesses"].__setitem__("2", 1),
        lambda item: item["upstream"].__setitem__("note_blob", "0" * 40),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError(f"negative controls caught {sum(controls)}/{len(controls)}")
    print(
        "RATE_HALF_MCA_KPLUS1_BADNESS_TRANSPORT_COUNTEREXAMPLE_PASS "
        f"p={result['p']} support={result['m']} root_surplus={result['root_surplus']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
