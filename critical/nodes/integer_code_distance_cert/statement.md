# integer_code_distance_cert

- **status:** TARGET
- **closure:** open row certificate
- **refs (legacy repo):** ['proof_sketch/s2_paid_ledger.md#3']

## Statement

For every row that a downstream prize certificate assigns to this lattice
route, pin the prime field, quotient order and root, class cell and its exact
cardinality, support bound `2l'`, explicit integer kernel matrix, and allowed
cyclotomic-relation basis. Then bank a machine-checkable certificate that no
non-cyclotomic ternary kernel vector of weight at most `2l'` remains and check
that the certified cell cardinality is greater than the row budget `B*`.

There is no hidden finite registry of official row primes. Closure must
therefore be either uniform over every admissible row assigned to this route,
or explicitly exhibit-scoped with every downstream claim narrowed to the same
field. Exact finite search proves procedure totality but does not prove that
its verdict is collision-free. The C-4 toy anchor is a format exemplar only.

The proved `integer_code_distance_high_field_folded_box_exclusion` pays the
complete order-128 folded cube whenever the row characteristic satisfies
`p>253^32`: every ternary kernel vector is then antipodal/cyclotomic. This is
an exact branch theorem, not a promotion. Lower characteristics, other
quotient orders, the universal row assignment, and the row's value-set budget
remain open.

## Attack surface

Before computation, bind the literal row payload and prove that its class count exceeds `B*`. Apply the high-field order-128 theorem where available. On a residual pinned row use: (1) pseudo-Boolean/SAT with proof logging (VeriPB-style); (2) MITM bands as baseline; or (3) LP/Delsarte. A collision verdict is a valid route outcome but does not close this no-vector target. E24's BKZ hunt is search evidence only.

## Falsifier

a non-cyclotomic ternary kernel vector inside the declared support bound, or a declared cell whose exact cardinality is at most `B*`

## Addendum (2026-08-07, round-21 closability probe — NOT closable via the transported distance laws)

Probe verdict (notes/pilots_20260807/red_closability_probes/): the
Z-1/Z-2 transport CANNOT close this node — hypotheses H1-H3 hold
and the shift-0 scope check PASSES, but the system supplies ell = 1
odd-power condition against the ell = 65 the threshold needs, and
ell = 1 is PERMANENT: multi_multiplier_reduction (REFUTED) proves
the k-multiplier residue matrix is a rank-1 outer product for every
k. Z-2 at ell = 1 yields only "weight >= 3", attained. The PROVED
high-field branch (p > 253^32) covers 5.02% of the e = 1 prime-row
log-window; the four pinned Proth exhibits sit 84.5-88.5 bits below
it. This node remains the genuine open content of the (re-posed)
mystery-5/kernel-lattice line.

## Round-22 addendum (2026-08-07, coordinator-applied on replay): exact fold-reduction thresholds — universal at toy scale; the residue is row-unboundedness, not per-row cost

The round-22 ge_floor_falsifier pilot made the certification
threshold EXACT and UNIVERSAL via the fold reduction (K_p has a
non-cyclotomic ternary vector of support <= 2l' iff p | Norm(w) for
a nonzero w in the {-2..2}^h box with ||w||_1 <= 2l'):

- **THEOREM (toy, PROVED-exhaustive):** for every p = 1 mod 16
  above 463249 (full radius) or above 4049 (radius 6), K_p is
  empty of non-cyclotomic ternary vectors; both thresholds
  ATTAINED. For N' = 8: threshold 137. The norm-instrument family
  cannot reach the prize rows: MAXNORM's plausible sharpening
  (base 4(h-1), weakly supported and false at h = 2) gives
  2^255.27 at h = 64 vs the needed 2^250 (base 224.6), and
  TIGHTEMPTY sits within 0.41 bits of MAXNORM at h = 8 — no
  which-primes refinement rescues it. The smallest new theorem is
  a certified lambda1 lower bound on the folded kernel lattice,
  priced in the round-22 lattice_cone_certificate addendum
  (laptop-scale per row at N' = 128).
- This node's "no hidden finite registry of official row primes"
  clause is CONFIRMED as the binding residue: the bad primes run
  up to the threshold with no gap. Per-row certification is cheap;
  the universal form (this node) remains the open content — now
  the CONVERGENCE POINT of three lanes (mystery 5's GE-WEAK,
  round-21 PROBE 1's ell-condition system, and the crossing safe
  side's ternary relation-set weight enumerator, round-22
  bb_nu_transport).
Source: notes/pilots_20260807/ge_floor_falsifier/
(coordinator-replayed).
