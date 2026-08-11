#!/usr/bin/env python3
"""Component-degree and restriction mutation audit."""


def main():
    profiles = 0
    for e in range(2, 100):
        # Any nonnegative component degree is positive; total degree one can
        # therefore support only one component.
        values = []
        for e_i in range(1, e + 1):
            for a_i in range(0, 4 * e_i):
                value = e * e_i - (e + 1) * a_i
                if value >= 0:
                    values.append((e_i, a_i, value))
                    assert value >= 1
        assert (e, e - 1, 1) in values
        profiles += len(values)

    e = 11
    mutated_value = e * 1 - e * 1
    assert mutated_value == 0

    print(
        "RATE_HALF_CA_HANKEL_STRICT_A3_FINAL_CORNER_INTEGRAL_PICARD_PIN_AUDIT_PASS "
        f"component_profiles={profiles} mutation=detected"
    )


if __name__ == "__main__":
    main()
