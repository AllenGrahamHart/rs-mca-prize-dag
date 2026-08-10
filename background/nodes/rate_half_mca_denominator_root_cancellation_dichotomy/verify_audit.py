#!/usr/bin/env python3
from itertools import product


for p in (3, 5, 7):
    for dimension in (1, 2, 3):
        vectors = product(range(p), repeat=2 * dimension)
        for packed in vectors:
            u = packed[:dimension]
            v = packed[dimension:]
            compatible = [
                gamma
                for gamma in range(p)
                if all((a + gamma * b) % p == 0 for a, b in zip(u, v))
            ]
            if any(v):
                assert len(compatible) <= 1
            else:
                assert compatible == list(range(p)) if not any(u) else compatible == []

# Concrete puncture-trivialization example: P={0}, k=2, m=3, gamma=1.
# On S'={1,2}, p0=p1=h=0 explains the puncture. At P the defects are
# u=-1 and v=1, so u+gamma*v=0 while v is nonzero.
p = 11
gamma = 1
u = (-1) % p
v = 1
assert (u + gamma * v) % p == 0
assert v != 0

print("PASS independent pole-defect slope-recovery audit fields=3 dimensions=1..3")
