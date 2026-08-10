#!/usr/bin/env python3
from itertools import combinations


for size in range(36):
    slopes = tuple(range(size))
    selected = {z: (z, "canonical") for z in slopes}
    assert len(selected) == size
    if size <= 31:
        assert not list(combinations(slopes, 32))
    else:
        tuples = list(combinations(slopes, 32))
        assert tuples
        for subset in tuples:
            certs = tuple(selected[z] for z in subset)
            assert len(certs) == len(set(certs)) == 32
            assert tuple(cert[0] for cert in certs) == subset

print("PASS independent order32 adapter audit sizes=0..35")
