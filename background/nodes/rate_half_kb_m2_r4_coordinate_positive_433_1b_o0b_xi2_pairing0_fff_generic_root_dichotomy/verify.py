#!/usr/bin/env python3
"""Verify the FFF generic determinant and exhaustive root dichotomy."""

import hashlib
import importlib.util
from pathlib import Path


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
DET_RESULT = EXP / "rate_half_kb_positive_433_1b_o0b_fff_r76_ntt_determinant_result.json"
DET_CHECK = EXP / "rate_half_kb_positive_433_1b_o0b_fff_r76_ntt_determinant_check.py"
ROOT_RESULT = EXP / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_roots_result.json"
ROOT_CHECK = EXP / "rate_half_kb_positive_433_1b_o0b_fff_exceptional_roots_check.py"
DET_RESULT_SHA256 = "a222789bb3e54df1a4198536644a6d331972087d968b61b227634eca22a79786"
DET_CHECK_SHA256 = "122ed0b3c2f863ddbc93d3feed8bacb3ab04ec49fd7dff15d1525527336c7778"
ROOT_RESULT_SHA256 = "e845607b89e7d21159bd308cbf00f9a3fd74a25120bc4d479a607f7e9d8751a7"
ROOT_CHECK_SHA256 = "568e78350d7232d9392df018b01e6936cf1b27f494dcda011b05517dc3884fa3"
ROOTS = [
    0, 1, 16711679, 47655010, 451278922, 465887767, 666570304,
    676802667, 1036595577, 1141382033, 1629292471, 1893783428,
    2113994754, 2130706432,
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def checkers():
    for path, digest in ((DET_RESULT, DET_RESULT_SHA256),
                         (DET_CHECK, DET_CHECK_SHA256),
                         (ROOT_RESULT, ROOT_RESULT_SHA256),
                         (ROOT_CHECK, ROOT_CHECK_SHA256)):
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "custody")
    return load("fff_det_check", DET_CHECK), load("fff_root_check", ROOT_CHECK)


def main():
    det_checker, root_checker = checkers()
    det = det_checker.verify()
    roots = root_checker.verify()
    require(det["status"] == "COMPLETE" and det["determinant_degree"] == 19060
            and det["determinant_term_count"] == 18711, "determinant theorem")
    require(roots["roots"] == ROOTS and roots["root_count"] == 14 and
            roots["groups"][-1]["roots"] == ROOTS, "root exhaustiveness")
    print("RATE_HALF_KB_POSITIVE_433_1B_O0B_XI2_PAIRING0_FFF_"
          "GENERIC_ROOT_DICHOTOMY_VERIFY_PASS degree=19060 roots=14")


if __name__ == "__main__":
    main()
