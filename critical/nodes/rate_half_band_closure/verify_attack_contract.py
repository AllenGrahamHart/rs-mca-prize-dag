#!/usr/bin/env python3
"""Check the exact arithmetic and custody markers in the current attack plan.

This is a documentation-contract verifier. It does not prove the TARGET node.
"""

from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = ROOT / "critical/nodes/rate_half_band_closure"


def require(text: str, marker: str, source: str) -> None:
    assert marker in text, f"missing marker in {source}: {marker}"


def main() -> None:
    m = 1 << 37
    rho_a3 = 4 * m - 1

    strict_e = (m, rho_a3 // 3)
    half_a3_e = (m + 1, rho_a3 // 3)
    a1_max = {
        0: 4 * m,
        1: (4 * m - 1) // 2,
        2: (4 * m - 2) // 3,
    }

    assert strict_e == (1 << 37, ((1 << 39) - 1) // 3)
    assert half_a3_e[0] == strict_e[0] + 1
    assert a1_max[0] == 1 << 39
    assert a1_max[1] == ((1 << 39) - 1) // 2
    assert a1_max[2] == ((1 << 39) - 2) // 3

    normalized_a = 31 * comb(30, 6)
    normalized_ab = normalized_a * comb(24, 3)
    paired = normalized_ab * 15
    assert normalized_a == 18_407_025
    assert normalized_ab == 37_255_818_600
    assert paired == 558_837_279_000

    attack = (NODE / "attack.md").read_text()
    statement = (NODE / "statement.md").read_text()
    requests = (ROOT / "notes/PRIZE_COMPUTE_REQUESTS.md").read_text()
    roadmap = (ROOT / "notes/PRIZE_RESOLUTION_ROADMAP.md").read_text()

    require(statement, "**status:** TARGET", "statement.md")
    require(attack, "B_ca^far(N-B+1)<=B", "attack.md")
    require(attack, "m<=e<=floor((4m-1)/3)", "attack.md")
    require(attack, "m+1<=e<=floor((4m-s)/(1+s))", "attack.md")
    require(attack, "cannot close either residual budget", "attack.md")
    require(attack, "It would not close this whole TARGET node", "attack.md")
    require(requests, "37,255,818,600", "PRIZE_COMPUTE_REQUESTS.md")
    # marker updated at wave-20: the pre-request was PROMOTED (the official
    # distance-three chart is theorem-closed); pin the promoted row's contract
    # language instead of the retired pre-request banner.
    require(requests, "coverage-complete symbolic compilers and measured pilots for one live face", "PRIZE_COMPUTE_REQUESTS.md")
    require(roadmap, "uniform Hankel split-pencil bound", "PRIZE_RESOLUTION_ROADMAP.md")

    print(
        "RATE_HALF_ATTACK_CONTRACT_PASS "
        f"strict_e={strict_e} half_a3_e={half_a3_e} "
        f"a1_max={a1_max} raw_ab={normalized_ab} paired={paired}"
    )


if __name__ == "__main__":
    main()
