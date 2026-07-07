# OVERNIGHT LOG 2026-07-08

## 2026-07-08 initial entry

Stage: Terminal A, h=3 char-zero classification.

Banked pose: `critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_CHAR0_CLASSIFICATION.md`.

Current route: direct unit-circle proof using `e2 = product * conjugate(e1)`,
which should classify all distinct char-zero h=3 trades as toral `mu_3`
coset pairs. Exact checker written but not yet replayed.

Next step: run `f3_h3_char0_classification.py`, fix any exact-check failures,
then commit the banked theorem/checker.

## 2026-07-08 Terminal A core replay

Stage: A1--A4.

Banked claim: direct unit-circle proof classifies all char-zero h=3 trades as
toral `mu_3` coset pairs. Exact checker replays in about two seconds and verifies
rows through `n=96`; the `n=96` row gives exactly `496 = binom(32,2)` char-zero
trades, all toral. The three banked finite-field norm-gate shapes at primes
`9601`, `13249`, and `18433` have both obstructions nonzero in `Q(zeta_96)` and
both obstructions zero modulo their activating prime.

Catch: the first checker implementation did repeated Sympy reductions inside
the pair loop and had to be interrupted after 60 seconds. The replay was repaired
by caching `X^e mod Phi_n` residues and grouping triples by exact `(e1,e2)`
signature before pairing.

Next step: add the requested node-candidate statement/proof files and commit the
stage.

## 2026-07-08 Terminal B partial replay

Stage: Terminal B, in-house explicit h=2.

Banked files:

```text
critical/nodes/u1_x4_direct_column_budget/notes/F3_H2_STEPANOV_RECONSTRUCTION.md
critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_energy_replay.py
```

Replay:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_energy_replay.py
```

Digest: `H2_ENERGY_REPLAY_PASS`.

Banked claim: exact h=2 F3 trade count is controlled by additive energy via
`T_2 <= E(H)/8`.  The exact energy decomposition is
`E(H)=8T_2+4M_2+2n^2-n`, where `M_2` is the diagonal/nondiagonal midpoint
count.  Rows `n=16,32,64,128,256,512` at the first primes `q=1 mod n` above
`n^2` and `n^3` replay exactly; max measured `E(H)/n^2.5 = 0.8906`.

Catch: the first written identity omitted midpoint collisions and claimed
`E(H)=8T_2+2n^2-n`.  The direct ordered-energy check falsified it immediately
at `(n,q)=(16,257)`.  The script and note now include the `4M_2` term.

Stepanov status: coefficient/degree arithmetic for a single-shift auxiliary
polynomial is checked through `n=512` with positive slack.  The missing in-house
steps are still the nonvanishing/rank lemma and the energy-level upgrade from
single-shift intersection bounds to `E(H) <= C n^2.5`.

External explicit-constant source located: Cochrane--Hart--Pinner--Spencer
record the Cochrane--Pinner explicit constant
`E(A) <= (16/3)|A|^2.5` for `|A| < p^(2/3)`; if accepted as an external import,
this gives `T_2 <= (2/3)n^2.5 < n^3` for every `n >= 1`.  This sharpens the
existing import but does not satisfy Terminal B's in-house proof requirement.

Next step: either reconstruct the HBK/Konyagin dyadic level-set upgrade with
explicit constants, or bank that exact step as the Terminal B blocker and move
to Terminal C per the brief's >90-minute rule.
