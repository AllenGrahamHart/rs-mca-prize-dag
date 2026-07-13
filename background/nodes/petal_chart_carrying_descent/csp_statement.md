# Chart-carrying descent at M = 2: statement packet (SUCCESSOR-A claims #132, #128 + composition)

- **status:** proposed PROVED (Claims 1, 2, 3a, 3b as conditional composition); see csp_proof.md
- **consumer:** `petal_chart_carrying_descent` (SUCCESSOR-A), thence `petal_small_scale_staircase_census`
- **verifier:** csp_verify.py (ramguard tiny)
- **provenance:** search ledger `background/nodes/petal_chart_carrying_descent/ccd_findings.md` (catches #128-#132); this packet is the proof-grade write-up owed by the node's "YIELD, proof-grade (packet + audit owed before PROVED status)" clause.

## 0. Setting and pinned conventions

Throughout, `q` is an odd prime power, `H <= F_q^*` is cyclic of order
`n = 2^s` with `n | q-1` and `s >= 2`, `g` is a fixed generator of `H`, and
`x_j := g^j` for `j in Z`. Since `n` is even, `q` is odd and
`g^{n/2} = -1`, so the `K_2`-fibers of `H` (orbits of the order-2 subgroup
`K_2 = {1,-1}`) are the antipodal pairs `{x, -x}`.

`k` is EVEN with `2 <= k <= n-2`. Put

```text
n' = n/2,   k' = k/2,   nf = k/2 - 1,   t = (n-k)/2  (>= 1).
```

The **official row** is `RS[F_q, H, k]` (codewords = polynomials of degree
`< k` evaluated on `H`). The **quotient row** is `RS[F_q, H^2, k']`, where
`H^2 = {x^2 : x in H}` is cyclic of order `n'` with points `y_j := x_j^2`,
`j = 0..n'-1`. The squaring projection is `pi : H -> H^2`, `pi(x) = x^2`;
`pi^{-1}(y_j) = {x_j, -x_j}`.

**Fiber-aligned chart layout** at `(n,k)` (the layout pin of
`petal_small_scale_staircase_census`, census convention
`build_layout('fiber_aligned')`, `sigma = 1`):

```text
core       Z   = {x_j, -x_j : 0 <= j < nf} u {x_nf},      |Z| = k-1,
residual   R0  = {-x_nf},                                   r = |R0| = 1,
petals     T_i = {x_i, -x_i},  nf+1 <= i <= n/2 - 1,       ell = 2 (sigma = 1),
labels     c_i in F_q^*  (arbitrary nonzero),               petal count m_max = t.
```

The **chart word** `U : H -> F_q` is the concrete sunflower word
(def:capf-concrete-sunflower with `P_star = 0`, `Y = Z`):

```text
U = 0 on Z u R0,        U = c_i L_Z on T_i,        L_Z(X) = prod_{z in Z}(X - z).
```

A **contributor** (to `U`) is a codeword `f` (deg `< k`) with exact agreement
set `S = agr(f, U) := {x in H : f(x) = U(x)}` of size `|S| >= k+1`. The
**scale** is `c(S) = |Stab_H(S)|`; `c(S) >= 2` iff `S` is `K_2`-invariant
(Lemma L0 below, from `thm:stabilizer-partition(i)` at 2-power `n`).
A **class** is an exact agreement support `S` (one class per support;
supports of size `>= k` determine their codeword, csp_proof.md Lemma L1).

**Quotient objects.** `Z' := {y_j : 0 <= j < nf}` (`|Z'| = k'-1`), the split
image `y_nf`, and the **petal points** `y_i`, `nf+1 <= i <= n'-1` (`t` of
them). These `k' + t = n'` points are pairwise distinct and partition `H^2`.

**Reading A (pin, catch #129).** All descended LAYER bookkeeping below uses

```text
core'' = Z' u {y_nf}   (size k'),   sigma' = 0 (ell' = 1),   r' = 0,
```

i.e. the split image `y_nf` is absorbed into the descended core, NOT retained
as a residual. Reading B (`y_nf` retained, `r' = 1 = ell'`) violates the
strict hypothesis `r' < ell'` of the PROVED `petal_top_band_tail_collapse`
verbatim and additionally loses one unit of both agreement and degree; no
statement in this packet holds under reading B (Claim 2 becomes FALSE under
the induced degree bookkeeping — see the mutation control M3).

For a descended agreement set `S' <= H^2` put

```text
W  = S' n core''   (z := |W|),      D0' = core'' \ W   (d' := |D0'| = k' - z),
I' = S' \ core''   (subset of the petal points).
```

---

## CLAIM 1 — the structure theorem (catch #132)

Let `(n, k, q, (c_i))` be as in Section 0. Then:

**(S1) Locator factorization.**
`L_Z(X) = L_{Z'}(X^2) (X - x_nf)`, where `L_{Z'}(Y) = prod_{w in Z'}(Y - w)`.

**(S2) Word factorization and components.**
`U(x) = (x - x_nf) u1(x^2)` for every `x in H`, where `u1 : H^2 -> F_q` is

```text
u1 = 0 on Z' u {y_nf},        u1(y_i) = c_i L_{Z'}(y_i)  (petal points y_i),
```

i.e. `u1` is EXACTLY the concrete sunflower chart word at the quotient row
with word-presentation data `(Y' = Z', R0' = {y_nf}, singleton petals
T'_i = {y_i}, sigma' = 0, P'_star = 0)` and the SAME labels `c_i`.
Moreover the `M = 2` vector word `(u_0, u_1)` of `U` (fiberwise components,
`U(x) = u_0(x^2) + x u_1(x^2)`) satisfies `u_0 = -x_nf * u1` pointwise and
its odd component equals `u1`.

*Normalization pin (catch #133).* "Same scalars" holds in the `L_{Z'}`
normalization above. Under reading A's layer bookkeeping the induced
def:capf-sunflower-layer auxiliary labels are `c_i / (y_i - y_nf)`, not
`c_i`; consumers must not mix the two normalizations.

**(S3) Lift form of the periodic subclass.**
Every contributor `f` with `c(S) >= 2` factors as

```text
f(X) = (X - x_nf) g(X^2),        g := f_1 (the odd Fourier component),
deg g < k',
```

and `S = pi^{-1}(S')` with `S' := agr(g, u1)`, `|S'| = |S|/2 >= k'+1`,
`y_nf in S'`. In particular `g` is a contributor to `u1` at the quotient row.

**(S4) Agreement semantics of lifts; membership characterization.**
For ANY `g` with `deg g < k'` and `f := (X - x_nf) g(X^2)`:

```text
agr(f, U) = {x_nf} u pi^{-1}( agr(g,u1) \ {y_nf} ) u ( {-x_nf} iff g(y_nf) = 0 ).
```

Consequently agreement of a lift with `U` is all-or-nothing on every petal
`T_i` and on every core fiber (full-petal membership is automatic), and for
lift contributors

```text
c(S) >= 2   <=>   g(y_nf) = 0.
```

The retained-zero constraint descends automatically: it IS the core''
membership `y_nf in W`. The correspondence `S <-> S'` is a bijection

```text
{ scale->=2 contributor classes of U }  <->
{ contributor classes S' of u1 with y_nf in S' },
```

and on codewords it is the bijection `f <-> g` above.

**(S5) Chart-data descent.**
For a scale->=2 contributor `f <-> g` with data as in Section 0:

```text
missed core   D0 = Z \ S = pi^{-1}(D0'),        d := |D0| = 2d',
retained      R0 = {-x_nf} <= S,                r = 1  ->  r' = 0 (reading A),
agreement     a = sigma + d + 1 - r = d+1  ->   a' = sigma' + d' + 1 - r' = d'+1,
touched sets  I = { i : T_i <= S } = I'  (petals <-> petal points, no merging,
                                          m' = m for any chart petal count),
band          d >= ell (m-2) = 2(m-2)   <=>    d' >= ell'(m'-2) = m'-2,
official touched threshold ceil(a/ell) = d'+1 = a'/ell'   (exact match),
image         G_P := f / L_{Z n S} = Q(X^2),   Q = (Y - y_nf) G',
              G' := g / L_W,   deg G' <= d' - 1.
```

The per-member exact-assignment band (`m = |I|`) is equivalent to
`|S'| <= k'+2`, i.e. official `|S| <= k+4`; since `|S|` is even for this
class, official top-band sizes are exactly `|S| in {k+2, k+4}`.

**(S6) Descended tail-collapse hypotheses (obligation (ii)).**
Under reading A, for every fixed `(W, P)` with `P` a set of `m' >= 2` petal
points, the descended chart satisfies verbatim the hypotheses of the PROVED
chain `petal_retained_zero_effective_degree` (vacuous at `r' = 0`),
`petal_full_touched_set_injection` (`m'` pairwise disjoint singleton petals
disjoint from `core''`, pairwise coprime locators, `a' = ell' + d' - r'`),
and — whenever the band `d' >= m'-2` holds — `petal_top_band_tail_collapse`
(`ell' = 1 >= 1`, `m' >= 2`, `0 <= r' = 0 < 1 = ell'` STRICT,
`d' >= ell'(m'-2)`), which yields `<= m'+1` classes per descended chart.
(Claim 2 sharpens this to `<= 1`.)

**Scope.** All `n = 2^s` (`s >= 2`), all even `k` with `2 <= k <= n-2`, all
`q` with `n | q-1`, all label vectors `c_i in F_q^*`; `sigma = 1` fiber-aligned
charts; descent scale `M = 2`. SCOPED OUT: (i) `sigma > 1` charts — the census
machinery and the search evidence are `sigma = 1` only; the proof shape
extends when petals are unions of full 2-fibers but this is NOT claimed here;
(ii) direct `X -> X^M` descent at `M > 2` — refuted-as-mechanism (catch #130);
`M > 2` is priced through Claim 3's `K_2`-reduction instead; (iii) odd `k`:
the split-point fiber-aligned layout above requires `k` even, and the
`M = 2` component decomposition needs `2 | k` for the uniform degree bound
— for odd `k` this packet claims NOTHING (the odd-`k` fiber-aligned layout
has no split point and its scale->=2 pricing is a separate obligation, not
discharged and not hidden here).

---

## CLAIM 2 — per-chart uniqueness at the descended row (catch #128)

**(U0) Abstract uniqueness lemma.** Let `F` be any field, `W, P <= F` finite
and disjoint, `v : P -> F` any word, and `D >= 0`, `A >= 1` integers. Call
`g in F[X]` a *member* if

```text
deg g <= D,     g|_W = 0,     |{ y in P : g(y) = v(y) }| >= A.
```

If `2A - |P| > D - |W|`, then there is AT MOST ONE member.

**(U1) Instantiation (descended band charts).** At the quotient row, a
*band chart* is a pair `(W, P)`: `W <= core''` with `y_nf in W`, `|W| = z`,
`1 <= z <= k'-1`, `d' = k'-z`, and `P` a set of petal points with
`|P| = m' <= d'+2` (the band `d' >= ell'(m'-2) = m'-2`). Its *members* are
the descended scale->=2 contributors `g` (Claim 1) whose chart data satisfies
`agr(g, u1) n core'' = W` and `agr(g, u1) \ core'' <= P`. Every member has
`deg g <= k'-1`, `g|_W = 0`, and `>= k'+1-z = d'+1` agreements with `u1` in
`P`; with `D = k'-1`, `A = d'+1`:

```text
2A - m' >= 2(d'+1) - (d'+2) = d' > d'-1 = D - |W|,
```

so **every band chart at the descended row holds at most one member** —
hence at most one descended class (classes <-> members, Lemma L1). The
`m'+1` line of S6 is safe with slack factor `m'+1`.

*Margin pin.* The inequality closes with margin exactly 1, and the effective
degree `D - |W| = d'-1` consumes reading A (core'' of size `k'`; `deg g < k'`
from the code). Any one-unit relaxation — `deg <= d'` images as in the
generic def:capf-sunflower-layer, or `A = d'` as under reading B, or
`m' = d'+3` — admits two distinct members (mutation control M3 exhibits
this numerically). Weakest-form discipline: U0 is exactly what the
composition consumes; no stronger form is claimed.

**(U2) Boundary cases.** `d' = 0` charts are empty (the only candidate is
`g = 0`, which has exactly `k' < k'+1` agreements); `m' <= d'` charts are
empty (`|I'| >= d'+1 > m'`); at `m' = d'+1` the unique possible touched set
is `I' = P`. All covered by U0/U1.

---

## CLAIM 3 — composition: per-U pricing of ALL small scales

**(L0) K_2-invariance of scale-M supports.** At `n = 2^s`, every `S <= H`
with `c(S) >= 2` is `K_2`-invariant; hence for every dyadic `2 <= M <= n`,
the scale-`M` subclass (`c(S) = M`) of any contributor list is contained in
the `K_2`-invariant subclass. (One line from the subgroup lattice of a
cyclic 2-group; equivalently `thm:stabilizer-partition(i)`.)

**(C) Composition theorem (conditional on coverage).** Let `U` be a
fiber-aligned chart word as in Section 0, `u1` its descended word (S2).
Suppose a finite set `A'` of band charts `(W, P)` (as in U1) at the quotient
row **covers the descended top band**: every contributor class `S'` of `u1`
with `y_nf in S'` and `|S'| <= k'+2` satisfies, for some `(W, P) in A'`,
`S' n core'' = W` and `S' \ core'' <= P`. (Note: `S'` need not itself be
periodic at the quotient row — it generically is not.) Then

```text
#{ classes S of contributors to U with c(S) >= 2 and |S| <= k+4 }  <=  |A'|,
```

and this single count simultaneously prices EVERY dyadic scale
`2 <= M <= t`: `sum_M #{scale-M top-band classes} = #{K_2-invariant top-band
classes} <= |A'|`. No word-uniform input is consumed.

**(R) Residual obligations (exact, honest).** The composition C is
unconditional EXCEPT for:

1. **G1 coverage (the only mathematical gap):** the atlas `A'` must exist and
   cover, per received word, at the QUOTIENT row for the descended word `u1`
   within G1's census budget. By S2, `u1` is itself a concrete sunflower
   chart word at `(n', k')` (singleton petals, `sigma' = 0`), so this is
   exactly G1's quotient-closed clause — not a new kind of demand — but G1
   is an open TARGET, and its budget must absorb the measured chart
   multiplicity (~4e4 nonempty charts per word at `(64,16)`, catch #131).
2. **Band scope:** only the top band `|S| <= k+4` (equivalently the
   per-member exact-assignment band pin `d >= 2(m-2)`) is priced here;
   below-band classes are outside SUCCESSOR-A's statement.
3. **sigma > 1 charts:** scoped out (untested; not claimed).
4. **Aperiodic classes** (`c(S) = 1`): not this node's business (K4 bucket).
5. Claims 1/2/C are per fiber-aligned chart word; G1's official-row atlas
   must supply charts in this layout for the descent to engage (layout pin).

**What is NOT an obligation:** n >= 128 (no cap in this packet depends on n;
only realized volumes were measured at n <= 64); the M > 2 direct mechanism
(replaced by L0, which is proved); k odd (nothing claimed).
