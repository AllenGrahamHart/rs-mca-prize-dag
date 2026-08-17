#!/usr/bin/env python3
"""Verify the exact K'=72 nested-carrier flag arithmetic."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
CONTRACT = Path(__file__).with_name("source_contract.json")
CONTRACT_SHA256 = "1965a3805d39369e088dce2c27099f42f5b833aa20a1bf4d212f3c6b272d79a6"
K71_VERIFY = ROOT / "background/nodes/rate_half_mca_rank11_k71_carrier_trichotomy_payment/verify.py"


class Reject(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, "module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K71 = load_module("k71_for_k72_flag", K71_VERIFY)


def charged(caps: tuple[int, ...], union: int, dimension: int) -> tuple[int, ...]:
    return K71.charged_vector(72, caps, union, dimension)


def premium(caps: tuple[int, ...]) -> int:
    return K71.premium(caps)


def validate(data: object) -> dict[str, object]:
    require(isinstance(data, dict), "contract")
    require(data["schema"] == "rate-half-mca-sparse-circuit-k72-nested-carrier-flag-router-v1", "schema")
    p = data["parameters"]
    require((p["Kprime"], p["q"], p["m"]) == (72, 62, 67544), "row")
    require(p["maxima"] == {"2": 28, "3": 30, "4": 31, "5": 31}, "maxima")
    require(p["carrier_sizes"] == {"2": 29, "3": 32, "4": 34, "5": 35}, "sizes")
    caps = tuple(p["active_caps"])
    cases = p["cases"]
    require(cases["overlap_two"] == {"status": "impossible", "union": 35}, "impossible")

    checks = 0
    for name in ("overlap_one_nested", "overlap_zero_transverse", "overlap_zero_nested"):
        row = cases[name]
        value = premium(charged(caps, row["union"], row["dimension"]))
        require(value == row["premium"], name)
        checks += 1
    flag = cases["overlap_one_flag"]
    flag_caps = charged(caps, flag["outer_union"], flag["outer_dimension"])
    flag_caps = charged(flag_caps, flag["inner_union"], flag["inner_dimension"])
    require(premium(flag_caps) == flag["premium"], "flag")
    require(cases["overlap_one_nested"]["premium"] <= p["premium_ceiling"], "nested safe")
    require(cases["overlap_zero_nested"]["premium"] <= p["premium_ceiling"], "zero nested safe")
    require(cases["overlap_zero_transverse"]["premium"] > p["premium_ceiling"], "transverse honest")
    require(flag["premium"] > p["premium_ceiling"], "flag honest")
    return {"cases": 5, "arithmetic_checks": checks + 5}


def tamper_selftest(data: dict[str, object]) -> int:
    mutations = (
        lambda item: item.__setitem__("schema", "wrong"),
        lambda item: item["parameters"].__setitem__("q", 61),
        lambda item: item["parameters"]["carrier_sizes"].__setitem__("3", 33),
        lambda item: item["parameters"]["cases"]["overlap_two"].__setitem__("status", "possible"),
        lambda item: item["parameters"]["cases"]["overlap_one_nested"].__setitem__("dimension", 5),
        lambda item: item["parameters"]["cases"]["overlap_zero_transverse"].__setitem__("premium", 0),
    )
    rejected = 0
    for mutate in mutations:
        trial = copy.deepcopy(data)
        mutate(trial)
        try:
            validate(trial)
        except (Reject, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "tamper rejection")
    return rejected


def main() -> int:
    raw = CONTRACT.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == CONTRACT_SHA256, "contract hash")
    data = json.loads(raw)
    result = validate(data)
    result["contract_sha256"] = CONTRACT_SHA256
    result["tamper_rejected"] = tamper_selftest(data)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Reject as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        raise SystemExit(1)
