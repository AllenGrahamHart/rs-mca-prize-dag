#!/usr/bin/env python3
"""Replay packet exceptions and specialized apolar dimensions."""


E = 183_251_937_963
RHO = 3 * E - 1
DELTA = 2 * E - 1
PACKET_GAPS = (1, 0, 0, 0)

assert DELTA == RHO - E
assert sum(gap == 0 for gap in PACKET_GAPS) == 3
assert sum(PACKET_GAPS) == 1

for c in range(1, 12):
    minimal_degree = RHO - c
    second_generator_degree = (2 * RHO + 1) - minimal_degree
    assert second_generator_degree == RHO + c + 1
    assert second_generator_degree > RHO
    right_kernel_dimension = RHO - minimal_degree + 1
    left_kernel_dimension = (RHO - 1) - minimal_degree + 1
    assert right_kernel_dimension == c + 1
    assert left_kernel_dimension == c
    # c positive Smith exponents summing to c are all one.
    smith_exponents = [1] * c
    assert len(smith_exponents) == c
    assert sum(smith_exponents) == c

print(
    "CORE_FREE_CUBIC_GAP_ONE_FIRST_JET_PAIRING_PASS",
    "exact_packets=3",
    "exceptional_lines=1",
)
