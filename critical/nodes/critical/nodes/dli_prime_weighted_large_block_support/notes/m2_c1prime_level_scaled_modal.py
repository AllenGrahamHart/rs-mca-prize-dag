#!/usr/bin/env python3
"""M2: preregistered out-of-sample attack on level-scaled C1'."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import modal


ROOT = Path("/repo") if Path("/repo").is_dir() else Path(__file__).resolve().parents[4]
SOURCE = ROOT / "m1_dli_m1_results.json"
OUTPUT = ROOT / "m2_c1prime_level_scaled_results.json"

ROWS = {
    1: (193, 449, 769, 1409, 3137, 5569, 7937, 12289),
    2: (193, 257, 449, 577),
}
N = 32
NPRIME = 64

app = modal.App("rs-mca-dli-m2-c1prime")
image = modal.Image.debian_slim().pip_install("numpy").add_local_dir(
    str(ROOT), remote_path="/repo", copy=True
)


def primitive_root(q: int) -> int:
    remaining = q - 1
    factors: set[int] = set()
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.add(divisor)
            remaining //= divisor
        divisor += 1
    if remaining > 1:
        factors.add(remaining)
    candidate = 2
    while any(pow(candidate, (q - 1) // factor, q) == 1 for factor in factors):
        candidate += 1
    return candidate


def orbit_key(vector: tuple[int, ...]) -> tuple[int, ...]:
    best: tuple[int, ...] | None = None
    for shift in range(2 * N):
        moved = [0] * N
        for exponent, coefficient in enumerate(vector):
            if coefficient == 0:
                continue
            target = (exponent + shift) % (2 * N)
            if target >= N:
                moved[target - N] -= coefficient
            else:
                moved[target] += coefficient
        key = tuple(moved)
        if best is None or key < best:
            best = key
    assert best is not None
    return best


@app.function(image=image, cpu=2, memory=2048, timeout=150, max_containers=64)
def primitive_orbit_count(payload: tuple[int, int, int]) -> dict[str, int]:
    import numpy as np

    q, level, weight = payload
    omega = pow(primitive_root(q), (q - 1) // NPRIME, q)
    odd_powers = [
        np.array(
            [pow(omega, (2 * ell - 1) * exponent, q) for exponent in range(N)],
            dtype=np.int64,
        )
        for ell in range(1, level + 1)
    ]
    signs = np.array(list(itertools.product((1, -1), repeat=weight - 1)), dtype=np.int64)
    signs = np.hstack([np.ones((len(signs), 1), dtype=np.int64), signs])
    combinations = itertools.combinations(range(N), weight)
    representatives: set[tuple[int, ...]] = set()
    chunk_size = 100_000

    while True:
        chunk = list(itertools.islice(combinations, chunk_size))
        if not chunk:
            break
        supports = np.asarray(chunk, dtype=np.int64)
        hit_mask = np.ones((len(supports), len(signs)), dtype=bool)
        for powers in odd_powers:
            hit_mask &= (powers[supports] @ signs.T) % q == 0
        for support_index, sign_index in np.argwhere(hit_mask):
            support = tuple(int(value) for value in supports[support_index])
            signed = tuple(int(value) for value in signs[sign_index])
            primitive = True
            for subset_mask in range(1, (1 << weight) - 1):
                if all(
                    sum(
                        signed[index] * pow(
                            omega,
                            (2 * ell - 1) * support[index],
                            q,
                        )
                        for index in range(weight)
                        if (subset_mask >> index) & 1
                    )
                    % q
                    != 0
                    for ell in range(1, level + 1)
                ):
                    continue
                # A proper subvector is a vanisher only if every equation is zero.
                if all(
                    sum(
                        signed[index] * pow(
                            omega,
                            (2 * ell - 1) * support[index],
                            q,
                        )
                        for index in range(weight)
                        if (subset_mask >> index) & 1
                    )
                    % q
                    == 0
                    for ell in range(1, level + 1)
                ):
                    primitive = False
                    break
            if not primitive:
                continue
            vector = [0] * N
            for exponent, coefficient in zip(support, signed):
                vector[exponent] = coefficient
            representatives.add(orbit_key(tuple(vector)))

    return {
        "q": q,
        "level": level,
        "weight": weight,
        "primitive_orbits": len(representatives),
    }


def full_spectrum_e(row: dict[str, object], q: int, level: int) -> Fraction:
    assert row["q"] == q and (row["t"] + 1) // 2 == level
    assert not row["suborbit_flags"]
    weighted = Fraction(1, 1)
    for weight_text, orbit_count in row["V_orbits"].items():
        weight = int(weight_text)
        weighted += Fraction(int(orbit_count) * 2 * N, 2**weight)
    return Fraction(q**level, 2**N) * weighted


@app.local_entrypoint()
def main() -> None:
    print("M2 PREREG: w_max(L)=L+5; KILL iff any exact K_prime > 4")
    source = json.loads(SOURCE.read_text())
    source_rows = {
        ((row["t"] + 1) // 2, row["q"]): row
        for row in source["rows"]
    }
    payloads = [
        (q, level, weight)
        for level, qs in ROWS.items()
        for q in qs
        for weight in range(level + 1, level + 6)
    ]
    returned = list(primitive_orbit_count.map(payloads, return_exceptions=True))
    failures = [row for row in returned if not isinstance(row, dict)]
    if failures:
        raise RuntimeError(f"M2 worker failures: {failures[:3]}")
    counts = {
        (row["level"], row["q"], row["weight"]): row["primitive_orbits"]
        for row in returned
    }

    reports = []
    killed = False
    for level, qs in ROWS.items():
        for q in qs:
            source_row = source_rows[(level, q)]
            e_value = full_spectrum_e(source_row, q, level)
            r_value = Fraction(q**level, 2**N)
            ledger = sum(
                Fraction(counts[(level, q, weight)] * 2 * N, 2**weight)
                for weight in range(level + 1, level + 6)
            )
            allowance = 4 * r_value * (1 + ledger)
            excess = e_value - 1
            row_killed = excess > allowance
            killed |= row_killed
            ratio = float(excess / (r_value * (1 + ledger)))
            report = {
                "level": level,
                "q": q,
                "N": N,
                "weights": list(range(level + 1, level + 6)),
                "primitive_orbits": {
                    str(weight): counts[(level, q, weight)]
                    for weight in range(level + 1, level + 6)
                },
                "E_minus_1": [excess.numerator, excess.denominator],
                "r": [r_value.numerator, r_value.denominator],
                "W_cl": [ledger.numerator, ledger.denominator],
                "K_prime": ratio,
                "killed": row_killed,
            }
            reports.append(report)
            print(
                f"L={level} q={q}: K_prime={ratio:.9f} "
                f"orbits={report['primitive_orbits']} "
                f"{'KILL' if row_killed else 'survives'}"
            )

    result = {
        "schema": "dli-c1prime-m2-v1",
        "pose": "w_max(L)=L+5, exact K_prime<=4",
        "rows": reports,
        "killed": killed,
        "verdict": "C1_prime_REFUTED" if killed else "C1_prime_SURVIVES_M2",
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"M2 VERDICT: {result['verdict']}")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
