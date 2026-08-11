#!/usr/bin/env python3
"""Exact replay for the two core-free bounded-divisor packets."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3
DELTA = 2 * E - 1


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    packets = []
    for i0, deficits in ((0, (1, 1)), (1, (1, 2))):
        csum = sum(deficits)
        incidence_degree = 2 * E - csum
        determinant_tail = DELTA - incidence_degree - 2 * i0
        picard_degree = csum - i0 - 1
        packets.append((i0, deficits, determinant_tail, picard_degree))
        need(csum == 2 + i0, "row deficit failed")
        need(determinant_tail == 1 - i0, "determinant tail failed")
        need(picard_degree == 1, "Picard degree failed")
        need(max(c + 1 for c in deficits) <= 3, "Forney tail cap failed")
    need(len(packets) == 2, "wrong packet count")
    need((RHO + 3) * E - (E + 1) * RHO == 1, "line-bundle degree failed")
    print(f"CORE_FREE_BOUNDED_DIVISOR_PASS e={E} packets={packets}")


if __name__ == "__main__":
    main()
