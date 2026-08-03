#!/usr/bin/env python3
"""Audit the complete fixed-a favorable-chain cell-14 exclusion ledger."""

import base64
import hashlib
import itertools
import json
from pathlib import Path
import zlib


DIRECTORY = Path(__file__).parent
COMPILER = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_flint_profile_modal.py"
LEDGER = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_flint_profile_result.json"
REPLAY_SCRIPT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_root_replay_modal.py"
REPLAY = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_root_replay_result.json"
CURVE = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_curve_kernel_result.json"
RESULT = DIRECTORY / "rate_half_kb_positive_433_1b_cell14_fixed_a_rankone_census_result.json"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ledger = json.loads(LEDGER.read_text())
    replay = json.loads(REPLAY.read_text())
    assert ledger["schema"] == (
        "rate-half-kb-positive-433-1b-cell14-fixed-a-rankone-flint-v1"
    )
    assert ledger["mode"] == "chain"
    assert ledger["source_script_sha256"] == sha256(COMPILER)
    assert ledger["source_curve_sha256"] == sha256(CURVE)
    assert replay["schema"] == (
        "rate-half-kb-positive-433-1b-cell14-fixed-a-root-replay-v1"
    )
    assert replay["status"] == "COMPLETE"
    assert replay["source_sha256"] == sha256(LEDGER)
    assert replay["source_script_sha256"] == sha256(REPLAY_SCRIPT)

    signs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    favorable = (3, 4, 5, 9, 10, 11, 12, 13, 14)
    expected = {
        (source, lane, xi_index, pairing_index)
        for source, lane in itertools.product(signs, repeat=2)
        for xi_index in range(3)
        for pairing_index in favorable
    }
    actual = {
        (
            tuple(row["epsilon"]), tuple(row["sigma"]),
            row["xi_index"], row["pairing_index"],
        )
        for row in ledger["rows"]
    }
    assert actual == expected
    assert len(actual) == len(ledger["rows"]) == ledger["case_count"] == 432
    assert ledger["unit_count"] == 432

    root_count = 0
    guard_boundaries = 0
    checked_roots = 0
    direct_fibers = 0
    target_boundaries = 0
    eliminant_bytes = 0
    maximum_degree = 0
    for row in ledger["rows"]:
        assert row["status"] == "CHAIN_COMPLETE"
        assert row["unit"] and row["case_excluded"]
        assert not row["unresolved_roots"]
        assert row["field_roots"] == [
            root["r"] for root in row["field_root_rows"]
        ]
        text = zlib.decompress(
            base64.b64decode(row["outer_zlib_base64"])
        ).decode()
        assert hashlib.sha256(text.encode()).hexdigest() == row["outer_sha256"]
        eliminant_bytes += len(text)
        maximum_degree = max(maximum_degree, row["outer_degrees"][2])
        root_count += len(row["field_roots"])
        for root in row["field_root_rows"]:
            if root["status"] == "GUARD_BOUNDARY":
                assert root["zero_guards"] or root["denominator_guards"]
                guard_boundaries += 1
                continue
            assert root["status"] == "CHECKED"
            assert not root["clearing_boundaries"]
            checked_roots += 1
            for item in root["direct_rows"]:
                direct = item["direct"]
                assert direct["status"] == "CHECKED"
                assert not direct["solutions"]
                direct_fibers += 1
                target_boundaries += len(direct.get("target_boundaries", []))
                target_boundaries += bool(direct.get("target_boundary"))

    assert root_count == replay["root_count"] == 9456
    assert replay["case_count"] == 432
    assert replay["shard_count"] == len(replay["shards"]) == 8
    assert all(row["status"] == "COMPLETE" for row in replay["shards"])
    assert sum(row["case_count"] for row in replay["shards"]) == 432
    assert sum(row["root_count"] for row in replay["shards"]) == 9456
    assert guard_boundaries == 5248
    assert checked_roots == 4208
    assert direct_fibers == 8736
    assert target_boundaries == 480
    assert eliminant_bytes == 84729848
    assert maximum_degree == 15680

    output = {
        "schema": "rate-half-kb-positive-433-1b-cell14-fixed-a-census-v1",
        "status": "PASS",
        "compiler_sha256": sha256(COMPILER),
        "ledger_sha256": sha256(LEDGER),
        "replay_script_sha256": sha256(REPLAY_SCRIPT),
        "replay_sha256": sha256(REPLAY),
        "curve_sha256": sha256(CURVE),
        "case_count": 432,
        "remaining_allmixed_case_count": 144,
        "root_count": root_count,
        "guard_boundary_count": guard_boundaries,
        "checked_root_count": checked_roots,
        "direct_fiber_count": direct_fibers,
        "target_boundary_count": target_boundaries,
        "maximum_eliminant_degree": maximum_degree,
        "decompressed_eliminant_bytes": eliminant_bytes,
    }
    RESULT.write_text(json.dumps(output, indent=2, sort_keys=True)+"\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
