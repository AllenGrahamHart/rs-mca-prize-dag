#!/usr/bin/env python3
"""Validate one hard-capped m=16 R_12 Singular pilot result."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


APP_NAME = "l1-mersenne-m16-r12-singular-pilot"
P = 8191
M = 16
H = 15
RAW_DEGREE_BOUND = 11520


def truncated_binomial() -> str:
    terms = []
    rising = "1"
    factorial = 1
    for r in range(H + 1):
        if r:
            rising = f"({rising})*(s+{r - 1})"
            factorial = factorial * r % P
        coefficient = rising if r == 0 else f"({pow(factorial, -1, P)})*({rising})"
        terms.append(f"({coefficient})*w^{H - r}")
    return "+".join(terms)


def singular_program() -> str:
    return "\n".join(
        [
            f"ring r={P},(w,z,t,s),lp;",
            "option(redSB);",
            f"poly Ps={truncated_binomial()};",
            f"poly Q=resultant(Ps,z-w^{M},w);",
            "matrix qc=coeffs(Q,z);",
            "poly C=qc[1,1];",
            "poly q1=qc[15,1];",
            "poly q2=qc[14,1];",
            "poly q14=qc[2,1];",
            "poly q13=qc[3,1];",
            'if (nrows(qc)!=16) { print("L1_M16_R12_PREFLIGHT_ROWS_ERROR"); quit; }',
            'if (qc[16,1]!=1) { print("L1_M16_R12_PREFLIGHT_MONIC_ERROR"); quit; }',
            'if (deg(q1)!=16) { print("L1_M16_R12_PREFLIGHT_Q1_ERROR"); quit; }',
            'if (deg(q2)!=32) { print("L1_M16_R12_PREFLIGHT_Q2_ERROR"); quit; }',
            'if (deg(q13)!=208) { print("L1_M16_R12_PREFLIGHT_Q13_ERROR"); quit; }',
            'if (deg(q14)!=224) { print("L1_M16_R12_PREFLIGHT_Q14_ERROR"); quit; }',
            'if (deg(C)!=240) { print("L1_M16_R12_PREFLIGHT_C_ERROR"); quit; }',
            "poly F1=C*subst(q1,s,t)-q14;",
            "poly F2=C*subst(q2,s,t)-q13;",
            "poly R12=resultant(F1,F2,t);",
            'print("L1_M16_R12_META_BEGIN");',
            "nrows(qc);",
            "size(Q);",
            "deg(q1);",
            "deg(q2);",
            "deg(q13);",
            "deg(q14);",
            "deg(C);",
            "deg(F1);",
            "size(F1);",
            "deg(F2);",
            "size(F2);",
            "deg(R12);",
            "size(R12);",
            'print("L1_M16_R12_META_END");',
            'print("L1_M16_R12_POLY_BEGIN");',
            "R12;",
            'print("L1_M16_R12_POLY_END");',
            "quit;",
        ]
    ) + "\n"


def load_result(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text())
    assert isinstance(value, dict)
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("result", type=Path)
    args = parser.parse_args()
    result = load_result(args.result)

    expected_program_hash = hashlib.sha256(singular_program().encode()).hexdigest()
    assert result["app"] == APP_NAME
    assert (result["p"], result["m"], result["h"]) == (P, M, H)
    assert result["program_sha256"] == expected_program_hash
    assert result["raw_degree_bound"] == RAW_DEGREE_BOUND
    assert result["status"] in {"COMPLETE", "TIMEOUT", "ERROR", "INCOMPLETE"}

    if result["status"] == "INCOMPLETE":
        assert result["app_id"] == "ap-wGlT1diHx4C7gUii0LhVyq"
        assert result["phase"] == "IMAGE_BUILD"
        assert result["reason"] == "DEFAULT_APT_RECOMMENDS_FANOUT"
        assert result["algebra_started"] is False
        assert result["retry_launched"] is False
        assert result["archives_mb"] == 1077
        assert result["installed_mb"] == 4098
        assert result["packages_new"] == 891
        assert result["packages_upgraded"] == 29
        assert result["packages_reached_before_abort"] == 310
        assert abs(float(result["cpu_cost_usd"]) - 0.00340405) < 1e-12
        assert abs(float(result["memory_cost_usd"]) - 0.00007667) < 1e-12
        assert abs(float(result["total_cost_usd"]) - 0.00348072) < 1e-12
        print(
            "L1_MERSENNE_M16_R12_SINGULAR_PILOT_CHECK_PASS "
            "status=INCOMPLETE phase=IMAGE_BUILD algebra_started=false "
            f"cost_usd={result['total_cost_usd']}"
        )
        return

    assert 0 <= float(result["seconds"]) <= 180
    assert 0 <= int(result["peak_mb"]) <= 2048

    if result["status"] == "COMPLETE":
        meta = [int(value) for value in str(result["meta"]).splitlines()]
        assert len(meta) == 13
        (
            rows,
            size_q,
            degree_q1,
            degree_q2,
            degree_q13,
            degree_q14,
            degree_c,
            degree_f1,
            size_f1,
            degree_f2,
            size_f2,
            degree_r12,
            size_r12,
        ) = meta
        assert rows == 16 and size_q > 0
        assert (degree_q1, degree_q2, degree_q13, degree_q14, degree_c) == (
            16,
            32,
            208,
            224,
            240,
        )
        assert degree_f1 == 256 and size_f1 > 0
        assert degree_f2 == 272 and size_f2 > 0
        assert 0 <= degree_r12 <= RAW_DEGREE_BOUND and size_r12 > 0
        assert int(result["r12_text_bytes"]) > 0
        digest = str(result["r12_text_sha256"])
        assert len(digest) == 64 and set(digest) <= set("0123456789abcdef")
    else:
        assert str(result["stdout_tail"]) or str(result["stderr_tail"]) or result["status"] == "TIMEOUT"

    print(
        "L1_MERSENNE_M16_R12_SINGULAR_PILOT_CHECK_PASS "
        f"status={result['status']} seconds={result['seconds']} peak_mb={result['peak_mb']}"
    )


if __name__ == "__main__":
    main()
