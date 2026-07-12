# Proofs (row-uniform quotient-row ledger, partial packet)

Setting: official row `n = 2^s` (13 <= s <= 41), `k = rho n`,
`rho in {1/2,1/4,1/8,1/16}`, `sigma = 1`, `t = (n-k)/2`; prime field `F`,
`q >= n^2`, `q ≡ 1 (mod n)`; `H <= F^*` cyclic of order `n`. Scale `M = 2^j`,
`2 <= M <= t`; `K = K_M <= H` of order `M`; `n' = n/M`. Intrinsic scale
`c(S) = |Stab_H(S)|` (dyadic). A scale-`M` class member is a codeword
(`deg < k`) whose exact agreement support `S` with the received word `U` has
`c(S) = M` and `|S| = A >= k + sigma`; by the stabilizer partition theorem
(`petal_g2_support_forcing`, PROVED) `S` is a union of `A/M` full `K`-fibers.

Throughout, "the claim's object" is `L_P(U', a)`: for a received word `U'` on
the quotient row `RS[F, H^M, k']` (`k' = k/M`), the number of codewords whose
exact agreement support has size exactly `a = A/M` and is aperiodic in
`H/K ≅ Z_{n'}`.

## Lemma 0 (support-faithfulness; the crux reconciliation)

At every consumed cell of every `M | k` pair, `a >= k' + 1`.

*Proof.* `M | A` (union of full fibers) and `M | k` (dyadic, `M <= k`), and
`A >= k + 1`; a multiple of `M` exceeding `k` is at least `k + M`, so
`a = A/M >= k' + 1`. QED (S2 verifies all 2900 pairs.)

Hence two distinct codewords cannot share an exact support of size `a`
(they would agree on `a > k'` points), so
`L_P(U', a) = #{aperiodic exact supports of size a}` — the list is counted by
supports. The same holds at the original row (`A > k`), which proves the
banked "multiplicity 1 everywhere" as a theorem, and shows the census class
count (distinct supports `S`) EQUALS the codeword count — the dag's note that
"the descent bounds CODEWORD count (stronger than the binding class count)"
is an equality at these cells, not a gap.

Two side corollaries (S2): the edge band `A = k + sigma = k+1` is odd while
`M | A` is even — the edge band is EMPTY for every scale `M >= 2`; the
own-scale band `A <= k + sigma + M - 1 = k + M` collapses to the single cell
`A = k + M`, i.e. `a = k' + 1`.

## T1: the support-count window (unconditional, field-free)

**Claim (single word).** For any received word on the quotient row and any
cell `a >= k' + 1`: `L_P(U', a) <= C(n', a)`.

*Proof.* By Lemma 0 the list injects into the size-`a` subsets of `Z_{n'}`. QED

**Claim (class level, ESP-free, no divisibility needed).** For any `M | n`
(including `M ∤ k`), the scale-`M` class at cell `(M, A)` has at most
`C(n', A/M)` members.

*Proof.* Class member -> its support `S` (injective by Lemma 0's original-row
form, `A > k`); `S` is `K`-invariant, so `S <-> S/K ⊆ Z_{n'}`, `|S/K| = A/M`,
is a bijection onto its image; distinct classes give distinct `S/K`. (That
`S/K` is aperiodic is `cyclic_fiber_interleaving_descent`'s final paragraph;
not needed for the count.) QED

**Numeric window** (S1, exact integers): `max_a C(n', a) <= (63/64) n'^6`
holds for `n' in {2,4,8,16,32}` — at `n' = 32`:
`C(32,16) = 601,080,390 <= 63*32^6/64 = 1,056,964,608` — and FAILS at
`n' = 64` (`C(64,32) ≈ 1.83e18 > 6.76e10`; mutation control M1). At any `n'`,
cells with `a <= 6` or `a >= n' - 6` are covered: `C(n', a) <= n'^6/720`.

So T1 proves the minted claim, uniformly over words and cells, for every
(row, M) with `n' <= 32` — the top four dyadic scales of every official row —
and transports to the ledger's class-level form directly (no ESP, no field
condition).

## T2: the Johnson window (cells `a^2 > (k'-1) n'`)

**Single word.** `petal_k4_johnson_slice` (independently replayed local form
of Paper D v13 `thm:capf-johnson-list(ii)`, which is generic over the
evaluation set — a quotient row qualifies; checked in the v13 source: the
theorem is stated for an arbitrary finite `Omega`, `|Omega| = n_0`, family
with pairwise agreement `<= kappa`) with `T = H^M` (`ell = n'`),
`d = k' - 1`, `N = a`: whenever `a^2 > (k'-1) n'`, the COMPLETE list at
agreement `>= a` — a superset of the aperiodic exact-support-size-`a` list —
has size `<= floor(n'(a-k'+1)/(a^2-(k'-1)n')) <= n'^2 <= (63/64) n'^6`
(`n' >= 2`). In cell terms: `A^2 > (k - M) n`.

**Class level (through the banked chain; the field condition is met).**
`cyclic_fiber_interleaving_descent` (hypotheses: `M | gcd(n,k)` — automatic
here since `n' >= 64` forces `M <= n/64 < k` for every rho; `char F ∤ M` — q
odd; `M | A`) injects the class into the common-support `M`-interleaved list
at agreement `a` with aperiodic-support property `P`. ESP
(`exact_support_interleaving_projection`) applies with `L_P <= n'^2` and
`r = n' - a < n'`:

```text
D = (q-r)^2 - L_P q >= q (q - 2r - L_P) >= q (4n'^2 - 2n' - n'^2) > 0
```

(using `q >= n^2 = M^2 n'^2 >= 4 n'^2`), and the inflation factor is

```text
q(q-r-1)/D <= (q-r-1)/(q - 2r - L_P) <= 4n'^2/(3n'^2 - 2n') = 4n'/(3n'-2) <= 2,
```

decreasing in `q`, so worst at `q = 4n'^2`. Hence class
`<= floor(2 L_P) <= 2 n'^2 <= (63/64) n'^6` for `n' >= 2` (S1, S7 exhibit).

## T3: the large-scale one-fiber lemma (M >= k; new)

**Lemma.** For any dyadic `M` with `k <= M <= t` (no divisibility `M | k`
required), the scale-`M` class has at most `n/M` members.

*Proof.* A scale-`M` support is a nonempty union of full `K_M`-fibers; fix
one fiber `xK_M` inside it. If two class codewords both contain that fiber in
their agreement supports, both agree with `U` on its `M >= k` points, hence
with each other on `>= k` points, hence are equal. The map
class -> (lexicographically first full fiber of its support) is therefore
injective into the `n/M` fibers. QED (S6 verifies it by complete brute
enumeration at (16,6,97), scales 8 and 16.)

This prices the scales `M in (k, t]` — nonempty exactly for `rho = 1/8`
(`M = 2k`) and `rho = 1/16` (`M in {2k, 4k}`) — where the minted claim does
not parse (`k/M` non-integral) and the descent does not apply (catch #111).
Their quotient sizes are `n' in {4, 8}`, so T1's class-level bound also covers
them; T3 gives the stronger linear bound `n/M`.

## Tools checked and found NOT applicable row-uniformly

- `petal_top_band_residual_free_johnson` (list <= m on the band
  `d >= ell(m-2)`): needs the sunflower chart data (petal partition, retained
  residual r = 0) attached to the received word; an arbitrary quotient-row
  word carries none. Its band condition at quotient parameters would even
  hold for `rho = 1/2` (`k'-1 >= n'/2 - 3`), but there is no chart to apply
  it to. Chart-level only.
- `petal_retained_zero_effective_degree`: needs a pinned retained-zero set
  `R` with `R ∩ T = ∅`; no such structure exists uniformly over received
  words. Chart-level only.
- `f2_deep_regime_exactness`: window arithmetic verified (S3) — at the
  minimal official field `q = n^2 = 2^{2s}`, the deep-regime condition
  `q > 2^{(1+eps) n'}` reads `2s > (1+eps) n'`, i.e. only `n' < 2s/(1+eps)`:
  `n' <= 16` for `s <= 16`, `n' <= 32` for `17 <= s <= 32` (both STRICTLY
  inside T1's unconditional window), and `n' = 64` only for `s >= 33` (36
  pairs). Moreover its conclusion is per-prime-window "almost every row"
  (sporadic primes divide fixed nonzero cyclotomic norms) — a row-UNIFORM
  claim cannot consume an almost-every quantifier — and its conclusion is
  F2-extras exactness, not a list bound. Verdict: not consumable here
  (catch #110); the task-sketch's "deep regime covers the top of the M range"
  is arithmetically correct but mathematically moot — T1 already covers that
  top unconditionally.
- Paper D `thm:deep-mca` (deep-regime MCA, soundness below one third of the
  distance): needs agreement `A' >= n' - (n'-k')/3 = (2n'+k')/3`; the
  descended own-band agreement is `k' + 1 << (2n'+k')/3`. High-agreement
  cells that would satisfy it are already inside T2's Johnson window
  (`sqrt((k'-1)n') <= (n'+k'-1)/2 <= (2n'+k')/3` region overlap). Not needed,
  not applicable at the binding cell.

## The open window and why it is exactly the K4 kernel

Uncovered cells: `n' >= 64` and
`a in [max(k'+1,7), min(n'-7, isqrt((k'-1)n'))]` — nonempty at every such
(s, rho, M) (S3), containing the binding own-band cell `a = k'+1` whenever
`k' >= 8`. Any proof would be a sub-Johnson aperiodic list bound at an
official-shaped row (`n' = 2^{s'}, k' = rho n'`) with an oversized field
(`q >= M^2 n'^2`), uniform over words — precisely the open kernel of
`petal_k4_primitive_bound` ("only `N^2 <= d|T|` remains open",
`petal_k4_johnson_slice`), stated at row level. The aperiodicity restriction
is load-bearing and correctly placed: the planted binomial columns of
`v13_capf_planted_lower_count` (the known super-polynomial lower bounds) are
quotient-PERIODIC families, excluded from this count by `c(S') = 1`; no known
construction contradicts the aperiodic `n'^6` form (the banked 372-cell
census shows two-orders-of-magnitude DECAY of count/column ratios). The
oversized field is genuine extra leverage a future proof may use (the
original-row K4 has `q >= n^2` only; here `q >= M^2 n'^2 >> n'^2`), and is
the one structural difference from the original-row kernel.

## Deferred verification

One Modal shard spec with pre-registered expected values in
`qrl_modal_shard_spec.md` (falsification probe at `n' = 64`, the first open
quotient size). Nothing in this packet depends on it.
