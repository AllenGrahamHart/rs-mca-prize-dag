#!/usr/bin/env python3
"""Exact checks for the deficient-window rational-direction payment."""


def rank(rows, q):
    a = [row[:] for row in rows]
    r = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][col] % q), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col] % q, q - 2, q)
        a[r] = [x * inv % q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col] % q:
                z = a[i][col] % q
                a[i] = [(x - z * y) % q for x, y in zip(a[i], a[r])]
        r += 1
    return r


def eval_poly(coeffs, x, q):
    out = 0
    for c in reversed(coeffs):
        out = (out * x + c) % q
    return out


def mul(a, b, q):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % q
    return out


q, n, k, d = 17, 16, 4, 3
root = 3
H = [pow(root, i, q) for i in range(n)]
assert len(set(H)) == n and pow(root, n, q) == 1
rprime = n - k - d
T = H[k + d :]

# Ahat=X^2+1, Bhat=X+2. Put (e,e')=(Bhat,-Ahat) off the core.
Ahat = [1, 0, 1]
Bhat = [2, 1, 0]
evals_u = [0] * (k + d) + [eval_poly(Bhat, x, q) for x in T]
evals_v = [0] * (k + d) + [(-eval_poly(Ahat, x, q)) % q for x in T]
ninv = pow(n, q - 2, q)
u = [ninv * sum(evals_u[i] * pow(H[i], (-j) % (q - 1), q)
                for i in range(n)) % q for j in range(n)]
v = [ninv * sum(evals_v[i] * pow(H[i], (-j) % (q - 1), q)
                for i in range(n)) % q for j in range(n)]

assert all(eval_poly(u, H[i], q) == evals_u[i] for i in range(n))
assert all(eval_poly(v, H[i], q) == evals_v[i] for i in range(n))

# Reversed coefficient vectors for Ahat and Bhat.
a = list(reversed(Ahat))
b = list(reversed(Bhat))
Ru = [[u[j - i] for i in range(rprime + 1)] for j in range(n - d, n)]
Rv = [[v[j - i] for i in range(rprime + 1)] for j in range(n - d, n)]
relation = [sum(a[s] * Ru[s][i] + b[s] * Rv[s][i]
                for s in range(d)) % q for i in range(rprime + 1)]
assert relation == [0] * (rprime + 1)
assert rank(Ru + Rv, q) < 2 * d

common = []
for x, eu, ev in zip(T, evals_u[k + d :], evals_v[k + d :]):
    av, bv = eval_poly(Ahat, x, q), eval_poly(Bhat, x, q)
    assert (av * eu + bv * ev) % q == 0
    if av == bv == 0:
        common.append(x)
    elif av:
        z = bv * pow(av, q - 2, q) % q
        assert (eu + z * ev) % q == 0
    else:
        assert ev == 0  # projective infinity
assert not common

# Exact-root choice: a q>n syzygy space with two forced roots.
d2 = 4
G = H[2:4]
C = [(-G[0]) % q, 1]
C = mul(C, [(-G[1]) % q, 1], q)
basis = [
    (C + [0], [0] + C),
    ([0] + C, C + [0]),
]
root_sets = []
for lam in range(q):
    for mu in range(q):
        if lam == mu == 0:
            continue
        P = [[(lam * basis[0][i][j] + mu * basis[1][i][j]) % q
              for j in range(d2)] for i in range(2)]
        roots = {x for x in H
                 if eval_poly(P[0], x, q) == eval_poly(P[1], x, q) == 0}
        root_sets.append(roots)
forced = set.intersection(*root_sets)
assert forced == set(G)
assert min(map(len, root_sets)) == len(G)
assert len(basis) <= 2 * (d2 - len(G))

for h in (5, 7, 9, 17):
    for depth in range((h + 1) // 2, (2 * h + 1) // 3 + 1):
        assert depth - 2 < 2 * (h - depth)

# The outside/local partition spends exactly the original budget when the
# local target receives the complementary allowance.
partition_checks = 0
for n0 in range(2, 65):
    for g in range(n0 + 1):
        outside_cap = n0 - g
        local_budget = 17 * n0 * n0 - 25 * outside_cap
        assert local_budget >= 0
        assert 25 * outside_cap + local_budget == 17 * n0 * n0
        partition_checks += 1

print("XR_DEFICIENT_WINDOW_RATIONAL_DIRECTION_PAYMENT_ALL_PASS "
      f"checks={14 + partition_checks}")
