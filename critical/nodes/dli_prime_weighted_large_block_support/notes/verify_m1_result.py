#!/usr/bin/env python3
"""Independent integrity and preregistered-read audit for the DLI M1 result."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "critical/nodes/dli_prime_weighted_large_block_support/notes/m1_dli_m1_results.json"

T2_SMALL = {193, 257, 449, 577, 641, 769, 1153, 1217}
FC_QS = {
    1409, 1601, 2113, 2689, 2753, 3137, 3329, 3457,
    4289, 4481, 4673, 4801, 4993, 5441, 5569, 5953,
    6337, 6529, 6977, 7297, 7489, 7681, 7873, 7937,
    8513, 8641, 9281, 9473, 9601, 9857, 10177, 10369,
}
T3_QS = {193, 257, 449, 577}


def poisson_binomial_pmf(probabilities: list[float]) -> list[float]:
    pmf = [1.0]
    for probability in probabilities:
        updated = [0.0] * (len(pmf) + 1)
        for index, mass in enumerate(pmf):
            updated[index] += mass * (1.0 - probability)
            updated[index + 1] += mass * probability
        pmf = updated
    return pmf


def two_sided_discrete(pmf: list[float], observed: int) -> float:
    lower = sum(pmf[: observed + 1])
    upper = sum(pmf[observed:])
    return min(1.0, 2.0 * min(lower, upper))


def poisson_two_sided(rate: float, observed: int) -> float:
    term = math.exp(-rate)
    lower = 0.0
    cutoff = max(observed, int(rate + 12.0 * math.sqrt(rate + 1.0) + 20.0))
    for index in range(cutoff + 1):
        if index <= observed:
            lower += term
        term *= rate / (index + 1)
    point = math.exp(-rate) * rate**observed / math.factorial(observed)
    upper = 1.0 - lower + point
    return min(1.0, 2.0 * min(lower, max(upper, 0.0)))


def fa_fires(rows: list[dict[str, object]]) -> tuple[bool, dict[int, float]]:
    by_octave: dict[int, list[float]] = {}
    for row in rows:
        bulk = float(row["bulk_ratio"])
        if math.isfinite(bulk) and bulk > 0.0:
            by_octave.setdefault(int(math.log2(int(row["q"]))), []).append(bulk)
    slope = {
        octave: math.exp(sum(math.log(value) for value in values) / len(values))
        / (octave + 0.5)
        for octave, values in by_octave.items()
    }
    octaves = sorted(slope)
    if len(octaves) < 3:
        return False, slope
    top = octaves[-3:]
    increasing = all(slope[left] < slope[right] for left, right in zip(top, top[1:]))
    doubled = slope[top[-1]] >= 2.0 * min(slope.values())
    return increasing and doubled, slope


def main() -> None:
    data = json.loads(RESULT.read_text())
    dag = json.loads((ROOT / "dag.json").read_text())
    node = next(
        item for item in dag["nodes"]
        if item["id"] == "dli_prime_weighted_large_block_support"
    )
    statement = (
        ROOT / "critical/nodes/dli_prime_weighted_large_block_support/statement.md"
    ).read_text()
    repose = (
        ROOT / "critical/nodes/dli_prime_weighted_large_block_support/REPOSE_B_WEAK.md"
    ).read_text()
    consumer = (
        ROOT / "critical/nodes/x4_exactlist_staircase_split/REDUCTION_PACKET.md"
    ).read_text()
    assert "q^{-t+H} * W_cen <= 2^121" in node["statement"]
    assert ("M1 ROUND SURVIVED" in node["statement"])  # master form (import adapt: no falsifier field; #121 custody)
    assert ("2^121" in statement)  # master head repaired at wave-4
    assert ("2^121" in repose or "2^{121}" in repose)  # REPOSE addendum form (in-place mutation refused, #121)
    assert "equivalently half-band count <= 2^121" in consumer

    rows = data["rows"]
    assert len(rows) == 45
    assert data["theta"] == 2.0
    assert all(row["n"] == 64 for row in rows)
    assert all(not row["suborbit_flags"] for row in rows)

    by_depth = {
        depth: [row for row in rows if row["t"] == depth]
        for depth in (2, 3)
    }
    assert {row["q"] for row in by_depth[2]} == T2_SMALL | FC_QS | {12289}
    assert {row["q"] for row in by_depth[3]} == T3_QS
    assert not any(row["t"] not in (2, 3) for row in rows)

    fa_reads = {depth: fa_fires(depth_rows) for depth, depth_rows in by_depth.items()}
    fa_fired_depths = sum(fired for fired, _ in fa_reads.values())
    fa_kill = fa_fired_depths >= 2
    assert not fa_kill
    assert data["Fa_fired"] is fa_kill

    census = sorted(
        (row for row in by_depth[2] if row["q"] in FC_QS),
        key=lambda row: row["q"],
    )
    assert len(census) == 32
    lambdas = [math.comb(32, 3) * 2**3 / (64 * row["q"]) for row in census]
    assert all(value <= 0.5 for value in lambdas)
    assert all(math.comb(32, 4) * 2**4 / (64 * row["q"]) > 0.5 for row in census)

    accidents = sum(
        any(accident["k"] == 3 for accident in row["accidents"])
        for row in census
    )
    orbit_quanta = sum(int(row["V_orbits"].get("3", 0)) for row in census)
    assert accidents == 0
    assert orbit_quanta == 2

    probabilities = [1.0 - math.exp(-value) for value in lambdas]
    p_exceedance = two_sided_discrete(poisson_binomial_pmf(probabilities), accidents)
    lambda_total = sum(lambdas)
    p_quanta = poisson_two_sided(lambda_total, orbit_quanta)
    assert abs(p_exceedance - 0.02581) < 5e-5
    assert abs(lambda_total - 4.350) < 5e-4
    assert abs(p_quanta - 0.3823) < 5e-4
    fc_kill = p_exceedance < 1e-3 or p_quanta < 1e-3
    assert not fc_kill
    assert data["Fc_fired"] is fc_kill
    assert data["verdict"].startswith("C2'' SURVIVES")

    print(
        "PASS DLI_M1_RESULT_AUDIT "
        f"endpoint=2^121 rows={len(rows)} fa_fired_depths={fa_fired_depths} "
        f"fc_accidents={accidents} fc_expected={sum(probabilities):.6f} "
        f"p_exceedance={p_exceedance:.6g} quanta={orbit_quanta} "
        f"lambda={lambda_total:.6f} p_quanta={p_quanta:.6g}"
    )


if __name__ == "__main__":
    main()
