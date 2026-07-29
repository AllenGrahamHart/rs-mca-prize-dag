#!/usr/bin/env python3
"""Verify the binding prize E1 profile-weight payoff ladder."""

from __future__ import annotations

from functools import cache
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EDGE_CAP = 65127585921474870475467050631501738502567
EXPECTED = (
    ((4, 2, 18), 1873053318886373426584792000465260242, 69541),
    ((3, 6, 18), 1386246316188473270092082114587711840, 93962),
    ((2, 10, 18), 1227527050040565145269313275179180544, 106111),
    ((1, 14, 18), 1154418456451360735963226152798543872, 112831),
    ((0, 18, 18), 1117325838856821897682125205459304448, 116577),
    ((4, 4, 20), 522452937039935372855706187881128712, 249314),
    ((3, 8, 20), 432776013393430570914298670133713280, 300975),
    ((2, 12, 20), 394747100704470761700528481188071424, 329971),
    ((1, 16, 20), 374901575688629273473602791080820736, 347438),
    ((0, 20, 20), 363409091422312822402997461372633088, 358425),
    ((5, 2, 22), 213637532202373724400313526161611334, 609701),
    ((4, 6, 22), 155883854763951097618312682146951968, 835591),
)


@cache
def weight(a: int, b: int) -> int:
    h = 128
    ell = 33
    n0 = h - a - b
    total = 0
    for j in range(b + 1):
        for r in range(n0 + 1):
            tx = a + j + r
            ty = a + b - j + r
            if tx <= ell and ty <= ell and (tx - ell) % 2 == 0 and (ty - ell) % 2 == 0:
                total += comb(b, j) * comb(n0, r) * 2**r
    return total


def eligible_profiles() -> list[tuple[int, int, int, int]]:
    profiles = []
    for a in range(129):
        for b in range(129 - a):
            square_mass = 4 * a + b
            if not 0 < square_mass <= 66:
                continue
            # The proved prize floor is S>=18 when b>0; the pure-even
            # branch has the separately proved a>=15 floor.
            if not ((b > 0 and square_mass >= 18) or (b == 0 and a >= 15)):
                continue
            value = weight(a, b)
            if value:
                profiles.append((value, a, b, square_mass))
    return sorted(profiles, reverse=True)


def main() -> None:
    profiles = eligible_profiles()
    assert len(profiles) == 271
    observed = tuple(
        ((a, b, square_mass), value, 2 * EDGE_CAP // value)
        for value, a, b, square_mass in profiles[: len(EXPECTED)]
    )
    assert observed == EXPECTED

    for _, value, cap in EXPECTED:
        assert value * cap <= 2 * EDGE_CAP
        assert value * (cap + 1) > 2 * EDGE_CAP

    # The first profile is already proved empty. The next four entries are
    # exactly the remaining S=18 payoff ladder; after all five are absent,
    # the first S=20 profile is the maximum live weight.
    assert EXPECTED[1][0] == (3, 6, 18) and EXPECTED[1][2] == 93962
    assert EXPECTED[2][0] == (2, 10, 18) and EXPECTED[2][2] == 106111
    assert EXPECTED[5][0] == (4, 4, 20) and EXPECTED[5][2] == 249314

    dag = json.loads((ROOT / "dag.json").read_text())
    nodes = {node["id"]: node for node in dag["nodes"]}
    assert nodes["e1_low_square_mass_weighted_kernel_dictionary"]["status"] == "PROVED"
    assert nodes["e1_prize_n256_s18_profile_exclusion"]["status"] == "PROVED"
    assert nodes["e1_official_low_square_mass_pair_budget"]["status"] == "TARGET"

    print(
        "E1_PROFILE_WEIGHT_PAYOFF_LADDER_PASS "
        "eligible=271 current_cap=93962 after_profile_36=106111 "
        "after_all_s18=249314 adjacent_checks=12"
    )


if __name__ == "__main__":
    main()
