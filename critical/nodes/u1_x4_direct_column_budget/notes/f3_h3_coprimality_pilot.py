#!/usr/bin/env python3
"""Terminal C light pilot for h=3 pair-coprimality.

This is intentionally local and exact.  It enumerates the activated non-toral
shape orbits in the banked n=96 prime ladder, then checks whether any activated
shape also activates at another prime in the same ladder.  A repeated activation
would falsify the strongest naive pair-coprimality heuristic immediately.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass

from f3_h3_char0_classification import (
    e1_terms,
    e2_terms,
    eval_mod_prime,
    is_zero_residue,
    primitive_root_mod_prime,
)


N = 96
QS = (9601, 13249, 18433, 26113, 36097, 42337, 46273)


@dataclass(frozen=True)
class Shape:
    a: tuple[int, int, int]
    b: tuple[int, int, int]

    def flat(self) -> tuple[int, ...]:
        return self.a + self.b


def canonical_shape(a: tuple[int, int, int], b: tuple[int, int, int]) -> Shape:
    best: Shape | None = None
    for shift in range(N):
        ar = tuple(sorted((x - shift) % N for x in a))
        br = tuple(sorted((x - shift) % N for x in b))
        for left, right in ((ar, br), (br, ar)):
            if left[0] != 0:
                continue
            candidate = Shape(left, right)
            if best is None or candidate.flat() < best.flat():
                best = candidate
    if best is None:
        raise AssertionError((a, b))
    return best


def is_toral(triple: tuple[int, int, int]) -> bool:
    step = N // 3
    return all(x % step == triple[0] % step for x in triple)


def shapes_at_prime(q: int) -> set[Shape]:
    zeta = primitive_root_mod_prime(q, N)
    domain = [pow(zeta, i, q) for i in range(N)]
    buckets: dict[tuple[int, int], list[tuple[int, int, int]]] = {}
    for triple in itertools.combinations(range(N), 3):
        x0, x1, x2 = (domain[i] for i in triple)
        sig = ((x0 + x1 + x2) % q, (x0 * x1 + x0 * x2 + x1 * x2) % q)
        buckets.setdefault(sig, []).append(triple)

    shapes: set[Shape] = set()
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
                shapes.add(canonical_shape(left, right))
    return shapes


def activates(shape: Shape, q: int) -> bool:
    zeta = primitive_root_mod_prime(q, N)
    return (
        eval_mod_prime(q, zeta, e1_terms(shape.a, shape.b)) == 0
        and eval_mod_prime(q, zeta, e2_terms(shape.a, shape.b)) == 0
    )


def main() -> None:
    by_prime = {q: shapes_at_prime(q) for q in QS}
    shape_sources: dict[Shape, list[int]] = {}
    for q, shapes in by_prime.items():
        for shape in shapes:
            shape_sources.setdefault(shape, []).append(q)

    print("Activated n=96 h=3 non-toral shapes by prime:")
    for q in QS:
        print(f"  q={q}: shapes={len(by_prime[q])}")
        for shape in sorted(by_prime[q], key=lambda s: s.flat()):
            print(f"    {list(shape.a)} | {list(shape.b)}")

    repeated_sources = {s: qs for s, qs in shape_sources.items() if len(qs) > 1}
    if repeated_sources:
        raise AssertionError(
            "same canonical shape appeared at multiple primes: "
            + repr({s.flat(): qs for s, qs in repeated_sources.items()})
        )

    cross_activations: dict[tuple[int, ...], list[int]] = {}
    for shape in shape_sources:
        # The char-zero theorem says a non-toral shape cannot have both
        # obstructions zero in Q(zeta_N).  Recheck here so a bad normalization
        # cannot pollute the coprimality pilot.
        if is_zero_residue(N, e1_terms(shape.a, shape.b)) and is_zero_residue(
            N, e2_terms(shape.a, shape.b)
        ):
            raise AssertionError(f"non-toral shape is char-zero zero: {shape}")
        hits = [q for q in QS if activates(shape, q)]
        cross_activations[shape.flat()] = hits
        if len(hits) != 1:
            raise AssertionError((shape, hits))

    print("Cross-prime activation check:")
    for flat, hits in sorted(cross_activations.items()):
        print(f"  {list(flat)} -> {hits}")
    print("H3_PAIR_COPRIMALITY_PILOT_PASS")


if __name__ == "__main__":
    main()
