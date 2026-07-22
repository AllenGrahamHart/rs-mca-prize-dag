#!/usr/bin/env python3
"""Mutation guards for the ambient-prime HGE4 contraction."""


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


mutations = 0
for s in range(13, 42):
    for r in range(4, s + 1):
        m = 1 << r
        cutoff = 2 * ceil_div(m * r, 8 * s)

        # Lowering the cutoff by one loses the floor(h/2) exponent.
        previous = cutoff - 1
        assert 2 * s * (previous // 2) < r * m // 4
        mutations += 1

        # The level-local mutation removes every proper-level gain.
        local_cutoff = 2 * ceil_div(m * r, 8 * r)
        assert local_cutoff == m // 4
        if r < s and cutoff < m // 4:
            mutations += 1

# At the largest row the first two nontrivial complete deletions are real.
s = 41
assert 2 * ceil_div((1 << 5) * 5, 8 * s) <= 4
assert 2 * ceil_div((1 << 6) * 6, 8 * s) <= 4
assert 2 * ceil_div((1 << 7) * 7, 8 * s) > 4
mutations += 3

# Exact parity ripple: even h=34 passes while the following odd width does
# not, so replacing the per-width predicate by an unproved suffix is false.
s, r = 13, 8
n, m = 1 << s, 1 << r
def exact_gate(h: int) -> bool:
    u_h = h // 2
    v_h = (h - 1) // 2 + 2
    return n ** (2 * u_h) >= (4 * h - v_h) ** (m // 4)

assert exact_gate(34)
assert not exact_gate(35)
assert exact_gate(36)
mutations += 3

print("F3_HGE4_AMBIENT_NORM_LEVEL_CONTRACTION_AUDIT_PASS", mutations)
