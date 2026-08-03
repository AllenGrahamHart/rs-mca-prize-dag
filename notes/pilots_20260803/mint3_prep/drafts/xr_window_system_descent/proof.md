# Proof

Notation as in `statement.md`. **Provenance of the argument.** LEMMA W
is machine-verified in the source against an independent oracle
(`algebra.py:150-154` vs `:142-147`) but **no prose proof exists**; it is
written out from scratch below. THEOREM D(a),(b) likewise. THEOREM D(c)
is reconstructed from the P3 text (`PREREG.md:49-56`). **THEOREM R is
the one genuine transplant** — its proof is written in the source at
`toeplitz.py:7-19` and is reproduced with its hypotheses made explicit.
**THEOREM L is RECONSTRUCTED with two gaps named** (F1.d, F1.e): the
source cites "REPORT section 3", which does not exist.

---

## LEMMA W

Write `Z := H \ T`, so `|Z| = n - r' = k + d` — `Z` is the core and `T`
its complement. Identify words with their degree-`< n` interpolants on
`H`. Put `E_T = prod_{t in T}(X-t)` and `E_Z = prod_{z in Z}(X-z)`, so

```text
(F)   E_T E_Z = X^n - 1,     deg E_T = r',   deg E_Z = k+d
```

because `X^n - 1 = prod_{x in H}(X - x)` splits with distinct roots.

**(=>)** Suppose `P` has `deg P < k` and `(u - P)|_Z = 0`. Since
`deg(u - P) < n` and `E_Z` is squarefree with root set `Z`, vanishing on
`Z` gives `E_Z | (u-P)` in `F_q[X]`: write `u - P = E_Z B` with

```text
deg B < n - (k+d) = r'.
```

Multiply by `E_T` and use (F):

```text
(u - P) E_T = E_Z E_T B = (X^n - 1) B  ==  0   in F_q[X]/(X^n - 1).
```

Hence `u E_T == P E_T (mod X^n - 1)`, and
`deg(P E_T) < k + r' = n - d`. So the reduction of `u E_T` mod
`X^n - 1` has degree `< n-d`: its coefficients in degrees
`n-d, ..., n-1` vanish.

**(<=)** Conversely suppose `Q := u E_T mod (X^n - 1)` has
`deg Q <= n-d-1`. By definition `u E_T = Q + (X^n - 1) S` for some `S`,
and by (F) `X^n - 1 = E_T E_Z`, so

```text
Q = u E_T - E_T E_Z S = E_T (u - E_Z S).
```

Thus `E_T | Q`, and `P := Q / E_T` is a polynomial with

```text
deg P = deg Q - r' <= (n-d-1) - (n-k-d) = k-1 < k.
```

From `E_T P = E_T(u - E_Z S)` and `E_T != 0` in the domain `F_q[X]` we
get `u - P = E_Z S`, which vanishes on `Z`. So `P` is the required
codeword. **QED (W)**

**The Toeplitz form (W-T).** The reduction mod `X^n - 1` is cyclic
convolution: for `0 <= j <= n-1`,

```text
[X^j](u E_T mod (X^n-1)) = sum_{i=0}^{r'} u_{(j-i) mod n} E_i,
```

`E_i := [X^i] E_T`. Imposing this for `j = n-d, ..., n-1` gives the `d`
stated equations. As `j` decreases by one the index `(j-i)` shifts
uniformly, so the coefficient matrix is Toeplitz; its entries are the
`u_m` for `m` running over the syndrome window. The system is **linear
in `E_T`'s coefficients**, with `E_{r'} = 1` fixed (monic). The joint
system for `(u,v)` is the conjunction of the two, `2d` equations, and a
joint core is a common solution — this is the definition of the joint
core, so there is nothing to prove beyond `(W)` applied twice. **QED**

## COROLLARY W2 (the coordinates)

**Attribution first (hard law 5).** The correspondence proved here is
the band-lane instantiation of the **banked** counting frame
(`critical/nodes/counting_frame/statement.md:9`,
`critical/nodes/v8_ledger/statement.md:9`, and the set is already named
`D_j` at `critical/nodes/spi_exceptional_class/proof.md:87`); the
"`2d` linear conditions" reading is banked at
`notes/band_heart_consolidation_20260803/CONSOLIDATION.md:59-62` off the
KEY LEMMA. What follows is the two-line verification in *this* lane's
notation, not a new theorem.

`X^n - 1` is squarefree and splits over `F_q` with root set `H`.
Therefore its monic divisors of degree `r'` are exactly the
`prod_{t in T}(X - t)` for `r'`-subsets `T <= H`, and `T -> E_T` is a
bijection

```text
{ r'-subsets of H }  <-->  { monic degree-r' divisors of X^n - 1 }.
```

Cores `Z = H \ T` are in bijection with `T`, hence with those divisors.
Writing a monic degree-`r'` polynomial by its lower coefficients
`(E_0, ..., E_{r'-1}) in A^{r'}`, the system `(W-T)` is `d` affine-linear
equations (single word) resp. `2d` (joint). An intersection of `<= 2d`
affine hyperplanes has codimension `<= 2d`. Hence **cores = monic
degree-`r'` divisors of `X^n - 1` lying on an affine subspace of
codimension `<= 2d`.** **QED (W2)**

*The codimension can be strictly less than `2d` — that is exactly the
rank question. THEOREM R says it is not, on the gated class.*

## THEOREM D(a)

`T` is a union of `mu_M`-cosets iff `T` is invariant under
multiplication by `mu_M` (a coset union is a union of orbits of the
`mu_M`-action on `H`, and `M | n` makes `mu_M <= mu_n`).

**(=>)** If `T = union_l g_l mu_M`, then for each `l`,
`prod_{x in g_l mu_M}(X - x) = X^M - g_l^M` (substitute `X = g_l Y`:
`g_l^M prod_{i}(Y - zeta^i) = g_l^M(Y^M - 1)`, with `zeta` a generator
of `mu_M`). Hence `E_T = prod_l (X^M - g_l^M) = G(X^M)` with
`G(W) := prod_l (W - g_l^M)`, monic of degree `r'/M`.

**(<=)** If `E_T(X) = G(X^M)` then for `w in mu_M` and any root `x` of
`E_T`, `E_T(wx) = G(w^M x^M) = G(x^M) = 0`, so the root set `T` is
`mu_M`-invariant, i.e. a coset union. **QED (a)**

*(Both directions are proved here. The source machine-checks only
`=>` — 364 instances of check `D(b)` — so the converse is a genuine
addition; the verifier checks it. F1.c.)*

## THEOREM D(b)

With `E_T(X) = G(X^M)` we have `E_i = 0` unless `M | i`. So in

```text
sum_{i=0}^{r'} u_{(j-i) mod n} E_i = 0
```

only indices `i = 0, M, 2M, ...` contribute, and for those
`(j - i) = j (mod M)`. Hence equation `j` involves only the syndrome
positions congruent to `j` modulo `M`. **QED (b)**

## THEOREM D(c) — RECONSTRUCTED

*Reconstruction notice (F1.c): the source states (c) and machine-checks
the resulting bijection (14 instances, `algebra.py:339-342`), but gives
no derivation. The argument below is mine; it is the only reading under
which the source's own quotient construction
(`algebra.py:301, 306-307, 314`) is correct.*

Assume `M | gcd(n,k)`, `M | d`, `E_T = G(X^M)`, and that the syndrome
window of `u` is supported in the single class `rho` mod `M`, i.e.
`u_m = 0` for all `m` in the window with `m != rho (mod M)`.

By (b), equation `j` sees only positions `= j (mod M)`. If
`j != rho (mod M)` every coefficient appearing in it is zero, so the
equation is vacuous. The equations `j in {n-d, ..., n-1}` with
`j = rho (mod M)` number exactly `d/M` (the window has length `d` and
`M | d`). Those are the surviving equations.

Now set `N := n/M`, `k' := k/M`, `d' := d/M`, and let `g` generate `mu_n`
so that `g_N := g^M` generates `mu_N`. Writing `G(W) = sum_s G_s W^s`
(so `E_{sM} = G_s`) and `U_s := u_{rho + sM}`, each surviving equation
reads

```text
sum_{s=0}^{r'/M} U_{(j' - s) mod N} G_s = 0,
```

with `j'` running over `d'` consecutive residues mod `N` — which is
exactly `(W-T)` for the instance `RS_{k'}` on `mu_N` at depth `d'` with
word `U`. (Degrees match: `r'/M = (n-k-d)/M = N - k' - d'`.) The map
`T -> T/mu_M` (equivalently `E_T = G(X^M) -> G`) is therefore a
bijection between scale-`M` cores upstairs and cores of the quotient
instance, since (a) makes `T <-> G` a bijection and the two systems have
identical solution sets under it. **QED (c), modulo the reconstruction
flag**

**COROLLARY D6.** The bijection sends the upstairs syndrome window to
the quotient's syndrome window coefficient-by-coefficient
(`U_s = u_{rho+sM}`), i.e. **syndromes descend**. So definitions item 6's
quotient convention is correct *for the window system*, and P3 fires
formally on an exactly-degenerate scale-`M` adversary. **Scope: the
window system only.** P3-EVASION (`planted.py:212-223`) shows the strip
filter itself can still be evaded when `rho_u != rho_v`, because each
pencil member meets both classes; that is not a counterexample to D6, it
is the reason THEOREM L is needed.

## THEOREM R — TRANSPLANTED (`toeplitz.py:7-19`)

Hypotheses: `n - k >= 2d`; the tangent gate (max agreement of `u` with
the code `<= A = k+h`); `d <= h-2`, `h << n-k`.

A linear dependency among the `d` rows of `R(u,d)`, with coefficients
`(lambda_j)_{j=n-d}^{n-1}`, says precisely that the syndrome sequence
satisfies the linear recurrence with characteristic polynomial

```text
Lambda(X) = sum_j lambda_j X^{j-(n-d)},      deg Lambda <= d-1,
```

across all `n-k` syndromes. Since `n - k >= 2d` there are at least
`2 deg Lambda + 2` consecutive syndromes obeying the recurrence, which
is the Berlekamp-Massey threshold: BM returns `Lambda` as an **error
locator** of degree `<= d-1`. A locator of degree `<= d-1` exhibits a
codeword agreeing with `u` on at least `n - (d-1) = n-d+1` points.

But the tangent gate caps agreement at `A = k+h`, and
`n-d+1 > k+h` because `d <= h-2` and `h << n-k` give
`n-d+1 >= n-h+3 > k+h`. Contradiction. Hence no dependency exists and

```text
rank R(u,d) = d   exactly (the matrix has d rows).
```

**QED (R)**

**Sharpness (the converse, machine-checked).** Planting a codeword at
distance `L < d` from `u` makes the syndrome sequence satisfy a
recurrence of degree `L`, and the rank drops to exactly `L`
(`toeplitz.py` check T2, 14 instances). So the tangent gate is not
merely sufficient — the criterion is sharp.

**Consequence.** The linear part of the window system never degenerates
on the gated class, so the codimension in W2 is exactly `2d` there (the
joint system is the direct sum of two full-rank blocks whenever the two
words are independent) and no adversary can gain by rank collapse: **any
blow-up must come from the arithmetic of the divisors of `X^n - 1`.**
The MC word illustrates the distinction — full rank `w`, yet its
solution set is the whole coset lattice.

**Adjacency (hard law 5).** The band lane has no prior statement, but
the Hankel lane already calls `ker M(Z)` "the classical key equation /
Berlekamp-Massey kernel"
(`critical/nodes/f_termination_hankel/notes/pro_brief_broad.md:24-28`),
and `hankel_rank_profile_entropy` (PROVED) carries a rank-profile
dichotomy for Hankel kernels. THEOREM R is a different statement — full
rank on the *tangent-gated* class — but it is adjacent and is cited as
such, not presented in isolation.

## THEOREM L — RECONSTRUCTED, with two named gaps

*The source's proof is cited to "REPORT section 3"
(`descent.py:15`); **that file does not exist**. What follows expands
the six-line docstring `descent.py:15-20` and marks the two steps that
cannot be completed from anything on disk.*

Setting: a depth-`d` pair `(u,v)`, each **separately `M`-quotient-
periodic** — i.e. each word's syndrome window is supported in a single
class mod `M`; write `a` for `u`'s class and `b` for `v`'s.

**GAP F1.d — `a` and `b` are never defined in the source.**
`descent.py:17` writes `g = gcd(M, b-a)` with no definition of `a`, `b`
anywhere in the file. The only reading consistent with the pilot's own
fixture (`planted.py:49`: `RHO_U, RHO_V = 0, 1  # DIFFERENT classes
mod M`) is `a = rho_u`, `b = rho_v`. **This node adopts that reading and
flags it.**

**Step 1 (transplanted).** For an `M`-structured depth-`d` pair the
extra agreement of any pencil projection beyond the core lies in
`g * {0, 1, ..., m}` where `g = gcd(M, b-a)` and `m = (n-k-d)/M`. This
is the generalisation of banked BP(3) from the shift class to every
`M`-quotient-periodic pair. *Stated, not re-derived: it is the content
the missing REPORT section was to supply.*

**Step 2 (transplanted).** Liveness requires the extra agreement to
equal `h - d` **exactly** (a live slope attains agreement exactly
`A = k+h` on a core of size `k+d`).

**Step 3 — `g = 1`.** `M | d`, and `h` is ODD. Hence `h - d` is odd
whenever `d` is even; and `g | M` is a power of two.

**GAP F1.e — this step is asserted, not derived, in the source.**
`descent.py:17` says "`g = gcd(M, b-a)` **a power of two**" without
argument (it is inherited from BP(3)'s six-row shape, where `n`, `k`,
`M` are powers of two, so `M` is a 2-power and every divisor of `M` is
too — that much is immediate). The step "`M | d` and `h` ODD force
`g = 1`" then reads: a live extra agreement `h-d` must lie in
`g*{0,...,m}`, so `g | h-d`; if `g` were even then `h-d` would be even,
whence `h` and `d` share parity; `M | d` with `M` an even 2-power makes
`d` even, so `h` would be even — contradicting `h` odd. Therefore
`g = 1`. **This completes only when `M` is even**; at `M = 1` the
statement is vacuous and at odd `M` (which does not occur at the
six-row shape) the argument does not apply. The node's statement carries
the six-row shape hypothesis for this reason.

**Step 4 (arithmetic).** With `g = 1` the extra agreement ranges over
`{0, ..., m}`, so liveness needs `h - d <= m = (n-k-d)/M`, i.e.

```text
M <= (n-k-d)/(h-d) ,    hence   M <= cap_d = floor((n-k-d)/(h-d)).
```

**Step 5 (contrapositive).** If `M > cap_d` no slope is live, so
`L_P = 0` and the pair is not counted by `N_d` (which counts depth-`d`
pairs with `L_P >= 2`, `BAND_LANE_DEFINITIONS.md:34-36`). **QED (L),
modulo F1.d and F1.e**

**`h` odd is load-bearing, and this is exhibited, not asserted.** At the
`h`-even control (`n=20, k=8, h=6`) the pilot's own scan reports
`proved_scales: []` and `live_excluded_at_dmin: false` — liveness
excludes nothing. Step 3 is exactly where evenness breaks the argument.

## Honest scope

- **`cap_d` is banked, not proved here**
  (`xr_band_ledger_theorems/statement.md:38-44` THEOREM 3, at `J = k+d`,
  `A = k+h`). THEOREM L consumes it.
- **THEOREM L closes only `M >= 2^21`** at the prize rows. The scales
  `M = 2^1..2^20` are closed by a first-moment **expectation**, which is
  not a certified bound; the code itself partitions `proved_scales` from
  `heuristic_scales` (`descent.py:152-178`) and this node keeps that
  partition everywhere.
- **Nothing here answers SL-2.** The aperiodic case is untouched; it is
  restated as SL-2-RES with its two load-bearing hypotheses (`h` odd,
  `q >= 2^209`).
- **No count claim rests on a toy.** By SL-3 sub-criticality — itself a
  **conjecture** (`listsize_program/REPORT.md:57-58`) — no toy fixture
  can exhibit the blow-up, and the pilot pre-registered that its assigned
  falsifier would not fire.
- **The `2d` codimension is the generic value.** W2 asserts only
  `<= 2d`; equality on the gated class follows from THEOREM R for each
  word separately, and the joint statement additionally needs the two
  row-spaces to intersect trivially, which is **not** proved here.
