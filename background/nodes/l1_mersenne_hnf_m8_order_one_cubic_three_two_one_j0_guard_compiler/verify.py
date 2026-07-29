#!/usr/bin/env python3
"""Symbolic source checker for the J-zero exact guard compiler."""

from pathlib import Path

import sympy as sp


NODE_ID = (
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_j0_guard_compiler"
)
DEPENDENCIES = (
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_generic_fully_"
    "proportional_exceptional_e_j0_role_p4_compiler",
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_common_quadratic_compiler",
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_scaled_quadratic_core_compiler",
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_coefficient_matrix_router",
    "l1_mersenne_hnf_m8_order_one_cubic_three_two_one_j0_outer_lift_compiler",
)


def main() -> None:
    root = Path(__file__).resolve().parents[3]
    dag = (root / "dag.json").read_text()
    statement = (Path(__file__).parent / "statement.md").read_text()
    assert f'"id": "{NODE_ID}"' in dag
    assert '"status": "PROVED"' in dag[dag.index(f'"id": "{NODE_ID}"') :]
    for dependency in DEPENDENCIES:
        assert f'"from": "{dependency}"' in dag
        assert dependency in statement

    X, A, Y, x, V, S, eta, d = sp.symbols("X A Y x V S eta d", nonzero=True)
    beta, gamma = sp.symbols("beta gamma", nonzero=True)
    qhat = X**2 + (x + Y) * X + V
    ghat = sp.expand(qhat * (X - Y))
    fhat = sp.expand(ghat + A * qhat + S)
    lhat = sp.expand(fhat * ghat)
    qy = sp.expand(qhat.subs(X, Y))
    role_r = sp.expand(A * qy)
    lam = (eta + 1) / eta

    a = A / d
    b_value = eta * role_r / d**3
    q_unscaled_y = qy / d**2
    saturation = sp.factor(a * b_value * (lam - 1) * q_unscaled_y)
    assert sp.simplify(saturation - role_r**2 / d**6) == 0

    disc_q = sp.discriminant(qhat, X)
    disc_f = sp.discriminant(fhat, X)
    disc_g = sp.discriminant(ghat, X)
    resultant = sp.resultant(ghat, fhat, X)
    assert sp.factor(disc_g - disc_q * qy**2) == 0
    assert sp.factor((resultant - lam * S**3).subs(S, eta * role_r)) == 0
    assert sp.degree(lhat, X) == 6
    assert disc_f != 0

    lam_colors = (gamma - 1) / (beta - 1)
    eta_colors = (beta - 1) / (gamma - beta)
    assert sp.factor(1 + 1 / eta_colors - lam_colors) == 0
    for anchor in (
        "a B (lambda-1) Q(y)=R_j^2/d^6",
        "D_Q*D_F!=0",
        "Lhat(-1)!=0",
        "G_alg*G_fib*G_split!=0",
        "separate global inner lift",
    ):
        assert anchor in statement
    print("L1_M8_H7_C321_J0_GUARD_COMPILER_PASS")


if __name__ == "__main__":
    main()
