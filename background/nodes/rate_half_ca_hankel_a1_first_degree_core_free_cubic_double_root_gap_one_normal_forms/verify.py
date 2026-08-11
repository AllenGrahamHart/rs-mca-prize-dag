#!/usr/bin/env python3
"""Exact replay for the u=1 double-root cubic packets."""

M = 1 << 37
RHO = 4 * M
E = (RHO + 1) // 3
DELTA = 2 * E - 1


def need(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    # i0, cs, cd, eps_s, eps_d, w, ts, td
    packets = (
        (0, 1, 1, 0, 0, 1, 1, E - 2),
        (0, 1, 1, 1, 0, 0, 2, E - 2),
        (0, 1, 1, 0, 1, 0, 1, E - 1),
        (1, 2, 1, 0, 0, 0, 2, E - 2),
    )
    omission = E - 1
    for i0, cs, cd, eps_s, eps_d, w, ts, td in packets:
        eps = eps_s + eps_d
        i_e = DELTA - 1 - i0
        c_tot = DELTA - w
        need(cs + cd == 2 + i0, "deficit sum failed")
        need(c_tot == i_e + eps + 2 * i0,
             "excess degree was not exhausted")
        need(ts + td == c_tot - omission, "new-root count failed")
        need((cs + eps_s - ts) % 3 == 0, "simple correction failed")
        need((cd + eps_d - td) % 3 == 0, "double correction failed")
        need(ts <= E - cs and td <= E - cd, "row support cap failed")

        simple_extra = 1 if i0 == 0 else 2
        double_extra = 1
        need((E - cs) + simple_extra == E,
             "simple vertical degree failed")
        need((E - cd) + double_extra == E,
             "double vertical degree failed")

    need(len(packets) == 4, "wrong packet count")
    print(f"CUBIC_DOUBLE_GAP_ONE_NORMAL_FORMS_PASS e={E} packets={len(packets)}")


if __name__ == "__main__":
    main()
