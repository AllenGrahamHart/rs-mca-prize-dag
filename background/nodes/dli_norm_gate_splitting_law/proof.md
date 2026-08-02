# Proof

Notation as in the statement. `sigma_a` is the Galois automorphism of
`Q(zeta_n)` with `sigma_a(zeta_n) = zeta_n^a`, `a in (Z/n)^*`; it restricts
to a ring automorphism of `Z[zeta_n] = Z[x]/(x^h+1)`.

## Lemma S0 (Galois acts on `W_w` by a signed permutation)

For `0 <= i < h` write `ai mod n = e`. If `e < h` then
`sigma_a(zeta_n^i) = zeta_n^e`; if `e >= h` then
`sigma_a(zeta_n^i) = zeta_n^{e-h} * zeta_n^h = -zeta_n^{e-h}`. So in the basis
`{zeta_n^i}_{i<h}`, `sigma_a` is `i -> (ai mod n) mod h` with a sign.

*That map is a bijection of `{0,...,h-1}`.* Suppose
`ai == aj (mod h)` with `0 <= i, j < h`. Then `a(i-j) == 0 (mod h)`, and since
`a` is odd (hence invertible mod `n = 2h`, so also mod `h`), `i == j (mod h)`,
i.e. `i = j`.

Consequently `sigma_a` permutes the `h` basis elements up to sign, so it maps
a ternary vector of weight `w` to a ternary vector of weight `w`, and

```text
sigma_a : W_w -> W_w   is a BIJECTION                                  (S0)
```

(its inverse is `sigma_{a^{-1}}`). QED.

## Lemma S0' (how `Z` transforms)

`(sigma_a alpha)(zeta^j) = alpha(zeta^{aj})` for every odd `j`: writing
`alpha = sum_i c_i x^i`, `sigma_a alpha` is the reduction of
`sum_i c_i x^{ai}` mod `x^h+1`, and evaluating at `zeta^j` gives
`sum_i c_i zeta^{aij} = alpha(zeta^{aj})`. Hence

```text
Z(sigma_a alpha) = a^{-1} Z(alpha),                                    (S0')
```

and therefore

```text
a in H_U(alpha)  <=>  a.U subset Z(alpha)  <=>  U subset a^{-1}Z(alpha)
                 <=>  U subset Z(sigma_a alpha)  <=>  sigma_a alpha in Sol_U.
```

QED.

## Claim 1 (S1: the counting identity)

Count the set `T = { (alpha, a) in W_w x (Z/n)^* : a in H_U(alpha) }` two ways.

*By `alpha`:* `|T| = sum_{alpha in W_w} |H_U(alpha)|`.

*By `a`:* for fixed `a`, by `(S0')` the fibre is
`{alpha in W_w : sigma_a alpha in Sol_U} = sigma_a^{-1}(Sol_U)`, and by `(S0)`
`sigma_a` is a bijection of `W_w`, so the fibre has exactly `|Sol_U|`
elements. Summing over the `phi(n)` values of `a`,

```text
|T| = phi(n) |Sol_U|.
```

Equating the two counts gives `(S1)`. QED (1).

**Corollary (root-independence).** Replacing `zeta` by another primitive
`n`-th root `zeta^c` (`c` odd) replaces `Z(alpha)` by `c^{-1}Z(alpha)`, hence
`Sol_U` by `{alpha : c in H_U(alpha)}`, whose cardinality is `|Sol_U|` by the
"by `a`" count above. So `|Sol_U|` (and `|D_U|`, `sum|H_U|`, `max_m`,
`max|H_U|`, which are manifestly root-independent) do not depend on the
choice. **This is the entire content of the "equidistribution": it is an
identity, not a Chebotarev estimate.** QED.

## Claim 2 (S2: ratio identity, inequality, equality condition)

`H_U(alpha) = empty` contributes `0` to the right-hand side of `(S1)`, so

```text
phi(n) |Sol_U| = sum_{alpha in D_U} |H_U(alpha)| = |D_U| * mbar,
```

where `mbar` is by definition the mean of `|H_U|` over `D_U`. Dividing by
`phi(n)|D_U|` gives `(S2)`. Every `alpha in D_U` has `|H_U(alpha)| >= 1`, so
`mbar >= 1` and the ratio is `>= 1/phi(n)`: **the deviation can only be
upward.** Equality `mbar = 1` holds iff `|H_U(alpha)| = 1` for every
`alpha in D_U`, i.e. iff `|H_U(alpha)| <= 1` for every `alpha in W_w`.
QED (2).

*Reading.* `Sol_U` is the "`a = 1` slice" of the `H_U` mass; S1 says the mass
is spread perfectly evenly over the `phi(n)` slices; S2 says the only way the
observed ratio can exceed `1/phi(n)` is that some `alpha` sits in several
slices at once — a MULTIPLICITY effect, not a bias.

## Claim 3 (S3: the exactness criterion)

Assume `Stab(U) = {1}` and `q^{o+1} > maxnorm(phi(n), w)`. Suppose some
`alpha in W_w` had `|H_U(alpha)| >= 2`, say `a_1 != a_2` in `H_U(alpha)`.

*Step 1: `a_1 U != a_2 U`.* If `a_1 U = a_2 U` then
`(a_2^{-1}a_1) U = U`, so `a_2^{-1}a_1 in Stab(U) = {1}`, i.e. `a_1 = a_2` —
contradiction.

*Step 2: `m(alpha) >= o + 1`.* Both `a_1 U` and `a_2 U` are contained in
`Z(alpha)`, they are distinct subsets of size `o`, so their union has at
least `o+1` elements and `m(alpha) = |Z(alpha)| >= o + 1`.

*Step 3: the norm contradiction.* `alpha` is nonzero and supported in the
basis range, so by `dli_norm_gate_forward_and_ofold` (Claim 4, `(LN3-3)`)
`Norm(alpha) != 0` and `v_q(Norm(alpha)) >= m(alpha) >= o+1`, hence

```text
q^{o+1} <= |Norm(alpha)| = Norm(alpha) <= maxnorm(phi(n), w),
```

(the middle equality by positivity, `dli_norm_gate_energy_ceiling` Claim 1),
contradicting `(S3)`.

So `|H_U(alpha)| <= 1` throughout `W_w`, and Claim 2's equality condition
gives ratio `= 1/phi(n)` exactly. QED (3).

**Hypothesis-free weakening.** Since
`maxnorm(phi(n), w) <= w^{phi(n)/2}` (energy ceiling with `E = w`), the
condition `q^{o+1} > w^{phi(n)/2}` implies `(S3)` without needing the banked
exact maxnorm table.

**Sufficient conditions for `Stab(U) = {1}`.**

- `U = {1}`: `b{1} = {1}` forces `b = 1`. Unconditional — so all of the
  `o = 1` theory (junction 0 at `t = 2`, and the whole C1 relation lane) uses
  S3 with no side hypothesis.
- `max(U)^2 < n`, provided `1 in U`: let `b in Stab(U)`. Since `1 in U`,
  `b = b.1 in U`, so `1 <= b <= M := max(U)`. If `b > 1` then `bM <= M^2 < n`,
  so `bM mod n = bM > M`; but `bM in bU = U` forces `bM <= M` — contradiction.
  Hence `b = 1`.

**Where the hypothesis genuinely fails (so it is load-bearing).** For the
block family `U_L = {1,3,...,2L-1} subset Z/n`, `n = 2^m`:
`Stab(U_{n/4}) = {1, n/2 - 1}` — the map `u -> (n/2-1)u = n/2 - u (mod n)`
reflects the odd residues below `n/2` onto themselves — and
`Stab(U_{n/2}) = (Z/n)^*` (the full odd-residue set). `verify.py` exhibits
both at `n = 16, 32, 64, 128` and confirms that no other `L` is exceptional
there. That triviality holds for all other `L` is an exhaustively verified
pattern (`m <= 11`), **not** proved here; the official blocks
(`L_j = n_j/512`) lie outside both exceptional sizes but are not covered by
either proved sufficient condition for `j <= 25`. Recorded as an open side
condition; nothing in `dli_official_support_forcing` depends on it.

## Remark (why the measured deviations are exactly where they are)

Combining Claims 2 and 3: a row deviates from `1/phi(n)` only if some
`alpha in W_w` has `m(alpha) >= o+1`, which by the norm ceiling requires
`q^{o+1} <= maxnorm(phi(n),w) <= w^{phi(n)/2}`. In the provenance pilot's
1,960-row record there are 63 deviating rows; of the 54 with a banked
`maxnorm`, not one satisfies `(S3)` (the other 9 are `n = 128` rows where no
banked `maxnorm` exists, so `(S3)` is untested there), and
the deviation `mbar in [1,2]` is always upward — exactly what Claims 2-3
predict. The verifier reproduces 8 of those deviating rows exactly
(`ratio*phi = 6/5, 4/3, 8/5, 9/8, 40/31, 20/17, 4/3, 2`).
