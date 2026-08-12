#!/usr/bin/env python3
"""Replay the divided-row Cauchy closed form over two finite fields."""


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def trim(poly):
    out = [value % PRIME for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def add(left, right):
    size = max(len(left), len(right))
    return trim([
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(size)
    ])


def scale(poly, scalar):
    return trim([scalar * value for value in poly])


def multiply(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return trim(out)


def inverse(value):
    return pow(value % PRIME, PRIME - 2, PRIME)


def product(values):
    answer = 1
    for value in values:
        answer = answer * value % PRIME
    return answer


def run_fixture(prime):
    global PRIME
    PRIME = prime
    e = 7
    p = (3 * e - 1) // 2
    n_0 = 3 * p - 2
    d = 2 * p - 1
    degree_x = p - 3
    source = list(range(1, n_0 + 1))
    x_star = n_0 + 9
    tau = 0
    gamma = n_0 + 3
    a_q = 7

    s_b = [0, 0, 1]
    g_star = [(-gamma) % PRIME, 1]
    h_nr = multiply(g_star, s_b)
    t_2 = [3, 4, 1]
    g_heavy = multiply(h_nr, t_2)
    q_heavy = scale(multiply(g_star, multiply(s_b, multiply(s_b, s_b))), a_q)
    lambda_form = multiply(multiply([1, 1], [2, 1]), [3, 1])

    def k_value(y):
        answer = [0]
        power = 1
        for degree in range(degree_x):
            coefficient = [degree + 2, y + degree + 1, 2 * degree + 1]
            answer = add(answer, scale(coefficient, power))
            power = power * y % PRIME
        return answer

    def g_value(y):
        return add(g_heavy, scale(k_value(y), y - x_star))

    l_at_star = product(x_star - y for y in source)
    l_prime = {
        y: product(y - z for z in source if z != y)
        for y in source
    }
    omega = {y: [y + 2, 2 * y + 1] for y in source}
    source_product = {
        y: scale(multiply(lambda_form, g_value(y)), inverse(l_prime[y]))
        for y in source
    }

    checks = 0
    previous_d = None
    previous_c = None
    for i in range(d + 1):
        d_i = [0]
        h_i = [0]
        f_i = [0]
        for y in source:
            y_power = pow(y, i, PRIME)
            d_i = add(
                d_i,
                scale(omega[y], y_power * inverse(x_star - y)),
            )
            h_i = add(h_i, scale(omega[y], y_power))
            divided_value = scale(
                add(source_product[y], scale(multiply(omega[y], q_heavy), -1)),
                inverse(y - x_star),
            )
            f_i = add(f_i, scale(divided_value, y_power))

        c_i = add(
            scale(
                multiply(lambda_form, t_2),
                -pow(x_star, i, PRIME) * inverse(l_at_star),
            ),
            scale(multiply(multiply(s_b, s_b), d_i), a_q),
        )
        require(f_i == multiply(h_nr, c_i), "Cauchy closed form")
        require(len(c_i) - 1 <= 5, "quintic degree")
        checks += 2

        if previous_d is not None:
            require(d_i == add(scale(previous_d, x_star), scale(previous_h, -1)),
                    "Cauchy recurrence")
            require(c_i == add(scale(previous_c, x_star),
                               scale(multiply(multiply(s_b, s_b), previous_h), -a_q)),
                    "quintic recurrence")
            checks += 2
        previous_d = d_i
        previous_h = h_i
        previous_c = c_i

        correction_value = c_i[0] % PRIME
        expected = (
            pow(x_star, i, PRIME)
            * scale(multiply(lambda_form, t_2), -inverse(l_at_star))[0]
        ) % PRIME
        require(correction_value == expected, "geometric correction value")
        checks += 1

    require(tau not in source and x_star not in source, "fixture separation")
    return checks + 1


total = sum(run_fixture(prime) for prime in (101, 127))
print(f"RATE_HALF_COLLISION_QUINTIC_CAUCHY_CLOSED_FORM_PASS checks={total}")
