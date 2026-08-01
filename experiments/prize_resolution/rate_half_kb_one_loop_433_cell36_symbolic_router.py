#!/usr/bin/env python3
"""Symbolic two-variable router for one-loop 433 cells 3 and 6."""

import argparse

import sympy as sp


def branch(epsilon_1, epsilon_2):
    t, r, b, c = sp.symbols("t r b c")
    iota = sp.I
    labels = (1, t**2, -1, r**2, -r**2)
    products = (-1, b, c, b*c, -b*c)
    sums = (0, 1+b, 1+c, b+c, b-c)
    roots = (1, t, epsilon_1*iota, r, epsilon_2*iota*r)
    q_values = tuple(root*edge_sum for root, edge_sum in zip(roots, sums))
    rows = [[-product, -product*label, 1, label]
            for product, label in zip(products, labels)]
    product_equations = [
        sp.expand(sp.det(sp.Matrix([rows[0], rows[1], rows[2], rows[index]])))
        for index in (3, 4)
    ]
    q_equations = []
    for third in (3, 4):
        left, right = 1, 2
        dl = products[0]-products[left]
        dr = products[0]-products[right]
        dk = products[0]-products[third]
        value = (
            q_values[left]*dr*dk*(labels[third]-labels[right])
            +q_values[right]*dl*dk*(labels[left]-labels[third])
            +q_values[third]*dl*dr*(labels[right]-labels[left])
        )
        q_equations.append(sp.cancel(
            value/((b+1)*(c+1)*(t-epsilon_1*iota))
        ))

    capital_r = r**2
    c_value = -(
        b*(capital_r**2+1)+2*capital_r
    )/(
        b*(capital_r**2+1+2*capital_r*b)
    )
    routed_q = []
    for index, value in enumerate(q_equations):
        numerator = sp.cancel(value.subs(c, c_value)).as_numer_denom()[0]
        factor = b-1 if index == 0 else b+1
        routed_q.append(sp.cancel(numerator/factor))
    compatibility = sp.factor(
        sp.resultant(routed_q[0], routed_q[1], t), extension=iota
    )

    x = sp.symbols("x")
    first_product = sp.Poly(product_equations[0], t)
    product_x = sum(
        coefficient*x**(power[0]//2)
        for power, coefficient in first_product.terms()
    )
    routed_product = sp.cancel(product_x.subs(c, c_value))
    x_value = sp.factor(
        -routed_product.subs(x, 0)/sp.diff(routed_product, x)
    )
    q_coefficient = sp.diff(routed_q[0], t)
    q_constant = routed_q[0].subs(t, 0)
    t_value = sp.factor(-q_constant/q_coefficient, extension=iota)
    square_equation = sp.factor(
        sp.cancel(t_value**2-x_value).as_numer_denom()[0],
        extension=iota,
    )
    return compatibility, square_equation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epsilon-1", type=int, choices=(-1, 1), required=True)
    parser.add_argument("--epsilon-2", type=int, choices=(-1, 1), required=True)
    arguments = parser.parse_args()
    compatibility, square_equation = branch(
        arguments.epsilon_1, arguments.epsilon_2
    )
    print(f"compatibility={compatibility}", flush=True)
    print(f"square_equation={square_equation}", flush=True)


if __name__ == "__main__":
    main()
