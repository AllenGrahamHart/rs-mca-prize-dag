#!/usr/bin/env python3
"""Verify the cell-3 BC- uncolored EF residual exclusion."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
E = ROOT / "experiments/prize_resolution"
PREFIX = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcminus_"
CORE = E / f"{PREFIX}uncolored_exceptional_certificate.py"
LAUNCHER = E / f"{PREFIX}uncolored_exceptional_fibers_modal.py"
GENERIC = E / f"{PREFIX}uncolored_generic_rank_result.json"
ROOTS = E / f"{PREFIX}uncolored_guard_roots_result.json"
LIFTS = E / f"{PREFIX}guard_lifts_result.json"
RESULT = E / f"{PREFIX}uncolored_exceptional_EF_result.json"
CORE_SHA256 = "94265c13d3fb11863442f02f784fc5b0f438c687e6eb7c528858e6b8630a96c0"
LAUNCHER_SHA256 = "a8528c7e57423cd96ca531d9899e228247fb26eacd41c5d1bcb525e32ea62b54"
GENERIC_SHA256 = "5f0a1569a0bdbf61b5e066874ea9adc4b20d8602153d3804e3a0fcf94e0e50c9"
ROOTS_SHA256 = "c0ebc30fd4499318b8a8fc883d418ab6c85db5b04fa49ed7f01c005e1d165705"
LIFTS_SHA256 = "0694f171b26fe86db214c27f5ffa0f05f49eaf8370938ae83b936babdf01b1fb"
RESULT_SHA256 = "519418c3a1fc95f78ec58005481c49769ae14d5119e8bc45eb01f0db3f2919c1"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_guard_lift_atlas"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcminus_uncolored_complete_outside_exclusion"
SPEC = importlib.util.spec_from_file_location("uncolored_certificate", CORE)
CERT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CERT)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_payloads():
    return tuple(json.loads(path.read_text()) for path in
                 (RESULT, GENERIC, ROOTS, LIFTS))


def validate(payload, generic, roots, lifts):
    require(payload["source_hashes"] == {
        "generic": GENERIC_SHA256,
        "roots": ROOTS_SHA256,
        "lifts": LIFTS_SHA256,
    }, "source links")
    return CERT.validate_exceptional("EF", payload, generic, roots, lifts)


def main():
    for path, digest in (
        (CORE, CORE_SHA256), (LAUNCHER, LAUNCHER_SHA256),
        (GENERIC, GENERIC_SHA256), (ROOTS, ROOTS_SHA256),
        (LIFTS, LIFTS_SHA256), (RESULT, RESULT_SHA256),
    ):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                f"custody {path.name}")
    summary = validate(*load_payloads())
    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {row["id"]: row for row in dag["nodes"]}
    edges = {(row["from"], row["to"], row.get("kind", "req"))
             for row in dag["edges"]}
    require(nodes[NODE.name]["status"] == "PROVED", "DAG status")
    require(nodes[PARENT]["status"] == "PROVED"
            and (PARENT, NODE.name, "req") in edges, "parent")
    require((NODE.name, CONSUMER, "req") in edges, "consumer")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_BCMINUS_UNCOLORED_EF_VERIFY_PASS cases={cases} fibers={fibers} unit_endpoints={endpoint_rows} labels=120".format(**summary))


if __name__ == "__main__":
    main()
