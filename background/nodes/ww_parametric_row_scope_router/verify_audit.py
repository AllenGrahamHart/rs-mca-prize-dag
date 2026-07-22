#!/usr/bin/env python3
"""Mutation audit for the W3 parametric row-scope repair."""

from __future__ import annotations

from copy import deepcopy

from verify import CONSUMER, DESCRIPTOR, NODE_ID, evaluate, load_inputs


def rejected(mutator) -> bool:
    dag, official, descriptor, documents = deepcopy(load_inputs())
    mutator(dag, official, descriptor, documents)
    return not all(evaluate(dag, official, descriptor, documents).values())


def main() -> None:
    dag, official, descriptor, documents = load_inputs()
    assert all(evaluate(dag, official, descriptor, documents).values())

    mutations = [
        lambda d, o, x, m: next(
            node for node in d["nodes"] if node["id"] == NODE_ID
        ).update(status="TARGET"),
        lambda d, o, x, m: next(
            node for node in d["nodes"] if node["id"] == CONSUMER
        ).update(status="REFUTED"),
        lambda d, o, x, m: d.update(
            edges=[
                edge
                for edge in d["edges"]
                if not (edge["from"] == DESCRIPTOR and edge["to"] == NODE_ID)
            ]
        ),
        lambda d, o, x, m: o.update(verdict="fixed_registry"),
        lambda d, o, x, m: x["target"].update(B_star_decimal="7"),
        lambda d, o, x, m: m.update(
            statement=m["statement"].replace("q=1705*2^120+1", "q=17")
        ),
        lambda d, o, x, m: m.update(
            frontier=m["frontier"].replace(
                "admissible prime", "unscoped field"
            )
        ),
        lambda d, o, x, m: m.update(
            frontier=m["frontier"].replace(
                "Do not run the former W3 envelope campaign", "Run W3 sweep"
            )
        ),
        lambda d, o, x, m: m.update(
            roadmap=m["roadmap"].replace(
                "D0 — RESOLVED BY SCOPE CORRECTION AND REWIRE", "D0 — raw sweep"
            )
        ),
        lambda d, o, x, m: m.update(
            compute=m["compute"].replace(
                "CANCELED; NO LIVE CONSUMER; DO NOT RUN", "READY"
            )
        ),
    ]
    outcomes = [rejected(mutator) for mutator in mutations]
    assert all(outcomes)
    print(
        "W3_PARAMETRIC_ROW_SCOPE_ROUTER_AUDIT_PASS "
        f"mutations={sum(outcomes)}/{len(outcomes)}"
    )


if __name__ == "__main__":
    main()
