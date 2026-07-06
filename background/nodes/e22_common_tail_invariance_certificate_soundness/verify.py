#!/usr/bin/env python3
"""Toy cyclic check for common-tail invariance certificates."""

from __future__ import annotations


def is_invariant(subset: set[int], kernel: set[int], modulus: int) -> bool:
    return all(((x + k) % modulus) in subset for x in subset for k in kernel)


def verify_certificate(cert: dict) -> None:
    tail = set(cert["tail"])
    moduli = cert["moduli"]
    assert tail
    assert len(tail) < min(moduli.values())
    assert all(m > cert["t"] and m & (m - 1) == 0 for m in moduli.values())
    for petal, support in cert["supports"].items():
        modulus = cert["ambient_modulus"]
        non_tail = set(support) - tail
        kernel = set(cert["kernels"][petal])
        assert is_invariant(non_tail, kernel, modulus)


def main() -> None:
    cert = {
        "ambient_modulus": 8,
        "t": 1,
        "tail": [7],
        "moduli": {"P0": 2, "P1": 4},
        "kernels": {"P0": [0, 4], "P1": [0, 2, 4, 6]},
        "supports": {
            "P0": [0, 4, 7],
            "P1": [0, 2, 4, 6, 7],
        },
    }
    verify_certificate(cert)
    print("PASS: common-tail kernel invariance certificate checks")


if __name__ == "__main__":
    main()
