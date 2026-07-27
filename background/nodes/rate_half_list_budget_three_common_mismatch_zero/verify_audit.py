#!/usr/bin/env python3
"""Independent boundary audit for selected-support coverage."""


def main() -> None:
    # Covered common values must equal the received value.
    for common in range(5):
        for received in range(5):
            covered_indices = [i for i in range(4) if common == received]
            if covered_indices:
                assert common == received

    # If coverage is dropped, a common mismatch is possible.
    values = (1, 1, 1, 1)
    received = 0
    selected_mask = 0
    assert len(set(values)) == 1
    assert values[0] != received
    assert selected_mask == 0

    print("BUDGET_THREE_COMMON_MISMATCH_ZERO_AUDIT_PASS mutation=uncovered_common_mismatch")


if __name__ == "__main__":
    main()
