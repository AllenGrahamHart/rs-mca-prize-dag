# PROOFS — THE CROSSING GAP (round 20, crossing_gap pilot)

Opus pilot, 2026-08-06. Every statement registered in `PREREG.md`
§G0–G5 **before** computation. Machine-checked by `cg_arith.py` and
`cg_census.py` (fail-closed; the permanent `failclosed` stage of each
script exits 1 by construction).

**Totals: 7,192 checks, 0 failures** across
`arith_{rhllb,pt2,cover,cwfloor}.out` and
`census_{haar,census,coupled,cwtoy,cwexhibit}.out`;
`arith_failclosed.out` and `census_failclosed.out` both exit 1.

---

## §0. Facts CITED VERBATIM, not claimed (subtraction, hard law 5)

**(V1) THEOREM SP-COVER / LEMMA COS / SP-UNIFORM.**
`background/nodes/es_ternary_suppression_instruments/statement.md:36-44`:

> **THEOREM SP-COVER / LEMMA COS / THEOREM SP-UNIFORM.** Full
> `<p>`-coset coverage of the odd window forces periodicity (engine:
> LEMMA AB — A - B is a TERNARY vector; F_3 is why p = 3 is
> extremal); w_cov(p, 2^m) is m-independent for m >= v_2(p^2-1) and
> <= 2^{v_2(p^2-1)}; hence p | N_odd(I_S) with strat(S) = 0 forces
> p > sqrt(w+1).

`notes/pilots_20260806/efloor_sparsity/PROOFS.md:122-128`:

> **THEOREM SP-COVER.** Let `n = 2^m`, `p` odd, and suppose **every coset of
> `<p>` in `(Z/n)^*` contains an odd `s` with `1 <= s <= w-1`.** Then for
> every `S <= Z/n` with `strat(S) = 0`,
> `p  does not divide  N(I_S).`

and `:149-151`:

> Define `w_cov(p,n) := 1 + max over <p>-cosets of the least element` (every
> element of `(Z/n)^*` is odd because `n` is a 2-power), so SP-COVER applies
> exactly when `w >= w_cov(p,n)`.

**(V2) LEMMA AB.** `efloor_sparsity/PROOFS.md:88-96`:

> **LEMMA AB.** Write `f_S = A + X^h B` with `deg A, deg B < h = n/2`, i.e.
> `A` is the indicator of `S n [0,h)` and `B` that of `S n [h,n)` shifted.
> Put `v := A - B in {-1,0,1}^h`. Then
> 1. `f_S = v (mod Phi_n)`, so for every **odd** `s`,
>    `f_S(xi^s) = v(xi^s)` for any primitive `n`-th root `xi` in char `p`;
> 2. `v = 0  <=>  S + n/2 = S  <=>  strat(S) >= 1`, for every odd `p`;
> 3. the number of `S` with a given `v` is exactly `2^{z(v)}`, where
>    `z(v) = #{i : v_i = 0}`.

**(V3) LEMMA OE.** `notes/pilots_20260806/crossing_low_w/PROOFS.md:150-151`:

> **LEMMA OE.** `p_t(S') = sum_j eps_j theta^{tj}` for `t` ODD, and
> `p_t(S') = sum_j sig_j (theta^2)^{(t/2)j}` for `t` EVEN.

and `background/nodes/crossing_dsa_refutation/statement.md:23-26`:

> **LEMMA OE.** Odd-index conditions see only eps_j = [j in S'] -
> [j+L in S'] (ternary); even-index conditions see only sigma and ARE
> the next stratum's conditions. The even-condition mechanism is real
> at every shallower stratum and vacuous exactly at the binding one.

**(V4) LEMMA TC.** `crossing_low_w/PROOFS.md:169-178`:

> **LEMMA TC.** The single deep-stratum condition depends on `S'` only through
> `eps in {0,±1}^L`. The fibre over `eps` has size
> `C(L−U, (r'_a−U)/2)` where `U = |supp(eps)|`, nonempty iff `U ≡ r'_a (mod 2)`
> and `U <= r'_a`; and
> `sum_{eps} C(L−U(eps), (r'_a−U(eps))/2)  =  C(2L, r'_a).`
> `eps = 0` is exactly the structural fibre, of size `C(L, r'_a/2)`.

**(V5) LEMMA DS.** `background/nodes/crossing_dsa_refutation/statement.md:15-21`:

> **LEMMA DS.** At n = 2^41, w = 2^v, r' = 2^40 - w, the deepest
> stratum a = v-1 has n_a = 2^{42-v}, L = 2^{41-v}, r'_a = L - 2
> (uniformly in v — ONE one-parameter family (2L, L-2)) ...

**(V6) THEOREM DSA.** `crossing_dsa_refutation/statement.md:35-38`:

> **THEOREM DSA (unconditional pigeonhole).** If p^{delta_a} <
> 2^{L-2} then a nonzero ternary relation exists with even support
> <= r'_a, hence W_w contains a NON-STRUCTURAL member ...

**(V7) THEOREM Z-FLOOR and its scope.**
`background/nodes/f2_z1_mass_knife_edge/statement.md:17-21`:

> **THEOREM Z-FLOOR (pointwise first-moment floor).** For EVERY
> F_p-subspace, Z(L) = sum_{eps in L^perp cap T} 2^{-wt(eps)} >=
> 2^m / p^{dim L}. One Cauchy-Schwarz from the banked collision
> identity sum_s |F_s|^2 = 2^m Z(L) ...

`background/nodes/tern_master_threshold/statement.md:47-50`:

> Z-FLOOR-M: holds for any finite X ⊆ Z^M with
> difference-multiplicity weights; NOT the constant-weight functional.
> Z-FLOOR ≡ DSA + support control (the same binary-difference
> collision; DSA's regime is tau < 1 - 2/N).

**(V8) COROLLARY PT-2 (the watch line under audit).**
`background/nodes/tern_master_threshold/statement.md:93-97`:

> **WATCH LINE (COROLLARY PT-2):** the crossing bracket's proved
> lower endpoint w = 2^34 clears the ternary counting threshold by
> 0.336 bits — one step below, the deep stratum is supercritical at
> RECORDED PRIME rows. Any change to the bracket's lower end must
> re-run this check.

and its derivation, `tern_unification_adversary/PROOFS.md:225-232`:

> **COROLLARY PT-2 (new, and campaign-relevant).** In I3's own coordinate the
> threshold is `w_tern = log2(3) * 2^33 = 2^33.66445`. The crossing bracket's
> lower endpoint `w = 2^34` clears it by only **0.336 bits**. In I2's
> coordinate, one step below the bracket (`v = 33`, `L = 256`) gives `tau = 1`
> and `Tcrit = +149.75` ...

**(V9) THEOREM MT / PT (the proved vs heuristic boundary).**
`background/nodes/tern_master_threshold/statement.md:55-59`:

> With tau := g·log2 p / h: existence is forced for tau < 1 (with
> |T| >= 2^h/p^g); ternary vectors are EXPECTED present iff
> tau < log2 3 = 1.585 (first-moment side, heuristic; only tau < 1 is
> proved, by pigeonhole).

**(V10) RHL-LB and its source.**
`critical/nodes/rate_half_list_adjacent_crossing/statement.md:31-41`:

> the proved cyclically rotated prefix floor gives
> `L_1(k+17,179,869,183)>B*,`
> so any valid crossing satisfies
> `a_L(C)>=k+17,179,869,184 = k+2^34.                  (RHL-LB)`

`critical/nodes/rate_half_cyclic_rotated_prefix_floor/statement.md:106-134`:

> For the prize-max rate-half row, take
> `n=2^41,  k=2^40,  c=2^33,  N=256,  d=1,  m=129,  s=c-1.`
> Then `(CR1)` is the field-independent integer
> `L_cyc = ceil(C(255,129)/256) > 2^238,`
> and `(CR2)` has excess
> `sigma_cyc = dc+s = 2^34-1 = 17,179,869,183.              (CR3)`

and `:145-149`:

> Among maximal-prefix instances `s=c-1` of `(CR1)` whose lower bound is
> certified uniformly by checking `(CR5)` at `q=2^256`, this is the unique
> largest agreement excess. This extremality is only for the printed cyclic
> construction and cap-uniform criterion; it is not an upper bound on arbitrary
> received words.

**(V11) (RHL-B12), which pins the LIVE budget range.**
`rate_half_list_adjacent_crossing/statement.md:65-76`:

> For every official rate-half multiplicative-coset row with
> `B* in {1,2},`
> the explicit low-budget theorem proves
> `a_L(C)=3n/4,       L_1(3n/4)<=B*<L_1(3n/4-1).       (RHL-B12)`

**(V12) The admissible characteristics.**
`notes/pilots_20260806/es_g_lanes/PROOFS.md:69-71`:

> **Characteristic arithmetic (proved, verify3_prizerow.py R3).** `n = 2^41`,
> `n | p^e - 1`, `p^e = q < 2^256` force `delta := ord_n(p) = 2^j` with
> `j <= 2`, so `delta in {1,2,4}` and `p >= 2^39 + 1`.

**(V13) The dichotomy this pilot re-audits.**
`crossing_dsa_refutation/statement.md:52-56`:

> **THE DICHOTOMY.** e = 1 prime rows are NEVER in the DSA regime:
> B* >= 3 forces log2 p >= 129.585 > 126. The recorded prize rows are
> untouched and RE-PRICED (HEURISTIC, labelled) ...

**(V14) The round-18 residual this pilot answers.**
`efloor_sparsity/REPORT.md:86`:

> 5. **Even-window conditions are used in none of the proofs**, yet the
> census shows they matter (`p=7` at `n=32` empties at `w=7` while odd
> conditions alone never suffice). An even-condition SP-COVER would lower
> every threshold — the most obvious next step.

**(V15) CATCH E-3 (the gap constant under audit).**
`efloor_sparsity/REPORT.md:77`:

> **CATCH E-3 (campaign-relevant).** The official row gate `v_2(q-1) >= 41` —
> *required* by the construction — forces `j_q >= 42`, so SP-COVER needs
> `w >= 2^42` while the bracket caps at `w = 2^39`. ... CS-EXCL closes
> `w > 2^37.3131` (independently reproduced); the gap to SP-COVER is
> `2^4.6869` in `w` and the two exclusions do not meet.

**(V16) The round-18 e=1 sub-range statement (subtraction for C3).**
`crossing_low_w/PROOFS.md:393`:

>    `log2 p > 202.875` is expected clean — which is where the recorded rows sit.

`crossing_low_w/REPORT.md:95`:

> **Exact remaining set:** (1) `w = 2^34` — (ES) REFUTED on 10 pairs outright
> + part of 6; only the `e=1` sub-range `log2 p > 202.875` is expected clean,
> which is where the recorded rows sit.

**SUBTRACTION.** (V16) is the upstream statement closest to this
pilot's C3 finding, and it is quoted so that the C3 catch is priced
correctly: the *mathematics* of the 202.875 boundary is round-18's;
what is new here is (i) that the MINTED watch line (V8) drops the
`log2 p` scope, (ii) the exact clearance **as a function of p** under
**all four** banked readings, and (iii) the identification of the LIVE
range via (RHL-B12). Nothing in §2 (CW-FLOOR) appears in the repo:
(V7) explicitly records the constant-weight functional as absent.

---

## §1. (C1) THE EVEN-CONDITION EXTENSION IS THE 2-ADIC HAAR TOWER

### 1.1 The tower, and the exact decomposition of the window

Let `n = 2^m`, `S ⊆ Z/n`, `xi` a primitive `n`-th root of unity in
characteristic `p` (odd). For `0 <= a <= m` put

```text
n_a := 2^{m-a},
m^{(a)}_j := #{ i in S : i = j (mod n_a) },        j in Z/n_a,
eps^{(a)}_j := m^{(a)}_j - m^{(a)}_{j + n_a/2},    j in Z/n_{a+1}.
```

So `m^{(0)}` is the 0/1 indicator of `S`, `m^{(a)}_j in [0, 2^a]`, and
`eps^{(a)}_j in [-2^a, 2^a]`. Note `eps^{(0)} = A - B` is LEMMA AB's
ternary vector `v`, and `m^{(1)}` is LEMMA OE's `sigma in {0,1,2}^{n/2}`.

> **PROPOSITION HT (the Haar tower).**
> (i) `m^{(a+1)}_j = m^{(a)}_j + m^{(a)}_{j+n_a/2}`, so
> `(eps^{(0)}, ..., eps^{(m-1)}, r')` determines `S` and conversely:
> the map is a BIJECTION onto the admissible tuples.
> (ii) For every `s in [1, n)` write `s = 2^a t` with `t` odd. Then
> ```text
> f_S(xi^s)  =  eps^{(a)}( theta_a^t ),        theta_a := xi^{2^a},
> ```
> `theta_a` of order `n_a` and `theta_a^t` again primitive of order `n_a`.
> (iii) `strat(S) >= b  <=>  eps^{(0)} = ... = eps^{(b-1)} = 0`.

**Proof.** (i) is the inverse pair
`m^{(a)}_j = (m^{(a+1)}_j + eps^{(a)}_j)/2`,
`m^{(a)}_{j+n_a/2} = (m^{(a+1)}_j - eps^{(a)}_j)/2`.
(ii) `xi^{si}` depends on `i` only mod `n/gcd(s,n) = n/2^a = n_a`, so
`f_S(xi^s) = sum_{j in Z/n_a} m^{(a)}_j theta_a^{tj}`; and
`theta_a^{t(j+n_a/2)} = theta_a^{tj} (theta_a^{n_a/2})^t = -theta_a^{tj}`
because `t` is odd and `theta_a^{n_a/2}` is the unique element of order 2.
Splitting the sum over antipodal pairs of `Z/n_a` gives
`sum_{j<n_a/2} eps^{(a)}_j theta_a^{tj}`. This is LEMMA OE (V3), stated
at every level rather than one level.
(iii) `eps^{(0)} = 0` iff `S + n/2 = S` (LEMMA AB(2)); inductively, given
`eps^{(0)} = ... = eps^{(b-2)} = 0` the set `S` is `n/2^{b-1}`-periodic and
`m^{(b-1)} = 2^{b-1} 1_{S mod n_{b-1}}`, so `eps^{(b-1)} = 0` iff the
reduced set is `n/2^b`-periodic. ∎

*Machine check:* `cg_census.py haar` — **6,802 checks, 0 failures**;
(ii) verified for EVERY `s in [1,n)` at `(n,p) in {(16,3),(16,7),(32,7),
(32,17),(64,5)}` over 40 random `S` each, (i) as a round trip, and (iii)
EXHAUSTIVELY over all `2^16` subsets at `n = 16`.

**Reading.** PROPOSITION HT is the exact sense in which "the even
conditions are the next recursion level": the window condition set
`{f_S(xi^s) = 0 : 1 <= s <= w-1}` partitions by `v_2(s)` into
independent conditions on the levels `eps^{(a)}`, with level `a`
carrying the odd exponents `t <= (w-1)/2^a`. The recursion is
`(n_a, alphabet [0,2^a], w_a)` with `w_a - 1 = floor((w-1)/2^a)` — the
same reduction LEMMA STRAT performs on `(n, r', w)`, but applied to the
FOLDING of `S` rather than to a periodic `S`.

### 1.2 The extended coverage criterion, and its integrality gate

> **THEOREM SP-COVER-R (recursive SP-COVER).** Let `a >= 0` and suppose
> (i) every `<p>`-coset of `(Z/n_a)^*` contains an odd `t` with
> `1 <= t <= floor((w-1)/2^a)`, i.e.
> ```text
> w  >=  2^a ( w_cov(p, n_a) - 1 ) + 1                     (LVL-a)
> ```
> and (ii) `p > 2^a` (the INTEGRALITY GATE). Then `eps^{(a)} = 0` as an
> INTEGER vector, i.e.
> ```text
> #{i in S : i = j  (mod n_a)}  =  #{i in S : i = j + n_a/2 (mod n_a)}
> ```
> for every `j` — `S` is EQUIDISTRIBUTED between the two halves of every
> residue class mod `n_a`.

**Proof.** By HT(ii) and Frobenius (`eps^{(a)} in F_p[X]`, so
`eps^{(a)}(theta_a^{pt}) = eps^{(a)}(theta_a^t)^p`), hypothesis (i) makes
`eps^{(a)}` vanish at EVERY primitive `n_a`-th root of unity, so
`Phi_{n_a}(X) = X^{n_a/2} + 1` divides `eps^{(a)}(X)` in `F_p[X]`. Since
`deg eps^{(a)} < n_a/2`, `eps^{(a)} = 0` in `F_p^{n_a/2}`. Each entry is an
integer of absolute value `<= 2^a < p`, so `eps^{(a)} = 0` over `Z`. ∎

At `a = 0` the gate is `p > 1` and the conclusion is `strat(S) >= 1`:
SP-COVER (V1) is exactly the `a = 0` case.

### 1.3 CATCH-20B — the even-condition route CANNOT lower the exclusion threshold

Three facts, each proved and each machine-checked:

**(B1) Even exponents are non-units, so they cannot cover.** The
conclusion `strat(S) >= 1`, i.e. the EXCLUSION of the `a = 0` class,
is by HT(iii) equivalent to `eps^{(0)} = 0`, and by HT(ii) only the
exponents `s` with `v_2(s) = 0` see `eps^{(0)}`. Coverage arguments at
level `a >= 1` conclude `eps^{(a)} = 0`, which is a COUNTING-BALANCE
condition on `S`, strictly weaker than periodicity (already at `n = 8`,
`S = {0,1,2,3}` has `m^{(1)} = (1,1,1,1)`, hence `eps^{(1)} = 0`, while
`eps^{(0)} = (1,1,1,1) != 0`, i.e. `strat(S) = 0`). **No amount of
even-condition coverage can produce the `a = 0` exclusion.**

**(B2) At official PRIME rows the level thresholds are all out of range.**
`e = 1` forces `n | p - 1` (the domain `D` is a multiplicative coset of
order `n = 2^41`), i.e. `p = 1 mod 2^41`, i.e. `delta = ord_n(p) = 1`, and
then `<p> = {1}` in `(Z/n_a)^*` at EVERY level, so every coset is a
singleton and

```text
w_cov(p, n_a) = n_a = 2^{41-a},   hence  (LVL-a):  w >= 2^41 - 2^a + 1.
```

The integrality gate `p > 2^a` with the admissible floor `p >= 2^39 + 1`
(V12) passes for every level `a <= 40` at live rows, and `w_min(a)` is
MINIMISED at the deepest level `a = 40`:
`min_a w_min(a) = 2^41 - 2^40 + 1 = 2^40 + 1`. Every crossing instance
has `r' = 2^40 - w >= 1`, i.e. `w <= 2^40 - 1`. **No level fires at any
admissible `w`, ever — and the margin is exactly 2.**

**(B3) The level law is NOT monotone — but the exceptions do not help.**
I registered (G1.2) that `(LVL-a)` is increasing in `a`. That is
**FALSIFIED**: `cg_arith.py cover` finds 42 `(p,m,a)` cells with
`w_min(a) < w_min(0)`, the first being `p=3, m=4, a=2` (5 < 6) and
`p=7, m=4, a=1` (7 < 12). Every such cell has `m - a < j_p = v_2(p^2-1)`,
i.e. LEMMA COS's `m`-uniformity hypothesis fails at the REDUCED level so
that `w_cov(p, n_a)` collapses; 27 of the 42 have `ord_{n_a}(p) = 1`,
which is exactly the official prime-row family. **Reported, not buried:
my registered monotonicity claim was wrong, the corrected law is
`(LVL-a)` with `w_cov` evaluated at the reduced length, and the campaign
conclusion is unchanged by (B1)+(B2).**

*Machine check:* `cg_arith.py cover` — **190 checks, 0 failures**,
including reproduction of the banked `w_cov` table, LEMMA COS's bound
and uniformity at `m = 4..12` for 11 primes, the closed form
`w_min(a) = 2^41 - 2^a + 1`, and the two range facts in (B2).

### 1.4 CATCH-20C — CATCH E-3's gap constant is 2^3.6869, not 2^4.6869

(V15) derives the SP-COVER threshold at official rows from
`w_cov <= 2^{j_q}` with `j_q = v_2(q^2-1) >= 42`. That is LEMMA COS's
BOUND, and LEMMA COS's `m`-uniformity requires `m >= j_p`; here
`m = 41 < 42`, so `2^{j_q}` is not the operative value. The operative
value is the one computed in (B2):

```text
w_cov(q, 2^41) = 2^41   at every e = 1 prime row (delta = 1),
gap to CS's w* = 2^37.3131  =  2^{41 - 37.3131}  =  2^3.6869.
```

The correction is in the SAFE direction (a smaller gap) and does not
move any verdict: `2^41 > 2^40 > w`, so the two exclusions still do not
meet, and CS's bracket coverage is untouched — `cg_arith.py cover`
reproduces `71.1645%` closed / `28.8355%` residual on the banked
LINEAR-in-`w` convention over `[2^34, 2^39]`.

### 1.5 THEOREM SP-COUPLE — what the even conditions DO buy, and the census gate

Only ONE structural coupling survives, and it is the whole content of
the even conditions at `a = 0`:

```text
supp(eps^{(0)})  =  { j : m^{(1)}_j = 1 }  =  { j : m^{(1)}_j odd }.
```

> **THEOREM SP-COUPLE.** Let `n = 2^m`, `h = n/2`, `p` odd, `S ⊆ Z/n`
> with `strat(S) = 0` and `p | N(I_S)`. Put `eps = A - B in {0,±1}^h`
> and `u = m^{(1)} in {0,1,2}^h`. Then SIMULTANEOUSLY
> (a) `eps in C_odd(n,p,w)` — the negacyclic `F_p`-code of length `h`
>     with zeros `{xi^s : s odd, 1 <= s <= w-1}` (SP-TERNARY's code);
> (b) `u in C_even(n,p,w)` — the cyclic `F_p`-code of length `h` with
>     zeros `{eta^t : 1 <= t <= floor((w-1)/2)}`, `eta = xi^2` of order `h`;
> (c) `supp(eps) = {j : u_j = 1}` and `sum_j u_j = r'`.
> Conversely every such pair `(eps, u)` comes from exactly one `S`.
> Hence, EXACTLY,
> ```text
> #{ S : strat(S) = 0, all w-1 window conditions } =
>     sum over nonzero ternary eps in C_odd of
>        #{ y ⊆ supp(eps)^c : 1_{supp(eps)} + 2·1_y in C_even }.
> ```
> If that count is 0 the `a = 0` class is EMPTY. SP-TERNARY is (a)
> alone, i.e. the same sum with the inner count replaced by `2^{z(eps)}`.

**Proof.** (a) is LEMMA AB(1) + Frobenius; (b) is HT(ii) at `a = 1`
plus Frobenius; (c) is `eps_j = [j in S] - [j+h in S]`,
`u_j = [j in S] + [j+h in S]`. The pair `(eps, u)` reconstructs `S`
(`u_j = 0`: neither; `u_j = 2`: both; `u_j = 1`: the one selected by
`sign(eps_j)`), which is PROPOSITION HT(i) truncated at level 1. ∎

**THE CENSUS GATE (V14) IS REPRODUCED.** `cg_census.py census` computes
the EXACT `a = 0` census over ALL `2^n` subsets by meet-in-the-middle:

| `n=32`, `p=7` | w=2 | w=3 | w=4 | w=5 | w=6 | **w=7** | w=8 | w=9 |
|---|---|---|---|---|---|---|---|---|
| `a=0`, FULL window | 1916928 | 38272 | 320 | 64 | 64 | **0** | 0 | 0 |
| `a=0`, ODD conditions only | 1916928 | 1916928 | 17408 | 17408 | 17408 | **17408** | 17408 | 17408 |

The odd conditions alone NEVER empty the class in the tested range
(consistent with `w_cov(7) = 12`); the full window empties it at exactly
`w = 7`, and the only condition added in passing from `w = 6` to `w = 7`
is `s = 6`, which is EVEN. `cg_census.py coupled` supplies the
certificate: at `(n,p,w) = (32,7,7)` the code `C_odd` contains **288**
nonzero ternary codewords (reproducing the banked SP-TERNARY count) and
**none of them admits a compatible `u in C_even`**, so the coupled count
is 0. The same certificate at `n = 16` gives 16 ternary codewords, 0
coupled.

*Machine checks:* `census` — 20 checks, 0 failures, including exact
reproduction of the banked round-18 table
(`efloor_sparsity/PROOFS.md:224-228`: `1048576/983040`, `4096/3072`,
`4096/3072`, `128/64`, `64/0`, `64/0`, `64/0` at `n=32, p=3`).
`coupled` — 30 checks, 0 failures: in all 15 cells the coupled count
EQUALS the independent exhaustive census, and `sum 2^{z(eps)}` EQUALS
the odd-only census.

### 1.6 (C1) VERDICT ON THE GAP

**0.00% of the gap closes.** The gap is governed by `w_cov(q, 2^41)`,
and by (B1) no even-condition coverage statement can move the `a = 0`
exclusion threshold at all, at any `n`, for any `p`. SP-COUPLE is
strictly stronger than SP-TERNARY and does explain every observed
sub-`w_cov` emptiness — but, like SP-TERNARY, it is a **per-`(n,p,w)`
certified criterion with no `n`-uniform form**; at the prize length it
would require deciding ternary-codeword existence in a code of length
`2^40`, which is the (ES) problem again (CATCH E-2). Round 18's named
next step (V14) is therefore answered: **an even-condition SP-COVER
does NOT lower every threshold; it cannot lower the coverage threshold
at all, for a structural reason (even exponents are non-units).**

---

## §2. (C2) THE CONSTANT-WEIGHT Z-FLOOR AT I2 — IT EXISTS

### 2.1 Setting

I2 (V5): `theta` of order `2L`, `Q := p^{delta_a} = |F_{p^{delta_a}}|`,
`L = 2^{41-v}`, `r'_a = L - 2`. For `a ⊆ [0,L)` put
`psi(a) := sum_{j in a} theta^j`, and for `S' ⊆ Z/2L` put
`Psi(S') := sum_{i in S'} theta^i`. Targets:

```text
R      := { eps in {0,±1}^L : sum_j eps_j theta^j = 0 }     (relations)
X_{r'} := { S' ⊆ Z/2L : |S'| = r',  Psi(S') = 0 }           (constant weight)
Y_W    := { a ⊆ [0,L) : |a| = W }                           (Johnson shell)
N(W,W'):= #{ (a,b) in Y_W × Y_{W'} : psi(a) = psi(b) }
```

By LEMMA OE, `Psi(S') = sum_j eps_j(S') theta^j`, so `S' in X_{r'}` iff
`eps(S') in R`; LEMMA TC (V4) is the fibration.

### 2.2 The shell decomposition (exact) and the diagonal floor

> **PROPOSITION SH (exact shell decomposition of LEMMA TC).** For every
> `r' >= 0`,
> ```text
> |X_{r'}|  =  sum_{W=0}^{r'}  N(W, r'-W).
> ```

**Proof.** A pair `(a,b) in Y_W × Y_{W'}` with `psi(a) = psi(b)` gives
`eps := 1_a - 1_b in R` with `U := |supp(eps)| = W + W' - 2|a ∩ b|` and
imbalance `#{+1} - #{-1} = W - W'`. Conversely, for `eps in R` with
imbalance `d` the pairs realizing it with `W + W' = r'` are obtained by
choosing the common part `a ∩ b` of size `c = (r' - U)/2` inside the
`L - U` coordinates off `supp(eps)`; so the number of such pairs is
`C(L - U, (r'-U)/2)` — IDENTICALLY LEMMA TC's fibre size — and the
imbalance determines `(W,W') = ((r'+d)/2, (r'-d)/2)` uniquely. Summing
over `W` therefore reassembles exactly LEMMA TC's sum, whose value is
`|X_{r'}|`. ∎

*(This coincidence — "the constant-weight collision multiplicity at
`W + W' = r'` IS LEMMA TC's fibre size" — is the whole reason the
restriction to the weight shell can work at all. Registered as G2.1.)*

> **THEOREM CW-FLOOR (the constant-weight Z-FLOOR).** For `r'` EVEN,
> ```text
> |X_{r'}|  >=  N(r'/2, r'/2)  >=  C(L, r'/2)^2 / p^{delta_a}.
> ```
> Consequently, if `C(L, r'/2) > p^{delta_a}` then
> `|X_{r'}| > C(L, r'/2) = |X_{r'}^struct|`: a NON-STRUCTURAL
> constant-weight solution exists, and its count is bounded below.

**Proof.** The first inequality is PROPOSITION SH with all terms
non-negative. The second is Cauchy–Schwarz on the diagonal shell: with
`f(v) := #{a in Y_{r'/2} : psi(a) = v}`,

```text
N(r'/2, r'/2) = sum_v f(v)^2  >=  (sum_v f(v))^2 / |image|
              >= C(L, r'/2)^2 / p^{delta_a}.
```

The corollary uses LEMMA TC's `eps = 0` fibre size `C(L, r'/2)`. ∎

This is the exact constant-weight analogue of THEOREM Z-FLOOR (V7)
(`Z(L) >= 2^m / p^{dim L}`), with the full cube `2^L` replaced by the
Johnson shell `C(L, r'/2)` and the difference-multiplicity weight
`2^{L-U}` replaced by LEMMA TC's `C(L-U, (r'-U)/2)`.

### 2.3 The break, located exactly

> **PROPOSITION BR (why the restriction is only half-available).**
> (i) The cross-shell terms `N(W, r'-W)` with `W != r'/2` carry NO
> Cauchy–Schwarz floor: `sum_v f_W(v) f_{W'}(v)` is bounded ABOVE by
> Cauchy–Schwarz and can be `0` while `C(L,W)C(L,r'-W)/Q > 1`.
> (ii) Hence Vandermonde's `sum_W C(L,W)C(L,r'-W) = C(2L,r')` is NOT
> recoverable, and CW-FLOOR loses exactly
> `log2 C(2L,r') - 2 log2 C(L,r'/2)` bits against the flat count.
> (iii) For `r'` ODD the route is UNAVAILABLE: every equal-weight
> collision produces a BALANCED `eps` (`#{+1} = #{-1}`), hence EVEN
> support `U`, while LEMMA TC's index set at odd `r'` consists of `eps`
> with `U` odd — the two sets meet only at `eps = 0`.

*Machine check:* `cg_census.py cwtoy` — **95 checks, 0 failures** over
8 `(L,p)` toys `× 2` weights: LEMMA TC reproduced against brute force
over all `C(2L,r')` subsets; PROPOSITION SH exact in every cell; the
diagonal floor `N(W,W) >= C(L,W)^2/Q` and `|X_{r'}| >= C(L,r'/2)^2/Q`
verified; and in EVERY cell at least one cross-shell term violates the
naive floor — e.g. `L=8, p=3, r'=6`: `N(2,4) = 15 < 24.198`;
`L=8, p=7, r'=6`: `N(1,5) = 7 < 9.143`; `L=6, p=7, r'=4`: `N(1,3) = 0`
against `2.449`. `census_cwexhibit.out` exhibits the corollary firing:
at `L=8, p=7, r'=6` (`Q = 49`, `C(8,3) = 56 > 49`) CW-FLOOR gives
`|X_6| >= 64` and the true value is `168 > 56 = ` structural.

### 2.4 (C2) VERDICT — a new instrument, vacuous where it is wanted

At the prize deep stratum `(L, r'_a) = (128, 126)` (`r'_a = L-2` is
EVEN at every `v`, by LEMMA DS):

| quantity | value (bits) |
|---|---|
| `log2 C(128,63)` — structural / CW-FLOOR threshold | **124.1491** |
| `2 log2 C(128,63)` — CW-FLOOR numerator | 248.2981 |
| `log2 C(256,126)` — flat count (= the retired PER-WEIGHT value) | 251.6279 |
| shell-diagonal loss | **3.3298** |
| THEOREM DSA's threshold `L-2` | 126.0000 |
| CW-FLOOR inside DSA by | **1.8509** |

- **CW-FLOOR fires iff `delta_a · log2 p < 124.1491`** — strictly
  inside DSA's regime (`< 126`) by 1.851 bits. It is therefore
  **VACUOUS at every `e = 1` prime row**, which need `log2 p >= 128`
  (`B* >= 1`) or `>= 129.585` (`B* >= 3`): short by 3.851 / 5.436 bits.
  Registered prediction G2.3 HELD exactly.
- **Where it does fire it is far stronger than DSA.** At the banked
  witness row `p = 3·2^41 + 1`, `delta_a = 1` (`log2 p = 42.585`),
  CW-FLOOR proves
  ```text
  |X_126|  >=  2^205.7132     vs  structural C(128,63) = 2^124.1491
  ```
  where THEOREM DSA proves only the single extra fibre
  `C(108,53) = 2^104.267`. Round 18's HEURISTIC estimate at that row is
  `C(256,126)/p = 2^209.043`; **CW-FLOOR converts that heuristic into a
  theorem, losing exactly the 3.3298-bit shell-diagonal gap.** G2.4 HELD.

**Novelty (subtraction).** (V7) records the constant-weight functional
as explicitly OUTSIDE Z-FLOOR-M's scope, and the round-19 adversary
registered it as the one untested cell. `grep -rn "C(2L\|Johnson
shell\|constant-weight floor"` over the repo finds no floor of this
shape. PROPOSITION SH and THEOREM CW-FLOOR are, to the best of my
subtraction, new; PROPOSITION BR(iii) is the proof of the negative half
the mandate also asked for.

---

## §3. (C3) THE PT-2 CLIFF — ADVERSARIAL RE-VERIFICATION

### 3.1 RHL-LB's constant: EXACT, not floored; CONVENTIONAL only in scope

From (V10), with `n = 2^41`, `c = 2^33`, `N = n/c = 256`, `d = 1`,
`m = N/2 + d = 129`, `s = c - 1`:

```text
sigma_cyc = d·c + s = 2^33 + (2^33 - 1) = 2^34 - 1 = 17,179,869,183
```

an **integer identity**: no floor, no rounding, no approximation. The
step to RHL-LB is the integer successor — `L_1(k + 2^34 - 1) > B*` and
`L_1` non-increasing in the agreement give `a_L >= k + 2^34` — again
exact. `cg_arith.py rhllb` re-derives `L_cyc = ceil(C(255,129)/256)` at
`log2 = 242.6503 > 238`, the cap step `B* < 2^128 < L_cyc`, and the
(CR5) margin at `q = 2^256` as `114.6503` bits (the statement prints
"> 114").

**What IS conventional** is the CHOICE `(c,d,s)`. I re-derived the
extremality from scratch (searching all `N = 2^j`, `j = 2..28`, all
certified `d`): `sigma = 2^34 - 1` at `(c,d) = (2^33, 1)` is the unique
maximum, the runners-up being `3·2^32 - 1 = 2^33.5850` and
`5·2^31 - 1 = 2^33.3219`. So the constant is extremal **only among
maximal-prefix instances of one printed construction under one
cap-uniform criterion**, exactly as the source says.

**DIRECTION CHECK (decisive for the cliff).** RHL-LB is a LOWER bound
on `a_L`. Any improvement to it raises `w = a_L - k`, i.e. moves the
endpoint AWAY from the ternary threshold. The endpoint cannot move
down. *18 checks, 0 failures.*

### 3.2 The clearance is p-DEPENDENT, and the banked 0.336 bits is the
### value at log2 p = 256 only

The threshold, re-derived: the deep stratum at `w = 2^v` is
first-moment subcritical iff `L·log2 3 < delta_a·log2 p` with
`L = 2^{41-v}`, i.e. iff

```text
w  >  w_tern(p) := 2^41 · log2(3) / log2(p)          (delta_a = 1).
```

At `log2 p = 256` this is `2^33.66445`, exactly PT-2's printed value,
and the clearance of `w = 2^34` is `0.33555` bits — reproduced to five
decimals. The I2 cross-check reproduces `tau = 1` and `Tcrit = +149.75`
at `v = 33` and `Tcrit = -53.125` at `v = 34`.

**Reading-invariance (G3.3 HELD).** The odd-part reading
(`g = w/2 = 2^33`, `h = n/2 = 2^40`) and the deep-stratum reading
(`g = delta_a = 1`, `h = L = 128`) give the SAME `log2 p` threshold,
`202.8752`, to `1e-9`. So the answer does not depend on the Lambda
parity convention.

**THE LIVE RANGE.** `B* in {1,2}` is CLOSED EXACTLY by (RHL-B12)
(`a_L = 3n/4`, i.e. `w = 2^39`, the TOP of the bracket), so the open
crossing instance requires `B* >= 3`, i.e. `q >= 3·2^128`. For `e = 1`
(`q = p`, forced by `n | p-1`) the live range is

```text
log2 p  in  [129.5849625, 256).
```

### 3.3 CATCH-20D (MAJOR) — the endpoint is BELOW threshold on a
### majority of the live prime range, under every banked reading

`cg_arith.py pt2`, 21 checks, 0 failures:

| reading (functional) | clearance at `log2 p = 129.585` | at `202.875` | at `255.999` | supercritical for | share of live range |
|---|---|---|---|---|---|
| TERNARY (odd-part = deep-stratum) | **−0.6467** | −0.0000 | +0.3355 | `log2 p < 202.8752` | **57.98%** |
| TERNARY orbit-corrected (LEMMA ROT) | **−0.5662** | +0.0562 | +0.3820 | `log2 p < 194.8752` | 51.65% |
| PER-WEIGHT (retired) | **−0.9393** | −0.3030 | +0.0251 | `log2 p < 251.6279` | 96.54% |
| GLOBAL (ES-G) | **−0.9822** | −0.3356 | −0.0000 | `log2 p < 256` | **100.00%** |

**ANSWER TO THE PRE-REGISTERED ADVERSARIAL QUESTION: YES.** Every
banked reading places the endpoint `w = 2^34` BELOW the first-moment
supercriticality threshold somewhere inside the live admissible `e = 1`
prime range; the two ternary readings do so on a MAJORITY of it, and
the GLOBAL (ES-G) functional does so on ALL of it.

**Honest calibration of what this is and is not.**

1. **It is not a refutation of emptiness.** By THEOREM MT (V9),
   existence is PROVED only for `tau < 1`, i.e. `log2 p < 128`, which
   `B* >= 1` forbids (`q >= 2^128`). THEOREM DSA (V6) needs
   `delta_a·log2 p < L - 2 = 126`, also forbidden. So on the live prime
   range the supercriticality is FIRST-MOMENT (heuristic), inside the
   `tau in (1, 1.585)` band that (V9) explicitly labels heuristic. The
   banked dichotomy (V13) is CORRECT and is re-verified here.
2. **The mathematics is upstream; the defect is in the minted scope.**
   Round 18 already recorded (V16) that "only the `e = 1` sub-range
   `log2 p > 202.875` is expected clean". The MINTED watch line (V8)
   drops that scope: it says "the crossing bracket's proved lower
   endpoint w = 2^34 clears the ternary counting threshold by 0.336
   bits" with no `p`-qualification, and "one step below, the deep
   stratum is supercritical at RECORDED PRIME rows". A maintainer
   re-running "this check" after a change to the bracket's lower end
   would, following the minted text, compute `0.336` and conclude
   safety — when for 57.98% of the live admissible prime range the
   correct value is negative. **CATCH-20D is a SCOPE DEFECT in a minted
   node statement, not a new theorem.** Priced accordingly.
3. **The correct watch line** is the closed form
   `w_tern(p) = 2^41·log2(3)/log2(p)` together with the live range
   `log2 p in [129.585, 256)`; the `0.336` figure is its value at the
   top of that range only.

Per the pre-registration ("reproduction script + stop"), the
reproduction is `cg_arith.py pt2` → `arith_pt2.out`, and I stopped the
C3 line here rather than searching for a rescue.

---

## §4. (C4) THE EXACT REMAINING GAP

**The instance.** Prime-row (ES) emptiness at `n = 2^41`, `k = 2^40`,
`e = 1`, `q = p ≡ 1 mod 2^41`, `B* >= 3` (`log2 p in [129.585, 256)`),
`w = a_L - k in [2^34, 2^39]`, `r' = 2^40 - w`.

**Closed.**
- `w > 2^37.3131` — THEOREM CS, at `log2 p = 256`; 71.1645% of the
  bracket on the banked LINEAR-in-`w` convention (reproduced here).
  NOTE: `w*` is itself `p`-dependent (`CS3`), so the 71.16% figure is
  also a top-of-range value.
- `B* in {1,2}` rows entirely — (RHL-B12) pins `a_L = 3n/4`, `w = 2^39`.

**Open — the exact residual.**
```text
{ w in [2^34, 2^37.3131] }  ×  { log2 p in [129.585, 256) },
```
i.e. 28.8355% of the bracket at the top of the prime range and MORE
below it, plus the whole `p`-dependence of `w*`, plus the entire
sub-range `log2 p < 202.875` where the bracket's own lower endpoint is
first-moment supercritical (CATCH-20D).

**Dead routes — named, do not resurrect.**
1. **SPD union bound** — PROVED VACUOUS in every regime
   (`efloor_sparsity/PROOFS.md:367`; `statement.md:61-62`: *"the SPD
   union-bound shape is PROVED VACUOUS in every regime (character sums
   + BCH cannot reach the middle)"*). Not touched by this pilot.
2. **Even-condition SP-COVER** — DEAD as a threshold-lowering device,
   by CATCH-20B(B1): even exponents are non-units and cannot cover
   `(Z/n)^*`; coverage at deeper levels concludes equidistribution, not
   periodicity. This pilot's negative closes round-18 residual 5.
3. **SP-COVER at official prime rows, at any level** — DEAD by
   CATCH-20B(B2): `w_cov = 2^41` and the best level threshold is
   `2^40.807`, both above the hard cap `w < 2^40`.
4. **CW-FLOOR at prime rows** — DEAD by §2.4: vacuous by 3.851 bits
   even at the most favourable admissible row.
5. **CC-sparsity as a lemma** — by CATCH E-2 it IS (ES) again at half
   length over a ternary alphabet.

**Alive — what could close it.**
- (a) **An `n`-uniform form of SP-COUPLE / SP-TERNARY.** SP-COUPLE
  explains every observed sub-`w_cov` emptiness exactly; what is
  missing is a length-uniform criterion for "no nonzero ternary
  codeword of `C_odd` admits a compatible `C_even` witness".
- (b) **A `p`-uniform CS.** CS's `w*` scales with `log2 p`; a version
  whose threshold does not degrade at the bottom of the live range
  would close both the residual bracket AND CATCH-20D's exposure.
- (c) **Raising the bracket's lower endpoint.** By §3.1 any improvement
  to RHL-LB moves `w` UP; pushing the endpoint above
  `w_tern(129.585) = 2^34.6467` would remove CATCH-20D outright. The
  printed construction is extremal, so this needs a NEW construction.
- (d) **Closing the `tau in (1, 1.585)` band.** THEOREM MT proves
  existence only below `tau = 1`; the live prime range sits entirely in
  `tau >= 1`. A proved statement anywhere in `(1, 1.585)` — in either
  direction — decides CATCH-20D.

---

## §5. Honesty ledger

- **Registered and FALSIFIED: G1.2** (level-`a` coverage monotone in
  `a`). 42 counterexample cells found and reported; the corrected law
  is stated in §1.3(B3) and the campaign conclusion is unchanged.
- **Registered and HELD:** G1.1, G1.3, G1.4 (as the divisibility
  corollary, unused because no level fires), G1.5, G1.6, G2.1, G2.2,
  G2.3, G2.4, G3.1, G3.2, G3.3, G3.4.
- **CATCH-20A** (`w_cov(11) = w_cov(19) = 6`, not 8) is a print error
  in `efloor_sparsity/REPORT.md:33` and COROLLARY SP5
  (`PROOFS.md:211-212`), which copied `2^{j_p}`; the corollary as
  printed stays TRUE but is not sharp, and the MINTED node prints no
  value for 11 or 19, so no minted statement is affected.
- **Scope of the censuses:** exhaustive over ALL `2^n` subsets at
  `n in {16, 32}`; nothing here is an `n`-extrapolation. Every
  prize-row statement in §1.3, §2.4, §3, §4 is a deduction from
  closed-form arithmetic or from theorems proved for all `n`.
- **CW-FLOOR's toys** are `L <= 8` with `2L in {8,12,16}`; the prize
  numbers in §2.4 are closed-form, not extrapolated.
- **COMPUTE LAW: no breaches.** Every `python3` invocation, including
  file patching and JSON/file peeking, went through
  `tools/ramguard tiny|local -- python3` with a literal `--`, from
  `/home/u2470931/smooth-read-solomin/prize`. No `git` write. No file
  written outside `notes/pilots_20260806/crossing_gap/` (verified:
  `find . -newermt '-3 hours' -type f` outside my dir returns empty).
  `gamma_shell/` never read; CAMPAIGN_LEDGER entries after the ROUND 20
  marker never read.
