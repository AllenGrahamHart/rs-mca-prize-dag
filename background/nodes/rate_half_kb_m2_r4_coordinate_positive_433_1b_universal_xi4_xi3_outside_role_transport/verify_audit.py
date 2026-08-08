#!/usr/bin/env python3
"""Independent integer audit of the universal xi4/xi3 transport."""

import itertools
from pathlib import Path


NODE = Path(__file__).resolve().parent
VALUES = (-3, -2, -1, 1, 2, 3)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def records(b, c, d, e, f, sigma_c, sigma_o):
    return (d*e, d*e, -d*e, d*f, sigma_o*e*f, b*f, sigma_c*c*f)


def sums(b, c, d, e, f, sigma_c, sigma_o):
    return (
        (d+e)**2, (d+e)**2, (d-e)**2, (d+f)**2,
        (e+sigma_o*f)**2, (b+f)**2, (c+sigma_c*f)**2,
    )


def guard_signature(values):
    output = {abs(value) for value in values}
    output |= {
        abs(left-right) for left, right in itertools.combinations(values, 2)
    }
    output |= {
        abs(left+right) for left, right in itertools.combinations(values, 2)
    }
    return output


def main():
    permutation = (0, 1, 2, 4, 3, 5, 6)
    residual_xi4 = (0, 1, 2, 3, 5, 6)
    residual_xi3 = (0, 1, 2, 4, 5, 6)
    rows = 0
    for sigma_c, sigma_o in itertools.product((-1, 1), repeat=2):
        for b, c, d, e, f in itertools.product(VALUES, repeat=5):
            original = records(b, c, d, e, f, sigma_c, sigma_o)
            original_sums = sums(b, c, d, e, f, sigma_c, sigma_o)
            D, E, F = sigma_o*e, sigma_o*d, f
            transported = records(b, c, D, E, F, sigma_c, sigma_o)
            transported_sums = sums(b, c, D, E, F, sigma_c, sigma_o)
            require(tuple(transported[i] for i in permutation) == original,
                    "record identity")
            require(tuple(transported_sums[i] for i in permutation)
                    == original_sums, "sum identity")
            require(tuple(original[i] for i in residual_xi4)
                    == tuple(transported[i] for i in residual_xi3),
                    "compact residual identity")
            require(guard_signature((1,b,c,d,e,f))
                    == guard_signature((1,b,c,D,E,F)), "guard identity")
            rows += 1
    proof = (NODE / "proof.md").read_text()
    audit = (NODE / "audit.md").read_text()
    require("15 common role cells" in proof, "universal common-role scope")
    require("31,104" in audit, "independent audit ledger")
    print(f"audit=ok integer_rows={rows} lanes=4 xi4_to_xi3=exact")


if __name__ == "__main__":
    main()
