#!/usr/bin/env python3
"""Mutation audit for the QA.22/W3 currency separation."""

from __future__ import annotations

from copy import deepcopy

from verify import NODE_ID, W3, WORST, XR_BUDGET, evaluate, load_inputs


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
            edge
            for edge in d["edges"]
            if edge["from"] == XR_BUDGET and edge["to"] == WORST
        ).update(kind="req"),
        lambda d, m: next(
            node for node in d["nodes"] if node["id"] == W3
        ).update(status="REFUTED"),
        lambda d, m: d.update(
            edges=[edge for edge in d["edges"] if edge["to"] != NODE_ID]
        ),
        lambda d, m: m.update(
            xr=m["xr"].replace("bad-slope count", "list-word count")
        ),
        lambda d, m: m.update(
            w3=m["w3"].replace("MCA `16n^3`", "list reserve")
        ),
        lambda d, m: m.update(
            worst=m["worst"].replace(
                "List(U)=p(U)+N_nonplant(U)", "QA.22's per-pair bound"
            )
        ),
        lambda d, m: m.update(
            compute=m["compute"].replace(
                "Do not spend contributor or Modal compute extending the old W3/QA.22 sweep",
                "Rerun QA.22 for W3",
            )
        ),
    ]
    outcomes = [rejected(mutator) for mutator in mutations]
    assert all(outcomes)
    print(
        "WW_QA22_CURRENCY_SEPARATION_AUDIT_PASS "
        f"mutations={sum(outcomes)}/{len(outcomes)}"
    )


if __name__ == "__main__":
    main()
