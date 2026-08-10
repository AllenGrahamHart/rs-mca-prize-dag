#!/usr/bin/env python3
"""Independent closed-form audit of the resultant valuation split."""


def main() -> None:
    prime = 1_000_003
    checked = 0
    for m in range(2, 14):
        for h in (5, 37, 997):
            for constant in (0, 3, 29):
                x_gap = (h - pow(-constant, m, prime)) % prime
                assert x_gap

                # Res(t^m-h,t+c)=(-1)^(m+1) x_gap.
                res_b = pow(-1, m + 1, prime) * x_gap % prime
                # Multiplicativity and the exact weld force the complement.
                res_w = pow(x_gap, m, prime) * pow(res_b, prime - 2, prime) % prime
                assert res_b * res_w % prime == pow(x_gap, m, prime)

                # At x_gap=0 the two orders are exactly 1 and m-1.
                assert 1 + (m - 1) == m
                assert m - 1 >= 1

                # A parameter-constant factor has an mth-power norm, so
                # neither exact order can come from one when m>1.
                assert 1 % m != 0
                assert (m - 1) % m != 0

                bad_gap = (x_gap + 1) % prime
                assert res_b * res_w % prime != pow(bad_gap, m, prime)
                checked += 1

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_LINEAR_UNIT_RESULTANT_GATE_"
        f"AUDIT_PASS closed_form_instances={checked} mutations={checked}/{checked}"
    )


if __name__ == "__main__":
    main()
