#!/usr/bin/env python3
from itertools import product


def canonical(valid):
    return min(valid) if valid else None


universe = (0, 1, 2)
certificates = ((z, payload) for z in universe for payload in range(3))
certificates = tuple(certificates)
checked = 0

for mask in product((0, 1), repeat=len(certificates)):
    valid = {cert for cert, bit in zip(certificates, mask) if bit}
    projected = {z for z in universe if any(cert[0] == z for cert in valid)}
    selected = {
        canonical(sorted(cert for cert in valid if cert[0] == z))
        for z in projected
    }
    assert None not in selected
    assert {cert[0] for cert in selected} == projected
    assert len(selected) == len(projected)
    assert all(sum(cert[0] == z for cert in selected) == 1 for z in projected)
    checked += 1

assert checked == 512
print(f"PASS independent selector audit finite_relations={checked} max_raw_fiber=3 selected_fiber=1")
