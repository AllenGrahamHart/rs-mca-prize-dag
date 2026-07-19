#!/usr/bin/env python3
"""Audit the bounded prime-field active-partition packet checker."""

import copy
import json
from pathlib import Path

from check_packet import PacketError, check_packet


HERE = Path(__file__).resolve().parent


def must_fail(packet, fragment):
    try:
        check_packet(packet)
    except PacketError as exc:
        assert fragment in str(exc), (fragment, str(exc))
        return
    raise AssertionError(f"mutation unexpectedly passed: {fragment}")


def main():
    packet = json.loads((HERE / "toy_packet.json").read_text())
    result = check_packet(packet)
    assert result["status"] == "PASS"
    assert result["clean_slopes"] == 3
    assert result["saturated_rows"] == 9
    assert result["nonincidence_edges"] == 18
    assert result["rs_checks"] == 4
    assert result["separation_rank"] == 2
    assert len(set(result["ranks"].values())) == 1

    incidence = copy.deepcopy(packet)
    incidence["saturated_fibers"][0]["roots"] = [8]
    must_fail(incidence, "incidence mismatch")

    cycle = copy.deepcopy(packet)
    cycle["clean_fibers"][0]["roots"][0] = 4
    cycle["saturated_fibers"][0]["roots"] = [50]
    must_fail(cycle, "cycle mismatch")

    bad_rank = copy.deepcopy(packet)
    bad_rank["expected_separation_rank"] = 3
    must_fail(bad_rank, "expected separation rank")

    print(
        "RATE_HALF_CA_HANKEL_A1_CORE_ONE_ACTIVE_PARTITION_"
        "PACKET_CHECKER_PASS toy=X3-t mutations=3"
    )


if __name__ == "__main__":
    main()
