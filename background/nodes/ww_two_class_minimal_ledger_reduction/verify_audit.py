#!/usr/bin/env python3
"""Mutation audit for the W3 two-class minimal-ledger reduction."""

from __future__ import annotations

from copy import deepcopy

from verify import CONSUMER, DEPENDENCY, NODE_ID, evaluate, load_inputs


def rejected(mutator) -> bool:
    dag, documents = deepcopy(load_inputs())
    mutator(dag, documents)
    return not all(evaluate(dag, documents).values())


def main() -> None:
    # Documentation is re-posed in the same commit; this baseline must pass.
    assert all(evaluate(*load_inputs()).values())
    mutations = [
        lambda d, m: next(
            node for node in d["nodes"] if node["id"] == NODE_ID
        ).update(status="TARGET"),
        lambda d, m: next(
            node for node in d["nodes"] if node["id"] == CONSUMER
        ).update(status="REFUTED"),
        lambda d, m: d.update(
            edges=[
                edge
                for edge in d["edges"]
                if not (edge["from"] == DEPENDENCY and edge["to"] == NODE_ID)
            ]
        ),
        lambda d, m: m.update(
            statement=m["statement"].replace(
                "set of distinct printed planted polynomials", "petal labels"
            )
        ),
        lambda d, m: m.update(
            statement=m["statement"].replace(
                "N_nonplant(U) <= B* - p(U)", "N_nonplant(U) <= B*"
            )
        ),
        lambda d, m: m.update(
            proof=m["proof"].replace(
                "not needed for the two-class identity", "required silently"
            )
        ),
        lambda d, m: m.update(
            w3=m["w3"].replace(
                "p(U)+N_nonplant(U) >= 7 > 6=B*", "p(U)+N_nonplant(U) <= B*"
            )
        ),
        lambda d, m: m.update(
            compute=m["compute"].replace(
                "CANCELED; NO LIVE CONSUMER; DO NOT RUN", "READY"
            )
        ),
    ]
    outcomes = [rejected(mutator) for mutator in mutations]
    assert all(outcomes)
    print(
        "W3_TWO_CLASS_MINIMAL_LEDGER_REDUCTION_AUDIT_PASS "
        f"mutations={sum(outcomes)}/{len(outcomes)}"
    )


if __name__ == "__main__":
    main()
