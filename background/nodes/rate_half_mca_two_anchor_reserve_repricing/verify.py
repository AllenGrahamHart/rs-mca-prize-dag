#!/usr/bin/env python3
"""Verify exact two-anchor repricing of the deployed MCA reserve."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "172934ca92647c61e054f30b8ec25be83844f2859f32245a20c5234eda11f56e"
TOP_KEYS = {
    "schema",
    "canonical_dossier_commit",
    "upstream",
    "old_exception_cap",
    "rows",
}
ROW_KEYS = {"name", "n", "K", "m", "B_star", "average_ceiling", "expected"}
EXPECTED_KEYS = {
    "w",
    "two_w",
    "combined_reserve",
    "g_min",
    "target_g_min",
    "target_full",
    "full_average_quotient",
    "full_average_remainder",
}


class Reject(ValueError):
    pass


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer field")
    return value


def validate(data: object) -> list[dict[str, int | str]]:
    if not isinstance(data, dict) or set(data) != TOP_KEYS:
        raise Reject("top-level schema")
    if data["schema"] != "rate-half-mca-two-anchor-reserve-source-v1":
        raise Reject("schema")
    if data["canonical_dossier_commit"] != "c8d48cd4b94fb256ad9fedfc1d53b4b14c77bfad":
        raise Reject("canonical pin")
    upstream = data["upstream"]
    if not isinstance(upstream, dict) or upstream != {
        "head": "e26c15b2d2c2f98ae12dda17b97c40981f76e1ff",
        "grande_finale_blob": "5e0cb1bad6b40c4db39f6b4cb3e5316aebeafe2f",
        "two_anchor_note_blob": "12bc4a0f06189829a9490928e4855d1aa958f940",
        "shortening_note_blob": "65a308ac97912de3dfe637d8a10a2f84e3a19c47",
    }:
        raise Reject("upstream pins")
    exception_cap = integer(data["old_exception_cap"])
    if exception_cap != 31:
        raise Reject("exception cap")
    rows = data["rows"]
    if not isinstance(rows, list) or len(rows) != 2:
        raise Reject("rows")

    output: list[dict[str, int | str]] = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != ROW_KEYS:
            raise Reject("row schema")
        expected = row["expected"]
        if not isinstance(expected, dict) or set(expected) != EXPECTED_KEYS:
            raise Reject("expected schema")
        name = row["name"]
        if not isinstance(name, str):
            raise Reject("name")
        n = integer(row["n"])
        dimension = integer(row["K"])
        agreement = integer(row["m"])
        budget = integer(row["B_star"])
        average = integer(row["average_ceiling"])
        if not 0 < dimension < agreement < n or budget <= 0 or average <= 0:
            raise Reject("row range")

        w = agreement - dimension
        two_w = 2 * w
        reserve = two_w + exception_cap
        g_min = 2 * agreement - dimension + 1
        target_min = budget - reserve - (n - g_min)
        target_full = budget - reserve
        quotient, remainder = divmod(target_full, average)
        derived = {
            "w": w,
            "two_w": two_w,
            "combined_reserve": reserve,
            "g_min": g_min,
            "target_g_min": target_min,
            "target_full": target_full,
            "full_average_quotient": quotient,
            "full_average_remainder": remainder,
        }
        if expected != derived:
            raise Reject("derived row")
        if w < 1 or 3 * w > n - dimension or two_w <= exception_cap:
            raise Reject("two-anchor or nonabsorption guard")
        if target_min <= 0 or target_full <= 0 or quotient < 1:
            raise Reject("target viability")

        affine_total = reserve + (n - agreement + 1)
        middle_total = reserve + n
        if affine_total >= budget or middle_total >= budget:
            raise Reject("small-owner branch margin")
        for g in range(g_min, n + 1):
            old_target = budget - exception_cap - (n - g)
            new_target = budget - reserve - (n - g)
            if old_target - new_target != two_w:
                raise Reject("target movement")
            if two_w + exception_cap + (n - g) + new_target != budget:
                raise Reject("large-owner exact sum")
        output.append(
            {
                "name": name,
                **derived,
                "affine_margin": budget - affine_total,
                "middle_margin": budget - middle_total,
            }
        )
    if [row["name"] for row in output] != ["KoalaBear MCA", "Mersenne-31 MCA"]:
        raise Reject("row order")
    return output


def main() -> None:
    if hashlib.sha256(CONTRACT.read_bytes()).hexdigest() != CONTRACT_SHA256:
        raise Reject("contract hash")
    data = json.loads(CONTRACT.read_text())
    rows = validate(data)

    mutations = (
        lambda item: item.__setitem__("old_exception_cap", 30),
        lambda item: item["rows"][0].__setitem__("B_star", item["rows"][0]["B_star"] - 1),
        lambda item: item["rows"][0]["expected"].__setitem__("two_w", 1),
        lambda item: item["rows"][0]["expected"].__setitem__("target_full", 0),
        lambda item: item["rows"][1].__setitem__("average_ceiling", 1_752_701),
        lambda item: item["rows"][1].__setitem__("m", item["rows"][1]["m"] + 1),
        lambda item: item["rows"].reverse(),
        lambda item: item["upstream"].__setitem__("head", "0" * 40),
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
        "RATE_HALF_MCA_TWO_ANCHOR_RESERVE_REPRICING_PASS "
        f"rows={len(rows)} g_checks={sum(2097152-int(row['g_min'])+1 for row in rows)} "
        f"mersenne_factor={rows[1]['full_average_quotient']} "
        f"controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
