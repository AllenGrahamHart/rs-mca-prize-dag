# Proof

Notation as in `statement.md`.

**PROVENANCE OF THE ARGUMENT — read first.** There is **no `REPORT.md`**
for this pilot and **no continuous prose proof of T0 anywhere on disk**.
The pieces that exist are:

| piece | where | form |
|---|---|---|
| T0's proof ROUTE | `f9/PREREG.md:143-154` | pre-registered sketch |
| LEMMA 5 | `f9/PREREG.md:196-201` | **full bracketed proof** |
| LEMMA 2 | `f9/PREREG.md:88-89` | one-line sketch |
| LEMMA 3 | `f9/PREREG.md:99-100` | one-line sketch |
| LEMMA 4 | — | **no written proof**; only the machine criterion |
| case (b) | `f9/FABLE_AUDIT.md:17-18` | **no written proof**; one clause |
| the closing chain | `f9/FABLE_AUDIT.md:18-20` | one clause, hand-verified |

The lemma numbering exists only as check-label strings in
`f9/verify.py:272-280`. Below, each step is marked **[T]** transplanted,
**[S]** expanded from a one-line sketch, or **[R]** reconstructed with no
source text. Every **[R]** is a place the coordinator must line-audit.

---

## 0. The normalisation the whole proof runs in [T]

`f9/PREREG.md:71-81`, consuming `v5_occupancy` LEMMA 1
(`v5_occupancy/REPORT.md:47-56`, proved there). At an ordered pair
`(i,j)` — valid for **any** pair, since the blocks are disjoint — there
are `w` on `A_i u A_j`, `w != 0`, and `g_a in F[X]_{<e}` with

```text
(POINT)   w B_a = g'_a        on A_i ,
          w B_a = lambda_a g'_a  on A_j ,
          g'_a := g_a/(z_a - z_j),  lambda_a := (z_a - z_j)/(z_a - z_i).
```

`Z := {x in A_i u A_j : w(x) = 0}`, `Z_i := Z ^ A_i`, `Z_j := Z ^ A_j`,
`d_{ij} := dim span{g'_a}`. The `lambda_a` are **distinct** (a Möbius
image of distinct slopes) and every `g'_a != 0` (else `w = 0`).
Write `B_i^Z := prod_{x in A_i \ Z_i}(X - x)` and
`zeta_i := prod_{x in Z_i}(X - x)`, so `B_i = B_i^Z zeta_i`.

## 1. Q0 — why T0 says "`>= 3` blocks" [T]

`unified_pencil_bound/PREREG.md:31-39`. Given two disjoint equal-size
blocks `B_1, B_2`, take `w` monic with root set `B_1` and `w'` monic with
root set `B_2`; then `B_1` and `B_2` are the fibres at `c = 0` and
`c = inf` of the pencil `<w, w'>`. So **every** disjoint pair is
pencil-structured, and the notion has content only from size `3`. **QED
(Q0)** — this is what makes T0's "`>= 3` blocks each" the right
quantifier rather than a convenience.

## 2. LEMMA 2 (r-formula) [S]

Source sketch: *"the vectors `(g'_a, lambda_a g'_a)` in `G+G`; if two
`g'` are independent any third non-zero `g'` produces a third independent
vector."* Expanded:

Consider the map `a -> (g'_a, lambda_a g'_a) in F[X]_{<e}^2`. Suppose
`d_{ij} = dim span{g'_a} = 1`, so all `g'_a = c_a g` for a common `g` and
scalars `c_a != 0`. Then the vectors are `c_a (g, lambda_a g)`, which lie
in the 2-dimensional space `span{(g,0), (0,g)}`; since the `lambda_a` are
distinct, any two of them are independent, so the span is exactly `2`.

Conversely if `d_{ij} >= 2`, pick `g'_1, g'_2` independent. Then
`(g'_1, lambda_1 g'_1)` and `(g'_2, lambda_2 g'_2)` are independent, and
any third `g'_3 != 0` gives a vector outside their span: if
`(g'_3, lambda_3 g'_3) = alpha(g'_1, lambda_1 g'_1) + beta(g'_2, lambda_2 g'_2)`
then `g'_3 = alpha g'_1 + beta g'_2` and
`lambda_3 g'_3 = alpha lambda_1 g'_1 + beta lambda_2 g'_2`; substituting
and using independence gives `alpha(lambda_3 - lambda_1) = 0` and
`beta(lambda_3 - lambda_2) = 0`, so `alpha = beta = 0` (distinct
`lambda`), contradicting `g'_3 != 0`. So the span is `>= 3`. Needing a
third block off the pair is exactly `V >= 5`. **QED (2)**

## 3. LEMMA 3 (pencil normal form) [S]

Source sketch: *"the admissibility conditions are affine in `lambda`; two
roots kill both coefficients."* Expanded: fix a `g`-direction shared by
`>= 2` blocks off the pair and set

```text
X_lambda := { f in F[X]_{<=t} : w f = c g on A_i,  w f = c lambda g on A_j }.
```

The defining conditions are affine in `lambda`, so `X_lambda != 0` for a
set of `lambda` cut out by the vanishing of two coefficient forms; two
distinct admissible `lambda` force both forms to vanish identically,
hence `X_lambda != 0` for **every** `lambda`. Solving the two interpolation
conditions gives the explicit basis

```text
f_0 = B_j^Z s_0  (deg s_0 <= |Z_j|),      f_1 = B_i^Z s_1  (deg s_1 <= |Z_i|),
```

and every block with that direction is a fibre of `P := <f_0, f_1>`.
**QED (3)** — *machine reconstruction of `(f_0,f_1)` at
`f9/verify.py:151-169`; note `:165-166` contains a dead duplicate `f0`
assignment with the opposite sign convention, harmless because the second
line wins, but do not quote line 165 as the formula.*

## 4. LEMMA 4 (rogue criterion) [R]

**No source proof exists**; only the machine criterion
`f9/verify.py:279-280`. Reconstruction: `B_j = B_j^Z zeta_j`, and
`B_j in <f_0, f_1> = <B_j^Z s_0, B_i^Z s_1>` means
`B_j^Z zeta_j = c_0 B_j^Z s_0 + c_1 B_i^Z s_1`. Since
`gcd(B_i^Z, B_j^Z) = 1` (the blocks are disjoint) and `B_j^Z` divides the
left side and the first right-hand term, `B_j^Z | c_1 B_i^Z s_1`, forcing
`B_j^Z | c_1 s_1`; but `deg s_1 <= |Z_i| < deg B_j^Z` unless `c_1 = 0`.
With `c_1 = 0`: `zeta_j = c_0 s_0`, i.e. **`s_0 ~ zeta_j`**. Conversely
`s_0 ~ zeta_j` gives `B_j = B_j^Z zeta_j ~ f_0 in P`. **QED (4),
reconstructed**

*This GENERALISES the pre-registered Q4 criterion "`Z_j = empty`": when
`Z_j = empty`, `zeta_j = 1` and `deg s_0 <= 0`, so `s_0 ~ zeta_j`
automatically. Q4 is the special case; LEMMA 4 also covers `Z_j != empty`.*

## 5. LEMMA 5 (intersection lemma) [T] — the one full transplant

Verbatim from `f9/PREREG.md:196-201`:

> `P' ^ <B_i,B_j>` is 0 unless `s_0 ~ zeta_j` (then it is `<B_j>`) or
> `s_1 ~ zeta_i` (then it is `<B_i>`); in every case it contains NO third
> block. *[Proof: `h = c_0 f_0 + c_1 f_1 = alpha B_i + beta B_j` gives
> `B_j^Z (c_0 s_0 - beta zeta_j) = B_i^Z (alpha zeta_i - c_1 s_1)`, and
> `gcd(B_i^Z, B_j^Z) = 1` with `deg <= |Z_j| < t - |Z_i| = deg B_i^Z`
> forces `c_0 s_0 = beta zeta_j` and `c_1 s_1 = alpha zeta_i`.]*

**The degree hypothesis is `|Z_i| + |Z_j| < t`, i.e. `|Z| < t`**, which is
**automatic** on the admissible window: `la_pencil_rigidity` THEOREM 5
gives `|Z| <= e-1`, and `e <= t-1`, so `|Z| <= t-2 < t`. **LEMMA 5 is
therefore unconditional here** — the residual does NOT attach to it.

**THE IN-RUN CORRECTION, and the hypothesis it forces into T0
(`f9/PREREG.md:185-195`).** Check E2 as first written asserted
"`P' ^ P` meets only in `0`" and **FAILED on 12 of 18 fixtures**. The
**check** was wrong, not the lemma: that conclusion holds only under the
hypothesis `B_i, B_j not in P'`. The fixtures are 1-rogue systems where
`B_2` *is* a fibre of `P'` (`Z_2 = empty => s_0 ~ zeta_2`), so a
1-dimensional intersection `<B_2>` is the **predicted** behaviour.
**Consequence, load-bearing: T0's proof must choose the normalising pair
inside `F \ F'`** — two blocks of the first family that are not in the
second. That hypothesis is stated explicitly in step 6.

## 6. T0 [R for case (b); T for the route and case (a)]

Suppose, for contradiction, that the blocks are covered by two **distinct**
pencils `P` and `P'`, each carrying `>= 3` blocks. By the correction in
step 5, **choose the normalising pair `(i,j)` with `B_i, B_j in P \ P'`**
(possible: `P` carries `>= 3` blocks and shares at most... — see the note
below). Put `P = <f_0, f_1>` in LEMMA 3's normal form.

`P'` carries `>= 3` blocks, so it carries a block `B` not in `{B_i,B_j}`.

- **Case (a) — the unconditional kill [T].** By **LEMMA 5**,
  `P' ^ <B_i,B_j>` contains **no third block**. So `B` is not in
  `<B_i,B_j> = P`. But `P` was assumed to cover the blocks jointly with
  `P'`; the sub-case where `B in P` is closed outright. **Unconditional.**
- **Case (b) — the cross-multiplication [R; hand-verified as a clause
  only].** Otherwise, writing `B = alpha B_i + beta B_j` and pushing it
  through `(POINT)` gives

  ```text
  alpha * zeta_i * s_0  =  c * lambda * zeta_j * s_1 .
  ```

  Since `Z_i <= A_i` and `Z_j <= A_j` are disjoint, `gcd(zeta_i, zeta_j) = 1`,
  so `zeta_i | s_1`. **If `deg s_1 <= |Z_i| = deg zeta_i`** this forces
  `s_1 ~ zeta_i`, i.e. (LEMMA 4 at `i`) `B_i in P'` — so the two pencils
  share `B_i`, and with a second shared block P-SHARE (step 7) makes them
  equal, contradicting distinctness. Otherwise `alpha = 0`, i.e. `B` is
  not a new block.

  **THE RESIDUAL LIVES EXACTLY HERE.** The degree hypothesis needed is
  `t >= e + max|Z|`. It is **unconditional for `e <= 3` and
  `t >= 2e-2`**; on the complementary band **`t <= 2e-3` it is NOT
  established**. See `statement.md` — and note the band is EMPTY for
  `t <= 4`, with smallest shape `(t,e) = (5,4)`.

**Closing chain, `T0 => M <= 1 => C = 1/2` [T, hand-verified].**
`f9/FABLE_AUDIT.md:18-20`: *"a lone rogue cannot carry a second family:
any 3-set through it has 2 P-blocks spanning P"* — i.e. once at most one
pencil carries `>= 3` blocks, any candidate second family of size `>= 3`
must contain `>= 2` blocks of `P`, and two distinct blocks of `P` span
`P`, so the second family **is** `P`. Hence `M <= 1`. Converting `M <= 1`
into `C = 1/2` then needs the **per-pencil point count**, which is
`unified_pencil_bound` PREREG Q3 and is **NOT part of this node** (see
`statement.md`, NOT claimed). **QED (T0), modulo the case-(b) residual**

## 7. P-SHARE [S for the fibre form; R for the slope form]

Source sketch (`f9/PREREG.md:48-52`): two shared slopes `z, z'` give
`A_z ^ A_z' = A_0 = A_0'` (cores equal, since blocks inside a family are
disjoint); then the two shared blocks are fibres of both pencils, and **a
degree-`s` polynomial is determined up to scalar by its `s` distinct
roots**, so both pencils equal the span of those two fibres — i.e. the
pencils coincide. Contrapositive: distinct pencils share `<= 1`.

Expanded: let `P = <w, w'>` and `P' = <v, v'>` be 2-dimensional, and
suppose they share two distinct fibres `F_1 != F_2`, each of size `s`.
A fibre `F` of `P` is the root set of some `p in P` with `deg p = s`;
since `p` is determined up to scalar by its `s` distinct roots, the
member of `P` with root set `F_1` and the member of `P'` with root set
`F_1` are **the same polynomial up to scalar**. Same for `F_2`. Two
distinct members of a 2-dimensional space span it, so
`P = <p_{F_1}, p_{F_2}> = P'`. **QED (P-SHARE)**

**Independent corroboration from the sibling pilot:** `unified_pencil_bound`'s
own exhaustive enumeration reports `worst_shared: 1` at all three
`(q,s)` it swept (`131`, `181`, `1055` pencils) — i.e. its registered
`<= 2` bound (Q5) was **never attained**, which is exactly what P-SHARE
explains.

## Honest scope

- **LEMMAS 2, 3, 4 were never hand-verified** — machine replay only. Of
  the chain above, only **LEMMA 5**, **the case-(b) cross-multiplication
  clause**, and **the closing chain** carry a coordinator hand-check.
- **Case (b) has no written source proof.** Step 6's case (b) is
  reconstructed from a single clause in the audit. It is the step the
  residual attaches to, and it is the single most important line-audit
  target in this node.
- **T0 is not the anchor.** `C = 1/2` needs `{UPB e=1 + T0 + P-SHARE}`;
  this node has the last two. A separate UPB node is owed.
- **P-DISJ is assumed where the block-system model is assumed**, and is
  not closed. The whole argument runs inside `B(V,t,t_0,k)`, i.e. on
  disjoint complements outside a common core.
- **`Delta` bookkeeping (F3.f).** `f9/verify.py:985` computes
  `Delta = 2e - t - 1`, which equals `la`'s registered
  `Delta = (V-2)(e+1-t) + 2t - V - e + 1` **only at `V = 5`**. At `V = 6`,
  `(t,e) = (3,2)`, la's formula gives `-1` while f9 reports `0`. Both are
  `<= 0`, so FB fires either way and no verdict changes — but quote
  `(V,t,e,Delta) = (5,3,2,0)` as the exact entry.
