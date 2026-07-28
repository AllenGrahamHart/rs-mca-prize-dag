#!/usr/bin/env python3
"""Square mass, not swap distance, is the collision invariant for E1 folding.

Everything here is derived from the definitions pinned in
`e1_prime_field_l2_norm_collision_radius`:

    (a,b,c) = numbers of opposite-sign antipodal pairs, singleton terms,
              and same-sign antipodal pairs,
    alpha   = sum_{i<h} c_i zeta^i,      S = sum_i c_i^2,
    s       = |B\\B'| = |B'\\B|,
    |Norm(alpha)| <= S^(h/2),  and if b = 0 then alpha = 2 beta with
    |Norm(beta)| <= s^(h/2).

Checks:

 1. the coordinate identities  S = 4a + b  and  s = a + b/2 + c, validated
    against all four pinned first-band profiles and their pinned band indices;
 2. that same-sign antipodal pairs cancel in alpha, so c is invisible to the
    norm -- the padding construction that makes s unbounded at fixed norm;
 3. the pinned exclusion cutoffs reproduce exactly (s<=4 at N=256, s=1 at
    N=512) when expressed through S;
 4. a full enumeration of band s=5 at N=256 returns exactly the pinned
    survivors {(3,4,0), (4,2,0)};
 5. the S=16 split inventory, and which split the census campaign covers;
 6. mutation controls.
"""

from __future__ import annotations

import math

THRESHOLD_BITS = 250          # every live pair-feasible prime is >= 2^250
LANES = {256: 128, 512: 256}  # N -> h

# (a, b, c) -> (N, pinned band index s) for the four first-surviving profiles
PINNED = {
    (3, 4, 0): (256, 5),
    (4, 2, 0): (256, 5),
    (1, 2, 0): (512, 2),
    (0, 4, 0): (512, 2),
}

CENSUS_PROFILE = (3, 4)       # the (a,b) split the 74-node campaign works


def square_mass(a: int, b: int) -> int:
    """S = sum c_i^2.  Opposite-sign pairs give |c_i|=2, singletons |c_i|=1,
    same-sign pairs cancel to c_i=0 and contribute nothing."""
    return 4 * a + b


def swap_distance(a: int, b: int, c: int) -> int:
    """2s = number of differing raw positions = 2a + b + 2c."""
    return a + b // 2 + c


def norm_excluded(a: int, b: int, c: int, h: int) -> bool:
    """True when the pinned norm bound puts this profile below 2^250."""
    if b == 0:                                    # alpha = 2 beta branch
        s = swap_distance(a, b, c)
        return s == 0 or (h / 2) * math.log2(s) < THRESHOLD_BITS
    S = square_mass(a, b)
    return S == 0 or (h / 2) * math.log2(S) < THRESHOLD_BITS


def main() -> None:
    checks = 0

    # --- 1. coordinate identities against every pinned profile -------------
    for (a, b, c), (N, s_pinned) in PINNED.items():
        assert swap_distance(a, b, c) == s_pinned, ((a, b, c), s_pinned)
        assert b % 2 == 0, "b must be even: 2s = 2a + b + 2c"
        checks += 2
    assert square_mass(3, 4) == 16 and square_mass(4, 2) == 18
    assert square_mass(1, 2) == 6 and square_mass(0, 4) == 4
    checks += 4

    # --- 2. c is invisible: padding keeps S fixed while s grows ------------
    a, b = CENSUS_PROFILE
    base_S = square_mass(a, b)
    seen_s = set()
    for c in range(0, 60):
        assert square_mass(a, b) == base_S, "padding changed the square mass"
        seen_s.add(swap_distance(a, b, c))
        checks += 1
    assert len(seen_s) == 60 and max(seen_s) - min(seen_s) == 59, \
        "padding did not move the swap distance"
    # so no bound on s can follow from a bound on the norm
    assert norm_excluded(a, b, 0, 128) == norm_excluded(a, b, 59, 128)

    # --- 3. the pinned cutoffs, reproduced through S ------------------------
    # N=256: opposite-sign-only profiles are excluded exactly up to s=4
    n256_cut = max(s for s in range(1, 40)
                   if (128 / 2) * math.log2(4 * s - 2) < THRESHOLD_BITS)
    assert n256_cut == 4, n256_cut
    n512_cut = max(s for s in range(1, 40)
                   if (256 / 2) * math.log2(4 * s - 2) < THRESHOLD_BITS)
    assert n512_cut == 1, n512_cut
    # and the square-mass floors those cutoffs correspond to
    assert math.ceil(2 ** (2 * THRESHOLD_BITS / 128)) == 15
    assert math.ceil(2 ** (2 * THRESHOLD_BITS / 256)) == 4
    checks += 4

    # --- 4. full enumeration of band s=5 at N=256 ---------------------------
    survivors = set()
    enumerated = 0
    for a in range(0, 6):
        for c in range(0, 6):
            b = 2 * (5 - a - c)
            if b < 0:
                continue
            enumerated += 1
            if not norm_excluded(a, b, c, 128):
                survivors.add((a, b, c))
    assert enumerated == 21, enumerated
    assert survivors == {(3, 4, 0), (4, 2, 0)}, survivors
    checks += 2

    # --- 5. the S=16 split inventory ---------------------------------------
    splits = []
    for a in range(4, -1, -1):
        b = 16 - 4 * a
        if b < 0 or b % 2:
            continue
        splits.append((a, b, norm_excluded(a, b, 0, 128)))
    assert [(a, b) for a, b, _ in splits] == [(4, 0), (3, 4), (2, 8), (1, 12), (0, 16)]
    excluded_splits = [(a, b) for a, b, ex in splits if ex]
    live_splits = [(a, b) for a, b, ex in splits if not ex]
    assert excluded_splits == [(4, 0)], excluded_splits
    assert live_splits == [(3, 4), (2, 8), (1, 12), (0, 16)], live_splits
    assert CENSUS_PROFILE in live_splits
    uncovered = [p for p in live_splits if p != CENSUS_PROFILE]
    assert uncovered == [(2, 8), (1, 12), (0, 16)], uncovered
    checks += 4

    # --- 6. mutation controls ----------------------------------------------
    # (a) wrong square-mass formula breaks the pinned band reconstruction
    assert not all(square_mass(a, b) == 4 * a + 2 * b
                   for (a, b, _) in PINNED)
    # (b) if same-sign pairs did NOT cancel, band s=5 would gain survivors
    def bad_excluded(a, b, c, h):
        S = 4 * a + b + 4 * c                     # pretend c contributes
        return S == 0 or (h / 2) * math.log2(S) < THRESHOLD_BITS
    bad_surv = {(a, 2 * (5 - a - c), c)
                for a in range(6) for c in range(6)
                if 2 * (5 - a - c) >= 0 and not bad_excluded(a, 2 * (5 - a - c), c, 128)}
    assert bad_surv != survivors, "mutation did not change the survivor set"
    checks += 2

    print(
        "E1_COLLISION_SQUARE_MASS_REPARAMETRIZATION_PASS "
        f"pinned_profiles={len(PINNED)} band5_enumerated={enumerated} "
        f"band5_survivors={sorted(survivors)} "
        f"n256_cut=s<={n256_cut} n512_cut=s<={n512_cut} "
        f"S_floor_n256=15 S16_live_splits={live_splits} "
        f"census_covers={CENSUS_PROFILE} uncovered={uncovered} checks={checks}"
    )


if __name__ == "__main__":
    main()
