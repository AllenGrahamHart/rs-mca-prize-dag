#!/usr/bin/env python3
"""Verify the guarded two-petal support-fiber correspondence."""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
from random import Random
import importlib.util


NODE = "pma_ratehalf_two_petal_support_fiber_reduction"
ROOT = Path(__file__).resolve().parents[3]
CROSS = (
    ROOT
    / "background"
    / "nodes"
    / "pma_ratehalf_source_crossratio_fiber_reduction"
    / "verify.py"
)
SPEC = importlib.util.spec_from_file_location("pma_crossratio_base", CROSS)
assert SPEC is not None and SPEC.loader is not None
cross = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cross)
aligned = cross.aligned
base = cross.base


def extended_gcd(
    left: list[int], right: list[int], p: int
) -> tuple[list[int], list[int], list[int]]:
    if right == [0]:
        unit = pow(left[-1], -1, p)
        return base.scale(left, unit, p), [unit], [0]
    quotient, remainder = aligned.divmod_poly(left, right, p)
    gcd, x1, y1 = extended_gcd(right, remainder, p)
    return gcd, y1, base.sub(x1, base.mul(quotient, y1, p), p)


def inverse_mod(poly: list[int], modulus: list[int], p: int) -> list[int]:
    gcd, inverse, _ = extended_gcd(poly, modulus, p)
    assert gcd == [1]
    _, remainder = aligned.divmod_poly(inverse, modulus, p)
    assert aligned.divmod_poly(base.mul(poly, remainder, p), modulus, p)[1] == [1]
    return remainder


def residue(poly: list[int], modulus: list[int], p: int) -> list[int]:
    return aligned.divmod_poly(poly, modulus, p)[1]


def support_candidate(
    data: dict[str, object],
    factors: dict[str, object],
    subset: tuple[int, ...],
    lambda_value: int,
    a: int = 1,
) -> dict[str, object]:
    p = int(data["p"])
    ell = int(data["ell"])
    l2 = list(data["l_petals"])[1]
    l3 = list(data["l_petals"])[2]
    r2 = aligned.divmod_poly(
        list(factors["p2"]),
        base.mul(list(data["l_petals"])[0], l3, p),
        p,
    )[0]
    r3 = aligned.divmod_poly(
        list(factors["p3"]),
        base.mul(list(data["l_petals"])[0], l2, p),
        p,
    )[0]
    l_s = base.locator(subset, p)
    v_s = residue(
        base.mul(
            base.mul(l3, r2, p),
            inverse_mod(residue(l_s, l2, p), l2, p),
            p,
        ),
        l2,
        p,
    )
    phi = residue(
        base.mul(
            base.mul(l_s, v_s, p),
            inverse_mod(residue(base.mul(l2, r3, p), l3, p), l3, p),
            p,
        ),
        l3,
        p,
    )
    quotient, remainder = aligned.divmod_poly(list(data["l_core"]), l_s, p)
    assert remainder == [0]
    exact = aligned.gcd_poly(v_s, quotient, p) == [1]
    degree_ok = base.degree(v_s) <= ell - a
    constant = base.degree(phi) <= 0
    target = phi == [lambda_value % p]
    return {
        "l_s": l_s,
        "v": v_s,
        "phi": phi,
        "degree_ok": degree_ok,
        "exact": exact,
        "constant": constant,
        "target": target,
    }


def setup_layout(p: int, points: list[int]) -> dict[str, object]:
    ell, b = 2, 1
    core = points[:7]
    petals = (tuple(points[7:9]), tuple(points[9:11]), tuple(points[11:13]))
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


def hostile_guard_search() -> dict[str, object]:
    rng = Random(0x5F6A2D)
    degree_witness = False
    exactness_witness = False
    layouts = 0
    for p in (17, 19, 23):
        for _ in range(160):
            points = rng.sample(range(p), 13)
            data = setup_layout(p, points)
            factors = cross.numerator_factors(data)
            core = list(data["core"])
            for a in (1, 2):
                m = 2 * int(data["ell"]) + int(data["b"]) + a - 2
                for subset in combinations(core, m):
                    row = support_candidate(data, factors, subset, 0, a=a)
                    phi = list(row["phi"])
                    if base.degree(phi) > 0 or phi[0] in (0, 1):
                        continue
                    degree_witness |= not bool(row["degree_ok"])
                    exactness_witness |= bool(row["degree_ok"]) and not bool(row["exact"])
            layouts += 1
            if degree_witness and exactness_witness:
                return {
                    "layouts": layouts,
                    "degree_witness": degree_witness,
                    "exactness_witness": exactness_witness,
                }
    return {
        "layouts": layouts,
        "degree_witness": degree_witness,
        "exactness_witness": exactness_witness,
    }


def reconstruct(
    data: dict[str, object],
    factors: dict[str, object],
    candidate: dict[str, object],
    lambda_value: int,
) -> list[int]:
    p = int(data["p"])
    l2 = list(data["l_petals"])[1]
    l3 = list(data["l_petals"])[2]
    r2 = aligned.divmod_poly(
        list(factors["p2"]),
        base.mul(list(data["l_petals"])[0], l3, p),
        p,
    )[0]
    r3 = aligned.divmod_poly(
        list(factors["p3"]),
        base.mul(list(data["l_petals"])[0], l2, p),
        p,
    )[0]
    f_lambda = base.add(
        base.mul(l3, r2, p),
        base.scale(base.mul(l2, r3, p), lambda_value, p),
        p,
    )
    numerator = base.sub(
        base.mul(list(candidate["l_s"]), list(candidate["v"]), p),
        f_lambda,
        p,
    )
    h, remainder = aligned.divmod_poly(numerator, base.mul(l2, l3, p), p)
    assert remainder == [0]
    assert base.degree(h) <= int(data["k0"]) - 1
    return h


def exact_bijection() -> dict[str, object]:
    data = cross.setup()
    factors = cross.numerator_factors(data)
    p = int(data["p"])
    core = list(data["core"])
    l = list(data["l"])
    l1 = list(data["l_petals"])[0]
    m = 2 * int(data["ell"]) + int(data["b"]) + 1 - 2
    support_rows = list(combinations(core, m))

    total_direct = 0
    total_guarded = 0
    constant_rows = 0
    degree_rejections = 0
    exactness_rejections = 0
    wrong_modulus_caught = False
    nonintegral_caught = False
    for lambda_value in range(2, p):
        p_star = base.add(
            list(factors["p2"]),
            base.scale(list(factors["p3"]), lambda_value, p),
            p,
        )
        guarded: dict[tuple[int, ...], tuple[int, ...]] = {}
        for subset in support_rows:
            row = support_candidate(data, factors, subset, lambda_value)
            constant_rows += int(row["constant"])
            degree_rejections += int(row["target"] and not row["degree_ok"])
            exactness_rejections += int(
                row["target"] and row["degree_ok"] and not row["exact"]
            )
            if row["target"] and row["degree_ok"] and row["exact"]:
                h = reconstruct(data, factors, row, lambda_value)
                z = base.mul(list(row["l_s"]), list(row["v"]), p)
                codeword = base.mul(l1, z, p)
                assert codeword == base.add(p_star, base.mul(l, h, p), p)
                roots = tuple(
                    x for x in core if base.evaluate(codeword, x, p) == 0
                )
                assert roots == subset
                guarded[subset] = tuple(h)

            # Swapping the first modulus does not reproduce the defining residue.
            l3 = list(data["l_petals"])[2]
            wrong_v = residue(
                base.mul(
                    list(factors["p2"]),
                    inverse_mod(residue(base.locator(subset, p), l3, p), l3, p),
                    p,
                ),
                l3,
                p,
            )
            wrong_modulus_caught |= wrong_v != row["v"]

        direct: dict[tuple[int, ...], tuple[int, ...]] = {}
        for coefficients in product(range(p), repeat=int(data["k0"])):
            h = base.trim(list(coefficients))
            codeword = base.add(p_star, base.mul(l, h, p), p)
            roots = tuple(x for x in core if base.evaluate(codeword, x, p) == 0)
            if len(roots) == m:
                assert roots not in direct
                direct[roots] = tuple(h)
        assert direct == guarded
        total_direct += len(direct)
        total_guarded += len(guarded)

        # A forced numerator mutation must fail divisibility by L2L3.
        if guarded:
            sample_subset = next(iter(guarded))
            sample = support_candidate(data, factors, sample_subset, lambda_value)
            mutated = dict(sample)
            mutated["v"] = base.add(list(sample["v"]), [1], p)
            try:
                reconstruct(data, factors, mutated, lambda_value)
            except AssertionError:
                nonintegral_caught = True

    assert total_direct == total_guarded and total_direct > 0
    assert constant_rows > 0
    assert wrong_modulus_caught and nonintegral_caught
    return {
        "lambdas": p - 2,
        "supports": len(support_rows),
        "contributors": total_direct,
        "constant_rows": constant_rows,
        "degree_rejections": degree_rejections,
        "exactness_rejections": exactness_rejections,
        "wrong_modulus": wrong_modulus_caught,
        "nonintegral": nonintegral_caught,
    }


def tail_arithmetic() -> dict[str, int]:
    ell, b, a = 11, 7, 1
    n_core = 4 * ell + b - 2
    k0 = ell + b - 1
    m = 2 * ell + b + a - 2
    cofactor = (n_core - ell) - m
    assert (m, cofactor, ell - a, k0 - 1) == (28, 10, 10, 16)
    return {"m": m, "cofactor": cofactor}


def main() -> None:
    bijection = exact_bijection()
    hostile = hostile_guard_search()
    tail = tail_arithmetic()
    assert hostile["degree_witness"] and hostile["exactness_witness"]
    mutations = sum(
        bool(value)
        for value in (
            bijection["wrong_modulus"],
            bijection["nonintegral"],
            bijection["constant_rows"] > bijection["contributors"],
            hostile["degree_witness"],
            hostile["exactness_witness"],
            tail["cofactor"] == 10,
            bijection["contributors"] > 0,
        )
    )
    assert mutations == 7
    print(
        f"{NODE}_PASS lambdas={bijection['lambdas']} "
        f"supports={bijection['supports']} contributors={bijection['contributors']} "
        f"constant_rows={bijection['constant_rows']} "
        f"degree_rejections={bijection['degree_rejections']} "
        f"exactness_rejections={bijection['exactness_rejections']} "
        f"hostile_layouts={hostile['layouts']} "
        f"tail_m={tail['m']} tail_cofactor={tail['cofactor']} "
        f"mutations={mutations}"
    )


if __name__ == "__main__":
    main()
