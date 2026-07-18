#!/usr/bin/env python3
"""Replay the split-pencil factorization on the exact order-eight witness."""

from __future__ import annotations

from itertools import combinations


P = 17
DOMAIN = (1, 9, 13, 15, 16, 8, 4, 2)
POLYS = (
    (0, 0, 0, 0),
    (11, 2, 8, 7),
    (8, 5, 13, 2),
    (15, 13, 15, 13),
)
RECEIVED = (11, 0, 0, 0, 4, 0, 0, 1)


def trim(poly: tuple[int, ...]) -> tuple[int, ...]:
    answer = list(poly)
    while len(answer) > 1 and answer[-1] % P == 0:
        answer.pop()
    return tuple(value % P for value in answer)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    size = max(len(left), len(right))
    return trim(tuple(
        (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
        for i in range(size)
    ))


def negate(poly: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-value % P for value in poly)


def subtract(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return add(left, negate(right))


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] = (answer[i + j] + a * b) % P
    return trim(tuple(answer))


def product(polys: list[tuple[int, ...]]) -> tuple[int, ...]:
    answer = (1,)
    for poly in polys:
        answer = multiply(answer, poly)
    return answer


def locator(roots: list[int]) -> tuple[int, ...]:
    return product([((-root) % P, 1) for root in roots])


def divide(numerator: tuple[int, ...], denominator: tuple[int, ...]):
    work = list(trim(numerator))
    denominator = trim(denominator)
    if denominator == (0,):
        raise ZeroDivisionError
    quotient = [0] * max(1, len(work) - len(denominator) + 1)
    inverse = pow(denominator[-1], -1, P)
    while len(work) >= len(denominator) and trim(tuple(work)) != (0,):
        work = list(trim(tuple(work)))
        shift = len(work) - len(denominator)
        coefficient = work[-1] * inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(denominator):
            work[index + shift] = (work[index + shift] - coefficient * value) % P
    return trim(tuple(quotient)), trim(tuple(work))


def evaluate(poly: tuple[int, ...], x: int) -> int:
    value = 0
    for coefficient in reversed(poly):
        value = (value * x + coefficient) % P
    return value


def main() -> None:
    words = tuple(tuple(evaluate(poly, x) for x in DOMAIN) for poly in POLYS)
    supports = tuple(
        {index for index, value in enumerate(word) if value == RECEIVED[index]}
        for word in words
    )
    assert tuple(map(len, supports)) == (5, 5, 5, 5)

    triple_roots = {i: [] for i in range(4)}
    edge_roots = {edge: [] for edge in combinations(range(4), 2)}
    full_roots: list[int] = []
    singleton_roots: list[int] = []
    for coordinate, x in enumerate(DOMAIN):
        members = tuple(i for i, support in enumerate(supports) if coordinate in support)
        if len(members) == 4:
            full_roots.append(x)
        elif len(members) == 3:
            omitted = next(i for i in range(4) if i not in members)
            triple_roots[omitted].append(x)
        elif len(members) == 2:
            edge_roots[tuple(sorted(members))].append(x)
        elif len(members) == 1:
            singleton_roots.append(x)
        else:
            raise AssertionError("the exact fixture has no empty incidence")

    assert sorted(map(len, triple_roots.values())) == [1, 1, 1, 2]
    assert sorted(map(len, edge_roots.values())) == [0, 0, 0, 0, 1, 1]
    assert len(full_roots) == 0 and len(singleton_roots) == 1

    A = {i: locator(roots) for i, roots in triple_roots.items()}
    E = {edge: locator(roots) for edge, roots in edge_roots.items()}
    J = locator(full_roots)
    W = locator(singleton_roots)
    vanishing = locator(list(DOMAIN))
    assert vanishing == (P - 1,) + (0,) * 7 + (1,)
    assert product([W, J, *A.values(), *E.values()]) == vanishing

    pair_locator = {}
    B = {}
    for i, j in combinations(range(4), 2):
        k, l = tuple(index for index in range(4) if index not in (i, j))
        pair_locator[i, j] = product([J, A[k], A[l], E[i, j]])
        direct = locator([DOMAIN[x] for x in sorted(supports[i] & supports[j])])
        assert pair_locator[i, j] == direct
        difference = subtract(POLYS[j], POLYS[i])
        quotient, remainder = divide(difference, direct)
        assert remainder == (0,)
        delta = 3 - (len(direct) - 1)
        assert len(quotient) - 1 <= delta
        B[i, j] = multiply(E[i, j], quotient)

    triangles = 0
    for i, j, k in combinations(range(4), 3):
        left = add(multiply(A[k], B[i, j]), multiply(A[i], B[j, k]))
        right = multiply(A[j], B[i, k])
        assert left == right
        triangles += 1

    product_pairs = product(list(pair_locator.values()))
    left = product([product_pairs, multiply(multiply(W, W), W), *[multiply(e, e) for e in E.values()]])
    right = product([vanishing, vanishing, vanishing, J, J, J])
    assert left == right

    mutated = dict(B)
    key = next(key for key, value in mutated.items() if value != (0,))
    mutated[key] = add(mutated[key], (1,))
    assert any(
        add(multiply(A[k], mutated[i, j]), multiply(A[i], mutated[j, k]))
        != multiply(A[j], mutated[i, k])
        for i, j, k in combinations(range(4), 3)
    )

    print(
        "AUDIT_RATE_HALF_LIST_BUDGET_THREE_SPLIT_PENCIL_NORMAL_FORM_PASS "
        f"pairs={len(pair_locator)} triangles={triangles} products=2 mutation=1/1"
    )


if __name__ == "__main__":
    main()
