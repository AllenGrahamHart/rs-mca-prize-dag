#!/usr/bin/env python3
"""Compute dual exact norms for the discovered mod-257 low-energy witnesses."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import modal


HERE = Path(__file__).resolve()
ROOT = (
    Path("/repo")
    if Path("/repo").is_dir()
    else HERE.parents[2] if len(HERE.parents) > 2
    else Path("/")
)
OUTPUT = ROOT / (
    "experiments/prize_resolution/"
    "e1_profile_36_m514_boundary_witness_norms_result.json"
)
SEARCH = ROOT / (
    "experiments/prize_resolution/"
    "e1_profile_36_m514_mod257_low_energy_search_result.json"
)
B_PRIZE = 317494674775468773183020924238786383963
P_MIN = B_PRIZE * 2**128
P_MAX = (B_PRIZE + 1) * 2**128 - 1
COFACTOR = 514

app = modal.App("e1-profile-36-m514-boundary-witness-norms")
image = modal.Image.debian_slim().apt_install("pari-gp").pip_install("python-flint")


def multiplicity(state: tuple[tuple[int, int], ...]) -> int:
    support = [position for position, value in state if abs(value) == 1]
    for derivative in range(16):
        if sum((derivative & ~position) == 0 for position in support) % 2:
            return derivative
    return 16


def energy(state: tuple[tuple[int, int], ...]) -> int:
    values = [0] * 64
    for index, (left, left_value) in enumerate(state):
        for right, right_value in state[index + 1 :]:
            delta = right - left
            if delta < 64:
                values[delta] += left_value * right_value
            elif delta > 64:
                values[128 - delta] -= left_value * right_value
    return sum(value * value for value in values)


def vanishes_mod_257(state: tuple[tuple[int, int], ...]) -> bool:
    return sum(
        coefficient * pow(3, position, 257) for position, coefficient in state
    ) % 257 == 0


@app.function(image=image, cpu=1.0, memory=256, timeout=60, max_containers=1)
def measure(
    vectors: tuple[tuple[tuple[int, int], ...], ...],
) -> list[dict[str, object]]:
    import subprocess

    from flint import fmpz, fmpz_poly

    cyclotomic = fmpz_poly([1] + [0] * 127 + [1])
    flint_norms = []
    pari_script = []
    for state in vectors:
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
    for state, norm in zip(vectors, flint_norms):
        quotient = norm // COFACTOR if norm % COFACTOR == 0 else None
        relation = (
            "below" if quotient is not None and quotient < P_MIN
            else "above" if quotient is not None and quotient > P_MAX
            else "inside" if quotient is not None
            else "not_divisible"
        )
        rows.append({
            "state": state,
            "energy": energy(state),
            "multiplicity": multiplicity(state),
            "vanishes_mod_257": vanishes_mod_257(state),
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
    search_packet = json.loads(SEARCH.read_text())
    witnesses = tuple(
        tuple((int(position), int(value)) for position, value in row["state"])
        for row in search_packet["rows"]
        if row["found"]
    )
    assert len(witnesses) == 5
    assert all(2 <= energy(state) <= 17 for state in witnesses)
    assert all(multiplicity(state) == 1 for state in witnesses)
    assert all(vanishes_mod_257(state) for state in witnesses)
    packet = {
        "schema": "e1-profile-36-m514-low-energy-witness-norms-v1",
        "complete": False,
        "agreement": False,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "search_sha256": hashlib.sha256(SEARCH.read_bytes()).hexdigest(),
        "search_app": "ap-vCwCehrnyit7WrDEjorD0c",
        "rows": [],
    }
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    packet["rows"] = measure.remote(witnesses)
    packet["agreement"] = all(row["flint_pari_agree"] for row in packet["rows"])
    packet["complete"] = True
    OUTPUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")
    relations: dict[str, int] = {}
    for row in packet["rows"]:
        relation = str(row["quotient_relation"])
        relations[relation] = relations.get(relation, 0) + 1
    print(
        "E1_PROFILE_36_M514_BOUNDARY_WITNESS_NORMS_PASS "
        f"witnesses={len(witnesses)} relations={relations} output={OUTPUT}"
    )
