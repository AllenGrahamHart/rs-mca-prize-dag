# PREREG — r35_l2_gate (round 35)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r34_m2_decision/REPORT.md` (round 34)
2. `background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/statement.md`

## Mandate

R-L2 — THE DECISIVE QUESTION ON THE BOARD. Round 34 proved the
syndrome realization layer M(Z)Q_Z = 0 is (m+2)(4m+1) equations on
16m unknowns — overdetermined by 4m^2-7m+2, with m = 1 the UNIQUE
underdetermined case — and found ZERO genuine (SAT1)-profile
objects with e = m = 2 in 2,800 curves over two fields (every hit
the predicted degenerate rank-1/s!=0 family; the e=2 Kummer
analogue analytically dead because the leading Z-coefficient must
itself be a degree-rho locator, not a constant). NOBODY has ever
exhibited a (SAT1)-profile pencil with e = m at any m >= 2.
DECIDE IT AT m = 2: does a (4m+1) x 4m Hankel pencil with minimal
index exactly m, generic rank 4m-1, s = 0 exist? EMPTY for
m >= 2 => the strict endpoint closes outright (via the banked
"e = m is the entire difficulty" reduction). NONEMPTY => the
campaign's first real m >= 2 object: measure its T, and F1/(NEWCAP)
are finally exercised (three rounds of zero power). Either answer
is worth more than anything else on the board.

## Deliverables

**D1 — THE STRATUM AS AN EXACT OBJECT.** From anchor 2 (the RNC
node): parameter forms Q_0..Q_m independent, nu_Q a degree-m
rational normal curve. Structure the m=2 system exactly: WHICH 4
conditions are the overdetermination — is the +4 transverse, or
does the stratum carry excess dimension? Round 34's own incidence
count (23 + 32 - 36 = 19 >= 0, expected codim ~13 in y-space) says
nonempty-expected while its corrected TCAP ledger says
empty-expected — RECONCILE the two counts or name exactly why they
answer different questions (the naive-count caveat is banked; a
count carries no verdict on its own).

**D2 — THE CONSTRUCTIVE ATTACK.** Round 34 bank 3 beat a worse
count (deficit 17 at m=3) by INVERTING: choose the object first,
read the parameters off it, pay only combinatorics. Try the
analogue here: ansatze honoring the analytic kill (Q_2 a genuine
degree-rho locator with prescribed roots), self-reciprocal /
symmetric families, the k in {2,3} admissible symmetries (the only
ones round 34 left alive), designed domains. ALSO: DEF-ID — the
W-layer (BIV-G) deficit and this layer's overdetermination are the
SAME quadratic 4m^2-7m+2 (observed by the coordinator across two
quarantined round-34 pilots; posed, unexplained). Determine whether
DEF-ID is a real transport (a map between the two systems that
would carry bank 3's m=3 witness technology into an (L2)
construction) or a coincidence of counts — either finding is a
deliverable.

**D3 — THE EMPTINESS ATTACK.** Can the +4 be made a THEOREM at
m = 2? Characterize the nullity-drop locus: for which curves Q
does M(Z)Q_Z = 0 admit a nonzero solution (exact algebraic
condition, not a rate)? Round 34 measured nullity 0 on 60/60
random curves per field; the question is whether the solvability
locus provably misses the (SAT1)+design conditions. Even an
m=2-only emptiness proof moves the board; an all-m >= 2 proof
closes the strict endpoint.

**D4 — VERDICT.** Misses first. If a witness: the full
(SAT1)-(SAT5) table, T measured, a* vs 7m-1 = 13 (F1's first real
test), two fields. If empty-with-proof: the exact statement +
hypotheses. If neither: the named gap, graded honestly
(fields-searched negatives are not theorems), and which of D1's
two counts survived contact.

## Blind priors to register

P(the e=m=2 stratum is nonempty), P(a witness lands this round),
P(an emptiness proof lands this round), P(DEF-ID is a real
transport rather than a coincidence), P(the +4 is transverse).

## Pilot registrations

Written after reading EXACTLY the two named anchors
(`notes/pilots_20260811/r34_m2_decision/REPORT.md`,
`background/nodes/rate_half_ca_hankel_endpoint_rational_normal_kernel_curve/statement.md`)
and BEFORE any other read, any grep, any ls, and any interpreter
invocation. No addenda after this point.

### R0 — route order (fixed in advance, not to be reordered to chase a positive)

(a) verify the m=2 block structure numerically; (b) verify or refute my
pre-committed reduction D-B; (c) reconcile the two counts (D1);
(d) run the inversion D-F (D2 constructive); (e) certify or refuse any
hit; (f) emptiness analysis (D3); (g) verdict. If (d) produces a hit I
still run (f) and report the emptiness side honestly.

### Pre-committed derivations (falsifiable, registered BEFORE any computation)

I derived the following from the two anchors alone. Each carries its
own falsifier; if a falsifier fires I report the refutation of my own
derivation ahead of any result.

- **D-A (block split).** At m=2 write `M(Z)=M_r(y_0)+Z M_r(y_1)`, `M_r(y)`
  the `9x8` Hankel `M[a][b]=y[a+b]`, `y_i in F^16`, and
  `Q_Z=Q_0+ZQ_1+Z^2Q_2` with `deg Q_j<=7`. Then `M(Z)Q_Z=0` splits into
  four 9-row blocks: `M_0Q_0=0`; `M_0Q_1+M_1Q_0=0`; `M_0Q_2+M_1Q_1=0`;
  `M_1Q_2=0`. **Blocks 0 and 3 are 9 equations of rank exactly 9 on
  `y_0` resp. `y_1`, so each leaves a 7-dimensional space** (the
  recurrence/locator space of `Q_0` resp. `Q_2`), and the two cross
  blocks are then **18 equations on 14 unknowns: the entire `+4` lives
  in the cross blocks.** FALSIFIER: a nonzero `Q_0` for which block 0
  has rank != 9 on `y_0`.
- **D-B (the exact solvability criterion — the load-bearing one).** If
  `Q_0,Q_2` are squarefree of degree 7 with disjoint root sets `S_0,S_2`
  (so `|W|=|S_0 u S_2|=14`), then `M(Z)Q_Z=0` has a nonzero solution
  **iff** there exist `f,g in F[X]` of degree `<=4`, not both zero, with
  `Q_2 f == Q_1 g (mod Q_0)` and `Q_1 f == Q_0 g (mod Q_2)`.
  Equivalently the `14x10` matrix `Phi(Q):(f,g) -> (Q_2f-Q_1g mod Q_0,
  Q_1f-Q_0g mod Q_2)` has rank `<=9`. Recovery: `lambda_x=u_xf(x)/Q_1(x)`
  on `S_0`, `mu_x=u_xf(x)/Q_0(x)` on `S_2`, `u_x=1/prod_{y in W,y!=x}(x-y)`,
  `y_0=sum lambda_x v_x`, `y_1=sum mu_x v_x`. FALSIFIER: any `Q` with
  `Q_0,Q_2` squarefree/coprime where `nullity(36x32) != 10-rank(Phi)`.
- **D-C (the +4 is not the existence count).** The existence locus is the
  rank-`<=31` locus of a `36x32` matrix, equivalently rank-`<=9` of the
  `14x10` `Phi`: **determinantal codimension `(36-31)(32-31)=5 =
  (14-9)(10-9)`, not 4.** So the round-34 "`+4`" is an equation-count
  excess, and the correct naive existence codimension in the 23-dim
  projective curve space is **5**, giving expected dimension **18**.
  FALSIFIER: a measured hit rate on random curves incompatible with
  `q^-5` after the degenerate family is excluded.
- **D-D (Kronecker ceiling on the minimal index).** For a `(4m+1)x4m`
  Hankel pencil `M_r(y_0+Zy_1)` of generic rank `4m-1` whose `4m-1`
  kernel roots are distinct over `F(Z)-bar`, the **left** kernel is
  spanned by `Q_Z` and `X Q_Z`, so both left minimal indices equal
  `e`, and Kronecker bookkeeping gives `3e+delta=4m-1` with `delta>=0`
  the size of the regular part. Hence **`e <= (4m-1)/3`; at `m=2`,
  `e<=2`, and `e=m=2` forces `delta=1` — exactly one parameter
  `z_0 in P^1`, with multiplicity one, at which the weight drops to 6.**
  FALSIFIER: an `e=2` witness whose rank-drop divisor is not a single
  reduced point.
- **D-E (the incidence count is contaminated by an excess component).**
  The locus `{Q: Q_0,Q_1,Q_2 share a root x*}` has dimension **21** in
  `P^23` and lies inside the solvability locus (take
  `y_0=lambda v_{x*}`, `y_1=mu v_{x*}`), whereas the expected dimension
  of that locus is **18**. So the solvability locus carries an **excess
  component of dimension 21**, the round-34 incidence count
  `23+32-36=19` is realized on the degenerate component (which in the
  incidence variety has dimension `20+3=23>19`), and **no dimension
  count can carry a verdict on the good stratum.** FALSIFIER: a
  common-root `Q` with `nullity(36x32)=0`.
- **D-F (the inversion, bank-3 analogue).** Clearing the congruences of
  D-B gives the identities `Q_2f-Q_1g-Q_0h=0` and `Q_1f-Q_0g-Q_2k=0`
  with `deg h,k<=4`: **24 equations, bilinear in the groups
  `A=(Q_0,Q_1,Q_2)` (24 unknowns) and `B=(f,g,h,k)` (20 unknowns).**
  For fixed `B` the system is a **square `24x24`** homogeneous system in
  `A`, so a curve exists iff `det M(B)=0` — **ONE condition on a
  19-dimensional projective `B`-space.** Predicted search cost `~q`
  random `B` draws, or one univariate root-find of a degree-`<=24`
  determinant along a line in `B`-space. FALSIFIER: `det M(B)` is
  identically zero (making the route vacuous) or its zero locus yields
  only degenerate `Q`.

### Blind priors (numeric, registered before any evidence)

- **P1** P(the `(L2)` stratum with `e=m=2`, generic rank 7, `s=0` is
  **nonempty over `F-bar`**) = **0.75**.
- **P1b** P(nonempty **over a small prime field** `q in {97,193}`,
  given nonempty over `F-bar`) = **0.85**.
- **P2** P(**a witness lands this round**, fully certified: `e=2`
  exactly, generic rank 7, `s=0`, `Q_j` independent) = **0.60**.
- **P2b** P(the D-F inversion is the route that produces it, given a
  witness) = **0.80**.
- **P3** P(**an emptiness proof lands this round**) = **0.08**
  (conditional on no witness: 0.20).
- **P4** P(**DEF-ID is a real transport** — an actual map between the
  W-layer/(BIV-G) system and this one, not a coincidence of the
  quadratic `4m^2-7m+2`) = **0.30**. P4b P(I can even locate the
  (BIV-G) statement inside my quarantine) = 0.55.
- **P5** P(**the `+4` is transverse** — i.e. at a generic point of the
  good stratum the 36 equations cut exactly the expected codimension
  and the good stratum carries **no** excess) = **0.55**; and
  **P5b** P(the operative existence codimension is **5**, not 4, i.e.
  D-C holds) = **0.90**; **P5c** P(the solvability locus has an excess
  component of dimension 21, i.e. D-E holds) = **0.88**.
- **P6** P(D-B verifies numerically as stated, no correction needed) =
  **0.70**. **P7** P(D-D's `e<=(4m-1)/3` ceiling verifies) = **0.80**.
- **P8** P(a witness, if found, has `T>=1` split parameters over the
  multiplicative domain `mu_32` **without** designing the domain) =
  **0.05**; P(`a*` measurable and `a* in {13,14}`) = **0.80**.
- **P9** P(the whole `(L2)` question is already banked in-repo in a
  form that answers it) = **0.10** (CATCH-24A will test this).

### MISS-2 GUARD (mean-vs-max, registered in advance)

The round-34 proven guard pattern, re-registered because I anticipate
both a max-over-sample and a rate-vs-existence step:
(i) **No max over a finite sample becomes a bound.** Any "max nullity /
max `n7` / max rank observed in `n` draws" stays a sample maximum and is
never converted into a statement about the true maximum.
(ii) **No mean/rate becomes an existence or emptiness verdict.** A
measured hit rate (e.g. `~1/q` for the inversion, `~q^-5` for random
curves) is evidence about a *distribution*, never a proof that the good
stratum is (non)empty; conversely 0 hits in `n` draws is a
fields-searched negative and I will say so in the verdict line itself.
(iii) **A single exactly-verified witness IS a theorem** (existence is
witness-checkable) — this is the one asymmetry I claim, and I claim it
only after re-verifying `M(Z)Q_Z=0` entrywise over the field, plus the
`e`, rank and `s` side conditions, on **two fields**.
(iv) **Dimension counts (mine and TCAP's) carry no verdict** whenever an
excess component is present (D-E); I will not quote 19, 18, `+4` or
`+5` as evidence for or against emptiness.

### Zero-power declarations (pre-declared)

- **Z1** Any negative search at `q in {97,193}` has **zero power** over
  the existence question: the good locus has expected codimension 5 and
  `q^-5 ~ 10^-10`.
- **Z2** The Thom–Porteous/Fulton–Lazarsfeld nonemptiness of a
  degeneracy locus of expected codimension 5 in `P^23` has **zero
  power on the good stratum**, because D-E predicts an excess component
  that already accounts for it.
- **Z3** If no witness arrives, **F1 and (NEWCAP) are untested for the
  fourth round running** and I claim zero power on them.
- **Z4** `T` measured on a synthesized `(L2)` object over a domain not
  designed for it has **zero power** over `(SAT3)`; `T=0` there is not
  evidence of anything.
- **Z5** Existence over `F_97`/`F_193` does not by itself give existence
  at the endpoint field `q ~ 2^128`; I will state explicitly whether any
  construction found is field-generic (a parameter identity valid over
  `Z`) or field-specific.
- **Z6** Anything I cannot read (the other `r35_*` dirs, the campaign
  ledger) is outside my evidence base; DEF-ID may be unresolvable from
  inside my quarantine and I pre-declare that as a possible outcome
  rather than a failure to report.
