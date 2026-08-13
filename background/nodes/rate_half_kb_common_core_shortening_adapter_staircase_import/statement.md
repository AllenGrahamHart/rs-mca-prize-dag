# Common-core shortening adapter and the exact KoalaBear staircase walls

- **status:** PROVED for the cancellation adapter and unaffected arithmetic
  walls; the former direction-separated payment is RETRACTED.
- **source:** upstream PR `#1163`
  `[MCA] Cut common-core shortening staircase` (scottdhughes), head
  `e26c15b2d`, stacked on `#1160` at `c5f4ea7a`; threshold note
  `experimental/notes/thresholds/kb_mca_v4_common_core_shortening_staircase_route_cut_v1.md`.
- **wired:** 2026-08-12 coordinator PR-sweep session, line-audited with an
  independent from-scratch replay (`verify_audit.py`).
- **consumer:** `rate_half_band_crossing_location` (evidence); the
  KoalaBear v4 S/A/E import cluster.

## Units and row

All counts are in distinct finite affine bad slopes on one actual
received line at the official KoalaBear MCA row

```text
(n,k,m,d,R,t) = (2097152, 1048576, 1116048, 67472, 1048576, 981104),
B_* = 274980728111395087,      d = m-k,  R = n-k,  t = n-m.
```

The "common core" here is notion (2) of the source's three: the
intersection of the maximal agreement supports of one selected
explanation family — not an exact-sparsification common support, not a
locator-pencil GCD.

## Theorem (same-record common-core cancellation; PROVED)

Fix distinct slopes `gamma_i` with degree-`<k` explanations `h_i`,
maximal agreement supports `S_hat_i`, each carrying an actual size-`m`
noncontained witness inside `S_hat_i`. Let `C = intersection S_hat_i`,
`c = |C|`, `G_C = prod_{x in C}(X-x)`. If the family is not globally
affine then `c < k` (source's maximal-support slope-degree theorem), and
subtracting the unique degree-`<c` interpolants `a_0,a_1` of `r_0,r_1`
on `C` followed by exact division by `G_C` is a **typed reversible
adapter** to a shortened record on `D minus C`:

```text
(n,k,m) -> (n-c, k-c, m-c) = (R+s, s, d+s),   s = k-c,
```

preserving the finite affine slopes, the field of definition, the
invariants `m-k`, `n-k`, `n-m`, maximal supports (`S_hat_i minus C`),
and same-support noncontainment in BOTH directions via
`(p_0,p_1) = (a_0 + G_C p'_0, a_1 + G_C p'_1)`. A noncontained witness
through `C` exists by the exchange-graph argument (adjacent size-`m`
subsets overlap in `m-1 >= k` points, so pair-containment would
propagate to all of `S_hat_i`). Two-cover complexity satisfies
`3m-k+3 = (3m'-k'+3) + 2c`. The adapter does **not** identify the
shortened line/carrier/support with the original objects; reverse
scalar-locator transport additionally needs `Q(x) != 0` on every deleted
point.

**Converse hardness:** the inverse lift embeds every compatible
shortened RS-MCA record into a common-core record with the same slopes
and badness — "divide the core and declare it paid" is false.

## The exact walls (PROVED, replayed here)

1. **Degree-18 interface wall.** `32m - 17n = 61952`, so the deployed
   order-32 degree-18 interface survives exactly through `c = 4130`
   (`61952 > 15c`) and the floor drops to 17 at `c = 4131`; at
   `c = k-1` the floor is 3. The `thm:partial-relative` constants
   cannot be reused uniformly after cancellation.
2. **Fixed-core compiler cells.** `B_cell(s) = min{C(R+s, d+s),
   C(R+s, s+1)}` fits under `B_*` through `s = 2`
   (`B_cell(2) = 192154133857304576`) and first fails at `s = 3`
   (`B_cell(3) = 50372197381489643749376 > B_*`).
3. **Retracted candidate boundary.** The legacy formula `J_s` crosses
   `B_*` between the displayed `J_13` and `J_14`, but PR #1165's exact
   counterexample and PR #1166's support-local repair prove that direction
   separation does not justify this formula. These integers are retained
   only as a negative-regression arithmetic record.
4. **Jo transfer wall.** At the first degree-drop core `c = 4131`,
   `C(n,4131) > B_* C(m,4131)`; the ceiling of the double-counting
   multiplier `C(n,c)/C(m,c)` has 3765 bits (1134 decimal digits), and
   staged shortening telescopes to the same factor. The published
   slope-preserving shortening transfer cannot pay the first uncovered
   core in frozen KoalaBear units.

This imported packet itself pays a fixed family only when it is globally
affine or `s<=2`. The replacement support-local theorem is banked
separately in `rate_half_mca_support_local_transversality_compiler`; it pays
automatic full-rank shortened cells through `s=9` and emits exact exception
terminals above that. No direction-separated `3<=s<=13` payment survives.

## Route cut (RECORD)

The local cancellation cannot be summed over varying local 32-tuple
cores. The active v4 source lacks a chronology-correct whole-line
selector sending each actual slope exactly once to an earlier owner, a
paid fixed-core family, or one of the two residual labels; until that
selector (or an alternative maximum-type whole-line theorem) exists,

```text
U_S = U_A = U_E = global ledger movement = 0.
```

The `#1160` 67,472-slope construction is globally affine and separately
near-rational-owned — it is a control, not a casualty, of this adapter
(see `v13_2_near_rational_supportwise_two_anchor_payment`).

## Scope

- Zero ledger movement; no S/A/E, KoalaBear, LIST, or universal
  four-rate closure is claimed.
- The `c < k` clause in the non-affine case is cited from the upstream
  source theorem, not re-proved here; every other clause is re-proved
  and machine-replayed in this package.
- Upstream marks the packet "independent review required"; this node's
  banking rests on the coordinator line audit plus the independent
  replay in `verify_audit.py`, the same standard used for the `#1160`
  import.

## Replay

```text
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_kb_common_core_shortening_adapter_staircase_import/verify.py
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_kb_common_core_shortening_adapter_staircase_import/verify_audit.py
```
