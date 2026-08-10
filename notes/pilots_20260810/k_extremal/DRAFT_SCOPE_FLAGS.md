# k_extremal — D3 exact-edit draft package (COORDINATOR-GATED, NOT APPLIED)

Round 29, pilot `k_extremal`, 2026-08-10. Verdict: **HOLE**.
Nothing here is applied. Every block below is an exact-edit proposal for
the coordinator; the E7 idiom (flag, do not silently resolve) is used
throughout. Node ids and line numbers are as read on 2026-08-10.

---

## D3.1 — The four scope flags (E7 style)

### FLAG A — `critical/nodes/mca_grand/node.json` (statement of record)

Append to the statement, after the existing "RATE SCOPE (amber audit
2026-07-06)" clause (which is the precedent idiom this reuses):

```text
ROW-SIZE SCOPE (k_extremal audit 2026-08-10, E7 SCOPE SEAM — FLAGGED,
NOT RESOLVED): "admissible C" is the descriptor family (background/nodes/
descriptor/proof.md:3-8: q=p^e, n=2^s, k=rho*n, checked against q<2^256,
k<=2^40, n | q-1). k <= 2^40 is an UPPER CAP, not a pin, so at rate 1/2
the family is the 41 row sizes n=2^s, k=2^(s-1), s=1..41 (per admissible
field), NOT the single row n=2^41, k=2^40. The rate-1/2 premise this
statement is declared conditional on, rate_half_band_closure, is posed at
"n=2^41, k=2^40" (its statement.md:66) and locates nothing at s<41. No
node establishes k=2^40 as extremal and no node reduces s<41 rate-half
rows to it. The rate-1/2 instance of this claim is therefore presently
carried only at s=41; s<=40 is UNCOVERED. Owner: a new reduction node
(candidate poses in notes/pilots_20260810/k_extremal/DRAFT_SCOPE_FLAGS.md
section D3.2).
```

### FLAG B — `critical/nodes/rate_half_band_closure`

Two defects, one flag. (i) `statement.md:66` opens "Let n=2^41, k=2^40"
— a pin, no quantifier. (ii) `node.json`'s statement of record instead
says "at every admissible rate-1/2 row in the razor slice", which under
the descriptor reading quantifies over all s<=41. The two texts of the
same node disagree on the (n,k) quantifier. Proposed addendum (to BOTH):

```text
ROW-SIZE SCOPE (k_extremal 2026-08-10): this node is posed AT n=2^41,
k=2^40 ONLY. The node.json phrase "every admissible rate-1/2 row" is
hereby read as "every admissible rate-1/2 row AT n=2^41, k=2^40" — i.e.
the quantifier that is live here is over q, not over the row size. The
clause "(log2 q in (255.900,256), the only rows where the band is
nonempty)" is likewise derived at n=2^41: the band interval
[2^33, sigma*=8,592,912,738] is a fixed absolute width, so "the band is
empty elsewhere" is an n=2^41 computation and carries NO information at
s<41. Rate-1/2 rows with s<41 are outside this node. FLAGGED, not
resolved.
```

### FLAG C — `critical/nodes/rate_half_list_adjacent_crossing`

`statement.md:5` and `statement_sections/00-live-contract-and-base-
reductions.md:7` both claim "For every admissible official rate-half
row", but the supplied bracket at `00-...:25-29` is introduced with "At
the prize-max razor row / n=2^41, k=2^40". Claim quantifier strictly
exceeds machinery quantifier — the exact round-28 tiling failure, one
axis over. Proposed addendum:

```text
ROW-SIZE SCOPE (k_extremal 2026-08-10): the claim line quantifies over
every admissible rate-1/2 row; the supplied lower bracket (RHL-LB,
a_L >= k+2^34) is proved only at n=2^41, k=2^40 and is VACUOUS below
k=2^35 (at rate 1/2, [k+2^34, 3n/4] = [k+2^34, 1.5k] is empty unless
k >= 2^35 — exact integer check in this pilot's report). Rows with
s <= 35 have no bracket at all; rows with 36 <= s <= 40 have an
unproved one. FLAGGED.
```

### FLAG D — the "official row" alias collision (documentation-only)

Two incompatible in-repo readings of the term "official row" are both
load-bearing:

- descriptor / official_row_primes_pinning reading: `(p,e,s,rho)` with
  s free under the caps (`background/nodes/descriptor/proof.md:3-8`,
  `background/nodes/ww_row_envelope_clause/specification_frontier.md:9`).
- the `dli_wcl_*` reading: "At every official row (q < 2^256,
  v_2(q-1) >= 41)" (`critical/nodes/dli_wcl_slot_1_5_emptiness/
  statement.md:6`), which pins s = 41.

Proposed: add to `notes/BAND_LANE_DEFINITIONS.md` as a new numbered
definition item —

```text
13. **official row** is AMBIGUOUS in-repo and must never be used bare in
    a new statement. Write either "admissible row" (the descriptor
    family, s free under k<=2^40) or "maximal row" (s pinned; state the
    pin). Existing bare uses are read at their node-local pin; the
    dli_wcl_* family's parenthetical "(q<2^256, v_2(q-1)>=41)" IS an
    s=41 pin and does not cover s<41.
```

### FLAG E — the two maximal-row conventions (second catch, other rates)

Out of the rate-1/2 mandate but found en route and reportable: the repo
carries two mutually exclusive descriptions of the four maximal rows.

- Convention A (n pinned): `critical/nodes/x4_primitive_star_u1_coverage/
  statement.md:11` "N=2^41, K=rho N, rho in {1/2,1/4,1/8,1/16}";
  same in `b2b_near_tail_bound/statement.md:8` and
  `u2c_exact_slice_extras_budget/statement.md:6`. Gives k = 2^40, 2^39,
  2^38, 2^37 at the four rates.
- Convention B (k pinned at the cap): `critical/nodes/petal_g1_layer_maps/
  notes/cp_packet_20260713/cp_statement.md:33-35` "the four official
  maximal rows are n = 2^41..2^44, k = 2^40"; used by
  `critical/nodes/petal_g3_pricing_multiplicity/statement.md:19`
  (n = 2^41,2^42,2^43,2^44). Gives k = 2^40 at all four rates.

They agree ONLY at rate 1/2. Under the caps, convention B's rows are the
cap-saturating ones; convention A's rates-below-1/2 rows are k-deficient
by 1-3 binary orders. Proposed: a coordinator adjudication note, since
this decides which rows the clean-rate lane — the campaign's PRIMARY
closure target per `critical/nodes/mca_grand/statement.md:13` — is
actually about.

---

## D3.2 — The reduction theorem, POSED NOT PROVED

Three candidate poses, in decreasing order of my confidence. None is
claimed. Each carries a pre-registered falsifier.

### POSE 1 (list side) — the small-row triviality corridor

```text
CLAIM (RHL-TRIV). Let C = RS[F,D,k] be an admissible rate-1/2 row,
n = 2k, B* = floor(q/2^128). If binom(n,k) <= B*, then a_L = k is an
exact adjacent list crossing: L_1(k) <= B* < L_1(k-1).
```

Sketch (elementary, 3 lines, NOT refereed): the upper side is
`background/nodes/list_interleaved_support_census/statement.md:13` (SC)
at a=k, i.e. L_m(a) <= binom(n,a); the lower side is that fixing any
(k-1)-subset S and requiring c|_S = u|_S leaves a 1-parameter family of
q codewords, each of agreement >= k-1, so L_1(k-1) >= q > floor(q/2^128)
= B*. Adjacency is then immediate.

Exact reach (this pilot's computation, `tools/ramguard tiny` exact
`math.comb`): binom(2^s, 2^(s-1)) <= floor(q/2^128) with q < 2^256 is
satisfiable ONLY for s <= 7, and then only above a threshold:

```text
s : n    k    log2 binom(n,k)   q must exceed 2^t, t =
1 : 2    1      1.000            129.000
2 : 4    2      2.585            130.585
3 : 8    4      6.129            134.129
4 : 16   8     13.652            141.652
5 : 32   16    29.163            157.163
6 : 64   32    60.669            188.669
7 : 128  64   124.171            252.171
8 : 256  128  251.673            379.673  -> exceeds 2^256: NEVER
```

So POSE 1, if proved, discharges exactly the corner
`{s <= 7} x {q > 2^(128 + log2 binom(2^s,2^(s-1)))}` and nothing else.
FALSIFIER: an admissible rate-1/2 row with binom(n,k) <= B* and
L_1(k) > B*, or with L_1(k-1) <= B*. NOTE: this is the LIST side only.
`B_mca` is a bad-SLOPE count with `B_mca(a)/q = epsilon_mca` (see
`critical/nodes/rate_half_band_closure/statement.md:78-80`), so the
binomial argument does NOT transfer to the MCA side; an MCA analogue is
a separate, unposed obligation.

### POSE 2 — k-monotonicity (the theorem the flag hoped for)

```text
CLAIM (RH-MONO). For admissible rate-1/2 rows, a located adjacent
crossing at (n,k) = (2^41, 2^40) implies a located adjacent crossing at
(2^s, 2^(s-1)) for every s <= 41, at the same q (or with an explicit
q-transport).
```

I DO NOT BELIEVE THIS AND DO NOT RECOMMEND IT AS THE ROUTE. Reasons,
registered: (i) the crossing index a is measured on a per-row grid of
size n, so "the same crossing" has no row-free meaning without a
normalisation, and the natural normalisation a/n is exactly what the
band arithmetic refuses to be uniform in; (ii) the proved rate-1/2
floors are ABSOLUTE-width objects — sigma_0 = 8,594,128,895 ~ 2^33.0007
(`rate_half_band_closure/statement.md:90-92`) and sigma* =
8,592,912,738 (`rate_half_cyclic_rotated_prefix_floor/statement.md:39`)
— so they are not even evaluable once k < sigma_0, i.e. below s = 34,
and cannot be the image of any monotone transport; (iii) B_C's
dependence on k is not shown monotone anywhere in-repo (CATCH-24A greps
in the report). FALSIFIER (cheap, and I recommend running it before any
work on this pose): any admissible small rate-half row whose exact
crossing index, normalised, sits outside the n=2^41 corridor
j/n in [0.4,0.5] that `critical/nodes/census_bounded_scales/
statement.md:9` assumes.

### POSE 3 (RECOMMENDED) — the per-s family statement

```text
CLAIM (RH-FAMILY). Re-pose the rate-1/2 lane as a family indexed by
s = 1..41, and prove the crossing per s-band rather than per row:
  band I  (s <= 7)      : POSE 1's triviality corridor + a residual
                          small-q sub-band, finite and enumerable;
  band II (8 <= s <= 33): no floor construction is evaluable (sigma_0
                          exceeds k); genuinely open, and the CHEAPEST
                          place to look for a counterexample to any
                          uniformity hope;
  band III (34<=s<=40)  : the floors become evaluable but the bracket
                          [k+2^34, 3n/4] stays empty until s = 36;
  band IV (s = 41)      : the existing lane, unchanged.
```

This is the E7-conforming shape: it makes the uncovered set a named
object with an owner per band instead of an invisible quantifier.
FALSIFIER for the whole pose: a proof that the challenge's "assuming
|F| is sufficiently large" proviso (`background/nodes/
official_row_primes_pinning/proof.md:27`) is intended to exclude
s < 41 — which would convert the HOLE into PINNED and retire bands
I-III. I could not settle that from in-repo text; it is a
rules-citation question for `rules_freeze`, and `rules_freeze/
statement.md:9`'s own tie-break ("on any residual ambiguity the
campaign plans against the stricter reading") currently forces the
HOLE reading.

---

## D4 — Blast radius (domain-level skim, not a re-audit)

### k-UNIFORM (survive a row-size widening unchanged)

| node | evidence |
| --- | --- |
| `background/nodes/descriptor` (PROVED) | `proof.md:3-8`: symbolic in `(p,e,s,rho)`; total on the admissible family |
| `background/nodes/list_interleaved_support_census` (PROVED) | `statement.md:6-40`: (SC)/(AV)/(HM)/(EK) all in `(n,k,q,m)` symbols; supplies a row-uniform safe anchor AND a row-uniform unsafe anchor. THE STRONGEST EXISTING COVERAGE |
| `critical/nodes/census_bounded_scales` (PROVED) | `statement.md:9`: "independent of n and k up to 2^40 ... The census is n-uniform". CAVEAT: its deciding-scale window `N' in [~120,~400]` must divide n, so it is EMPTY for s <= 6 and singleton for s = 7 — the "n-uniform" claim silently floors at s ~ 7-8 |
| `critical/nodes/staircase` (PROVED-cited) | `statement.md:9`: "for a row (n,k,q=q_line) ... B_tan(A) <= n-A+1", explicitly with a small-row regime note |
| `critical/nodes/petal_g1_layer_maps` (PROVED) | `proof.md:47`: "verified for all rate-1/2 rows s = 3..44"; `proof.md:38`: rates 1/4-1/16 for s = 13..44 |
| `critical/nodes/unsafe_crossing_family_instantiation` (TARGET) | `statement.md:8`: "For every admissible row" — correctly posed already; no edit owed |

### k-SPECIFIC (break, or become vacuous, below a stated s)

| node / object | pin | breaks below |
| --- | --- | --- |
| `rate_half_band_closure` | `statement.md:66` "n=2^41, k=2^40" | all s < 41 |
| `rate_half_band_crossing_location` | `statement.md:11` "n = 2^41, k = 2^40" | all s < 41 |
| `rate_half_cyclic_rotated_prefix_floor` | `statement.md:39,109,162`: sigma* = 8,592,912,738, declared family q_0 = 3*2^41+1 | not evaluable once k < sigma* ~ 2^33, i.e. s <= 34 |
| RH-LOW floor `B_mca(k+sigma_0) > B*` | `rate_half_band_closure/statement.md:90-92`, sigma_0 = 8,594,128,895 | needs k + sigma_0 <= n = 2k, i.e. k >= sigma_0: VACUOUS for s <= 34 |
| RH-BRACKET / RHL-LB `a in [k+2^34, 3n/4]` | `rate_half_band_crossing_location/statement.md:34`; `rate_half_list_adjacent_crossing/statement_sections/00-...:40` | at rate 1/2 the interval is EMPTY unless k >= 2^35: VACUOUS for s <= 35 |
| `dli_wcl_*` slot-emptiness family | `dli_wcl_slot_1_5_emptiness/statement.md:6` "(q<2^256, v_2(q-1)>=41)" | s = 41 pinned by the v_2 condition |
| `petal_g3_pricing_multiplicity`'s 719 | `statement.md:19` "floor(n^6/C(n+6,6))=719 at n=2^41..2^44" | SOFT: the true value is 87/224/.../718 at s=3..13 (exact check in the report). Since it is used as an upper allowance and the quantity is INCREASING in n, quoting 719 transports downward CONSERVATIVELY — this one bends, it does not break |

### The honest summary of the radius

The supporting-lemma layer is substantially k-uniform already; what is
k-specific is precisely the rate-1/2 crossing/floor layer — four nodes
plus two absolute-width constants. That is a narrow blast radius, and it
is narrow for a bad reason: the small-s rows are not covered by weaker
machinery, they are simply not addressed at all.
