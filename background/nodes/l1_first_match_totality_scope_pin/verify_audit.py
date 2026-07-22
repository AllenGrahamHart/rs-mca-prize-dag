#!/usr/bin/env python3
"""Mutation controls for the first-match totality scope pin."""


def main() -> None:
    carrying = ({0, 2}, {1, 2}, {0, 1})
    owners = tuple(min(keys) for keys in carrying)
    assert owners == (0, 1, 0)

    cells = tuple(
        {item for item, owner in enumerate(owners) if owner == key}
        for key in range(3)
    )
    assert set().union(*cells) == {0, 1, 2}
    assert sum(len(cell) for cell in cells) == 3

    # Raw carrying-chart cells overlap; first ownership is materially needed.
    raw_cells = tuple(
        {item for item, keys in enumerate(carrying) if key in keys}
        for key in range(3)
    )
    assert sum(len(cell) for cell in raw_cells) == 6 > 3

    # Partition totality alone has no polynomial-payment content.
    owner_cell_caps_proved = False
    polynomial_key_sum_proved = False
    assert not owner_cell_caps_proved and not polynomial_key_sum_proved

    print("L1_FIRST_MATCH_TOTALITY_SCOPE_PIN_AUDIT_PASS mutations=4")


if __name__ == "__main__":
    main()
