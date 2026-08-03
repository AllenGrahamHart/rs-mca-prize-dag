# pb_block_dichotomy

- **status:** PROVED
- **closure:** proof
- **scope:** disjoint-block families with a FIXED core, in the degree-`A`
  pencil model. Core-varying families, non-block families, and non-coset
  blocks are **out of scope** and are explicitly recorded as open.
  Claims 1-3 are elementary and scale-free; Claim 4 (the collinearity
  necessary condition) is **reconstructed** — see the flags below and
  `../../AUDIT_CHECKLIST.md` F4.a-F4.e.
- **provenance:** P-B (H4) hunt pilot,
  `notes/pilots_20260802/pb_h4_hunt/REPORT.md:15` (the claim, "*Block
  dichotomy* (**proved + verified**)"), `expE.py:1-14` (the statement in
  code, deferring the proof "to the report"), `EXPE.json` (the residue
  measurement), `FABLE_AUDIT.md:12-14, 19-23` (coordinator verdict
  ACCEPTED; "hand-verified: ... the coset power-sum vanishing behind the
  dichotomy"), self-limitation at `REPORT.md:60-63`. Consumed by the P-B
  TARGET's 2026-08-02 scope addendum
  (`critical/nodes/xr_lowcore_spread_heart/notes/OFFICIAL_SCALE_REFRAME_20260802.md:42-53`,
  `dag.json` `xr_lowcore_spread_heart`) as (SF-SELFCOLLISION).
- **HONESTY FLAG (read before citing).** The record asserts this result
  as "proved + verified" but contains **no written derivation anywhere**
  (grep over `background/`, `critical/`, `dag.json`, and the pilot tree
  returns only the two assertion sites above). What is written down here
  is: Claims 1-3 proved from scratch (each is a few lines, and the coset
  computation is the part the coordinator hand-verified); Claim 4
  reconstructed **in corrected coordinates** — the source states it in
  POWER-SUM coordinates while its own code computes ELEMENTARY-SYMMETRIC
  ones, and the two are not affinely equivalent. See F4.a.

## Setting

`RS_K` on `D = mu_n <= F_q^*` (`n` a 2-power, `q` prime — the official
shape); `A = K + h`. **Pencil model** (`pb_h4_hunt/core.py:16-32`):
`u = U|_D`, `v = V|_D` with `U` monic of degree `A`, `deg V < A`. Then
`S` (`|S| = A`) is an exact-`A` witness of the pair at slope `z` iff

```text
(STAR)   e_j(S) = alpha_j + z beta_j ,   j = 1..h,
         alpha_j = (-1)^j U_{A-j},  beta_j = (-1)^j V_{A-j},
```

i.e. the **moment vector** `E(S) := (e_1(S), ..., e_h(S))` lies on the
affine line `L = {alpha + z beta}` of `AG(h,q)`. Only the top `h`
coefficients matter; everything of degree `< K` is invisible gauge. The
**design space of degree-`A` pencils IS the space of affine lines of
`AG(h,q)`**, and a pencil's planted family is `E^{-1}(L)`.

**A live slope direction** means `beta != 0` (the gauge-invariant form of
the strip gate, `pb_h4_hunt/REPORT.md:23`); equivalently the family's
moment vectors are not all equal, so at least two distinct slopes occur.

**Block family.** Fix a core `G` and a pool of `b` pairwise-disjoint
blocks `B_1..B_b`, all of common size `m`, all disjoint from `G`. For an
`a`-subset `J` of the pool put

```text
S_J = G u (union_{j in J} B_j),      |S_J| = |G| + a m = A.
```

**Truncated reversed polynomial.** For any set `S`,
`R_S(Y) := prod_{x in S} (1 - x Y)  =  sum_j (-1)^j e_j(S) Y^j`, read in
`R := F_q[Y]/(Y^{h+1})`. For **disjoint** `S, T`:
`R_{S u T} = R_S R_T` in `R`. Every `R_S` has constant term `1`, hence is
a unit of `R`; and `E(S)` is exactly the coefficient data of `R_S` in
degrees `1..h`, up to the signs `(-1)^j`.

## Statement (all PROVED)

1. **CLAIM 1 (spread threshold).** For `a >= 1` and `b >= a+1`:

   ```text
   the family {S_J} is SPREAD (all pairwise cores <= K-1)  <=>  m >= h+1.
   ```

   More precisely `|S_J ^ S_{J'}| = |G| + m |J ^ J'|`, whose maximum over
   distinct `J, J'` is `|G| + (a-1) m = A - m`; and
   `A - m <= K - 1  <=>  m >= h+1`.
2. **CLAIM 2 (SF-SELFCOLLISION, derived — not assumed).** If `m <= h`
   then every pair of members meeting in `a-1` blocks has core
   `A - m >= K`. Every planted member therefore has a partner at core
   `>= K` and lies in `Gamma_hi`: **the family self-collides.** This
   derives the range `m <= h` in which (SF-SELFCOLLISION) operates,
   rather than assuming it. (Together with Claim 3 the operative window
   is `m <= h < 2m`.)
3. **CLAIM 3 (coset blocks, and THE DICHOTOMY).** Let the blocks be
   cosets of `mu_m <= mu_n` (`m | n`), `B_j = g_j mu_m`. Then
   `prod_{x in B_j}(X - x) = X^m - g_j^m`, so in `R`

   ```text
   R_{B_j}(Y) = 1 - g_j^m Y^m .
   ```

   Hence
   - **if `m > h`:** `R_{B_j} = 1` in `R`, so `E(B_j) = 0` and
     `E(S_J)` is **the same point `P` for every `J`**. The family
     occupies a single point of `AG(h,q)`. Hence **the whole family is
     witnessed at ONE slope**: if `beta != 0` then `P = alpha + z beta`
     for exactly one `z`, and every member is a witness at that same `z`;
     if `beta = 0` the pencil is slope-free. Either way the family
     exhibits **no live slope direction** — it is a strip, not a
     multi-slope spread family.
   - **if `m <= h < 2m`:** `R_{S_J} = R_G * prod_{j in J}(1 - g_j^m Y^m)
     = R_G - (sum_{j in J} g_j^m) Y^m` in `R` (all cross terms vanish,
     `2m > h`), so the moment vectors DO move — along the single
     direction `e_m` — and a live slope direction exists; but by Claim 1
     the family is **not spread** (`m <= h`).

   **THE DICHOTOMY: for every coset-block geometry, spreadness and a
   live slope direction are INCOMPATIBLE.**
4. **CLAIM 4 (collinearity is necessary — RECONSTRUCTED, in
   ELEMENTARY-SYMMETRIC coordinates).** Suppose every `S_J`
   (`J` over the `a`-subsets of the pool) is a witness of one pencil,
   i.e. `E(S_J) in L` for all `J`. Then the **block moment vectors
   `E(B_1), ..., E(B_b)` lie on one affine line of `AG(h,q)`** — for
   `a = 1` with no further hypothesis, and for `a >= 2` provided
   `b >= a + 2`.

   **COORDINATE FLAG (F4.b).** The source states this in POWER-SUM
   coordinates: "the block moment vectors `beta_j = (p_1(B_j),...,p_h(B_j))`
   satisfy `beta_j = beta_1 + c_j d`" (`expE.py:7-8`). Its own code
   computes `core.moment_vector` = the ELEMENTARY-SYMMETRIC vector
   `(e_1,...,e_h)` (`expE.py:49-50`, `core.py:144-150`). Newton's
   identities relate the two by a **non-affine** polynomial change of
   variables, so "collinear in `p`" and "collinear in `e`" are different
   conditions in general (the verifier exhibits the failure). The
   statement above — the one the code tests and the one the proof gives
   — is in `e`-coordinates. **For coset blocks the two readings coincide**
   (both give the direction `e_m`), so Claim 3 and the dichotomy are
   unaffected either way.

   **HYPOTHESIS FLAG (F4.c).** The source's hypothesis is `b >= a+1`
   (`expE.py:5`). At `b = a+1` only two blocks vary and collinearity is
   vacuous; the argument needs `b >= a+2` for `a >= 2` (and nothing for
   `a = 1`). Stated correctly above.

## Explicitly NOT claimed (context)

- **The non-coset residue is OPEN.** "NON-coset blocks of size
  `m >= h+1` with collinear moment vectors" (`expE.py:12-14`) is the
  residue the dichotomy leaves. At toy scale it is **measured FEASIBLE**
  at 4 of the pilot's 5 shapes (`EXPE.json`: richest line carries 66
  blocks, 6 of them disjoint, family `C(6,2) = 15`), and it is closed at
  official scale only by a FIRST-MOMENT count which the pilot itself
  says "is **not a theorem** (split-fibre is the standing proof that
  first moments can be wrong by `2^170` on an exceptional locus)"
  (`REPORT.md:61`). **Nothing here closes it.**
- **Core-varying and non-block families are out of scope**
  (`REPORT.md:60`); they are covered in the record only by the toy
  exhaustive search and by `pb_design_ceiling`.
- **`Gamma_lo = 0` for split-fibre is NOT an identity consequence — the
  SELECTOR CATCH.** `(SF-SELFCOLLISION)`'s max core `A-m >= K` is
  attained ONLY by adjacent label sets, whose partners live at OTHER
  slopes. `Gamma_lo = 0` therefore additionally requires the SELECTOR to
  be support-keyed: measured, support-lex first-match gives
  `Gamma_lo = 0` at 18/18 points across `nu in [0.05, 30]`, while a
  UNIFORM selector leaves `~q e^{-nu}` survivors — at official RowC 1/4
  (`nu = 3.0`) that is `~2^187 >> 8n^3` (`REPORT.md:43`,
  `FABLE_AUDIT.md:26-36`). **The K1 closure is a JOINT
  identity-plus-support-keyed-selector statement and re-couples to the
  ratified PP4.0 compression-order class.** This node proves the
  identity half only.
- **No P-B bound, and no discharge of (H4)** (`REPORT.md:63`).
- **No claim that the design space is exhausted** — the pencil model is
  a `2h`-dimensional slice of the `2(n-K)`-dimensional word model
  (`REPORT.md:57`).
- **The first-moment infeasibility margins** (262-957 bits at RowC,
  `~10^12` bits at prize, `OFFICIAL.json` `spread_blocks`) are RECORDED
  context, not claims: they are first-moment counts, per `REPORT.md:61`.

## Falsifier

A coset-block family that is simultaneously spread and carries two
distinct slopes; or a block family with `|S_J ^ S_{J'}| != |G| + m|J^J'|`;
or a coset `g mu_m` with `prod_{x}(X-x) != X^m - g^m`; or a witness
family `{S_J}` of a single pencil (`a = 1`, or `a >= 2` with `b >= a+2`)
whose block moment vectors `E(B_j)` are NOT collinear.

## Verifier

`verify.py` in this node (profile: `tiny`; pure python integers,
deterministic, no third-party imports, no reads outside this directory).
Checks: (A) the core formula `|S_J ^ S_{J'}| = |G| + m|J ^ J'|` and
Claim 1's threshold, over coset-block families at several shapes;
(B) Claim 2 — at `m <= h` every member has a partner at core `>= K`;
(C) the coset identity `prod(X - x) = X^m - g^m`, the `e`-vector support,
and the power-sum form `p_t = m g^t [m | t]`; (D) Claim 3 both branches —
at `m > h` all `E(S_J)` coincide (no direction), at `m <= h < 2m` they
move along `e_m` and the family is not spread; (E) the ring identity
`R_{S u T} = R_S R_T` in `F_q[Y]/(Y^{h+1})` and the linearity of
multiplication by a fixed unit — the mechanism of Claim 4; (F) Claim 4 at
`a = 1` and at `a = 2, b >= a+2`, on planted families; (G) the COORDINATE
FLAG — an explicit `p`-collinear triple whose Newton images are NOT
`e`-collinear, and the coset case where the two agree; (H) the OPEN
residue, replayed at the pilot's `n=20, q=101, h=2, m=3` shape and
LABELLED MEASURED-OPEN (not a claim).

## Addendum (2026-08-03, cross-lane cash-out): the selector and the L-B dichotomy

Machine-decided (equivariance test 11/11 vs 1/11): the SELECTOR CATCH
and the L-B over-agreement dichotomy are DIFFERENT species (liveness
vs attribution) but COMPLEMENTARY on the split-fibre locus — keyed by
codeword, the selector's nontrivial classes are exactly the
over-agreeing ones, and after an L-B-type prune every surviving class
is a singleton: the selector becomes VACUOUS. Proving over-agreement
forcing on the split-fibre locus would DE-COUPLE the K1 closure from
PP4.0's compression order. See notes/pilots_20260803/crosslane_cashout/.
