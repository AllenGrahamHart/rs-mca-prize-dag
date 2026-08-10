#!/usr/bin/env python3
"""Hostile completeness audit for the cell-11 parallel-DE packet."""

import copy
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("cell11_parallel_verify", NODE / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def rejected(callback, message):
    try:
        callback()
    except (RuntimeError, KeyError, TypeError):
        return
    raise RuntimeError(message)


def keyed(rows):
    return {(tuple(row["epsilon"]), row["cut_kind"]): row for row in rows}


def check_cover(payload):
    wanted = {(sign, kind) for sign in VERIFY.SIGNS for kind in VERIFY.KINDS}
    rows = keyed(payload["rows"])
    VERIFY.require(set(rows) == wanted, "row cover")
    return rows


def check_replay(payload):
    rows = check_cover(payload)
    for row in rows.values():
        VERIFY.require(
            row["status"] == "COMPLETE"
            and row["excluded_generic"]
            and not row["witnesses"]
            and not row["unresolved"],
            "terminal replay",
        )


def check_kernel(payload):
    signatures = {
        tuple((item["degree"], item["terms"]) for item in row["kernel"])
        for row in payload["rows"]
    }
    VERIFY.require(len(signatures) == 1, "sign-dependent common kernel")


def main():
    norm, replay, audit = VERIFY.validate()

    dropped = copy.deepcopy(audit)
    dropped["rows"].pop()
    rejected(lambda: check_cover(dropped), "dropped audit row survived")

    altered = copy.deepcopy(norm)
    altered["rows"][0]["candidate_roots"][0] += 1
    rejected(
        lambda: VERIFY.require(
            altered["rows"][0]["candidate_roots"]
            == audit["rows"][0]["candidate_roots"],
            "candidate mismatch",
        ),
        "altered candidate root survived",
    )

    witness = copy.deepcopy(replay)
    witness["rows"][0]["witnesses"].append({"hostile": True})
    witness["rows"][0]["excluded_generic"] = False
    rejected(lambda: check_replay(witness), "generic witness survived")

    kernel = __import__("json").loads(VERIFY.KERNEL.read_text())
    check_kernel(kernel)
    divergent = copy.deepcopy(kernel)
    divergent["rows"][0]["kernel"][0]["degree"] += 1
    rejected(lambda: check_kernel(divergent), "divergent kernel survived")

    print("PASS hostile cell-11 parallel-DE audit: 4/4 mutations rejected")


if __name__ == "__main__":
    main()
