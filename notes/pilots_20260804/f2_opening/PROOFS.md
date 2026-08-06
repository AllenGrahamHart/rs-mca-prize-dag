# F2 opening pilot — the proofs

Round 14, mystery 2. All statements below are proved; each carries the
verifier stage that checks it. Notation is fixed in `verify.py`'s module
docstring and repeated where load-bearing.

## Setting (banked upstream, restated)

`p` odd, `e = v_2(p-1) >= 2`; `F_{p^2} = F_p(w)`, `Tr(a+bw) = 2a`;
`G = mu_{n}` with `n | p^2-1`, `n` even; `psi(s) = zeta_p^s`.

A **window** `W <= G` is any subset closed under `x -> -x`. Write
`m := |W|/2` for its number of antipodal pairs and `y_1..y_m` for one
representative per pair. (The deployed rung-`j` window is
`W = {x : ord(x) = n_j}`, `m_j = 2^{22+j}`; the full-group window is
`W = mu_n`. Both are antipodally closed —
`f2_antipodal_descent_lemma` Corollary A.)

A **frequency** is `f(x) = sum_{l in Lambda} C_l x^l`, `C_l in F_{p^2}`,
with character `chi_c(x) = Tr(f(x)) in F_p`. The census term is

```text
T_W(c) = prod_{x in W} (1 + psi(chi_c(x)))            ( = "exp S_c" )
P_W(c; z) = prod_{x in W} (1 + z psi(chi_c(x))),  V_b := [z^b] P_W.
```

**Class K1** = the parity-pure class: `Lambda` consists of ODD exponents
only (`f2_deployed_windows/REPORT.md:41`). *Not* the `k=1` of
`critical/nodes/f2_k1_contraction_theorem` — a live naming collision.

For `c in K1`, `f(-x) = -f(x)`, so `chi_c(-y) = -chi_c(y)`, and pairing
`x` with `-x`:

```text
(1 + zeta^s)(1 + zeta^{-s}) = 2 + zeta^s + zeta^{-s} = |1 + zeta^s|^2 >= 0
T_W(c) = prod_{i=1}^{m} (2 + zeta^{s_i} + zeta^{-s_i}),   s_i := chi_c(y_i).
```

(Total positivity is already proved upstream: `f2_fixed_sector/REPORT.md:19`,
470/470 K1 frequencies at four primes. We cite, we do not re-derive.)

Let **`L`** be the image of the `F_p`-linear evaluation map
`K1(Lambda) -> F_p^m`, `c |-> (s_1, ..., s_m)`.

---

## LEMMA 1 (the ternary-dual identity). *Verified: V2, 7 rows, exact.*

Averaging over the **full** `F_p`-subspace `K1(Lambda)` (with `c = 0`
included),

```text
    E_{c in K1(Lambda)} [ T_W(c) ]  =  sum_{eps in L^perp cap {-1,0,1}^m}
                                              2^{m - wt(eps)}
                                    =  2^{m} * Z(L),
    Z(L) := sum_{eps in L^perp cap {-1,0,1}^m} 2^{-wt(eps)},
```

`wt` = number of nonzero coordinates. In particular `E[T_W]` is a
non-negative **integer**.

*Proof.* Expand each pair factor as `2*1 + zeta^{s_i} + zeta^{-s_i}`,
i.e. sum over `eps_i in {-1,0,+1}` with weight `2` when `eps_i = 0` and
`1` otherwise. Multiplying out,

```text
T_W(c) = sum_{eps in {-1,0,1}^m} 2^{m - wt(eps)} zeta^{<eps, s(c)>}.
```

`c |-> s(c)` is `F_p`-linear with image `L`, so `s(c)` is uniform on `L`
as `c` runs over the subspace. For a fixed `eps`,
`E_c[zeta^{<eps, s>}] = (1/|L|) sum_{s in L} zeta^{<eps,s>}` is `1` if
`<eps, s> = 0` for all `s in L` (i.e. `eps in L^perp`) and `0` otherwise,
by orthogonality on the group `L`. Summing gives the identity. QED

**Arithmetic meaning of the dual.** `eps in L^perp` says
`sum_i eps_i chi_c(y_i) = 0` for all `c`, i.e. (as `Tr` is surjective and
the `C_l` are free in `F_{p^2}`)

```text
    sum_{i=1}^{m} eps_i y_i^{l} = 0  in F_{p^2},  for every l in Lambda.
```

Since every `l in Lambda` is odd, `eps_i y_i^l = (eps_i y_i)^l`, so with
`z_i := eps_i y_i` this reads: **a subset `S` of `W` containing at most
one element of each antipodal pair, all of whose `l`-th power sums
vanish.** (O1) is therefore a *vanishing-power-sum* question, not an
analytic one.

**Corollary 1.1 (the unconditional floor).** `eps = 0` always lies in
`L^perp`, so `Z(L) >= 1` and

```text
    E_{c in K1}[T_W(c)]  >=  2^{m}  =  2^{|W|/2}   for EVERY Lambda.
```

So (O1)'s target `2^{n/2+o(n)}` can never be beaten: **(O1) is an
equality-shaped obligation with zero slack.** This makes the
fixed-sector pilot's "dead heat, zero structural margin"
(`f2_fixed_sector/REPORT.md:27`) a theorem rather than a reading.

---

## LEMMA 2 (surjectivity; the sharp form). *Verified: V12, 8 rows; V3, 8 rows; V3b, full brute force over 390 625 frequencies.*

Suppose `Lambda ⊇ {1, 3, 5, ..., 2m-1}` and these are distinct residues
mod `n` (automatic: `2m-1 < n` for both the full and the deployed
window). Then the evaluation map is **surjective**: `L = F_p^m`, hence
`L^perp = 0` and `Z(L) = 1`.

*Proof.* Over `F_{p^2}` the relevant matrix is
`M = (y_i^{2r-1})_{i,r=1..m}`. Factor

```text
    M = diag(y_1, ..., y_m) * ( (y_i^2)^{r-1} )_{i,r},
```

a diagonal (invertible: `y_i != 0`) times a Vandermonde in the squares
`y_i^2`. The map `y -> y^2` on `mu_n` is exactly 2-to-1 with fibres the
antipodal pairs `{y,-y}`, and the `y_i` are one per pair, so the `y_i^2`
are **pairwise distinct**; the Vandermonde is invertible. Hence
`(C_l) |-> (sum_l C_l y_i^l)_i` is onto `F_{p^2}^m`, and composing with
the (surjective, `F_p`-linear) trace coordinatewise gives `L = F_p^m`. QED

**Alternative hypothesis (weaker matrix input, more symmetric).** If
`Lambda` contains *every* odd residue mod `n`, surjectivity also follows
by a DFT argument: extend `eps in L^perp` to `nu` on `Z/n` by
`nu(a_i) = eps_i`, `nu(a_i + n/2) = -eps_i`, zero off `W`. Then
`nu(a + n/2) = -nu(a)`, so `nu_hat(l) = (-1)^{l+1} nu_hat(l)`, forcing
`nu_hat` to be supported on odd `l`; and `nu_hat(l) = 2 sum_i eps_i y_i^l
= 0` there by hypothesis. So `nu_hat ≡ 0`, hence `nu ≡ 0` and `eps = 0`.
(This is the route pre-registered as P2; Lemma 2 supersedes it, needing
`2m-1` conditions instead of `n-1`.)

### THEOREM A — (O1) is DISCHARGED, exactly. *Verified: V3b (brute force), V3, V12.*

Under Lemma 2's hypothesis,

```text
    E_{c in K1(Lambda)} [ T_W(c) ]  =  2^{|W|/2}   EXACTLY,   o(n) = 0.
```

*Proof.* Lemma 1 with `Z(L) = 1`. QED

Equivalently: the pair values `s_1..s_m` are **exactly independent and
uniform** on `F_p^m`, so the product's mean is the product of the
per-pair means, and the per-pair mean is
`(1/p) sum_s (2 + 2 cos(2 pi s/p)) = 2` exactly — the constant the
fixed-sector pilot measured and could only bank as a heuristic
(`PREDICTION_VS_MEASUREMENT.json` P6: "the product-level `2^{n/2}`
statement is banked as a FIRST-MOMENT HEURISTIC"). **Theorem A supplies
the missing product-level step: independence, by surjectivity.**

**Punctured version** (the obligation's `c != 0` reading): with
`N := |K1(Lambda)| = p^{2|Lambda|}`,

```text
    E_{c != 0}[T_W] = (N * 2^m - 4^m) / (N - 1)  <  2^m,
```

since `T_W(0) = 4^m > 2^m`. So excluding the trivial frequency only
*helps*: (O1) holds in both readings.

---

## THEOREM B — the b-resolved law; (O2) is NOT an independent obligation. *Verified: V4, 5 rows + the surjective row, exact.*

For **every** `Lambda`, define for `A ⊆ {1..m}`

```text
    N(A) := #{ eps in {-1,+1}^A x {0}^{A^c} : eps in L^perp }   (>= 0, an integer).
```

Then

```text
 (i)   E_c[V_b] = sum_{A, B disjoint, |A| + 2|B| = b} N(A)
                = sum_{A : |A| <= b, |A| = b mod 2} N(A) * C(m - |A|, (b-|A|)/2),
 (ii)  E_c[V_b] >= 0 for every b,
 (iii) sum_b E_c[V_b] = E_c[T_W],
 (iv)  hence E_c[V_b] <= E_c[T_W] for every b.
```

*Proof.* Per pair the `z`-factor is
`(1 + z zeta^{s})(1 + z zeta^{-s}) = 1 + z(zeta^{s} + zeta^{-s}) + z^2`.
Choosing the `1` or the `z^2` contributes `eps_i = 0` (the `z^2` term is
`zeta^{s} zeta^{-s} = 1`); choosing the middle term contributes
`eps_i = ±1` and one unit of `b`. Averaging over `c` and applying the same
orthogonality as Lemma 1 kills every `eps` outside `L^perp`, leaving the
stated non-negative counts. (iii) is `z = 1`; (ii) and (iv) follow since
all terms are non-negative. QED

**Consequence for the obligation list.** (O2) as stated — "the same at
fixed `b`", i.e. `E_c[V_b] <= 2^{n/2+o(n)}` — follows from (O1) by (iv).
It is *strictly weaker*, not harder. **The obligation list shortens from
three to two.**

**Theorem B'** (the sharp slice law). Under Lemma 2's hypothesis
`N(A) = 0` for `A != ∅` and `N(∅) = 1`, so

```text
    E_c[V_b] = C(m, b/2) for b even,   0 for b odd.
```

The maximum over `b` is `C(m, m/2) ~ 2^m / sqrt(pi m / 2)`: the
b-resolved first moment beats the full-window bound by a factor
`sqrt(m)`. This answers the *Hamming-slice fence* on its own terms — the
fence's worry was that a full-window statement says nothing at fixed
`b`; here the fixed-`b` statement is exact and is `sqrt(m)` **better**.

---

## LEMMA 3 (a rigorous necessary condition at partial condition sets). *Verified: V6, 5 rows; tight (3856 >= 3855 at p=17).*

For any `Lambda`, since `T_W >= 0` pointwise on K1 and `s = 0` is
attained (at `c = 0`),

```text
    E_{c in K1}[T_W] >= T_W(0)/|L| = 4^m / p^{dim L} = 2^{|W|} / p^{dim L}.
```

Hence **(O1) forces**

```text
    dim_{F_p} L  >=  m / log2 p  -  o(n)/log2 p.
```

*Proof.* Drop every term but `c` in the kernel of the evaluation map;
each contributes `T_W(0) = 4^m`, and the kernel has index `|L| = p^{dim L}`.
QED

**Official-row reading** (`V11`): the condition count must satisfy
`t >= m_j / log2 p`. At rung 16 (`m_16 = 2^38`) this needs
`8.87e9` against `t ~ 7e10` — a **7.89x margin**. Not orders of
magnitude: the tower is only just wide enough, and any re-pricing of `t`
downward by an order of magnitude would violate a *proved necessary
condition* for (O1).

---

## LEMMA 4 — (O3): the pullback ramification, exactly. *Verified: V8, 12 rows, exact in Z[zeta_p].*

Let `f(x) = g(x^{2^d})`. Then as polynomials in `z`,

```text
    P_{mu_n}(f; z)  =  ( P_{mu_{n/2^d}}(g; z) )^{2^d},
```

hence `T_j(f) = (T_{j-d}(g))^{2^d}` and the b-coefficients are the
`2^d`-fold convolution of the reduced ones.

*Proof.* `x -> x^{2^d}` maps `mu_n` **onto** `mu_{n/2^d}` with every
fibre of size exactly `2^d` (`n` a 2-power times the relevant factor;
`gcd(2^d, p) = 1`). The product over `x in mu_n` therefore factors into
`2^d` identical copies of the product over `u in mu_{n/2^d}`. QED

**What PP5.0 must carry.** A pullback frequency is **not** an
independent factor in the composition: its contribution is a `2^d`-th
*power* of a lower-rung contribution. Any composition law that multiplies
per-sector factors as if independent will over-count the K2 branch by
exactly this ramification. (This makes precise the requirement recorded
at `f2_fixed_sector/REPORT.md:21,33`; the terminal-step sign edge case
noted there — 1/40 at `p=641` — is *not* addressed here and stays named.)

---

## THEOREM C — T3-uniform is FALSE. *Verified: V9, 3 rows, explicit exhibits.*

Suppose the condition set covers every residue mod `n` (i.e. `t >= n`).
Then the folded frequency `f|_{mu_n}` is an **arbitrary** function
`mu_n -> F_{p^2}` (the DFT/Vandermonde over `mu_n` is a bijection between
coefficient vectors and value vectors). Consequently there exists a
frequency in the **generic class G** (both parity parts nonzero) whose
deployed window has

```text
    every Delta_i EVEN,   |R_p| = 1 exactly,   flat = 0 exactly,   D = m.
```

*Proof / construction.* Assign values `chi_c(x) = v(x)` freely with every
`v(x)` **even** and `< p/2`, and with `v(y) != v(-y)` for some pair and
`v(y) + v(-y) != 0` for some pair. `v(x) < p/2` makes every carry flag
`[2s > p]` zero, so `sigma = s` and `Delta_i = v(y_i) - v(-y_i)`, which
is even because both values are. Then
`R_p = (1/m) sum_i (-1)^{Delta_i} = 1` (`omega^p = -1`), so `flat = 0`.
The two "some pair" conditions put the interpolated `f` in class G.
Interpolate `C_l` by the inverse DFT. QED

*Exhibits*: `p=41, n=16` (G: 8 odd / 8 even support), `p=17, n=32`
(16/1), `p=97, n=64` (32/32) — all with `m R_p = m` exactly.

**So "generic-frequency flatness, uniform in `p` and `m`"
(`f2_deployed_windows/REPORT.md:45`) is not merely unproved — as a
uniform statement it is false, and refuting it needs no analytic input
at all.** The measured `flat ~ 0.55-0.60` is a statement about *sampled*
frequencies, i.e. it was always a measure statement.

---

## LEMMA 5 — the parity machinery cannot pay (O1). *Verified: V10, 2 rows.*

The antipodal-descent / parity-defect machinery is a functional of the
`Delta` **multiset**; the K1 mass is a functional of the **additive
relations** among the `y_i^l` (Lemma 1). They are independent:

Fix the deployed window `W` and vary only the condition set. On *every*
K1 frequency of *either* condition set the certificate returns the
identical output — all `Delta_i` even, `D = m`, `flat = 0` — while

```text
    p=17, m=8 :  E_c[T_W] = 3856      (Lambda = {1})   vs  256    (Lambda ⊇ {1,3,..,2m-1})
    p=97, m=16:  E_c[T_W] = 44 278 048 (Lambda = {1})  vs  65 536 (ditto)
```

a factor of 15.06 and 675.6 respectively.

**Verdict.** `f2_parity_defect_certificate` is not merely
tight-but-empty on deployed windows for (O1) — it is the **wrong
functional**, and no sharpening of it can discharge (O1). Its live use
is as the **T3 vehicle** (it is informative exactly on
parity-INHOMOGENEOUS windows, i.e. the G class), not as an (O1) tool.

---

## Scope, and what is NOT claimed

- Theorem A/B require `Lambda ⊇ {1,3,...,2m-1}`. At the official row
  (`m_j = 2^{22+j}`, `t ~ 7e10`) that is **rungs 1..13**. Rungs 14-16 are
  **NOT** discharged; there `L^perp != 0` is possible (at rungs 15-16 it
  is forced, since `dim L <= t < m`) and (O1) reduces to bounding
  `Z(L)` — the vanishing-power-sum problem of Lemma 1. This is the
  pilot's residual and its top-ranked sub-lemma.
- The 2x window-reconstruction ambiguity flagged at
  `f2_deployed_windows/REPORT.md:69` moves the rung cut-off by one; it
  cannot affect Lemmas 1-5, which are window-agnostic.
- Nothing here touches the **generic-class** mass constant `(4/pi)^n`
  (`f2_annealed_phase_split`, PROVED, with a standing no-go against
  absolute routes) — Theorem A is about the K1 class only.
- Nothing here freezes PP5.0, and Lemma 4 constrains it without
  discharging it. The K2 terminal-step sign edge case stays named.
- `E_c[.]` is an **average** over the K1 subspace. The consumer sums
  over frequencies; the normalisation `|K1|` is a seam question for
  PP5.0, raised as CATCH-3 in `REPORT.md`.
- No status flip is proposed for any minted node.
