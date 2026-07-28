#!/usr/bin/env python3
"""Compute dual exact norms for the complete live cofactor-514 residue."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re

import modal


HERE = Path(__file__).resolve()
ROOT = (
    Path("/repo")
    if Path("/repo").is_dir()
    else HERE.parents[2] if len(HERE.parents) > 2
    else Path("/")
)
PRIMARY = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_m514_live_exact_result.json"
AUDIT = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_m514_live_exact_audit_result.json"
OUTPUT = ROOT / "experiments/prize_resolution/e1_profile_36_mu1_m514_live_norms_result.json"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
P_MAX = (B_PRIZE + 1) * 2**128 - 1
COFACTOR = 514

app = modal.App("e1-profile-36-mu1-m514-live-norms")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


def candidates(
    packet: dict,
) -> list[tuple[int, int, tuple[tuple[int, int], ...]]]:
    found = []
    pattern = r"CANDIDATE E=(\d+) q=(\d+) state=([^\n]+?) roots="
    for row in packet["rows"]:
        for energy, odd_weight, encoded in re.findall(pattern, row["stdout"]):
            state = tuple(
                (int(position), int(coefficient))
                for position, coefficient in re.findall(r"(\d+):(-?\d+),", encoded)
            )
            assert len(state) == 9
            found.append((int(energy), int(odd_weight), state))
    return sorted(found)


def counts(packet: dict) -> Counter[str]:
    result: Counter[str] = Counter()
    for row in packet["rows"]:
        for line in row["stdout"].splitlines():
            if not line.startswith("PASS "):
                continue
            for key, value in re.findall(r"([a-z_0-9]+)=([0-9]+)", line):
                result[key] += int(value)
    return result


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=1)
def measure(
    vectors: list[tuple[int, int, tuple[tuple[int, int], ...]]],
) -> list[dict[str, object]]:
    import subprocess

    from flint import fmpz, fmpz_poly

    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    flint_norms = []
    pari_script = []
    for _, _, state in vectors:
        dense = [0] * 128
        for position, coefficient in state:
            dense[position] = coefficient
        flint_norms.append(abs(int(cyclotomic.resultant(fmpz_poly(dense)))))
        polynomial = "+".join(
            f"({coefficient})*x^{position}" for position, coefficient in state
        )
        pari_script.append(f"print(abs(polresultant(x^128+1,{polynomial})));" )
    completed = subprocess.run(
        ["gp", "-q"],
        input="\n".join(pari_script) + "\n",
        capture_output=True,
        check=True,
        text=True,
        timeout=55,
    )
    pari_norms = [int(line) for line in completed.stdout.splitlines() if line.strip()]
    assert flint_norms == pari_norms and len(flint_norms) == len(vectors)

    rows = []
    for (energy, odd_weight, state), norm in zip(vectors, flint_norms):
        quotient = norm // COFACTOR if norm % COFACTOR == 0 else None
        relation = (
            "below" if quotient is not None and quotient < P_MIN
            else "above" if quotient is not None and quotient > P_MAX
            else "inside" if quotient is not None
            else "not_divisible"
        )
        rows.append({
            "energy": energy,
            "odd_weight": odd_weight,
            "state": state,
            "norm": norm,
            "norm_bits": norm.bit_length(),
            "valuation": (norm & -norm).bit_length() - 1,
            "quotient": quotient,
            "quotient_relation": relation,
            "quotient_is_prime": bool(fmpz(quotient).is_prime()) if quotient else False,
            "flint_pari_agree": True,
        })
    return rows


@app.local_entrypoint()
def main() -> None:
    primary = json.loads(PRIMARY.read_text())
    audit = json.loads(AUDIT.read_text())
    vectors = candidates(primary)
    assert vectors == candidates(audit) and len(vectors) == 8
    primary_counts = counts(primary)
    audit_counts = counts(audit)
    assert primary_counts == audit_counts
    assert primary_counts["orbits"] == 123196
    assert primary_counts["geometry8"] == 4
    assert primary_counts["mod257_8"] == 2
    assert primary_counts["geometry10"] == 8
    assert primary_counts["mod257_10"] == 6
    packet = {
        "schema": "e1-profile-36-mu1-m514-live-norms-v1",
        "complete": False,
        "agreement": False,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "primary_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "audit_sha256": hashlib.sha256(AUDIT.read_bytes()).hexdigest(),
        "candidates": len(vectors),
        "census_counts": dict(sorted(primary_counts.items())),
        "rows": [],
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    packet["rows"] = measure.remote(vectors)
    packet["agreement"] = all(row["flint_pari_agree"] for row in packet["rows"])
    packet["complete"] = True
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    relations: dict[str, int] = {}
    for row in packet["rows"]:
        relation = str(row["quotient_relation"])
        relations[relation] = relations.get(relation, 0) + 1
    print(
        "E1_PROFILE_36_MU1_M514_LIVE_NORMS_PASS "
        f"candidates={len(vectors)} relations={relations} "
        f"census_counts={dict(sorted(primary_counts.items()))} output={OUTPUT}"
    )
