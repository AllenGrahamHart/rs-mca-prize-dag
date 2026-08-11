#!/usr/bin/env python3
"""Replay the core-one quadratic root-router arithmetic."""


E = 183_251_937_963
DELTA = E - 2
U_MAX = (E - 1) // 5

assert U_MAX == 36_650_387_592

for u in (4, 5, U_MAX):
    v = E + 2 - u
    omission = DELTA - v
    assert omission == u - 4
    for i0 in (0, u):
        i_e = DELTA - u - i0
        assert i_e > 0
        for r in (1, 2):
            c_e = r * E - i_e
            assert c_e == (r - 1) * E + 2 + u + i0
        lower_without_eps = E + 2 - 2 * u - i0
        assert lower_without_eps > 0
        assert 3 * u + 2 * i0 <= 5 * u < E

# At the first excluded integer, the strict first-fifth implication ends.
assert 5 * (U_MAX + 1) >= E

print(
    "CORE_ONE_QUADRATIC_ROOT_MULTIPLICITY_ROUTER_PASS",
    f"e={E}",
    f"u_range=4..{U_MAX}",
)
