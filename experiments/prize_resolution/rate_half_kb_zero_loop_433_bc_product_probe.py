#!/usr/bin/env python3
"""Product-skeleton probe for zero-loop 433 BC-singleton common packets."""

import argparse
import importlib.util
import itertools
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_zero_loop_433_cell2_product_probe.py"
)
SPEC = importlib.util.spec_from_file_location("product_router", SCRIPT)
PRODUCT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PRODUCT)

P = PRODUCT.P
PACKETS = {
    12: (
        (1361855312, 1859271856),
        (1859271856, 1361855312),
        (271434577, 768851121),
        (768851121, 271434577),
        (33423358, 1056997377),
        (1073709056, 2097283075),
        (1056997377, 33423358),
        (2097283075, 1073709056),
    ),
    13: (
        (1061119412, 2122238824),
        (1069587021, 8467609),
        (8467609, 1069587021),
        (2122238824, 1061119412),
    ),
    14: (
        (1061119412, 8467609),
        (1069587021, 2122238824),
        (8467609, 1061119412),
        (2122238824, 1069587021),
    ),
}


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def involution(cell, b, c):
    if cell == 12:
        pairs = ((b, -b % P), (c, -c % P))
        mate = -b * c % P
        relation = ("negation", None)
    elif cell == 13:
        pairs = ((b, c), (-b % P, -c % P))
        mate = 1
        relation = ("reciprocal", b * c % P)
    elif cell == 14:
        pairs = ((b, -c % P), (-b % P, c))
        mate = P - 1
        relation = ("reciprocal", -b * c % P)
    else:
        raise RuntimeError(cell)
    common = {b, -b % P, c, -c % P, b * c % P}
    require(mate not in common, "singleton mate collision")
    if relation[0] == "negation":
        require(all(z == -y % P for y, z in pairs), "negation pairs")
    else:
        require(all(y * z % P == relation[1] for y, z in pairs),
                "reciprocal pairs")
    return mate, relation


def relation_row(left, right, relation):
    left_powers, left_coefficient = left
    right_powers, right_coefficient = right
    if relation[0] == "negation":
        row = tuple(
            right_powers[index] - left_powers[index] for index in range(3)
        )
        value = PRODUCT.extension_log(
            -left_coefficient * pow(right_coefficient, -1, P) % P
        )
    else:
        row = tuple(
            right_powers[index] + left_powers[index] for index in range(3)
        )
        value = PRODUCT.extension_log(
            relation[1]
            * pow(left_coefficient * right_coefficient % P, -1, P) % P
        )
    return row, value


def polynomial_equations(products, forced_index, matching, mate, relation):
    residual = products[:forced_index] + products[forced_index + 1:]
    equations = [products[forced_index] - mate]
    for left, right in matching:
        if relation[0] == "negation":
            equations.append(residual[left] + residual[right])
        else:
            equations.append(residual[left] * residual[right] - relation[1])
    return tuple(equations)


def probe(cell, packet_index, name, verbose=True, print_limit=3):
    b, c = PACKETS[cell][packet_index]
    mate, relation = involution(cell, b, c)
    forms = tuple(PRODUCT.product_forms(name, b, c))
    expected = {"Z0": 4, "Z1": 32, "Z2": 16, "Z3": 32, "Z4": 16}
    require(len(forms) == expected[name], "form census")
    checked = soluble = isolated = family_samples = 0
    guarded = []
    families = []
    started = time.monotonic()
    for form_index, products in enumerate(forms):
        data = tuple(PRODUCT.monomial(expression) for expression in products)
        for forced_index in range(7):
            residual_indices = tuple(
                index for index in range(7) if index != forced_index
            )
            forced_powers, forced_coefficient = data[forced_index]
            for matching_index, matching in enumerate(PRODUCT.MATCHINGS):
                rows = [forced_powers]
                values = [PRODUCT.extension_log(
                    mate * pow(forced_coefficient, -1, P) % P
                )]
                for left, right in matching:
                    row, value = relation_row(
                        data[residual_indices[left]],
                        data[residual_indices[right]],
                        relation,
                    )
                    rows.append(row)
                    values.append(value)
                rank, solutions, family = PRODUCT.solve_congruences(
                    tuple(rows), tuple(values)
                )
                if family:
                    equations = polynomial_equations(
                        products, forced_index, matching, mate, relation
                    )
                    collision = PRODUCT.forced_guard_collision(
                        equations, b, c, products
                    )
                    families.append(
                        (
                            form_index, forced_index, matching_index, rank,
                            collision or "unresolved",
                        )
                    )
                if solutions:
                    soluble += 1
                    if family:
                        family_samples += len(solutions)
                    else:
                        isolated += len(solutions)
                    for logs in solutions:
                        if PRODUCT.guarded_assignment(logs, b, c, products):
                            guarded.append(
                                (form_index, forced_index, matching_index, logs)
                            )
                            if verbose and len(guarded) <= print_limit:
                                print(
                                    "BC_PRODUCT_GUARDED "
                                    f"cell={cell} packet={packet_index} "
                                    f"skeleton={name} form={form_index} "
                                    f"forced={forced_index} matching={matching_index} "
                                    f"logs={logs}",
                                    flush=True,
                                )
                checked += 1
                if verbose and checked % 1000 == 0:
                    print(
                        "BC_PRODUCT_PROGRESS "
                        f"cell={cell} packet={packet_index} skeleton={name} "
                        f"checked={checked} guarded={len(guarded)} "
                        f"families={len(families)} "
                        f"seconds={time.monotonic()-started:.2f}",
                        flush=True,
                    )
    return {
        "checked": checked,
        "soluble": soluble,
        "isolated": isolated,
        "family_samples": family_samples,
        "guarded": tuple(guarded),
        "families": tuple(families),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell", type=int, choices=(12, 13, 14), required=True)
    parser.add_argument("--packet", type=int, required=True)
    parser.add_argument("--skeleton", choices=PRODUCT.SKELETONS, required=True)
    parser.add_argument("--print-limit", type=int, default=3)
    arguments = parser.parse_args()
    require(0 <= arguments.packet < len(PACKETS[arguments.cell]), "packet")
    result = probe(
        arguments.cell, arguments.packet, arguments.skeleton,
        print_limit=arguments.print_limit,
    )
    print(
        "RATE_HALF_KB_ZERO_LOOP_433_BC_PRODUCT_PROBE "
        f"cell={arguments.cell} packet={arguments.packet} "
        f"skeleton={arguments.skeleton} checked={result['checked']} "
        f"soluble={result['soluble']} isolated={result['isolated']} "
        f"family_samples={result['family_samples']} "
        f"guarded={len(result['guarded'])} "
        f"families={len(result['families'])}",
        flush=True,
    )


if __name__ == "__main__":
    main()
