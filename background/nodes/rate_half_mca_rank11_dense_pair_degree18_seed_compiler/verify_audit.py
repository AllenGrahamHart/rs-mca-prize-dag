#!/usr/bin/env python3
"""Independent audit of the dense-pair degree pin."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


CONTRACT = Path(__file__).with_name("source_contract.json")
SHA256 = "48c77d234369c35e783a1ad98afe915caef50c071ddd263a2912034bc2de7906"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> dict[str, int]:
    require(isinstance(data, dict), "contract")
    row = data.get("official")
    toy = data.get("toy")
    schedule = data.get("selection_schedule")
    require(isinstance(row, dict) and isinstance(toy, dict) and isinstance(schedule, list), "records")

    low, pairs = row.get("low_record_minimum"), row.get("pair_type_maximum")
    quotient, remainder = divmod(low, pairs)
    require((quotient, remainder) == (219, 121255661729), "pigeonhole division")
    require(quotient + bool(remainder) == row.get("dense_pair_owner_minimum") == 220, "owner ceiling")
    require(pairs + 981105 < low, "second heavy pair")

    singles = []
    for entry in schedule:
        t = entry.get("basis_pairs")
        doubled = min(t, row.get("other_slot_budget") - t)
        require(entry.get("used") == row.get("dense_records_selected") + t + doubled, "slot count")
        require(entry.get("doubled_pairs") == doubled, "double count")
        require(entry.get("single_pairs") == t - doubled, "single count")
        singles.append(t - doubled)
    require(max(singles) == 6, "six singles")
    selected_core = row.get("K") - 4923 + max(singles) * 387
    require(selected_core == row.get("selected_common_support_maximum") == row.get("K") - 2601, "core")

    p = toy.get("field")
    a, b, q = (toy.get(k) for k in ("line_constant", "line_direction", "degree18_coefficient"))
    values = []
    for z in toy.get("slopes"):
        product = 1
        for root in range(toy.get("dense_slopes")):
            product = product * (z - root) % p
        values.append((a + b * z + q * product) % p)
    differences = values
    highest = 0
    for order in range(1, len(values)):
        differences = [(differences[i + 1] - differences[i]) % p for i in range(len(differences) - 1)]
        if any(differences):
            highest = order
    require(highest == toy.get("expected_degree") == 18, "finite-difference degree")
    require(all(values[z] == (a + b * z) % p for z in range(18)), "eighteen roots")
    require(values[18] != (a + 18 * b) % p, "off line")
    require(row.get("slope_degree_minimum") == 18 and row.get("slope_degree_maximum") == 31, "degree range")
    return {"owner": quotient + 1, "core": selected_core, "degree": highest}


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    result = audit(data)
    controls = []
    for section, key, value in (
        ("official", "pair_type_maximum", 869784434120),
        ("official", "selected_common_support_maximum", 1045976),
        ("official", "slope_degree_maximum", 30),
        ("toy", "degree18_coefficient", 0),
        ("toy", "expected_degree", 17),
    ):
        altered = copy.deepcopy(data)
        altered[section][key] = value
        try:
            audit(altered)
        except (Reject, TypeError, ZeroDivisionError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "audit controls")
    print(
        "RATE_HALF_MCA_RANK11_DENSE_PAIR_DEGREE18_SEED_AUDIT_PASS "
        f"owner={result['owner']} core={result['core']} degree={result['degree']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
