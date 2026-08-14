#!/usr/bin/env python3
"""Independent audit for component-star owner-pencil routing."""

from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "source_contract.json"
CONTRACT_SHA256 = "23894520514168a69e1de5e638705c2036c6303e678bd295c124fe4278a917f7"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def audit(data: object) -> tuple[int, int, int]:
    require(isinstance(data, dict), "contract")
    p = data.get("parameters")
    require(isinstance(p, dict), "parameters")
    rho = Fraction(p["component_incidence_ppb"], 10**9)
    tau = Fraction(p["record_threshold_percent"], 100)
    fraction = (rho - tau) / (1 - tau)
    require(fraction == Fraction(5405467, 10**7), "record fraction")
    records = (p["non_dense_record_floor"] * fraction.numerator + fraction.denominator - 1) // fraction.denominator
    require(records == p["threshold_record_floor"], "records")
    K = p["K_max"]
    m = p["d"] + K
    E = (98 * (m - 10) + 99) // 100
    require(m - 10 - E == p["full_rank_owner_deficiency_ceiling"], "owner deficiency")
    pencil = E - (K - 11)
    require(pencil == p["rank9_pencil_extension_floor"], "pencil")
    require(p["space_dimension"] - 8 == p["low_rank_kernel_dimension_floor"], "kernel")
    require(len(data["routes"]) == 3 and len(data["logical_pins"]) == 5, "structure")

    statement = (HERE / "statement.md").read_text()
    proof = (HERE / "proof.md").read_text()
    for token in ("148639925144138894", "beta*(-gamma*u,u)", "45153"):
        require(token in statement, f"statement token {token}")
    for token in (
        "11*C(m',11)=C(m',10)(m'-10)",
        "Differences of any two such pairs",
        "recordwise statements",
    ):
        require(token in proof, f"proof token {token}")
    return records, E, pencil


def main() -> None:
    require(hashlib.sha256(CONTRACT.read_bytes()).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(CONTRACT.read_text())
    records, extensions, pencil = audit(data)
    mutations = (
        lambda item: item["parameters"].__setitem__("component_incidence_ppb", 990810933),
        lambda item: item["parameters"].__setitem__("record_threshold_percent", 97),
        lambda item: item["parameters"].__setitem__("K_max", 1048000),
        lambda item: item["parameters"].__setitem__("low_rank_kernel_dimension_floor", 3),
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
        "RATE_HALF_MCA_RANK11_COMPONENT_STAR_OWNER_PENCIL_ROUTER_AUDIT_PASS "
        f"records={records} extensions={extensions} pencil={pencil} controls={sum(controls)}/{len(controls)}"
    )


if __name__ == "__main__":
    main()
