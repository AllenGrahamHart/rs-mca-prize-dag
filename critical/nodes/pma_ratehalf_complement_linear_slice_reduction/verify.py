#!/usr/bin/env python3
"""Verify the PMA complement-divisor linear-slice correspondence."""

from __future__ import annotations

from itertools import combinations
from pathlib import Path
import importlib.util


NODE = "pma_ratehalf_complement_linear_slice_reduction"
ROOT = Path(__file__).resolve().parents[3]
SOURCE = (
    ROOT
    / "background"
    / "nodes"
    / "pma_ratehalf_two_petal_support_fiber_reduction"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("pma_support_fiber_base", SOURCE)
assert SPEC is not None and SPEC.loader is not None
support = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(support)
cross = support.cross
aligned = support.aligned
base = support.base


def rank_mod(matrix: list[list[int]], p: int) -> int:
    rows = [[entry % p for entry in row] for row in matrix]
    if not rows:
        return 0
    nrows, ncols = len(rows), len(rows[0])
    rank = 0
    for column in range(ncols):
        pivot = next(
            (row for row in range(rank, nrows) if rows[row][column]), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, p)
        rows[rank] = [(entry * inverse) % p for entry in rows[rank]]
        for row in range(nrows):
            if row == rank or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [
                (left - factor * right) % p
                for left, right in zip(rows[row], rows[rank])
            ]
        rank += 1
        if rank == nrows:
            break
    return rank


def coefficient(poly: list[int], index: int) -> int:
    return poly[index] if index < len(poly) else 0


def slice_rank(
    etilde: list[int], modulus: list[int], ell: int, a: int, p: int
) -> tuple[int, int, int]:
    images = []
    for exponent in range(2 * ell):
        monomial = [0] * exponent + [1]
        image = support.residue(base.mul(monomial, etilde, p), modulus, p)
        images.append([coefficient(image, row) for row in range(2 * ell)])
    multiplication = [
        [images[column][row] for column in range(2 * ell)]
        for row in range(2 * ell)
    ]
    high = multiplication[ell - a + 1 :]
    d = 2 * ell - a
    truncated_rank = rank_mod([row[: d + 1] for row in high], p)
    return (
        rank_mod(multiplication, p),
        rank_mod(high, p),
        d + 1 - truncated_rank,
    )


def exact_fixture() -> dict[str, int]:
    data = cross.setup()
    factors = cross.numerator_factors(data)
    p = int(data["p"])
    ell = int(data["ell"])
    b = int(data["b"])
    a = 1
    m = 2 * ell + b + a - 2
    l1, l2, l3 = list(data["l_petals"])
    modulus = base.mul(l2, l3, p)
    core = list(data["core"])

    checked = 0
    guarded = 0
    unit_checks = 0
    complement_mutations = 0
    cutoff_mutations = 0
    exactness_mutations = 0
    for lambda_value in range(2, p):
        e_c, p_star, y_poly = cross.source_pair(data, (0, 1, lambda_value))
        etilde, remainder = aligned.divmod_poly(e_c, l1, p)
        assert remainder == [0] and base.degree(etilde) < 2 * ell
        f_lambda, remainder = aligned.divmod_poly(p_star, l1, p)
        assert remainder == [0]
        assert base.mul(list(data["l_core"]), etilde, p) == base.add(
            f_lambda, base.mul(modulus, y_poly, p), p
        )
        assert aligned.gcd_poly(etilde, modulus, p) == [1]
        full_rank, high_rank, truncated_dimension = slice_rank(
            etilde, modulus, ell, a, p
        )
        assert full_rank == 2 * ell
        assert high_rank == ell + a - 1
        assert truncated_dimension == ell - 2 * a + 2
        unit_checks += 1

        for subset in combinations(core, m):
            row = support.support_candidate(
                data, factors, subset, lambda_value, a=a
            )
            divisor, remainder = aligned.divmod_poly(
                list(data["l_core"]), list(row["l_s"]), p
            )
            assert remainder == [0] and base.degree(divisor) == 2 * ell - a
            v_atom = support.residue(base.mul(divisor, etilde, p), modulus, p)
            slice_ok = base.degree(v_atom) <= ell - a
            exact = aligned.gcd_poly(v_atom, divisor, p) == [1]
            old_guard = bool(row["target"] and row["degree_ok"] and row["exact"])
            new_guard = slice_ok and exact
            assert old_guard == new_guard
            if slice_ok:
                assert v_atom == row["v"]
                assert row["target"] and row["degree_ok"]
            if new_guard:
                h_old = support.reconstruct(data, factors, row, lambda_value)
                numerator = base.sub(
                    base.mul(list(row["l_s"]), v_atom, p), f_lambda, p
                )
                h_new, remainder = aligned.divmod_poly(numerator, modulus, p)
                assert remainder == [0] and h_new == h_old
                assert base.degree(h_new) <= ell + b - 2
                guarded += 1

            wrong_v = support.residue(
                base.mul(list(row["l_s"]), etilde, p), modulus, p
            )
            complement_mutations += int(wrong_v != v_atom)
            cutoff_mutations += int(
                not slice_ok and base.degree(v_atom) <= ell - a + 1
            )
            exactness_mutations += int(slice_ok and not exact)
            checked += 1

    assert checked == (p - 2) * 35
    assert guarded > 0
    assert complement_mutations > 0
    assert cutoff_mutations > 0
    hostile = support.hostile_guard_search()
    assert hostile["exactness_witness"]

    # The distinct-label hypothesis is load-bearing for the unit assertion.
    e_zero, _, _ = cross.source_pair(data, (0, 1, 0))
    etilde_zero, remainder = aligned.divmod_poly(e_zero, l1, p)
    assert remainder == [0]
    assert aligned.gcd_poly(etilde_zero, modulus, p) != [1]
    return {
        "lambdas": unit_checks,
        "supports": checked,
        "guarded": guarded,
        "complement_mutations": complement_mutations,
        "cutoff_mutations": cutoff_mutations,
        "exactness_mutations": exactness_mutations
        + int(bool(hostile["exactness_witness"])),
        "hostile_layouts": int(hostile["layouts"]),
    }


def tail_arithmetic() -> tuple[int, int, int, int, int, int]:
    ell, b, a = 11, 7, 1
    d = 2 * ell - a
    slice_dimension = ell - a + 1
    codimension = ell + a - 1
    assert (d, slice_dimension, codimension) == (21, 11, 11)
    sample_a = 3
    sample_ambient = ell - sample_a + 1
    sample_truncated = ell - 2 * sample_a + 2
    assert (sample_ambient, sample_truncated) == (9, 7)
    return ell, d, slice_dimension, codimension, sample_ambient, sample_truncated


def main() -> None:
    fixture = exact_fixture()
    ell, d, dimension, codimension, sample_ambient, sample_truncated = (
        tail_arithmetic()
    )
    print(
        f"{NODE}_PASS lambdas={fixture['lambdas']} "
        f"supports={fixture['supports']} guarded={fixture['guarded']} "
        f"complement_mutations={fixture['complement_mutations']} "
        f"cutoff_mutations={fixture['cutoff_mutations']} "
        f"exactness_mutations={fixture['exactness_mutations']} "
        f"hostile_layouts={fixture['hostile_layouts']} "
        f"tail_ell={ell} tail_d={d} slice_dim={dimension} codim={codimension} "
        f"a3_dims={sample_ambient}/{sample_truncated}"
    )


if __name__ == "__main__":
    main()
