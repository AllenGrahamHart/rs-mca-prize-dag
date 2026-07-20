#!/usr/bin/env python3
"""Exact light checks for the WCL fixed-divisor straight-line lift."""

import sympy as sp


NODE = "dli_wcl_fixed_divisor_straight_line_lift"
P = 65537
SLOTS = (
    ("1,5", 256, 5, 3),
    ("1,6", 256, 6, 5),
    ("2,7", 512, 7, 4),
    ("4,9", 1024, 9, 4),
)


def trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(left, right, p=P):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out)


def add(left, right, p=P):
    out = [0] * max(len(left), len(right))
    for i in range(len(out)):
        out[i] = ((left[i] if i < len(left) else 0)
                  + (right[i] if i < len(right) else 0)) % p
    return trim(out)


def monic_divmod(poly, modulus, p=P):
    assert modulus[-1] % p == 1
    work = [coefficient % p for coefficient in poly]
    w = len(modulus) - 1
    quotient = [0] * max(1, len(work) - w)
    for degree in range(len(work) - 1, w - 1, -1):
        coefficient = work[degree] % p
        quotient[degree - w] = coefficient
        for j in range(w + 1):
            work[degree - w + j] = (
                work[degree - w + j] - coefficient * modulus[j]
            ) % p
    return trim(quotient), trim(work[:w])


def polynomial_from_roots(roots, p=P):
    value = [1]
    for root in roots:
        value = mul(value, [(-root) % p, 1], p)
    return value


def transcript(modulus, m, p=P):
    w = len(modulus) - 1
    value = [0, 1]
    rows = []
    for _ in range(m):
        square = mul(value, value, p)
        quotient, remainder = monic_divmod(square, modulus, p)
        assert len(quotient) <= w - 1
        assert len(remainder) <= w
        assert add(mul(modulus, quotient, p), remainder, p) == square
        rows.append((value, quotient, remainder))
        value = remainder
    return rows


def pruned_transcript(modulus, m, p=P):
    w = len(modulus) - 1
    s = (w - 1).bit_length() - 1
    value = [0] * (1 << s) + [1]
    rows = []
    for _ in range(s, m):
        square = mul(value, value, p)
        quotient, remainder = monic_divmod(square, modulus, p)
        assert len(quotient) <= w - 1
        assert len(remainder) <= w
        assert add(mul(modulus, quotient, p), remainder, p) == square
        rows.append((value, quotient, remainder))
        value = remainder
    return rows


def size_checks():
    expected = {
        "1,5": (75, 77),
        "1,6": (93, 94),
        "2,7": (121, 124),
        "4,9": (174, 179),
    }
    for name, n, w, base_variables in SLOTS:
        m = n.bit_length() - 1
        assert 1 << m == n
        variables = base_variables + m * (2 * w - 1)
        equations = m * (2 * w - 1) + w
        assert (variables, equations) == expected[name]


def pruned_size_checks():
    expected = {
        "1,5": (2, 6, 52, 54),
        "1,6": (2, 6, 65, 66),
        "2,7": (2, 7, 88, 91),
        "4,9": (3, 7, 114, 119),
    }
    for name, n, w, base_variables in SLOTS:
        m = n.bit_length() - 1
        s = (w - 1).bit_length() - 1
        assert (1 << s) < w <= (1 << (s + 1))
        k = m - s
        variables = base_variables + k * (2 * w - 1) - w
        equations = k * (2 * w - 1)
        assert (s, k, variables, equations) == expected[name]


def symbolic_shape_checks():
    y = sp.symbols("y")
    shapes = []

    c0, c1, b = sp.symbols("c0 c1 b")
    A = y**2 + c1 * y + c0
    shapes.append((y * A**2 - (b * y + 1) ** 2, (c0, c1, b), 5))

    e0, e1, e2, b0, b1 = sp.symbols("e0 e1 e2 b0 b1")
    E = y**3 + e2 * y**2 + e1 * y + e0
    B = b1 * y + b0
    shapes.append((E**2 - y * B**2, (e0, e1, e2, b0, b1), 6))

    c0, c1, c2, b = sp.symbols("d0 d1 d2 db")
    A = y**3 + c2 * y**2 + c1 * y + c0
    shapes.append((y * A**2 - (b * y + 1) ** 2, (c0, c1, c2, b), 7))

    c0, c1, c2, c3 = sp.symbols("a0 a1 a2 a3")
    A = y**4 + c3 * y**3 + c2 * y**2 + c1 * y + c0
    shapes.append((y * A**2 - 1, (c0, c1, c2, c3), 9))

    for expression, variables, w in shapes:
        poly = sp.Poly(expression, y)
        assert poly.degree() == w and poly.LC() == 1
        for coefficient in poly.all_coeffs():
            assert sp.Poly(coefficient, *variables).total_degree() <= 2


def cubic_equation_check():
    y = sp.symbols("y")
    c0, c1, b = sp.symbols("c0 c1 b")
    v = sp.symbols("v0:5")
    vn = sp.symbols("n0:5")
    q = sp.symbols("q0:4")
    A = y**2 + c1 * y + c0
    G = y * A**2 - (b * y + 1) ** 2
    V = sum(v[j] * y**j for j in range(5))
    VN = sum(vn[j] * y**j for j in range(5))
    Q = sum(q[j] * y**j for j in range(4))
    equations = sp.Poly(sp.expand(V**2 - VN - G * Q), y)
    variables = (c0, c1, b) + v + vn + q
    coefficients = [equations.nth(j) for j in range(9)]
    assert len(coefficients) == 9
    assert max(sp.Poly(item, *variables).total_degree()
               for item in coefficients) == 3


def finite_field_transcripts():
    assert pow(3, (P - 1) // 2, P) == P - 1
    signatures = []
    for name, n, w, _ in SLOTS:
        omega = pow(3, (P - 1) // n, P)
        assert pow(omega, n, P) == 1
        assert pow(omega, n // 2, P) == P - 1
        roots = [pow(omega, j, P) for j in range(w)]
        modulus = polynomial_from_roots(roots)
        rows = transcript(modulus, n.bit_length() - 1)
        pruned = pruned_transcript(modulus, n.bit_length() - 1)
        assert rows[-1][2] == [1]
        assert pruned[-1][2] == [1]
        assert pruned == rows[(w - 1).bit_length() - 1:]
        signatures.append((name, tuple(modulus), len(rows), len(pruned)))
    assert len({item[1] for item in signatures}) == 4
    return signatures


def main():
    size_checks()
    pruned_size_checks()
    symbolic_shape_checks()
    cubic_equation_check()
    signatures = finite_field_transcripts()
    print(
        "DLI_WCL_FIXED_DIVISOR_STRAIGHT_LINE_LIFT_PASS "
        f"slots={len(signatures)} recurrences={sum(item[2] for item in signatures)} "
        f"pruned={sum(item[3] for item in signatures)} "
        "max_degree=3"
    )


if __name__ == "__main__":
    main()
