#!/usr/bin/env python3
"""Pack exact cell-5 guard-power matrix coefficients into a compact binary file."""

import argparse
import hashlib
import json
import struct
from pathlib import Path


DIRECTORY = Path(__file__).parent
SOURCE = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_matrix_coefficients_result.json"
)
OUTPUT = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_matrix_coefficients.bin"
)
METADATA = DIRECTORY / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_matrix_coefficients_meta.json"
)
BASIS_SHA256 = "8fd93095924f616770e49257ae45f255a8859f43c4f87100859cadfc8cc77ed6"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, action="append")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--metadata", type=Path, default=METADATA)
    parser.add_argument("--power", type=int, default=1)
    return parser.parse_args()


def main():
    args = parse_args()
    if not 1 <= args.power <= 99:
        raise RuntimeError("power must lie in 1..99")
    sources = args.source or [SOURCE]
    shards = [item for source in sources for item in json.loads(source.read_text())]
    complete = [item for item in shards if item["status"] == "COMPLETE"]
    if any(item["basis_sha256"] != BASIS_SHA256 for item in complete):
        raise RuntimeError("coefficient shard basis hash mismatch")
    if any(item.get("guard_power", 1) != args.power for item in complete):
        raise RuntimeError("coefficient shard guard-power mismatch")
    covered = {
        column
        for item in complete
        for column in range(item["start"], item["stop"] + 1)
    }
    if covered != set(range(1, 65)):
        raise RuntimeError("coefficient shard coverage is incomplete")
    raw_entries = [
        item for shard in complete for item in shard["matrix_entries"]
    ]
    entries = {
        (item["row"], item["column"]): (
            item["numerator"],
            item["denominator"],
        )
        for item in raw_entries
    }
    if len(entries) != len(raw_entries):
        raise RuntimeError("duplicate matrix entry")
    if sorted({column for _, column in entries}) != list(range(1, 65)):
        raise RuntimeError("matrix columns do not cover 1..64")
    canonical = "\n".join(
        f"{row},{column}:{','.join(map(str, numerator))}/"
        f"{','.join(map(str, denominator))}"
        for (row, column), (numerator, denominator) in sorted(entries.items())
    )
    coefficients_sha256 = hashlib.sha256(canonical.encode()).hexdigest()

    packet = bytearray(f"KBC5M{args.power:02d}\n".encode())
    packet.extend(struct.pack("<I", len(entries)))
    packet.extend(bytes.fromhex(BASIS_SHA256))
    packet.extend(bytes.fromhex(coefficients_sha256))
    max_numerator_length = 0
    max_denominator_length = 0
    for (row, column), (numerator, denominator) in sorted(entries.items()):
        if not 1 <= row <= 64 or not 1 <= column <= 64:
            raise RuntimeError("matrix index outside 1..64")
        if not numerator or not denominator:
            raise RuntimeError("empty coefficient vector")
        if len(numerator) > 65535 or len(denominator) > 65535:
            raise RuntimeError("coefficient vector exceeds packet format")
        if any(not 0 <= value < 2130706433 for value in numerator + denominator):
            raise RuntimeError("coefficient outside deployed field")
        packet.extend(
            struct.pack("<BBHH", row, column, len(numerator), len(denominator))
        )
        packet.extend(struct.pack(f"<{len(numerator)}I", *numerator))
        packet.extend(struct.pack(f"<{len(denominator)}I", *denominator))
        max_numerator_length = max(max_numerator_length, len(numerator))
        max_denominator_length = max(max_denominator_length, len(denominator))
    args.output.write_bytes(packet)
    metadata = {
        "schema": "rate-half-kb-positive-433-1a-cell5-guard-power-matrix-v1",
        "guard_power": args.power,
        "basis_sha256": BASIS_SHA256,
        "coefficients_sha256": coefficients_sha256,
        "packet_sha256": hashlib.sha256(packet).hexdigest(),
        "packet_bytes": len(packet),
        "matrix_dimension": 64,
        "matrix_nonzero_entries": len(entries),
        "column_coverage": 64,
        "max_numerator_length": max_numerator_length,
        "max_denominator_length": max_denominator_length,
    }
    args.metadata.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_GUARD_MATRIX_PACK_PASS "
        f"entries={len(entries)} bytes={len(packet)} "
        f"sha256={metadata['packet_sha256']}"
    )


if __name__ == "__main__":
    main()
