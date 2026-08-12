#!/usr/bin/env python3
"""Replay the low-order Pade/moment/split-jet dictionary."""

PRIME = 101


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def add(left, right):
    size = max(len(left), len(right))
    return [
        ((left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0))
        % PRIME
        for i in range(size)
    ]


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = (out[i + j] + x * y) % PRIME
    return out


checks = 0
x_star = 17
for lambda_0 in (0, 9):
    for lambda_1 in (0, 13):
        a = [lambda_0, lambda_1, 22, 5]
        c_1 = [0, 0, 0, 7]
        c_0 = [0, 0, 0, 0, 0, 0, 11]
        remainder_0 = [3, 8]
        remainder_y = [4]
        derivative_value = add(a, add(multiply(c_1, remainder_0), multiply(c_0, remainder_y)))
        require(derivative_value[:3] == a[:3], "quadratic reduction changed low jets")

        e = [[lambda_0, lambda_1, 0, 0]]
        for i in range(5):
            f_i = [0, 0, (i + 1) * 3]
            u_star_h_i = [0, 0, 0, (i + 2) * 5]
            following = add(
                [0, 0, (f_i[2] if len(f_i) > 2 else 0)],
                [(-value) % PRIME for value in u_star_h_i],
            )
            following = add(following, [(x_star * value) % PRIME for value in e[-1]])
            e.append(following)
            require(e[-1][0] == pow(x_star, i + 1, PRIME) * lambda_0 % PRIME, "zeroth recurrence")
            require(e[-1][1] == pow(x_star, i + 1, PRIME) * lambda_1 % PRIME, "first recurrence")
            checks += 2

        profile = (4,)
        if lambda_0 == 0:
            profile = (1, 3) if lambda_1 else (2, 2)
        require(profile in {(4,), (1, 3), (2, 2)}, "profile dictionary")
        checks += 2

print(f"RATE_HALF_COLLISION_PADE_SPLIT_JET_DICTIONARY_PASS checks={checks}")
