#!/usr/bin/env python3
"""Independent audit for dense-root high-span saturation."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "9847a084251f60c01dabceda6a29f64b11df92cdb06352e922a19fa4ba1e79a6"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> tuple[int, int, int]:
    require(isinstance(data, dict), "contract")
    parameters = data.get("parameters")
    require(isinstance(parameters, dict), "parameters")
    roots = parameters["dense_root_count"]
    maximum = parameters["slope_degree_maximum"]
    quotient = parameters["quotient_degree_maximum"]
    dimension = parameters["deviation_dimension"]
    require((roots, maximum, quotient, dimension) == (18, 31, 13, 10), "pins")
    require(roots + quotient == maximum, "factor degree")
    require(parameters["triangular_coefficient_start"] == roots, "triangle start")
    require(parameters["high_coefficient_start"] <= roots, "high containment")
    require(parameters["surviving_correction_dimension"] == dimension, "saturation")
    require(len(data["logical_pins"]) == 5, "pins")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("span{H_j:j>=2}", "W=V'", "dimensions `2..9`"):
        require(token in statement, f"statement token {token}")
    for token in (
        "ten actual records whose deviations form a basis",
        "Descending triangular elimination",
        "It supplies no bound on the number",
    ):
        require(token in proof, f"proof token {token}")
    return roots, quotient, dimension


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    roots, quotient, dimension = audit(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("dense_root_count", 17),
        lambda item: item["parameters"].__setitem__("slope_degree_maximum", 32),
        lambda item: item["parameters"].__setitem__("triangular_coefficient_start", 17),
        lambda item: item["parameters"].__setitem__("surviving_correction_dimension", 9),
        lambda item: item["logical_pins"].pop(),
    )
    controls = []
    for mutate in mutations:
        altered = copy.deepcopy(data)
        mutate(altered)
        try:
            audit(altered)
        except (Reject, KeyError, TypeError, ValueError):
            controls.append(True)
        else:
            controls.append(False)
    require(all(controls), "mutation controls")
    print(
        "RATE_HALF_MCA_RANK11_DENSE_ROOT_HIGHSPAN_SATURATION_AUDIT_PASS "
        f"factor={roots}+{quotient} dimension={dimension} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
