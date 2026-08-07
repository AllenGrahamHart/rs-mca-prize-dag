#!/usr/bin/env python3
"""Verify the first-64 WCL ell=1 weight-six MITM certificate."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/dli_wcl_ell1_weight6_admissible_mitm_result.json"
SOURCE = ROOT / "experiments/prize_resolution/dli_wcl_ell1_weight6_admissible_mitm.cpp"
LAUNCHER = ROOT / "experiments/prize_resolution/dli_wcl_ell1_weight6_admissible_mitm_modal.py"
PANEL = ROOT / "experiments/prize_resolution/dli_wcl_terminal_weight5_mitm_result.json"
PANEL_VERIFIER = ROOT / "background/nodes/dli_wcl_weight5_first64_mitm_exclusion/verify.py"

SOURCE_SHA256 = "861e9c5b73a97b0584b1450139441a97291cc72d6f0fd9296252bdf3199d6562"
LAUNCHER_SHA256 = "e8bdf83c037817924232a38d9ddc241cb8bca1e65da0f4abf332b4c91f8512fc"
RESULT_SHA256 = "6b61d2f270513afad9549cb990337d51aa5ec6b6f053d05082d010b8e5139d80"
PANEL_SHA256 = "7cacbc06bae852bf3bd8e7dd427af035d882bfb202c1a28c1b592dc323712c36"
PANEL_VERIFIER_SHA256 = "61a1c6cd3e57b751bb4cacae0fee19449b5eb685ec9c9806bb60a001d481eac7"

COUNT = 64
PAIR_COUNT = 129_540
TRIPLE_COUNT = 21_849_080
TOP_KEYS = {"primes", "relation_count", "rows", "schema", "status", "worker_errors"}
ROW_KEYS = {"omega", "p", "pair_count", "seconds", "seed", "status", "triples_scanned"}


class Reject(ValueError):
    pass


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integer(value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise Reject("integer field")
    return value


def certified_primes() -> list[int]:
    if digest(PANEL) != PANEL_SHA256 or digest(PANEL_VERIFIER) != PANEL_VERIFIER_SHA256:
        raise Reject("panel dependency hash")
    spec = importlib.util.spec_from_file_location("weight5_panel_verifier", PANEL_VERIFIER)
    if spec is None or spec.loader is None:
        raise Reject("panel verifier import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = module.validate(json.loads(PANEL.read_text()))
    primes = [int(row["q"]) for row in rows]
    if len(primes) != COUNT:
        raise Reject("certified panel size")
    return primes


def validate(data: object, primes: list[int]) -> list[dict[str, object]]:
    if not isinstance(data, dict) or set(data) != TOP_KEYS:
        raise Reject("top-level schema")
    if (
        data["schema"] != "dli-wcl-ell1-weight6-admissible-mitm-panel-v1"
        or data["status"] != "COMPLETE"
        or data["worker_errors"] != []
        or integer(data["relation_count"]) != 0
        or data["primes"] != primes
    ):
        raise Reject("header")
    rows = data["rows"]
    if not isinstance(rows, list) or len(rows) != COUNT:
        raise Reject("row count")

    seen: set[int] = set()
    for expected, row in zip(primes, rows):
        if not isinstance(row, dict) or set(row) != ROW_KEYS:
            raise Reject("row schema")
        p = integer(row["p"])
        seed = integer(row["seed"])
        omega = integer(row["omega"])
        seconds = row["seconds"]
        if (
            p != expected
            or p in seen
            or row["status"] != "EXHAUSTED"
            or integer(row["pair_count"]) != PAIR_COUNT
            or integer(row["triples_scanned"]) != TRIPLE_COUNT
            or not isinstance(seconds, (int, float))
            or isinstance(seconds, bool)
            or seconds < 0
            or not 2 <= seed < p
            or not 1 <= omega < p
            or pow(seed, (p - 1) // 2, p) != p - 1
            or any(pow(base, (p - 1) // 2, p) != 1 for base in range(2, seed))
            or omega != pow(seed, (p - 1) // 512, p)
            or pow(omega, 512, p) != 1
            or pow(omega, 256, p) != p - 1
        ):
            raise Reject("row payload")
        seen.add(p)
    return rows


def replay(rows: list[dict[str, object]]) -> None:
    if digest(SOURCE) != SOURCE_SHA256 or digest(LAUNCHER) != LAUNCHER_SHA256:
        raise Reject("search source hash")
    with tempfile.TemporaryDirectory() as directory:
        binary = Path(directory) / "weight6_mitm"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(SOURCE), "-o", str(binary)],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        for index in (0, COUNT // 2, COUNT - 1):
            expected = rows[index]
            process = subprocess.run(
                [str(binary), str(expected["p"])],
                check=True,
                capture_output=True,
                text=True,
                timeout=15,
            )
            replayed = json.loads(process.stdout.strip().splitlines()[-1])
            for key in ("status", "p", "seed", "omega", "pair_count", "triples_scanned"):
                if replayed.get(key) != expected[key]:
                    raise Reject(f"representative replay {index}: {key}")


def main() -> None:
    if digest(RESULT) != RESULT_SHA256:
        raise Reject("result hash")
    primes = certified_primes()
    data = json.loads(RESULT.read_text())
    rows = validate(data, primes)

    controls = []
    mutations = (
        lambda item: item["rows"].pop(),
        lambda item: item["rows"][0].__setitem__("status", "FOUND"),
        lambda item: item["rows"][0].__setitem__("triples_scanned", TRIPLE_COUNT - 1),
        lambda item: item["rows"][0].__setitem__("omega", 1),
        lambda item: item["rows"].__setitem__(1, copy.deepcopy(item["rows"][0])),
        lambda item: item.__setitem__("relation_count", 1),
    )
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            validate(altered, primes)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    if not all(controls):
        raise AssertionError(f"negative controls caught {sum(controls)}/{len(controls)}")

    replay(rows)
    print(
        "DLI_WCL_ELL1_WEIGHT6_FIRST64_PASS "
        f"rows={len(rows)} pairs={PAIR_COUNT*COUNT} triples={TRIPLE_COUNT*COUNT} "
        f"representative_replays=3 controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
