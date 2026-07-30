#!/usr/bin/env python3
"""Exact genus-zero class budget for the surviving KoalaBear m=4 outer map."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter


LETTERS = tuple(range(6))
PAIRS = tuple(itertools.combinations(LETTERS, 2))
PAIR_INDEX = {pair: i for i, pair in enumerate(PAIRS)}


def cycle_type(perm: tuple[int, ...]) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(len(perm)):
        if start in seen:
            continue
        point = start
        length = 0
        while point not in seen:
            seen.add(point)
            point = perm[point]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def on_pairs(perm: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        PAIR_INDEX[tuple(sorted((perm[left], perm[right])))]
        for left, right in PAIRS
    )


def is_even(letter_type: tuple[int, ...]) -> bool:
    return (6 - len(letter_type)) % 2 == 0


def label(letter_type: tuple[int, ...]) -> str:
    return ".".join(map(str, letter_type))


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[point]] for point in LETTERS)


def inverse(perm: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(perm)
    for point, image in enumerate(perm):
        result[image] = point
    return tuple(result)


def generated_order(generators: tuple[tuple[int, ...], ...]) -> int:
    identity = LETTERS
    steps = generators + tuple(inverse(generator) for generator in generators)
    group = {identity}
    queue = [identity]
    while queue:
        current = queue.pop()
        for step in steps:
            candidate = compose(current, step)
            if candidate not in group:
                group.add(candidate)
                queue.append(candidate)
    return len(group)


def class_table() -> list[dict[str, object]]:
    classes: dict[tuple[int, ...], dict[str, object]] = {}
    for perm in itertools.permutations(LETTERS):
        letter_type = cycle_type(perm)
        pair_type = cycle_type(on_pairs(perm))
        if letter_type in classes:
            assert classes[letter_type]["pair_cycle_type"] == pair_type
            classes[letter_type]["class_size"] += 1
            continue
        classes[letter_type] = {
            "letter_cycle_type": letter_type,
            "pair_cycle_type": pair_type,
            "pair_index": 15 - len(pair_type),
            "letter_parity": "even" if is_even(letter_type) else "odd",
            "class_size": 1,
        }
    table = sorted(classes.values(), key=lambda row: row["letter_cycle_type"])
    assert len(table) == 11
    assert sum(int(row["class_size"]) for row in table) == 720
    return table


def residual_passports(table: list[dict[str, object]]) -> list[dict[str, object]]:
    nonidentity = [row for row in table if int(row["pair_index"]) > 0]
    passports: list[dict[str, object]] = []

    def visit(start: int, budget: int, chosen: list[dict[str, object]]) -> None:
        if budget == 0:
            odd_count = sum(row["letter_parity"] == "odd" for row in chosen)
            if odd_count % 2:
                return
            passports.append(
                {
                    "residual_classes": [
                        label(tuple(row["letter_cycle_type"])) for row in chosen
                    ],
                    "residual_indices": [int(row["pair_index"]) for row in chosen],
                    "odd_class_count": odd_count,
                    "ambient_candidates": ["A6"] if odd_count == 0 else ["S6"],
                }
            )
            return
        for index in range(start, len(nonidentity)):
            row = nonidentity[index]
            cost = int(row["pair_index"])
            if cost <= budget:
                visit(index, budget - cost, chosen + [row])

    visit(0, 16, [])
    return passports


def tuple_audit(passports: list[dict[str, object]]) -> list[dict[str, object]]:
    permutations = tuple(itertools.permutations(LETTERS))
    by_label: dict[str, tuple[tuple[int, ...], ...]] = {}
    for perm in permutations:
        by_label.setdefault(label(cycle_type(perm)), tuple())
        by_label[label(cycle_type(perm))] += (perm,)

    pole_5a = (1, 2, 3, 4, 0, 5)
    pole_5b = compose(pole_5a, pole_5a)
    assert cycle_type(pole_5a) == cycle_type(pole_5b) == (5, 1)
    identity = LETTERS
    audits: list[dict[str, object]] = []
    order_cache: dict[tuple[tuple[int, ...], ...], int] = {}

    for passport in passports:
        classes = list(passport["residual_classes"])
        prefix_classes = [by_label[class_name] for class_name in classes[:-1]]
        final_label = classes[-1]
        target_order = 360 if passport["ambient_candidates"] == ["A6"] else 720
        poles = [("5A", pole_5a)]
        if target_order == 360:
            poles.append(("5B", pole_5b))
        pole_audits: list[dict[str, object]] = []
        for pole_name, pole in poles:
            product_one = 0
            generated_orders: Counter[int] = Counter()
            for prefix in itertools.product(*prefix_classes):
                product = pole
                for branch_cycle in prefix:
                    product = compose(product, branch_cycle)
                final = inverse(product)
                if label(cycle_type(final)) != final_label:
                    continue
                assert compose(product, final) == identity
                product_one += 1
                generators = (pole,) + prefix + (final,)
                cache_key = tuple(sorted(generators))
                order = order_cache.get(cache_key)
                if order is None:
                    order = generated_order(generators)
                    order_cache[cache_key] = order
                generated_orders[order] += 1
            pole_audits.append(
                {
                    "pole_class": pole_name,
                    "product_one_tuple_count": product_one,
                    "generated_order_counts": {
                        str(order): count
                        for order, count in sorted(generated_orders.items())
                    },
                    "generating_tuple_count": generated_orders[target_order],
                }
            )
        audits.append(
            {
                "residual_classes": classes,
                "target_order": target_order,
                "pole_class_audits": pole_audits,
                "realized": any(row["generating_tuple_count"] > 0 for row in pole_audits),
            }
        )
    return audits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    table = class_table()
    pole = next(row for row in table if row["letter_cycle_type"] == (5, 1))
    assert pole["pair_cycle_type"] == (5, 5, 5)
    assert pole["pair_index"] == 12

    passports = residual_passports(table)
    audits = tuple_audit(passports)
    payload = {
        "degree": 15,
        "genus_zero_total_index": 28,
        "mandatory_pole_letter_type": "5.1",
        "mandatory_pole_pair_type": [5, 5, 5],
        "mandatory_pole_index": 12,
        "residual_index_budget": 16,
        "class_table": table,
        "necessary_passports": passports,
        "passport_count": len(passports),
        "tuple_audit": audits,
        "realized_passport_count": sum(row["realized"] for row in audits),
        "ambient_counts": dict(
            sorted(
                Counter(row["ambient_candidates"][0] for row in passports).items()
            )
        ),
        "scope": "geometric passport existence only; field descent and source-star incidence remain unchecked",
    }
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return

    for row in table:
        print(
            f"{label(tuple(row['letter_cycle_type'])):11} "
            f"size={row['class_size']:3} parity={row['letter_parity']:4} "
            f"pairs={label(tuple(row['pair_cycle_type'])):20} "
            f"index={row['pair_index']:2}"
        )
    print(f"passports={len(passports)} ambient={payload['ambient_counts']}")
    for row in passports:
        print(
            f"{row['ambient_candidates'][0]} "
            f"classes={','.join(row['residual_classes'])} "
            f"indices={row['residual_indices']}"
        )
    for row in audits:
        for pole_audit in row["pole_class_audits"]:
            print(
                f"tuple classes={','.join(row['residual_classes'])} "
                f"pole={pole_audit['pole_class']} "
                f"product_one={pole_audit['product_one_tuple_count']} "
                f"orders={pole_audit['generated_order_counts']} "
                f"target={row['target_order']} "
                f"generating={pole_audit['generating_tuple_count']}"
            )


if __name__ == "__main__":
    main()
