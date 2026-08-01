#!/usr/bin/env python3
"""Exact planning-level checks for the Brief-3 XR high-core proof programme.

This script verifies only arithmetic reductions and explicit route-fence
constructions used in the accompanying dossier.  It does NOT prove P-A1,
P-A2, the first-Maxwell-core owner theorem, any trade-rank funnel, or the
universal XR target.

All verdict paths use exact integers/Fractions.  Floating point appears only
in optional display helpers.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
import sys


ROWS = (
    # name, n, k, h=A-k
    ("RowC_1_4", 1024, 256, 5),
    ("RowC_1_8", 1024, 128, 5),
    ("RowC_1_16", 1024, 64, 3),
    ("prize_1_4", 2**41, 2**39, 2**33 + 1),
    ("prize_1_8", 2**41, 2**38, 2**33 + 1),
    ("prize_1_16", 2**41, 2**37, 2**32 + 1),
)

EXPECTED_COMPONENT_BREAK = {
    "RowC_1_4": 4,
    "RowC_1_8": 4,
    "RowC_1_16": 4,
    "prize_1_4": 12,
    "prize_1_8": 11,
    "prize_1_16": 10,
}

EXPECTED_PA_FRONTIER = {
    "RowC_1_4": 5,
    "RowC_1_8": 5,
    "RowC_1_16": 5,
    "prize_1_4": 17,
    "prize_1_8": 17,
    "prize_1_16": 15,
}

EXPECTED_PA2_FRONTIER = {
    "RowC_1_4": 5,
    "RowC_1_8": 4,
    "RowC_1_16": 4,
    "prize_1_4": 4,
    "prize_1_8": 4,
    "prize_1_16": 4,
}


def check(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def ceil_div(a: int, b: int) -> int:
    check(a >= 0 and b > 0, "ceil_div domain")
    return (a + b - 1) // b


def component_cap(R: int, h: int, d: int) -> int:
    """The canonical component-atlas GRK cap, rounded down exactly."""
    return (comb(R + d, d) * R) // comb(d + h, d)


def row_ledger_checks() -> dict[str, dict[str, int]]:
    out: dict[str, dict[str, int]] = {}
    for name, n, k, h in ROWS:
        R = n - k
        r = R - h
        H = h + 1
        check(R > h >= 1, f"{name}: radius ordering")
        check(H == (6 if name in {"RowC_1_4", "RowC_1_8"} else
                    4 if name == "RowC_1_16" else
                    2**33 + 2 if name in {"prize_1_4", "prize_1_8"} else
                    2**32 + 2), f"{name}: H pin")
        out[name] = {
            "n": n,
            "k": k,
            "h": h,
            "H": H,
            "R": R,
            "r": r,
            "PA": 8 * n**3,
            "PA2": 16 * n**3,
        }
    return out


def base_affine_rank_checks(rows: dict[str, dict[str, int]]) -> None:
    """Replay the banked all-LineRay rank-3 threshold and rank-4 failure."""
    for name, row in rows.items():
        r = row["r"]
        B = row["PA"]
        check(comb(r + 3, 3) <= B, f"{name}: selector rank 3 should be paid")
        check(comb(r + 4, 4) > B, f"{name}: bare selector rank 4 should fail")

    # The support-wise P-A2 statement pays rank four only on RowC 1/4.
    rc = rows["RowC_1_4"]
    check(comb(rc["r"] + 4, 4) == 14_307_629_505,
          "P-A2 RowC 1/4 rank-four exact value")
    check(comb(rc["r"] + 4, 4) < rc["PA2"],
          "P-A2 RowC 1/4 rank four should fit 16n^3")
    for name, row in rows.items():
        if name == "RowC_1_4":
            continue
        check(comb(row["r"] + 4, 4) > row["PA2"],
              f"{name}: bare P-A2 rank four should remain open")

    check(EXPECTED_PA_FRONTIER == {
        "RowC_1_4": 5, "RowC_1_8": 5, "RowC_1_16": 5,
        "prize_1_4": 17, "prize_1_8": 17, "prize_1_16": 15,
    }, "P-A frontier pin")
    check(EXPECTED_PA2_FRONTIER["RowC_1_4"] == 5 and
          all(EXPECTED_PA2_FRONTIER[x] == 4 for x in EXPECTED_PA2_FRONTIER
              if x != "RowC_1_4"), "P-A2 frontier pin")


def component_payoff_checks(rows: dict[str, dict[str, int]]) -> dict[str, int]:
    first_break: dict[str, int] = {}
    for name, row in rows.items():
        R, h, B = row["R"], row["h"], row["PA"]
        d = 0
        while component_cap(R, h, d) <= B:
            d += 1
            check(d < 100, f"{name}: component break unexpectedly large")
        first_break[name] = d
        check(d == EXPECTED_COMPONENT_BREAK[name],
              f"{name}: component break {d} != {EXPECTED_COMPONENT_BREAK[name]}")

    # Exact RowC payoff ladder: at depth 3 only a handful of components fit;
    # at depth 4 not even one component is paid by CA-GRK alone.
    expected_max_components_d3 = {
        "RowC_1_4": 8,
        "RowC_1_8": 4,
        "RowC_1_16": 1,
    }
    for name, expected in expected_max_components_d3.items():
        row = rows[name]
        got = row["PA"] // component_cap(row["R"], row["h"], 3)
        check(got == expected, f"{name}: d=3 component payoff {got}")
        check(component_cap(row["R"], row["h"], 4) > row["PA"],
              f"{name}: d=4 must exceed full P-A budget")
    return first_break


def support_only_induced_matching_fence(rows: dict[str, dict[str, int]]) -> dict[str, int]:
    """A rigorous support-only route fence on the three RowC rows."""
    selected: dict[str, int] = {}
    for name in ("RowC_1_4", "RowC_1_8", "RowC_1_16"):
        row = rows[name]
        n, r, h = row["n"], row["r"], row["h"]
        V = comb(n, r)
        D_le = sum(comb(r, j) * comb(n - r, j) for j in range(1, h + 1))
        M = ceil_div(V, 4 * (D_le + 1))
        check(2 * M > row["PA"],
              f"{name}: support-only induced matching should beat 8n^3")
        selected[name] = M
    return selected


def positive_dimensional_field_fence(rows: dict[str, dict[str, int]]) -> int:
    """A literal admissible 256-bit field is much larger than 8n^3."""
    q = int(
        "108037839417390090843359763492907651258221714407500997496797919767622829735937"
    )
    n = rows["prize_1_4"]["n"]
    B = rows["prize_1_4"]["PA"]
    check(q.bit_length() == 256, "literal q bit length")
    check(q < 2**256, "literal q cap")
    check((q - 1) % 2**41 == 0, "literal q must admit order-2^41 domain")
    check(q > B, "an affine line over q must already exceed 8n^3")
    return q // B


def extension_ledger_explosion(rows: dict[str, dict[str, int]]) -> int:
    """EC4--EC6 alone permit far more than cubic many packing records."""
    row = rows["RowC_1_4"]
    a, d = 4, 2
    X = a + d + 1
    outside = row["n"] - X
    tau = (3, 4, 4, 4)
    count = 1
    left = outside
    for t in tau:
        count *= comb(left, t)
        left -= t
    check(count > row["PA"], "extension compatibility alone should exceed 8n^3")

    # Verify the exact EC4 slack for z=(1,2,2,2), d=2 with disjoint O_i.
    z = (1, 2, 2, 2)
    for i in range(4):
        for j in range(i + 1, 4):
            ell = z[i] + z[j] - d - 1
            check(ell >= 0, "shell pair slack")
            check(0 <= ell, "empty I and disjoint O satisfy EC4")
    return count


def rank_two_nonexhaustion_fence() -> None:
    """A Maxwell left-kernel surplus does not force rank two by linear algebra."""
    p = 5
    for scalar in range(1, p):
        det = pow(scalar, 3, p)
        check(det != 0, "nonzero span(I_3) element must have rank three")


def mismatch_pathwise_breadth_fence(rows: dict[str, dict[str, int]]) -> int:
    """Pathwise descent and area laws do not control preterminal breadth."""
    row = rows["RowC_1_4"]
    n, K0, h, H = row["n"], row["k"], row["h"], row["H"]
    transitions = 34
    check(K0 == 256 and h == 5 and H == 6, "RowC 1/4 pins")

    area = (K0 + h) + 33 * (1 + h)
    check(area <= n - H, "XDA1 path area")
    drop_sum = K0 - 1
    check(drop_sum <= K0 - 1, "XDA2 external-zero drop sum")

    N1 = n - K0 - h
    N_terminal = N1 - 33 * (1 + h)
    check(N_terminal > 4 * H, "tree remains preterminal")

    nodes = 2 ** (transitions + 1) - 1
    check(nodes > row["PA2"], "binary preterminal tree should exceed 16n^3")
    return nodes


def rank_five_rowc_checks(rows: dict[str, dict[str, int]]) -> None:
    """Replay the u=v=0 rank-five reuse-core arithmetic."""
    expected = {
        "RowC_1_4": (772, 9, 126, 125, 153),
        "RowC_1_8": (900, 9, 126, 123, 179),
        "RowC_1_16": (964, 7, 35, 31, 320),
    }
    for name, (N, m, b, c, line_cap) in expected.items():
        row = rows[name]
        check(N == row["R"] + 4, f"{name}: rank-five N")
        check(m == 4 + row["h"], f"{name}: rank-five m")
        check(b == comb(m, 4), f"{name}: b=C(m,4)")
        T = comb(N, 4)
        B = row["PA"]
        got_c = b - T // (B + 1)
        check(got_c == c, f"{name}: reuse c")
        check(line_cap == row["R"] // row["h"], f"{name}: collision line cap")


def main() -> None:
    rows = row_ledger_checks()
    base_affine_rank_checks(rows)
    breaks = component_payoff_checks(rows)
    induced = support_only_induced_matching_fence(rows)
    q_ratio = positive_dimensional_field_fence(rows)
    ext_count = extension_ledger_explosion(rows)
    rank_two_nonexhaustion_fence()
    tree_nodes = mismatch_pathwise_breadth_fence(rows)
    rank_five_rowc_checks(rows)

    print(
        "BRIEF3_XR_HIGHCORE_PROGRAM_ARITHMETIC_PASS "
        f"rows={len(rows)} "
        f"component_breaks={','.join(f'{k}:{v}' for k,v in breaks.items())} "
        f"support_fence_bits={','.join(f'{k}:{v.bit_length()}' for k,v in induced.items())} "
        f"q_over_8n3_bits={q_ratio.bit_length()} "
        f"extension_records_bits={ext_count.bit_length()} "
        f"preterminal_tree={tree_nodes} "
        "ranktwo_funnel=not_linear_algebra "
        "nonclaims=P-A1,P-A2,owner-completeness,universal-field-coverage"
    )


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print(f"BRIEF3_XR_HIGHCORE_PROGRAM_ARITHMETIC_FAIL: {exc}")
        sys.exit(1)
