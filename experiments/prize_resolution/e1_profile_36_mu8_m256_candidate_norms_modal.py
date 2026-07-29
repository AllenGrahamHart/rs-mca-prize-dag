#!/usr/bin/env python3
"""Compute dual exact norms for the complete cofactor-256 live residue."""

from __future__ import annotations

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
PRIMARY = ROOT / "experiments/prize_resolution/e1_profile_36_mu8_m256_live_exact_result.json"
AUDIT = ROOT / "experiments/prize_resolution/e1_profile_36_mu8_m256_live_exact_audit_result.json"
OUTPUT = ROOT / "experiments/prize_resolution/e1_profile_36_mu8_m256_candidate_norms_result.json"
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
P_MAX = (B_PRIZE + 1) * 2**128 - 1
COFACTOR = 256

app = modal.App("e1-profile-36-mu8-m256-candidate-norms")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


def candidates(
    packet: dict,
) -> list[tuple[int, int, int, tuple[tuple[int, int], ...]]]:
    found = []
    pattern = re.compile(
        r"CANDIDATE E=(\d+) q=(\d+) L=(\d+) state=([^\n]+)"
    )
    for row in packet["rows"]:
        for energy, odd_weight, l1_norm, encoded in pattern.findall(row["stdout"]):
            state = tuple(
                (int(position), int(coefficient))
                for position, coefficient in re.findall(r"(\d+):(-?\d+),", encoded)
            )
            assert len(state) == 9
            found.append((int(energy), int(odd_weight), int(l1_norm), state))
    return sorted(found)


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=1)
def measure(
    vectors: list[tuple[int, int, int, tuple[tuple[int, int], ...]]],
) -> list[dict[str, object]]:
    import subprocess

    from flint import fmpz, fmpz_poly

    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    flint_norms = []
    pari_script = []
    for _, _, _, state in vectors:
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
    for (energy, odd_weight, l1_norm, state), norm in zip(vectors, flint_norms):
        valuation = (norm & -norm).bit_length() - 1
        divisible = norm % COFACTOR == 0
        quotient = norm // COFACTOR if divisible else None
        relation = (
            "wrong_valuation" if valuation != 8
            else "below" if quotient is not None and quotient < P_MIN
            else "above" if quotient is not None and quotient > P_MAX
            else "inside" if quotient is not None
            else "not_divisible"
        )
        rows.append({
            "energy": energy,
            "odd_weight": odd_weight,
            "l1_norm": l1_norm,
            "state": state,
            "norm": norm,
            "norm_bits": norm.bit_length(),
            "valuation": valuation,
            "quotient": quotient,
            "quotient_relation": relation,
            "quotient_is_prime": bool(fmpz(quotient).is_prime()) if quotient else False,
            "flint_pari_agree": True,
        })
    return rows


@app.local_entrypoint()
def main() -> None:
    primary_packet = json.loads(PRIMARY.read_text())
    audit_packet = json.loads(AUDIT.read_text())
    primary_candidates = candidates(primary_packet)
    audit_candidates = candidates(audit_packet)
    assert primary_candidates == audit_candidates
    assert len(primary_candidates) == 54
    unique_candidates = sorted(set(primary_candidates))
    packet = {
        "schema": "e1-profile-36-mu8-m256-candidate-norms-v1",
        "complete": False,
        "agreement": False,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "primary_sha256": hashlib.sha256(PRIMARY.read_bytes()).hexdigest(),
        "audit_sha256": hashlib.sha256(AUDIT.read_bytes()).hexdigest(),
        "candidate_lines": len(primary_candidates),
        "unique_candidates": len(unique_candidates),
        "rows": [],
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    packet["rows"] = measure.remote(unique_candidates)
    packet["agreement"] = all(row["flint_pari_agree"] for row in packet["rows"])
    packet["complete"] = True
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    relations: dict[str, int] = {}
    energies: dict[str, int] = {}
    for row in packet["rows"]:
        relation = str(row["quotient_relation"])
        relations[relation] = relations.get(relation, 0) + 1
        energy = str(row["energy"])
        energies[energy] = energies.get(energy, 0) + 1
    packet["relations"] = relations
    packet["energies"] = energies
    packet["max_quotient"] = max(int(row["quotient"]) for row in packet["rows"])
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    print(
        "E1_PROFILE_36_MU8_M256_CANDIDATE_NORMS_PASS "
        f"candidate_lines={len(primary_candidates)} "
        f"unique_candidates={len(unique_candidates)} relations={relations} "
        f"energies={energies} max_quotient={packet['max_quotient']} "
        f"output={OUTPUT}"
    )


if __name__ == "__main__":
    main()
