#!/usr/bin/env python3
"""Verify the eight literal common degree-6 leading-curve exclusions."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent / (
    "rate_half_kb_m2_r4_diagonal_c2_112_aligned_positive_fixed_r02_r20_"
    "degree12_leading_branch_decomposition"
)
FILES = {
    "modal_degree12_degree6_f04_output.json":
        "b5f4f7c3dfe3de88b053f73e4c64bb6f80b05bbf9c3de19d498e3e32cbc7dbb1",
    "modal_degree12_degree6_rest_output.json":
        "416782b403c58e109256db5b97947c28cc9cdad8b58e7525cafb433caa008292",
}
CELLS = {
    f"{assignment}-{target}"
    for assignment in ("F04", "F05", "F06", "F07")
    for target in ("R02", "R20")
}
DEGREE6_HASHES = {
    "F04": "980f453afd73141b252e9bb982a85c7e0759a61d4296d3de5f3130e5e3505272",
    "F05": "68d2b371255fa281cd7ee7b717cd7ae97bf3bce699feb9f546027ddc5f328a27",
    "F06": "68d2b371255fa281cd7ee7b717cd7ae97bf3bce699feb9f546027ddc5f328a27",
    "F07": "980f453afd73141b252e9bb982a85c7e0759a61d4296d3de5f3130e5e3505272",
}
SELECTED_HASHES = {
    "F04": "5b07627ec18114d36bf3190d4cfa3bd0c5abe9ee45f76d72e10f6e3a84c2ab1b",
    "F05": "a16b5cb9613f097c828602233c052672dda16df8427ecc5d9fd57c475407c94d",
    "F06": "a16b5cb9613f097c828602233c052672dda16df8427ecc5d9fd57c475407c94d",
    "F07": "5b07627ec18114d36bf3190d4cfa3bd0c5abe9ee45f76d72e10f6e3a84c2ab1b",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def terminal_record(row: dict) -> dict:
    records = [record for record in row["records"] if record.get("phase") == "DONE"]
    require(len(records) == 1, f"DONE record count {row['cell']}")
    return records[0]


def validate(rows: list[dict]) -> None:
    require({row["cell"] for row in rows} == CELLS, "literal cell coverage")
    require(all(row["status"] == "PASS" for row in rows), "Modal status")
    for row in rows:
        done = terminal_record(row)
        assignment = row["cell"].split("-")[0]
        require(done["terminal"] == "DEGREE12_DEGREE6_EMPTY", f"terminal {row['cell']}")
        require(done["degree6_sha256"] == DEGREE6_HASHES[assignment], f"L6 hash {row['cell']}")
        require(done["selected_sha256"] == SELECTED_HASHES[assignment], f"R12 hash {row['cell']}")
        require(done["seed_basis_size"] == 8, f"seed basis {row['cell']}")
        expected_size = 46 if assignment in ("F04", "F07") else 43
        require(done["basis_size"] == expected_size, f"full basis {row['cell']}")
        require(done["dimension"] == 1 and not done["unit_ideal"], f"ideal {row['cell']}")
        require(done["localizer_nilpotence_index"] == 1, f"nilpotence {row['cell']}")
        steps = done["localizer_steps"]
        require(len(steps) == 17, f"localizer length {row['cell']}")
        require(all(not step["factor_zero"] for step in steps), f"zero factor {row['cell']}")
        require(all(not step["zero"] for step in steps[:-1]), f"early zero {row['cell']}")
        require(steps[-1]["index"] == 17 and steps[-1]["zero"], f"terminal zero {row['cell']}")


def main() -> None:
    rows = []
    for name, expected_hash in FILES.items():
        raw = (PARENT / name).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == expected_hash, f"file hash {name}")
        payload = json.loads(raw)
        require(payload["counts"]["FAIL"] == 0, f"FAIL count {name}")
        require(payload["counts"]["TIMEOUT"] == 0, f"TIMEOUT count {name}")
        require(payload["counts"]["REMOTE_ERROR"] == 0, f"REMOTE count {name}")
        rows.extend(payload["results"])

    validate(rows)

    mutation_terminal = copy.deepcopy(rows)
    terminal_record(mutation_terminal[0])["terminal"] = "DEGREE12_DEGREE6_SURVIVES"
    try:
        validate(mutation_terminal)
    except AssertionError:
        pass
    else:
        raise AssertionError("terminal mutation survived")

    mutation_localizer = copy.deepcopy(rows)
    terminal_record(mutation_localizer[0])["localizer_steps"][-1]["zero"] = False
    try:
        validate(mutation_localizer)
    except AssertionError:
        pass
    else:
        raise AssertionError("localizer mutation survived")

    print("KB_C2_112_FIXED_R02_R20_DEGREE12_DEGREE6_PASS cells=8 mutations=2/2")


if __name__ == "__main__":
    main()
