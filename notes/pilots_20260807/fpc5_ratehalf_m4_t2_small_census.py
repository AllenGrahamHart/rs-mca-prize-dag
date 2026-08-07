#!/usr/bin/env python3
"""Exact small-row census of the sharp rate-half M=4,t=2 cell."""

from __future__ import annotations

import argparse
from itertools import combinations
import json
from pathlib import Path
import random


def primitive_root(p: int) -> int:
    factors = []
    value = p - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors):
            return candidate
    raise AssertionError("no primitive root")


def add(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            + (right[index] if index < len(right) else 0)
        ) % p
    return out


def scale(poly: list[int], scalar: int, p: int) -> list[int]:
    return [scalar * coefficient % p for coefficient in poly]


def mul(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return out


def evaluate(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def locator(points: tuple[int, ...] | list[int], p: int) -> list[int]:
    out = [1]
    for point in points:
        out = mul(out, [(-point) % p, 1], p)
    return out


def lagrange_basis(points: list[int], p: int) -> list[list[int]]:
    basis = []
    for index, point in enumerate(points):
        numerator = [1]
        denominator = 1
        for other_index, other in enumerate(points):
            if other_index == index:
                continue
            numerator = mul(numerator, [(-other) % p, 1], p)
            denominator = denominator * (point - other) % p
        basis.append(scale(numerator, pow(denominator, -1, p), p))
    return basis


def interpolate(values: list[int], basis: list[list[int]], p: int) -> list[int]:
    out = [0] * len(basis)
    for value, polynomial in zip(values, basis):
        out = add(out, scale(polynomial, value, p), p)
    return out


def count_layout(
    core: list[int],
    background: list[int],
    petals: list[list[int]],
    labels: list[int],
    p: int,
) -> tuple[int, list[dict[str, int]]]:
    ell = len(petals[0])
    defect = 2 * ell - 3
    total = 0
    pair_counts = []
    for first, second in combinations(range(4), 2):
        sample = background + petals[first] + petals[second][:1]
        assert len(sample) == defect + 1
        basis = lagrange_basis(sample, p)
        split_count = primitive_count = exact_count = 0
        for missed in combinations(core, defect):
            f = locator(missed, p)
            values = [0] * len(background)
            values += [labels[first] * evaluate(f, x, p) % p for x in petals[first]]
            values += [labels[second] * evaluate(f, petals[second][0], p) % p]
            w = interpolate(values, basis, p)

            if any(
                evaluate(w, x, p) != labels[second] * evaluate(f, x, p) % p
                for x in petals[second][1:]
            ):
                continue
            split_count += 1
            if any(evaluate(w, x, p) == 0 for x in missed):
                continue
            primitive_count += 1
            untouched = set(range(4)) - {first, second}
            if any(
                evaluate(w, x, p) == labels[index] * evaluate(f, x, p) % p
                for index in untouched
                for x in petals[index]
            ):
                continue
            exact_count += 1
        pair_counts.append(
            {"split": split_count, "primitive": primitive_count, "exact": exact_count}
        )
        total += exact_count
    return total, pair_counts


def adversarial_layout(
    core: list[int],
    background: list[int],
    petals: list[list[int]],
    p: int,
) -> list[dict[str, object]]:
    """Solve the touched-label ratio instead of sampling it."""
    ell = len(petals[0])
    defect = 2 * ell - 3
    witnesses = []
    for first, second in combinations(range(4), 2):
        sample = background + petals[first] + petals[second][:1]
        basis = lagrange_basis(sample, p)
        for missed in combinations(core, defect):
            f = locator(missed, p)
            values_1 = [0] * len(background)
            values_1 += [evaluate(f, x, p) for x in petals[first]]
            values_1 += [0]
            values_2 = [0] * (len(background) + len(petals[first]))
            values_2 += [evaluate(f, petals[second][0], p)]
            w1 = interpolate(values_1, basis, p)
            w2 = interpolate(values_2, basis, p)

            rows = [
                (
                    evaluate(w1, x, p),
                    (evaluate(w2, x, p) - evaluate(f, x, p)) % p,
                )
                for x in petals[second][1:]
            ]
            nonzero = next(((a, b) for a, b in rows if a or b), None)
            if nonzero is None:
                lambdas = range(2, p)
            else:
                a, b = nonzero
                if b == 0:
                    continue
                lambdas = [(-a * pow(b, -1, p)) % p]

            for label_2 in lambdas:
                if label_2 in (0, 1):
                    continue
                if any((a + label_2 * b) % p for a, b in rows):
                    continue
                w = add(w1, scale(w2, label_2, p), p)
                if any(evaluate(w, x, p) == 0 for x in missed):
                    continue

                untouched = sorted(set(range(4)) - {first, second})
                chosen = [1, label_2]
                other_labels = []
                possible = True
                for index in untouched:
                    forbidden = {
                        evaluate(w, x, p) * pow(evaluate(f, x, p), -1, p) % p
                        for x in petals[index]
                    }
                    label = next(
                        (
                            value
                            for value in range(1, p)
                            if value not in forbidden
                            and value not in chosen
                            and value not in other_labels
                        ),
                        None,
                    )
                    if label is None:
                        possible = False
                        break
                    other_labels.append(label)
                if not possible:
                    continue

                labels = [0] * 4
                labels[first], labels[second] = 1, label_2
                for index, label in zip(untouched, other_labels):
                    labels[index] = label
                witnesses.append(
                    {
                        "pair": [first, second],
                        "missed": list(missed),
                        "labels": labels,
                        "f": f,
                        "w": w,
                    }
                )
                break
    return witnesses


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--layouts", type=int, default=50)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--adversarial", action="store_true")
    parser.add_argument("--summary-only", action="store_true")
    args = parser.parse_args()

    p, n, ell = 97, 32, 4
    k, background_size, defect = 5 * ell - 4, ell - 3, 2 * ell - 3
    generator = primitive_root(p)
    step = (p - 1) // n
    domain = [pow(generator, step * exponent, p) for exponent in range(n)]
    assert len(set(domain)) == n
    assert k + 1 == 4 * ell + background_size

    records = []
    for seed in range(args.layouts):
        points = domain[:]
        if seed:
            random.Random(seed).shuffle(points)
        core = points[: k - 1]
        background = points[k - 1 : k - 1 + background_size]
        tail = points[k - 1 + background_size :]
        petals = [tail[index * ell : (index + 1) * ell] for index in range(4)]
        if args.adversarial:
            witnesses = adversarial_layout(core, background, petals, p)
            records.append(
                {
                    "seed": seed,
                    "total": len(witnesses),
                    "witnesses": witnesses,
                }
            )
        else:
            label_rng = random.Random(10_000 + seed)
            labels = label_rng.sample(range(1, p), 4)
            total, pair_counts = count_layout(core, background, petals, labels, p)
            records.append(
                {"seed": seed, "labels": labels, "total": total, "pairs": pair_counts}
            )

    result = {
        "field": p,
        "n": n,
        "k": k,
        "ell": ell,
        "background": background_size,
        "defect": defect,
        "layouts": args.layouts,
        "nonempty_layouts": sum(record["total"] > 0 for record in records),
        "total_contributors": sum(record["total"] for record in records),
        "mode": "adversarial-label" if args.adversarial else "sampled-label",
        "maximum_layout": max(record["total"] for record in records),
        "records": records,
    }
    if not args.adversarial:
        result["split_locators"] = sum(
            pair["split"] for record in records for pair in record["pairs"]
        )
        result["primitive_locators"] = sum(
            pair["primitive"] for record in records for pair in record["pairs"]
        )
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(rendered + "\n")
    print(
        "FPC5_RATEHALF_M4_T2_SMALL_CENSUS_PASS "
        f"layouts={args.layouts} nonempty={result['nonempty_layouts']} "
        f"contributors={result['total_contributors']} max={result['maximum_layout']}"
    )
    if not args.summary_only:
        print(rendered)


if __name__ == "__main__":
    main()
