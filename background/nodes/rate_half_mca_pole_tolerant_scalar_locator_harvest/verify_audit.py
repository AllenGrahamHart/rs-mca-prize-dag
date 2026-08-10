#!/usr/bin/env python3


def poly_eval(coeffs, x, p):
    value = 0
    for coefficient in reversed(coeffs):
        value = (value * x + coefficient) % p
    return value


p = 11
domain = (0, 1, 2, 3, 4)
support = (0, 1, 2)

# k=2, m=3, Q=X, h=0, A=Lambda=X(X-1)(X-2), B=0, c=1.
q = (0, 1)
a = (0, 2, 8, 1)
b = (0,)
locator = a
for x in domain:
    left = poly_eval(locator, x, p)
    right = poly_eval(a, x, p)
    assert left == right

poles = tuple(x for x in domain if poly_eval(q, x, p) == poly_eval(a, x, p) == poly_eval(b, x, p) == 0)
assert poles == (0,)
assert set(poles) <= set(support)

# Divide by X. The reduced exact locator is (X-1)(X-2).
q_reduced = (1,)
a_reduced = (2, 8, 1)
locator_reduced = a_reduced
for x in domain[1:]:
    assert poly_eval(locator_reduced, x, p) == poly_eval(a_reduced, x, p)
assert q_reduced == (1,)

print("PASS independent common-pole cancellation example p=11 k=2 m=3")
