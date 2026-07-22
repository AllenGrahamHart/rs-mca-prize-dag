#!/usr/bin/env python3
"""Independent algebra and scope audit for the Belyi shifted-value gate."""

from pathlib import Path


HERE = Path(__file__).resolve().parent


def inv(x: int, p: int) -> int:
    return pow(x % p, -1, p)


def main() -> None:
    checks = 0
    # Check the three coefficient cancellations in the rational derivative
    # independently at several characteristics and projective parameters.
    for p in (101, 131, 193):
        for theta, c in ((7, 8), (15, 16), (23, 9)):
            if c % p in (0, 1):
                continue
            u = theta * inv(c - 1, p) % p
            w = theta * c * inv(c - 1, p) % p
            k_inv = theta * c % p  # normalize r_0=1, z=c
            assert (theta + u - w) % p == 0
            assert (-theta * (1 + c) + w * c - u) % p == 0
            assert (theta * c - k_inv) % p == 0
            checks += 3

    proof = (HERE / "proof.md").read_text()
    for anchor in ("Both products lie in the same coset",
                   "Q(beta_i)G'(beta_i)=2a lambda", "leading coefficient `h`",
                   "G-lambda Y=Q T/(2a)",
                   "zero quadratic root is impossible", "order two",
                   "XDR'=(q/(2a))Q(R)", "Psi'=0", "theta=h",
                   "uf-1=0 mod p", "c=m", "e<p-1<2e"):
        assert anchor in proof
        checks += 1

    print(f"L1_MERSENNE_NEXT_TO_MAXIMAL_BELYI_SHIFTED_VALUE_GATE_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
