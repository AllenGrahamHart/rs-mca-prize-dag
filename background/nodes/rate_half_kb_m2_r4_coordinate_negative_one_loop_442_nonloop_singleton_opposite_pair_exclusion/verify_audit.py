#!/usr/bin/env python3
"""Independent F_73 replay of the opposite-pair exclusion."""


PRIME = 73
IOTA = 27


def main():
    if IOTA*IOTA % PRIME != PRIME-1:
        raise RuntimeError("fourth root")
    guarded_product_rows = 0
    guarded_q_rows = 0
    for epsilon_1 in (1, -1):
        for epsilon_2 in (1, -1):
            for b in range(1, PRIME):
                if b in (1, PRIME-1):
                    continue
                for r in range(1, PRIME):
                    x = r*r % PRIME
                    if x in (1, PRIME-1):
                        continue
                    denominator = (x*x+2*b*x+1) % PRIME
                    constant = b*(b*x*x+b+2*x) % PRIME
                    if denominator == 0:
                        if constant == 0:
                            raise RuntimeError("guarded denominator branch")
                        continue
                    c = constant*pow(denominator, -1, PRIME) % PRIME
                    if c in (0, 1, PRIME-1) or c*c % PRIME == b*b % PRIME:
                        continue
                    guarded_product_rows += 1
                    factors = {
                        (1, 1): (r-1)*(r-IOTA)*(r*r-IOTA),
                        (1, -1): (r+1)*(r-IOTA)*(r*r+IOTA),
                        (-1, 1): (r+1)*(r+IOTA)*(r*r-IOTA),
                        (-1, -1): (r-1)*(r+IOTA)*(r*r+IOTA),
                    }
                    if factors[(epsilon_1, epsilon_2)] % PRIME == 0:
                        guarded_q_rows += 1
    if guarded_product_rows == 0 or guarded_q_rows != 0:
        raise RuntimeError("finite guarded exclusion")
    print(
        "RATE_HALF_KB_M2_R4_COORDINATE_NEGATIVE_ONE_LOOP_442_OPPOSITE_AUDIT_PASS "
        f"field=73 product_rows={guarded_product_rows} q_survivors=0"
    )


if __name__ == "__main__":
    main()
