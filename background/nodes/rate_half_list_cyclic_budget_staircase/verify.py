#!/usr/bin/env python3
"""Exact verifier for rate_half_list_cyclic_budget_staircase.

Checks, in exact integer arithmetic:
  - parent-theorem hypothesis admissibility at the official row for every
    dyadic quotient order N_0 in {8,...,256} at d=1, s=c-1;
  - the six printed Lambda(N_0) values (exact ceiling binomials);
  - strict monotonicity of Lambda and strict decrease of the agreement;
  - the budget-interval partition (each B* below the cap has a unique best
    tier, and the printed interval endpoints are exact);
  - the N_0=8 tier recovers the 3n/4-1 predecessor and the N_0=256 tier
    recovers the banked cap-uniform agreement k+2^34-1.
"""
from __future__ import annotations

from math import comb


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


N = 2**41
K = 2**40

EXPECTED = {
    8: 3,
    16: 313,
    32: 8_286_954,
    64: 13_449_656_337_410_111,
    128: 90_680_420_711_626_756_043_662_381_605_286_945,
    256: 11_092_230_961_998_080_258_863_221_315_535_829_014_398_723_445_840_079_610_908_300_691_051_869_570,
}


def lam(order: int) -> int:
    return (comb(order - 1, order // 2 + 1) + order - 1) // order


def agreement(order: int) -> int:
    return K + 2 * N // order - 1


def main() -> None:
    orders = sorted(EXPECTED)
    for order in orders:
        c = N // order
        require((N // 2) % c == 0, f"c does not divide n/2 at N_0={order}")
        require(c >= 2, f"s=c-1 needs c>=2 at N_0={order}")
        require(1 <= order // 2 - 1, f"d=1 out of range at N_0={order}")
        require(lam(order) == EXPECTED[order],
                f"Lambda mismatch at N_0={order}: {lam(order)}")
        require(agreement(order) == K + 2 * N // order - 1,
                f"agreement formula at N_0={order}")

    for a, b in zip(orders, orders[1:]):
        require(lam(a) < lam(b), f"Lambda not increasing {a}->{b}")
        require(agreement(a) > agreement(b), f"agreement not decreasing {a}->{b}")

    require(agreement(8) == 3 * N // 4 - 1, "N_0=8 tier is not 3n/4-1")
    require(agreement(16) == 5 * N // 8 - 1, "N_0=16 tier is not 5n/8-1")
    require(agreement(256) == K + 2**34 - 1, "N_0=256 tier is not k+2^34-1")
    require(lam(256) > 2**242 > 2**128, "cap-uniform tier margin")

    # Budget-interval partition: best tier = smallest N_0 with B* < Lambda.
    boundaries = [1] + [lam(o) for o in orders[:-1]] + [2**128]
    for i, order in enumerate(orders):
        lo, hi = boundaries[i], boundaries[i + 1] - 1
        require(lo <= hi, f"empty interval at N_0={order}")
        for b_star in (lo, hi):
            best = next(o for o in orders if b_star < lam(o))
            require(best == order,
                    f"tier selection fails at B*={b_star}: got {best}, want {order}")
    # Spot endpoints named in the statement.
    require(boundaries[1] == 3 and boundaries[2] == 313
            and boundaries[3] == 8_286_954, "printed interval endpoints")

    print("RATE_HALF_LIST_CYCLIC_BUDGET_STAIRCASE_PASS",
          f"tiers={len(orders)}",
          f"agreements={[agreement(o) for o in orders]}")


if __name__ == "__main__":
    main()
