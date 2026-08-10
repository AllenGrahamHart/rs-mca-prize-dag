# MINT PACKAGE — slack_recursion (round 29), draft for the coordinator's mint queue

Four statements. A and B together **pin the model's arbitrary-word supply
maximum inside one bit at every scale**; C explains why the banked
F_SUBSET proxy degenerates; D corrects the round-28 recursion note.
Everything below is proved here and verified by the harness pointers.

## Setting (the object rounds 27/28 measured)

`n = 2^r`, `D = mu_n subset F_q` (`q` prime, `q = 1 mod n`), `k = n/2`,
`t = 1`, `a = k + t = n/2 + 1`, `m = n - a = n/2 - 1`.
`C = RS[n,k]` = evaluations on `D` of polynomials of degree `< k`.
For a received word `y in F_q^n`:

```text
F_LIST(y)   = #{ f : deg f < k, agree(y,f) >= a }        (the supply object)
F_SUBSET(y) = #{ A subset D : |A| = a, y|_A in P_{<k}|_A }   (the banked proxy)
PLATEAU(n)  = C(n/2-1, n/4)          (the slack-0 / theorem-cap maximum)
MAXWORD_LIST(n) = max over ALL received words y of F_LIST(y)
```

Dedup law (banked, round 27): `F_SUBSET = sum_j m_j C(j,a)`, `m_j` = number
of listed codewords of agreement exactly `j`. Hence `F_LIST <= F_SUBSET`.

---

## THEOREM A (PRODUCT WORD — the maximiser)

Let `c in F_q^*` and let `y` be the received word

```text
y(x) = x^{-1} + c * x^{n/2}          (x in mu_n),
i.e.  Y(X) = X^{n-1} + c X^{n/2},    deg Y = n - 1 = a + (m-1):  MAXIMAL SLACK.
```

Then

```text
(A1)  A is an agreement set of size a  <=>  prod_{x in A} x = -1/c ;
(A2)  every listed codeword has agreement EXACTLY a (the profile is flat);
(A3)  F_LIST(y) = F_SUBSET(y) = #{A : |A| = a, prod x = -1/c} = C(n,a)/n .
```

**Proof.** *(A1)* `A` (with `|A| = a`) is an agreement set iff the unique
interpolant of `y` on `A`, of degree `< a`, has degree `< k = a-1`, i.e. iff
its leading coefficient vanishes. By Lagrange that coefficient is
`sum_{x in A} y(x)/L'_A(x)` with `L_A(X) = prod_{x in A}(X-x)`.
Two evaluations:

* `sum_{x in A} x^{a-1}/L'_A(x) = 1` (the standard identity: the sums
  `sum_x x^j/L'_A(x)` vanish for `j <= a-2` and equal 1 for `j = a-1`), and
  `a-1 = k = n/2`, which is exactly the exponent of the second term;
* `h(X) := (L_A(0) - L_A(X))/(X L_A(0))` has degree `a-1` and satisfies
  `h(x) = 1/x` for every `x in A`, so it IS the interpolant of `x^{-1}`;
  its leading coefficient is `-1/L_A(0)`, and `L_A(0) = (-1)^a prod x
  = -prod x` since `a = n/2+1` is odd. Hence
  `sum_{x in A} x^{-1}/L'_A(x) = 1/prod_{x in A} x`.

So the leading coefficient is `1/prod_{x in A} x + c`, and it vanishes iff
`prod_{x in A} x = -1/c`. ∎(A1)

*(A2)* If a listed codeword `f` had agreement `R` with `|R| >= a+1`, then
every `a`-subset of `R` would be an agreement set, so by (A1) any two
`a`-subsets of `R` differing in one element would have equal products,
forcing the two swapped elements to be equal — contradiction. ∎(A2)

*(A3)* By (A2) the map (agreement set) -> (codeword) is a bijection onto the
list, so `F_LIST = F_SUBSET = #{A : prod = -1/c}`. Writing `A = {g^i : i in I}`
for a generator `g` of `mu_n`, the condition is `sum I = s (mod n)`. Rotation
`I -> I+1` shifts `sum I` by `a`, and `gcd(a,n) = 1` because `a` is odd and
`n` is a 2-power; so rotation permutes the `n` residue classes transitively
and all classes have the same size `C(n,a)/n`. ∎

**Corollary.** `MAXWORD_LIST(n) >= C(n, n/2+1)/n` for every `n = 2^r`,
with the maximiser explicit, char-0 (independent of `q`), and with all
agreements exactly `a`.

*Relation to the literature (subtraction, hard law 5).* The **code** here —
`a`-subsets with prescribed index-sum mod `n` — is the classical
Graham-Sloane construction for binary constant-weight codes of minimum
distance 4 (`A(n,4,w) >= C(n,w)/n`). Own-repo grep: the repo carries
constant-weight/Johnson language in the L1 background layer
(`l1_background_quotient_johnson_bound`, `l1_joint_plotkin_boundary_payment`)
but **no** occurrence of this construction, of "prescribed product", or of
Graham-Sloane. What is new here is (i) that a **single explicit received
word** realises that code as its list, through the `x^{-1}` interpolation
identity, and (ii) Theorem B.

## THEOREM B (matching upper bound — the model's supply is pinned to 1 bit)

```text
MAXWORD_LIST(n) <= C(n, a-1)/a = 2 * C(n,a)/n .
```

**Proof.** Let `f_1..f_L` be a list for `y`, with full agreement sets
`R_i`. Distinct codewords of degree `< k` agree in at most `k-1 = a-2`
points, so `|R_i cap R_j| <= a-2`. Choose any `a`-subset `A_i subset R_i`;
then `|A_i cap A_j| <= a-2`, i.e. `{A_i}` is a binary constant-weight-`a`
code of minimum distance 4. No `(a-1)`-subset lies in two different `A_i`
(that would force `|A_i cap A_j| >= a-1`), and each `A_i` contains `a` of
them, so `L*a <= C(n, a-1)`. Finally
`C(n,a-1)/a = C(n,a) * (a/(n-a+1)) / a = C(n,a)/(n/2) = 2C(n,a)/n`. ∎

**Consequence (with A).** `C(n,a)/n <= MAXWORD_LIST(n) <= 2C(n,a)/n`:
the arbitrary-word supply maximum is determined **within one bit at every
scale**, and equals the lower end exactly at `n = 8` (7, by exhaustion over
every received word at `q = 73, 97, 113`).

## THEOREM C (why the banked F_SUBSET proxy degenerates at high slack)

The Hamming-distance-1 word `Y = f + c(X^n-1)/(X-u)` has slack `m-1`
(maximal), word class `W(z) = sum_{j<=m} u^j z^j`, and

```text
F_SUBSET = C(n-1, a),   F_LIST = 1,   AGRPROF = {n-1 : 1}.
```

**Proof.** `Y - f` vanishes on `D\{u}`, so the single codeword `f` has
agreement `n-1` and contributes `C(n-1,a)` `a`-subsets; any second listed
codeword `f'` would satisfy `agree(f,f') >= (n-1) + a - n = k`, forcing
`f = f'`. ∎

So `max_y F_SUBSET(y) >= C(n-1,a)` with a list of size **one**: comparing
`F_SUBSET` values ACROSS slack strata is confounded by the `C(j,a)`
inflation factors, and the supply object must be `F_LIST`.
(Measured, exhaustively at `n = 8`: `max_y F_SUBSET = 21 = C(7,5)` exactly,
3 fields; at `n = 16`: 5005 = C(15,9) with `F_LIST = 1`, 2 fields.)

## THEOREM D (the round-28 recursion note, corrected)

Notation of the banked parity theorem: `n = 2M`, `M = 2K`, `omega` of order
`M`, `rho = omega^2` of order `K`; `S` inside the even pair class,
`S = {2u : u in U}`, `U subset [0,K)`, signs `sigma`.

* **REC-STRONG (the round-28 one-line note, read literally): FALSE.**
  It would say that the parity theorem re-applies to `E' = E|_{even class}`
  against the level-`n` target equation `E' - omega_T = c`, forcing `U`
  into a single level-`M` parity class and iterating the `s <= n/4`
  stratum ceiling. Refuted by explicit counterexamples: at `n = 32`,
  **88 of the 103 contributing even-class nodes** have `U` meeting both
  parities (e.g. `U = {0,1,2}`, contributing 6 to the total 1974); at
  `n = 16`, 4 of 7.

* **REC-BOX (what is actually true, proved).** Splitting `Z[omega] =
  Z[rho] + omega Z[rho]`, the odd component of `E'` is `omega X'' Y''` with
  `X'' = sum_{u in U even} sigma_u rho^{u/2}`,
  `Y'' = sum_{u in U odd} sigma_u rho^{(u-1)/2}`, while the odd component
  of `omega_T` is `omega * sum_j d_{2j+1} rho^j` with `d in {-1,0,1}^K`.
  Hence the equation forces only

  ```text
  X'' * Y''  lies in the {-1,0,1}-coefficient box of Z[rho].
  ```

  The reason REC-STRONG fails is exactly that the level-`M` T-part of a
  genuine level-`M` problem uses only the even powers `rho^j`, whereas the
  level-`n` restricted problem keeps all `K` powers `omega^i`.

* **Reduction factor, measured** (`BOXFRAC` = fraction of enumerated
  even-class nodes passing REC-BOX): `1.000` (n=8), `0.802` (n=16),
  `0.366` (n=32) — prune factors 1.0, 1.25, 2.7. Extrapolating, the
  `n = 128` antipodal scan stays at `~10^13` nodes: **Modal-class and
  dead**, and in any case of ~zero decision value now (the delta=1 branch
  is decided at four scales and, by Theorem A, is not where the supply
  maximum lives).

## Verification harness

All under `notes/pilots_20260810/slack_recursion/`:

| claim | script (scratch/) | data (data/) |
|---|---|---|
| A, at n=8/16, 2-3 fields, flat profile | `sr_product.py prod` | `prodword_16_*.json` |
| A+B, exact all-word max at n=8 (t=1,2,3) | `sr_product.py allw`, `sr_words.py n8all` | `n8_allwords.json`, `allw_8_*_t*.json` |
| A, maximiser identified as the product word | `sr_n8struct.py` | `n8_maximizer_structure.json` |
| C, distance-1 word, banked instrument | `sr_deg1.py` (imports `nf_probe_copy`) | `t2_distance1.json` |
| D, REC-STRONG/REC-BOX/BOXFRAC | `sr_rec.py` | `d1_recursion.json` |
| trend table (exact integers, n=8..256) | `sr_trend.py` | `supply_trend.json` |
| escape replays (6/46/1974; 349/67; 2054/53) | `ms_exact_copy.py`, `sr_words.py word` | `escape1_msexact.json`, `escape2_w*.json` |
| locator ladder, orbit-exhaustive, 2 fields | `sr_words.py nloc` | `locladder_16_*.json` |
