#!/usr/bin/env python3
"""Memory-controlled exact replay of the M720 large h=3 gate rows."""

from __future__ import annotations

import itertools


def mu_n_generator(p: int, n: int) -> int:
    assert (p - 1) % n == 0
    e = (p - 1) // n
    a = 2
    while True:
        z = pow(a, e, p)
        if pow(z, n // 2, p) != 1:
            return z
        a += 1


def h3_census(n: int, p: int) -> dict[str, int]:
    z = mu_n_generator(p, n)
    powers = [pow(z, a, p) for a in range(n)]

    payload_bits = 41
    payload_mask = (1 << payload_bits) - 1
    records: list[int] = []
    for i, j, k in itertools.combinations(range(n), 3):
        x, y, w = powers[i], powers[j], powers[k]
        e1 = (x + y + w) % p
        e2 = (x * y + x * w + y * w) % p
        e3 = (x * y * w) % p
        key = e1 * p + e2
        payload = (e3 << 24) | (i << 16) | (j << 8) | k
        records.append((key << payload_bits) | payload)

    records.sort()
    unordered = 0
    anchored_cores = set()
    pos = 0
    while pos < len(records):
        end = pos + 1
        key = records[pos] >> payload_bits
        while end < len(records) and (records[end] >> payload_bits) == key:
            end += 1

        if end - pos > 1:
            bucket = []
            for rec in records[pos:end]:
                payload = rec & payload_mask
                e3 = payload >> 24
                i = (payload >> 16) & 0xFF
                j = (payload >> 8) & 0xFF
                k = payload & 0xFF
                mask = (1 << i) | (1 << j) | (1 << k)
                bucket.append((mask, e3, (i, j, k)))

            for a, (mask_a, e3_a, triple_a) in enumerate(bucket):
                for mask_b, e3_b, triple_b in bucket[a + 1:]:
                    if mask_a & mask_b:
                        continue
                    if e3_a == e3_b:
                        continue
                    unordered += 1
                    if triple_a[0] == 0:
                        anchored_cores.add(triple_a)
                    if triple_b[0] == 0:
                        anchored_cores.add(triple_b)

        pos = end

    return {
        "unordered_trades": unordered,
        "toral": 0,
        "nontoral": unordered,
        "anchored_cores": len(anchored_cores),
    }


def main() -> None:
    rows = [
        (128, 17921, {"unordered_trades": 384, "toral": 0, "nontoral": 384, "anchored_cores": 18}),
        (256, 65537, {"unordered_trades": 5504, "toral": 0, "nontoral": 5504, "anchored_cores": 129}),
    ]
    for n, p, expected in rows:
        got = h3_census(n, p)
        assert got == expected, (n, p, got, expected)
        print(f"full_census({n},3,{p}) = {got}")
    print("M720 large h=3 gate replay PASS")


if __name__ == "__main__":
    main()
