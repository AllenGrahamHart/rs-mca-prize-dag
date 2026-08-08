# The t-petal overlap-cap lemma at general t

**DRAFT for coordinator replay. Round 24, 2026-08-08.**
Pilot: `notes/pilots_20260808/t_petal_lemma/`. No node, dag, or tool
file was touched. No status flip is claimed here.

## 0. The headline the coordinator needs first

**The lemma is TRUE at every `t`, and it is ALREADY PROVED IN THIS
REPO.** It is clause 2 of
`background/nodes/l1_fixed_support_defect_johnson_bound`
(status PROVED, `verify.py` passes), whose support pattern `X` has
**arbitrary size `h`** and is in no way restricted to two or three
petals:

> `background/nodes/l1_fixed_support_defect_johnson_bound/statement.md:36-40`
> ```
> 2. if `r_J>=0`, the defect sets of two distinct members satisfy
>
>    |D_1 intersect D_2|<=r_J;                               (JB3)
> ```
> with `background/.../statement.md:30`
> ```
> r_J=2d-h,       e=max(0,r_J+1).                            (JB2)
> ```

Put `h = t*ell` (t full petals). Then `r_J = 2d - t*ell = e - 1` with
`e = 2d+1-t*ell`, and `(JB3)` reads `|Z(F) cap Z(F')| <= e-1`
verbatim. The Johnson count that consumes it is the same node's
`(JB4)`, whose denominator `d^2 - N*r_J` is the sieve's
`J = d^2 - N(e-1)` exactly.

Therefore the board's standing claim at
`critical/nodes/l1_fpc5_large_source_payment/statement.md:31-34` —

> ```
> (i) NO mu-basis / overlap-cap theorem exists for t >= 4 (the
> three-petal theorems do not generalize as stated; even the Johnson
> functional J is undefined there)
> ```

is **false in both clauses**: the overlap-cap theorem exists at
arbitrary `h`, and `J` is exactly `(JB4)`'s denominator at arbitrary
`h`. The gap was bookkeeping, not mathematics. What follows is the
self-contained proof in the `t`-petal language, so the coordinator can
replay it without re-deriving the translation.

## 1. Statement

Let `K` be a field. Let `L_1,...,L_t in K[X]` be pairwise coprime
squarefree monic polynomials, `deg L_i = ell_i`, and put

```text
Lambda = L_1 L_2 ... L_t,      h = sum_i ell_i,
```

(the full-petal case is `ell_i = ell` for all `i`, `h = t*ell`). Let
`c_1,...,c_t in K` be scalars — **not required to be distinct**. Let
`C subset K` be a core disjoint from the zero set of `Lambda`. Define
the `t`-petal slice

```text
V = {(F,W) : deg F <= d, deg W <= d, L_i | (W - c_i F) for i=1..t}.
```

Call `(F,W) in V` a **member** if `F` is monic of degree exactly `d`,
`F` splits with `d` distinct roots `Z(F) subset C`, and
`gcd(F,W) = 1`. Put

```text
e = 2d + 1 - h.
```

**LEMMA (t-petal overlap cap).** For two distinct members `(F,W)`,
`(F',W')` of the SAME slice (same `L_i`, same `c_i`),

```text
|Z(F) cap Z(F')| <= e - 1.                                  (TPC)
```

In particular, if `e <= 0` the slice has at most one member.

## 2. Proof

Set the cross-determinant

```text
Delta = F W' - F' W.                                        (1)
```

**(a) `Delta != 0`.** Suppose `Delta = 0`, i.e. `F W' = F' W`. From
`gcd(F,W) = 1` and `F | F' W` we get `F | F'`. Both are monic of the
same degree `d`, hence `F = F'`. Cancelling the nonzero `F` in
`F W' = F W` gives `W' = W`, so the members coincide, contrary to
hypothesis. (This is the only step that uses monicity and equal
degree; it is the same step as
`background/nodes/l1_fixed_support_defect_johnson_bound/proof.md:9-12`.)

**(b) `Lambda | Delta`.** Fix `i`. Modulo `L_i` we have `W = c_i F`
and `W' = c_i F'`, hence

```text
Delta = F (c_i F') - F' (c_i F) = 0   (mod L_i).
```

So `L_i | Delta` for every `i`, and the `L_i` are pairwise coprime,
whence `Lambda | Delta`. **No step here mentions `t`.** Note also
that this needs no distinctness of the labels `c_i`.

**(c) `L_I | Delta`, `I = Z(F) cap Z(F')`.** `F` splits with simple
roots, so `L_I = prod_{x in I}(X-x)` divides `F` and divides `F'`;
hence `L_I` divides both terms of `(1)`.

**(d) Coprimality of the two divisors.** `I subset C` and `C` is
disjoint from the zero set of `Lambda`, so `gcd(Lambda, L_I) = 1`.
With (b) and (c),

```text
Lambda * L_I | Delta.                                       (2)
```

**(e) Degree ledger.** `deg Delta <= deg F + deg W' <= 2d`. With (a)
and (2),

```text
h + |I| <= 2d,      i.e.   |I| <= 2d - h = e - 1.           (3)
```

If `e <= 0` then `(3)` is unsatisfiable for `|I| >= 0`, so no two
distinct members exist. QED.

**Equivalent cofactor form.** By (b) one may write
`Delta = Lambda * E` with

```text
deg E <= 2d - h = e - 1,
```

and every point of `Z(F) cap Z(F')` is a root of `E` because
`Lambda` does not vanish on `C`. `(TPC)` is then just
"a nonzero polynomial of degree `<= e-1` has at most `e-1` roots".

## 3. Why the t=2 and t=3 mechanisms are special cases, not
##    ingredients

Registered checkpoint **(C6)** predicted the mu-basis is a detour.
It is.

- **t = 3.** `critical/nodes/pma_three_petal_mu_basis_reduction/statement.md:145`
  gives `(DET)`: `F_pW_q-F_qW_p=kappa L_1L_2L_3`. Writing
  `(F_j,W_j) = u_j(F_p,W_p) + v_j(F_q,W_q)` and expanding the
  determinant bilinearly,

  ```text
  F_1W_2 - F_2W_1 = (u_1v_2 - u_2v_1)(F_pW_q - F_qW_p)
                  = kappa * H_12 * Lambda.
  ```

  So the `H_12` of
  `critical/nodes/pma_three_petal_projective_johnson_bound/proof.md:25`
  is exactly `kappa^{-1}` times the cofactor `E` of section 2, and
  `deg H_12 <= r_u + r_v = e-1`
  (`.../proof.md:28-31`) is exactly the degree ledger `(3)`. The
  mu-basis supplies a *coordinate system* in which the cofactor is
  visible; section 2 gets the same polynomial without coordinates.
  **What the mu-basis is genuinely needed for is the DIMENSION
  formula `dim V = e+1` — which `(TPC)` never uses.**

- **t = 2.** `background/nodes/l1_fpc5_ratehalf_m4_t2_joint_support_distance/proof.md:6`
  forms `Delta = A_1A'_2 - A'_1A_2` in cofactor coordinates
  `A_i = (W - c_iF)/L_i`. Since `L_1A_1 - L_2A_2 = (c_2-c_1)F`
  (`critical/nodes/pma_two_full_petal_linear_slice_reduction/statement.md:24`),
  that `Delta` differs from `(F W' - F' W)/(L_1L_2)` by the nonzero
  scalar `(c_2-c_1)`; its degree bound `2s = 2d-2ell = e-1` is again
  `(3)`.

**The load-bearing observation.** The `t = 3` proof of `(PJ2)` derives
`deg H_12 <= e-1` from the mu-basis budget `(BUDGET)`
(`.../mu_basis_reduction/statement.md:127-131`), which is a
rank-2-syzygy fact. At `t >= 4` the syzygy module of `(L_1..L_t)` has
rank `t-1` and there is no two-generator budget — this is the real
reason the `t=3` write-up does not transcribe. Section 2 shows the
budget is not needed: the degree bound comes from
`deg Delta <= 2d` and `deg Lambda = h`, i.e. from **counting
degrees, not from the syzygy structure.**

## 4. Scope, and what is NOT claimed

`(TPC)` is a pairwise cap. Feeding it into Cauchy-Schwarz gives the
per-cell Johnson count `(JB4)` / `(PJ4)`:

```text
J = d^2 - N(e-1) > 0   ==>   |Z| <= N(d-e+1)/J,     N = |C|.
```

That is a **per-cell** count. It does not by itself pay the
large-source branch: the aggregate over support patterns, defect
degrees, labels and charts is the business of `(JB5)`
(`.../l1_fixed_support_defect_johnson_bound/statement.md:54-60`), which
is stated at a bounded petal-polarity cap `p <= P`. Nothing here
touches the sub-Johnson tail `N(e-1) >= d^2`, which is where the
408 residual rows live.

## 5. Hypothesis-transfer audit (registered checkpoint C8)

Every `(JB1)` hypothesis, checked against the FPC5 large-source
`t >= 4` cells:

| `(JB1)` hypothesis | holds at `t >= 4`? | witness |
|---|---|---|
| `F = L_D` monic, `deg F = d`, `D subset C` | YES | exact-defect locator, split on the source core |
| `deg W <= d` | YES | `A_d={(F,W): deg F=d monic, deg W<=d}` — `l1_bounded_mark_affine_split_pencil_compiler/statement.md:22` |
| `gcd(F,W)=1` | YES | exact-defect saturation; same hypothesis the `t=2,3` nodes use |
| `X` disjoint from `C` | YES | core/petal disjointness of the sunflower chart |
| both members share ONE labelling `alpha` | YES | `alpha` is the received word: "For a fixed intrinsic fiber partition **and received word**" — `l1_mixed_residual_intersection_pin/statement.md:201`; labels `c_i` are chart data, `l1_bounded_mark_affine_split_pencil_compiler/statement.md:10-11` |
| `h >= d + g` (list threshold) | NOT NEEDED for `(JB3)` | the proof of `(JB3)` (`proof.md:3-34`) never uses it; it is used only for `(JB7)` |
| labels distinct | NOT NEEDED | section 2(b) uses only that the two members share them |
| full petals | NOT NEEDED | `h = |X|` is arbitrary; partial petals give `h = t*ell - u`, matching `l1_mixed_residual_intersection_pin/statement.md:17-19` |

No hypothesis fails. The transfer is clean.

## 5b. A hypothesis that can be dropped: core/petal disjointness

Step 2(d) used "`C` disjoint from the zero set of `Lambda`". For
**primitive** members this is automatic and need not be assumed:

> If `x` is a root of `L_i` and `F(x) = 0`, then `L_i | (W - c_iF)`
> gives `W(x) = c_i F(x) = 0`, so `(X-x)` divides `gcd(F,W) = 1` — a
> contradiction. Hence `Z(F)` never meets the petals.

So `I = Z(F) cap Z(F')` is disjoint from `Z(Lambda)` for free, and
`gcd(Lambda, L_I) = 1` follows from primitivity alone. This is a
(small) strengthening of `(JB3)`, which assumes `X` disjoint from
`C` in its hypotheses. Machine-checked: 5671 primitive members over
360 deliberately overlapping configurations, **zero** with a petal
root (`tpetal_cj3_probe.py`, PROBE B).

## 5c. THE SLICE-DIMENSION THEOREM AT GENERAL t (new)

The overlap cap is a pairwise fact. Round-23b's red-3 split needed a
second, different thing — a linear flat **of known dimension** —
and recorded its absence:

> `notes/pilots_20260807/mf_wall_adversary/red3_split.py:5-11`
> ```
> The (MF) statement can only be INSTANTIATED on a cell whose
> contributors are proved to inject into a linear flat.  That
> injection exists at t = 2 ... and at t = 3 ...  For t >= 4 NO
> such reduction is proved
> ```

The same cross-determinant supplies it.

**THEOREM.** If `V` contains a saturated pair `(F,W)` — `F` monic of
degree exactly `d`, `gcd(F,W) = 1` — then `dim_K V = e + 1`.

*Proof.* `>=`: the `h` evaluation conditions on `2(d+1)` unknowns
give `dim V >= 2d+2-h = e+1`.
`<=`: fix the saturated `(F,W)` and define the **linear** map

```text
E : V -> K[X],      E(G,B) = (F B - G W)/Lambda.
```

It is well defined: both pairs satisfy the same congruences, so
`L_i | (FB - GW)` for every `i` exactly as in 2(b), hence
`Lambda | (FB - GW)`. Its image lands in degree `<= 2d - h = e-1`,
an `e`-dimensional space, by 2(e). Its kernel is
`{(G,B) : FB = GW}`; from `gcd(F,W)=1` we get `F | G`, and
`deg G <= d = deg F` forces `G = lambda F`, then `B = lambda W`. So
the kernel is the line `K(F,W)`, of dimension 1. Therefore
`dim V <= 1 + e`. QED

This is the general-`t` replacement for `(TF3)` at `t=2`
(`critical/nodes/pma_two_full_petal_linear_slice_reduction/statement.md:31`,
`dim V_s = 2s+2 = e+1`) and for `(HF)`+`(BAL)` at `t=3`
(`critical/nodes/pma_three_petal_mu_basis_reduction/statement.md:82,107`,
`dim V_s = 2s-ell+2 = e+1` under `(SAT)`). It needs neither the
syzygy module nor its rank, which is why it survives `t >= 4` where
the mu-basis does not.

Note the saturation hypothesis is load-bearing and matches `(BAL)`'s
at `t=3`: without a saturated pair `dim V` may exceed `e+1`, and the
theorem claims nothing there.

Machine-checked by `notes/pilots_20260808/t_petal_lemma/tpetal_dim.py`
at `t = 4,5,6,7,8`, `e = 1..5`: 215 cells, 155 with a saturated pair;
`dim V >= e+1` in all 215; `dim V = e+1` in all 155 saturated cells;
the image bound (`deg E <= e-1`) and the kernel rank
(`rank E = dim V - 1`) hold in all 155.

## 6. Machine evidence

- `background/nodes/l1_fixed_support_defect_johnson_bound/verify.py`
  PASSES (replayed 2026-08-08 under `tools/ramguard local`):
  `L1_FIXED_SUPPORT_DEFECT_JOHNSON_PASS sharp=3 boundary=6
  local_not_global=24 set_cases=50 set_rows=991 positive=540112
  tail=55552`. Its `check_cross_divisibility`
  (`verify.py:45-58`) asserts
  `support_locator * locator(intersection) | (w1*f2 - w2*f1)` and
  `len(d_1 & d_2) <= r_j` at arbitrary support size — i.e. it already
  machine-checks `(2)` and `(3)` above.
- `notes/pilots_20260808/t_petal_lemma/tpetal_refute.py` — this
  pilot's independent adversarial search at `t = 4, 5, 6`; see the
  pilot's final report for coverage, the tight cells, and the
  power-control arms.
