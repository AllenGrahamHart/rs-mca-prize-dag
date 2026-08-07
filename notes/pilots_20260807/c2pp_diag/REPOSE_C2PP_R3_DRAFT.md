# C2'' RE-POSE OF RECORD — DRAFT (round 23, 2026-08-07, c2pp_diag pilot)

DRAFT ONLY. Proposed replacement text for `dli_c2pp_joint_reserve`.
Not applied. No status flip is proposed or implied. The coordinator
replays and decides.

Pre-registration: `PREREG.md`, "# PILOT REGISTRATIONS".
Reproduction: `fd_coset_routing_attack.py`, `fdb_accident_multiplicity.py`,
`fdc_coset_mechanism.py` (+ the `*_results.json` artifacts).

---

## Why a re-pose is owed

The node's statement of record asserts a bound on the UNREDUCED joint
loss:

> `X(R) = q^(-t+H) W_cen(R)` ... `X(R) <= 2^21 A(R)`
> — `critical/nodes/dli_c2pp_joint_reserve/statement.md:9-19`

The clause the pose defends, and the clause both survived F-rounds
tested, is the REDUCED one:

> `E_U[ prod_j rho_j ]_reduced  <=  2^R_joint * prod_j E_U[ rho_j ]`
> — `critical/nodes/.../notes/C2PP_POSED_20260710.md:35-36`

The qualifier `_reduced` occurs in exactly ONE place in the whole
critical/background/dag corpus — `m4_assembly_verifier.py:112` — and is
absent from `statement.md`, `node.json`, `dag.json`, `conditional.md`,
and from the assembly step that consumes it
(`m4_assembly_verifier.py:827-828`). The consumer face needs the
unreduced quantity (`x4_exactlist_staircase_split/REDUCTION_PACKET.md:51`,
`:62`: "half-band count <= 2^121").

Measured gap between the two (banked 8-row calibration grid, exact):
the reduction removes a junction factor of up to 21.80x
(`coset_weight_shift`), and the reduced object is IDENTICALLY ZERO at
3 of the 4 rows where the unreduced object overflows.

---

## PROPOSED STATEMENT — C2''-r3 (aggregate, non-uniform, transport-explicit)

For every official prize row `R`, under the generated-field
normalization (pin P-FIELD, catch #13), over the ACTUAL 33 junctions
of the official 34-level schedule, with `rho_j` the level-j normalized
valid-skew count and `E_U` the unconditional U-weighted expectation:

```text
    sum_{j=1}^{33}  log2 ( E_U[ rho_j | state_{<j} null ] / E_U[ rho_j ] )   <=   21.
                                                                   (C2''-r3)
```

Equivalently `X(R) = q^{-t+H} W_cen(R) <= 2^21 * A(R)`, `A(R) = prod_j E_U[rho_j]`
— the UNREDUCED form the consumer needs, stated as a genuine sum over
the actual junctions.

The claim is AGGREGATE. No per-junction bound is asserted. No
decomposition into coset / accident / bulk columns is asserted, and in
particular no clause licenses discarding a column before the sum is
taken: every column that contributes to `E_U[rho_j | null]` is inside
the sum at its actual weight.

## BINDING NOT-EVIDENCE CLAUSE (symmetric; the load-bearing repair)

A single-junction measurement multiplied by 33 ("uniform stacking",
`x**33` vs `2**21`, `m4_assembly_verifier.py::gate_calibration`,
lines 402-417) is NOT evidence FOR C2''-r3 and NOT evidence AGAINST it.

This clause is symmetric by design and it retires, in one stroke:
- F-round 2's survival read ("worst clause-(ii) bulk ratio 1.0662 ...
  -> 14.53% of the 21-bit reserve (~85% margin)", `node.json:8`), and
- this pilot's F-d refutation read (482.46% of the reserve at
  t=2, q=32801).

Both are the same arithmetic applied to different columns of the same
banked rows. Neither may stand while the other falls. The pose's own
text already disclaims the uniform form ("No uniform per-junction bound
and no factorization identity are asserted", `statement.md:22-23`); this
clause makes the disclaimer binding on the EVIDENCE as well as on the
claim, which is what was missing.

### Prior partial adoption of this clause (convergent, independent)

The survival half of this clause was ALREADY adopted on 2026-08-01 and
never propagated to `node.json`:

> "1. **The C2R2 "14.53% of reserve" margin is NOT evidence about the
> true joint ratio** — it stacks one-junction proxies, and the 4-wise
> trap realizes all-local-statistics-iid with truth 2^22. Empirical
> support for the measured proxy only."
> — `notes/pro_briefs_20260801/responses/BRIEF2_ADVERSARIAL_AUDIT_SUMMARY.md:40-43`

with the construction:

> "**The 32-wise trap (the centerpiece):** at the ADMISSIBLE gate prime
> q = 3*2^41+1, the 33 moment-curve forms on F_q^32 are 32-wise
> independent — every proper subtower exactly iid — yet the full product
> is q > 2^21, via a unique circuit supported on ALL 33 junctions."
> — same file, lines 16-22

C2''-r3 simply makes that demotion symmetric and puts it in the node.

### Why no column-stripping convention can be repaired

The overflow mechanism is ROW-DEPENDENT, so no fixed choice of which
column to strip is safe:

- at (t=2,q=32801) and (t=4,q=193) the whole conditional mass is in the
  COSET column (`coset_mass_share` = 1.000000 vs `uncond_coset_share`
  = 0.385) — coset selection;
- at (t=4,q=97) `coset_leakage` = 0.9807 < 1, and the overflow is
  carried by the ACCIDENT column (factor 3.7834, 63.3 bits at 33x).

The independently-built nullity compiler reached the same split from
the other side: "the joint excess `R` is carried by the `delta = 0`
stratum" and "L9 the joint excess is carried by delta=0 (91% at
(32,4,97))" — `notes/pilots_20260802/c2pp_nullity_structure/REPORT.md:11,67`
— i.e. NONCOSET at exactly the row where my `coset_leakage` < 1.

## PRE-REGISTERED FALSIFIER (fixed here, before any round-4 computation)

C2''-r3 is REFUTED by either:

- **(G-a) DIRECT**: a replayable measurement of
  `sum_{j in J} log2( E_U[rho_j | state_{<j} null] / E_U[rho_j] )`
  over a set `J` of `|J| >= 8` CONSECUTIVE junctions of a SINGLE
  nested tower at a single admissible row, together with a stated and
  separately justified junction-count transport `J -> 33`, whose
  transported total exceeds 21 bits. The transport must be justified
  on its own terms; uniform stacking is excluded by the not-evidence
  clause above.
- **(G-b) SELECTION GROWTH**: a demonstration that the coset selection
  factor `omega_j := P[state_j in the coset column | null] /
  P[state_j in the coset column]` has an aggregate `sum_j log2(omega_j)`
  growing without bound in `q` along admissible rows, measured on
  `>= 8` consecutive junctions at `>= 3` increasing q-scales.

NOT falsifiers (explicit, and DIFFERENT from the retired list): raw or
stripped single-junction ratios at any magnitude; any 33x uniform
stack; per-column vacuity; failure of any factorized or per-junction
proxy.

## WHY THIS IS THE WEAKEST FORM

- It is what the consumer needs and no more
  (`REDUCTION_PACKET.md:51,62`; `conditional.md:3-5`).
- It is not vacuous at the rows that carry the loss — the defect that
  makes the current clause (ii) untestable there.
- It is measurable by the existing kernels, extended in one direction
  only: junction DEPTH.

## COST OF THE NEXT DECISIVE TEST

The pose's own honest-gaps line already names the bottleneck:

> "No multi-junction joint measurement beyond t=4/n=32"
> — `C2PP_POSED_20260710.md:92-93`

Every banked C2'' number — M1's, round 2's, and this pilot's — is a
shallow-tower measurement transported to 33 junctions by convention.
The missing instrument is a nested-tower census that carries `>= 8`
consecutive junctions of one tower with exact conditional means at each.
That instrument does not exist in the repo. Building it is the
mystery's real next step, and until it exists C2'' is neither supported
nor refuted by any banked number — it is UNMEASURED at its own
quantifier depth.

The 32-wise trap sets the bar: any instrument with reach `k < 33` can
be defeated by construction at an admissible gate prime. So `>= 8`
junctions is a MINIMUM for a meaningful reading, not a sufficient
depth, and the honest statement is that the decisive test may require
an all-33-junction argument rather than any census at all.

---

## MANDATORY PIN IF ANY THREE-PART FORM IS KEPT

`theta` is NOT a convention. It is a load-bearing constant that decides
the verdict, and the pose's claim that it is immaterial is false on the
pose's own 8 rows:

> "theta = 2 is a pose-time convention (results insensitive for theta
> in [2,4] at the 8 rows)"
> — `C2PP_POSED_20260710.md:93-95`

Measured (`fdd_theta_fragility.py`), F-b's own kill rule over F-b's own
search set, nothing changed but theta:

| theta | x_max | F-b score | % of reserve | F-b |
|---|---|---|---|---|
| 2.0 | 1.066159 (t=3,q=193) | 3.0508 bits | 14.53% | does not fire |
| 2.5 | 2.238705 (t=2,q=8353) | 38.3683 bits | 182.71% | **FIRES** |
| 3.0 | 2.238705 | 38.3683 bits | 182.71% | **FIRES** |
| 4.0 | 2.238705 | 38.3683 bits | 182.71% | **FIRES** |

Mechanism: at (t=2, q=8353) the theta=2 cut calls three classes
accidents, with class ratios `6.6204` (k=7), `2.2414` (k=12) and
`2.1429` (k=14). The last two clear theta=2 by 0.24 and 0.14. Any
theta > 2.2414 returns both to BULK, where they are charged 33x at
2.2387 per junction = 38.37 bits, instead of once at 0.0003 bits.
The 85% margin is produced by that classification, not by the tower.

Therefore any surviving three-part form MUST pin theta as an operative
constant (like P-CONS and P-FIELD), and must carry a stability
requirement: the verdict may not change over the declared theta range.
C2''-r3 above avoids the issue by taking no decomposition at all.

---

## DOWNSTREAM EXPOSURE FLAGGED (not repaired here)

The repo-wide FD (Finite Defect) schema takes C2'' as its first
instance and cites the number this pilot shows is selection-biased:

> "First instance: the c2pp bulk identity (worst case 1.0662,
> monotone-decreasing slope)."
> — `notes/roadmap/sections/03-unifying-lemmas.md:519-524`

1.0662 is the max of `bulk_ratio` over rows with `bulk_ratio > 0`
(`c2r2_local.py:93`), and `bulk_ratio` is identically 0 at 3 of the 4
rows where the joint factor overflows. `notes/roadmap/sections/07-tracks.md:1913`
already gates the schema on this adjudication ("H2 FD as a schema only
after the c2pp instance adjudicates"). The coordinator should decide
whether FD's first instance survives.
