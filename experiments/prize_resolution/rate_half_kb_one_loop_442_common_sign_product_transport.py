#!/usr/bin/env python3
"""Check the common product data in one sextic root-sign row."""

import argparse
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LOOP_PATH = ROOT / (
    "experiments/prize_resolution/"
    "rate_half_kb_one_loop_442_s1_loop_buchberger.py"
)
SPEC = importlib.util.spec_from_file_location("loop", LOOP_PATH)
LOOP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LOOP)
SOLVER = LOOP.SOLVER

EXPECTED = (
    (
        (165644906, 1305134575, 1484956850),
        (1244418779, 141852127, 1677606574),
    ),
    (
        (1190295236, 1600338149, 1091152148),
        (368587486, 183733761, 1744133513),
    ),
)


def action_data(component, c_value):
    modulus = SOLVER.CUBICS[component]
    b = SOLVER.B_ELEMENT
    b_squared = SOLVER.multiply(b, b, modulus)
    alpha = SOLVER.neg(SOLVER.multiply(
        b, SOLVER.add(c_value, b_squared), modulus
    ))
    beta = SOLVER.multiply(
        b_squared,
        SOLVER.sub(
            SOLVER.sub(c_value, b_squared),
            SOLVER.scale(2, SOLVER.multiply(b, c_value, modulus)),
        ),
        modulus,
    )
    gamma = SOLVER.sub(
        SOLVER.add(c_value, SOLVER.scale(2, b)), b_squared
    )
    determinant = SOLVER.add(
        SOLVER.multiply(alpha, alpha, modulus),
        SOLVER.multiply(beta, gamma, modulus),
    )
    return alpha, beta, gamma, determinant


def check_row(epsilon_1, epsilon_2):
    records = []
    for component in (0, 1):
        c_value, mate_value = LOOP.common_values(
            component, epsilon_1, epsilon_2
        )
        if (c_value, mate_value) != EXPECTED[component]:
            raise RuntimeError(
                f"common product data drift in row "
                f"{epsilon_1},{epsilon_2}, component {component}"
            )
        modulus = SOLVER.CUBICS[component]
        nonsquare = SOLVER.power(
            SOLVER.neg(mate_value), (SOLVER.P**3-1)//2, modulus
        )
        if nonsquare != SOLVER.neg(SOLVER.ONE):
            raise RuntimeError("forced-loop square class")
        action = action_data(component, c_value)
        if action[3] == SOLVER.ZERO:
            raise RuntimeError("singular product involution")
        records.append((component, c_value, mate_value, action[3]))
    return tuple(records)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("epsilon_1", type=int, choices=(-1, 1))
    parser.add_argument("epsilon_2", type=int, choices=(-1, 1))
    arguments = parser.parse_args()
    records = check_row(arguments.epsilon_1, arguments.epsilon_2)
    print(
        "ONE_LOOP_442_COMMON_SIGN_PRODUCT_TRANSPORT_PASS "
        f"signs={arguments.epsilon_1},{arguments.epsilon_2} "
        f"components={len(records)} common_c_m=True loop_nonsquare=True"
    )


if __name__ == "__main__":
    main()
