#!/usr/bin/env python3
"""Verify the cell-3 BC+ uncolored EF residual exclusion."""

import hashlib
import importlib.util
import json
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
E = ROOT / "experiments/prize_resolution"
PREFIX = "rate_half_kb_positive_433_1b_o0b_common_repeat_cell3_bcplus_"
CORE = E / f"{PREFIX}uncolored_exceptional_certificate.py"
LAUNCHER = E / f"{PREFIX}uncolored_exceptional_fibers_modal.py"
GENERIC = E / f"{PREFIX}uncolored_generic_rank_result.json"
ROOTS = E / f"{PREFIX}uncolored_guard_roots_result.json"
TORUS = E / f"{PREFIX}monomial_probe_result.json"
RESULT = E / f"{PREFIX}uncolored_exceptional_EF_result.json"
CORE_SHA256 = "a4ed26484ebf046ee9789e16a5ce246fe18e4240b0ef07444f6f0ff32410a0b7"
LAUNCHER_SHA256 = "f6bb5864d7bc1c672cb4d61960d991478ef86952487d550f31d6db76198da86d"
GENERIC_SHA256 = "084af4aebeaaa536558c1e71252a2ed6c3e19ac21f00160eb136ee70dc8a65fe"
ROOTS_SHA256 = "719e586402513ac950c59a588b0aab0e35bdb4e7073f301e460cbceec3b3ad98"
TORUS_SHA256 = "9ad509b330416fc095fcbf6ff2ac75ae82123cc824b4f819e3c6aac0c78279fc"
RESULT_SHA256 = "2bf7ca06b66ec2bb825e6a149a20788174a16ef5f87ba6ff7f4d350ef060a7f1"
PARENT = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cell3_bcplus_uncolored_guard_root_atlas"
CONSUMER = "rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_repeat_cells3_6_bcplus_complete_outside_exclusion"
SPEC = importlib.util.spec_from_file_location("uncolored_certificate", CORE)
CERT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CERT)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_payloads():
    return tuple(json.loads(path.read_text()) for path in
                 (RESULT, GENERIC, ROOTS, TORUS))


def validate(payload, generic, roots, torus):
    require(payload["source_hashes"] == {
        "generic": GENERIC_SHA256,
        "roots": ROOTS_SHA256,
        "torus": TORUS_SHA256,
    }, "source links")
    return CERT.validate_exceptional("EF", payload, generic, roots, torus)


def main():
    for path, digest in (
        (CORE, CORE_SHA256), (LAUNCHER, LAUNCHER_SHA256),
        (GENERIC, GENERIC_SHA256), (ROOTS, ROOTS_SHA256),
        (TORUS, TORUS_SHA256), (RESULT, RESULT_SHA256),
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
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_REPEAT_BCPLUS_UNCOLORED_EF_VERIFY_PASS cases={cases} fibers={fibers} unit_endpoints={endpoint_rows} labels=120".format(**summary))


if __name__ == "__main__":
    main()
