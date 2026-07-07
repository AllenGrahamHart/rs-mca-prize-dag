# Falsification-Pruning Frontier Summary

Date: 2026-07-05

Scope: six priority critical red/frontier chains from the standing
falsification goal, with the user's premise-first rule applied to immediate
downstream amber consumers.  Amber implications are treated as already proved
unless a defect is found; the live question is whether the premise `A` consumed
by the implication is true, nonvacuous, and paid.

This file is an index over the replay ledger, not a replacement for it.  Full
commands, parameters, and JSON outputs are in `ledger.md` and `results/`.

## Summary Table

| Chain | Downstream premise attacked | Main attempts | Current falsification verdict | Stable frontier / next target |
| --- | --- | --- | --- | --- |
| `sov_gridsum_residual` | Bohr / large-power-sum exceptional mass is narrow enough to be paid before residual Lane-1 closure | 1, 11, 19, 23 | Threshold-only gates are false as paid-class premises: beta 0.90 admits near-uniform huge-mass families, while even near-pure 6-substitution intervals already have positive naive paid mass at ratio 0.994 | Stable frontier is a structural/parameterized paid Bohr certificate plus an internal Lane-1 fallback for diluted threshold-passers |
| `m720_conductor_compression` | Actual complete official h=7..20 primitive norm-gate manifest exists | 2, 10, 12, 20 | No unpaid non-toral slice witness found, but the manifest premise is unsatisfied in this worktree: 8 complete/algebraic rows, 19 slice-only rows, 109 unprobed rows in the configured grid | Stable frontier is the official norm-gate manifest or a uniform nonvanishing theorem; slice evidence is not a certificate |
| `e22_mixed_petal_covariance` | Common-tail / kernel-saturation or tail-removed quotient-factor certificate is meaningful enough for pricing | 3, 7, 8, 13, 18 | Literal common-tail certificates are often vacuous, but all-tail coverage resisted a 72-cell layout/scalar sweep with 0 omissions; multiplicity collisions remain load-bearing | Stable frontier is an explicit all-tail pricing/multiplicity theorem or a strengthened proper-scale retained-fiber premise with separate all-tail handling |
| `petal_primitive_residue_kernel_rank` | Squarefree classification ledger pays multi-character families or excludes them from the actual squarefree-realizable locator locus | 4, 9, 14, 17, 21, 22 | Old PRK absolute residual bound is false with current paid menu; actual-locus sweeps found only a charged-like binomial/coset CRT hit and 0 unclassified hits, including 77 split rows in a deeper `(127,3,6)` stress | Stable frontier is `petal_squarefree_classification_ledger_payload`, especially multi-character chargeability / actual-locus realizability |
| `dli_prime_weighted_large_block_support` | U-weighted small/exceptional support is suppressed enough for conductor-mass implication | 5, 15 | No weighted low-support falsifier at prize-shaped `alpha=256`; low-support mass is dangerous below about `alpha=160`, so the seen-coordinate margin is load-bearing | Stable frontier is the actual map-determined large-block support theorem; entropy-side sparse-support attack resisted |
| `rate_half_band_closure` | A concrete mechanism closes the rate-1/2 band before adjacency consumers use it | 6, 16 | Known concrete premises are refuted/unsatisfied: AQB convex-combination route dead; dihedral sibling certificate refuted; floor depth misses by 2,978,146 radii | Stable frontier is new mechanism or bracket-grade treatment; current downstream premise is not satisfied |

## Premise-Level Outcomes

### SOV

The original Bohr pricing attack found interval/Bohr cells are rare enough under
one naive locator-density calculation, but Attempt 11 showed that loose
low-frequency thresholds admit diluted cells whose sampled h-sum behavior is
close to uniform while the naive locator family count explodes.  This does not
kill SOV: it sharpens the premise.  The Bohr exception must be a tight paid
structural class, not a broad Fourier-threshold gate.

Attempt 19 refined the transition.  At `beta=0.90`, diluted interval cells have
median max small-frequency ratio `0.902398`, so they pass a `0.90` gate, but
their sampled h-sum collision ratio is only `1.1003` times uniform while the
naive locator-density log2 is `1439.57`.  Thus the loose-threshold paid-class
premise is false; a valid SOV premise needs a near-pure structural gate, a
parameterized diluted-Bohr price, or an internal Lane-1 fallback.

Attempt 23 attacked the near-pure edge.  Pure intervals through 4 random
substitutions still have negative naive locator-density log2 (`-31.563` at
4 substitutions), but 6 substitutions already flip positive (`+10.565`) while
the median max small-frequency ratio remains `0.994069`.  Therefore even a
`0.99` threshold is too broad as a paid class; the Bohr premise needs either a
very tight structural gate, a parameterized price by off-interval substitutions,
or a proved fallback route.

Replay:
- `sov_bohr_pricing_census.py`
- `sov_modal_bohr_dilution_probe.py`

### M720

The premise consumed downstream is not "many slices have no witnesses"; it is a
complete official manifest.  The audit found that the current clone does not
satisfy that premise.  Additional n=1024 slices found no unpaid non-toral
witness, but all new rows were incomplete (`W<n`) evidence.

Attempt 20 added the next suggested official slices at the manifest audit's
`6,000,000` count ceiling.  `(64,8,2)` completed the `W=29` slice with
`1,184,040` hash and `3,108,105` probe subsets and found no nontoral witness;
`(64,8,3)` aborted during hash construction.  The combined audit now has
`19` slice-only no-witness rows and `109` unprobed official rows.  The premise
is still unsatisfied.

Replay:
- `m720_manifest_gap_audit.py`
- `m720_modal_slice_probe.py`

### E22

The common-tail premise is formally satisfiable too often by the all-tail
choice `M=n`, `B=touched_support`.  The downstream chain therefore needs a
pricing-useful version of the premise.  Attempt 13 found that most tested
structured challengers have no retained quotient fiber at any proper dyadic
scale, so "kernel-invariant after deleting everything" cannot be silently used
as a charged quotient-factor certificate.

Attempt 18 attacked the all-tail pricing premise across four layouts and two
scalar modes.  Across `72` local cells and `8386` structured challengers, every
all-tail case had a selected dyadic representative.  The falsification signal
shifted to multiplicity: `34` selected-representative/support collisions with
polynomial excess `37`, concentrated in small high-`k` rows.  Thus coverage
resists, while the exact multiplicity convention remains load-bearing.

Replay:
- `e22_common_tail_certificate_probe.py`
- `e22_tail_only_pricing_coverage.py`
- `e22_premise_vacuity_audit.py`
- `e22_all_tail_mode_sweep.py`

### Petal / PRK

The premise below `petal_cofactor_chargeability` is the most fragile.  The
current paid menu cannot leave multi-character kernel families uncharged:
two-character residual dimension grows with `c/M`, and all-character residual
dimension grows essentially like `c`.  The repair can still be true only if the
ledger explicitly pays a parameterized multi-character class or proves that the
actual squarefree-realizable locus excludes the modeled bulk.

Attempt 17 tested that exclusion premise directly in a small executable
split-locator chart.  The narrow family `X^d + aX^(d-M) + b` produced `9`
split-squarefree rows, and `50000` random two-character rows produced another
`16` split rows, but none satisfied the CRT degree condition in the tested
petal/scalar charts.  This is evidence for actual-locus exclusion, not a proof
and not a repair of the abstract budget problem.

Attempt 21 expanded the actual-locus search across `(p,M,t)` rows
`(127,3,5)`, `(127,3,6)`, `(127,3,7)`, `(97,4,5)`, `(193,4,5)`,
and `(101,5,5)`, with `64` sampled petal charts and five scalar modes.  It
found exactly one CRT-realizable hit, `X^14+105` at `(127,3,6)`, but this has
support `[0,14]` and is classified as a binomial/coset paid shape.  No
unclassified multi-character actual-locus witness was found.

Attempt 22 spent a deeper Modal budget on `(127,3,6)`: `245441` random
two-character rows produced `77` split rows, and the narrow family produced
`9` split rows, but there were `0` CRT hits under the sampled charts/scalars.
Thus the actual-locus exclusion premise continues to resist for unclassified
multi-character bulk; the proof still must explicitly pay the binomial/coset
case and then exclude or pay the rest.

Replay:
- `prk_multichar_chargeability_budget.py`
- `petal_squarefree_ledger_scope_probe.py`
- `petal_multichar_realizability_probe.py`
- `petal_multichar_modal_sweep.py`

### DLI

The old sup premise is false, so the only relevant premise is the corrected
U-weighted one.  The exact DP rows and threshold scan support the weighted
premise at the prize-shaped seen-coordinate expansion.  The falsification route
via sparse support entropy is suppressed by roughly `q^{-0.88 L}` or better at
`alpha=256` for the tested cutoffs.

Replay:
- `dli_weighted_average_probe.py`
- `dli_large_block_threshold_scan.py`

### Rate Half

The guardrail arithmetic is stable, but the concrete premises that would close
the band are not.  AQB constants quantify a missing gain but the AQB family
average is blocked by convexity.  The dihedral sibling route is refuted by the
degree audit and Dickson fiber collapse.  The node should be treated as
new-mechanism or bracket-grade until a new concrete premise is supplied.

Replay:
- `rate_half_guardrail_replay.py`
- `nodes/aqb_coupled_family_entropy_manifest_payload/refutation.md`
- `nodes/dihedral_sibling_window_certificate/proof.md`

## Next Best Attacks

1. Petal / PRK: test whether modeled multi-character families actually occur in
   the executable squarefree-realizable locus at larger or more structured
   rows.  This remains the sharpest premise-risk because it can invalidate the
   downstream chargeability premise rather than merely leave it open.
2. SOV: quantify the tight Bohr gate or Lane-1 fallback boundary.  Attempt 19
   shows a `0.90` threshold is false as a paid-class premise.
3. E22: audit the exact multiplicity convention used by the all-tail staircase
   pricing column.  Coverage resisted; collisions are now the live issue.
4. M720: continue bounded Modal slices only as evidence; the decisive task is
   a manifest/theorem audit, not more incomplete slices.
5. DLI: move from entropy side to actual map-partition exceptional-block
   definitions; sparse-support entropy has not falsified the premise.
6. Rate half: do not retry AQB or dihedral sibling without a genuinely new
   premise; both concrete routes are already refuted.

## Validation State

As of this summary, no DAG/status edits have been made in this clone.  The DAG
verifier passes structure, refs, acyclicity, reachability, and status
propagation with the pre-existing root satisfiability warning.  All
falsification result JSON files parse.
