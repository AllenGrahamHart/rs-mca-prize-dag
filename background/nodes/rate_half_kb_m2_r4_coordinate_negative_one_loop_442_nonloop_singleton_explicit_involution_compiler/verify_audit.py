#!/usr/bin/env python3
"""Independent F_41 audit of the explicit involution."""


PRIME = 41


def main():
    b, c = 10, 5
    gamma = (c+2*b-b*b) % PRIME
    alpha = (-b*(c+b*b)) % PRIME
    beta = (b*b*(c-b*b-2*b*c)) % PRIME
    if (gamma, alpha, beta) != (7, 16, 16):
        raise RuntimeError("coefficients")

    def phi(left, right):
        return (gamma*left*right-alpha*(left+right)-beta) % PRIME

    if phi(-b*b, b) or phi(-b, -c):
        raise RuntimeError("common pairs")
    determinant = (alpha*alpha+gamma*beta) % PRIME
    if determinant != 40:
        raise RuntimeError("determinant")
    denominator = (gamma*c-alpha) % PRIME
    mate = (alpha*c+beta)*pow(denominator, -1, PRIME) % PRIME
    if mate != 18 or phi(c, mate):
        raise RuntimeError("forced mate")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_INVOLUTION_AUDIT_PASS "
        "field=41 coefficients=7,16,16 mate=18"
    )


if __name__ == "__main__":
    main()
