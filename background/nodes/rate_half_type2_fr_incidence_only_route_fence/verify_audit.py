#!/usr/bin/env python3
"""Independent membership-direction replay of the FR incidence witness."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "experiments/prize_resolution/rh_type2_fr_incidence_m64_result.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    data = json.loads(RESULT.read_text())
    m = 64
    q = 257
    reps = [1, 3, 9, 27]
    inverses = [pow(rep, -1, q) for rep in reps]
    quartics = {x for x in range(1, q) if pow(x, m, q) == 1}
    require(len(quartics) == m, "quartic-power subgroup")

    raw = bytes.fromhex(data["W_bitset_hex_little_endian"])
    require(len(raw) == 128, "certificate byte length")
    require(hashlib.sha256(raw).hexdigest() == data["W_sha256"], "certificate digest")
    mask = int.from_bytes(raw, "little")

    def in_w(i: int, x: int) -> bool:
        return bool((mask >> (i * 256 + x - 1)) & 1)

    def in_block(gamma: int, i: int, x: int) -> bool:
        if gamma == 0 and i == 0 and x == 1:
            return False
        difference = (x - gamma) % q
        return difference != 0 and difference * inverses[i] % q in quartics

    sizes = []
    intersections = []
    spends = []
    degrees = [0] * 1024
    rows: list[int] = []
    for gamma in range(q):
        row = 0
        meet = 0
        for i in range(4):
            for x in range(1, q):
                if not in_block(gamma, i, x):
                    continue
                index = i * 256 + x - 1
                row |= 1 << index
                degrees[index] += 1
                meet += int(in_w(i, x))
        rows.append(row)
        size = row.bit_count()
        sizes.append(size)
        intersections.append(meet)
        spends.append(size - meet)

    w_size = mask.bit_count()
    min_union = min((rows[g] | rows[h]).bit_count() for g in range(q) for h in range(g + 1, q))
    require(set(sizes) == {255}, "row sizes")
    require(sorted(degrees) == [63] + [64] * 1023, "independent degree profile")
    require(sum(64 - degree for degree in degrees) == 1, "independent deficit")
    require(w_size == 447, "independent W size")
    require(min_union == 447, "independent pair union")
    require(min(spends) == 66, "independent spend")
    require(max(intersections) == 189 and intersections.index(189) == 0, "independent maximum")
    require(max(intersections) > 2 * m and max(intersections) - 2 * m == 61, "independent violation")

    # Two hostile mutations must fail fixed certificate gates.
    require((mask ^ 1).bit_count() != w_size, "single-bit mutation escaped size gate")
    require(hashlib.sha256((int.from_bytes(raw, "little") ^ 1).to_bytes(128, "little")).hexdigest() != data["W_sha256"], "digest mutation")

    print(
        "RH_TYPE2_FR_INCIDENCE_ROUTE_FENCE_AUDIT_PASS "
        f"rows={len(rows)} points={len(degrees)} min_union={min_union} "
        f"min_spend={min(spends)} max_meet={max(intersections)} gap=61"
    )


if __name__ == "__main__":
    main()
