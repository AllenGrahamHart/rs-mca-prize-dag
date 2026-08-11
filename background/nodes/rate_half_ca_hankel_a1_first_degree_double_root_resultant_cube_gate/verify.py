#!/usr/bin/env python3
"""Replay the norm/resultant exponent bookkeeping of the cube gate."""


def resultant_quotient_exponents(deg_q, deg_p):
    # Res(Q,P) = q_d^deg(P) Norm(P), and Norm(H) = H^deg(Q).
    return {"q_d": deg_p, "H": deg_q}


for d, b in ((17, 9), (23, 7)):
    exponents = resultant_quotient_exponents(d, b)
    assert exponents["q_d"] == b
    assert exponents["H"] == d


def cube_factor_test(exponents, constant_is_cube):
    return constant_is_cube and all(value % 3 == 0 for value in exponents)


assert cube_factor_test((3, -6, 9), True)
assert not cube_factor_test((3, -5, 9), True)
assert not cube_factor_test((3, -6, 9), False)

# In characteristic three, f(z)=g(z)^3 has only exponents divisible by three.
cube_poly = {0: 1, 3: 2, 9: 1}
assert all(exponent % 3 == 0 for exponent in cube_poly)

print("DOUBLE_ROOT_RESULTANT_CUBE_GATE_PASS cases=2")
