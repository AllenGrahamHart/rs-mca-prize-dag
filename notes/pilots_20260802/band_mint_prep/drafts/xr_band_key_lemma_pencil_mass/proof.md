# Proof

Notation as in `statement.md`.

## Claim 1 (THEOREM I, I', corollaries)

**I.** For `x in D` with `v(x) != 0`, the equation
`u(x) + z v(x) = c(x)` has the UNIQUE solution
`z = (c(x) - u(x)) / v(x)` in `F_q`. Summing the agreement indicator
over `(x, z)` in `D x F_q` therefore counts each `x` exactly once:
`sum_z agr(c, w_z) = n`. (Equivalently:
`agr(c, w_z) = |phi_c^{-1}(z)|` for `phi_c : D -> F_q`,
`x -> (c(x) - u(x))/v(x)`; fibres partition `D`.)

**I'.** If `v(x) = 0` the equation reads `u(x) = c(x)`: satisfied for
ALL `q` values of `z` if `u(x) = c(x)`, for none otherwise. Total:
`q e(c) + (n - |Z_v|)`. QED

**I.1.** With `v` nowhere zero, `sum_z agr = n` and each term
`>= a` can occur at most `floor(n/a)` times. **I.2.** If `2a > n`,
two members `z != z'` sharing a codeword `c` with `agr >= a` at each
would give `sum_z agr(c, w_z) >= 2a > n`. QED (1)

*(Note the identity is over `z in F_q`; the `(0:1)` member `v` is
outside the sum — corollaries about "the pencil" quantify over `F_q`
and are stated so.)*

## Claim 2 (KEY LEMMA)

Interpolation on a fixed `S` is `F_q`-linear in the word, so
`I_S(w_z) = I_S(u) + z I_S(v)` exactly, and the top-`(a-k)`
coefficient vector satisfies `top(I_S(w_z)) = A(S) + z B(S)`.
`I_S(w_z)` is a codeword iff its top vanishes (degree `< k`).

- If `A = B = 0`: every member's interpolant on `S` (including
  `z = (0:1)`, whose interpolant is `I_S(v)`) is a codeword;
  `f := I_S(u)` and `g := I_S(v)` are codewords with `u = f`,
  `v = g` on `S` — a joint-explanation event of size `a` (joint
  codeword-pair explanation at depth `a - k`).
- Otherwise `(A, B) != (0, 0)`: `A + z B = 0` has at most one
  solution `z in F_q`, and the `(0:1)` member is a codeword iff
  `B = 0`; in total at most ONE member of `P^1(F_q)` — the affine
  line `{A + zB}` in `F_q^{a-k}` passes through `0` at most once.

If a codeword `c` of member `w_z` has agreement set containing `S`,
then `c` interpolates `w_z` on `S`, so `c = I_S(w_z)` (degree `< a`
interpolant is unique) and `I_S(w_z)` is a codeword. Hence two
DISTINCT members sharing a common agreement `a`-set `S` force
`A(S) = B(S) = 0` — the joint-explanation event — and then all `q+1`
members use `S`. Conversely a joint-explanation event on `S` makes
`f + z g` agree with `w_z` on `S` for every `z`. The graded
consequence and its `a >= A - 1` instance ("below cascade iff no
shared agreement sets at cascade size") follow by definition items
3/5. QED (2)

## Claim 3 (MC-1) and Claim 4 (MC-2)

Setup: `H = x_0 mu_n`, `prod_{x in H} (X - x) = X^n - beta`
(`beta = x_0^n`), `u = X^{n-1} + c X^{k+w-1}`, `c != 0`,
`r' = n - k - w`. Let `P` be a codeword (`deg < k`) and
`e := u - P`, a polynomial of degree exactly `n - 1` (leading
coefficient 1) whose coefficients in degrees `[k, n-2]` are `0`
except `c` at `k + w - 1`.

Suppose `e` vanishes on `H \ T'` for some `T' <= H`, `|T'| = t'`
(i.e. agreement `>= n - t'`). Let
`V_{T'} = sum_{j=0}^{t'} (-1)^j e_j(T') X^{t'-j}` (elementary
symmetric polynomials of `T'`, `e_0 = 1`). Since
`prod_{x in H}(X - x) = X^n - beta`, vanishing on `H \ T'` means
`V_{T'} e = (X^n - beta) G` for a monic `G` of degree `t' - 1`
(degree count: `n - 1 + t' = n + t' - 1`; `t' = 0` forces `e = 0`,
impossible).

**Top window (determines `G`).** Compare coefficients of `X^{n+i}`,
`0 <= i <= t' - 1`. RHS: `G_i`. LHS: `e`'s coefficient `1` at
`X^{n-1}` meets `V_{T'}`'s `X^{t'-j}` at `j = t' - 1 - i`, giving
`(-1)^{t'-1-i} e_{t'-1-i}(T')`; the `c X^{k+w-1}` term would need
`j = t' - 1 - i - r' + (r' - ... ) = k + w - 1 + t' - n - i < 0`
whenever `t' <= r'` (as `k + w - 1 - n = -r' - 1`), and the
`deg < k` part cannot reach degree `n`. So

```text
G_i = (-1)^{t'-1-i} e_{t'-1-i}(T'),   i.e. G is the reversal of V_{T'}.
```

**Claim 4 (MC-2: ceiling).** Suppose agreement `>= k + w + 1`, i.e.
`t' <= r' - 1`. Compare coefficients of `X^{k+w-1+t'}`. RHS:
`X^n G` needs index `k+w-1+t'-n = t' - r' - 1 < 0`; `-beta G` needs
index `k+w-1+t' > t' - 1`: both `0`. LHS: the `c X^{k+w-1}` term
against `V_{T'}`'s leading `X^{t'}` gives `c`; `e`'s zero window
`[k+w, n-2]` kills every other pairing (`d = k+w-1+j`,
`1 <= j <= t'`, lands in `[k+w, k+w-1+t']` with
`k+w-1+t' <= n-2`), and `deg < k` terms cannot reach. So
`c = 0` — contradiction. No codeword agrees on `>= k+w+1` points.
QED (4)

**Claim 3 (MC-1: window classification).** Now `t' = r'` (by MC-2 the
agreement is exactly `k + w`, support exactly `T`, `|T| = r'`).
Compare coefficients of `X^{n-1-s}` for `s = 0, 1, ..., w-1`:

- `s = 0` (`X^{n-1}`): RHS `0` (indices out of `G`'s range as above:
  `X^n G` would need index `-1`; `-beta G` index `n-1 > r'-1`). LHS:
  `X^{n-1}`-term of `e` against `j = r'`: `(-1)^{r'} e_{r'}(T)`; the
  `c`-term against `j = 0`: `c`. Hence
  `e_{r'}(T) = (-1)^{r'+1} c = gamma` — **the product condition**
  (`e_{r'}(T) = prod T`).
- `1 <= s <= w-1`: RHS `0` likewise. LHS: the `c`-term against
  `j = s` gives `c (-1)^s e_s(T)`; the `X^{n-1}`-term would need
  `j = r' + s > r'`; window/degree kill the rest (pairings land in
  `e`'s zero window `[k+w-s-1+1, k+w-2]`... precisely: `d = k+w-1-s+j`
  for `0 <= j < s` lies in `[k+w-1-s, k+w-2]`, inside the zero
  window since `s <= w-1` gives `k+w-1-s >= k`). Hence
  `e_s(T) = 0` for `s = 1..w-1` — **the window conditions**.

Conversely, given `T` with the `w` conditions, set `G` := the reversal
of `V_T`; then `(X^n - beta) G = V_T V_{H\T} G` is divisible by
`V_T`, and `e := V_{H\T} G` has degree `n-1`, leading coefficient 1,
and satisfies the same coefficient identities; the `w` conditions are
exactly the requirement that `u - e` has degree `< k` (dimension
count: `e` is determined by `T`'s `r'` symmetric functions through the
top window; the remaining `w` window equations are the derived
conditions). So `P_T := u - e` is a codeword agreeing with `u`
exactly off `T`, computable as `P_T = (u V_T mod (X^n - beta)) / V_T`
— the verifier's construction. Injectivity: `T` = the non-agreement
set of `P_T`. Exactness of agreement is MC-2. QED (3)

*(The mechanism — the locator factorization and the coefficient
window — is the banked `e22_tail_coset_locator_algebra` / crossing
PK1 algebra; the general-`w` statement and ceiling are what this node
adds. Machine-checked exhaustively; the pilot's own record is 161 + 30
+ 3,571 checks across shapes and fields.)*

## Claim 5 (MC-3: exact `q`-free count)

A `mu_M`-coset of `H` is `{x_0 omega^i mu : mu in mu_M}` with
`omega` a generator of `mu_n`; cosets correspond to residues
`i mod N`, `N = n/M`. The banked `e22` factorization gives
`e_1 = ... = e_{M-1} = 0` for any union of full cosets (the coset
vanishing polynomial is a polynomial in `X^M`, so `V_T = G_T(X^M)`
up to the stated form, and the low elementary symmetric functions
vanish). For the product: the product over one coset equals
`(x_0 omega^i)^M prod(mu_M) = (-1)^{M+1} (x_0 omega^i)^M`, so the
product over a union indexed by an `m`-subset `S` of `Z/N` is
`(-1)^{m(M+1)} x_0^{mM} (omega^M)^{sum S}` — it depends on `S` only
through `sum S mod N` (`omega^M` has exact order `N`). The product
condition `prod T = gamma` therefore reads `sum S = t_0 (mod N)` for
a fixed `t_0`. When `gcd(m, N) = 1` the shift `S -> S + 1` changes
the sum by the unit `m`, so the `C(N, m)` subsets fall into `N`
classes of EXACTLY `C(N,m)/N` each (the shift action's orbits hit
every residue equally; this is PK1 Lemma 5's equidistribution). The
count is independent of `q` — `q`-free. QED (5)

## Claim 6 (MC-5: no pencil exclusion)

`X` is invertible mod `X^n - beta` (`gcd = 1`), so
`v := u / X^j mod (X^n - beta)` satisfies `v(x) = u(x) x^{-j}` on
`H`. The banked factorization gives `X^{M-1} | P_T`, so for
`j <= M-1`, `Q_T := P_T / X^j` is a polynomial of degree `< k` with
`Q_T(x) = P_T(x) x^{-j}` on `H`. For any `z in F_q`:
`w_z - (P_T + z Q_T) = (u - P_T) + z (v - Q_T)`, and both summands
vanish off `T` (`v - Q_T = (u - P_T) x^{-j}` pointwise), so
`P_T^{(z)} := P_T + z Q_T` is a codeword of `w_z` with agreement
`>= n - r' = k + w`. The `(0:1)` member `v` admits `Q_T` likewise.
Hence every member admits the entire family and
`min_{z in P^1} L(w_z, k+w) >= C(N,m)/N`. QED (6)

## Honest scope

Claims 1-2 are complete elementary proofs, domain-agnostic. Claims
3-6 are complete modulo the banked coset-locator algebra (`e22`,
PK1), cited not re-derived per hard law 5; every constructive step is
machine-checked exhaustively in `verify.py` on fresh code. The
retired-reduction context (why this node must not be read as a list
bound) is recorded in `statement.md`; the (R1) first-moment half of
the pilot's refutation is NOT part of this node's claims.
