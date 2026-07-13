# Proofs (chart-carrying descent at M = 2)

Notation and hypotheses as in csp_statement.md Section 0. All congruences of
exponents are mod `n`; all polynomial identities are in `F_q[X]` (or
`F_q[Y]` at the quotient row). Recall `q` is odd (because `2 | n | q-1`),
`g^{n/2} = -1`, `x_j = g^j`, `y_j = x_j^2 = g^{2j}`.

Two facts used repeatedly, proved first.

**Lemma L1 (classes <-> members).** Let `v` be any word on a finite set
`Omega` of field points. If `g_1, g_2` are polynomials of degree `<= D` and
`S <= Omega` satisfies `|S| > D` and `g_1 = v = g_2` on `S`, then
`g_1 = g_2`. In particular, for contributors (official row:
`deg <= k-1 < k <= |S|`; quotient row: `deg <= k'-1 < k' < |S'|`) the exact
agreement support determines the codeword, so distinct classes have distinct
codewords and counting classes equals counting codewords-with-support.

*Proof.* `g_1 - g_2` has degree `<= D` and `>= |S| > D` roots, hence is the
zero polynomial. ∎

**Lemma L2 (fiberwise component bijection; M = 2 case of the proved
`cyclic_fiber_interleaving_descent` decomposition).** Since `k` is even,
every `f in F_q[X]` with `deg f < k` has a unique decomposition

```text
f(X) = f_0(X^2) + X f_1(X^2),      deg f_0, deg f_1 <= k'-1,
```

(exponents `2i <= k-2` and `2i+1 <= k-1` both force `i <= k'-1`). For any
word `v : H -> F_q` define its vector word `(v_0, v_1)` on `H^2` by solving,
on each fiber `{x, -x}` (over `y = x^2`),

```text
v(x) = v_0(y) + x v_1(y),      v(-x) = v_0(y) - x v_1(y);
```

the matrix `[[1, x], [1, -x]]` has determinant `-2x != 0` (`q` odd,
`x != 0`), so `(v_0(y), v_1(y))` exists and is unique, and for every
codeword `f` and every `y in H^2`:

```text
f = v at BOTH points of the fiber over y   <=>   f_0(y) = v_0(y) and f_1(y) = v_1(y).
```

*Proof.* Uniqueness/existence of the decomposition is the exponent-residue
split; the equivalence is the invertibility of the displayed 2x2 system. ∎

---

## Claim 1

### (S1) Locator factorization

`Z = {x_j, -x_j : j < nf} u {x_nf}` and, for each `j`,
`(X - x_j)(X + x_j) = X^2 - y_j`. Multiplying over `j < nf` gives
`prod_{j<nf}(X^2 - y_j) = L_{Z'}(X^2)`, and the split point contributes
`(X - x_nf)`. Both sides are monic of degree `2 nf + 1 = k-1`. ∎

### (S2) Word factorization and components

Define `u1` on `H^2` by the displayed table (`0` on `Z' u {y_nf}`,
`c_i L_{Z'}(y_i)` at petal point `y_i`). The `n'` points `y_0, ..., y_{n'-1}`
are pairwise distinct (`2i ≡ 2j (mod n) <=> i ≡ j (mod n')`), and
`Z' u {y_nf} u {petal points}` = `{y_j : 0 <= j <= n'-1}` partitions `H^2`
into `k'-1 + 1 + t = n'` points, so `u1` is a well-defined word. Check
`U(x) = (x - x_nf) u1(x^2)` pointwise on `H`:

- `x = ±x_j`, `j < nf` (core fibers): LHS `= 0`; RHS `= (x - x_nf) u1(y_j) = (x - x_nf) · 0 = 0`. ✓
- `x = x_nf`: LHS `= 0`; RHS has the factor `(x_nf - x_nf) = 0`. ✓
- `x = -x_nf`: LHS `= 0` (residual); RHS `= (-2x_nf) u1(y_nf) = 0`. ✓
- `x = ±x_i`, `nf+1 <= i <= n/2-1` (petal `T_i`): LHS `= c_i L_Z(x)`; by S1,
  `L_Z(x) = L_{Z'}(x^2)(x - x_nf) = L_{Z'}(y_i)(x - x_nf)`, so LHS
  `= (x - x_nf) c_i L_{Z'}(y_i) =` RHS. ✓

For the vector word: `U(x) = (x - x_nf)u1(x^2) = -x_nf u1(x^2) + x u1(x^2)`
exhibits, on each fiber, the (unique, Lemma L2) solution
`u_0(y) = -x_nf u1(y)`, `u_1(y) = u1(y)`. Hence `u_0 = -x_nf u1` pointwise
and the odd component of `U` is exactly `u1`. That `u1` is the concrete
sunflower word at `(n', k')` with data `(Y' = Z', |Y'| = k'-1, R0' = {y_nf},
T'_i = {y_i}, P'_star = 0, labels c_i)` is a literal reading of
def:capf-concrete-sunflower: `u1 = P'_star = 0` on `Y' u R0'` and
`u1 = P'_star + c_i L_{Y'}` on `T'_i`, with `L_{Y'} = L_{Z'}`. ∎

*Proof of the normalization pin (#133).* For a descended member `g` with
core-agreement set `W` (so `g = L_W h`), the reading-A layer image is
`G' = g / L_W`, and at a petal agreement point `y_i`:
`G'(y_i) = u1(y_i)/L_W(y_i) = c_i L_{Z'}(y_i) / L_W(y_i)`. Since
`L_{core''} = L_{Z'} · (Y - y_nf) = L_W · L_{D0'}`, we get
`L_{Z'}(y_i)/L_W(y_i) = L_{D0'}(y_i)/(y_i - y_nf)`, i.e. the auxiliary word
in def:capf-sunflower-layer normal form is
`U'_{D0'}(y_i) = [c_i/(y_i - y_nf)] L_{D0'}(y_i)`: labels `c_i/(y_i - y_nf)`. ∎

### (S4) first (S3 consumes it): agreement semantics of lifts

Let `deg g < k'`, `f = (X - x_nf) g(X^2)` (degree `<= 2(k'-1)+1 = k-1 < k`,
a codeword). For every `x in H`, by S2:

```text
f(x) - U(x) = (x - x_nf) [ g(x^2) - u1(x^2) ].
```

- `x = x_nf`: the first factor vanishes — `x_nf` ALWAYS agrees.
- `x = -x_nf`: first factor `-2x_nf != 0`; agreement `<=> g(y_nf) = u1(y_nf) = 0`.
- any other `x` (fiber over `y != y_nf`): first factor `!= 0` at both fiber
  points (`x = x_nf` only at `x = x_nf`), so each of `x, -x` agrees
  `<=> g(y) = u1(y)` — the same condition for both: agreement is
  all-or-nothing on every fiber other than the split fiber.

This is exactly the displayed formula for `agr(f, U)`. Petals and core
fibers are fibers, so full-petal / all-or-nothing membership is automatic.

Now let `f` be a lift contributor and `S = agr(f, U)`, `S° := agr(g, u1)`.
If `g(y_nf) = 0` then `S = pi^{-1}(S°)` is `K_2`-invariant, so `c(S) >= 2`.
If `g(y_nf) != 0` then `x_nf in S` but `-x_nf notin S`, so `S` is not
`K_2`-invariant; since `c(S) | n = 2^s`, any `c(S) >= 2` would make `c(S)`
even and `S` `K_2`-invariant (L0 below) — contradiction; hence `c(S) = 1`.
This proves `c(S) >= 2 <=> g(y_nf) = 0` for lifts.

*Bijectivity of `S <-> S'`.* For scale->=2 lift contributors set
`S' := S°` (so `S = pi^{-1}(S')`, `|S| = 2|S'|`, `y_nf in S'`). The map
`f -> g` is injective (the decomposition of L2 is unique), and surjective
onto quotient contributors with `y_nf in agr`: given `g` with `deg g < k'`,
`g(y_nf) = 0`, `|agr(g, u1)| >= k'+1`, the lift `f` has
`|S| = 2|agr| >= k+2 >= k+1` — a contributor — with `c(S) >= 2`. Threshold
match: `|S| >= k+1` with `|S| = 2|S'|` even forces `|S| >= k+2` (`k` even),
i.e. `|S'| >= k'+1` — no class is lost or gained at the threshold. Distinct
classes correspond: `S = pi^{-1}(S')` and `S' = pi(S)` are mutually inverse
on this family (Lemma L1 pins one codeword per support on each side). ∎

### (S3) Lift form

Let `f` be a contributor with `c(S) >= 2`. By L0, `S` is `K_2`-invariant:
`S = pi^{-1}(S_0)` for `S_0 := pi(S)`, `|S_0| = |S|/2 >= (k+1)/2`, and since
`|S_0|` is an integer and `k` is even, `|S_0| >= k'+1`. Write
`f = f_0(X^2) + X f_1(X^2)` (L2). For every `y in S_0`, `f` agrees with `U`
at both fiber points, so by L2 `f_0(y) = u_0(y)` and `f_1(y) = u_1(y)`.
By S2 `u_0 = -x_nf u1`, so the polynomial `f_0 + x_nf f_1`, of degree
`<= k'-1`, vanishes at every `y in S_0` — at `>= k'+1 > k'-1` points — and
is therefore identically zero: `f_0 = -x_nf f_1`. Hence

```text
f(X) = -x_nf f_1(X^2) + X f_1(X^2) = (X - x_nf) g(X^2),   g := f_1,  deg g < k'.
```

By S4's semantics, `S = agr(f,U)` forces `agr(g, u1) = S_0` and (from
`-x_nf in S`) `g(y_nf) = 0`; thus `S' = S_0`, `|S'| >= k'+1`, `y_nf in S'`,
and `g` is a quotient contributor. ∎

### (S5) Chart-data descent

Let `f <-> g` be a scale->=2 contributor, `S = pi^{-1}(S')`,
`W = S' n core''`, `z = |W|`, `d' = k'-z`, `I' = S' \ core''`.

- `y_nf in W` always (S3), so `|W n Z'| = z-1`.
- Core fibers: for `j < nf`, `{x_j, -x_j} <= S <=> y_j in S' <=> y_j in W`.
  The split point `x_nf in S` always, `-x_nf in S` always (scale->=2). Hence
  `S n Z` = (fibers over `W n Z'`) `u {x_nf}`, `|S n Z| = 2(z-1)+1 = 2z-1`,
  and `D0 := Z \ S = pi^{-1}(core'' \ W) = pi^{-1}(D0')` — note
  `D0' <= Z'` since `y_nf in W` — with `d = |D0| = 2(k'-z) = 2d'`.
- Retained: `R0 = {-x_nf} <= S`, `r = 1`. Under reading A the point `y_nf`
  is a core'' point, `W` contains it, and no residual remains: `r' = 0`.
- Agreement bookkeeping: official `a = sigma + d + 1 - r = d+1`
  (def:capf-concrete-sunflower with `sigma = 1, r = 1`); descended
  `a' = sigma' + d' + 1 - r' = d'+1`. Touched threshold: official
  `ceil(a/ell) = ceil((2d'+1)/2) = d'+1 = a'/ell'`. Members meet it:
  `|I'| = |S'| - z >= k'+1-z = d'+1`.
- Touched sets: `T_i <= S <=> y_i in S'` (S4 all-or-nothing), and
  `i -> y_i` is injective on petal indices with images disjoint from
  `core''` (distinctness of the `y_j`, S2 proof). So `I = I'` under this
  identification; petals map to petal points with NO merging, and any chart
  petal count is preserved: `m' = m`.
- Band: `d = 2d'` gives `d >= 2(m-2) <=> d' >= m-2 = m'-2` — an exact
  equivalence for every `m`. For the per-member exact-assignment reading
  (`m = |I| = |S'| - z`): `d' >= m'-2 <=> k'-z >= |S'| - z - 2 <=>
  |S'| <= k'+2 <=> |S| <= k+4`; evenness of `|S|` (= `2|S'|`) makes the
  official top-band sizes exactly `{k+2, k+4}`.
- Image: `Z n S` = fibers over `W \ {y_nf}` plus `x_nf`, so by the S1
  computation applied to this subset,
  `L_{Z n S}(X) = L_{W \ {y_nf}}(X^2) (X - x_nf)`. Therefore

  ```text
  G_P(X) = f(X)/L_{Z n S}(X)
         = (X - x_nf) g(X^2) / [ (X - x_nf) L_{W \ {y_nf}}(X^2) ]
         = [ g / L_{W \ {y_nf}} ](X^2) =: Q(X^2).
  ```

  `g` vanishes on all of `W` (`y in W n Z'`: fiber over `y` in `S` and
  `u1(y) = 0` force `g(y) = 0`; and `g(y_nf) = 0`), so `L_W | g` and
  `Q = g/L_{W\{y_nf}} = (Y - y_nf) · (g/L_W) = (Y - y_nf) G'` with
  `G' := g/L_W` the reading-A descended image,
  `deg G' <= (k'-1) - z = d'-1`. The official retained-zero constraint
  `G_P(-x_nf) = 0` reads `Q(y_nf) = 0` — the factor `(Y - y_nf)` — i.e. it
  has descended automatically into the core'' membership `y_nf in W`. ∎

*(Note the sharpening: `deg G' <= d'-1`, one better than the generic layer
bound `<= d'`. This is exactly what reading A buys and what Claim 2 spends.)*

### (S6) Descended tail-collapse hypotheses

Fix `(W, P)`, `m' = |P| >= 2` petal points. Check the PROVED chain's
hypotheses verbatim at the descended chart:

- `petal_retained_zero_effective_degree` (H1): needs `R'` and `T'` disjoint,
  `|R'| = r' <= d'`, members vanish on `R'`. Here `r' = 0`, `R' = ∅`: the
  bijection `G -> Q` is the identity; the hypothesis holds vacuously.
- `petal_full_touched_set_injection` (H2): needs `m'` pairwise disjoint
  petals of size `ell'`, disjoint from `D0'` and `R'`, full-petal
  membership, `a' = ell' + d' - r'`, pairwise coprime petal locators.
  Singletons `{y_i}` are pairwise disjoint and disjoint from
  `core'' >= D0'` (S2/S5); membership at singletons is trivially
  all-or-nothing; `a' = 1 + d' - 0 = d'+1` matches S5; the locators
  `(Y - y_i)` are distinct monic linear, pairwise coprime.
- `petal_top_band_tail_collapse` (H3): needs `ell' >= 1` (= 1 ✓),
  `m' >= 2` (✓ by hypothesis), `0 <= r' < ell'` STRICT (`0 < 1` ✓ — this is
  where reading B dies: `r' = 1 = ell'` fails), and the band
  `d' >= ell'(m'-2) = m'-2` (✓ whenever the chart is a band chart; by S5
  this is EQUIVALENT to the official band `d >= 2(m-2)` at the same `m`).
- H4 (per-chart fixed data): the chart fixes `(W, P)`; members agree on all
  of `(core'' \ D0') u R' = W` (definition of `W`) and have no agreements
  outside `W u P` (chart membership requires `S' \ core'' <= P`; and
  `S' n core'' = W` exactly).

Hence `petal_top_band_tail_collapse` applies and gives `<= m'+1` distinct
classes per descended band chart. ∎

**Status of Claim 1: PROVED** (no step relies on search evidence; the ~100k
member verification of ccd_findings.md is corroboration, and csp_verify.py
replays it independently on banked + new cells).

---

## Claim 2

### (U0) Abstract uniqueness lemma

Let `g_1, g_2` be members: `deg g_i <= D`, `g_i|_W = 0`,
`I_i := {y in P : g_i(y) = v(y)}`, `|I_i| >= A`. Then

```text
|I_1 n I_2| >= |I_1| + |I_2| - |P| >= 2A - |P| > D - |W|.
```

Since `g_i` vanishes on `W`, `g_i = L_W h_i` with
`deg h_i <= D - |W|` (if `D < |W|` then `g_i = 0` and uniqueness is
trivial). The points of `P` are outside `W`, so `L_W != 0` there, and for
`y in I_1 n I_2`: `h_1(y) = v(y)/L_W(y) = h_2(y)`. Thus `h_1 - h_2` has
degree `<= D - |W|` and more than `D - |W|` roots, so `h_1 = h_2`, so
`g_1 = g_2`. ∎

### (U1) Instantiation

A member `g` of the band chart `(W, P)` is a quotient codeword
(`deg g <= k'-1 = D`) with `agr(g, u1) n core'' = W` — in particular
`g|_W = 0`, because `u1|_{core''} = 0` (S2) — and
`agr(g, u1) \ core'' <= P` with `|agr(g, u1)| >= k'+1`, so at least
`k'+1-z = d'+1 = A` agreements lie in `P`. The chart's word on `P` is
`v = u1|_P`. With `|P| = m' <= d'+2`:

```text
2A - |P| >= 2(d'+1) - (d'+2) = d' > d'-1 = D - |W|,
```

so U0 applies: at most one member. Classes equal members by Lemma L1
(`|S'| >= k'+1 > k'-1`). ∎

### (U2) Boundary cases

If `z = k'` (`d' = 0`): a member would vanish on `k'` points with degree
`<= k'-1`, forcing `g = 0`; but `agr(0, u1) = Z' u {y_nf}` has size
`k' < k'+1` (labels `c_i != 0` and `L_{Z'}(y_i) != 0` keep `u1 != 0` on
every petal point), so no member exists. If `m' <= d'`: `|I'| >= d'+1 > m'`
is impossible. If `m' = d'+1`: `|I'| >= d'+1 = m'` forces `I' = P`, and two
members would share all `d'+1 > d'-1` petal agreements — equal by the U0
computation. ∎

**Status of Claim 2: PROVED.** *Sharpness (consumed by mutation control M3):
with `D = k'` in U0 (equivalently images of degree `d'`, the generic
def:capf-sunflower-layer bound, or reading B's bookkeeping) the inequality
fails at `m' = d'+2`, and two distinct members do exist: interpolate
`h_1` through `v` on `J u {q_1}` and `h_2` through `v` on `J u {q_2}` where
`J <= P`, `|J| = d'`, `P \ J = {q_1, q_2}` — both have `>= d'+1` agreements
in `P` and generically `h_1 != h_2`. csp_verify.py exhibits this.*

---

## Claim 3

### (L0) K_2-invariance of scale-M supports

`Stab_H(S)` is a subgroup of the cyclic 2-group `H` (order `n = 2^s`), so
`c(S) = |Stab_H(S)|` is a power of 2. If `c(S) >= 2`, then `Stab_H(S)` is a
nontrivial subgroup of a cyclic 2-group, hence contains the unique subgroup
of order 2, which is `K_2 = {1, -1}` (`-1 = g^{n/2}` is the unique element
of order 2 in `F_q^*`, and it lies in `H`). Thus `K_2 · S = S`. Every
scale-`M` support (`c(S) = M >= 2`) is therefore `K_2`-invariant.
(This is `thm:stabilizer-partition(i)` specialized to `c = 2`, `n = 2^s`;
the one-line proof is included to keep the packet self-contained.) ∎

### (C) Composition theorem

Let `N := #{classes S of contributors to U with c(S) >= 2 and |S| <= k+4}`.

1. By L0, every such `S` is `K_2`-invariant, and by S3/S4 the map
   `S -> S' = pi(S)` is a bijection onto the contributor classes `S'` of
   `u1` with `y_nf in S'` and `|S'| = |S|/2 <= k'+2`; write `g_{S'}` for the
   (unique, L1) member codeword of `S'`.
2. By the coverage hypothesis, each such `S'` has a chart
   `(W_{S'}, P_{S'}) in A'` with `S' n core'' = W_{S'}` and
   `S' \ core'' <= P_{S'}`; then `g_{S'}` is a member of that band chart in
   the sense of U1.
3. By Claim 2 (U1), each chart of `A'` has at most one member. Distinct
   classes have distinct members (L1), so the assignment
   `S' -> (W_{S'}, P_{S'})` (choose any covering chart) is injective.
4. Hence `N <= |A'|`.

For the per-scale clause: the scale-`M` top-band classes (`M >= 2` dyadic)
partition the `c(S) >= 2` top-band classes by the value of `c(S)`
(`thm:stabilizer-partition(i)`: `c(S)` is well-defined and dyadic), so

```text
sum_{M >= 2 dyadic} #{scale-M top-band classes} = N <= |A'|.
```

No step consumed any word-uniform hypothesis on `U` beyond the fiber-aligned
chart-word form itself. ∎

**Status of Claim 3: L0 PROVED; C PROVED as stated (conditional on its
explicit coverage hypothesis).** The coverage hypothesis is the honest open
content and belongs to G1 (residual list R in csp_statement.md). Nothing
else in C is open.

---

## Where search evidence substitutes for argument: NOWHERE at M = 2

Every step above is a complete argument at general parameters. The roles of
the numerics are: (a) corroboration across ~85 cells / ~100k members
(ccd_findings.md); (b) regression pinning (csp_verify.py compares an
independent implementation against banked tables and new cells); (c) the
sharpness exhibits (M3) showing the uniqueness margin is exactly 1. The open
items are exactly the residual list R of Claim 3 (G1 coverage + budget;
band scope; sigma > 1; layout pin) — none is silently consumed above.
