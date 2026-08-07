#!/usr/bin/env python3
"""Verify affine source normalization and the residual cross-ratio fiber."""

from __future__ import annotations

from itertools import product
from pathlib import Path
from random import Random
import importlib.util


NODE = "pma_ratehalf_source_crossratio_fiber_reduction"
ROOT = Path(__file__).resolve().parents[3]
SOURCE = (
    ROOT
    / "background"
    / "nodes"
    / "pma_ratehalf_source_aligned_gcd_excess"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("pma_source_aligned_base", SOURCE)
assert SPEC is not None and SPEC.loader is not None
aligned = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(aligned)
base = aligned.base


def setup() -> dict[str, object]:
    p = 17
    ell, b = 2, 1
    core = list(range(7))
    petals = ((7, 8), (9, 10), (11, 12))
    petal_points = [x for petal in petals for x in petal]
    l_core = base.locator(core, p)
    l_petals = [base.locator(petal, p) for petal in petals]
    l = [1]
    for petal_locator in l_petals:
        l = base.mul(l, petal_locator, p)
    return {
        "p": p,
        "ell": ell,
        "b": b,
        "k0": ell + b - 1,
        "core": core,
        "petals": petals,
        "petal_points": petal_points,
        "l_core": l_core,
        "l_petals": l_petals,
        "l": l,
    }


def source_pair(data: dict[str, object], labels: tuple[int, int, int]) -> tuple[list[int], list[int], list[int]]:
    p = int(data["p"])
    petals = tuple(data["petals"])
    values = [
        labels[index]
        for index, petal in enumerate(petals)
        for _ in petal
    ]
    e_c = base.interpolate(list(data["petal_points"]), values, p)
    y_poly, p_star = aligned.divmod_poly(
        base.mul(list(data["l_core"]), e_c, p), list(data["l"]), p
    )
    return e_c, p_star, y_poly


def affine_normalization(data: dict[str, object]) -> dict[str, object]:
    p = int(data["p"])
    k0 = int(data["k0"])
    core = list(data["core"])
    l_core = list(data["l_core"])
    l = list(data["l"])
    q0, p0 = aligned.divmod_poly(l_core, l, p)
    assert base.degree(q0) == k0 - 1

    rng = Random(0xC2055)
    cases = 0
    wrong_lambda_caught = False
    for _ in range(400):
        labels = tuple(rng.sample(range(p), 3))
        alpha = rng.randrange(1, p)
        beta = rng.randrange(p)
        transformed = tuple((alpha * value + beta) % p for value in labels)
        _, p_star, y_poly = source_pair(data, labels)
        _, p_prime, y_prime = source_pair(data, transformed)
        assert p_prime == base.add(base.scale(p_star, alpha, p), base.scale(p0, beta, p), p)
        assert y_prime == base.add(base.scale(y_poly, alpha, p), base.scale(q0, beta, p), p)

        h = base.trim([rng.randrange(p) for _ in range(k0)])
        h_prime = base.add(base.scale(h, alpha, p), base.scale(q0, beta, p), p)
        old_roots = {
            x
            for x in core
            if base.evaluate(base.add(p_star, base.mul(l, h, p), p), x, p) == 0
        }
        new_roots = {
            x
            for x in core
            if base.evaluate(base.add(p_prime, base.mul(l, h_prime, p), p), x, p) == 0
        }
        assert old_roots == new_roots

        normal_alpha = pow((labels[1] - labels[0]) % p, -1, p)
        normal_beta = -normal_alpha * labels[0] % p
        normalized = tuple(
            (normal_alpha * value + normal_beta) % p for value in labels
        )
        lambda_value = (labels[2] - labels[0]) * pow(
            (labels[1] - labels[0]) % p, -1, p
        ) % p
        assert normalized == (0, 1, lambda_value)
        wrong_lambda_caught |= lambda_value != (
            (labels[2] - labels[1])
            * pow((labels[1] - labels[0]) % p, -1, p)
            % p
        )
        cases += 1

    in_code = []
    for labels in product(range(p), repeat=3):
        _, _, y_poly = source_pair(data, labels)
        if base.degree(y_poly) <= k0 - 1:
            in_code.append(labels)
    assert len(in_code) == p
    assert all(row[0] == row[1] == row[2] for row in in_code)
    return {
        "cases": cases,
        "q_degree": base.degree(q0),
        "intersection": len(in_code),
        "wrong_lambda": wrong_lambda_caught,
    }


def numerator_factors(data: dict[str, object]) -> dict[str, object]:
    p = int(data["p"])
    ell = int(data["ell"])
    core = list(data["core"])
    l1, l2, l3 = list(data["l_petals"])
    _, p2, _ = source_pair(data, (0, 1, 0))
    _, p3, _ = source_pair(data, (0, 0, 1))
    r2, rem2 = aligned.divmod_poly(p2, base.mul(l1, l3, p), p)
    r3, rem3 = aligned.divmod_poly(p3, base.mul(l1, l2, p), p)
    assert rem2 == rem3 == [0]
    assert r2 != [0] and r3 != [0]
    assert base.degree(r2) < ell and base.degree(r3) < ell
    exceptional = [x for x in core if base.evaluate(p3, x, p) == 0]
    assert exceptional == [x for x in core if base.evaluate(r3, x, p) == 0]
    assert len(exceptional) <= ell - 1
    return {
        "p2": p2,
        "p3": p3,
        "r2_degree": base.degree(r2),
        "r3_degree": base.degree(r3),
        "exceptional": exceptional,
        "factor_mutation": base.degree(p3) >= base.degree(r3) + 2 * ell,
    }


def lambda_votes(data: dict[str, object], factors: dict[str, object]) -> dict[str, object]:
    p = int(data["p"])
    k0 = int(data["k0"])
    core = list(data["core"])
    l = list(data["l"])
    p2 = list(factors["p2"])
    p3 = list(factors["p3"])
    lambda_value = 3
    p_star = base.add(p2, base.scale(p3, lambda_value, p), p)
    exceptional = set(factors["exceptional"])
    rng = Random(0x1A2BDA)
    votes = 0
    ambient_unaligned = False
    for _ in range(2_000):
        polys: list[list[int]] = []
        while len(polys) < 3:
            candidate = base.trim([rng.randrange(p) for _ in range(k0)])
            if candidate not in polys:
                polys.append(candidate)
        agreement_sets = []
        for poly in polys:
            codeword = base.add(p_star, base.mul(l, poly, p), p)
            agreement_sets.append(
                {x for x in core if base.evaluate(codeword, x, p) == 0}
            )
        for x in core:
            members = [index for index, row in enumerate(agreement_sets) if x in row]
            if len(members) < 2 or x in exceptional:
                continue
            common_value = base.evaluate(polys[members[0]], x, p)
            assert all(base.evaluate(polys[index], x, p) == common_value for index in members)
            vote = (
                -(base.evaluate(p2, x, p) + base.evaluate(l, x, p) * common_value)
                * pow(base.evaluate(p3, x, p), -1, p)
            ) % p
            assert vote == lambda_value
            votes += len(members) - 1

        a_poly = base.sub(polys[0], polys[1], p)
        for x in core:
            if base.evaluate(a_poly, x, p) == 0 and not (
                x in agreement_sets[0] and x in agreement_sets[1]
            ):
                ambient_unaligned = True
                break
    assert votes > 0 and ambient_unaligned
    return {"votes": votes, "ambient_unaligned": ambient_unaligned}


def sharp_tail_residual() -> dict[str, int]:
    ell, b, a = 11, 7, 1
    triple = set(range(13))
    e12 = set(range(13, 16))
    e13 = set(range(16, 19))
    e23 = set(range(19, 22))
    r1 = set(range(22, 31))
    r2 = set(range(31, 40))
    r3 = set(range(40, 49))
    sets = (
        triple | e12 | e13 | r1,
        triple | e12 | e23 | r2,
        triple | e13 | e23 | r3,
    )
    assert tuple(map(len, sets)) == (28, 28, 28)
    weights = {
        x: max(0, sum(x in row for row in sets) - 1) for x in range(49)
    }
    total = sum(weights.values())
    exceptional = set(range(ell - 1))
    exceptional_weight = sum(weights[x] for x in exceptional)
    residual = total - exceptional_weight
    expected = 2 * b + 3 * a - 2
    assert (total, exceptional_weight, residual, expected) == (35, 20, 15, 15)
    return {
        "total": total,
        "exceptional_weight": exceptional_weight,
        "residual": residual,
    }


def main() -> None:
    data = setup()
    affine = affine_normalization(data)
    factors = numerator_factors(data)
    votes = lambda_votes(data, factors)
    tail = sharp_tail_residual()
    mutations = sum(
        bool(value)
        for value in (
            affine["q_degree"] == int(data["k0"]) - 1,
            affine["cases"] > 0,
            affine["wrong_lambda"],
            factors["factor_mutation"],
            len(factors["exceptional"]) <= int(data["ell"]) - 1,
            tail["exceptional_weight"] > int(data["ell"]) - 1,
            tail["residual"] > 0,
            votes["ambient_unaligned"],
        )
    )
    assert mutations == 8
    print(
        f"{NODE}_PASS affine_cases={affine['cases']} "
        f"source_intersection={affine['intersection']} "
        f"r_degrees={factors['r2_degree']},{factors['r3_degree']} "
        f"exceptional={len(factors['exceptional'])} votes={votes['votes']} "
        f"tail_total={tail['total']} tail_exceptional={tail['exceptional_weight']} "
        f"tail_residual={tail['residual']} mutations={mutations}"
    )


if __name__ == "__main__":
    main()
