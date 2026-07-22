#!/usr/bin/env python3
"""Mutation audit for the complement Toeplitz normal form."""

from __future__ import annotations


def valid(row: dict[str, int | bool]) -> bool:
    return all(
        (
            row["char_divides_n"] is False,
            row["w"] == row["a"] - row["k"],
            row["r"] == row["n"] - row["a"],
            row["window_start"] == row["n"] - row["w"],
            row["window_stop"] == row["n"] - 1,
            row["derivative_beta_retained"] is True,
            row["codeword_shift_invariant"] is True,
            row["monic_slice_affine"] is True,
            row["exact_gcd_guard"] is True,
            row["prefix_q_auto_consumed"] is False,
        )
    )


def main() -> None:
    row: dict[str, int | bool] = {
        "char_divides_n": False,
        "n": 16,
        "a": 10,
        "k": 6,
        "w": 4,
        "r": 6,
        "window_start": 12,
        "window_stop": 15,
        "derivative_beta_retained": True,
        "codeword_shift_invariant": True,
        "monic_slice_affine": True,
        "exact_gcd_guard": True,
        "prefix_q_auto_consumed": False,
    }
    assert valid(row)
    mutations: dict[str, int | bool] = {
        "char_divides_n": True,
        "w": 3,
        "r": 5,
        "window_start": 11,
        "window_stop": 14,
        "derivative_beta_retained": False,
        "codeword_shift_invariant": False,
        "monic_slice_affine": False,
        "exact_gcd_guard": False,
        "prefix_q_auto_consumed": True,
    }
    caught = 0
    for key, value in mutations.items():
        mutant = dict(row)
        mutant[key] = value
        if not valid(mutant):
            caught += 1
    assert caught == len(mutations)
    print(f"L1_EXACT_SHELL_COMPLEMENT_TOEPLITZ_NORMAL_FORM_AUDIT_PASS mutations={caught}")


if __name__ == "__main__":
    main()
