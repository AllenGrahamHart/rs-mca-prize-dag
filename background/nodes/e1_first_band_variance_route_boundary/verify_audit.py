#!/usr/bin/env python3
"""Independent exact-rational reconstruction of the E1 route boundary."""

from __future__ import annotations

from fractions import Fraction as Q


# Transcribed independently from the pinned certificate implementation.
H = (
    (Q(48735, 79507), Q(30772, 79507), Q(-3445, 1849)),
    (Q(4788, 79507), Q(-4788, 79507), Q(301253, 1475502)),
    (Q(-213, 79507), Q(213, 79507), Q(-4243, 737751)),
    (Q(2, 79507), Q(-2, 79507), Q(71, 1475502)),
)
DEN = 2544224
THRESHOLDS = {68: 1947, 66: 1732, 64: 1517, 62: 1302, 60: 1087, 50: 13}


def log_interval(x: Q, terms: int = 53) -> tuple[Q, Q]:
    y = (x - 1) / (x + 1)
    lower = 2 * sum((y ** (2*j + 1) / (2*j + 1) for j in range(terms)), Q(0))
    first = 2 * terms + 1
    tail = 2 * y**first / (first * (1 - y*y))
    return lower, lower + tail


L2 = log_interval(Q(2))
L87 = log_interval(Q(8, 7))
L6457 = log_interval(Q(64, 57))


def coeffs(v: int, m3: int, basis=H, m3_v_slope: int = 48) -> tuple[Q, Q, Q, Q]:
    moments = (Q(1), Q(16), Q(256 + v), Q(4096 + m3_v_slope*v + m3))
    f = tuple(sum((moments[i] * basis[i][j] for i in range(4)), Q(0)) for j in range(3))
    c = Q(-7488*v + 128*m3 - 270521, DEN)
    return c, f[0], f[1], f[2]


def margins(v: int, m3: int, **kw) -> tuple[Q, Q]:
    c, a, b, d = coeffs(v, m3, **kw)
    assert c < 0 and a > 0 and b > 0
    lower = c*L2[1] + a*L87[0] + b*L6457[0] - d
    upper = c*L2[0] + a*L87[1] + b*L6457[1] - d
    return lower, upper


def pinned(v: int, m3: int, **kw) -> bool:
    return margins(v, m3, **kw)[0] > 0 and margins(v, m3 + 1, **kw)[1] < 0


def main() -> None:
    # Affineness is checked by vanishing mixed and second finite differences.
    for coordinate in range(4):
        f00 = coeffs(40, 100)[coordinate]
        f10 = coeffs(42, 100)[coordinate]
        f20 = coeffs(44, 100)[coordinate]
        f01 = coeffs(40, 101)[coordinate]
        f11 = coeffs(42, 101)[coordinate]
        assert f20 - 2*f10 + f00 == 0
        assert f11 - f10 - f01 + f00 == 0

    # A direct interval for one M3 step proves strict decrease.
    step_c, step_a, step_b, step_d = (
        coeffs(40, 101)[i] - coeffs(40, 100)[i] for i in range(4)
    )
    step_upper = step_c*L2[1] + step_a*L87[1] + step_b*L6457[0] - step_d
    step_lower = step_c*L2[0] + step_a*L87[0] + step_b*L6457[1] - step_d
    assert step_lower <= step_upper < 0

    assert all(pinned(v, m3) for v, m3 in THRESHOLDS.items())
    dead = [v for v in range(2, 49, 2) if margins(v, 0)[1] < 0]
    assert dead == list(range(2, 49, 2))

    # Independently bound the affine boundary slope by finite differences.
    dv = tuple(coeffs(42, 100)[i] - coeffs(40, 100)[i] for i in range(4))
    dv_lower = dv[0]*L2[1] + dv[1]*L87[0] + dv[2]*L6457[0] - dv[3]
    dv_upper = dv[0]*L2[0] + dv[1]*L87[1] + dv[2]*L6457[1] - dv[3]
    # dv is for two units of V; -step is for one unit of M3.
    slope_lower = dv_lower / (2 * -step_lower)
    slope_upper = dv_upper / (2 * -step_upper)
    assert Q(107) < slope_lower <= slope_upper < Q(108)

    bad_basis = (H[0], H[1], H[2], (H[3][0], H[3][1], H[3][2] + Q(1, 1475502)))
    assert not any(pinned(v, m3, basis=bad_basis) for v, m3 in THRESHOLDS.items())
    assert not any(pinned(v, m3, m3_v_slope=47) for v, m3 in THRESHOLDS.items())

    print("E1_FIRST_BAND_VARIANCE_ROUTE_BOUNDARY_AUDIT_PASS terms=53 thresholds=6 dead_levels=24 slope_in=(107,108) mutations=2")


if __name__ == "__main__":
    main()
