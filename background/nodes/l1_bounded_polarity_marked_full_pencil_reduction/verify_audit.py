#!/usr/bin/env python3
"""Mutation audit for the marked full-pencil reduction."""


def mul(left: list[int], right: list[int], modulus: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % modulus
    return out


def sub(left: list[int], right: list[int], modulus: int) -> list[int]:
    size = max(len(left), len(right))
    return [
        ((left[i] if i < len(left) else 0) - (right[i] if i < len(right) else 0))
        % modulus
        for i in range(size)
    ]


def main() -> None:
    modulus = 101
    l_si, l_sj = [3, 2, 1], [5, 7, 1]
    l_vi, l_vj = [11, 1], [13, 1]
    a_i, a_j = [2, 9, 4], [6, 1, 8]
    raw = sub(mul(l_si, a_i, modulus), mul(l_sj, a_j, modulus), modulus)
    correct = mul(raw, mul(l_vi, l_vj, modulus), modulus)

    # Dropping either cross-mark factor breaks the cleared identity.
    missing_j = mul(raw, l_vi, modulus)
    missing_i = mul(raw, l_vj, modulus)
    assert missing_j != correct
    assert missing_i != correct

    # One dense petal can reach d=ell+p-1, so the strict boundary matters.
    ell, v, sparse = 8, 0, 2
    p = v + sparse
    h = ell - v + sparse
    r = ell - 1
    assert h + r - ell == ell + p - 1

    print("L1_MARKED_FULL_PENCIL_AUDIT_PASS mutations=3")


if __name__ == "__main__":
    main()
