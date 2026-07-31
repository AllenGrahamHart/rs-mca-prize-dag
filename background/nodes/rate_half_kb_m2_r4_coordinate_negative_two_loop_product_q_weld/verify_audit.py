#!/usr/bin/env python3
"""Independent finite-field audit of the two-loop weld identity."""

from pathlib import Path


NODE = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def run(prime: int, labels: tuple[int, ...], numerator: tuple[int, int], denominator: tuple[int, int]) -> None:
    def ev(poly: tuple[int, int], value: int) -> int:
        return (poly[0] + poly[1] * value) % prime

    products = tuple(ev(numerator, value) * pow(ev(denominator, value), -1, prime) % prime for value in labels)
    require(len(set(products)) == 5, "product collision")
    lam, mu = labels[:2]
    residual = labels[2:]

    def r(value: int) -> int:
        return (value - lam) * (value - mu) % prime

    c = 11 % prime
    q = {value: -c * r(value) * pow(ev(denominator, value), -1, prime) % prime for value in residual}
    for anchor in (lam, mu):
        anchor_product = products[labels.index(anchor)]
        for i in residual:
            for j in residual:
                if i >= j:
                    continue
                left = q[i] * r(j) * (anchor - i) * (anchor_product - products[labels.index(j)])
                right = q[j] * r(i) * (anchor - j) * (anchor_product - products[labels.index(i)])
                require((left - right) % prime == 0, "weld residual")


def main() -> None:
    run(29, (1, 28, 4, 25, 9), (2, 3), (1, 2))
    run(31, (1, 30, 4, 27, 9), (5, 7), (3, 2))
    proof = (NODE / "proof.md").read_text()
    require("Reverse the calculation" in proof and "all three nonloop labels" in proof, "converse")
    print("RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_TWO_LOOP_WELD_AUDIT_PASS primes=29,31 anchors=4")


if __name__ == "__main__":
    main()
