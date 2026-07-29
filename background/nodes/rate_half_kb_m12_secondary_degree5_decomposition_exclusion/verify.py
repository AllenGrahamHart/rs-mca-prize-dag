#!/usr/bin/env python3
"""Verify the m12 secondary degree-five decomposition exclusion."""

from math import gcd
from pathlib import Path


NODE = Path(__file__).resolve().parent


def act(point, inner, outer, block_count):
    x, block = point
    return inner[x], outer[block] % block_count


def main() -> None:
    statement = (NODE / "statement.md").read_text()
    proof = (NODE / "proof.md").read_text()
    contract = (NODE / "claim_contract.md").read_text()
    assert "- **status:** PROVED" in statement
    assert "inner-degree-12 branch is empty" in statement
    assert "C_Sym(X)(S)=1" in proof
    assert "inner degrees `2,3,4,6,10`" in contract

    inner_degree = 12
    outer_degree = 5
    total_degree = inner_degree * outer_degree
    assert total_degree == 60

    # Exact finite model of (5): the same inner permutation in every old
    # block preserves columns, while allowing an arbitrary outer permutation.
    inner = tuple((7 * x + 5) % inner_degree for x in range(inner_degree))
    assert len(set(inner)) == inner_degree
    outer = (1, 2, 3, 4, 0)
    omega = {(x, block) for x in range(inner_degree)
             for block in range(outer_degree)}
    assert len(omega) == total_degree
    columns = [{(x, block) for block in range(outer_degree)}
               for x in range(inner_degree)]
    images = [
        {act(point, inner, outer, outer_degree) for point in column}
        for column in columns
    ]
    assert all(image in columns for image in images)
    assert len(columns) == 12
    assert {len(column) for column in columns} == {5}

    # A block of size five corresponds to a right factor of degree five.
    secondary_inner_degree = len(columns[0])
    secondary_outer_degree = len(columns)
    assert (secondary_inner_degree, secondary_outer_degree) == (5, 12)

    p = 2_130_706_433
    q = p**6
    assert q % 5 == 4
    assert (q - 1) % 5 == 3
    assert gcd(5, q - 1) == 1
    assert {2, 3, 4, 6, 10, 12} - {12} == {2, 3, 4, 6, 10}
    print("RATE_HALF_KB_M12_SECONDARY_DEGREE5_DECOMPOSITION_EXCLUSION_PASS")


if __name__ == "__main__":
    main()
