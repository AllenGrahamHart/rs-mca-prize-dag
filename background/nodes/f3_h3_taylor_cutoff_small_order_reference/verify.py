#!/usr/bin/env python3
"""Verify the bounded C36 Taylor-cutoff reference packet."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

from sympy import primitive_root


ROOT = Path(__file__).resolve().parents[3]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

import c36_taylor_cutoff_reference as reference  # noqa: E402


NODE = "f3_h3_taylor_cutoff_small_order_reference"
DEPENDENCIES = {
    "f3_h3_global_resultant_compression",
    "f3_h3_quotient_orbit_canonical_resultant_manifest",
    "f3_h3_quotient_orbit_taylor_cutoff_ladder",
}
CONSUMERS = {"f3_h3_official_order_template_survivor"}
PRIMES = (17, 41, 73, 89, 97, 113, 137, 193)
PRODUCT_HASH = "aed6191d1d069c78fda87ab942aee18926a3c8f2e535b257efada12de953b25b"


def block_id(spec: tuple[int, str, int]) -> str:
    return f"{spec[0]}{spec[1]}{spec[2]}"


def validate_payload(payload: dict) -> None:
    assert payload["schema"] == reference.SCHEMA
    assert payload["complete"] is True
    assert payload["stage"] == "complete"
    assert payload["exponent"] == 3 and payload["order"] == 8
    assert payload["cutoffs"] == [2, 3]
    assert payload["expected_blocks"] == 12
    assert payload["selected_blocks"] == 12
    assert payload["product_degree"] == 49
    assert payload["product_hash"] == PRODUCT_HASH

    expected_ids = [block_id(spec) for spec in reference.canonical_block_specs(3)]
    blocks = payload["blocks"]
    assert [block["id"] for block in blocks] == expected_ids
    for block in blocks:
        assert block["degree"] in {2, 4}
        assert len(block["orbit_polynomial_sha256"]) == 64
        assert set(block["cutoffs"]) == {"2", "3"}
        for cutoff in (2, 3):
            result = block["cutoffs"][str(cutoff)]
            content = int(result["odd_content"])
            assert content > 0 and content % 2 == 1
            assert result["x_degree"] <= cutoff * block["degree"]
            assert len(result["certificate_sha256"]) == 64


def direct_event(prime: int, cutoff: int, order: int = 8) -> bool:
    assert (prime - 1) % order == 0
    generator = int(primitive_root(prime))
    root = pow(generator, (prime - 1) // order, prime)
    assert pow(root, order, prime) == 1
    assert pow(root, order // 2, prime) != 1

    shifted = [(1 - pow(root, exponent, prime)) % prime for exponent in range(1, order)]
    assert len(set(shifted)) == order - 1 and 0 not in shifted
    products = [0] * prime
    quotients = [0] * prime
    for left in shifted:
        inverse = pow(left, -1, prime)
        for right in shifted:
            products[(left * right) % prime] += 1
            quotients[(right * inverse) % prime] += 1
    return any(
        target != 1
        and products[target] >= cutoff + 1
        and quotients[target] > 0
        for target in range(prime)
    )


def content_event(payload: dict, prime: int, cutoff: int) -> bool:
    return any(
        int(block["cutoffs"][str(cutoff)]["odd_content"]) % prime == 0
        for block in payload["blocks"]
    )


def cross_check(payload: dict) -> dict[int, list[int]]:
    survivors = {2: [], 3: []}
    for cutoff in survivors:
        for prime in PRIMES:
            direct = direct_event(prime, cutoff)
            compiled = content_event(payload, prime, cutoff)
            assert direct == compiled
            if direct:
                survivors[cutoff].append(prime)
    assert survivors == {2: [17, 41], 3: [17]}
    return survivors


def packet_check() -> None:
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for dependency in DEPENDENCIES:
        assert nodes[dependency]["status"] == "PROVED"
        assert (dependency, NODE, "req") in edges
    for consumer in CONSUMERS:
        assert (NODE, consumer, "ev") in edges

    base = ROOT / "background" / "nodes" / NODE
    required = {
        "statement.md",
        "proof.md",
        "claim_contract.md",
        "dependency_subdag.md",
        "audit.md",
        "result.md",
        "verify.py",
        "verify_audit.py",
    }
    assert required <= {path.name for path in base.iterdir()}
    text = "".join(
        (base / name).read_text() for name in required if name.endswith(".md")
    )
    for marker in (
        "finite exhaustive verification",
        "{17,41}",
        "{17}",
        "complete=false",
        "correctness oracle",
        "does not validate `n=16`",
    ):
        assert marker in text


def checked_packet() -> dict:
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / "packet.json"
        payload = reference.run_reference(3, [2, 3], output, 30.0)
        assert json.loads(output.read_text()) == payload
    validate_payload(payload)
    cross_check(payload)
    return payload


def main() -> None:
    checked_packet()
    packet_check()
    print(
        "F3_H3_TAYLOR_CUTOFF_SMALL_ORDER_REFERENCE_PASS "
        "n=8 blocks=12 comparisons=16 c2=17,41 c3=17"
    )


if __name__ == "__main__":
    main()
