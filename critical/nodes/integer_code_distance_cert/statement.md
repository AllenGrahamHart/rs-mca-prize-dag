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

## Round-23 addendum (2026-08-07, coordinator-applied on replay: ge_lattice_cert + the cw_shared_target qualification)

**THE LITERAL-EXHIBIT HALF OF THE STATUS RULING IS NOW SUPPLIED:**
e1_folded_no_vector_certificate_128_payload is PROVED — a complete
enumeration certificate with a deterministic standalone checker at
the exact pinned field/root (2,061,127,954 nodes, EMPTY;
fail-closed planted control at the same dimension/determinant).
What this does NOT supply, per this node's own ruling: the
family-uniform theorem, the narrowing of consumers to the exhibit
field, or the value-set side. The four deployed Proth prize rows
(167-171 bits, below the 253^32 analytic threshold) now carry
radius-graded complete certificates to support <= 24 (12 swaps —
four times the archimedean-free radius L = 6); their full-radius
cells are priced at 2^60-2^63 (LLL) / 2^38-2^40 (BKZ-90) — the
laptop-scale reclassification holds only above ~242 bits (the
PRICE-CLIFF). The GS-FLOOR obstruction (round-23, proved) shows no
lambda_1-floor certificate exists for ANY basis at admissible
rows: the enumeration is irreducible, only its price moves.
Witness-count note: the round-22 toy thresholds remain ATTAINED;
the attaining sets are full 2h-orbits (16, not 2, at p = 463249 —
CATCH-23A).

**THE CONVERGENCE QUALIFIED (round-23 cw_shared_target):** this
node remains the convergence point of the GE-WEAK / PROBE-1 /
crossing-deep-stratum lanes at the OBJECT level (one functional:
the ternary theta / weight enumerator of K_p), but the round-23
pricing shows the crossing lane's LIVE crux (Acc_shallow +
aperiodic S) does NOT reduce to this object — its only bridge
loses >= 4.565e11 bits at the official row. One object, two
targets: closing this node serves mystery 5's per-row line and
mystery 2's terminal-adjacent form; it does NOT close the
crossing crux.

## Round-24 BOARD EVENT (2026-08-08, coordinator-replayed: kernel_window_hunt): THE FAMILY-UNIFORM EMPTINESS FORM IS FALSE

**Witness of record (REPRO PASS, coordinator-replayed):** at the
BLS-PROVEN 247-bit prime P = 18838259725604806405449165455743336372
0577825648201882790490986150665597569, P = 1 mod 128, P < 2^256:
Norm(w) = P exactly for a box vector with ||w||_1 = 127 <= 2l' =
128, whose ternary lift is a NON-CYCLOTOMIC kernel vector of K_P.
Plus 20,636 W_TOP hits (2,747 stored with all-distinct primes;
probable primes labelled as such). AND the mis-filing catch: the
repo has held EIGHT exhibited (w, p) pairs at N' = 256 (226-255
bits) since July 2026 — the e1_n256 campaign's own audit dismissed
a 248-bit prime as "below 2^250 and therefore harmless", filtering
by PRIZE-INTERVAL membership instead of admissibility; the uniform
form was already dead at N' = 256 on banked evidence.

**CONSEQUENCE:** per this node's own status ruling, the
"family-uniform theorem" branch is CLOSED OFF; the living branches
are (a) EXHIBIT-SCOPED closure with every consumer formally
narrowed, (b) an o(1)-SPARSITY re-pose (untouched — even
supported — by the measurements), or (c) a LARGE-v_2 RESTRICTION:
the generic witnesses have v_2(p-1) = 7 while EVERY pinned/deployed
row has v_2(p-1) in [92, 200] — the witness rows cannot support
the deployed 2^41+ smooth domains, making (c) a real and possibly
defensible narrowing. THE CHOICE AMONG (a)/(b)/(c) IS SURFACED TO
THE USER (genuine consumer-scope decision). Source:
notes/pilots_20260808/kernel_window_hunt/ (repro_witness_proven.py
REPRO PASS; calibration C1-C4 against the round-22 exhaustive
ground truth; coverage 2^22.0 of the box; the novelty subtraction
amended by the pilot itself — the N' = 128 exhibit and the stated
conclusion are new; the forward-direction method and N' = 256
exhibits are prior art).
