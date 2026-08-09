#!/usr/bin/env python3
"""Directly audit the cell-12 parallel-DE pairing-11 packet."""

import ast
import sys
from pathlib import Path

import sympy as sp


NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
EXP = ROOT / "experiments/prize_resolution"
sys.path.insert(0, str(EXP))

from rate_half_kb_positive_433_1b_cell12_common_f_resultant_audit import audit_result


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    root_script = EXP / "rate_half_kb_positive_433_1b_cell12_de_pairing11_14_frobenius_roots_modal.py"
    source = root_script.read_text()
    ast.parse(source)
    for snippet in ("fmpz_mod_poly_ctx", "polynomial.gcd(pow(x, PRIME, polynomial) - x)", "root_part.factor()"):
        require(snippet in source, f"root method: {snippet}")
    b0, b1, b2, c0, c1, c2, f = sp.symbols("b0 b1 b2 c0 c1 c2 f")
    resultant = sp.resultant(b0 + b1*f + b2*f**2,
                             c0 + c1*f + c2*f**2, f)
    printed = (b2*c0-b0*c2)**2 - (b2*c1-b1*c2)*(b1*c0-b0*c1)
    require(sp.expand(resultant - printed) == 0, "quadratic resultant")
    primaries = {
        "pairing11": EXP / "rate_half_kb_positive_433_1b_cell12_de_pairing11_template_adapter_result.json",
        "pairing14": EXP / "rate_half_kb_positive_433_1b_cell12_positive_de_pairing14_template_adapter_result.json",
    }
    summary = audit_result(
        result=primaries["pairing11"],
        root_result=EXP / "rate_half_kb_positive_433_1b_cell12_de_pairing11_14_frobenius_roots_result.json",
        primary_paths=primaries,
        tower_path=EXP / "rate_half_kb_positive_433_1b_cell12_four_basis_tower_result.json",
        kernel_path=EXP / "rate_half_kb_positive_433_1b_cell12_compact_kernel_result.json",
        pairing=11, xi_values=(0, 2), matching=((0, 4), (1, 5), (2, 3)),
    )
    expected = {
        "rows": 32, "combined_profiles": 57, "profile_visits": 320,
        "target_root_count": 256, "candidate_root_count": 464,
        "source_point_count": 592, "route_point_count": 592,
        "uf_candidate_count": 0, "colored_solution_count": 0,
        "leading_boundaries": 32, "product_boundaries": 96,
        "target_boundaries": 144, "missing_impossible": 96,
        "checked": 400, "colored_nonzero": 0,
    }
    require(summary == expected, "direct pairing-11 census")
    print("PASS direct pairing-11 audit: rows=32 candidates=464 checked=400")


if __name__ == "__main__":
    main()
