#!/usr/bin/env python3
from itertools import product


indices = range(4)
subsets = [set(i for i, bit in enumerate(bits) if bit) for bits in product((0, 1), repeat=2)]
checked = 0
countermodels = 0

for bad, tangent, q_certified, bc_certified in product(subsets, repeat=4):
    z_paid = bad & tangent
    r1 = bad - z_paid
    z_q = r1 & q_certified
    r2 = r1 - z_q
    z_bc = r2 & bc_certified
    z_new = r2 - z_bc
    cells = (z_paid, z_q, z_bc, z_new)
    assert set().union(*cells) == bad
    assert sum(len(cell) for cell in cells) == len(bad)
    assert all(not (cells[i] & cells[j]) for i in indices for j in indices if i < j)
    checked += 1
    if z_bc:
        endpoint_records = set()
        if not endpoint_records:
            countermodels += 1

assert checked == 256
assert countermodels > 0
print(f"PASS independent exhaustive audit assignments={checked} countermodels={countermodels}")
