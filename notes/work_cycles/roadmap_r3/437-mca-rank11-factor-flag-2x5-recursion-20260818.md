# Cycle 437: rank-eleven factor-flag `2 x 5` recursion

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 803a13266
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
relevant open PRs: #1173 (2788d5ec3), #1172, #1171, #1170
critical mandatory-open count: 28 TARGET nodes
```

Canonical and upstream heads are unchanged, and the open-PR search contains
no successor to `#1173`. No source tree was modified.

## Action

Attack the exact factor-flag model suggested by the full-span survivor:
`C'=span(PB)` with dimensions `2 x 5`, each promoted rich container lying in
one slice `g_iB`. Split containers by heavy pencil-factor roots and count the
remaining residual subspaces by labelled ordered bases.

## Result: NARROWED

`rate_half_mca_rank11_factor_flag_2x5_recursive_router` is PROVED. In the
base-free pencil branch, factor cutoff `T=408` leaves at least `37978`
residual common roots. If every residual is `18165`-transverse, the complete
nontransverse charge is

```text
fixed-factor classes       2763267104042675
dimension-two residuals   11330947785633956
dimension-three residuals 51071925374444624
union                     65166140264121255
```

Adding the transverse envelope gives `274978898701800872`, with slack
`1829409594215`. The adjacent threshold is over by `15983178478905`; an
all-cutoff scan proves `18165` is globally maximal. Therefore every unsafe
exact `2 x 5` factor flag emits either an anchor-good common pencil base
coordinate or a deeper residual rich flat on at least `18166` coordinates.

## Burn-down

```text
node/workboard item: KoalaBear rank-eleven exact factor-flag recursion
result: NARROWED
DAG delta: +1 PROVED background node; critical open count remains 28
upstream delta: successor-packet candidate recorded; no competing PR opened
delta-star movement: none
new assumptions: exact 2 x 5 factor presentation and slice cover are scoped premises
live compute requests: none
Modal spend: zero
next action: derive the factor presentation from the full-span atlas, or pay
             the common-base/deeper-residual horns
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_2x5_recursive_router/verify.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_2x5_recursive_router/verify_audit.py
tools/ramguard tiny -- python3 background/nodes/rate_half_mca_rank11_factor_flag_2x5_recursive_router/verify.py --tamper-selftest
tools/ramguard local -- python3 tools/verify_prize_dag.py
```

## Upstream posture

The theorem uses `#1173`'s factor-flag language and supplies an exact
recursive output for one proposed `2 x 5` model. It must be exported as a
conditional scoped theorem, not as existence of the model or as the general
base-field-normalized split-pencil census. Since `#1173` remains open, hold
the formal successor packet and avoid racing its branch.
