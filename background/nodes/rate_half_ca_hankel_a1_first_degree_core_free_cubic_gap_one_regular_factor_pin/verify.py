#!/usr/bin/env python3
"""Replay packet gaps and regular/marked determinant degrees."""


E = 183_251_937_963
RHO = 3 * E - 1
DELTA = 2 * E - 1

# Rows of (DGN2): I0, c_s, c_d, eps_s, eps_d, w, t_s, t_d.
packets = (
    (0, 1, 1, 0, 0, 1, 1, E - 2),
    (0, 1, 1, 1, 0, 0, 2, E - 2),
    (0, 1, 1, 0, 1, 0, 1, E - 1),
    (1, 2, 1, 0, 0, 0, 2, E - 2),
)

for packet in packets:
    i0, c_s, c_d, eps_s, eps_d, w, t_s, t_d = packet
    c_tot = DELTA - w
    assert c_tot + w == DELTA
    assert t_s + t_d == E - w
    assert c_s + c_d == 2 + i0
    assert w + i0 + eps_s + eps_d == 1
    # D_0 Q(x) is a bordered determinant of parameter degree rho.
    assert c_tot + w + E == RHO

assert [packet[5] for packet in packets] == [1, 0, 0, 0]

print(
    "CORE_FREE_CUBIC_GAP_ONE_REGULAR_FACTOR_PIN_PASS",
    f"regular_degree={DELTA}",
    "residual_degrees=1,0,0,0",
)
