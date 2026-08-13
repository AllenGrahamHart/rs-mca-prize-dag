#!/usr/bin/env python3
"""Probe the first degree-two/four official characteristics for WCL (1,6)."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import modal


CPP = Path(__file__).with_name("dli_wcl_ell1_weight6_extension_row_mitm.cpp")
OUTPUT = Path(__file__).with_name("dli_wcl_ell1_weight6_extension_row_mitm_result.json")
BASES_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)

base = modal.Image.debian_slim().apt_install("g++")
image = (
    base.add_local_file(str(CPP), "/root/search.cpp", copy=True)
    .run_commands("g++ -O3 -std=c++17 /root/search.cpp -o /usr/local/bin/search")
)
app = modal.App("rs-mca-wcl-ell1-weight6-extension-row-mitm")


def is_prime_u64(n: int) -> bool:
    """Deterministic Miller-Rabin for n < 2^64."""
    if n < 2:
        return False
    for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % prime == 0:
            return n == prime
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for base_value in BASES_64:
        if base_value % n == 0:
            continue
        x = pow(base_value, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def first_prime_rows(valuation: int, degree: int, count: int) -> list[dict[str, int]]:
    rows: list[dict[str, int]] = []
    k = 1
    while len(rows) < count:
        p = k * (1 << valuation) + 1
        if is_prime_u64(p):
            q = p**degree
            assert q < 1 << 256
            assert pow(p, degree, 1 << 41) == 1
            if degree > 1:
                assert pow(p, degree // 2, 1 << 41) != 1
            rows.append(
                {
                    "p": p,
                    "q": q,
                    "k": k,
                    "degree": degree,
                    "valuation": valuation,
                }
            )
        k += 2
    return rows


@app.function(image=image, cpu=1, memory=1024, timeout=60, max_containers=64)
def search(row: dict[str, int]) -> dict[str, object]:
    process = subprocess.run(
        ["/usr/local/bin/search", str(row["p"])],
        check=True,
        capture_output=True,
        text=True,
        timeout=55,
    )
    if process.stderr:
        print(process.stderr, end="")
    result = json.loads(process.stdout.strip().splitlines()[-1])
    result.update({key: row[key] for key in ("q", "k", "degree", "valuation")})
    return result


@app.local_entrypoint()
def main(single: int = 0, count: int = 64) -> None:
    panel = first_prime_rows(39, 4, count) + first_prime_rows(40, 2, count)
    if single:
        selected = next((row for row in panel if row["p"] == single), None)
        if selected is None:
            raise ValueError("single characteristic is not in the generated panel")
        print(json.dumps(search.remote(selected), sort_keys=True))
        return

    result: dict[str, object] = {
        "schema": "dli-wcl-ell1-weight6-extension-row-mitm-panel-v1",
        "status": "IN_PROGRESS",
        "panel": panel,
        "rows": [],
        "worker_errors": [],
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    for source, row in zip(
        panel,
        search.map(panel, order_outputs=True, return_exceptions=True),
    ):
        if isinstance(row, BaseException):
            result["worker_errors"].append({"p": source["p"], "error": repr(row)})
        else:
            result["rows"].append(row)
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    result["status"] = "COMPLETE" if not result["worker_errors"] else "PARTIAL"
    result["relation_count"] = sum(
        row["status"] == "FOUND" for row in result["rows"]
    )
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(
        "DLI_WCL_ELL1_WEIGHT6_EXTENSION_ROW_MITM "
        f"status={result['status']} rows={len(result['rows'])}/{len(panel)} "
        f"relations={result['relation_count']}"
    )
