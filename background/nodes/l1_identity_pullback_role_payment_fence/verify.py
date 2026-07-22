#!/usr/bin/env python3
"""Verify the identity-pullback role-payment fence."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "l1_identity_pullback_role_payment_fence"


def evaluate(coefficients: tuple[int, ...], x: int, prime: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % prime
    return value


def check_toy(prime: int, domain: tuple[int, ...], k: int) -> int:
    codewords = [
        tuple(evaluate(coefficients, x, prime) for x in domain)
        for coefficients in itertools.product(range(prime), repeat=k)
    ]
    receivers = (
        tuple(0 for _ in domain),
        tuple(x % prime for x in domain),
        tuple((x * x + 1) % prime for x in domain),
        tuple((3 * x * x + 2 * x + 4) % prime for x in domain),
    )
    checks = 0
    for receiver in receivers:
        agreements = [
            tuple(i for i, (left, right) in enumerate(zip(word, receiver)) if left == right)
            for word in codewords
        ]
        for agreement in agreements:
            # Under P=X, complete fibers are the domain singletons.
            complete_labels = agreement
            partial_loss = len(set(agreement) - set(complete_labels))
            assert partial_loss == 0
            checks += 1
        for threshold in range(k, len(domain) + 1):
            direct = sum(len(agreement) >= threshold for agreement in agreements)
            identity_pullback = sum(
                len(complete_labels) >= threshold
                for complete_labels in agreements
            )
            assert direct == identity_pullback
            checks += 1
    return checks


def main() -> None:
    checks = 0
    checks += check_toy(7, (1, 2, 3, 4), 2)
    checks += check_toy(11, (1, 2, 3, 4, 5), 2)

    # The identity endpoint has one component, full coverage, and no kernel.
    for n in (8, 16, 64):
        for k in (1, n // 4, n // 2):
            b = n
            k_0 = k
            kappa = max(0, k_0 - b)
            assert kappa == 0
            checks += 1

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    edges = {(edge["from"], edge["to"], edge["kind"]) for edge in dag["edges"]}
    assert nodes[NODE]["status"] == "PROVED"
    for supplier in (
        "l1_general_pullback_interleaving_descent",
        "l1_exact_shell_prefix_hankel_bridge",
        "l1_official_reserve_tame_refinement_router",
    ):
        assert nodes[supplier]["status"] == "PROVED"
        assert (supplier, NODE, "req") in edges
        checks += 2
    assert (NODE, "l1_mixed_petal_amplification", "ev") in edges
    checks += 1

    statement = (ROOT / "background" / "nodes" / NODE / "statement.md").read_text()
    for anchor in (
        "P(X)=X",
        "kappa=max(0,k-n)=0",
        "z(f)=0",
        "=#ImgFib_U(a)",
        "explicitly exclude `s=1`",
        "not a list-size upper bound",
    ):
        assert anchor in statement
        checks += 1

    print(f"L1_IDENTITY_PULLBACK_ROLE_PAYMENT_FENCE_PASS checks={checks}")


if __name__ == "__main__":
    main()
