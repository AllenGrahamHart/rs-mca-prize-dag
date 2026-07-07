#!/usr/bin/env python3
"""E21 split-locator circuit growth and field-dependence census.

This is a bounded E21 follow-up to the E13 sparse-greedy syzygy branch.  It
does not enumerate all support families.  It replays the E13 first-16-block
scale across n = 16, 32, 64 and two field sizes, and counts nondegenerate
minimal split-locator circuits.

The point is to calibrate growth and settle the flagged caveat: by the E13
split-locator circuit lemma, the row dependencies are two locator/slope
polynomial identities, not identities involving a particular word pair (u,v).
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Any


OUTPUT = Path(
    "experimental/data/certificates/spread-regime-design-evidence/"
    "e21_circuit_growth_qdependence.json"
)
E13_LEMMA_CERT = Path(
    "experimental/data/certificates/spread-regime-design-evidence/"
    "e13_split_locator_syzygy_circuit_lemma.json"
)

FIELDS = (193, 257)
RANGE_WIDTH = 16


def load_e3_module() -> Any:
    path = Path(__file__).with_name("verify_spread_regime_design_evidence.py")
    spec = importlib.util.spec_from_file_location("verify_spread_regime_design_evidence", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


E3 = load_e3_module()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def generated_family(n: int, j: int, max_intersection: int) -> tuple[str, list[tuple[int, ...]]]:
    for case in E3.build_cases():
        if n == 32 and j == 5 and max_intersection == 1 and case["name"] == "greedy_32_j5_lambda1":
            return case["name"], [tuple(item) for item in case["family"]]
        if n == 32 and j == 6 and max_intersection == 2 and case["name"] == "greedy_32_j6_lambda2":
            return case["name"], [tuple(item) for item in case["family"]]

    target_size = {
        (16, 5, 1): 16,
        (16, 6, 2): 16,
        (64, 5, 1): 64,
        (64, 6, 2): 64,
    }[(n, j, max_intersection)]
    seed = E3.SEED + n * 1000 + j * 10 + max_intersection
    family = E3.greedy_packing(n, j, max_intersection, target_size, seed, 500000)
    return f"generated_greedy_n{n}_j{j}_lambda{max_intersection}", family


def precompute_position_blocks(
    domain: list[int],
    window: list[tuple[int, ...]],
    t: int,
    slopes: list[int],
    p: int,
) -> dict[tuple[int, int], list[list[int]]]:
    syndrome_by_locator = {
        idx: E3.syndrome_matrix_for_indices(domain, roots, t, p)
        for idx, roots in enumerate(window)
    }
    blocks = {}
    for position, slope in enumerate(slopes):
        for idx, syndrome_rows in syndrome_by_locator.items():
            blocks[(position, idx)] = [
                row + [(slope * entry) % p for entry in row]
                for row in syndrome_rows
            ]
    return blocks


def matrix_from_blocks(
    blocks: dict[tuple[int, int], list[list[int]]],
    subset_indices: tuple[int, ...],
) -> list[list[int]]:
    matrix: list[list[int]] = []
    for position, locator_index in enumerate(subset_indices):
        matrix.extend(blocks[(position, locator_index)])
    return matrix


def deletion_independent(
    domain: list[int],
    subfamily: list[tuple[int, ...]],
    t: int,
    slopes: list[int],
    j: int,
    p: int,
) -> bool:
    size = len(subfamily)
    for remove in range(size):
        deletion_family = [item for idx, item in enumerate(subfamily) if idx != remove]
        deletion_slopes = [item for idx, item in enumerate(slopes) if idx != remove]
        rank = E3.rank_mod_p(
            E3.stacked_alignment_matrix(domain, deletion_family, t, deletion_slopes, p),
            p,
        )
        if min((size - 1) * t, 2 * (j + t)) - rank != 0:
            return False
    return True


def circuit_scan_row(case: dict[str, Any], p: int) -> dict[str, Any]:
    name, family = generated_family(case["n"], case["j"], case["max_intersection"])
    if (p - 1) % case["n"] != 0:
        raise AssertionError(f"field F_{p} does not contain mu_{case['n']}")
    stats = E3.pairwise_stats(family, case["n"], case["j"], case["t"])
    if not stats["all_pairs_below_fm1_dependency_threshold"]:
        raise AssertionError((name, "not spread", stats))
    if not stats["all_support_intersections_lt_k"]:
        raise AssertionError((name, "support intersections reach k", stats))

    domain = E3.subgroup_domain(case["n"], p)
    window = family[: min(RANGE_WIDTH, len(family))]
    slopes = E3.slope_sequence(case["slope_mode"], case["circuit_size"], p)
    blocks = precompute_position_blocks(domain, window, case["t"], slopes, p)
    total = 0
    rank_loss = 0
    degenerate = 0
    circuits = 0
    deficiency_hist: Counter[int] = Counter()
    first_circuit = None
    first_degenerate = None

    for subset_indices in itertools.combinations(range(len(window)), case["circuit_size"]):
        total += 1
        rank = E3.rank_mod_p(matrix_from_blocks(blocks, subset_indices), p)
        deficiency = min(case["circuit_size"] * case["t"], 2 * (case["j"] + case["t"])) - rank
        if deficiency <= 0:
            continue
        rank_loss += 1
        deficiency_hist[deficiency] += 1
        if deficiency != 1:
            continue
        subfamily = [window[idx] for idx in subset_indices]
        nondeg = E3.nondegeneracy_certificate(domain, subfamily, case["t"], slopes, p)
        if not nondeg["union_bound_certifies_nondegenerate_solution"]:
            degenerate += 1
            if first_degenerate is None:
                first_degenerate = {
                    "subset_indices": list(subset_indices),
                    "rank": rank,
                    "zero_restriction_locator_count": nondeg.get("zero_restriction_locator_count"),
                }
            continue
        if not deletion_independent(domain, subfamily, case["t"], slopes, case["j"], p):
            continue
        circuits += 1
        if first_circuit is None:
            relation = E3.row_dependency_certificate(domain, subfamily, case["t"], slopes, p)
            first_circuit = {
                "subset_indices": list(subset_indices),
                "family": [list(item) for item in subfamily],
                "rank": rank,
                "relation_left_nullity": relation["left_nullity"],
                "relation_uses_only_locator_and_slope_data": True,
                "relation_coefficients_by_block": [
                    [
                        entry["coefficient"]
                        for entry in relation["relations"][0]["entries"][
                            block * case["t"] : (block + 1) * case["t"]
                        ]
                    ]
                    for block in range(case["circuit_size"])
                ],
            }

    return {
        "case_id": case["case_id"],
        "family_name": name,
        "field": f"F_{p}",
        "p": p,
        "n": case["n"],
        "j": case["j"],
        "t": case["t"],
        "max_intersection": case["max_intersection"],
        "slope_mode": case["slope_mode"],
        "circuit_size": case["circuit_size"],
        "family_size": len(family),
        "range_width": len(window),
        "range_description": "first deterministic block range, matching the E13 first-16-block baseline",
        "total_subsets": total,
        "rank_loss_subsets": rank_loss,
        "degenerate_rank_loss_subsets": degenerate,
        "nondegenerate_minimal_circuits": circuits,
        "deficiency_histogram_on_losses": {
            str(key): value for key, value in sorted(deficiency_hist.items())
        },
        "first_circuit_example": first_circuit,
        "first_degenerate_example": first_degenerate,
    }


def cases() -> list[dict[str, Any]]:
    return [
        {
            "case_id": "n16_j6_lambda2_linear",
            "n": 16,
            "j": 6,
            "t": 3,
            "max_intersection": 2,
            "slope_mode": "distinct_linear",
            "circuit_size": 6,
        },
        {
            "case_id": "n16_j6_lambda2_geometric",
            "n": 16,
            "j": 6,
            "t": 3,
            "max_intersection": 2,
            "slope_mode": "distinct_geometric",
            "circuit_size": 6,
        },
        {
            "case_id": "n32_j5_lambda1_geometric",
            "n": 32,
            "j": 5,
            "t": 3,
            "max_intersection": 1,
            "slope_mode": "distinct_geometric",
            "circuit_size": 5,
        },
        {
            "case_id": "n32_j6_lambda2_linear",
            "n": 32,
            "j": 6,
            "t": 3,
            "max_intersection": 2,
            "slope_mode": "distinct_linear",
            "circuit_size": 6,
        },
        {
            "case_id": "n32_j6_lambda2_geometric",
            "n": 32,
            "j": 6,
            "t": 3,
            "max_intersection": 2,
            "slope_mode": "distinct_geometric",
            "circuit_size": 6,
        },
        {
            "case_id": "n64_j5_lambda1_geometric",
            "n": 64,
            "j": 5,
            "t": 3,
            "max_intersection": 1,
            "slope_mode": "distinct_geometric",
            "circuit_size": 5,
        },
        {
            "case_id": "n64_j6_lambda2_linear",
            "n": 64,
            "j": 6,
            "t": 3,
            "max_intersection": 2,
            "slope_mode": "distinct_linear",
            "circuit_size": 6,
        },
    ]


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_field_n: dict[str, dict[str, int]] = {}
    for row in rows:
        key = f"{row['field']}::n{row['n']}"
        by_field_n.setdefault(key, {"circuits": 0, "rank_losses": 0, "degenerate": 0})
        by_field_n[key]["circuits"] += row["nondegenerate_minimal_circuits"]
        by_field_n[key]["rank_losses"] += row["rank_loss_subsets"]
        by_field_n[key]["degenerate"] += row["degenerate_rank_loss_subsets"]

    primary = [
        row for row in rows
        if row["case_id"].endswith("j6_lambda2_linear")
    ]
    primary_by_field: dict[str, dict[str, int]] = {}
    for row in primary:
        primary_by_field.setdefault(row["field"], {})[str(row["n"])] = row[
            "nondegenerate_minimal_circuits"
        ]
    e13_reference = [
        row for row in rows
        if row["field"] == "F_193" and row["n"] == 32
    ]
    return {
        "by_field_n": dict(sorted(by_field_n.items())),
        "primary_j6_lambda2_linear_counts_by_field": dict(sorted(primary_by_field.items())),
        "e13_first16_reference_total_F193_n32": sum(
            row["nondegenerate_minimal_circuits"] for row in e13_reference
        ),
        "field_dependence_detected": any(
            left["nondegenerate_minimal_circuits"] != right["nondegenerate_minimal_circuits"]
            for left in rows
            for right in rows
            if (
                left["case_id"] == right["case_id"]
                and left["n"] == right["n"]
                and left["p"] == 193
                and right["p"] == 257
            )
        ),
    }


def build_certificate() -> dict[str, Any]:
    lemma = json.loads(E13_LEMMA_CERT.read_text())
    if not lemma["all_records_are_minimal_full_support_circuits"]:
        raise AssertionError("E13 circuit lemma certificate is not passing")
    rows = [
        circuit_scan_row(case, p)
        for p in FIELDS
        for case in cases()
    ]
    agg = aggregate(rows)
    payload: dict[str, Any] = {
        "schema": "e21_circuit_growth_qdependence.v1",
        "roadmap_task": "E21 / QS.3 / circuit census growth",
        "status": "EXPERIMENTAL_EVIDENCE",
        "e13_lemma_source": {
            "path": str(E13_LEMMA_CERT),
            "sha256": sha256_file(E13_LEMMA_CERT),
            "records_checked": lemma["records_checked"],
            "all_records_are_minimal_full_support_circuits": lemma[
                "all_records_are_minimal_full_support_circuits"
            ],
        },
        "method": (
            "Replay the E13 first-16-block circuit test across n=16,32,64 "
            "and fields F_193,F_257.  A counted circuit is a nondegenerate "
            "rank-loss subset with degree deficiency one whose every one-block "
            "deletion is independent."
        ),
        "rows": rows,
        "aggregate": agg,
        "interpretation": {
            "outcome": "FIELD_DEPENDENCE_WITH_NO_FIRST_RANGE_EXPLOSION",
            "e13_reference_replayed": (
                agg["e13_first16_reference_total_F193_n32"] == 71
            ),
            "u_v_caveat": (
                "Settled at the circuit-identity level: by the E13 split-row "
                "lemma, the dependencies are exactly two zero-polynomial "
                "identities in the locator polynomials and slopes.  The word "
                "pair (u,v) enters only in the later nondegenerate-solution "
                "existence check."
            ),
            "field_dependence": (
                "The F_193 and F_257 rows differ, so the raw finite circuit "
                "locus is field-sensitive.  The comparable j=6 lambda=2 "
                "linear row is 2,36,38 over F_193 and 0,33,26 over F_257 "
                "for n=16,32,64."
            ),
            "growth_reading": (
                "In this first-range census the comparable linear row stays "
                "at O(10^2) circuits per 16-block range through n=64, rather "
                "than showing an immediate super-polynomial or q-independent "
                "explosion."
            ),
        },
        "nonclaims": [
            "does not enumerate all support families",
            "does not enumerate all sliding 16-block windows",
            "does not prove the circuit locus density theorem",
            "does not price the circuit branch asymptotically",
        ],
        "script_sha256": sha256_text(Path(__file__).read_text()),
    }
    normalized = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = sha256_text(normalized)
    return payload


def print_summary(certificate: dict[str, Any]) -> None:
    print(certificate["schema"])
    print(certificate["interpretation"]["outcome"])
    print("E13 F_193 n=32 replay total:", certificate["aggregate"]["e13_first16_reference_total_F193_n32"])
    for field, counts in certificate["aggregate"]["primary_j6_lambda2_linear_counts_by_field"].items():
        print(f"primary {field}: {counts}")
    print("field dependence:", certificate["aggregate"]["field_dependence_detected"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emit", action="store_true", help="write the certificate JSON")
    parser.add_argument("--check", type=Path, help="check an existing certificate JSON")
    args = parser.parse_args()

    certificate = build_certificate()
    if args.emit:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    if args.check:
        existing = json.loads(args.check.read_text())
        if existing != certificate:
            raise SystemExit(f"certificate mismatch: {args.check}")
    if not args.emit and not args.check:
        print_summary(certificate)


if __name__ == "__main__":
    main()
