#!/usr/bin/env python3
"""Independent F_73 audit of the aligned outside-loop q contradiction."""


PRIME = 73
IOTA = 27


def roots(function):
    return [value for value in range(PRIME) if function(value) % PRIME == 0]


def main():
    if IOTA*IOTA % PRIME != PRIME-1:
        raise RuntimeError("fourth root")
    rows = 0
    survivors = 0

    for r in roots(lambda value: value*value+value+1):
        b = IOTA*r % PRIME
        c = IOTA*r*r % PRIME
        h = c
        a_roots = roots(lambda w: (w-c)*(w-IOTA))
        if set(a_roots) != {h, IOTA}:
            raise RuntimeError("family A q roots")
        loop_product = b*pow(IOTA, -1, PRIME) % PRIME
        if loop_product != r:
            raise RuntimeError("family A loop product")
        for sign_product in (1, PRIME-1):
            for d in range(1, PRIME):
                if (-d*d-loop_product) % PRIME == 0 and (
                    pow(d, 4, PRIME)
                    +sign_product*b*b*c*c
                ) % PRIME == 0:
                    survivors += 1
        if (b*b-loop_product) % PRIME == 0:
            survivors += 1
        rows += 1

    for b in roots(lambda value: IOTA*value*value+value-IOTA):
        c = -pow(b, -1, PRIME) % PRIME
        h = -b % PRIME
        a_roots = roots(lambda w: (w+b)*(w-IOTA))
        if set(a_roots) != {h, IOTA}:
            raise RuntimeError("family B q roots")
        loop_product = IOTA*b % PRIME
        for sign_product in (1, PRIME-1):
            for d in range(1, PRIME):
                if (-d*d-loop_product) % PRIME == 0 and (
                    pow(d, 4, PRIME)
                    +sign_product*b*b*c*c
                ) % PRIME == 0:
                    survivors += 1
        if (b*b-loop_product) % PRIME == 0:
            survivors += 1
        rows += 1

    if rows != 4 or survivors:
        raise RuntimeError("finite aligned loop-q audit")
    print(
        "RATE_HALF_KB_ONE_LOOP_442_ALIGNED_LOOP_Q_AUDIT_PASS "
        f"field={PRIME} family_rows={rows} survivors={survivors}"
    )


if __name__ == "__main__":
    main()
