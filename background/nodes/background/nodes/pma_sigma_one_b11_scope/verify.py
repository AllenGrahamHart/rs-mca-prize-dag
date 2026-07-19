#!/usr/bin/env python3
"""Exact official-grid replay of the sigma-one B11 route theorem."""

from math import comb, isqrt


CHECKS = 0


def check(label, condition):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1


def floor_root4(value):
    root = isqrt(isqrt(value))
    while (root + 1) ** 4 <= value:
        root += 1
    while root**4 > value:
        root -= 1
    return root


def owner(d, slack, slack_j, g2, gr, v2=2):
    if d > 2:
        return "GROW"
    if slack >= slack_j:
        return "J"
    if g2 <= v2:
        return "A2"
    if gr <= 0:
        return "AR"
    return "RES"


ppm_ranges = {den: [] for den in (2, 4, 8, 16)}
for exponent in range(13, 45):
    n = 1 << exponent
    for denominator in (2, 4, 8, 16):
        k = n // denominator
        ell = 2
        petals = (n - k) // 2
        background = n - (k - 1) - ell * petals
        check("maximal sigma-one decomposition", background == 1)

        radicand = n * (k - 1)
        root = isqrt(radicand)
        check("Johnson starts above k+1", (k + 1) ** 2 <= radicand)
        slack_j = root - k
        delta = (root + 1) ** 2 - radicand
        check("exact Johnson threshold", (k + slack_j) ** 2 <= radicand < (k + slack_j + 1) ** 2)
        check("positive Johnson denominator", delta > 0)

        seen = set()
        for d in range(5):
            for slack in (max(0, slack_j - 1), slack_j, slack_j + 1):
                for g2 in range(3):
                    for gr in range(1, 4):
                        cell = owner(d, slack, slack_j, g2, gr)
                        seen.add(cell)
                        if d <= 2:
                            check("bounded defect paid", cell in {"J", "A2"})
                        else:
                            check("large defect is GROW", cell == "GROW")
        check("collapsed cells", seen == {"J", "A2", "GROW"})

        coefficient = 11 * comb(petals, 2)
        check("two-anchor specialization", sum(comb(4, v) for v in range(3)) == 11)
        check("background anchor vanishes", comb(background, ell) == 0)

        fit_numerator = delta * n**6 - n * (n - k + 1)
        check("positive generous allowance", fit_numerator > 0)
        fit_power = fit_numerator // (delta * coefficient)
        q_fit = floor_root4(fit_power)
        check("fourth-root lower boundary", delta * coefficient * q_fit**4 + n * (n - k + 1) <= delta * n**6)
        check("fourth-root upper boundary", delta * coefficient * (q_fit + 1) ** 4 + n * (n - k + 1) > delta * n**6)
        ppm_ranges[denominator].append(q_fit * 1_000_000 // n)

        if denominator in (8, 16):
            check("low-rate field ceiling below domain minimum", q_fit < n + 1)
            check("A2 certificate alone exceeds n^6", coefficient * (n + 1) ** 4 > n**6)
        else:
            check("high-rate near-minimal field can fit generous ceiling", q_fit >= n + 1)

# Mutation: V_2=1 leaves a genuine RES state at d=2 below Johnson.
check("V2 mutation exposes RES", owner(2, 0, 1, 2, 1, v2=1) == "RES")

for denominator in (2, 4, 8, 16):
    values = ppm_ranges[denominator]
    print(
        f"rate=1/{denominator}: q_fit/n ppm range "
        f"[{min(values)},{max(values)}]"
    )

print(f"PMA sigma-one B11 scope: PASS ({CHECKS} checks, 128 official rows)")
