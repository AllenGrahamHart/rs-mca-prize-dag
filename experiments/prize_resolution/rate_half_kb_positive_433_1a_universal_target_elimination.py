#!/usr/bin/env python3
"""Verify universal target elimination for positive 433-1a outside rows."""

import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp


DIRECTORY = Path(__file__).resolve().parent
SYMMETRY_SCRIPT = DIRECTORY / (
    "rate_half_kb_positive_433_1a_outside_case_symmetry.py"
)
RESULT = DIRECTORY / (
    "rate_half_kb_positive_433_1a_universal_target_elimination_result.json"
)
RECORDS = ("DE+", "DE-", "DF+", "DF-", "EF", "BE", "CF")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def payload_hash(value):
    clone = copy.deepcopy(value)
    clone.pop("payload_sha256", None)
    return hashlib.sha256(canonical_json(clone).encode()).hexdigest()


def load_symmetry():
    specification = importlib.util.spec_from_file_location(
        "outside_case_symmetry", SYMMETRY_SCRIPT
    )
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def universal_identity_replay(cycle_sign):
    b, c, d, e, f = sp.symbols("b c d e f", nonzero=True)
    records = {
        "DE+": d * e,
        "DE-": -d * e,
        "DF+": d * f,
        "DF-": -d * f,
        "EF": cycle_sign * e * f,
        "BE": b * e,
        "CF": c * f,
    }
    product_relations = (
        records["DE-"] + records["DE+"],
        records["DF-"] + records["DF+"],
        records["BE"] * records["CF"]
        - cycle_sign * b * c * records["EF"],
        b * records["DE+"] * records["CF"]
        - c * records["DF+"] * records["BE"],
    )
    require(all(sp.expand(value) == 0 for value in product_relations),
            "universal product relations")

    reconstructed = {
        "e": records["BE"] / b,
        "f": records["CF"] / c,
        "d": b * records["DE+"] / records["BE"],
    }
    require(sp.cancel(reconstructed["e"] - e) == 0, "reconstruct e")
    require(sp.cancel(reconstructed["f"] - f) == 0, "reconstruct f")
    require(sp.cancel(reconstructed["d"] - d) == 0, "reconstruct d")

    sums_squared = {
        "DE+": (d + e)**2,
        "DE-": (d - e)**2,
        "DF+": (d + f)**2,
        "DF-": (d - f)**2,
        "EF": (e + cycle_sign * f)**2,
        "BE": (b + e)**2,
        "CF": (c + f)**2,
    }
    cleared_sum_relations = {
        "DE+": (
            b**2 * records["BE"]**2 * sums_squared["DE+"]
            - (b**2 * records["DE+"] + records["BE"]**2)**2
        ),
        "DE-": (
            b**2 * records["BE"]**2 * sums_squared["DE-"]
            - (b**2 * records["DE+"] - records["BE"]**2)**2
        ),
        "DF+": (
            c**2 * records["CF"]**2 * sums_squared["DF+"]
            - (c**2 * records["DF+"] + records["CF"]**2)**2
        ),
        "DF-": (
            c**2 * records["CF"]**2 * sums_squared["DF-"]
            - (c**2 * records["DF+"] - records["CF"]**2)**2
        ),
        "EF": (
            b**2 * c**2 * sums_squared["EF"]
            - (c * records["BE"]
               + cycle_sign * b * records["CF"])**2
        ),
        "BE": (
            b**2 * sums_squared["BE"]
            - (b**2 + records["BE"])**2
        ),
        "CF": (
            c**2 * sums_squared["CF"]
            - (c**2 + records["CF"])**2
        ),
    }
    require(all(sp.expand(value) == 0
                for value in cleared_sum_relations.values()),
            "universal squared-sum relations")
    return {
        "cycle_sign": cycle_sign,
        "product_relation_count": len(product_relations),
        "squared_sum_relation_count": len(cleared_sum_relations),
        "reconstruction": {
            "e": "BE/b",
            "f": "CF/c",
            "d": "b*DE+/BE",
        },
    }


def case_slot_map(case):
    eta, xi, matching = case
    slots = ("u", "v", "w")
    record_to_slot = {xi: "xi"}
    for source, pair in zip(slots, matching):
        record_to_slot[pair[0]] = source
        record_to_slot[pair[1]] = f"-{source}"
    require(set(record_to_slot) == set(RECORDS), "complete case slot map")
    return {
        "eta": eta,
        "xi_record": xi,
        "record_to_source_slot": record_to_slot,
    }


def compile_result():
    symmetry = load_symmetry()
    quotient = symmetry.compile_result()
    compiled = {}
    for alignment in ("aligned", "near"):
        entries = []
        for representative in quotient["representatives"][alignment]:
            case = (
                representative["eta"],
                representative["xi"],
                tuple(tuple(pair) for pair in representative["matching"]),
            )
            entries.append(case_slot_map(case))
        compiled[alignment] = entries
    require((len(compiled["aligned"]), len(compiled["near"])) == (39, 228),
            "compiled representative counts")

    template_a = {
        "DE+": "u", "DF-": "-u", "DE-": "v", "CF": "-v",
        "DF+": "w", "BE": "-w", "EF": "xi",
    }
    template_b = {
        "DE+": "u", "CF": "-u", "DE-": "v", "DF+": "-v",
        "DF-": "w", "BE": "-w", "EF": "xi",
    }
    template_cross_relations = {
        "A": "b*F(u)*F(-v)-c*F(w)*F(-w)=0",
        "B": "b*F(u)*F(-u)-c*F(-v)*F(-w)=0",
    }
    require(template_a["EF"] == template_b["EF"] == "xi",
            "template missing mate")

    data = {
        "schema": "rate-half-kb-positive-433-1a-universal-target-elimination-v1",
        "scope": (
            "all seven target product and squared-sum records for every "
            "formal outside case; source/common equations and route "
            "emptiness remain open"
        ),
        "cycle_sign_replays": [
            universal_identity_replay(cycle_sign) for cycle_sign in (-1, 1)
        ],
        "universal_product_relations": [
            "DE-+DE+=0",
            "DF-+DF+=0",
            "BE*CF-sigma*b*c*EF=0",
            "b*DE+*CF-c*DF+*BE=0",
        ],
        "universal_squared_sum_relations": {
            "DE+": "b^2*BE^2*H(DE+)-(b^2*DE++BE^2)^2=0",
            "DE-": "b^2*BE^2*H(DE-)-(b^2*DE+-BE^2)^2=0",
            "DF+": "c^2*CF^2*H(DF+)-(c^2*DF++CF^2)^2=0",
            "DF-": "c^2*CF^2*H(DF-)-(c^2*DF+-CF^2)^2=0",
            "EF": "b^2*c^2*H(EF)-(c*BE+sigma*b*CF)^2=0",
            "BE": "b^2*H(BE)-(b^2+BE)^2=0",
            "CF": "c^2*H(CF)-(c^2+CF)^2=0",
        },
        "explicit_target_reconstruction": {
            "e": "BE/b",
            "f": "CF/c",
            "d": "b*DE+/BE",
            "guards": ["b", "c", "DE+", "DF+", "EF", "BE", "CF"],
        },
        "compiled_case_maps": {
            "aligned_count": len(compiled["aligned"]),
            "near_count": len(compiled["near"]),
            "sha256": hashlib.sha256(canonical_json(compiled).encode()).hexdigest(),
        },
        "triangle_template_repair": {
            "A_record_to_slot": template_a,
            "B_record_to_slot": template_b,
            "missing_cross_relations": template_cross_relations,
        },
        "conclusion": {
            "target_variables_d_e_f_eliminated_exactly": True,
            "formal_case_count_compiled": 267,
            "outside_source_systems_proved_empty": False,
            "route_deleted": False,
        },
        "nonclaims": [
            "the four product relations do not impose the source rational map F",
            "the seven sum relations do not impose source-pair distinctness or unsquared q signs",
            "no formal case, alignment branch, 433-1a route, K3 row, or Prize result is closed",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    arguments = parser.parse_args()
    expected = compile_result()
    if arguments.write:
        RESULT.write_text(json.dumps(expected, indent=2, sort_keys=True) + "\n")
    if arguments.check or not arguments.write:
        observed = json.loads(RESULT.read_text())
        require(payload_hash(observed) == observed.get("payload_sha256"),
                "result seal")
        require(observed == expected, "result content")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_UNIVERSAL_TARGET_ELIMINATION_PASS "
        "product_relations=4 sum_relations=7 case_maps=267 "
        "template_cross_repairs=2"
    )


if __name__ == "__main__":
    main()
