#!/usr/bin/env python3
"""Split oversized critical-node notebooks into checked, indexed packets.

The refactor is intentionally presentation-only.  Each packet sequence must
reassemble byte-for-byte to the pre-refactor document hash.  The short parent
document remains the live entry point; node.json continues to own truth and
dependency status.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Document:
    source: str
    sha256: str
    line_count: int
    packet_dir: str
    packets: tuple[tuple[str, int, int, tuple[str, ...]], ...]
    index: str
    addenda: tuple[tuple[str, tuple[str, ...]], ...] = ()


DOCUMENTS = (
    Document(
        source="critical/nodes/l1_mixed_petal_amplification/statement.md",
        sha256="b584bf55b8e02310637fd59ed67494b7049cdc0af8d645c16c030db50986321f",
        line_count=1356,
        packet_dir="critical/nodes/l1_mixed_petal_amplification/statement_sections",
        packets=(
            ("00-original-contract-and-evidence.md", 1, 66, ("l1_mixed_petal_amplification",)),
            ("01-local-first-owner-payments.md", 67, 291, (
                "l1_first_match_totality_scope_pin",
                "l1_fixed_source_quotient_partition_anchor_census",
                "l1_fixed_source_anchored_triple_polarity_closure",
                "l1_tame_fixed_petal_refinement_census",
            )),
            ("02-global-exact-shell-route.md", 292, 943, (
                "l1_exact_shell_prefix_hankel_bridge",
                "l1_exact_shell_fixed_cofactor_prefix_transport",
                "l1_full_locator_pade_section_all_cofactors",
                "l1_pade_remainder_jacobian_tangent_dichotomy",
            )),
            ("03-official-checkpoint-route.md", 944, 1287, (
                "l1_official_checkpoint_characteristic_atlas",
                "l1_official_first_checkpoint_split_pencil_reduction",
                "l1_mersenne_hnf_order_zero_quadratic_collisionfree_exclusion",
            )),
            ("04-balanced-pencil-atlas.md", 1288, 1356, (
                "l1_balanced_pencil_anchor_determinant_atlas",
            )),
        ),
        index="""# L1: mixed-petal / diffuse partial-petal amplification

## Live target

At every official row and for every received word, bound the mixed-petal and
diffuse partial-petal contribution to the exact-shell image fiber by the
corrected finite reserve.  The target remains open.  Its two complete routes
are:

1. a row-sharp primitive received-word Toeplitz/Pade prefix bound with the
   tangent and quotient-periodic shells paid separately; or
2. an aggregate first-owner payment of every remaining local pullback,
   refinement, wild, and balanced-pencil class.

The exact proposition and current upstream typing are in `node.json`.  This
file is the live entry point, not a proof and not a status claim.

## Sub-DAG packets

- `statement_sections/00-original-contract-and-evidence.md`: original target,
  provenance, falsifier, and known-mass witness.
- `statement_sections/01-local-first-owner-payments.md`: local first-match and
  anchored-payment chain.
- `statement_sections/02-global-exact-shell-route.md`: exact-shell,
  Toeplitz/Pade, and tangent split.
- `statement_sections/03-official-checkpoint-route.md`: official
  characteristic checkpoint reductions.
- `statement_sections/04-balanced-pencil-atlas.md`: balanced-pencil terminal.
- `statement_addenda/05-round21-v4-audit.md`: Round-21 survey status and
  canonical interpretation correction.
- `statement_addenda/06-round21-growing-petal-repose.md`: Round-21 exact-box
  diagnosis and growing-petal re-pose.
- `statement_addenda/07-round22-ell-sweep.md`: Round-22 ell-sweep — F-w1
  exhaustively silent at the proper-band frontier; normaliser amended to
  `N_{k+1}/q`.

`statement_sections/document.json` pins the pre-refactor byte stream and the
existing DAG nodes represented by each packet.  Run
`tools/ramguard tiny -- python3 tools/refactor_critical_node_documents.py`
to verify lossless decomposition.
""",
        addenda=(
            (
                "critical/nodes/l1_mixed_petal_amplification/statement_addenda/05-round21-v4-audit.md",
                ("l1_mixed_petal_amplification",),
            ),
            (
                "critical/nodes/l1_mixed_petal_amplification/statement_addenda/06-round21-growing-petal-repose.md",
                ("l1_mixed_petal_amplification",),
            ),
            (
                "critical/nodes/l1_mixed_petal_amplification/statement_addenda/07-round22-ell-sweep.md",
                ("l1_mixed_petal_amplification",),
            ),
        ),
    ),
    Document(
        source="critical/nodes/l1_mixed_petal_amplification/attack.md",
        sha256="6b1287214fbf161c2baabbb571a8b19d5dd6275b4c8b687ccb2938761c69ed46",
        line_count=940,
        packet_dir="critical/nodes/l1_mixed_petal_amplification/attack_sections",
        packets=(
            ("00-falsification-and-growth.md", 1, 24, ("l1_mixed_petal_amplification",)),
            ("01-global-exact-shell-program.md", 25, 361, (
                "l1_exact_shell_prefix_hankel_bridge",
                "l1_pade_remainder_jacobian_tangent_dichotomy",
            )),
            ("02-local-first-owner-program.md", 362, 468, (
                "l1_first_match_totality_scope_pin",
                "l1_fixed_source_anchored_triple_polarity_closure",
            )),
            ("03-order-zero-checkpoint-program.md", 469, 651, (
                "l1_mersenne_hnf_order_zero_quadratic_collisionfree_exclusion",
            )),
            ("04-order-one-checkpoint-program.md", 652, 914, (
                "l1_mersenne_hnf_order_one_newton_reciprocal_reduction",
            )),
            ("05-balanced-pencil-program.md", 915, 940, (
                "l1_balanced_pencil_anchor_determinant_atlas",
            )),
        ),
        index="""# L1 mixed-petal attack index

The live target has two principal proof routes and one finite checkpoint
subprogram.  Attack a named packet and its existing DAG nodes; do not append
another global narrative to this file.

1. `attack_sections/01-global-exact-shell-program.md`: preferred uniform
   Toeplitz/Pade prefix route.
2. `attack_sections/02-local-first-owner-program.md`: aggregate local
   first-owner alternative.
3. `attack_sections/03-order-zero-checkpoint-program.md` and
   `attack_sections/04-order-one-checkpoint-program.md`: finite official-row
   checkpoint residuals.
4. `attack_sections/05-balanced-pencil-program.md`: balanced-pencil route.

The Round-21 v4 campaign survey and field-normalized census correction are in
`attack_addenda/06-round21-v4-audit.md`.  The completed exact-box diagnosis,
retired fixed-petal run, and growing-petal experiment request are in
`attack_addenda/07-round21-growing-petal-repose.md`.

The preregistered growth falsifier and its bounded evidence are in
`attack_sections/00-falsification-and-growth.md`.  Packet integrity and DAG
ownership are pinned by `attack_sections/document.json`.
""",
        addenda=(
            (
                "critical/nodes/l1_mixed_petal_amplification/attack_addenda/06-round21-v4-audit.md",
                (
                    "l1_mixed_petal_amplification",
                    "pma_sigma_one_variable_defect_exact_hit_floor",
                ),
            ),
            (
                "critical/nodes/l1_mixed_petal_amplification/attack_addenda/07-round21-growing-petal-repose.md",
                ("l1_mixed_petal_amplification",),
            ),
        ),
    ),
    Document(
        source="critical/nodes/rate_half_list_adjacent_crossing/statement.md",
        sha256="ce6bc78cb6f9135a596c9e0caa5fadf923f77447430b834e0b33911e65d23cf1",
        line_count=4059,
        packet_dir="critical/nodes/rate_half_list_adjacent_crossing/statement_sections",
        packets=(
            ("00-live-contract-and-base-reductions.md", 1, 142, (
                "rate_half_list_adjacent_crossing",
                "rate_half_list_low_budget_exact_crossing",
                "rate_half_list_budget_three_intersection_reduction",
            )),
            ("01-c2-one-antipodal-fourier-chain.md", 143, 491, (
                "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_canonical_cell_fourier_ladder",
                "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_degree_defect_global_gate_router",
                "rate_half_list_budget_three_fiber_two_cycle_c2_one_antipodal_reciprocal_affine_collapse",
            )),
            ("02-fiber-two-cycle-c1-c2-chain.md", 492, 1111, (
                "rate_half_list_budget_three_fiber_two_path_exclusion",
                "rate_half_list_budget_three_fiber_two_cycle_quotient_embedding",
                "rate_half_list_budget_three_fiber_two_cycle_matched_trace_jacobi_norm_transfer",
                "rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router",
            )),
            ("03-wave11-pin-v1.md", 1112, 1347, ("rate_half_list_budget_three_intersection_reduction",)),
            ("04-wave12-pin-v1.md", 1348, 1595, ("rate_half_list_budget_three_split_pencil_normal_form",)),
            ("05-wave13-pin.md", 1596, 1684, ("rate_half_list_budget_three_multideletion_multifiber_exclusion",)),
            ("06-wave11-pin-v2.md", 1685, 2402, ("rate_half_list_budget_three_intersection_reduction",)),
            ("07-wave12-pin-v2.md", 2403, 2650, ("rate_half_list_budget_three_split_pencil_normal_form",)),
            ("08-wave14-pin.md", 2651, 2739, ("rate_half_list_budget_three_fiber_four_rank_gate",)),
            ("09-wave11-pin-of-record.md", 2740, 3764, ("rate_half_list_budget_three_intersection_reduction",)),
            ("10-wave12-pin-of-record.md", 3765, 4010, ("rate_half_list_budget_three_split_pencil_normal_form",)),
            ("11-h1-s3-addendum.md", 4011, 4059, ("rate_half_list_adjacent_crossing",)),
        ),
        index="""# Rate-half ordinary-list adjacent crossing

## Live target

For every admissible official rate-half row, with
`B*=floor(|F|/2^128)`, determine adjacent integers `a_L-1,a_L` satisfying

```text
L_1(a_L) <= B* < L_1(a_L-1).
```

Budgets `B*=1,2` are proved exactly at `a_L=3n/4`.  For `B*>=3`, the safe
anchor and unsafe floor do not meet, so this node remains `TARGET`.

## Sub-DAG packets

- `statement_sections/00-live-contract-and-base-reductions.md`: exact scope,
  endpoint convention, and budget-three reduction.
- `statement_sections/01-c2-one-antipodal-fourier-chain.md`: the current
  one-antipodal Fourier/support/collision chain.
- `statement_sections/02-fiber-two-cycle-c1-c2-chain.md`: matched and
  mismatch cycle, parity, torsion, and trace/Jacobi routes.
- `statement_sections/03-wave11-pin-v1.md`,
  `statement_sections/04-wave12-pin-v1.md`, and
  `statement_sections/05-wave13-pin.md`: first chronology-preserving pins.
- `statement_sections/06-wave11-pin-v2.md`,
  `statement_sections/07-wave12-pin-v2.md`, and
  `statement_sections/08-wave14-pin.md`: expanded audited pins.
- `statement_sections/09-wave11-pin-of-record.md` and
  `statement_sections/10-wave12-pin-of-record.md`: forward-facing pin bodies;
  earlier versions remain solely for provenance.
- `statement_sections/11-h1-s3-addendum.md`: later list-compiler addendum.
- `statement_addenda/12-round18-dsa-scope.md`: Round-18 DSA scope update.
- `statement_addenda/13-wave47-theorem-bb.md`: Wave-47 budget break and
  relocated safe-side obligation.
- `statement_addenda/14-round22-u2-accident-cap.md`: Round-22 PROPOSITION U2
  — first accident upper bound of record; crux relocated to the
  constant-weight BCH population cap.
- `statement_addenda/15-round23-cw-pricing.md`: Round-23 constant-weight
  pricing — deep stratum settled at v>=35; Acc_shallow not bridged; one
  object, two targets.

Each mathematical supplier is already an independent DAG node.  This parent
does not absorb those theorems and does not become conditional on them.
`statement_sections/document.json` proves that the extracted packets preserve
the pre-refactor statement byte-for-byte.  Later addenda are indexed and
verified separately, so they do not rewrite that historical archive.
""",
        addenda=(
            (
                "critical/nodes/rate_half_list_adjacent_crossing/statement_addenda/12-round18-dsa-scope.md",
                (
                    "rate_half_list_adjacent_crossing",
                    "crossing_dsa_refutation",
                    "es_ternary_suppression_instruments",
                ),
            ),
            (
                "critical/nodes/rate_half_list_adjacent_crossing/statement_addenda/13-wave47-theorem-bb.md",
                (
                    "rate_half_list_adjacent_crossing",
                    "crossing_dsa_refutation",
                ),
            ),
            (
                "critical/nodes/rate_half_list_adjacent_crossing/statement_addenda/14-round22-u2-accident-cap.md",
                (
                    "rate_half_list_adjacent_crossing",
                    "crossing_dsa_refutation",
                    "es_ternary_suppression_instruments",
                ),
            ),
            (
                "critical/nodes/rate_half_list_adjacent_crossing/statement_addenda/15-round23-cw-pricing.md",
                (
                    "rate_half_list_adjacent_crossing",
                    "crossing_dsa_refutation",
                    "es_ternary_suppression_instruments",
                ),
            ),
        ),
    ),
    Document(
        source="critical/nodes/rate_half_band_closure/attack.md",
        sha256="26f1d1c5015a99cabbbd0abda13f046da317f2aafa04e9856733c818640b58cd",
        line_count=3950,
        packet_dir="critical/nodes/rate_half_band_closure/attack_sections",
        packets=(
            ("00-koalabear-owner-and-q6-ledger.md", 1, 413, (
                "rate_half_kb_q6_u2_complete_source_conic_exclusion",
                "rate_half_kb_m2_r2_dihedral_full_v4_exclusion",
            )),
            ("01-banked-range.md", 414, 439, ("rate_half_band_closure",)),
            ("02-exact-residual-budgets.md", 440, 749, (
                "rate_half_ca_hankel_strict_a3_slope_slack_ledger",
                "rate_half_ca_hankel_half_distance_a3_slope_slack_ledger",
                "rate_half_ca_hankel_half_distance_a1_core_slope_slack_ledger",
            )),
            ("03-exact-arithmetic-route-discipline.md", 750, 977, ("rate_half_band_closure",)),
            ("04-compute-custody.md", 978, 987, ("rate_half_band_closure",)),
            ("05-strict-a3-norm-route-fence.md", 988, 1030, (
                "rate_half_ca_hankel_strict_a3_slope_slack_ledger",
            )),
            ("06-full-v4-source-facet-close.md", 1031, 1079, (
                "rate_half_kb_m2_r2_dihedral_full_v4_exclusion",
            )),
            ("07-coordinate-order-two-signature.md", 1080, 1124, (
                "rate_half_kb_m2_r4_order2_coordinate_source_facet_signature",
            )),
            ("08-diagonal-whole-fiber-program.md", 1125, 1856, (
                "rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler",
                "rate_half_kb_m2_r4_diagonal_c2_112_source_line_complete_exclusion",
            )),
            ("09-coordinate-negative-two-loop-program.md", 1857, 2408, (
                "rate_half_kb_m2_r4_coordinate_k_fiber_vieta_rank_compiler",
                "rate_half_kb_m2_r4_coordinate_negative_two_loop_442_complete_edge_skeleton_classifier",
                "rate_half_kb_m2_r4_coordinate_negative_two_loop_433_complete_edge_skeleton_classifier",
            )),
            ("10-coordinate-negative-one-zero-loop-program.md", 2409, 3249, (
                "rate_half_kb_m2_r4_coordinate_negative_one_loop_442_complete_exclusion",
                "rate_half_kb_m2_r4_coordinate_negative_one_loop_433_complete_exclusion",
                "rate_half_kb_m2_r4_coordinate_negative_zero_loop_433_complete_exclusion",
            )),
            ("11-coordinate-positive-three-loop-program.md", 3250, 3387, (
                "rate_half_kb_m2_r4_coordinate_positive_three_loop_complete_edge_skeleton_classifier",
            )),
            ("12-coordinate-positive-433-program.md", 3388, 3950, (
                "rate_half_kb_m2_r4_coordinate_positive_433_1a_common_vieta_minor_compiler",
                "rate_half_kb_m2_r4_coordinate_positive_433_1b_common_vieta_minor_compiler",
            )),
        ),
        addenda=(
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/13-wave51-positive-433-cell4-campaign.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/14-wave52-positive-433-cell4-pairing3.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/15-wave53-positive-433-cell4-pairing4.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/16-wave54-positive-433-cell4-pairing9.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/17-wave55-positive-433-cell4-pairing5.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/18-wave56-positive-433-cell4-pairing12.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/19-wave57-positive-433-cell4-pairing7.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/20-wave58-positive-433-cell4-pairing10.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/21-wave59-positive-433-cell4-pairing8.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/22-wave60-positive-433-cell4-pairing13.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/23-wave61-positive-433-cell4-pairing11.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/24-wave62-positive-433-cell4-pairing14.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/25-wave63-positive-433-cell4-endpoints.md",
                ("rate_half_band_closure",),
            ),
            (
                "critical/nodes/rate_half_band_closure/attack_addenda/26-wave64-positive-433-universal-xi43-transport.md",
                ("rate_half_band_closure",),
            ),
        ),
        index="""# Rate-half adjacent-certificate attack index

## Live finite contract

The exact adjacent MCA crossing is proved below `2^167`.  At the next two
budgets the missing condition is the far-CA bound at `N-B+1`; larger budgets
remain open even if both displayed residuals close.  The node is therefore
still `TARGET`.

## Sub-DAG packets

- `attack_sections/00-koalabear-owner-and-q6-ledger.md`: deployed KoalaBear
  owner ledger and Q6 structural reductions.
- `attack_sections/01-banked-range.md` and
  `attack_sections/02-exact-residual-budgets.md`: exact finite contract for
  the strict and half-distance budgets.
- `attack_sections/03-exact-arithmetic-route-discipline.md`: proved route
  fences and permitted proof endpoints.
- `attack_sections/04-compute-custody.md`: compute policy local to this node.
- `attack_sections/05-strict-a3-norm-route-fence.md`: strict A=3 endpoint
  fence.
- `attack_sections/06-full-v4-source-facet-close.md` and
  `attack_sections/07-coordinate-order-two-signature.md`: banked source
  facets.
- `attack_sections/08-diagonal-whole-fiber-program.md`: diagonal source-line
  completion.
- `attack_sections/09-coordinate-negative-two-loop-program.md` and
  `attack_sections/10-coordinate-negative-one-zero-loop-program.md`: negative
  signed coordinate Vieta programs.
- `attack_sections/11-coordinate-positive-three-loop-program.md` and
  `attack_sections/12-coordinate-positive-433-program.md`: positive signed
  coordinate Vieta programs.
- `attack_addenda/13-wave51-positive-433-cell4-campaign.md`: wave-51 cell-4
  campaign progress (extracted from the archived packet, CATCH-W51).
- `attack_addenda/14-wave52-positive-433-cell4-pairing3.md`: exact pairing-3
  exclusion and honest pairing-3/6 quotient composition.
- `attack_addenda/15-wave53-positive-433-cell4-pairing4.md`: exact degree-eight
  pairing-4 exclusion and honest pairing-4/9 quotient composition.
- `attack_addenda/16-wave54-positive-433-cell4-pairing9.md`: direct positive-
  `DE` pairing-9 exclusion and complete pairing-4/9 block.
- `attack_addenda/17-wave55-positive-433-cell4-pairing5.md`: exact degree-eight
  pairing-5 exclusion and honest pairing-5/12 quotient composition.
- `attack_addenda/18-wave56-positive-433-cell4-pairing12.md`: direct positive-
  `DE` pairing-12 exclusion and complete pairing-5/12 block.
- `attack_addenda/19-wave57-positive-433-cell4-pairing7.md`: exact degree-eight
  pairing-7 exclusion and honest pairing-7/10 quotient composition.
- `attack_addenda/20-wave58-positive-433-cell4-pairing10.md`: direct positive-
  `DE` pairing-10 exclusion and complete pairing-7/10 block.
- `attack_addenda/21-wave59-positive-433-cell4-pairing8.md`: exact degree-eight
  pairing-8 exclusion and honest pairing-8/13 quotient composition.
- `attack_addenda/22-wave60-positive-433-cell4-pairing13.md`: direct positive-
  `DE` pairing-13 exclusion and complete pairing-8/13 block.
- `attack_addenda/23-wave61-positive-433-cell4-pairing11.md`: exact common-`f`
  pairing-11 exclusion and honest pairing-11/14 quotient composition.
- `attack_addenda/24-wave62-positive-433-cell4-pairing14.md`: direct positive-
  `DE` pairing-14 exclusion and completion of the 45-label parallel-`DE`
  layer.
- `attack_addenda/25-wave63-positive-433-cell4-endpoints.md`: source-only
  endpoint exclusion for missing `bf` and `sigma_c cf`, leaving only the
  `df/ef` roles live.
- `attack_addenda/26-wave64-positive-433-universal-xi43-transport.md`:
  universal outside-role transport reducing the live independent cell-4
  obligation to missing `df`.

New work belongs in the narrowest owning theorem node.  Update this index only
when the live residual partition changes.  The packet manifest verifies
byte-for-byte preservation of the former append-only attack notebook.
""",
    ),
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def section_manifest(document: Document) -> dict[str, object]:
    manifest = {
        "schema": "sectioned-critical-node-document-v1",
        "source_index": document.source,
        "pre_refactor_sha256": document.sha256,
        "pre_refactor_line_count": document.line_count,
        "status_semantics": "presentation-only; node.json remains authoritative",
        "sections": [
            {
                "path": f"{document.packet_dir}/{name}",
                "original_lines": [start, end],
                "dag_nodes": list(nodes),
            }
            for name, start, end, nodes in document.packets
        ],
    }
    if document.addenda:
        manifest["post_refactor_addenda"] = [
            {"path": path, "dag_nodes": list(nodes)}
            for path, nodes in document.addenda
        ]
    return manifest


def write_document(document: Document) -> None:
    source = ROOT / document.source
    data = source.read_bytes()
    if digest(data) != document.sha256:
        raise SystemExit(f"refusing to split changed source: {document.source}")
    lines = data.splitlines(keepends=True)
    if len(lines) != document.line_count:
        raise SystemExit(f"line-count mismatch: {document.source}")

    packet_dir = ROOT / document.packet_dir
    packet_dir.mkdir(parents=True, exist_ok=False)
    for name, start, end, _ in document.packets:
        (packet_dir / name).write_bytes(b"".join(lines[start - 1 : end]))
    (packet_dir / "document.json").write_text(
        json.dumps(section_manifest(document), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    source.write_text(document.index, encoding="utf-8")


def repacket_document(document: Document) -> None:
    packet_dir = ROOT / document.packet_dir
    data = b"".join(
        (packet_dir / name).read_bytes()
        for name, _, _, _ in document.packets
    )
    if digest(data) != document.sha256:
        raise SystemExit(f"refusing to repacket changed archive: {document.source}")
    lines = data.splitlines(keepends=True)
    if len(lines) != document.line_count:
        raise SystemExit(f"archive line-count mismatch: {document.source}")
    for name, start, end, _ in document.packets:
        (packet_dir / name).write_bytes(b"".join(lines[start - 1 : end]))
    (packet_dir / "document.json").write_text(
        json.dumps(section_manifest(document), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def check_document(document: Document) -> list[dict[str, object]]:
    packet_dir = ROOT / document.packet_dir
    manifest_path = packet_dir / "document.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected_manifest = section_manifest(document)
    checks: list[dict[str, object]] = []

    def add(name: str, ok: bool) -> None:
        checks.append({"name": f"{document.source}:{name}", "ok": ok})

    add("manifest_exact", manifest == expected_manifest)
    chunks = []
    all_small = True
    all_nodes_exist = True
    index = (ROOT / document.source).read_text(encoding="utf-8")
    add("index_exact", index == document.index)
    dag = json.loads((ROOT / "dag.json").read_text(encoding="utf-8"))
    dag_nodes = {node["id"] for node in dag["nodes"]}
    for name, _, _, nodes in document.packets:
        path = packet_dir / name
        chunks.append(path.read_bytes())
        all_small &= path.stat().st_size < 50_000
        all_nodes_exist &= set(nodes) <= dag_nodes
        add(f"index_links_{name}", f"{document.packet_dir.split('/')[-1]}/{name}" in index)
    for path_string, nodes in document.addenda:
        path = ROOT / path_string
        all_small &= path.stat().st_size < 50_000
        all_nodes_exist &= set(nodes) <= dag_nodes
        add(f"index_links_{Path(path_string).name}", path_string.split(f"{Path(document.source).parent}/", 1)[-1] in index)
    original = b"".join(chunks)
    add("pre_refactor_sha256", digest(original) == document.sha256)
    add("all_packets_under_50kb", all_small)
    add("all_named_dag_nodes_exist", all_nodes_exist)
    return checks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--repacket", action="store_true")
    args = parser.parse_args()

    if args.write:
        for document in DOCUMENTS:
            write_document(document)
    if args.repacket:
        for document in DOCUMENTS:
            repacket_document(document)

    checks = [check for document in DOCUMENTS for check in check_document(document)]
    result = {
        "status": "PASS" if all(check["ok"] for check in checks) else "FAIL",
        "documents": len(DOCUMENTS),
        "packets": sum(len(document.packets) for document in DOCUMENTS),
        "addenda": sum(len(document.addenda) for document in DOCUMENTS),
        "checks": checks,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
