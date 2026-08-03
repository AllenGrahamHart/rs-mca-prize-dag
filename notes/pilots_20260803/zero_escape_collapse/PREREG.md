# Pre-registration (written BEFORE any computation), 2026-08-03

Pilot: zero-escape collapse (PRIMARY) + `V <= m/2` for non-collapsing
systems (SECONDARY).  Attack route: duality (route 2 of the brief).

## The route, stated before running anything

Annihilator form.  `Row = sum_a G_{z_a}(C_{S_a}) <= C_U x C_U`,
`U = union S_a`, `m = |U| - k`.  A functional on `C_U x C_U` is a pair
`(lambda, mu)` of vectors in `F^U` modulo `(RS_k|_U)^2`; it annihilates
`Row` iff for every ray `a`

```text
(lambda + z_a mu)|_{S_a}  in  RS_k|_{S_a}
```

i.e. iff there are polynomials `p_a`, `deg p_a < k`, with
`lambda(x) + z_a mu(x) = p_a(x)` for all `x in S_a`.  So
`rank = 2m - dim Ann` and the collapse is the statement `Ann = 0`.

Pointwise (collinearity) form: for each `x in U` the points
`(z_a, p_a(x))`, `a` ranging over the rays containing `x`, are collinear
in the `(z, Y)` plane; trivial solutions are `p_a = P + z_a Q`.

Predicted obstruction (V = 4, blocks `A_i := U \ S_i`, `A_0` = points in
all four supports): normalising `p_1 = p_2 = 0`, the four polynomials
`p_3`, `p_4`, `E_1 = (z_4-z_2) p_3 - (z_3-z_2) p_4`,
`E_2 = (z_4-z_1) p_3 - (z_3-z_1) p_4` lie in one 2-dimensional PENCIL
`M <= F[X]_{<k}` and vanish on `A_0 u A_4`, `A_0 u A_3`, `A_0 u A_1`,
`A_0 u A_2` respectively; the four directions in `P(M)` must satisfy a
CROSS-RATIO equation against the slopes.  Hence a nonzero annihilator
should EXIST whenever the supports are built from four fibres of a
pencil and the slopes are solved from the cross-ratio equation.

## Pre-registered predictions and falsifiers

Fixture **X1**: `q = 17`, `k = 3`, pencil `M = <X^2, 1>`, four fibres
`A_i = {x : x^2 = c_i}` with `(c_1,c_2,c_3,c_4) = (1,2,4,8)` (all
nonzero squares), `U = A_1 u A_2 u A_3 u A_4` (8 points),
`S_i = U \ A_i` (size 6), `V = 4`, `h = 3`, `m = 5`.  Slopes solved
from `alpha/beta = (c_3-c_1)/(c_4-c_1)`, `gamma/delta = (c_3-c_2)/(c_4-c_2)`
with `z_3 = 0`, `z_4 = 1`, then translated to avoid slope 0.

* **P1 (the counterexample).**  `rank(Row) = 2m - 1 = 9` at X1, and
  `dim Rel = Vh - rank = 3`.
  FALSIFIER: `rank = 10 = 2m`.  Then the pencil construction is wrong
  and the collapse survives this attack; I report PARTIAL/no refutation.
* **P2 (gates).**  X1 is combinatorially full-gate: all `|S_a| = k+h`,
  all pairwise `|S_a ^ S_b| = k+1` (uniform depth `d = 1`, so
  "pairwise intersecting" in the pilot's `>= k+1` sense), all triples
  `= k-1` EXACTLY (k-packing SATURATED, not violated), zero escape
  (`S_a^inf = S_a`).
  FALSIFIER: any gate value off these numbers.
* **P3 (cross-ratio criterion).**  With X1's supports fixed and
  `z_3 = 0, z_4 = 1`, sweep all `(z_1, z_2)`.  The set of slope tuples
  with `rank < 2m` is EXACTLY the locus
  `CR(tau_1,tau_2,tau_3,tau_4) = CR(z_3,z_4,z_1,z_2)` predicted by the
  pencil, where `tau_i` are the four pencil directions.
  FALSIFIER: any off-locus tuple with `rank < 2m`, or any on-locus tuple
  with `rank = 2m`.
* **P4 (second fixture, different `k`).**  `q = 17`, `k = 5`, pencil
  `<X^4, 1>`, four fibres of size 4 (`U = F_17^*`, 16 points),
  `V = 4`, `h = 7`, `m = 11`: `rank = 2m - 1 = 21`.
  FALSIFIER: `rank = 22`.
* **P5 (the measured fixtures are explained, not contradicted).**  The
  band-mint verifier's zero-escape clique `(3,5,3,5)` satisfies
  `|S_a ^ S_b ^ S_c| >= k` for all triples, which by the triple-cover
  criterion FORCES `rank = 2m` for EVERY slope tuple; the 60
  deterministic tuples must all give `rank = 2m = 14`.
  FALSIFIER: a tuple with `rank != 14`, or a triple intersection `< k`.
* **P6 (secondary conjecture).**  X1 is non-collapsing (`rank < 2m`)
  with `V = 4 > m/2 = 2.5`, refuting "non-collapsing => `V <= m/2`".
  FALSIFIER: P1 falsified, or X1 failing a gate that the conjecture's
  standing hypothesis list requires.
* **P7 (duality is not tautological).**  For every fixture, the
  independently computed interpolation solution space
  `{(lambda,mu) : (lambda + z_a mu)|_{S_a} in RS_k|_{S_a}}` has
  dimension `2|U| - rank(Row)`, and every basis element really does
  interpolate to `deg < k` polynomials on each `S_a`.
  FALSIFIER: any mismatch.

## Honesty rules fixed in advance

* Measured != proved.  Any statement checked only on fixtures is
  labelled MEASURED.
* If the counterexample verifies, the primary claim "zero-escape =>
  rank = 2m" is REFUTED, and the deliverable is the exact criterion
  plus the proved sufficient conditions, not a proof of the collapse.
* Slope conventions: all slopes finite and pairwise distinct; the
  `z = (0:1)` case is stated separately and not swept.
