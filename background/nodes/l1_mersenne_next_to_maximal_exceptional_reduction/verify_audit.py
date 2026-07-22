#!/usr/bin/env python3
"""Independent companion-matrix and proof-scope audit."""

from pathlib import Path


HERE = Path(__file__).resolve().parent
ROWS = (
    (8191, 8, (64, 8127), 8100),
    (131071, 8, (130815, 130815), 109166),
    (524287, 8, (523775, 512), 454794),
    (2147483647, 8, (32768, 2147450879), 634005911),
    (8191, 16, (6456, 7379), 6763),
)


def fadd(x, y, p):
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def fmul(x, y, p):
    return ((x[0] * y[0] - x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)


def fpow(x, n, p):
    out = (1, 0)
    while n:
        if n & 1:
            out = fmul(out, x, p)
        x = fmul(x, x, p)
        n //= 2
    return out


def mmul(a, b, p):
    return tuple(tuple(fadd(fmul(a[i][0], b[0][j], p),
                             fmul(a[i][1], b[1][j], p), p)
                       for j in range(2)) for i in range(2))


def mpow(a, n, p):
    out = (((1, 0), (0, 0)), ((0, 0), (1, 0)))
    while n:
        if n & 1:
            out = mmul(out, a, p)
        a = mmul(a, a, p)
        n //= 2
    return out


def main() -> None:
    checks = 0
    for p, m, generator, xi in ROWS:
        assert fpow(generator, m, p) == (1, 0)
        assert fpow(generator, m // 2, p) != (1, 0)
        epsilon = (1, 0)
        surviving = []
        inv_xi = pow(xi, -1, p)
        a = ((1 - inv_xi) % p, 0)
        for index in range(m):
            b = (epsilon[0] * inv_xi % p, epsilon[1] * inv_xi % p)
            companion = (((0, 0), b), ((1, 0), a))
            powered = mpow(companion, p + 1, p)
            r0 = fadd(powered[0][0], (-epsilon[0] % p, -epsilon[1] % p), p)
            r1 = powered[1][0]
            if r1 == (0, 0):
                degree = 2 if r0 == (0, 0) else 0
            else:
                norm = (r1[0] * r1[0] + r1[1] * r1[1]) % p
                inv_r1 = (r1[0] * pow(norm, -1, p) % p,
                          -r1[1] * pow(norm, -1, p) % p)
                root = fmul((-r0[0] % p, -r0[1] % p), inv_r1, p)
                value = fadd(
                    fadd(fmul((xi, 0), fmul(root, root, p), p),
                         fmul(((1 - xi) % p, 0), root, p), p),
                    (-epsilon[0] % p, -epsilon[1] % p), p,
                )
                degree = 1 if value == (0, 0) else 0
            if degree:
                surviving.append((index, degree))
            epsilon = fmul(epsilon, generator, p)
        assert surviving == [(0, 1)]
        checks += m + 3

    proof = (HERE / "proof.md").read_text()
    for anchor in ("deg H<=m-1-nu", "Every distinct root", "p<=h^2",
                   "Consequently `P_y=0`", "v=(h-d-1)p-m", "q=2a(p-m)b",
                   "A'(y)", "t=e=1", "r in {0,1}", "B(R(0))=0",
                   "deg R'=p-m-1", "a_0+a_z", "equality of degrees",
                   "F=(R-r_0)/(z-r_0)", "every finite critical point",
                   "(m-3)p<=m-nu", "m-2` distinct", "degree one"):
        assert anchor in proof
        checks += 1
    print(f"L1_MERSENNE_NEXT_TO_MAXIMAL_EXCEPTIONAL_REDUCTION_AUDIT_PASS checks={checks}")


if __name__ == "__main__":
    main()
