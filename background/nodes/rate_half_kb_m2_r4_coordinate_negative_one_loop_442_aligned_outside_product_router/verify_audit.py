#!/usr/bin/env python3
"""Independent finite-field audit of the retained product branches."""


PRIME = 73


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def guarded(common, outside, representatives):
    squares = {value*value % PRIME for value in representatives}
    return (len(common) == 5 and len(set(outside)) == 7
            and not common.intersection(outside)
            and len(squares) == len(representatives))


def main():
    i = 27
    require(i*i % PRIME == PRIME-1, "fourth root")

    # Family A, S2.
    r, b, c, t = 8, 70, 49, 7
    d, e, f = 2, 8, 4
    require((r*r+r+1) % PRIME == 0 and b == i*r % PRIME
            and c == i*r*r % PRIME and t*t % PRIME == c, "family A")
    common = {-b*b % PRIME, b, -b % PRIME, c, -c % PRIME}
    outside = [c*d % PRIME, -c*d % PRIME, -e*e % PRIME,
               d*f % PRIME, -d*f % PRIME, e*f % PRIME, -e*f % PRIME]
    require(-e*e % PRIME == b*b % PRIME, "S2 forced loop")
    require(guarded(common, outside, (1, b, c, d, e, f)), "S2 guards")

    # Family B, S1-DF, with all four signs negative.
    b, c, r, t = 3, 24, 64, 17
    d, e, f = 10, 8, 21
    a = be = g = de = -1
    require((i*b*b+b-i) % PRIME == 0
            and b*c % PRIME == PRIME-1
            and b*r % PRIME == -i % PRIME
            and t*t % PRIME == -b % PRIME, "family B")
    common = {-b*b % PRIME, b, -b % PRIME, c, -c % PRIME}
    x, y, z = a*c*e, be*c*f, -d*d
    u, v = g*d*e, de*d*f
    outside = [value % PRIME for value in (x, y, z, u, v, e*f, -e*f)]
    require(v % PRIME == b*b % PRIME and (x+z) % PRIME == 0
            and (y+u) % PRIME == 0, "S1-DF routing")
    require(pow(d, 4, PRIME)
            == (-a*be*g*de*b*b*c*c) % PRIME, "S1 quartic")
    require(guarded(common, outside, (1, b, c, d, e, f)), "S1 guards")

    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_ROUTER_AUDIT_PASS "
        "field=73 retained=S1-DF,S2"
    )


if __name__ == "__main__":
    main()
