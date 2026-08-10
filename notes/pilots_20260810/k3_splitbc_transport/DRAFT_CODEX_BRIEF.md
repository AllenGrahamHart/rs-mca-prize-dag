# DRAFT brief — 433-1b -> O0b split-BC product-rank-five block

Status: DRAFT, coordinator-gated. Produced by round-30 pilot
`k3_splitbc_transport` as deliverable D3. Not yet shipped to
`notes/codex_briefs/`. Evidence and misses are in `REPORT.md` beside this
file; every count below is derived there with file:line sources.

## 0. One-sentence summary

The whole *common/source* layer of the 37,800-label split block is already
paid by the closed `433-1b -> O0a` route and needs zero recomputation; the
*outside* layer must be rebuilt, but four exact transports cut it from
37,800 raw labels to **11,304 representative systems** before any algebra is
run, and a fifth (not yet certified) would cut it to about **3,414**.

## 1. What transports for free (do not recompute)

| layer | O0a -> O0b split verdict | licence |
|---|---|---|
| common products/sums `(-1,b,c,bc,-bc)`, `(0,1+b,1+c,b+c,b-c)` | **identical** | `background/nodes/rate_half_kb_m2_r4_coordinate_positive_433_1b_o0b_common_vieta_minor_atlas/statement.md:10-11`, `proof.md:9-10` |
| 60 compiled split algebra rows (15 cells x 4 root-sign rows) | **shared by all six split lanes** | same node, `proof.md:8-12`, `statement.md:19-24` |
| product-rank-drop branch (rank(P)<=4) | **already closed for O0b** | `..._433_1b_o0b_split_rankdrop_complete_exclusion/proof.md:3-4` |
| 16 deployed rank-drop points, cells 9/10 | **transported** | `..._433_1b_product_rankdrop_deployed_rational_classifier/statement.md:29-38` |
| per-cell common loci (curves/towers) | **transported** | `..._433_1b_cell3_compact_curve_kernel`, `..._cell4_four_basis_tower_kernel`, `..._cell5_elliptic_common_kernel`, `..._cell9_global_five_relation_common_locus`, `..._cell11_quadratic_four_basis_common_locus`, `..._cell12_elliptic_four_basis_common_locus`, `..._cell14_quadratic_curve_structure` |
| role-cell orbit structure `[0][1,2][3,6][4,7][5,8][9,10][11][12,13][14]` | **transported** | the six `..._433_1b_cells*_duplicate_role_*` nodes plus the standalone `cell0/cell11/cell14` closures |

## 2. What does NOT transport (do not try)

1. **The O0a universal 105->36 label quotient**
   (`..._433_1b_universal_generic_outside_label_orbit_quotient`). Both
   generators die on O0b. `P` needs two identical `DE` records, which exist
   in O0b only in `SDE`/`SDF`, not in `S0`/`SBC`. `Q` (the `D/E` transport)
   needs *both* colored incidences at `F`; O0b's colored edges are `BE` and
   `CF`, so `d <-> e` sends `be -> bd`, which is not a record. See REPORT
   miss M1: that node's statement carries no route qualifier and must not be
   applied to O0b.
2. **Any 433-1a signed-pair guard factorization.** Upstream PR #1155 fence
   (recorded at `notes/work_cycles/roadmap_r3/17-positive-433-repeat-bc-20260810.md:306-311`)
   is taken as a hard datum. Nothing in this brief uses a guard-only
   closure; the residual quadratic cover is *counted*, exactly as the fence
   demands.
3. **The cells-3/6 repeated-BC outside exclusions.** They consume the
   repeated-BC common curves, which the split lanes do not have.

## 3. The four exact transports to certify first (cheap, no algebra)

**T1 — S0 inherits the `d -> -d` quotient (105 -> 57).**
`S0` and `SBC` have *identical* outside record lists
`(BE,CF,DE+,DE-,DF+,DF-,EF)`
(`..._o0b_split_rankdrop_outside_modal.py:164-168` vs
`..._o0b_common_repeat_cell3_outside_label_quotient/node.json:8`). The banked
quotient's proof uses only the outside records
(`.../proof.md:1-13`) and requires only the O0b atlas
(`.../node.json:24-26`). Falsifiable prediction to check: the canonical
orbit ledger digest for `S0` must be **bit-identical** to the banked
`70c074ad010a7c8a03c84d6eaeb6206f14b941de455301180c9aa51a03f02b91`
(`.../statement.md:29-30`), because the label ledger depends only on the
index permutation `(2 3)(4 5)`.
*Deliverable:* one node, statement widened to "every O0b lane whose outside
record list is `(BE,CF,DE+,DE-,DF+,DF-,EF)`, i.e. all four `SBC` and both
`S0` lanes".

**T2 — SDE/SDF identical-record exchange (105 -> 60).**
`SDE` has records 2 and 3 both equal to `(d*e, +)` with equal squared sums
`(d+e)^2`; `SDF` has records 4 and 5 both `(d*f, +)`
(`..._split_rankdrop_outside_modal.py:169-178`, `181-188`). The exchange of
two records with identical product and squared sum is a system bijection —
the exact argument already used at
`..._433_1b_universal_generic_outside_label_orbit_quotient/proof.md:9-10`.
Orbit census: **60 orbits, profile 1:15, 2:45** (verified by
`label_orbits.py` in the pilot dir, whose model reproduces both banked
censuses 57 and 36 exactly).

**T3 — SDE -> SDF lane transport (kills 2 of 6 lanes outright).**
Apply `B<->C` and `E<->F`. On the common side it exchanges roles `AB<->AC`
and fixes `BC+` and `BC-` individually (`bc -> cb = bc`). On the outside it
sends `BE<->CF`, `DE+<->DF+`, `DE-<->DF-`, fixes `EF` and preserves the
outside-cycle sign. Applied to `SDE`'s record tuple it returns exactly
`SDF`'s tuple. This is the *same map* already proved for the repeated lanes
at `..._o0b_common_repeat_cells3_6_full_system_transport/statement.md:6-17`,
`proof.md:3-14`; only the common-side check changes (split `bc,-bc` instead
of repeated `sigma*bc,sigma*bc`), and that check is one line.
*Consequence:* all 12,600 `SDF` labels are free.

**T4 — S0 role-cell transport (15 cells -> 9 orbits per S0 lane).**
The same `B<->C, E<->F` map is a *self*-map of each `S0` lane (record
permutation `(0 1)(2 4)(3 5)`, outside-cycle sign preserved) and sends role
cell `i` to `rho(i)` with
`rho = (1 2)(3 6)(4 7)(5 8)(9 10)(12 13)`, fixing `{0,11,14}`.
Note `BC1<->BC2` is *not* available on split lanes (it would need a gauge
flipping the sign of `bc`, which breaks the `ab`/`ac` normalization), which
is exactly why cells 11 and 14 stay separate here while they pair on the
repeated side.
*Required care:* print the induced source-root-sign map per cell. The O0a
precedent flips `epsilon_2` in cells 9/10
(`..._433_1b_cells9_10_duplicate_role_transport/proof.md:3`) while the O0b
repeated cells 3/6 fix both signs
(`..._o0b_common_repeat_cells3_6_full_system_transport/statement.md:7`).

## 4. Exact residual after T1-T4

Raw block: `6 lanes * 15 cells * 4 root-sign rows * 105 labels = 37,800`.

```text
piece                       raw labels   representative systems   quotient used
SDF lanes (2)                   12,600            0               T3 (whole lanes)
SDE lanes (2)                   12,600        7,200               T2  (120 rows x 60)
S0 lanes, rho-paired cells      10,080        2,736               T4 + T1 (2 x 6 x 4 x 57)
S0 lanes, rho-fixed {0,11,14}    2,520        1,368               T1 only (2 x 3 x 4 x 57)
total                           37,800       11,304               factor 3.34
```

Optional extra on the `rho`-fixed cells: `T1` and `T4` commute there and
generate a Klein four-group on labels with **32 orbits (1:3, 2:7, 4:22)**;
using it needs the sign-row action of T4 resolved and would take the last
line from 1,368 to at best 768, i.e. total **10,704**.

## 5. The one certificate worth building before the census (factor ~3.3 more)

There is **no 433-1b source root-sign symmetry quotient in the repo**
(`ls background/nodes | grep -i root_sign` returns only three 433-1a ids).
The 433-1a node
`..._433_1a_common_root_sign_symmetry_quotient/statement.md:44-51` collapses
60 raw common matching/root-sign rows to **10** representatives. Its
cells-3..14 argument is purely source-side — the loop is the canonical
root-`1` anchor with `q=0`, so its deck mate represents the same loop record
(`.../statement.md:23-25`) — and in 433-1b cells 3..14 the loop role `LA`
likewise sits inside a pair rather than being the singleton
(`..._433_1b_cells1_2_complete_exclusion/statement.md:13-14`,
`..._433_1b_cell0_complete_exclusion/statement.md:10-14`).
*Caveat to check before assuming it ports:* the 433-1a cell-0/1/2 arguments
use "two identical `AB+` roles" (`.../statement.md:27-35`), and 433-1b split
lanes have five *distinct* common products `(-1,b,c,bc,-bc)`, so only the
source-reciprocity half of that argument is available in cells 0,1,2.

Conditional arithmetic (4 rows -> 1 in cells 3..14; 4 -> 2 in cells 0,1,2):

```text
SDE lanes:  2 lanes x 18 rows x 60 =  2,160
S0 paired:  2 lanes x  7 rows x 57 =    798
S0 fixed:   2 lanes x  4 rows x 57 =    456
total                                 3,414      factor 11.1 vs raw
```

## 6. Attack shape for the residue (census only where transport ran out)

Do **not** build a monolithic all-variable outside ideal. The cell-11
precedent hit the 300s cap on exactly that object
(`notes/work_cycles/roadmap_r3/17-positive-433-repeat-bc-20260810.md:205-206, 216`).
Note also that the 10,080-system split rank-drop run that completed cleanly
was over *zero-dimensional deployed points*
(`..._o0b_split_rankdrop_complete_exclusion/statement.md:16-25`); the
rank-five block sits over positive-dimensional common curves, so 11,304 is a
*count* match, not a difficulty match.

Recommended per-piece shape, reusing the O0a cell certificates as the source
algebra:

1. For each representative role cell, take the banked O0a common locus
   (curve/tower) as the base; no new common elimination.
2. Build a function-field generic-rank atlas over that base for the five
   necessary equations (missing product, three paired products, missing-mate
   squared sum), following
   `..._o0b_common_repeat_cell11_uncolored_generic_rank_atlas` — full-rank at
   one exact specialization is enough to prove the determinant is not
   identically zero.
3. Reconstruct the determinant-zero fibers and replay them exactly. This is
   the step cycle-17 leaves open for cell 11 (`:319-320`); the split block
   will need the same tool, so build it once and use it twice.
4. Treat missing `BE`/`CF` separately, as in the repeated block: eliminate
   the unknown endpoint without dividing by the missing value
   (`..._o0b_common_repeat_cell3_bcminus_colored_norm_atlas`).

## 7. Certificates this brief would produce

```text
id (proposed)                                              content
..._433_1b_o0b_split_s0_outside_label_quotient             T1, 105->57 on both S0 lanes, ledger digest must equal 70c074ad...
..._433_1b_o0b_split_sde_sdf_identical_record_quotient     T2, 105->60, profile 1:15,2:45
..._433_1b_o0b_split_sde_sdf_lane_transport                T3, SDE(sigma_o) -> SDF(sigma_o), cell i -> rho(i)
..._433_1b_o0b_split_s0_role_transport                     T4, rho = (1 2)(3 6)(4 7)(5 8)(9 10)(12 13), fixed {0,11,14}
..._433_1b_common_root_sign_symmetry_quotient              optional, ports the 433-1a 60->10 quotient to 433-1b
```

Only after all five are banked should an elimination campaign be selected,
and it should be sized against 11,304 (or 3,414) representative systems, not
37,800 labels.
