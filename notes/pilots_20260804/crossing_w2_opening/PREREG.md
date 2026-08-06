# PRE-REGISTRATION — crossing at w >= 2 (MYSTERY 4 opening)

Written BEFORE any computation. Round 14, 2026-08-06.

## Object under study

From `background/nodes/xr_band_key_lemma_pencil_mass` MC-1 (PROVED,
general `w`): with `H = x_0 mu_n` (`n | q-1`, split),
`u = X^{n-1} + c X^{k+w-1}`, `c != 0`, `r' = n-k-w`, the codewords of
agreement `>= k+w` with `u` are EXACTLY indexed by

```text
{T <= H : |T| = r', e_1(T) = ... = e_{w-1}(T) = 0, prod T = gamma},
gamma = (-1)^{r'+1} c.
```

Write `T = T(S) = {x_0 zeta^i : i in S}` for `S <= Z/n`, `|S| = r'`,
`zeta` a fixed generator of `mu_n <= F_q^*`. Define the WINDOW SET

```text
W_w := {S <= Z/n : |S| = r', e_s(T(S)) = 0 for s = 1..w-1}
```

(`W_1` = ALL `r'`-subsets, no condition) and `sig(S) := sum_{i in S} i mod n`.
The crossing count is `X_w(gamma) := #{S in W_w : prod T(S) = gamma}`.

## Pre-registered claims (to be proved and machine-checked)

- **(X) product equidistribution, general `T`, all `w`.** `W_w` is invariant
  under the rotation `rho: S -> S+1`, and `sig(rho S) = sig(S) + r'`.
  With `d := gcd(r', n)`, the fibres of `sig` over any two residues in the
  SAME class mod `d` have EQUAL size; hence
  `X_w(gamma) = (d/n) * #{S in W_w : sig(S) = j mod d}` for the class `j`
  determined by `gamma`, and `X_w(gamma) = 0` unless
  `gamma / x_0^{r'} in mu_n`. Special case `d = 1`: `X_w = |W_w| / n` exactly.
  MC-3's Lemma-5 step is the coset-restricted instance.
  **Falsifier:** two same-class `sig`-fibres of different size.

- **(Q) q-collapse: the w >= 2 dependence is on `p = char F_q` ONLY.**
  All `e_s(T(S))` lie in `F_p(mu_n) = F_{p^delta}`, `delta = ord_n(p)`,
  a subfield of every admissible `F_q`; vanishing there is unchanged in any
  extension. Hence `|W_w|` and the whole `sig`-fibre profile depend on `q`
  only through `p` (given `n, r', w`), never on the extension degree `e` in
  `q = p^e`. Choice of `zeta` permutes the profile by `S -> aS` only.
  **Falsifier:** two fields `q = p^{e1}, p^{e2}` (same `p`, both with
  `n | q-1`) giving different `|W_w|` or different fibre multiset.

- **(Y) Newton/BCH linearization, valid iff `w <= p`.** For `char p > w-1`,
  Newton's identities give
  `e_1 = ... = e_{w-1} = 0  <=>  p_1 = ... = p_{w-1} = 0`,
  and `p_s(T(S)) = x_0^s * chi_S(zeta^s)` with `chi_S(X) = sum_{i in S} X^i`
  the 0/1 indicator polynomial. Hence

  ```text
  W_w = {weight-r' 0/1 vectors in the cyclic code of length n over F_p
         with defining zeros zeta, zeta^2, ..., zeta^{w-1}}
  ```

  i.e. a CONSTANT-WEIGHT COUNT IN A BCH CODE of designed distance `w`.
  **Falsifier (pre-registered, expected to FIRE):** at `p = 2, w = 3` the
  Newton step is invalid (`2 e_2 = p_1^2 - p_2` degenerates), so the BCH
  set should STRICTLY CONTAIN `W_3`. I predict a measured mismatch there.

- **(S) structural / accidental split.** `E_s(S) in Z[zeta_n]` (char-0 lift).
  `W_w = W_w^{struct} (E_s(S) = 0 in char 0)  UNION  W_w^{acc}
  (E_s(S) != 0 but P | E_s(S))`. Predict `|W_w| >= |W_w^{struct}|` for every
  `p`, with equality for all `p` above a finite bound `B(n, r', w)`.
  **Falsifier:** a `p` with `|W_w| < |W_w^{struct}|`.

- **(P) w = 1 contrast (PK1 recovery).** `W_1` = all `C(n, r')` subsets;
  by (X), `X_1 = (d/n) C(n,r')_{class j}` — no field equation is imposed at
  all, so the count is q-free. This is the exact mechanism separating
  `w = 1` from `w >= 2`.
  **Falsifier:** any measured `w = 1` count varying with `p`.

- **(V) MC-1 replay.** Independent brute-force census of codewords at
  agreement `>= k+w` must equal `X_w(gamma)` from the window side, and no
  codeword at `>= k+w+1` (MC-2).
  **Falsifier:** any mismatch.

## Pre-registered measurement plan (all `tiny`, pure python)

1. Direct census: enumerate all degree-`<k` codewords over small `F_q`,
   measure agreement with `u`; compare with the window count. (V)
2. Window-set enumeration over `S <= Z/n` for small `n`, `w = 2, 3`,
   sweeping primes `p` with `n | p-1` and extensions `p^e`. (Q), (Y), (S)
3. `sig`-fibre profile for every case, test (X).
4. char-0 structural count via exact arithmetic in `Z[X]/(Phi_n)`. (S)

## Subtraction (hard law 5) — declared BEFORE measuring

- The coset mechanism, MC-1/2/3/5, the `e22` locator factorization, PK1's
  Lemma 5 equidistribution: ALL BANKED, cited not re-derived.
- Newton-identities linearization (locator prefix <-> power sums, with the
  `d < p` caveat and the Frobenius-checkpoint repair) is BANKED IN THE L1
  LANE: `critical/nodes/l1_mixed_petal_amplification/statement.md` lines
  376-404 (`l1_official_newton_cofactor_window_router`,
  `l1_official_frobenius_checkpoint_q_router`). NOT claimed as new.
- "BCH-type low-weight window" / "lie in the explicit Mersenne cyclic code"
  is BANKED for a DIFFERENT object (L1 Mersenne collision words):
  same file lines 968-995, `l1_mersenne_checkpoint_cyclotomic_normal_form`,
  `l1_m4_h3_colored_cyclic_equivalence`. NOT claimed as new.
- What this pilot claims as new is only: the TRANSFER of that mechanism to
  the CROSSING lane's MC-1 window system, the general-`T` equidistribution
  (X), and the q-collapse (Q). No "weight enumerator"/"weight distribution"
  string exists anywhere in the repo (checked); the constant-weight-in-BCH
  identification of the crossing count is not present in the crossing lane.
