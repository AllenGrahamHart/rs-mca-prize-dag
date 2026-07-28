#!/usr/bin/env python3
"""Classify every E13 odd norm part above the pair-feasible floor."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve().parent
CENSUS = HERE / "e13_four_profile_census_result.json"
NORMS = HERE / "e13_four_profile_norm_result.json"
RESULT = HERE / "e13_large_odd_candidate_result.json"
app = modal.App("e1-n256-e13-large-odd-candidate")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=2)
def classify_flint(values: list[int]) -> list[bool]:
    from flint import fmpz
    return [bool(fmpz(value).is_prime()) for value in values]


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=2)
def classify_pari(values: list[int]) -> list[bool]:
    import subprocess
    script = "\n".join(f"print(isprime({value}));" for value in values) + "\n"
    completed = subprocess.run(["gp", "-q"], input=script, capture_output=True,
                               check=True, text=True, timeout=55)
    flags = [line.strip() == "1" for line in completed.stdout.splitlines() if line.strip()]
    if len(flags) != len(values):
        raise RuntimeError(f"expected {len(values)} PARI flags, got {len(flags)}")
    return flags


def load_candidates() -> list[dict[str, object]]:
    census = json.loads(CENSUS.read_text()); norms = json.loads(NORMS.read_text())
    if not census["complete"] or not norms["complete"] or not norms["agreement"]:
        raise RuntimeError("E13 source packets are incomplete")
    vectors = []
    for row in census["rows"]:
        for match in row["primary"]["matches"]:
            vectors.append({
                "template": int(row["template"]),
                "light": [int(value) for value in row["primary"]["light"]],
                "profile": int(match["profile"]),
                "positions": [int(value) for value in match["positions"]],
                "coefficients": [int(value) for value in match["coefficients"]],
            })
    exact_norms = [int(value)
                   for row in sorted(norms["flint"], key=lambda item: int(item["batch"]))
                   for value in row["norms"]]
    if not len(vectors) == len(exact_norms) == int(norms["vectors"]):
        raise RuntimeError("E13 vector/norm cardinality mismatch")
    candidates = []
    for index, (vector, norm) in enumerate(zip(vectors, exact_norms)):
        valuation = (norm & -norm).bit_length() - 1
        odd_part = norm >> valuation
        if odd_part >= 2**250:
            candidates.append({"index": index, "norm": norm, "valuation": valuation,
                               "odd_part": odd_part, "residue_mod_256": odd_part % 256,
                               **vector})
    return candidates


@app.local_entrypoint()
def main() -> None:
    candidates = load_candidates(); values = [int(row["odd_part"]) for row in candidates]
    flint_flags = classify_flint.remote(values); pari_flags = classify_pari.remote(values)
    if flint_flags != pari_flags:
        raise RuntimeError("FLINT/PARI E13 primality mismatch")
    for row, flag in zip(candidates, flint_flags):
        row["is_prime"] = flag
        row["pair_feasible_prime"] = bool(
            flag and int(row["odd_part"]) > 2**250
            and int(row["residue_mod_256"]) == 1)
    packet = {
        "schema": "e1-e13-large-odd-candidate-v1", "complete": True,
        "agreement": True,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "census_sha256": hashlib.sha256(CENSUS.read_bytes()).hexdigest(),
        "norm_sha256": hashlib.sha256(NORMS.read_bytes()).hexdigest(),
        "threshold": 2**250, "modulus": 256, "candidates": candidates,
        "summary": {
            "candidates": len(candidates), "distinct_odd_parts": len(set(values)),
            "prime_candidates": sum(flag for flag in flint_flags),
            "congruence_candidates": sum(value % 256 == 1 for value in values),
            "pair_feasible_prime_candidates": sum(bool(row["pair_feasible_prime"])
                                                  for row in candidates),
        },
    }
    RESULT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print("E13_LARGE_ODD_CANDIDATE " + json.dumps(packet["summary"], sort_keys=True))
    print(f"E13_LARGE_ODD_CANDIDATE_RESULT {RESULT}")
