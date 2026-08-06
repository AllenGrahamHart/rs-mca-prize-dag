#!/usr/bin/env python3
"""Verify the private-linear PGL2 normal form for h=3 rank bookkeeping."""

from __future__ import annotations

from f3_h3_rc_rank_normalization_invariance import (
    Curve,
    P,
    linear_root,
    substitution_rank,
)


def inv(x: int, p: int) -> int:
    return pow(x % p, -1, p)


def private_value(x: int, alpha: int, beta: int, p: int) -> int | None:
    den = (x - beta) % p
    if den == 0:
        return None
    return ((x - alpha) * inv(den, p)) % p


def normal_value(y: int, zero: int, pole: int | None, p: int) -> int | None:
    if pole is None:
        return (y - zero) % p
    den = (y - pole) % p
    if den == 0:
        return None
    return ((y - zero) * inv(den, p)) % p


def t_value(x: int, alpha1: int, beta1: int, alpha2: int, p: int) -> int | None:
    base = private_value(alpha2, alpha1, beta1, p)
    if base in (None, 0):
        raise AssertionError(("bad normalizing base", alpha1, beta1, alpha2))
    value = private_value(x, alpha1, beta1, p)
    if value is None:
        return None
    return (value * inv(base, p)) % p


def pgl2_parameters(
    params: tuple[tuple[int, int], tuple[int, int], tuple[int, int]], p: int
) -> tuple[int, int, int]:
    (alpha1, beta1), (_, beta2), (alpha3, beta3) = params
    alpha2 = params[1][0]
    lam = t_value(beta2, alpha1, beta1, alpha2, p)
    eta = t_value(alpha3, alpha1, beta1, alpha2, p)
    theta = t_value(beta3, alpha1, beta1, alpha2, p)
    if lam is None or eta is None or theta is None:
        raise AssertionError(("normal form parameter at infinity", params))
    forbidden = {0, 1}
    if lam in forbidden or eta in forbidden or theta in forbidden or eta == theta:
        raise AssertionError(("normal form collision", lam, eta, theta))
    return lam, eta, theta


def verify_value_equivalence(
    params: tuple[tuple[int, int], tuple[int, int], tuple[int, int]], p: int
) -> tuple[int, int, int]:
    lam, eta, theta = pgl2_parameters(params, p)
    normal_specs = ((0, None), (1, lam), (eta, theta))
    scalars: list[int | None] = [None, None, None]
    checked = 0
    for x in range(p):
        y = t_value(x, params[0][0], params[0][1], params[1][0], p)
        if y is None:
            continue
        for idx, ((alpha, beta), (zero, pole)) in enumerate(zip(params, normal_specs)):
            original = private_value(x, alpha, beta, p)
            normal = normal_value(y, zero, pole, p)
            if original is None or normal is None:
                continue
            if normal == 0:
                if original != 0:
                    raise AssertionError((p, idx, x, y, original, normal))
                continue
            ratio = original * inv(normal, p) % p
            if scalars[idx] is None:
                scalars[idx] = ratio
            elif scalars[idx] != ratio:
                raise AssertionError((p, idx, x, y, ratio, scalars[idx]))
            checked += 1
    if any(scalar in (None, 0) for scalar in scalars):
        raise AssertionError(("missing nonzero scalar", p, scalars))
    if checked == 0:
        raise AssertionError(("no comparisons", p))
    return lam, eta, theta


def rank_normal_form_check() -> tuple[int, int, tuple[int, int, int]]:
    params = ((2, 3), (5, 7), (11, 13))
    lam, eta, theta = verify_value_equivalence(params, P)
    original = Curve(
        ps=tuple(linear_root(alpha) for alpha, _ in params),
        qs=tuple(linear_root(beta) for _, beta in params),
    )
    normalized = Curve(
        ps=(linear_root(0), linear_root(1), linear_root(eta)),
        qs=((1,), linear_root(lam), linear_root(theta)),
    )
    original_rank = substitution_rank(original)
    normalized_rank = substitution_rank(normalized)
    if original_rank != normalized_rank:
        raise AssertionError((original_rank, normalized_rank, (lam, eta, theta)))
    return original_rank, normalized_rank, (lam, eta, theta)


def main() -> None:
    cases = (
        (97, ((2, 3), (5, 7), (11, 13))),
        (193, ((17, 29), (41, 73), (89, 137))),
        (769, ((101, 151), (211, 307), (401, 503))),
    )
    print("h=3 private-linear PGL2 normal form")
    for p, params in cases:
        lam, eta, theta = verify_value_equivalence(params, p)
        print(f"p={p} params={params} lambda={lam} eta={eta} theta={theta}")
    original_rank, normalized_rank, normal_params = rank_normal_form_check()
    print(
        f"rank check over p={P}: original={original_rank} "
        f"normal={normalized_rank} normal_params={normal_params}"
    )
    print("private-linear triples reduce to Y, (Y-1)/(Y-lambda), (Y-eta)/(Y-theta)")
    print("H3_PRIVATE_LINEAR_PGL2_NORMAL_FORM_PASS")


if __name__ == "__main__":
    main()
