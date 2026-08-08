#!/usr/bin/env python3
"""Independent custody and source-identity audit for endpoint exclusion."""

import copy
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
P = 2130706433
REPLAY = EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_compatibility_replay_result.json"
PRIMARY = EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_residual_census_result.json"
AUDIT = EXP / "rate_half_kb_positive_433_1b_cell12_endpoint_residual_audit_result.json"
KERNEL = EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def pairings(values):
    values = tuple(values)
    if not values:
        yield ()
        return
    first = values[0]
    for index in range(1, len(values)):
        second = values[index]
        rest = values[1:index] + values[index + 1:]
        for tail in pairings(rest):
            yield ((first, second),) + tail


def target_summary(payload):
    expected = {
        (epsilon, endpoint, sigma)
        for epsilon in itertools.product((-1, 1), repeat=2)
        for endpoint in ("b", "c")
        for sigma in itertools.product((-1, 1), repeat=2)
    }
    rows = {}
    for row in payload["rows"]:
        key = (tuple(row["epsilon"]), row["endpoint"], tuple(row["sigma"]))
        require(key in expected and key not in rows, "bad target key")
        systems = row["systems"]
        complete = (
            row["status"] == "COMPLETE"
            and not row.get("witnesses", []) and not row.get("unresolved", [])
        )
        if "unit_systems" in row:
            complete = complete and row["unit_systems"] == systems
        if "unit_unrestricted" in row:
            complete = complete and row["unit_unrestricted"] == systems
        require(complete, "incomplete target row")
        rows[key] = systems
    require(set(rows) == expected, "target Cartesian coverage")
    return rows


def main():
    replay = json.loads(REPLAY.read_text())
    primary = json.loads(PRIMARY.read_text())
    audit = json.loads(AUDIT.read_text())
    kernel_payload = json.loads(KERNEL.read_text())
    t, r, b, c = sp.symbols("t r b c")
    kernel = [sp.sympify(item["expression"])
              for item in kernel_payload["rows"][0]["kernel"]]

    point_total = 0
    for row in replay["rows"]:
        endpoint = row["endpoint"]
        for point in row["generic_points"]:
            substitutions = {t: point["t"], r: point["r"],
                             b: point["b"], c: point["c"]}
            values = [int(value.subs(substitutions)) % P for value in kernel]
            x = -point["t"] * point["t"] % P
            av = sum(values[i] * pow(x, i, P) for i in range(3)) % P
            bv = sum(values[i + 3] * pow(x, i, P) for i in range(3)) % P
            require(av and point["missing"] == bv * pow(av, -1, P) % P,
                    "missing-product replay")
            source_sum = x * pow((values[6] + values[7] * x) % P, 2, P)
            source_sum = source_sum * pow(av, -2, P) % P
            require(point["source_sum"] == source_sum, "source-sum replay")
            u = point[endpoint]
            compatibility = (pow((u*u + point["missing"]) % P, 2, P)
                             - source_sum*u*u) % P
            require(compatibility == 0, "endpoint compatibility replay")
            representatives = (1, point["b"], point["c"])
            require(all(representatives)
                    and all((left-right) % P and (left+right) % P
                            for left, right in itertools.combinations(
                                representatives, 2)),
                    "source guard replay")
            point_total += 1
    require(point_total == 40, "source-point total")

    matchings = tuple(pairings(range(6)))
    require(len(matchings) == 15 and len(set(matchings)) == 15,
            "independent matching count")
    primary_summary = target_summary(primary)
    audit_summary = target_summary(audit)
    require(primary_summary == audit_summary
            and sum(primary_summary.values()) == 2400,
            "independent ledger agreement")
    require(audit["source_primary_sha256"] == hashlib.sha256(
        PRIMARY.read_bytes()).hexdigest(), "audit-primary custody")

    hostile = copy.deepcopy(audit)
    hostile["rows"][0]["unit_unrestricted"] -= 1
    try:
        target_summary(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile completeness mutation survived")

    hostile = copy.deepcopy(primary)
    hostile["rows"].append(copy.deepcopy(hostile["rows"][0]))
    try:
        target_summary(hostile)
    except RuntimeError:
        pass
    else:
        raise RuntimeError("hostile duplicate mutation survived")
    print("PASS independent endpoint audit: identities, 15 matchings, 2400 systems")


if __name__ == "__main__":
    main()
