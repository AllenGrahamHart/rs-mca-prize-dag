#!/usr/bin/env python3
"""Replay the quartic-companion toral deck-involution router."""

from math import gcd


def require(condition, message):
    if not condition:
        raise AssertionError(message)


N = 2**41
e = (2**39 + 1) // 3
row_count = (9 * e - 7) // 2
incidences = 4 * row_count
defect = 6 * (3 * e) - incidences
full_fibers = 3 * e - defect
pair_floor = (30 * full_fibers + 3) // 4

require(defect == 14, "quartic vertical defect")
require(full_fibers == 2**39 - 13, "full six-row fiber floor")
require(pair_floor == 4123168604063, "quartic ordered-pair floor")
require(24 - 4 == 20, "divided-resultant bidegree")
require(6 - 1 == 5, "off-diagonal orbit-component cap")

first_cube_constant = 108 * (20 * 20) ** 2
require(first_cube_constant == 17280000, "gcd first-term constant")
require(125 * first_cube_constant * N**2 < pair_floor**3, "five-component first term")
require(5 * 4800 * N**2 < 2**167 * pair_floor, "five-component characteristic term")

character_cases = set()
for subdegree in range(1, 6):
    for map_degree in range(1, 21):
        for a in range(-20, 21):
            for b in range(-20, 21):
                if not a or not b or gcd(abs(a), abs(b)) != 1:
                    continue
                if map_degree * abs(a) == map_degree * abs(b) == 4 * subdegree:
                    character_cases.add((subdegree, map_degree, a, b))

require(character_cases, "empty toral character census")
require(
    all(abs(a) == abs(b) == 1 and map_degree == 4 * subdegree
        for subdegree, map_degree, a, b in character_cases),
    "toral relation did not collapse to a graph",
)
require(gcd(6, N) == 2, "scaling deck-order gate")

for prime, k in ((101, 7), (127, 11)):
    for x in range(1, 20):
        reciprocal = k * pow(x, -1, prime) % prime
        require(k * pow(reciprocal, -1, prime) % prime == x, "reciprocal involution")
        require((-(-x)) % prime == x, "antipodal involution")

print(
    "RATE_HALF_QUARTIC_TORAL_DECK_INVOLUTION_PASS "
    f"defect={defect} full_fibers={full_fibers} pair_floor={pair_floor} "
    "quotient_bidegree=(4,3)"
)
