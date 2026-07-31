#!/usr/bin/env python3
"""Small-field replay of both aligned-pair families."""


def equations(prime, iota, b, c, r, t2):
    return (
        b*b*r*r*t2-b*b+b*c*r*r-b*c*t2+b*r*r-b*t2+c*r*r*t2-c,
        -b*b*r*r*t2-b*b+b*c*r*r+b*c*t2-b*r*r-b*t2+c*r*r*t2+c,
        b*b*r*r-iota*b*b+(iota-1)*b*c*r+(iota-1)*b*r+c*r*r-iota*c,
        -b*b*r*r-iota*b*b+(iota+1)*b*c*r-(iota+1)*b*r+c*r*r+iota*c,
    )


def check(prime, values):
    b, c, r, t2 = values
    if any(value % prime for value in equations(prime, 5, b, c, r, t2)):
        raise RuntimeError(f"failed family witness {values}")
    labels = (t2, 1, -1, r*r, -r*r)
    products = (-b*b, b, -b, c, -c)
    if len({value % prime for value in labels}) != 5:
        raise RuntimeError("label collision")
    if len({value % prime for value in products}) != 5:
        raise RuntimeError("product collision")


def main():
    prime = 13
    iota = 5
    # Family A, r=3; family B, b=7.
    check(prime, (iota*3 % prime, iota*9 % prime, 3, iota*9 % prime))
    b = 7
    check(prime, (b, -pow(b, -1, prime) % prime,
                  -iota*pow(b, -1, prime) % prime, -b % prime))
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_ALIGNED_AUDIT_PASS "
        "prime=13 families=2"
    )


if __name__ == "__main__":
    main()
