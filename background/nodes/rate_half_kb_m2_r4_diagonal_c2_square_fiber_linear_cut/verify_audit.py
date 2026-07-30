#!/usr/bin/env python3
"""Independent exact-rational audit of the c=2 minor factorization."""

from fractions import Fraction as F

from verify import compose, evaluation_matrices, rank


def main() -> None:
    quotient = [[-3, 1, 0], [-2, 0, 1]]
    for epsilon, dimensions in ((1, (4, 6)), (-1, (3, 5))):
        u, v = evaluation_matrices(epsilon, 2)
        combined = []
        u_cut = compose(quotient, u)
        v_cut = compose(quotient, v)
        for row in u_cut:
            combined.append(row + [0] * len(v[0]))
        for row in v_cut:
            combined.append([0] * len(u[0]) + row)
        assert rank(combined) == 4
        assert len(combined[0]) - rank(combined) == dimensions[0]

        u_zero, _ = evaluation_matrices(epsilon, 0)
        ramified_cut = compose(quotient, u_zero)
        assert rank(ramified_cut) == 2
        assert len(u_zero[0]) + len(v[0]) - rank(ramified_cut) == dimensions[1]

    # For reciprocal chi=W^2-sW+1, the three claimed linear quotients
    # satisfy the two reciprocal minor identities coefficient by coefficient.
    s, a, b, c = F(5, 2), F(7, 3), F(-4, 5), F(11, 7)
    chi = [F(1), -s, F(1)]

    def mul(x, y):
        out = [F(0)] * (len(x) + len(y) - 1)
        for i, left in enumerate(x):
            for j, right in enumerate(y):
                out[i + j] += left * right
        return out

    m12 = mul(chi, [b, a])
    m01 = mul(chi, [-a, -b])
    m02 = mul(chi, [-c, c])
    assert m01 == [-value for value in reversed(m12)]
    assert m02 == [-value for value in reversed(m02)]

    print(
        "RATE_HALF_KB_M2_R4_DIAGONAL_C2_SQUARE_FIBER_LINEAR_CUT_AUDIT_PASS "
        "constraint_rank=4 ramified_rank=2 reciprocal_minor_relations=2"
    )


if __name__ == "__main__":
    main()
