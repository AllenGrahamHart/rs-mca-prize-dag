#!/usr/bin/env python3
"""Independent audit of the dimension-three type-population ceiling."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "780248e2f3b8498f7ccc9e5dccf23f88e4dc7d154453c3df6adb5c844cf26373"


def c2(value: int) -> int:
    return value * (value - 1) // 2


def independent_cross(q: int) -> int:
    p = c2(q) - 217 * q + c2(218)
    b = 217 * q * 67470 - c2(218) * 1048576 + c2(q)
    a = 218 * 1048576 - q * 67470
    return 2 * (p * a - b * (q - 218))


def main() -> None:
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256
    data = json.loads(CONTRACT.read_text())
    for q in range(520, 3388):
        factored = -109 * q * (q - 218) * (619 * q - 1962831)
        assert independent_cross(q) == factored
    assert independent_cross(3170) == 613022740560
    assert independent_cross(3171) == -18372095406

    q = 3170
    p = c2(q) - 217 * q + c2(218)
    b = 217 * q * 67470 - c2(218) * 1048576 + c2(q)
    a = 218 * 1048576 - q * 67470
    assert divmod(b, p) == (4959, data["endpoint_pair_lower_remainder"])
    assert divmod(a, q - 218) == (4982, data["endpoint_plane_upper_remainder"])
    assert 1048576 + 4960 - (a - (q - 218) * 4960) == \
        data["endpoint_full_owner_coordinate_floor"] == 985788
    assert 1048576 + 4982 - (a - (q - 218) * 4982) == \
        data["endpoint_upper_row_full_owner_coordinate_floor"] == 1050754
    assert (255011043 + 3169) // 3170 == data["dense_type_record_floor"] == 80446

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["rate_half_mca_rank11_pair_pencil_dimension_three_pair_overlap_moment_floor"]["status"] == "PROVED"
    proof = " ".join((HERE / "proof.md").read_text().split())
    audit = " ".join((HERE / "audit.md").read_text().lower().split())
    assert "-109q(q-218)(619q-1962831)" in proof
    assert "chronology-safe first-owner averaging" in audit
    print("RANK11_D3_TYPE_POP_AUDIT_PASS q=520..3170 dense=80446 K=4960..4982 full=985788")


if __name__ == "__main__":
    main()
