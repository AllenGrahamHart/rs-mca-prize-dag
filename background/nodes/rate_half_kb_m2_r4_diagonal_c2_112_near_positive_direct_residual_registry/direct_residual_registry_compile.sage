#!/usr/bin/env sage
"""Compile exact fingerprints for the 30 residual affine literal cells."""

load("/near_literal_assignment_transport_audit.sage")


REPRESENTATIVE_ASSIGNMENTS = ("F02", "F04", "F06", "M01", "M03")
REPRESENTATIVE_ROOTS = ("A", "OB")
ALLOCATIONS = ("RX", "RL", "RM")


def polynomial_record(value):
    polynomial = primitive(R(K(value).numerator()))
    text = str(polynomial)
    return polynomial, {
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
        "terms": int(len(polynomial.dict())),
        "total_degree": int(polynomial.total_degree()),
        "degrees_bcd": [int(polynomial.degree(generator)) for generator in R.gens()],
        "text_bytes": int(len(text.encode())),
    }


cells = []
all_equation_hashes = []
for assignment in REPRESENTATIVE_ASSIGNMENTS:
    residuals, systems = cache[assignment]
    for root in REPRESENTATIVE_ROOTS:
        for allocation in ALLOCATIONS:
            target_id = f"{root}-{allocation}"
            target_pair = TARGETS[target_id]
            equations = []
            polynomials = []
            denominator_factors = []
            for residual, target in zip(residuals, target_pair):
                assert residual.degree() == target.degree() == 2
                for index in (0, 1):
                    raw = K(residual[index] - residual[2] * target[index])
                    polynomial, record = polynomial_record(raw)
                    assert polynomial != 0
                    polynomials.append(polynomial)
                    equations.append(record)
                    all_equation_hashes.append(record["sha256"])
                    for factor, _ in strip_units(K(raw.denominator())).factor():
                        if not factor.is_constant():
                            denominator_factors.append(str(primitive(factor)))
            common = polynomials[0]
            for polynomial in polynomials[1:]:
                common = common.gcd(polynomial)
            _, common_record = polynomial_record(common)
            cells.append({
                "cell": f"{assignment}-{target_id}",
                "assignment": assignment,
                "target": target_id,
                "equations": equations,
                "equation_tuple_sha256": hashlib.sha256(
                    "\n".join(record["sha256"] for record in equations).encode()
                ).hexdigest(),
                "common_gcd": common_record,
                "denominator_factors": sorted(set(denominator_factors)),
                "radical_localizer_factors": factor_set(systems[target_id], "I"),
            })

payload = {
    "schema": "kb-c2-112-near-literal-direct-residual-registry-v1",
    "assignments": list(REPRESENTATIVE_ASSIGNMENTS),
    "root_representatives": list(REPRESENTATIVE_ROOTS),
    "allocations": list(ALLOCATIONS),
    "cells": cells,
    "cell_count": int(len(cells)),
    "equation_count": int(sum(len(cell["equations"]) for cell in cells)),
    "registry_sha256": hashlib.sha256("\n".join(all_equation_hashes).encode()).hexdigest(),
    "max_terms": int(max(
        equation["terms"] for cell in cells for equation in cell["equations"]
    )),
    "max_total_degree": int(max(
        equation["total_degree"] for cell in cells for equation in cell["equations"]
    )),
    "terminal": "DIRECT_RESIDUAL_REGISTRY_COMPILED",
}
print(
    "DIRECT_RESIDUAL_REGISTRY_JSON "
    + json.dumps(payload, sort_keys=True, separators=(",", ":"), default=int)
)
