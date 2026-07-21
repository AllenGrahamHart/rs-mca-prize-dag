#!/usr/bin/env python3
"""Independent mutation audit for the HGE4 midpoint trace-power gate."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
NODE = "f3_hge4_kummer_midpoint_trace_power_gate"


def main() -> None:
    mutations = 0
    for u, v in ((Fraction(2), Fraction(3)), (Fraction(5), Fraction(11))):
        s = (u + v) / 2
        a = (v - u) / 2
        w = -1 / (u * v)
        z = -3 * (u + v) / (u * v * (v - u) ** 2)
        lam = w - z * s
        actual = 1 - a * a * lam
        expected = -(u + v) ** 2 / (8 * u * v)
        assert actual == expected
        assert actual != (u + v) ** 2 / (8 * u * v)
        assert actual != -(u + v) ** 2 / (4 * u * v)
        mutations += 2

    prime, order = 97, 32
    generator = pow(5, (prime - 1) // order, prime)
    roots = {pow(generator, exponent, prime) for exponent in range(order)}
    assert len(roots) == order
    traces = {
        (x + pow(x, -1, prime)) % prime
        for x in roots - {1, prime - 1}
    }
    assert len(traces) == (order - 2) // 2
    square_traces = {
        (x + pow(x, -1, prime)) % prime
        for x in roots - {1, prime - 1}
        if pow(x, (prime - 1) // 2, prime) == 1
    }
    assert (prime - 1) // order % 2 == 1
    assert len(square_traces) == order // 4 - 1
    assert (-(prime - 1 + 1) ** 2) % prime == 0
    mutations += 3

    base = ROOT / "background" / "nodes" / NODE
    statement = (base / "statement.md").read_text()
    audit = (base / "audit.md").read_text()
    consumer = (ROOT / "critical" / "nodes" / "f3_hge4_norm_gate_count" / "statement.md").read_text()
    for marker in (
        "kappa=-(1+x)^2/(8x)",
        "(-(tau+2)/8)^((p-1)/m)=1",
        "necessary candidate gate",
    ):
        assert marker in statement
    assert "The factor `8`" in audit
    assert "does not determine a Belyi" in audit
    assert NODE in consumer

    print(
        "F3_HGE4_KUMMER_MIDPOINT_TRACE_POWER_GATE_AUDIT_PASS "
        f"mutations={mutations} trace_count={(order - 2) // 2}"
    )


if __name__ == "__main__":
    main()
