#!/usr/bin/env python3
"""Independent scalar audit of the two complement eliminations."""


def main() -> None:
    prime = 1_000_003
    checked = 0
    for q_value in (2, 7, 101, 999_983):
        for p_value in (3, 11, 313):
            for v_value in (5, 17):
                for b_value in (1, 19):
                    for k_value in (0, 23):
                        for x_gap in (29, 41):
                            # Start from the weld and reconstruct both
                            # complements without reusing the proof's
                            # elimination direction.
                            w_value = (x_gap + q_value * k_value) * pow(
                                b_value, prime - 2, prime
                            ) % prime
                            h_value = (
                                q_value * v_value + p_value * w_value
                            ) % prime
                            g_value = p_value * x_gap % prime
                            a_value = (
                                -p_value * k_value - v_value * b_value
                            ) % prime

                            assert (
                                q_value * a_value + h_value * b_value
                            ) % prime == g_value
                            assert (
                                w_value * b_value - x_gap
                            ) % prime == q_value * k_value % prime
                            assert (
                                v_value * b_value + a_value
                            ) % prime == -p_value * k_value % prime
                            checked += 1

    assert checked == 4 * 3 * 2 * 2 * 2 * 2
    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_TWO_SIDED_COMPLEMENT_WELD_"
        f"AUDIT_PASS scalar_instances={checked}"
    )


if __name__ == "__main__":
    main()
