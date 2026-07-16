#!/usr/bin/env python3
"""Verify the reciprocal-quadratic PMA obstruction."""

from __future__ import annotations

from itertools import combinations, permutations
from math import comb


CHECKS = 0


def check(condition: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def mul(left: list[int], right: list[int], p: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return out


def locator(roots: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for root in roots:
        out = mul(out, [(-root) % p, 1], p)
    return out


def evaluate(poly: list[int], x: int, p: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % p
    return value


def primitive_root(p: int) -> int:
    factors = []
    value = p - 1
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    for candidate in range(2, p):
        if all(pow(candidate, (p - 1) // factor, p) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def lower_numerator(n: int) -> tuple[int, int]:
    capital_n = n // 2
    petals = n // 4
    numerator = (petals - 15) * (capital_n - 6) * (capital_n - 3) * comb(petals, 5)
    return numerator, 6 * petals


# The lower bound first beats n^6 at the asserted power-of-two threshold and
# remains above it throughout the official range.
first = None
for exponent in range(6, 45):
    n = 1 << exponent
    numerator, denominator = lower_numerator(n)
    beats = numerator > denominator * n**6
    if beats and first is None:
        first = exponent
    if first is not None:
        check(beats, f"lower-bound monotonicity at 2^{exponent}")
check(first == 22, f"unexpected first exponent {first}")
check(lower_numerator(1 << 41)[0] > lower_numerator(1 << 41)[1] * (1 << 41) ** 6,
      "official rate-half row")


# Exact small-field realization of the polynomial identity and one diffuse,
# primitive source word. This is a proof-interface fixture, not asymptotic
# evidence.
p = 97
n = 32
generator = primitive_root(p)
zeta = pow(generator, (p - 1) // n, p)
domain = [pow(zeta, exponent, p) for exponent in range(n)]
group = tuple(domain[::2])
coset = tuple(domain[1::2])
r = zeta

q_value = lambda x: (pow(x, p - 2, p) + r * x) % p
check(all(q_value(x) != 0 for x in coset), "labels nonzero")
check(len({q_value(x) for x in coset}) == len(coset), "labels injective")

x_set = tuple(domain[exponent] for exponent in range(1, 16, 2))
y_set = tuple((-x) % p for x in x_set)
selected = tuple(x_set[:5])
target_product = r
for value in selected:
    target_product = target_product * value % p

defect = None
background = None
residual = None
for roots in combinations(group, 3):
    product = roots[0] * roots[1] % p * roots[2] % p
    if product != target_product:
        continue
    ld = locator(roots, p)
    ls = locator(selected, p)
    numerator = mul([1, 0, r], ld, p)
    numerator += [0] * (len(ls) - len(numerator))
    ls += [0] * (len(numerator) - len(ls))
    numerator = [(a - r * b) % p for a, b in zip(numerator, ls)]
    while numerator and numerator[-1] == 0:
        numerator.pop()
    check(numerator[0] == 0, "division by X")
    candidate = numerator[1:]
    check(len(candidate) <= 4, "residual degree")
    for b in group:
        if b not in roots and evaluate(candidate, b, p) != 0:
            defect, background, residual = roots, b, candidate
            break
    if residual is not None:
        break

check(residual is not None, "small fixture exists")
core = tuple(value for value in group if value != background)
ld = locator(defect, p)
lc_minus_d = locator(tuple(value for value in core if value not in defect), p)
codeword = mul(lc_minus_d, residual, p)
check(len(codeword) - 1 < n // 2, "source codeword degree")

found = False
for perm in permutations(y_set):
    petals = tuple(zip(x_set, perm))
    agreement = set(value for value in core if value not in defect)
    full = False
    for x, y in petals:
        label = q_value(x)
        in_petal = 0
        for value in (x, y):
            received = label * evaluate(locator(core, p), value, p) % p
            if evaluate(codeword, value, p) == received:
                agreement.add(value)
                in_petal += 1
        full |= in_petal == 2
    if evaluate(codeword, background, p) == 0:
        continue
    if full or not set(selected).issubset(agreement):
        continue
    if all((-x) % p not in agreement for x in selected):
        found = True
        break

check(found, "diffuse primitive matching fixture")
check(len(agreement) >= n // 2 + 1, "listing agreement")

print(f"PMA reciprocal-quadratic obstruction: PASS ({CHECKS} checks, first=2^{first})")
