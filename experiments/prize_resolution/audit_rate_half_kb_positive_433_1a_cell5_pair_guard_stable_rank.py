#!/usr/bin/env python3
"""Hostile mutations for the independent cell-5 guard stable-rank checker."""

import copy
import hashlib
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_rate_half_kb_positive_433_1a_cell5_pair_guard_stable_rank as checker


def rejected(action, label):
    try:
        action()
    except (checker.CertificateError, KeyError, ValueError):
        return
    raise RuntimeError(f"hostile mutation accepted: {label}")


(
    metadata,
    square_entries,
    _,
    _,
    data,
    coordinates,
    _,
    cleared,
) = checker.load_certificate()
pivots_hash = hashlib.sha256(checker.SQUARE_PIVOTS.read_bytes()).hexdigest()

dropped = copy.deepcopy(data)
dropped.pop()
rejected(
    lambda: checker.collect_coordinates(dropped, metadata, pivots_hash),
    "dropped shard",
)

mutated_coordinates = dict(coordinates)
numerator, denominator = mutated_coordinates[(1, 25)]
changed = list(numerator)
changed[0] = (changed[0] + 1) % checker.PRIME
mutated_coordinates[(1, 25)] = (tuple(changed), denominator)
rejected(
    lambda: checker.exact_factorization(
        square_entries, mutated_coordinates, cleared, [25]
    ),
    "changed exact coordinate",
)

raw = bytearray(checker.SQUARE_PACKET.read_bytes())
raw[-1] ^= 1
with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "mutated.bin"
    path.write_bytes(raw)
    rejected(
        lambda: checker.read_packet(path, checker.SQUARE_METADATA, 2),
        "flipped packet byte",
    )

print(
    "RATE_HALF_KB_POSITIVE_433_1A_CELL5_GUARD_STABLE_RANK_MUTATION_PASS "
    "rejected=dropped_shard,changed_coordinate,flipped_packet_byte"
)
