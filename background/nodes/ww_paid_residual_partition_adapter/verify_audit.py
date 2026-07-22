#!/usr/bin/env python3
"""Mutation audit for the W3 paid/residual partition adapter."""

from __future__ import annotations

from copy import deepcopy

from verify import CONSUMER, DEPENDENCY, NODE_ID, evaluate, load_inputs


def rejected(mutator) -> bool:
    dag, documents = deepcopy(load_inputs())
    mutator(dag, documents)
    return not all(evaluate(dag, documents).values())


def main() -> None:
    assert all(evaluate(*load_inputs()).values())
    mutations = [
        lambda d, m: next(
            node for node in d["nodes"] if node["id"] == NODE_ID
        ).update(status="TARGET"),
        lambda d, m: next(
            node for node in d["nodes"] if node["id"] == DEPENDENCY
        ).update(status="TARGET"),
        lambda d, m: next(
            node for node in d["nodes"] if node["id"] == CONSUMER
        ).update(status="REFUTED"),
        lambda d, m: d.update(
            edges=[edge for edge in d["edges"] if edge["to"] != NODE_ID]
        ),
        lambda d, m: m.update(
            statement=m["statement"].replace(
                "B_chal(U) = B* - sum_i u_i(U)", "B_chal(U) is heuristic"
            )
        ),
        lambda d, m: m.update(
            statement=m["statement"].replace(
                "does not define the paid predicates", "defines all predicates"
            )
        ),
        lambda d, m: m.update(
            proof=m["proof"].replace("enlarges the residual", "is discarded")
        ),
    ]
    outcomes = [rejected(mutator) for mutator in mutations]
    assert all(outcomes)
    print(
        "W3_PAID_RESIDUAL_PARTITION_ADAPTER_AUDIT_PASS "
        f"mutations={sum(outcomes)}/{len(outcomes)}"
    )


if __name__ == "__main__":
    main()
