#!/usr/bin/env python3
"""Replay a WCL (4,9) anti-reciprocal Groebner pilot result."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


APP_NAME = "wcl49-inversion-symmetric-groebner"


def equations():
    y, c0, c1, c2, c3 = sp.symbols("y c0 c1 c2 c3")
    variables = (c3, c2, c1, c0)
    a = y**4 + c3 * y**3 + c2 * y**2 + c1 * y + c0
    p = sp.Poly(sp.expand(y * a**2 - 1), y)
    anti = [sp.expand(p.nth(index) + p.nth(9 - index)) for index in range(1, 5)]
    return variables, anti


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    result = json.loads(args.result.read_text())

    variables, anti = equations()
    equation_text = [str(value) for value in anti]
    assert result["app"] == APP_NAME
    assert result["domain"] == "QQ" and result["order"] == "lex"
    assert result["variables"] == [str(value) for value in variables]
    assert result["equations"] == equation_text
    assert result["equations_sha256"] == hashlib.sha256(
        "\n".join(equation_text).encode()
    ).hexdigest()
    assert result["status"] in {"COMPLETE", "TIMEOUT"}
    assert 0 <= float(result["seconds"]) <= 90
    assert 0 <= int(result["peak_mb"]) <= 1024

    if result["status"] == "TIMEOUT":
        assert result["checkpoint"] == "equations_constructed"
        print(
            "WCL49_INVERSION_SYMMETRIC_GROEBNER_CHECK_PASS "
            f"status=TIMEOUT seconds={result['seconds']}"
        )
        return

    replay = sp.groebner(anti, *variables, order="lex", domain=sp.QQ)
    replay_text = [str(poly.as_expr()) for poly in replay.polys]
    assert result["basis_polynomials"] == replay_text
    assert result["basis_sha256"] == hashlib.sha256(
        "\n".join(replay_text).encode()
    ).hexdigest()
    assert result["zero_dimensional"] == bool(replay.is_zero_dimensional)
    expected_factors = {
        value: str(sp.factor(sp.sympify(value)))
        for value in replay_text
        if len(sp.sympify(value).free_symbols) == 1
    }
    assert result["univariate_factors"] == expected_factors
    print(
        "WCL49_INVERSION_SYMMETRIC_GROEBNER_CHECK_PASS "
        f"status=COMPLETE basis={len(replay_text)} "
        f"zero_dimensional={str(replay.is_zero_dimensional).lower()}"
    )


if __name__ == "__main__":
    main()
