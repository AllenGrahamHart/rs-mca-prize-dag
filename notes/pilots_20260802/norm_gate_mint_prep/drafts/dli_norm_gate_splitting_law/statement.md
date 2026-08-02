# dli_norm_gate_splitting_law

- **status:** PROVED
- **closure:** proof
- **scope:** `n = 2^s >= 4`, `q` odd prime with `n | q - 1`, `U` any set of
  `o` odd residues mod `n`, and `W_w` the set of ternary weight-`w` vectors
  supported in the basis range `[0, phi(n))`. Claims 1-2 are unconditional;
  Claim 3 carries the explicit hypothesis `Stab(U) = {1}`.
- **provenance:** notes/pilots_20260802/dli_norm_gate/{REPORT,FABLE_AUDIT}.md
  (lemma LN7 = S1-S3), with the full measurement record in
  `results/splitting_*.json` + `results/analysis.json` (1,960 rows;
  `S1_violations = 0`, `S2_violations = 0`, `S3_violations = 0`,
  `LN6_violations = 0`; 63 rows deviate from `1/phi(n)`, and of the 54 of
  those that have a banked `maxnorm` NOT ONE satisfies S3's condition — the
  remaining 9 are `n = 128` rows for which no banked `maxnorm` exists, so S3
  is untested rather than confirmed there). **Discharges** the C2'' pilot's L13 splitting
  observation (`notes/pilots_20260802/c2pp_nullity_structure/REPORT.md` §5:
  "at `q = 97, 113` exactly `1/8 = 1/phi(16)` of norm-divisible sign patterns
  are solutions", recorded there as CONJECTURAL beyond three primes) from a
  Chebotarev-flavoured equidistribution guess to an exact counting identity
  plus a bounded, checkable correction.

## Setting

Notation of `dli_norm_gate_forward_and_ofold`: `h = phi(n) = n/2`,
`Z[zeta_n] = Z[x]/(x^h+1)`, `zeta in F_q^*` of exact order `n`,
`Z(alpha) = {j odd mod n : alpha(zeta^j) = 0}`, `m(alpha) = |Z(alpha)|`.
`W_w` = ternary weight-`w` vectors supported in `[0,h)`
(`|W_w| = C(h,w) 2^w`). For a block `U` of `o` odd residues put

```text
H_U(alpha) = { a in (Z/n)^* : a.U subset Z(alpha) },
Sol_U      = { alpha in W_w : U subset Z(alpha) } = { alpha : 1 in H_U(alpha) },
D_U        = { alpha in W_w : H_U(alpha) != empty },
Stab(U)    = { b in (Z/n)^* : b.U = U }.
```

`Sol_U` is exactly the set of block-`U` skew/relation solutions at the
CHOSEN root `zeta` (at `o = 1`, `D_U = {alpha : q | Norm(alpha)}`, the
norm-divisible set — which is why the measured statistic is "the fraction of
norm-divisible sign patterns that are solutions"). Write
`maxnorm(h, w) = max{ Norm(alpha) : alpha in W_w }` (the banked C1 ladder).

## Statement

1. **S1 (the counting identity — THEOREM, unconditional).**

   ```text
   phi(n) * |Sol_U|  =  sum_{alpha in W_w} |H_U(alpha)|.               (S1)
   ```

   Equivalently: for every `a in (Z/n)^*`, `#{alpha in W_w : a in H_U(alpha)}`
   is the same number `|Sol_U|`. **Corollary:** `|Sol_U|` does not depend on
   which primitive `n`-th root of `F_q` is chosen — Galois equidistributes
   EXACTLY; there is no equidistribution conjecture here.
2. **S2 (the ratio identity, the inequality, and the equality condition —
   THEOREM, unconditional).** If `|D_U| > 0` then

   ```text
   |Sol_U| / |D_U|  =  mbar / phi(n),   mbar := (1/|D_U|) sum_{alpha in D_U}
                                                |H_U(alpha)|  >= 1,     (S2)
   ```

   so the ratio is `>= 1/phi(n)`, **the deviation is upward only**, and

   ```text
   |Sol_U| / |D_U| = 1/phi(n)   <=>   |H_U(alpha)| <= 1 for every alpha in W_w.
   ```

   The equality condition is a theorem, not an observation.
3. **S3 (an exactness criterion — THEOREM, under the stated hypothesis).**
   Assume `Stab(U) = {1}`. If

   ```text
   q^{o+1} > maxnorm(phi(n), w)                                        (S3)
   ```

   then `|H_U(alpha)| <= 1` for every `alpha in W_w`, hence by S2 the ratio
   is **exactly `1/phi(n)`**. A weaker but hypothesis-free sufficient form
   (using `dli_norm_gate_energy_ceiling`): `q^{o+1} > w^{phi(n)/2}`.
   *Two proved sufficient conditions for the hypothesis:* `U = {1}` (so the
   whole `o = 1` theory, including junction 0 at `t = 2` and the entire C1
   relation lane, is unconditional); and `max(U)^2 < n`.

## The `1/phi(n)` law at official scale — a CONSEQUENCE, stated precisely

There is **no** unconditional claim that the official splitting ratio is
`1/phi(n)`. What is proved is the implication: *at any junction where the
CHECKABLE inequality `(S3)` holds for the relevant `(q, o, w)` and the block
has trivial stabilizer, the ratio is exactly `1/phi(n)`; and whenever it
fails, S2 still pins the ratio to `mbar/phi(n) >= 1/phi(n)` with the excess
`mbar` bounded by the norm ceiling (`mbar - 1` is carried entirely by the
`alpha` with `m(alpha) >= o+1`, of which there are none once `(S3)` holds).*
This replaces a conjecture by a theorem plus a finite check.

## Explicitly NOT claimed (context)

- **Not** that `(S3)` holds at every official junction. `(S3)` is a
  criterion; whether it fires at a given official `(j, w)` is an arithmetic
  question about `maxnorm(N_j, w)` versus `q^{L_j+1}`.
- **Not** that `Stab(U_j) = {1}` for every official block. The two proved
  sufficient conditions cover `U = {1}` and blocks with `max(U)^2 < n`; the
  official `U_j = {odd u : u 2^j <= t}` satisfies the latter only for
  `j >= 26`. For the block family `U = {1,3,...,2L-1}` in `Z/2^m` the
  stabilizer is trivial for every `L` except `L = n/4` (where it is
  `{1, n/2-1}`) and `L = n/2` (where it is everything) — **exhaustively
  verified for `m <= 11` and reproduced in `verify.py` at `n <= 128`, but a
  VERIFIED PATTERN, not a theorem.** Official blocks have `L_j = n_j/512`,
  outside both exceptional sizes. **FLAGGED for the coordinator.**
- **Not** a distributional model. The variance of the solution count within
  a support is under-dispersed by roughly `2x` relative to a binomial model
  (provenance pilot §6, R2), and the `q`-independent norm multiset does NOT
  determine the junction ratio `rho` (R3, a scored pre-registration MISS:
  332/409 = 81% of classes are ambiguous). S1-S3 are exact counting
  statements about `|Sol_U|` and `|H_U|`, nothing more.
- **Not** a statement about `Norm`-divisibility counts. S1-S3 relate
  solutions to `H_U`; the arithmetic input is only `q^{m} | Norm` and
  `Norm <= maxnorm`, both banked elsewhere.

## Falsifier

An `(n, q, w, U)` with `phi(n)|Sol_U| != sum|H_U|`; a row with ratio
`< 1/phi(n)`; a row with `Stab(U) = {1}` and `q^{o+1} > maxnorm(phi(n),w)`
whose ratio is not exactly `1/phi(n)`; or a choice of primitive `n`-th root
changing `|Sol_U|`.

## Verifier

`verify.py` in this node (profile: `tiny`, pure python, ~1.4 s). Independent
re-scan of 30 rows of the pilot grid at `n = 16, 32, 64` and `o = 1, 2`
(all counts matched against the pilot's persisted JSON), plus: the signed
permutation lemma at `h = 4,8,16,32`; the S1 identity; the S1 corollary over
all `phi(n)` choices of primitive root; the S2 identity, inequality and
equality condition (8 deviating rows found, all upward, ratios
`6/5, 4/3, 8/5, 9/8, 40/31, 20/17, 4/3, 2`); S3 firing on 13 rows and
correctly abstaining on all 8 deviating ones; and the stabilizer hypothesis
with its exceptional family exhibited.
