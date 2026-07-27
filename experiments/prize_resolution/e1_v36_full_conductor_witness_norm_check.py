#!/usr/bin/env python3
"""Check the compact V=36 full-conductor witness norm packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "e1_v36_full_conductor_witness_norm_modal.py"
RESULT = HERE / "e1_v36_full_conductor_witness_norm_result.json"


def main() -> None:
    packet = json.loads(RESULT.read_text())
    assert packet["schema"] == "e1-v36-full-conductor-witness-norm-v1"
    assert packet["complete"] is packet["agreement"] is True
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == packet["source_sha256"]
    assert packet["coefficients"] == [
        [0, 2], [16, -2], [32, -1], [48, 1],
        [65, 1], [80, -1], [96, -2],
    ]
    norm = int(packet["norm"])
    odd_part = int(packet["odd_part"])
    valuation = int(packet["valuation"])
    assert valuation == 1 and norm == odd_part << valuation
    assert norm.bit_length() == packet["norm_bits"] == 249
    assert odd_part.bit_length() == packet["odd_part_bits"] == 248
    assert odd_part % 256 == packet["odd_part_mod_256"] == 1
    assert packet["odd_part_is_prime"] is True
    assert packet["odd_part_above_2_250"] is (odd_part > 2**250) is False
    assert packet["odd_part_below_2_256"] is (odd_part < 2**256) is True
    print("E1_V36_FULL_CONDUCTOR_WITNESS_NORM_CHECK_PASS norm_bits=249 odd_bits=248 eligible=0")


if __name__ == "__main__":
    main()
