#!/usr/bin/env python3
"""Pack the cell-5 cleared-denominator rank certificate."""

import hashlib
import json
import struct
from pathlib import Path


HERE = Path(__file__).parent
SOURCE = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_cleared_result.json"
)
OUTPUT = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_cleared.bin"
)
METADATA = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_cleared_meta.json"
)
SQUARE_PACKET = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_matrix_coefficients.bin"
)
FACTORIZATION = HERE / (
    "rate_half_kb_positive_433_1a_cell5_pair_guard_square_"
    "factorization_structured_result.json"
)
PRIME = 2130706433
TAGS = {"E": 1, "P": 2, "B": 3, "D": 4, "Y": 5}


def key(record):
    if record["tag"] == "E":
        return ("E", record["index"], 0)
    if record["tag"] == "D":
        return ("D", 0, record["index"])
    return (record["tag"], record["row"], record["column"])


def expected_keys():
    keys = {("E", row, 0) for row in range(1, 65)}
    keys |= {("P", row, column) for row in range(1, 65)
             for column in range(1, 25)}
    keys |= {("B", row, column) for row in range(1, 65)
             for column in range(25, 65)}
    keys |= {("D", 0, column) for column in range(25, 65)}
    keys |= {("Y", row, column) for row in range(1, 25)
             for column in range(25, 65)}
    return keys


def main():
    shards = json.loads(SOURCE.read_text())
    if len(shards) != 104 or any(item["status"] != "COMPLETE" for item in shards):
        raise RuntimeError("cleared shard coverage is incomplete")
    row_coverage = {item["index"] for item in shards if item["kind"] == "r"}
    column_coverage = {item["index"] for item in shards if item["kind"] == "c"}
    if row_coverage != set(range(1, 65)) or column_coverage != set(range(25, 65)):
        raise RuntimeError("cleared row/column coverage mismatch")
    header_keys = (
        "basis_sha256",
        "coefficients_sha256",
        "packet_sha256",
        "factorization_sha256",
    )
    headers = {
        name: {item[name] for item in shards}
        for name in header_keys
    }
    if any(len(values) != 1 for values in headers.values()):
        raise RuntimeError("cleared shard provenance mismatch")
    header = {name: next(iter(values)) for name, values in headers.items()}
    if hashlib.sha256(SQUARE_PACKET.read_bytes()).hexdigest() != header["packet_sha256"]:
        raise RuntimeError("square packet hash mismatch")
    if hashlib.sha256(FACTORIZATION.read_bytes()).hexdigest() != header[
        "factorization_sha256"
    ]:
        raise RuntimeError("factorization hash mismatch")

    records = {}
    for shard in shards:
        for record in shard["records"]:
            record_key = key(record)
            if record_key in records:
                raise RuntimeError("duplicate cleared record")
            coefficients = tuple(record["coefficients"])
            if (
                not coefficients
                or len(coefficients) > 65535
                or any(not 0 <= value < PRIME for value in coefficients)
            ):
                raise RuntimeError("invalid cleared polynomial")
            records[record_key] = coefficients
    if set(records) != expected_keys():
        raise RuntimeError("cleared record coverage mismatch")

    digest = hashlib.sha256()
    for index, ((tag, row, column), coefficients) in enumerate(sorted(records.items())):
        if index:
            digest.update(b"\n")
        digest.update(
            f"{tag},{row},{column}:{','.join(map(str, coefficients))}".encode()
        )
    cleared_sha256 = digest.hexdigest()

    packet = bytearray(b"KBC5CLR\n")
    packet.extend(struct.pack("<I", len(records)))
    packet.extend(bytes.fromhex(header["basis_sha256"]))
    packet.extend(bytes.fromhex(header["coefficients_sha256"]))
    packet.extend(bytes.fromhex(header["packet_sha256"]))
    packet.extend(bytes.fromhex(header["factorization_sha256"]))
    packet.extend(bytes.fromhex(cleared_sha256))
    max_length = 0
    for (tag, row, column), coefficients in sorted(records.items()):
        packet.extend(struct.pack("<BBBH", TAGS[tag], row, column, len(coefficients)))
        packet.extend(struct.pack(f"<{len(coefficients)}I", *coefficients))
        max_length = max(max_length, len(coefficients))
    OUTPUT.write_bytes(packet)
    metadata = {
        "schema": "rate-half-kb-positive-433-1a-cell5-guard-cleared-v1",
        **header,
        "cleared_sha256": cleared_sha256,
        "cleared_packet_sha256": hashlib.sha256(packet).hexdigest(),
        "packet_bytes": len(packet),
        "record_count": len(records),
        "max_polynomial_length": max_length,
        "ntt_prime": PRIME,
    }
    METADATA.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(
        "RATE_HALF_KB_POSITIVE_433_1A_CELL5_GUARD_CLEARED_PACK_PASS "
        f"records={len(records)} bytes={len(packet)} "
        f"sha256={metadata['cleared_packet_sha256']}"
    )


if __name__ == "__main__":
    main()
