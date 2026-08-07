# PROOFS — the COPRIMALITY MECHANISM behind (ES)

Round 17, 2026-08-06. Opus pilot, `notes/pilots_20260806/es_coprimality/`.
Everything here is registered in `PREREG.md` §Q0-Q6 **before** computation.
Machine-checked by `verify_cop.py` (fail-closed, exit nonzero on failure)
and `prize_floor.py`.

---

## §0. Setup

`n = 2^m`, `h = n/2 = phi(n) = [K:Q]`, `K = Q(zeta_n)`, `O_K = Z[zeta_n]`,
`Phi_n(X) = X^h + 1`. `S <= Z/n`, `|S| = r'`. For `s in Z/n`

```text
x_s = sum_{i in S} zeta^{s i}  in  O_K,      I_S = (x_1,...,x_{w-1}) <= O_K,
N(I_S) = [O_K : I_S]   (N(0) = 0, N(O_K) = 1).
```

`delta = ord_n(p)`; `Z_w` = the `p`-cyclotomic closure of `{1,...,w-1}` mod
`n`; `Z_w^odd = {s in Z_w : s odd}`; `a_{n/2}(S) = #{(i,j) in SxS :
i-j = n/2 mod n}`; `strat(S) = max{a >= 0 : S + n/2^a = S}`.

**The census identity** (round 16, method M1), quoted verbatim from
`notes/pilots_20260806/es_boundary_adversary/es_lib.py:23-28`:

> ```
>     S is a solution in characteristic p for SOME choice of primitive n-th
>     root of unity in F_{p^delta}
>       <=>  some prime P | p contains every x_s
>       <=>  gcd( Phi_n, V_1, ..., V_{w-1} )  has degree >= 1  in F_p[X]
>       <=>  p | N(I_S),   I_S = (x_1, ..., x_{w-1}) <= O_K.
> ```

**The lead being formalized**, verbatim from
`notes/pilots_20260806/es_boundary_adversary/REPORT.md:88`:

> **(C4-c) Generic coprimality is the real suppressor.** Accidents
> require the ideals (x_1,…,x_{w-1}) to share a prime; for w ≥ 3 the
> gcd of norms collapses to 1 for almost every orbit. This — not
> entropy — is why the crossing shape is clean over all p, and it is the
> structural reason suppression beats the entropy prediction wherever it
> does.

---

## §1. Facts CITED, not claimed (subtraction, hard law 5)

**(B1) LEMMA Z.** `critical/nodes/b1_char0_giant_coset_theorem/node.json:9`,
status `PROVED`, verbatim opening:

> "Over characteristic zero: every 0/1 t-null vector on mu_n (n = 2^s) is a
> union of mu_M-cosets with M > t."

**(B2) The elementary norm gate NG1.**
`notes/U1_OFFICIAL_ROW_NORM_GATE_TABLE.md:19-25`, verbatim:

> Let `K` be a number field, `u` a nonzero algebraic integer, and `p` a row
> characteristic.  If `r` distinct prime ideals of `O_K` above `p` divide
> `(u)`, then
>
> ```text
> p^r divides |Norm_(K/Q)(u)|.                         (NG1)
> ```

**(B3) The archimedean ceiling.**
`background/nodes/f3_h3_low_distance_ideal_star_router/statement.md:44-48`,
status `PROVED`, verbatim:

> ```text
> p divides N(K_(E;F,G))
>   divides gcd(|Norm((beta_F-beta_E)/pi^2)|,
>               |Norm((beta_G-beta_E)/pi^2)|)
>   <= 6^(n/4)/4.                                      (ISR4)
> ```

**(B4) The ideal-index reduction.**
`background/nodes/dli_wcl_ell2_weight5_pair_ideal_index_obstruction/proof.md:36-52`,
status `PROVED` — the `J <= ker(O -> F_q) => q | [O:J]` step plus the
Smith-normal-form identification of the index. Used verbatim as the
justification that `N(I_S)` is computable as a lattice index.

**(B5) Lam-Leung / Conway-Jones is EXHAUSTED at `n = 2^m`.**
`critical/nodes/dli_prime_weighted_large_block_support/notes/S5_LAM_LEUNG_TRANSPORT.md:1`,
verbatim title:

> `# S5: the Lam–Leung / Conway–Jones transport — resolved (empty at n′ = 2^s)`

**(B6) The standing open lemma this pilot attacks.**
`background/nodes/u1_x4_direct_column_budget/notes/F3_SHALLOW_LADDER.md:200-202`,
verbatim:

> ```
> boundary, dying with q). ONE open lemma (pair-coprimality / norm-gate
> sparsity) stands between the data and the theorem — shared verbatim
> with F2's accident story.
> ```

**(B7) Provenance of "generically coprime".**
`background/nodes/u2c_giant_tnull_dichotomy/node.json:8` — status
`CONDITIONAL`, verbatim fragment:

> `1440 trials, positively controlled against the known p=257 window accident) finds ZERO candidate sub-balance primes — the multi-condition ideals are generically coprime; the engineering channel is structurally empty, mirroring the E2 finding.`

This is an **empirical survival credit on a CONDITIONAL node**, not a
theorem. Nothing in the repository proves `N(I_S) = 1` generically.

---

## §2. LEMMA TWO — the 2-adic normalization (CATCH-17A)

> **LEMMA TWO.** Let `pi = 1 - zeta`, the unique prime of `O_K` above 2
> (totally ramified, `pi^h ~ 2`). Then for every `s`,
> `x_s = r' (mod pi)`. Consequently
> * if `r'` is EVEN, `pi` divides every `x_s`, so `I_S <= pi` and
>   `2 | N(I_S)` — **`N(I_S) = 1` is impossible**;
> * if `r'` is ODD, `N(I_S)` is odd.

**Proof.** `zeta = 1 (mod pi)`, hence `zeta^{si} = 1 (mod pi)` for all
`s, i`, hence `x_s = sum_{i in S} 1 = r' (mod pi)`. If `2 | r'` then
`pi | r'` (as `pi | 2`) so `pi | x_s` for every `s`, so `I_S <= pi` and
`N(pi) = 2` divides `N(I_S)`. If `r'` is odd then `x_1 = 1 (mod pi)`, so
`pi` does not contain `x_1`, so `pi` does not contain `I_S`; since `pi` is
the ONLY prime above 2, `2` does not divide `N(I_S)`. QED

**Consequence for the conjecture.** The correct invariant is the **ODD
part** `N_odd(I_S)`. This is not cosmetic: at the prize crossing rows
`r' = 2^40 - w` is even for every `w >= 2`, so `N(I_S) = 1` is FALSE at
every prize row while `N_odd(I_S) = 1` is exactly the right statement.
`p = 2` is ramified and is excluded from every (ES) row, so nothing is
lost. **My own first draft of (K1) in `PREREG.md` §Q1 said `N(I_S) = 1`
and was wrong; LEMMA TWO is the repair, found by the measurement, and I
record the correction rather than quietly restating the conjecture.**

*Machine check:* `verify_cop.py rate` checks `v_2(N(I_S)) > 0 <=> r' even`
on every orbit of every measured row — **75,806 checks, 0 failures**.

---

## §3. LEMMA STRAT — the stratum reduction

> **LEMMA STRAT.** Suppose `strat(S) >= a >= 1`, i.e. `S` is
> `(n/2^a)`-periodic. Put `n_a = n/2^a`, let `S' <= Z/n_a` be the
> reduced set (`|S'| = r'/2^a`), `K_a = Q(zeta_{n_a})`, and
> `iota : K_a -> K` the inclusion `zeta_{n_a} |-> zeta^{2^a}`. Then
>
> 1. `x_s = 0` whenever `2^a` does not divide `s`;
> 2. `x_{2^a t} = 2^a * iota(p_t(S'))` where `p_t(S') = sum_{j in S'} zeta_{n_a}^{t j}`;
> 3. `I_S = 2^a * iota(I_{S'}) O_K` with `w' = floor((w-1)/2^a) + 1`;
> 4. the ODD primes dividing `N(I_S)` are EXACTLY the odd primes dividing
>    `N_{K_a/Q}(I_{S'})` at the reduced instance `(n_a, r'/2^a, w')`.

**Proof.** (1)+(2): group `S` into `mu_{2^a}`-cosets. For a coset with
representative `i_0`,
`sum_{j=0}^{2^a-1} zeta^{s(i_0 + j n_a)} = zeta^{s i_0} sum_j eta^{sj}`
where `eta = zeta^{n_a}` is a primitive `2^a`-th root of unity. The inner
geometric sum is `2^a` if `2^a | s` and `0` otherwise. Summing over cosets
gives (1), and for `s = 2^a t` gives
`x_s = 2^a sum_{i_0} (zeta^{2^a})^{t i_0} = 2^a iota(p_t(S'))`.
(3): the surviving generators are exactly `s in {1,...,w-1}` with
`2^a | s`, i.e. `s = 2^a t` with `1 <= t <= floor((w-1)/2^a)`, so
`I_S = (2^a iota(p_1(S')), ..., 2^a iota(p_{w'-1}(S')))`.
(4): `N(I_S) = N(2^a)^{?} * N(iota(I_{S'}))`; concretely
`N_{K/Q}(2^a O_K) = 2^{a h}` and `N_{K/Q}(iota(J)) = N_{K_a/Q}(J)^{[K:K_a]}`
for any ideal `J` of `O_{K_a}` (the extension `K/K_a` is unramified at
every odd prime because only 2 ramifies in `K/Q`). Raising to the power
`[K:K_a]` and multiplying by a power of 2 changes neither the set of odd
prime divisors nor their presence. QED

**What this delivers for (K1).** It answers the mandate's question *"the
conjecture should predict WHICH strata carry the exceptional class"*
exactly:

* `a >= log2 M` (`M` = least power of two `>= w`): then `w' = 1`, there
  are no conditions, `I_S = 0`, `N(I_S) = 0` — this is the **structural**
  family of LEMMA Z, not an exception.
* `1 <= a < log2 M`: the instance collapses to `(n/2^a, r'/2^a, w')` with
  `w' = floor((w-1)/2^a)+1 << w`. **The binding stratum is the largest `a`
  with `w' = 2`**, because at `w' = 2` the reduced ideal is PRINCIPAL,
  `N(I_{S'}) = |N(x'_1)| >> 1`, and non-coprimality is generic.
* `a = 0`: the generic case, governed by THEOREM CS below.

*Machine check:* `verify_cop.py strat` — 80 stratified fixtures at
`n in {16,32}`, `a in {1,2}`: identities (1),(2) exact, and the odd
prime supports of `N(I_S)` and `N(I_{S'})` equal in every case —
**240 checks, 0 failures**.

*Both deep round-16 witnesses are explained by this lemma.* The measured
factorizations (`verify_cop.py wit`) are
`N(I_S) = 2^16 * 7^4` reducing to `n=16, S'={0,2,5}, w'=2, N = 7^2`, and
`N(I_S) = 2^16 * 17^2` reducing to `n=16, S'={0,1,3}, w'=2, N = 17`.
Both reduced instances have `w' = 2` — a **principal** ideal. That is the
mechanism behind round-16's `(C4-a)`: the deep witnesses are not deep,
they are a `w = 2` problem wearing a `w = 4` costume.

---

## §4. THEOREM CS — the coprimality norm floor

This is the pilot's main asset, and the answer to (K2).

> **THEOREM CS.** Let `n = 2^m`, `p` an odd prime, `delta = ord_n(p)`,
> `S <= Z/n` with `|S| = r'` and `x_1 != 0`. If `p | N(I_S)` then
>
> ```text
> p^{|Z_w^odd|}  divides  |N_{K/Q}(x_1)|                            (CS1)
> ```
>
> and, unconditionally,
>
> ```text
> |N_{K/Q}(x_1)|^2  <=  ( r' - a_{n/2}(S) )^h ,   h = n/2.          (CS2)
> ```
>
> Hence
>
> ```text
> |Z_w^odd| * log2 p  <=  (n/4) * log2( r' - a_{n/2}(S) ).          (CS3)
> ```
>
> Moreover `|Z_w^odd| >= ceil((w-1)/2)` **uniformly in `delta`**, so
>
> ```text
> ceil((w-1)/2) * log2 p  <=  (n/4) * log2 r'.                      (CS4)
> ```

### Proof of (CS1)

**Step 1 (Frobenius closure).** By the census identity, `p | N(I_S)` means
some prime `P` of `O_K` above `p` contains every `x_s`, `1 <= s <= w-1`.
Since `n` is a power of two and `p` is odd, `p` is unramified in `K`, and
`K/Q` is abelian with `Gal(K/Q) = (Z/n)^*` via `sigma_c(zeta) = zeta^c`.
The Frobenius at `P` is `sigma_p`, and `sigma_p(P) = P`. Now
`sigma_p(x_s) = sum_{i in S} zeta^{p s i} = x_{ps}`. So `x_s in P` implies
`x_{ps} in sigma_p(P) = P`. Iterating, **`P` contains `x_s` for every
`s in Z_w`** — the `p`-cyclotomic closure. (This is precisely why `|Z_w|`,
not `w-1`, is the exponent in round-15's balance functional `Lam`.)

**Step 2 (odd indices are Galois conjugates of `x_1`).** For `s` odd,
`s in (Z/n)^*` and `sigma_s(x_1) = sum_{i in S} zeta^{si} = x_s`. Hence
for every `s in Z_w^odd`,
`x_1 = sigma_s^{-1}(x_s) in sigma_s^{-1}(P)`.
So `x_1` lies in the prime `P_s := sigma_s^{-1}(P)` for **every**
`s in Z_w^odd`.

**Step 3 (counting the distinct primes).** `P_s = P_t` iff
`sigma_{s t^{-1}}(P) = P` iff `s t^{-1}` lies in the decomposition group
of `P`, which for `K/Q` abelian is `<p> <= (Z/n)^*`, of order `delta`.
Multiplication by `p` preserves parity (`p` odd), so `Z_w^odd` is a union
of `<p>`-cosets; `<p>` acts freely on `(Z/n)^*` by translation, so every
coset has exactly `delta` elements. Therefore the primes `{P_s}` are
`r := |Z_w^odd| / delta` **distinct** primes above `p`, each of residue
degree `delta`.

**Step 4 (the norm).** Distinct primes are coprime, so
`prod_{i=1}^{r} P_i` divides `(x_1)`, whence
`prod_i N(P_i) = (p^{delta})^{r} = p^{|Z_w^odd|}` divides
`|N_{K/Q}(x_1)|`. (This is (B2)/NG1 refined by the residue degree; the
NEW ingredient is Step 3 — the identification of the multiplicity `r`
with the **window's Galois orbit count**. Round-16's registered M3
`es_boundary_adversary/PREREG.md:169-172` uses ONE prime and obtains
exponent `delta`; the upgrade `delta -> |Z_w^odd|` is this pilot's.) QED

### Proof of (CS2)

The embeddings of `K` are `sigma_c`, `c` odd mod `n` — there are `h = n/2`
of them — and `sigma_c(x_1) = x_c`. Compute the second moment exactly:

```text
sum_{c odd mod n} |x_c|^2 = sum_{c odd} sum_{i,j in S} zeta^{c(i-j)}.
```

For fixed `d = i-j`, `sum_{c=0}^{n-1} zeta^{cd} = n*[d=0]` and
`sum_{c even} zeta^{cd} = (n/2)*[d = 0 or d = n/2]`, so
`sum_{c odd} zeta^{cd} = (n/2)([d=0] - [d=n/2])`. Therefore

```text
sum_{c odd} |x_c|^2 = (n/2) ( r' - a_{n/2}(S) ) = h * ( r' - a_{n/2}(S) ).
```

AM-GM on the `h` nonnegative reals `|x_c|^2`:

```text
|N(x_1)|^{2/h} = ( prod_c |x_c|^2 )^{1/h} <= (1/h) sum_c |x_c|^2
               = r' - a_{n/2}(S),
```

which is (CS2). QED

*(CS3) is (CS1)+(CS2) in logarithms, valid because `x_1 != 0` makes
`N(x_1)` a nonzero integer, so `p^{|Z_w^odd|} <= |N(x_1)|`.*

### Proof of the uniform form (CS4)

`Z_w` contains `{1,...,w-1}` by definition, so `Z_w^odd` contains every
odd `s` in `[1, w-1]`, of which there are `ceil((w-1)/2)`. Hence
`|Z_w^odd| >= ceil((w-1)/2)` for **every** `p`, with equality when
`delta = 1`. Since `a_{n/2}(S) >= 0`, (CS3) implies (CS4). QED

### Machine verification

* **(CS1) and (CS3) against every round-16 census accident.**
  `verify_cop.py floor`: 642 bad-prime records at `n in {16,32}`,
  637 with `x_1 != 0`, 5 with `x_1 = 0` (all confirmed `mu_2`-periodic,
  i.e. LEMMA STRAT's branch). **1280 checks, 0 failures.**
* **The bound is SHARP.** The tightest measured (CS3) margin is
  **0.0000 bits**, attained at `n=16, r'=3, w=2, p=3, |Z_w^odd|=4`.
  Equality in AM-GM means all `|x_c|` equal — so (CS2) cannot be improved
  by a constant factor in general.
* **(CS2) exactly**, as an integer inequality `N(x_1)^2 <= (r'-a)^h`:
  exhaustive over ALL subsets at `n = 8` and `n = 16`, plus 40 random at
  `n = 32` — inside the **65,613 checks, 0 failures** of
  `verify_cop.py self`.

---

## §5. Corollaries — what THEOREM CS excludes

> **COROLLARY CS-EXCL.** If `ceil((w-1)/2) * log2 p > (n/4) * log2 r'`
> then for EVERY `S <= Z/n` of size `r'` with `x_1 != 0`, `p` does not
> divide `N(I_S)`: `S` is not a solution in characteristic `p`, for any
> choice of primitive `n`-th root of unity.

> **COROLLARY CS-TOWER.** The exclusion survives the stratum recursion.
> At stratum `a`, LEMMA STRAT reduces to `(n/2^a, r'/2^a, w_a)` with
> `w_a = floor((w-1)/2^a)+1`.  The exact biting condition is
>
> ```text
> ceil(floor((w-1)/2^a)/2) log2 p
>     > (n/2^{a+2}) log2(r'/2^a).                         (CS-TOWER-a)
> ```
>
> Thus every nonstructural stratum is excluded when `(CS-TOWER-a)` is
> checked for each such `a`.  If `w=2^v`, then its left coefficient is
> exactly `2^{v-a-1}` for `a<v`; after multiplying by `2^a`, the left
> side is independent of `a` and the right side strictly decreases.
> Therefore, for power-of-two `w`, exclusion at `a=0` implies exclusion
> at every deeper nonstructural stratum.  Combined with LEMMA Z (which
> handles `a >= log2 M`), **every** `S` is then covered.

The earlier displayed simplification replaced the exact ceiling by
`w/2^{a+1}`.  That is harmless for the power-of-two prize windows used by
the machine check, but is not an identity for arbitrary `w`; general
windows require the finite per-stratum checks printed above.

*Machine check:* `prize_floor.py` — 12 tower checks at `w = 2^38, 2^39`,
`a = 0..5`, all bite, margins **widening** with `a` (ratio 1.62 -> 1.85).

### The prize-row consequence (this is (K5))

Crossing row constants quoted verbatim from
`notes/pilots_20260804/mun_anticoncentration/REPORT.md:48`:

> `| crossing razor | `F_p`, `p >= 2^39+1`; recorded rows `q = p` PRIME ~2^256, `delta = 1` | `2^41` | `Z_w = {1..w-1}`, `\|Z_w\| = w-1` | `[2^41, 2^41-w+1, w]` **MDS = Reed-Solomon** | `r' = 2^40-w`, `w in [2^34,2^39]` | `B* = floor(q/2^128) < 2^128` |`

At `n = 2^41`, `r' = 2^40 - w`, the **benchmark substitution**
`log2 p = 256` gives (`prize_floor.py`, exact):

| `w` | LHS (bits) | RHS (bits) | verdict |
|---|---|---|---|
| `2^34` | 2.19902e12 | 2.19777e13 | vacuous |
| `2^35` | 4.39805e12 | 2.19651e13 | vacuous |
| `2^36` | 8.79609e12 | 2.19390e13 | vacuous |
| `2^37` | 1.75922e13 | 2.18843e13 | vacuous |
| `2^38` | 3.51844e13 | 2.17621e13 | **EXCLUDED** |
| `2^39` | 7.03687e13 | 2.14405e13 | **EXCLUDED** |

Exact boundary by bisection: the first excluded integer is
`w_0 = 170,752,922,588 = 2^37.3131` (equivalently, the last unexcluded
integer is `170,752,922,587`).  Thus CS-EXCL excludes every `w >= w_0`,
i.e. **71.16% of the crossing bracket
`[2^34, 2^39]`**, and 2 of the 6 power-of-two `w` (the only `w` with a
nonempty structural family, round-15 `(P4)`).

Threshold vs field size: `log2 p = 128 -> 39.57%`; `208 -> 63.83%`;
`256 -> 71.16%`; `512 -> 87.14%`. At `log2 p <= 64` the bound is vacuous
across the whole bracket.

The percentage depends on the **base characteristic `p`**, not on the
ambient field size `q=p^e`.  Consequently `71.16%` is a near-256-bit
prime-characteristic benchmark, not uniform coverage of all admissible
extension-field rows and not a status change for the crossing target.

---

## §6. (K1) THE COPRIMALITY CONJECTURE — final form

> **COPRIMALITY CONJECTURE (CC).** Let `n = 2^m`, `w >= 3`,
> `S <= Z/n` with `|S| = r'`. Define the exceptional class
>
> ```text
> E(n,r',w) = E_strat  u  E_floor,
> E_strat = { S : 1 <= strat(S) < log2 M },        M = least 2-power >= w
> E_floor = { S : some odd p | N_odd(I_S) has
>                 |Z_w^odd(p)| log2 p <= (n/4) log2 r' }.
> ```
>
> Then `N_odd(I_S) = 1` for every `S` outside
> `E(n,r',w) u {S : strat(S) >= log2 M}`, and moreover
> `|E_floor| / #orbits -> 0` as `w` grows at fixed `(n, r'/n)`.

**Status of each clause.**

* `strat(S) >= log2 M` gives `N(I_S) = 0` — **PROVED**, LEMMA Z (B1),
  independently re-verified here (`verify_cop.py self`, check S4:
  `N(I_S) = 0 <=> S periodic`, exhaustive at `n = 8` all `r'`, and
  `n = 16` for `r' <= 4`).
* `E_strat` reduces to a smaller instance — **PROVED**, LEMMA STRAT §3.
* Every `S` outside `E_strat` with a bad prime lies in `E_floor` —
  **PROVED**, THEOREM CS §4. So the exhaustiveness half of CC is a
  theorem, not a conjecture.
* `E_floor` is **sparse** — this is the genuinely conjectural half, and
  it is what (K4) measures.

**How (ES) follows (the (K1) requirement, discharged).** If
`N_odd(I_S) = 1` then `I_S` is contained in no prime of `O_K` of odd
residue characteristic, so by the census identity `S` is a solution in NO
odd characteristic whatsoever — one statement kills every `p` at once.
Quantifying over `S`: the only solutions at any odd `p` are the LEMMA Z
periodic ones, which is exactly the (ES) crossing instance
`|W_w| = C(n/M, r'/M)`. **Unconditionally**, CS-EXCL + CS-TOWER + LEMMA Z
already give this at every row satisfying (CS4).

---

## §7. (K2) The three registered tools — verdicts

Tested in the mandated order, each with a named verdict.

**(a) Resultant factorization (the DLI/WCL banked method) — VERDICT:
DEAD as a closed form, USED as machinery.** The banked halving recursion
`Res(X^n+1,f) = Res(Y^{n/2}+1, f_0^2 - Y f_1^2)`
(`background/nodes/dli_wcl_ell2_weight6_recursive_norm_exclusion/proof.md:77-80`,
PROVED) computes `N(x_s)` fast but yields **no closed form whose prime
support is characterized** — nothing in the repository does, and I found
none. Worse, the banked **collapse identity** (`archive/compressed_dli_lane_20260705/pcf_evaluation_flatness/statement.md:8-12`:
*"Res(X^N+1, Q_{d,r}) = Res(X^N+1, Q_{d,1}) for all odd r — the collapse
identity, proved+verified"*) shows the odd-index resultants are all
**equal**, so the gcd-of-norms over the odd window carries exactly the
information of ONE norm. **This is why the norm-gcd route cannot see the
`w >= 3` collapse at all**: the collapse is an *ideal*-level phenomenon
(distinct primes `P_s`), invisible to the gcd of principal norms. Route
(a) is the correct diagnosis of why round-16's "gcd of norms" framing
undersells its own finding.

**(b) Galois-orbit counting — VERDICT: THIS IS THE PROOF.** §4 Steps 1-3
are exactly a Galois-orbit count: the window forces `x_1` into
`|Z_w^odd|/delta` distinct primes above `p`, each of residue degree
`delta`. As registered in `PREREG.md` §Q2 I expected (b) to be the one
that works, and it is.

**SCOPE LIMIT OF (b), STATED PLAINLY.** The improvement factor of
THEOREM CS over the banked M3 is exactly
`|Z_w^odd| / delta = #{ <p>-orbits meeting {s odd, 1 <= s <= w-1} }`.
At `w = 3` the odd part of `{1,2}` is `{1}`, whose `<p>`-orbit is `<p>`
itself, so `|Z_3^odd| = delta` and **THEOREM CS at `w = 3` is exactly
round-16's M3 — it adds nothing.** The factor is 1 at `w in {2,3}`, is 2
generically at `w = 4`, and grows like `w/2`. **So the mandate's literal
(K2) target — the `w = 3` collapse — is NOT explained by this theorem.**
The measured `w = 3` coprimality rate (0.95-0.99, §K4) is therefore
evidence for the *sparsity* half of CC, which remains conjectural. What
THEOREM CS does explain is the collapse for `w >= 4`, increasingly
strongly with `w`, which is where the entire prize-row payoff sits.

**(c) Lam-Leung pushed to bounds on `N(I_S)` — VERDICT: DEAD, and it was
pre-refuted in the repository.** (B5): at `n = 2^s` the only prime is 2,
so every char-0 vanishing sum is a combination of antipodal pairs, and
`S5_LAM_LEUNG_TRANSPORT.md` records the transport as *resolved (empty)*.
The literature map independently records
(`notes/literature_map_20260726/LITERATURE_MAP.md:500`):

> ```
> - **A char-`p` structure theorem for 2-power-order vanishing sums** — Lam–Leung explicitly disclaim a conjecture; DZ02's method is the only lead and is inaccessible.
> ```

Lam-Leung controls **vanishing** (`N = 0`), which LEMMA Z already gives in
sharper form; it says nothing about `N != 0` being *small*. I did not
pursue it further and report it as dead on banked grounds, not as
unattempted.

---

## §8. AK-UNIT self-check (registered in `PREREG.md` §Q5)

`THEOREM AK-UNIT`, verbatim from
`notes/pilots_20260806/es_axkatz_transfer/REPORT.md:44`:

> **(ii+) DEAD-BY-SHAPE. THEOREM AK-UNIT (unconditional).** At every crossing row the (ES) target `|W^struct| = C(L, r'/M)` has `L = n/M = 2^{41−v} ≤ 128`, and every prime factor of `C(a,b)` is `≤ a`. Since `p ≥ 2^39+1 ≫ 128`, **`p ∤ |W^struct|` for every admissible `p`, with no case split on δ.**

**Verdict: THEOREM CS is NOT excluded by AK-UNIT.** AK-UNIT (with
COROLLARY AK-ACCIDENT) excludes any route whose conclusion is a
congruence about the **count** `|W_w|`. THEOREM CS's conclusion is
`p^{|Z_w^odd|} | N_{K/Q}(x_1)` — a divisibility statement about an
**algebraic-integer norm attached to one individual set `S`**, never
about a count. It is used only to contradict an **archimedean** size
bound (CS2). The output is per-set ("`S` is not a solution at `p`"); the
statement about the count is obtained by quantifying over `S`, and at no
point is a congruence on `|W_w|` asserted or used. The route is an
archimedean/`p`-adic squeeze, which is the shape AK-UNIT leaves open.

Cross-check against `COROLLARY AK-ACCIDENT` (same file:45): that corollary
says a proof of `p | |W_w|` would force accidents to EXIST. CS proves the
opposite direction (no accidents), and indeed CS is consistent with
`p ∤ |W_w|`: under CS the count equals `|W^struct| = C(L, r'/M)`, whose
prime factors are all `<= L <= 128 < p`. **CS and AK-UNIT agree.** That
is a nontrivial consistency check, and it passes.

---

## §9. What remains (honest)

1. **The gap `w <= 2^37.31`.** CS-EXCL is vacuous on 28.84% of the
   crossing bracket, including 4 of the 6 power-of-two `w`
   (`2^34..2^37`). The `w = 2^34` end is short by a factor of 10 in the
   exponent. Since (CS2) is **sharp** (equality measured at `n=16`), the
   gap cannot be closed by improving the archimedean side; it needs
   either a better lower bound on `v_p(N(x_1))` than `|Z_w^odd|` or a
   genuinely different mechanism.
2. **`E_floor` sparsity is unproved.** Measured, not proved (§K4). No
   asymptotic statement in `n` is established.
2b. **`w = 3` is untouched.** Per §7, THEOREM CS degenerates to the banked
   M3 at `w = 3`. The observed `w = 3` collapse (rate 0.9897 at
   `n=32, r'=6`) has NO proof here. This is the mandate's literal (K2)
   target and I did not close it.
3. **Band rows are untouched.** THEOREM CS is stated for the window/prefix
   object; the band consumers use generic linear forms and are outside
   its hypotheses.
4. **Scale.** All measurements are `n in {16, 32}`; the prize row is
   `n = 2^41`. The prize-row statements in §5 are *proved consequences of
   THEOREM CS*, not extrapolations from the measurements — but THEOREM CS
   itself is proved for all `n`, so this is a genuine transfer, not a fit.
