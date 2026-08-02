# FM0 — Selector manifest for the P-B first-match pilot

> **PILOT ORDER, NOT RATIFIED.** Everything in §4 is a *pilot* convention
> chosen by this experiment because the repository does not pin one. It is
> pending planner ratification (this is exactly the "PP4.0 semantic freeze"
> that `BRIEF4_DOSSIER_AUDIT.md` lists as adopted-but-unwritten). No DAG
> change is proposed or implied by this file.

Scope: `critical/nodes/xr_lowcore_spread_heart` (P-B), read together with
`critical/nodes/xr_tangent_support_mismatch_bridge` (the PROVED bridge that
*defines* the selector's scope) and the `xr_smallcore_spread_count` consumer.

---

## 1. What the repository actually says

### 1.1 The selector is named, never defined

Sources, verbatim:

| source | text |
|---|---|
| `xr_lowcore_spread_heart/statement.md` L6-7 | "fix the **support-wise first-match post-strip selector**" |
| `xr_tangent_support_mismatch_bridge/statement.md` L38-41 | "select one exact-`A` witness/codeword by a **fixed first-match order**" |
| `xr_tangent_support_mismatch_bridge/statement.md` L13-14 | "select one exact-`A` support-wise bad ray **per live slope**" |
| `xr_tangent_mismatch_full_external_zero_canonicalization/statement.md` L23 | "After fixing **any deterministic first-match order** on witness/codeword pairs" |
| same node, `claim_contract.md` L5 | "**Selection:** any fixed deterministic first-match order, **once per slope**." |
| `notes/pro_briefs_20260801/BRIEF_4_...md` L63-64 | "The selector (support-wise first-match post-strip) is **normative**; results for other selectors need a **transport lemma**." |
| `BRIEF4_ADVERSARIAL_AUDIT_SUMMARY.md` L57-59 | "For `W_z` = all exact-`A` witnesses at slope `z` and the normative `(p_z,S_z) = min_prec W_z` ..." |

**Finding FM0-1 (the central ambiguity).** The concrete order `prec` is
**nowhere defined in this repository.** Every occurrence is either "a fixed
order", "any deterministic order", or `min_prec` with `prec` undefined. The
`PP4.0 semantic freeze` that would fix it was *adopted* in
`BRIEF4_DOSSIER_AUDIT.md` §"Adopted posture" item 1 ("cheap, immediate, ours
to write") and **has not been written**. Grep evidence: no file in the tree
contains a definition of the P-B/bridge witness order; the ~25 hits for
"lexicographically first" all belong to *other* lanes (flat-nullity circuits,
rank-two fundamental circuits, Maxwell trade space) and order different
objects (bases, circuits, orientations), not exact-`A` agreement supports.

**Finding FM0-2 (the ambiguity is load-bearing, by the audit's own words).**
`BRIEF4_ADVERSARIAL_AUDIT_SUMMARY.md` L52-54: "An order-independent producer
theorem is FALSE (an adversarial witness order selects the whole family), so
any P-B proof must exploit **the exact canonical order's algebra**." So the
undefined object is precisely the one the surviving route must exploit. This
pilot therefore reports **every measurement under four different orders**, and
treats order-sensitivity as a primary output rather than a nuisance.

### 1.2 What *is* pinned

These are unambiguous in the tree and are used as-is:

1. **Objects ordered.** `(p_z, S_z)`: an exact-`A` witness polynomial
   `p_z` of degree `< K` together with its agreement support
   `S_z = D \ supp(u + z v - p_z)`, `|S_z| = A`.
   (`bridge/statement.md` L38-46.)
2. **One selection per slope**, and only for **live** slopes (slopes carrying
   at least one exact-`A` witness). (`canonicalization/claim_contract.md` L5.)
3. **Exact-`A`, not `>= A`.** Both the bridge and the heart say "exact-`A`".
4. **Post-strip** = after the T0-T4 strips of
   `critical/nodes/stratification_partition_thm/proof.md` §"the eight case
   predicates": T0 containment, T1 degenerate (`u=0`/`v=0`/`v=λu`),
   T2 tangent overlap (some slope has agreement `A_0 > A`), T3 quotient
   periodicity (the pencil folds rate-preservingly through `x -> x^M`,
   `M | gcd(n,k)`, `M > 1`), T4 direction rank. Dihedral-symmetric and
   extension-type slopes are **not** stripped — `heart/statement.md` L16-17
   says they "remain inside the predicate allocation".
5. **Support-wise** = the low/high split is on **agreement supports**:
   `Gamma_lo` = live slopes whose selected support meets every *other*
   selected support in at most `K-1` coordinates (`heart/statement.md`
   L7-9). Note this is a property of the *whole selected family*, not of a
   slope in isolation.
6. **Scope hypothesis.** Globally generic branch: no codeword pair
   `(c_0,c_1)` jointly explains `(u,v)` on an `A`-support
   (`bridge/statement.md` L11-13).

### 1.3 A structural fact that constrains any order (proved here, used below)

**Lemma (disjoint witness sets).** In the split-fibre pencil below,
`deg V = A - m >= K`. If `S in W_z` and `S in W_w` with `z != w`, then
`f_z - p_z = prod_{x in S}(X-x) = f_w - p_w`, so `(z-w) V = p_z - p_w` has
degree `< K` — contradicting `deg V >= K`. Hence
**`W_z ∩ W_w = ∅` for `z != w`**, for *every* order.

Consequence for FM2: **no selector can compress the family by making two
slopes share a support.** "Compression" can only mean (i) higher pairwise
intersections (pushing slopes out of `Gamma_lo` into `Gamma_hi`, i.e. P-A1),
or (ii) repeated oriented differences (additive energy). This sharpens the
pre-registered OUTCOME-A: it must be read as *structural* compression, never
as cardinality collapse. (This is the same lemma the maintainer's audit calls
the "distinct-support lemma", `BRIEF4_DOSSIER_AUDIT.md` L34-37, re-derived
here in the degree form that applies to the pencil.)

---

## 2. Ambiguities found — flagged, NOT resolved

Each is a genuine fork. This pilot picks one branch **for the pilot only** and
measures the others where feasible.

| # | ambiguity | branches | pilot choice |
|---|---|---|---|
| A1 | Is `prec` an order on **supports** or on **witness polynomials**? Bridge L38 says "witness/codeword pairs"; heart L6 says "support-wise". Since `S` determines `p` and vice versa (given `z`), the two induce *different* total orders. | (a) order supports; (b) order coefficient vectors of `p` | (a) primary, (b) measured as `ORD-POLYLEX` |
| A2 | If supports: **lex** on the increasing sorted index tuple, or **colex** (equivalently, compare support bitmasks as integers)? Both are "lexicographic on sorted index sets" under different sorting conventions. | lex / colex | lex primary, colex measured as `ORD-COLEX` |
| A3 | Coordinate order on `D`. The domain is a multiplicative coset; the tree never fixes an enumeration. | `x_i = omega^i` (i ascending) / integer-representative order / any relabelling | `x_i = omega^i`, `i = 0..n-1` |
| A4 | If polynomials: coefficients read **low-to-high** or **high-to-low**, and with which representatives of `F_q` (`0..q-1`? centred? Conway-ordered?) | 4+ branches | low-to-high, representatives `0..q-1` |
| A5 | Does the selector run **before or after** the strips? "post-strip selector" is ambiguous between "select, then strip the selected rays" and "strip slopes, then select on survivors". | before / after | irrelevant at the pilot parameters: the pencil is proved strip-free (§3), so both agree. Flagged for the general case. |
| A6 | Ties. Two distinct witnesses can share neither `S` nor `p` at a fixed slope, so a *total* order on supports has no ties; but `ORD-POLYLEX` ties would need a rule. | — | no ties occur in any pilot run (verified: all four orders are total on each `W_z`); no tie-break rule is invented |
| A7 | Is the slope set `F_q` or `P^1(F_q)` (is `z = infinity`, i.e. the pure-`v` ray, a slope)? | affine / projective | measured: at the pilot parameters `z = infinity` is **dead** (`deg(V - p) = A - m < A`, so it carries no exact-`A` witness), so the choice is immaterial here |
| A8 | Whether "first match" means *minimum under a fixed total order* at all, or the first hit of some **search procedure** (e.g. a decoder's enumeration order, as in `pma_sigma_one_b11_scope/audit.md` L7 where "GROW is tested before J/A2"). | order-minimum / procedural | order-minimum (the audit's `min_prec W_z` reading) |

---

## 3. Strip status of the pilot family (so "post-strip" is not vacuous)

For the scaled split-fibre pencil used in FM1 (`U = G X^{ma}`,
`V = -G X^{m(a-1)}`, `deg G = g >= 1`), each T-strip is checked
*computationally per case* and holds *structurally*:

- **T0/T1**: `u != 0`, `v != 0`, `v != λu` (the ratio `-X^m` is nonconstant on
  `D`); no containment locator (checked exactly).
- **T2 (tangent)**: `deg(u + z v) = A` exactly for every `z` (leading term of
  `U`, `deg V < deg U`). So `f_z - p` is a **monic degree-`A`** polynomial for
  every degree-`<K` `p`, hence has **at most `A`** roots: no slope can reach
  agreement `A_0 > A`. **The pencil is tangent-free by degree.**
- **T3 (quotient periodicity)**: this is the one that bites. If `g = 0` then
  `U = X^{ma}` and `V = -X^{m(a-1)}` are both functions of `X^m`, the whole
  pencil folds through `x -> x^m`, and — when `m | gcd(n,K)` — the family is
  **quotient-stripped and worthless as a post-strip witness**. The pilot
  therefore *requires* `g >= 1` with the core **not** a union of complete
  fibres, and checks `u(ζx) != u(x)` for a primitive `M`-th root `ζ` for every
  `M | gcd(n,K)`, `M > 1`. (The audit's RowC 1/4 construction is safe for the
  same reason: its 53-point core is not a union of 4-point fibres.)
- **T4 (direction rank)**: rank 2 (the pencil is a genuine line, `u`, `v`
  independent) — checked.
- **Global genericity**: automatic and unconditional here. Any joint
  explanation would need agreement with `V` on `>= A` points, but
  `deg(V - c_1) = A - m` (nonzero because `deg V >= K > deg c_1`), so the
  joint support has size `<= A - m < A`. **Checked as a degree identity, no
  search needed.**

---

## 4. THE PILOT SELECTOR (exact definition used by FM1/FM2)

> Pilot convention. Pending planner ratification. Reported results are given
> under all four orders so that the ratification decision can be taken on
> evidence.

**Canonical coordinate order.** `D = {x_0, ..., x_{n-1}}`, `x_i = omega^i`,
where `omega` is the smallest primitive `n`-th root of unity generated as
`g^((q-1)/n)` from the least primitive root `g` of `F_q`. Supports are
identified with index sets `S ⊆ {0,...,n-1}`.

**Live slopes.** `z in F_q` with `W_z != ∅`, where

```text
W_z = { (p, S) : deg p < K, |{x in D : (u + z v)(x) = p(x)}| = A, S = that set }.
```

At the pilot parameters `W_z` is in bijection with

```text
{ S ⊆ D, |S| = A : deg( (U + zV) - prod_{x in S}(X - x) ) < K },
```

because `U + zV` is monic of degree `A`; the witness is
`p = (U+zV) - prod_{x in S}(X-x)`. This is the FM1 compiler's exact and
complete characterisation (no interpolation search needed).

**Primary order `ORD-LEX` (the pilot's normative order).**
For `S != T` both of size `A`, write them as increasing index tuples
`S = (s_1 < ... < s_A)`, `T = (t_1 < ... < t_A)`. Then

```text
S  prec_LEX  T   iff   (s_1,...,s_A) < (t_1,...,t_A) lexicographically.
```

`(p_z, S_z) := (p, S)` with `S = min_{prec_LEX} W_z`. Total on each `W_z`
(distinct supports); **no ties**, so no tie-break rule is invented (A6).

**Comparison orders (all measured).**

- `ORD-COLEX`: `S prec T` iff `int(bitmask(S)) < int(bitmask(T))`, i.e.
  `max(S Δ T) in T`. (Branch (b) of A2.)
- `ORD-POLYLEX`: compare the witness polynomials
  `(p^{(0)}, p^{(1)}, ..., p^{(K-1)})` — coefficients low-to-high, residues in
  `{0,...,q-1}` — lexicographically. (Branch (b) of A1, with A4 fixed.)
- `ORD-HASH-<seed>`: `S prec T` iff
  `blake2b(bitmask(S), key=seed) < blake2b(bitmask(T), key=seed)`. A
  deterministic stand-in for "an arbitrary total order", used as the **null
  control**: it is what the measurements should look like if the outcome owes
  nothing to the *algebra* of the canonical order.

**Post-strip.** All T-strips are verified inapplicable per §3, so the
post-strip selected family equals the selected family.

**`Gamma_lo` (the P-B object).** Given the selected family
`{S_z : z live}`, `Gamma_lo = { z : |S_z ∩ S_w| <= K-1 for all live w != z }`,
`Gamma_hi` its complement. P-B is the claim `|Gamma_lo| <= 8n^3`.

---

## 5. Honest limits of this manifest

- The order in §4 is **not** the repository's order — the repository has none.
  Any FM2 conclusion is a conclusion **about `ORD-LEX` (etc.)**, not about a
  ratified normative selector. This is the single biggest caveat on the
  pilot's verdict and it is restated in `REPORT.md`.
- A transport lemma between orders is *not* attempted and is not implied by
  agreement across the four orders; agreement is evidence, not proof.
- Nothing here touches `dag.json`, node statuses, or any `positive` path.
