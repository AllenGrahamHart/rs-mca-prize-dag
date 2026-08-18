#!/usr/bin/env python3
"""Verify exclusion of all fourteen exceptional FFF fibers."""

import hashlib
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
SPEC_RESULT = EXP / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_specializations_result.json"
SPEC_CHECK = EXP / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_specializations_check.py"
ADM_RESULT = EXP / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_admissibility_result.json"
ADM_CHECK = EXP / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_admissibility_check.py"
SPEC_RESULT_SHA256 = "c066bb4f5813be4915e40a51225287cfde11284b3b3df4cabdae889778a97b88"
SPEC_CHECK_SHA256 = "4f181e05b7a2fa4db332551a5f35f58030e937ab9dc333e56e7621dd5b5b9623"
ADM_RESULT_SHA256 = "71bb63b164620fb408c08377e33224db69b6dac929ab375ead370ebd658e45ee"
ADM_CHECK_SHA256 = "7575d298187363331f7a9b18179a059de0adb1849e15f123af5140dfb44d8f65"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def checkers():
    for path, digest in ((SPEC_RESULT, SPEC_RESULT_SHA256),
                         (SPEC_CHECK, SPEC_CHECK_SHA256),
                         (ADM_RESULT, ADM_RESULT_SHA256),
                         (ADM_CHECK, ADM_CHECK_SHA256)):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "custody")
    return load("fff_spec_check", SPEC_CHECK), load("fff_adm_check", ADM_CHECK)


def main():
    spec_checker, adm_checker = checkers()
    first = spec_checker.verify()
    second = adm_checker.verify()
    direct = {row["root"] for row in first if row["unit"]}
    survivors = {row["root"] for row in first if not row["unit"]}
    closed = {row["root"] for row in second if row["unit"]}
    require(len(direct) == 5 and len(survivors) == 9 and
            closed == survivors, "fiber partition")
    require({row["first_unit_stage"] for row in second} <=
            {"route:0", "route:3", "route:5", "q4"}, "closure stages")
    require(sum(row["first_unit_stage"] == "q4" for row in second) == 2,
            "q4 fiber census")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_FFF_"
          "EXCEPTIONAL_FIBER_VERIFY_PASS direct=5 guarded=9 total=14")


if __name__ == "__main__":
    main()
