#!/usr/bin/env python3
"""Independent audit of the HGE4 trace-power gcd compiler."""

from __future__ import annotations

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_kummer_trace_power_gcd_compiler"
VERIFY = ROOT / "background" / "nodes" / NODE / "verify.py"


def load_verify():
    spec = importlib.util.spec_from_file_location("trace_gcd_verify", VERIFY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    verify = load_verify()
    expected_polynomials = {
        4: [0, 1],
        8: [0, -2, 0, 1],
        16: [0, -4, 0, 10, 0, -6, 0, 1],
    }
    for order, expected in expected_polynomials.items():
        prime = 65537
        actual = verify.trace_quotient(order, prime)
        assert actual == [value % prime for value in expected]

    controls = {(8, 137): 1, (16, 593): 1, (32, 1249): 1, (32, 97): 0}
    for (order, prime), expected in controls.items():
        compiled = len(verify.candidate_gcd(order, prime)) - 1
        direct = len(verify.direct_trace_candidates(order, prime))
        assert compiled == direct == expected

    # Wrong exponents do not reproduce the exact control ledger.
    order, prime = 16, 593
    trace_poly = verify.trace_quotient(order // 2, prime)
    inverse_eight = pow(8, -1, prime)
    scalar = [(-2 * inverse_eight) % prime, (-inverse_eight) % prime]
    wrong = verify.subtract(verify.power_mod(scalar, order, trace_poly, prime), [1], prime)
    wrong_count = len(verify.monic_gcd(trace_poly, wrong, prime)) - 1
    assert wrong_count != controls[(order, prime)]

    base = ROOT / "background" / "nodes" / NODE
    statement = (base / "statement.md").read_text()
    audit = (base / "audit.md").read_text()
    consumer = (ROOT / "critical" / "nodes" / "f3_hge4_norm_gate_count" / "statement.md").read_text()
    assert "degree-at-most-`m/2-1`" in statement
    assert "gcd may be nonconstant" in statement
    assert "one trace may support" in audit
    assert NODE in consumer
    print(
        "F3_HGE4_KUMMER_TRACE_POWER_GCD_COMPILER_AUDIT_PASS "
        "quotients=3 controls=4 wrong_exponent=1"
    )


if __name__ == "__main__":
    main()
