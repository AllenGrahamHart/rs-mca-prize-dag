#!/usr/bin/env python3
"""Fail-closed verifier for the four balanced fixed exclusions."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
GENERIC = HERE / "modal_groebner_deployed_output.json"
RANK_DROP = HERE / "modal_rank_drop_all_output.json"
CELLS = ("F04-R11", "F05-R11", "F06-R11", "F07-R11")
EXPECTED_FILE_HASHES = {
    GENERIC.name: "92b875c99a3acdc0e4e211f21ae7c3cf072d60e00b36f74defedf702a0f3ca10",
    RANK_DROP.name: "04ebf7d90819ff2c1fc64e32ac70cf24dcd81e04838559a6f99275e34134b54d",
}
EXPECTED_GENERIC_BASES = {
    "F04-R11": "7c8a38347c7b8b45af2a346cbe9c8c0ac4f6e7158f1b060407583851c69c940e",
    "F05-R11": "d27d3cabc1d0ab4cb1e1ff490d969bd7c5967f44087776b5f74fcfa6f917387f",
    "F06-R11": "e6de209a7bff3b7756dc928309346d7eb9da494aec950731b9ec955de7385d19",
    "F07-R11": "09609c7a17cef90f854d055792fa1aea3781dd3daf1806b3bd566692118b0180",
}
EXPECTED_RANK_BASES = {
    ("F04-R11", 0): (9, "4c691fb37eb716319cec2798c96c157c1b9168e3fd89e8996dca78fbfb08fc39"),
    ("F04-R11", 1): (104, "e836e61de8f97c2138728c72fc436d0b240e3750a60c5e2beae0c7e3c3d66fe2"),
    ("F05-R11", 0): (9, "d62479cc12122df3115f07f04393fda65eb851170db08f13b075bffad99febfe"),
    ("F05-R11", 1): (106, "783b54538fb2df1c9aa437111c6d982f377fa7a37d05432bb2d265ab0572fff6"),
    ("F06-R11", 0): (9, "d62479cc12122df3115f07f04393fda65eb851170db08f13b075bffad99febfe"),
    ("F06-R11", 1): (106, "e2a0ecf51227f974c397015d9ae0c67dc983b4996240e7fd745dadeffd0217d9"),
    ("F07-R11", 0): (9, "4c691fb37eb716319cec2798c96c157c1b9168e3fd89e8996dca78fbfb08fc39"),
    ("F07-R11", 1): (104, "5002a355fdb89d637fc4f8ba538e3393ac0181346abc9a0df363af4bb02ccbe5"),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def done_record(row: dict[str, object]) -> dict[str, object]:
    records = [record for record in row["records"] if record.get("phase") == "DONE"]
    require(len(records) == 1, "exactly one DONE record")
    return records[0]


def check_generic(data: dict[str, object]) -> None:
    require(data["upstream_commit"] == "55ac3e07477bd7a768190a3e755f22b0d44354b0", "generic commit")
    require(data["counts"] == {"FAIL": 0, "PASS": 4, "REMOTE_ERROR": 0, "TIMEOUT": 0}, "generic counts")
    require(tuple(row["cell"] for row in data["results"]) == CELLS, "generic cells")
    for row in data["results"]:
        require(row["status"] == "PASS" and row["prime"] == 2130706433, "generic status")
        done = done_record(row)
        require(done["basis_size"] == 151 and done["dimension"] == 1, "generic basis shape")
        require(done["basis_sha256"] == EXPECTED_GENERIC_BASES[row["cell"]], "generic basis hash")
        require(done["localizer_factor_count"] == 25, "generic unit count")
        require(done["localizer_nilpotence_index"] == 1, "generic localizer")
        require(done["localizer_steps"][-1]["index"] == 16, "generic zero step")
        require(done["localizer_steps"][-1]["zero"] is True, "generic zero remainder")
        require(done["terminal"] == "EMPTY_AFTER_ESSENTIAL_CORE_LOCALIZATION", "generic terminal")


def check_rank_drop(data: dict[str, object]) -> None:
    require(data["upstream_commit"] == "55ac3e07477bd7a768190a3e755f22b0d44354b0", "rank commit")
    require(data["counts"] == {"FAIL": 0, "PASS": 8, "REMOTE_ERROR": 0, "TIMEOUT": 0}, "rank counts")
    require({(row["cell"], row["factor_index"]) for row in data["results"]} == set(EXPECTED_RANK_BASES), "rank cases")
    for row in data["results"]:
        key = (row["cell"], row["factor_index"])
        require(row["status"] == "PASS" and row["prime"] == 2130706433, "rank status")
        branch = next(record for record in row["records"] if record.get("phase") == "BRANCH")
        done = done_record(row)
        require(branch["nonnamed_v_factor_count"] == 2, "rank factor census")
        require(branch["selected"]["degree"] == (2 if key[1] == 0 else 10), "rank factor degree")
        require(branch["selected"]["terms"] == (6 if key[1] == 0 else 112), "rank factor terms")
        require((done["basis_size"], done["basis_sha256"]) == EXPECTED_RANK_BASES[key], "rank basis")
        require(done["dimension"] == 2 and done["localizer_nilpotence_index"] == 1, "rank localization")
        require(done["localizer_steps"][-1]["zero"] is True, "rank zero remainder")
        require(done["terminal"] == "RANK_DROP_FACTOR_EMPTY_AFTER_NAMED_LOCALIZATION", "rank terminal")


def main() -> None:
    for path in (GENERIC, RANK_DROP):
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        require(observed == EXPECTED_FILE_HASHES[path.name], f"file hash {path.name}")
    generic = json.loads(GENERIC.read_text())
    rank_drop = json.loads(RANK_DROP.read_text())
    check_generic(generic)
    check_rank_drop(rank_drop)

    hostile = copy.deepcopy(generic)
    hostile["results"][0]["records"][-1]["terminal"] = "SURVIVES"
    try:
        check_generic(hostile)
    except AssertionError:
        pass
    else:
        raise AssertionError("generic terminal mutation accepted")

    hostile = copy.deepcopy(rank_drop)
    hostile["results"][0]["records"][-1]["localizer_nilpotence_index"] = None
    try:
        check_rank_drop(hostile)
    except AssertionError:
        pass
    else:
        raise AssertionError("rank localizer mutation accepted")

    print("KB_C2_112_FIXED_BALANCED_FOUR_CELL_PASS generic=4 rank_branches=8 mutations=2/2")


if __name__ == "__main__":
    main()
