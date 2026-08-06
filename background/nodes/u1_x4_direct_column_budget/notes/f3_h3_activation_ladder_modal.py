#!/usr/bin/env python3
"""Modal activation ladder for Terminal C h=3 common-root coprimality."""

from __future__ import annotations

import modal


app = modal.App("rs-mca-h3-activation-ladder")
image = modal.Image.debian_slim()

N = 96
N_PRIMES = 64
CHUNK = 8


def is_prime(m: int) -> bool:
    if m < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for a in small:
        if m % a == 0:
            return m == a
    d, r = m - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in small:
        if a >= m:
            continue
        x = pow(a, d, m)
        if x in (1, m - 1):
            continue
        for _ in range(r - 1):
            x = x * x % m
            if x == m - 1:
                break
        else:
            return False
    return True


def prime_ladder() -> list[int]:
    out = []
    q = (N * N // N) * N + 1
    while len(out) < N_PRIMES:
        if q > N * N and is_prime(q):
            out.append(q)
        q += N
    return out


@app.function(image=image, cpu=2, memory=2048, timeout=60)
def scan_chunk(primes: list[int]) -> list[dict]:
    import itertools

    def primitive_root(q: int) -> int:
        for cand in range(2, q):
            z = pow(cand, (q - 1) // N, q)
            if z == 1:
                continue
            y, order = z, 1
            while y != 1 and order <= N:
                y = y * z % q
                order += 1
            if order == N:
                return z
        raise RuntimeError(f"no primitive root for {q}")

    def canonical(a, b):
        best = None
        for shift in range(N):
            ar = tuple(sorted((u - shift) % N for u in a))
            br = tuple(sorted((u - shift) % N for u in b))
            for left, right in ((ar, br), (br, ar)):
                if left[0] != 0:
                    continue
                cand = left + right
                if best is None or cand < best:
                    best = cand
        return best

    def is_toral(triple):
        step = N // 3
        return all(u % step == triple[0] % step for u in triple)

    rows = []
    triples = list(itertools.combinations(range(N), 3))
    for q in primes:
        zeta = primitive_root(q)
        domain = [pow(zeta, i, q) for i in range(N)]
        buckets = {}
        for triple in triples:
            x0, x1, x2 = (domain[i] for i in triple)
            sig = ((x0 + x1 + x2) % q, (x0 * x1 + x0 * x2 + x1 * x2) % q)
            buckets.setdefault(sig, []).append(triple)

        shapes = set()
        trades = 0
        for members in buckets.values():
            if len(members) < 2:
                continue
            for i, left in enumerate(members):
                lset = set(left)
                for right in members[i + 1 :]:
                    if lset & set(right):
                        continue
                    if is_toral(left) and is_toral(right):
                        continue
                    trades += 1
                    shapes.add(canonical(left, right))
        rows.append(
            {
                "q": q,
                "trades": trades,
                "shape_count": len(shapes),
                "shapes": [list(s) for s in sorted(shapes)],
            }
        )
    return rows


@app.local_entrypoint()
def main():
    primes = prime_ladder()
    chunks = [primes[i : i + CHUNK] for i in range(0, len(primes), CHUNK)]
    rows = []
    for item in scan_chunk.map(chunks, return_exceptions=True):
        if isinstance(item, Exception):
            print(f"SHARD_ERROR {item!r}")
            continue
        for row in item:
            rows.append(row)
            print(f"q={row['q']} trades={row['trades']} shapes={row['shape_count']}")

    owners = {}
    for row in rows:
        for shape in row["shapes"]:
            owners.setdefault(tuple(shape), []).append(row["q"])
    repeats = {shape: qs for shape, qs in owners.items() if len(qs) > 1}
    print(
        f"TOTAL primes={len(rows)} activated_shapes={sum(r['shape_count'] for r in rows)} "
        f"distinct_shapes={len(owners)} repeats={len(repeats)}"
    )
    for shape, qs in sorted(repeats.items())[:10]:
        print(f"REPEAT {list(shape)} -> {qs}")
    if not repeats:
        print("H3_ACTIVATION_LADDER_PASS")


if __name__ == "__main__":
    main()
