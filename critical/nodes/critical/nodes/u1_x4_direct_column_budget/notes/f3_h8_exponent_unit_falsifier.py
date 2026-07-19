#!/usr/bin/env python3
"""Refute exponent-unit maps as x83 support symmetries."""

from __future__ import annotations

from f3_h8_n64_x83_obstruction_interface import (
    forced_obstructions,
    is_square_mod,
    locator_from_exponents,
    root_table,
)


P = 193
BASE_SUPPORT = (0, 1, 2, 9, 10, 16, 24, 25, 32, 33, 34, 41, 42, 48, 56, 57)

EXPECTED_BASE = {
    "locator": [14, 0, 189, 0, 138, 0, 90, 0, 167, 0, 78, 0, 66, 0, 29, 0, 1],
    "square_root": [47, 0, 156, 0, 145, 0, 111, 0, 1],
    "obstructions": [0, 0, 0, 0, 0, 0, 0],
    "lambda": 72,
    "lambda_square": True,
    "full_zero": True,
}
EXPECTED_IMAGES = {
    3: {
        "support": (0, 3, 6, 8, 11, 16, 27, 30, 32, 35, 38, 40, 43, 48, 59, 62),
        "locator": [42, 0, 191, 0, 37, 0, 162, 0, 123, 0, 66, 0, 183, 0, 160, 0, 1],
        "square_root": [74, 0, 129, 0, 76, 0, 80, 0, 1],
        "obstructions": [0, 180, 0, 60, 0, 20, 0],
        "lambda": 30,
        "lambda_square": False,
        "full_zero": False,
    },
    63: {
        "support": (0, 7, 8, 16, 22, 23, 30, 31, 32, 39, 40, 48, 54, 55, 62, 63),
        "locator": [69, 0, 71, 0, 115, 0, 171, 0, 136, 0, 34, 0, 65, 0, 110, 0, 1],
        "square_root": [1, 0, 164, 0, 64, 0, 55, 0, 1],
        "obstructions": [0, 64, 0, 82, 0, 87, 0],
        "lambda": 125,
        "lambda_square": False,
        "full_zero": False,
    },
}


def classify(support: tuple[int, ...], p: int) -> dict[str, object]:
    vals = root_table(p, 64)
    locator = locator_from_exponents(support, vals, p)
    square_root, obstructions, lam = forced_obstructions(locator, p, 8)
    lam_square = lam != 0 and is_square_mod(lam, p)
    return {
        "locator": locator,
        "square_root": square_root,
        "obstructions": obstructions,
        "lambda": lam,
        "lambda_square": lam_square,
        "full_zero": all(value == 0 for value in obstructions) and lam_square,
    }


def main() -> None:
    base = classify(BASE_SUPPORT, P)
    if base != EXPECTED_BASE:
        raise AssertionError(("base", base, EXPECTED_BASE))

    print("h=8 exponent-unit falsifier")
    print(f"p={P}")
    print(f"base support: {BASE_SUPPORT}")
    print(f"base obstructions: {base['obstructions']}, lambda={base['lambda']}, full_zero={base['full_zero']}")
    for unit, expected in EXPECTED_IMAGES.items():
        image_support = tuple(sorted((unit * exponent) % 64 for exponent in BASE_SUPPORT))
        image = classify(image_support, P)
        if image_support != expected["support"]:
            raise AssertionError((unit, image_support, expected["support"]))
        expected_image = dict(expected)
        expected_image.pop("support")
        if image != expected_image:
            raise AssertionError((unit, image, expected_image))
        print(f"unit u={unit} image support: {image_support}")
        print(
            f"unit u={unit} obstructions: {image['obstructions']}, "
            f"lambda={image['lambda']}, full_zero={image['full_zero']}"
        )
    print("H8_EXPONENT_UNIT_FALSIFIER_PASS")


if __name__ == "__main__":
    main()
