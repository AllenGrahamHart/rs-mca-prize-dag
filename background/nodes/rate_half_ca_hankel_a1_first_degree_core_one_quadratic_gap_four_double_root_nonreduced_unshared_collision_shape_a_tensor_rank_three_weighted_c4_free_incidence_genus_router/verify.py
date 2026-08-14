#!/usr/bin/env python3
"""Replay the official weighted incidence/genus arithmetic."""

from __future__ import annotations

from dataclasses import dataclass


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


@dataclass(frozen=True)
class Formula:
    official_e: int = 183251937963
    official_m: int = 183251937961
    official_n: int = 274877906941
    parameter_branches: int = 549755813889
    domain_branches: int = 824633720830
    total_deficit: int = 366503875919
    parameter_image_floor: int = 10
    domain_image_floor: int = 10
    zero_deficit_mass_floor: int = 183251937970


def replay(formula: Formula) -> dict[str, int]:
    e = (2**39 + 1) // 3
    m = e - 2
    n = (3 * e - 7) // 2
    parameter_branches = 3 * e
    domain_branches = 3 * n + 7
    total_deficit = 2 * e - 7
    parameter_square_cap = (m - 1) * (m - 2) + parameter_branches
    domain_square_cap = (n - 1) * (n - 2) + domain_branches
    parameter_floor = (parameter_branches**2 + parameter_square_cap - 1) // parameter_square_cap
    domain_floor = (domain_branches**2 + domain_square_cap - 1) // domain_square_cap
    zero_deficit_mass = parameter_branches - total_deficit

    require(e == formula.official_e, "official e")
    require(m == formula.official_m, "official m")
    require(n == formula.official_n, "official n")
    require(parameter_branches == formula.parameter_branches, "parameter branches")
    require(domain_branches == formula.domain_branches, "domain branches")
    require(total_deficit == formula.total_deficit, "total deficit")
    require(parameter_square_cap == e * e - 4 * e + 12, "parameter square cap")
    require(domain_square_cap == n * n + 9, "domain square cap")
    require(parameter_floor == formula.parameter_image_floor, "parameter image floor")
    require(domain_floor == formula.domain_image_floor, "domain image floor")
    require(zero_deficit_mass == formula.zero_deficit_mass_floor, "zero-deficit mass")
    require(zero_deficit_mass > m - 1, "two zero-deficit vertices")
    return {
        "e": e,
        "m": m,
        "n": n,
        "parameter_floor": parameter_floor,
        "domain_floor": domain_floor,
        "total_deficit": total_deficit,
        "zero_deficit_mass": zero_deficit_mass,
    }


def tamper_selftest() -> int:
    base = Formula()
    rejected = 0
    for field in base.__dict__:
        values = dict(base.__dict__)
        values[field] += 1
        try:
            replay(Formula(**values))
        except VerificationError:
            rejected += 1
    require(rejected == len(base.__dict__), "hostile mutations")
    return rejected


def main() -> None:
    result = replay(Formula())
    mutations = tamper_selftest()
    print(
        "RATE_HALF_SHAPE_A_RANK3_WEIGHTED_C4_GENUS_PASS",
        f"image_floors={(result['parameter_floor'], result['domain_floor'])}",
        f"total_deficit={result['total_deficit']}",
        f"zero_mass={result['zero_deficit_mass']}",
        f"mutations={mutations}/{mutations}",
    )


if __name__ == "__main__":
    main()
