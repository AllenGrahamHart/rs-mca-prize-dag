#!/usr/bin/env python3
"""Exact F_17 replay of the full Hankel contact order."""


P_FIELD = 17
Y_0 = (1, 10, 16, 2, 14, 0, 3, 11)
Y_1 = (0, 14, 9, 7, 13, 12, 15, 0)
Q_0 = (7, 0, 9, 1)
Q_1 = (0, 12, 4, 0)
RHO = 3


def polymul(first, second):
    out = [0] * (len(first) + len(second) - 1)
    for i, x in enumerate(first):
        for j, y in enumerate(second):
            out[i + j] = (out[i + j] + x * y) % P_FIELD
    return out


def main():
    tails = []
    for t in range(P_FIELD):
        y = [(a + t * b) % P_FIELD for a, b in zip(Y_0, Y_1)]
        q = [(a + t * b) % P_FIELD for a, b in zip(Q_0, Q_1)]
        product = polymul(list(reversed(q)), y)
        assert product[RHO : 2 * RHO + 2] == [0] * (RHO + 2)
        tails.append(product[2 * RHO + 2])

    assert any(tails)
    assert len(set(tails)) > 1

    mutated_q_1 = list(Q_1)
    mutated_q_1[1] = (mutated_q_1[1] + 1) % P_FIELD
    mutation_detected = False
    for t in range(P_FIELD):
        y = [(a + t * b) % P_FIELD for a, b in zip(Y_0, Y_1)]
        q = [(a + t * b) % P_FIELD for a, b in zip(Q_0, mutated_q_1)]
        product = polymul(list(reversed(q)), y)
        if any(product[RHO : 2 * RHO + 2]):
            mutation_detected = True
            break
    assert mutation_detected

    print(
        "RATE_HALF_CA_HANKEL_CLEAN_ENDPOINT_PICARD_FORNEY_CONTACT_EXCLUSION_AUDIT_PASS "
        f"fixture=F17_m1 parameters={P_FIELD} contact_order={2 * RHO + 2}"
    )


if __name__ == "__main__":
    main()
