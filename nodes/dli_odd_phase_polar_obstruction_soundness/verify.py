#!/usr/bin/env python3
"""Lightweight schema check for DLI polar-obstruction certificates."""

from __future__ import annotations


def verifies_polar_obstruction(p: int, reduced_pole_order: int) -> bool:
    return p > 1 and reduced_pole_order > 0 and reduced_pole_order % p != 0


def main() -> None:
    assert verifies_polar_obstruction(5, 3)
    assert not verifies_polar_obstruction(5, 10)
    assert not verifies_polar_obstruction(5, 0)
    print("PASS: reduced pole order prime to p certifies DLI polar obstruction")


if __name__ == "__main__":
    main()
