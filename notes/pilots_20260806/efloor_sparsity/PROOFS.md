# PROOFS — E_floor SPARSITY: the small-prime end is a theorem

Round 18, 2026-08-06. Opus pilot, `notes/pilots_20260806/efloor_sparsity/`.
Everything here is registered in `PREREG.md` §E0-E9 **before** computation.
Machine-checked by `verify_sp.py` (fail-closed; the permanent `failclosed`
stage exits 1 by construction, every other stage exits 0).

---

## §0. Setup (unchanged from round 17)

`n = 2^m`, `h = n/2 = phi(n) = [K:Q]`, `K = Q(zeta_n)`, `O_K = Z[zeta_n]`,
`Phi_n(X) = X^h + 1`. `S <= Z/n`, `|S| = r'`,
`x_s = sum_{i in S} zeta^{si}`, `I_S = (x_1,...,x_{w-1})`,
`f_S(X) = sum_{i in S} X^i in F_p[X]` (the 0/1 indicator polynomial),
`delta = ord_n(p)`, `Z_w` = the `p`-cyclotomic closure of `{1,...,w-1}`,
`strat(S) = max{a >= 0 : S + n/2^a = S}`.

## §1. Facts CITED, not claimed (subtraction, hard law 5)

**(A1) The census identity.** `es_boundary_adversary/es_lib.py:23-28`,
quoted at `es_coprimality/PROOFS.md:27-33`:

> ```
>     S is a solution in characteristic p for SOME choice of primitive n-th
>     root of unity in F_{p^delta}
>       <=>  some prime P | p contains every x_s
>       <=>  gcd( Phi_n, V_1, ..., V_{w-1} )  has degree >= 1  in F_p[X]
>       <=>  p | N(I_S),   I_S = (x_1, ..., x_{w-1}) <= O_K.
> ```

**(A2) LEMMA Y (cyclic-code framing), BANKED round 14.**
`notes/pilots_20260804/mun_anticoncentration/PREREG.md:53-61`:

> ```
> - **(U1)** The crossing count is exactly a constant-weight count in an
>   explicit p-ary cyclic code:
>   W_w = { x in {0,1}^n <= F_p^n : wt(x) = r',  x in C(n, p, Z_w) }
>   where `C(n,p,Z_w)` is the cyclic code of length `n` over `F_p` with
>   defining zero set `Z_w` = the p-cyclotomic closure of `{1,...,w-1}`
>   mod `n`; `dim C = n - |Z_w|`, `w-1 <= |Z_w| <= delta (w-1)`.
>   This is LEMMA Y, BANKED round 14 — cited, not claimed.
> ```

**(A3) LEMMA Z.** `critical/nodes/b1_char0_giant_coset_theorem/node.json:9`,
status `PROVED`:

> "Over characteristic zero: every 0/1 t-null vector on mu_n (n = 2^s) is a
> union of mu_M-cosets with M > t."

At `t = 1` this is: `x_1 = 0` **iff** `S + n/2 = S` iff `strat(S) >= 1`.

**(A4) THEOREM CS (round 17).** `es_coprimality/PROOFS.md:202-225`:

> ```
> > **THEOREM CS.** Let `n = 2^m`, `p` an odd prime, `delta = ord_n(p)`,
> > `S <= Z/n` with `|S| = r'` and `x_1 != 0`. If `p | N(I_S)` then
> > p^{|Z_w^odd|}  divides  |N_{K/Q}(x_1)|                            (CS1)
> > and, unconditionally,
> > |N_{K/Q}(x_1)|^2  <=  ( r' - a_{n/2}(S) )^h ,   h = n/2.          (CS2)
> > Hence
> > |Z_w^odd| * log2 p  <=  (n/4) * log2( r' - a_{n/2}(S) ).          (CS3)
> ```

**(A5) The conjecture under attack.** `es_coprimality/PROOFS.md:367-379`:

> ```
> > E(n,r',w) = E_strat  u  E_floor,
> > E_strat = { S : 1 <= strat(S) < log2 M },        M = least 2-power >= w
> > E_floor = { S : some odd p | N_odd(I_S) has
> >                 |Z_w^odd(p)| log2 p <= (n/4) log2 r' }.
> > ... and moreover `|E_floor| / #orbits -> 0` as `w` grows ...
> ```

**Subtraction.** No banked node states a fixed-prime divisibility density
for `N(I_S)`; the `dli_wcl_weight3/weight4_ambient_exclusion` nodes prove
`v_2(q-1)>=41` gate emptiness by exhaustive resultant factorisation at
`n=512`, weights 3 and 4 only (`weight3/statement.md:8-32`), with no
small-prime and no density content. The naive density heuristic is
**already refuted in-repo** (`mun_anticoncentration/REPORT.md:102`:
*"(ACC) REFUTED — and the truth is better."*), so everything below is a
one-sided UPPER bound or an exact count, never a heuristic estimate.

---

## §2. LEMMA AB — the engine (odd conditions live on a ternary vector)

> **LEMMA AB.** Write `f_S = A + X^h B` with `deg A, deg B < h = n/2`, i.e.
> `A` is the indicator of `S n [0,h)` and `B` that of `S n [h,n)` shifted.
> Put `v := A - B in {-1,0,1}^h`. Then
>
> 1. `f_S = v (mod Phi_n)`, so for every **odd** `s`,
>    `f_S(xi^s) = v(xi^s)` for any primitive `n`-th root `xi` in char `p`;
> 2. `v = 0  <=>  S + n/2 = S  <=>  strat(S) >= 1`, for every odd `p`;
> 3. the number of `S` with a given `v` is exactly `2^{z(v)}`, where
>    `z(v) = #{i : v_i = 0}`.

**Proof.** (1) `X^h = -1 (mod Phi_n)`, so `f_S = A - B (mod Phi_n)`; a
primitive `n`-th root of unity is a root of `Phi_n` (in char `p` odd,
`X^n-1` is separable), and odd `s` makes `xi^s` primitive again.
(2) `v = 0` in `F_p^h` means `A_i - B_i = 0` in `F_p` with
`A_i, B_i in {0,1}`, so `A_i - B_i in {-1,0,1}` and `p >= 3` forces
`A_i = B_i` as integers, i.e. `i in S <=> i + h in S`.
(3) Given `v`, each coordinate with `v_i = 0` has the two lifts
`(A_i,B_i) in {(0,0),(1,1)}` and each `v_i = +-1` has exactly one. QED

**This is the whole engine.** It converts the a=0 question ("is there a
non-periodic bad set?") into: *does the ternary vector `v != 0` satisfy the
odd window conditions?* Note `{-1,0,1} = F_3`, so the ternary constraint is
**vacuous exactly when `p = 3`** — which is why `p = 3` is the hard prime
and needs §3, while `p >= 5` also admits §5.

*Machine check:* `verify_sp.py tern` — the identity
`#{S : odd conditions, strat=0} = sum_{v != 0} 2^{z(v)}` verified against
the independent meet-in-the-middle census in **all 56 cells**
(`n in {16,32}`, `p in {3,5,7,17}`, `w in [2,8]`), 112 checks, 0 failures.

---

## §3. THEOREM SP-COVER — the first sparsity theorem

> **THEOREM SP-COVER.** Let `n = 2^m`, `p` odd, and suppose **every coset of
> `<p>` in `(Z/n)^*` contains an odd `s` with `1 <= s <= w-1`.** Then for
> every `S <= Z/n` with `strat(S) = 0`,
> ```text
> p  does not divide  N(I_S).
> ```
> Equivalently: `p | N(I_S)` forces `S + n/2 = S`.

**Proof.** Suppose `p | N(I_S)`. By the census identity (A1) there is a
primitive `n`-th root `xi` in `F_{p^delta}` with `f_S(xi^s) = 0` for
`s = 1,...,w-1`. Since `f_S in F_p[X]`, Frobenius gives
`f_S(xi^{ps}) = f_S(xi^s)^p = 0`, so `f_S(xi^s) = 0` for every `s` in the
`<p>`-closure, in particular for every `s` in the `<p>`-closure of the odd
part of the window. By hypothesis that closure is **all of `(Z/n)^*`**, so
`f_S` vanishes at *every* primitive `n`-th root of unity, i.e.

```text
Phi_n(X) = X^h + 1  divides  f_S(X)  in F_p[X].
```

By LEMMA AB(1), `f_S = v (mod Phi_n)` with `v = A - B`, so `v = 0`, and by
LEMMA AB(2) `strat(S) >= 1`. Contrapositive: `strat(S) = 0` implies
`p` does not divide `N(I_S)`. QED

*(The case `N(I_S) = 0` is not an escape: `strat(S) = 0` gives `x_1 != 0`
by LEMMA Z (A3), so `I_S != 0` and `N(I_S) != 0`.)*

Define `w_cov(p,n) := 1 + max over <p>-cosets of the least element` (every
element of `(Z/n)^*` is odd because `n` is a 2-power), so SP-COVER applies
exactly when `w >= w_cov(p,n)`.

### §3.1 LEMMA COS — `w_cov` is `n`-uniform and bounded by `p^2`

> **LEMMA COS.** Put `j_p := v_2(p^2 - 1) (>= 3)`. For `m >= j_p`,
> `<p>` contains `U_{j_p} := {s : s = 1 mod 2^{j_p}}`, so the coset of `s`
> in `(Z/2^m)^*/<p>` depends only on `s mod 2^{j_p}`. Consequently
> ```text
> w_cov(p, 2^m)  is independent of m for m >= j_p,   and
> w_cov(p, 2^m)  <=  2^{j_p}  <=  p^2 - 1.
> ```

**Proof.** `p` odd gives `p^2 = 1 (mod 8)`, so `j_p >= 3`. For `2 <= j < m`
the group `U_j = 1 + 2^j Z/2^m` is cyclic of order `2^{m-j}` and any `u`
with `v_2(u-1) = j` exactly generates it. Since `v_2(p^2-1) = j_p`, we get
`<p^2> = U_{j_p}`, hence `<p> ⊇ U_{j_p}`. Therefore the quotient map
`(Z/2^m)^* -> (Z/2^m)^*/<p>` factors through
`(Z/2^m)^*/U_{j_p} = (Z/2^{j_p})^*`: the coset of `s` is a function of
`s mod 2^{j_p}`. The odd integers `1,3,...,2^{j_p}-1` realise **every**
odd residue mod `2^{j_p}`, hence every coset, so a window with
`w - 1 >= 2^{j_p} - 1` covers. Finally `2^{j_p} | p^2 - 1` gives
`2^{j_p} <= p^2 - 1`. QED

> **THEOREM SP-UNIFORM.** If `w >= 2^{v_2(p^2-1)}` then `p` divides no
> `N(I_S)` with `strat(S) = 0`. Contrapositive — **the small-prime end of
> the bad-prime range, which was previously unbounded below:**
> ```text
> p | N(I_S)  and  strat(S) = 0   ==>   2^{v_2(p^2-1)} > w   ==>   p > sqrt(w+1).
> ```

Together with round 17's COROLLARY CS-EXCL (which bounds bad primes from
**above**), the bad-prime range at stratum `a = 0` is now **two-sided**:

```text
sqrt(w+1)  <  p  <=  r'^{ n / (4 ceil((w-1)/2)) }.
```

### §3.2 The named corollaries (the mandate's `p = 3, 7, 17`)

`verify_sp.py cover` computes `w_cov(p,2^m)` for `m = 4..12`, checks
`w_cov <= 2^{j_p}` and `n`-uniformity (each a machine check):

| `p` | `j_p = v_2(p^2-1)` | `2^{j_p}` | `w_cov(p,2^m)`, `m = 4..12` |
|---|---|---|---|
| **3** | 3 | 8 | **6, 6, 6, 6, 6, 6, 6, 6, 6** |
| **5** | 3 | 8 | **4, 4, 4, 4, 4, 4, 4, 4, 4** |
| **7** | 4 | 16 | **12, 12, 12, 12, 12, 12, 12, 12, 12** |
| 11 | 3 | 8 | 6, 6, 6, 6, 6, 6, 6, 6, 6 |
| 13 | 3 | 8 | 4, 4, 4, 4, 4, 4, 4, 4, 4 |
| **17** | 5 | 32 | **16, 16, 16, 16, 16, 16, 16, 16, 16** |
| 19 | 3 | 8 | 6, 6, 6, 6, 6, 6, 6, 6, 6 |
| 23 | 4 | 16 | 12, 12, ... |
| 47 | 5 | 32 | 8, 24, 24, ... |
| 97 | 6 | 64 | 16, 32, 32, ... |
| 257 | 9 | 512 | 16, 32, 64, 128, 256, 256, ... |

> **COROLLARY SP3.** For every `m >= 3` and every `w >= 6` and every `r'`:
> `3 | N(I_S)` forces `strat(S) >= 1`. **`p = 3` contributes NOTHING to
> `E_floor` outside `E_strat`, at every `n`, for all `w >= 6`.**
>
> **COROLLARY SP5.** Same with `w >= 4` for `p = 5`; `w >= 12` for `p = 7`;
> `w >= 16` for `p = 17`; `w >= 8` for `p in {11,19}`; `w >= 4` for `p = 13`.

The reason `p = 3` needs `w >= 6` and not less is exact and visible in
LEMMA COS: `<3> = {s = 1,3 mod 8}` (index 2), so the second coset's least
odd element is `5`, and the window must reach it.

### §3.3 Machine verification of SP-COVER — EXHAUSTIVE, not sampled

`verify_sp.py cover` runs the meet-in-the-middle census of §5, which is
exact over **all `2^n` subsets** at `n = 16` and `n = 32`, split into
`strat >= 1` and `strat = 0`:

| `n=32`, `p=3` | w=2 | w=3 | w=4 | **w=5** | **w=6** | w=7 | w=8..12 |
|---|---|---|---|---|---|---|---|
| bad, all `S` | 1048576 | 4096 | 4096 | 128 | 64 | 64 | 64/4 |
| bad, periodic | 65536 | 1024 | 1024 | 64 | 64 | 64 | 64/4 |
| **bad, `a=0`** | 983040 | 3072 | 3072 | **64** | **0** | **0** | **0** |

`w_cov(3,32) = 6` and the `a=0` bad set is nonempty at `w = 5` and empty
from `w = 6` on: **SP-COVER is sharp at `(n=32, p=3)`.** Every SP-COVER
emptiness check passes at `n in {16,32}` for `p in {3,5,7,17}` and every
`w in [w_cov, 12]` — **0 failures**, and again at `n = 64` (§6).

**REGISTERED PREDICTION (P2) MISSED — reported, not buried.** I registered
in `PREREG.md` §E1 that `w_cov` would be **sharp**, i.e. that a `strat=0`
witness would exist at `w = w_cov - 1`. It does at `(n=32, p=3)` — and
**nowhere else**: at `(16,3)`, `(16,5)`, `(16,7)`, `(32,5)`, `(32,7)` the
`a=0` class is already empty below `w_cov`. **5 of 6 registered sharpness
cells missed.** SP-COVER's hypothesis is therefore *sufficient but not
necessary*; the true exclusion threshold is often smaller, and §5 explains
why (the ternary mechanism, which is invisible to a covering argument and
bites earlier for every `p >= 5`). The theorem itself passed every one of
its own checks; it is my prediction about its tightness that was wrong.

**The `a=0` mass at `n=32, p=3`, by weight `r'` (new: round 17 measured
only `r' <= 8`):**

```
w=2 : (3,32) (5,416) (6,384) (7,2496) (8,3840) (9,11200) (10,17280) (11,37216) (12,50176) (13,84192) (14,97024) (15,126592) ...
w=3 : (7,32) (9,32) (11,128) (13,384) (14,256) (15,448) (16,512) (17,448) (18,256) (19,384) (21,128) (23,32)
w=4 : identical to w=3        (s=3 is Frobenius-free: 3 in <3>)
w=5 : (15,32) (17,32)
w>=6: EMPTY
```

Every count is a multiple of `n = 32`, independently reproducing the banked
quantization law (`mun_anticoncentration/REPORT.md:102`: *"Accidental
counts are **quantized in multiples of `n`**"*).

---

## §4. CATCH E-1 — `E_floor` is a TAUTOLOGY given THEOREM CS

> **PROPOSITION TAUT.** On the stratum `strat(S) = 0`,
> ```text
> E_floor  =  { S : N_odd(I_S) > 1 }   exactly.
> ```

**Proof.** (⊇) Let `strat(S)=0` and `N_odd(I_S) > 1`; pick an odd prime
`p | N_odd(I_S)`. By LEMMA Z (A3), `strat(S)=0` gives `x_1 != 0`, so
THEOREM CS applies and yields (CS3)
`|Z_w^odd| log2 p <= (n/4) log2(r' - a_{n/2}(S)) <= (n/4) log2 r'`
because `a_{n/2}(S) >= 0`. That is precisely the `E_floor` predicate, so
`S in E_floor`. (⊆) If `S in E_floor` some odd `p` divides `N_odd(I_S)`,
so `N_odd(I_S) >= p > 1`. QED

**Consequence, stated plainly.** The round-17 decomposition
`E = E_strat u E_floor` is a **restatement, not a reduction**: the floor
inequality is *derived* by CS for every bad prime, so membership in
`E_floor` carries no information beyond non-coprimality itself. Hence
"CC-sparsity" is **exactly** as hard as the original open lemma
(`F3_SHALLOW_LADDER.md:200-202`, *"ONE open lemma (pair-coprimality /
norm-gate sparsity) stands between the data and the theorem"*). Nothing is
hidden in the decomposition. This does not touch THEOREM CS itself, whose
prize-row content (CS-EXCL) is unaffected.

*Machine check:* `verify_sp.py floor` — at `n = 32`, `r' in {5,6}`,
`w in {3,4,5}`, over affine orbit reps weighted by orbit size: the sets with
`N_odd > 1` and the sets in `E_floor` agree **exactly** in all 6 cells, and
the CS floor predicate holds for **every** odd prime dividing `N_odd`
(25 checks, 0 failures). Re-verified at `n = 64` (874 checks, 0 failures).

---

## §5. THEOREM SP-TERNARY — a certified criterion strictly stronger than
SP-COVER for `p >= 5`

By LEMMA AB the odd-window conditions are conditions on `v in {0,+-1}^h`.
Let `C_odd(n,p,w) := { v in F_p^h : v(xi^s) = 0 for all odd s in [1,w-1] }`,
a cyclic (negacyclic) code of length `h` and codimension
`deg G = delta * #{<p>-cosets met by the odd window}`.

> **THEOREM SP-TERNARY.** If `C_odd(n,p,w)` contains **no nonzero vector
> with all coordinates in `{0,+-1}`**, then `p` divides no `N(I_S)` with
> `strat(S) = 0`. Moreover, exactly,
> ```text
> #{ S : strat(S)=0, odd conditions hold } = sum over nonzero ternary
>                                            v in C_odd of 2^{z(v)}.
> ```

**Proof.** Immediate from LEMMA AB: a bad `S` gives `v = A - B` ternary and
in `C_odd`; `strat(S) = 0` gives `v != 0`; the multiplicity is `2^{z(v)}`.
SP-COVER is the special case `C_odd = {0}` (full coverage forces
`deg G = h`). QED

**Exact ternary counts** (`verify_sp.py tern`, cross-checked against the
independent MITM census in every cell):

| `n=32` | `p=3` | `p=5` | `p=7` | `p=17` |
|---|---|---|---|---|
| `w=2` nonzero ternary codewords | 6560 | **0** | 16640 | 148224 |
| `w=4` | 6560 | **0** | 288 | 288 |
| `w=6` | **0** | **0** | 288 | **0** |
| `w=8` | **0** | **0** | 288 | **0** |
| SP-TERNARY excludes from `w` = | 6 (`=w_cov`) | **2** | never (`<=8`) | 6 |

**Reading.** For `p = 3` the ternary constraint is vacuous (`F_3` *is*
`{0,+-1}`), so SP-TERNARY degenerates to SP-COVER — `p = 3` is genuinely
the extremal prime. For `p = 5` it excludes already at `w = 2`, far below
`w_cov = 4`. For `p = 7` the odd conditions alone never suffice in the
tested range, yet the census shows the `a=0` set empty from `w = 7`: there
the **even** window conditions do the work.

**Honest scope:** SP-TERNARY is a *certified criterion*, verified instance
by instance. Its `n`-uniformity is **NOT** established; SP-COVER (§3) is the
`n`-uniform theorem.

**An anomaly worth recording (lead).** At `n = 32`, `p = 5`, `w = 2` the
code `C_odd` has `3^{16} = 4.3e7` ternary candidates mapping into
`5^8 = 3.9e5` syndromes, so a flat model predicts about **110** nonzero
ternary codewords. The exact count is **0**. This is the same
"suppression arrives 1-2 orders of magnitude early" phenomenon banked at
`mun_anticoncentration/REPORT.md:111`, now visible at the ternary level.

---

## §6. CATCH E-2 — `E_floor` sparsity is a SELF-SIMILAR copy of (ES)

LEMMA AB + THEOREM SP-TERNARY identify the object that must be counted:

```text
(ES)                : # 0/1 vectors of length n   in a cyclic F_p-code    -> conjectured structural
E_floor sparsity    : # {0,+-1} vectors of length n/2 in a cyclic F_p-code -> conjectured 0/sparse
```

They are the **same shape**: constant-alphabet vectors in a `p`-ary cyclic
code with a consecutive defining set. So the conjecture invoked to close
(ES) is a copy of (ES) itself at half the length over a ternary alphabet.
**CC-sparsity is not a lemma below (ES); it is (ES) again.** That is the
structural reason the round-17 conditional (K5) could not be discharged by
elementary means, and it is a scope warning for anyone planning to close
the residual 28.84% of the crossing bracket by proving CC-sparsity.

---

## §7. THEOREM SPD — the natural density route, PROVED and VACUOUS

Registered in `PREREG.md` §E2. I prove it, and then show it is numerically
empty everywhere — reported as a negative result, not omitted.

> **THEOREM SPD.** Fix odd `p`, `n`, `w`, `r'`; put `theta = r'/n`,
> `D = |Z_w|`, `gamma = sqrt(1 - 2 theta(1-theta)(1 - cos(2 pi/p)))`, and
> let `d` be any lower bound on the minimum distance of the dual code
> `C(n,p,Z_w)^perp`. Then, for one prime `P | p`,
> ```text
> #{S : |S| = r', f_S in C} / C(n,r')  <=  (n+1) ( p^{-D} + gamma^{d} ),
> ```
> and a union bound over the `e = n/(2 delta)` primes above `p` multiplies
> the right side by `e`.

**Proof.** Let `X_i` be i.i.d. Bernoulli(`theta`) and `c = (X_i)`. For
`phi in F_p^n`, `E[e_p(<phi,c>)] = prod_i (1 - theta + theta w^{phi_i})`
with `w = e^{2 pi i/p}`, and
`|1 - theta + theta w^a|^2 = 1 - 2 theta(1-theta)(1 - cos(2 pi a/p))
<= gamma^2` for `a != 0` (the maximum of `cos(2 pi a/p)` over `a != 0` is
at `a = +-1`). Hence `|E[e_p(<phi,c>)]| <= gamma^{wt(phi)}`. Orthogonality
gives
`P[c in C] = p^{-D} sum_{phi in C^perp} E[e_p(<phi,c>)]
<= p^{-D}(1 + (p^D - 1) gamma^{d}) <= p^{-D} + gamma^{d}`.
Conditioned on `wt(c) = r'`, `c` is uniform on weight-`r'` vectors, so
`P[c in C] >= P[wt(c) = r'] * N_{r'}/C(n,r')`, and `P[wt(c) = r'] >=
1/(n+1)` because the binomial pmf with mean `r'` is maximised at `r'` and
has `n+1` atoms. QED

> **BCH bound (classical, proved here for self-containment).** If the
> defining set of a cyclic code of length `n` contains `l` consecutive
> elements then its minimum distance exceeds `l`.
> *Proof.* A codeword of weight `<= l` supported on `i_1 < ... < i_l`
> satisfies `sum_k c_{i_k} (xi^{i_k})^{b+j} = 0` for `j = 0..l-1`; the
> matrix `(xi^{(b+j) i_k})` is `diag(xi^{b i_k})` times a Vandermonde in the
> distinct nodes `xi^{i_k}`, hence invertible, so `c = 0`. QED

Applying it to `C^perp` (defining set `Z/n \ (-Z_w)`, of size `n - |Z_w|`;
removing `|Z_w|` points from a cycle leaves a run of length at least
`(n - |Z_w|)/|Z_w|`) gives `d >= n/|Z_w|`.

**VERDICT: vacuous, in every regime, and provably so.** The bound is
non-trivial only when `(n+1) e gamma^{d} < 1`, i.e. roughly
`d * log(1/gamma) > log n`, and `log(1/gamma) ~ pi^2 theta(1-theta)/p^2`.
With `d ~ n/|Z_w| <= n/(w-1)` this needs
```text
n / ( (w-1) p^2 )  >~  log n,
```
which fails for `p = 3` at every `n` (there `|Z_w| >= delta = n/4`, so
`d <= 4`), and fails at the prize rows for every `p` (there `p ~ 2^256`).
**So the theorem shape registered in the coordinator brief — "a union bound
over the FINITE bad-prime range that CS3 leaves alive" — cannot be closed
by the standard character-sum/BCH tool.** This is exactly the outcome I
pre-registered in `PREREG.md` §E9.3, and it is the honest (S1) verdict:
the two ENDS of the prime range are theorems, the MIDDLE is untouched.

---

## §8. (S2) The adversarial half — the densest family, and the trade-off law

> **LEMMA QS (the quarter-shift family F1).** Let `S = T u (T + n/4)` with
> `T n (T + n/4) = empty`. Then `x_s = 0` for **every** `s = 2 (mod 4)`.
> *Proof.* `x_s = (1 + zeta^{s n/4}) * sum_{i in T} zeta^{si}` and
> `zeta^{n/4}` is a primitive 4th root of unity, so `1 + i^s = 0` exactly
> when `s = 2 (mod 4)`. QED  These `S` have `strat(S) = 0` in general.

Measured exactly at `n = 32`, `r' = 6` (`verify_sp.py dense`; `E_floor`
membership decided by the banked exact HNF ideal norm, i.e. over **all**
characteristics at once):

| family | `w` | size | `a=0` tested | in `E_floor` | internal density | share of total `a=0` floor mass | exact? |
|---|---|---|---|---|---|---|---|
| **BASELINE (all `C(32,6)`)** | 3 | 906192 | 905632 | 6528 | 0.00721 | 100% | EXACT (orbit-weighted) |
| **F1 quarter-shift** | 3 | **3808** | 3808 | **3200** | **0.84034** | **49.0%** | **EXACT** |
| F2 shift `j=3` / `j=4` | 3 | 4032 | 4032 | 0 | 0 | 0 | EXACT |
| F3 symmetric `S=-S` | 3 | 560 | 546 | 0 | 0 | 0 | EXACT |
| F5 AP supports | 3 | 448 | 448 | 0 | 0 | 0 | EXACT |
| F4 multiplier-inv `u=17` | 3 | 25984 | 5084 | 106 | 0.02085 | ~8% (est.) | SUBSAMPLE 5197/25984 |
| F6 coset-near `M=2` | 3 | 44240 | 5496 | 0 | 0 | 0 (est.) | SUBSAMPLE 5530/44240 |
| F7 antipodal-loaded | 3 | 349440 | 5923 | 28 | 0.00473 | ~25% (est.) | SUBSAMPLE 5923/349440 |
| **every family, and the baseline** | **4** | — | — | **0** | **0** | — | as above |

**Honesty note on the three SUBSAMPLE rows.** F4, F6 and F7 exceed the
6000-set cap that keeps a cell inside `ramguard local`, so they were
measured on a deterministic stride subsample and their shares are
*estimates*. In particular **the zeros for F6 are not exact zeros** — a
null from a subsample is not a null for the family (round-16 rule). The
headline result (F1) and the four other families are exact, unsampled
counts, as is the baseline.

**Findings.**

1. **F1 is the densest floor family found: 0.42% of the sets carry 49% of
   the entire `a=0` floor mass**, with an internal density `116x` the
   baseline. Its mechanism is LEMMA QS: at `w = 3` it annihilates the
   `s = 2` condition, so it is a `w = 2` instance wearing a `w = 3`
   costume — the same phenomenon round 17 recorded as CATCH-17C.
2. **No family refutes CC-sparsity.** Every constructed family is
   exponentially small in `n` (F1 has `~7^{n/4}` members against `2^n`),
   so `|F n E_floor| / C(n,r') -> 0`; the registered falsifier of
   `PREREG.md` §E5 was **not** triggered.
3. **The trade-off law (measured, not proved).** A family that annihilates
   `k` window conditions gains a factor `~p^{k delta}` in internal floor
   density and pays an exponential-in-`n` factor in size. At
   `(32,6,3)`: F1 pays `2^{-7.9}` in size, gains `2^{+6.9}` in density,
   net `2^{-1.0}` — it cannot win, and one step of `w` destroys the gain
   entirely (F1 at `w = 4`: **zero**).

---

## §9. (S3) The `n`-asymptotic — round 16's flag CLOSED

Round 16's honest flag, `es_boundary_adversary/REPORT.md:106`:
> **n=64 was registered in my grid and never executed.** A null from an
> unreached regime is not evidence.

**Executed, exactly, two independent ways.**

**(a) All-characteristic exact census at `n = 64`** (`verify_sp.py n64all`,
banked HNF ideal norm + full factorisation, affine orbits weighted by orbit
size; complete over **every** characteristic, no prime list):

| `r'` | `w` | orbits | `a=0` sets | `E_floor` | density | bad primes at `a=0` |
|---|---|---|---|---|---|---|
| 3 | 2 | 35 | 41664 | 37760 | 0.906298 | 3,7,17,47,97,193,257,353,449,641 |
| 3 | **3,4,5** | 35 | 41664 | **0** | **0.000000** | **none** |
| 4 | 2 | 399 | 634880 | 546560 | 0.860887 | 7,17,31,47,79,97,193,223,257,353 |
| 4 | **3,4,5** | 399 | 634880 | **0** | **0.000000** | **none** |

874 checks, 0 failures — including a check that **every** bad prime found
satisfies both the CS floor predicate and SP-UNIFORM (`2^{v_2(p^2-1)} > w`).

**(b) Exact per-prime census at `n = 64` (`r' <= 6`, `w <= 12`) and at
`n = 128` (`r' <= 4`, `w <= 8`)** — meet in the middle, exact, no sampling
(`verify_sp.py n64`; 155 + 148 checks, 0 failures):

| `n` | `p` | `w_cov` | `a=0` at `w=2` | `a=0` at `w=3` | `a=0` at `w>=4` |
|---|---|---|---|---|---|
| 64 | 3 | 6 | 3712 (`r'=3,5,6`) | **0** | **0** |
| 64 | 5 | 4 | **0** | **0** | **0** |
| 64 | 7 | 12 | 5568 (`r'=3..6`) | 64 (`r'=6`) | **0** |
| 64 | 17 | 16 | 20032 (`r'=3..6`) | 512 (`r'=5,6`) | **0** |
| 128 | 3 | 6 | 128 (`r'=3`) | **0** | **0** |
| 128 | 5 | 4 | **0** | **0** | **0** |
| 128 | 7 | 12 | 256 (`r'=3,4`) | **0** | **0** |
| 128 | 17 | 16 | 896 (`r'=3,4`) | **0** | **0** |

**Verdict.** Round 16's `n = 64` flag is **CLOSED**, and `n = 128` is
reached as a bonus. At `n = 64` the `a=0` exceptional class is empty for
every `w >= 3` at `r' <= 4` **over all characteristics**, and empty for
`w >= 4` at `r' <= 6` for `p in {3,5,7,17}`. At `n = 128`, `r' <= 4`, it is
empty for every `w >= 3` for all four primes.

**The `n`-trend is a strengthening, and it is visible twice.** In the
all-weights census the last `a=0` witness moves *later* with `n`
(`w = 4` at `n=16`, `w = 5` at `n=32`, both `p=3`) — the class survives
longer because there are more weights available. At **fixed** small `r'`
the opposite and more relevant trend holds: the class empties *earlier*
with `n` (e.g. `p = 17`, `r' <= 6`: last witness at `w = 3` for `n = 64`,
gone by `w = 3` for `n = 128`), and all `w >= 2` bad counts at fixed `r'`
shrink by roughly an order of magnitude per doubling of `n`
(`p=17, w=2`: 20032 at `n=64` -> 896 at `n=128` restricted to `r' <= 4`).
Note also that **every** `a=0` count in the table is a multiple of `n`.

---

## §10. (S4) The u2c conversion statement

`background/nodes/u2c_giant_tnull_dichotomy/node.json:6` is
`"status": "CONDITIONAL"`, and the credit at stake is, verbatim from
`node.json:8`:

> "| SURVIVAL +2 (2026-07-07, F2-A2): engineered accident-selection (the dli
> round-5 norm-gate transported; 1440 trials, positively controlled against
> the known p=257 window accident) finds ZERO candidate sub-balance primes —
> the multi-condition ideals are generically coprime; the engineering
> channel is structurally empty, mirroring the E2 finding."

> **THE CONVERSION STATEMENT.** The 1440-trial credit becomes mathematics
> if and only if one proves, at the official row parameters
> (`n = 2^41`, `r' = 2^40 - w`, `q` prime with `v_2(q-1) >= 41`):
> ```text
> (CONV)  for every S <= Z/n with strat(S) = 0,  q does not divide N(I_S).
> ```
> By the census identity that is exactly "no engineered accident exists at
> `q`", which is what the trials probed.

**How far this pilot gets toward (CONV): the two ends, not the middle.**

* SP-UNIFORM proves (CONV) for every `q` with `2^{v_2(q^2-1)} <= w` —
  i.e. all `q <= sqrt(w+1)`, which at the bracket ends is
  `q <= 2^17.00` (`w = 2^34`) up to `q <= 2^19.50` (`w = 2^39`).
* CS-EXCL (round 17) proves (CONV) for all `q` above the CS3 floor.
* **The official `q` is in neither end, and provably so.** The official row
  gate `v_2(q-1) >= 41` forces `j_q = v_2(q^2-1) = v_2(q-1) + 1 >= 42`, so
  SP-COVER needs `w >= 2^42` while the bracket caps at `w = 2^39`
  (`verify_sp.py prize`, 5 checks, 0 failures):

```
v_2(q-1)=41 -> SP-COVER needs w >= 2^42 ; bracket caps at 2^39  -> VACUOUS
CS-EXCL threshold w* = 170752922588 = 2^37.3131  (reproduces round 17)
UNCOVERED segment w in [2^34, 2^37.3131];  GAP to SP-COVER = 2^4.6869 in w
```

> **CATCH E-3 (structural, campaign-relevant).** The official-row condition
> `v_2(q-1) >= 41` — which the code construction *requires*, since the row
> needs `2^41`-th roots of unity in `F_q` — is **exactly** the condition
> that makes SP-COVER vacuous. The row primes are the worst possible primes
> for the coset-covering mechanism, and this is not an accident of the
> proof: `<q>` has index `2^{v_2(q^2-1)-2}`-ish in `(Z/n)^*`, so a large
> `v_2(q-1)` means many cosets to cover and a correspondingly long window.
> Any future attempt to close the residual `28.84%` of the bracket by a
> covering/periodicity argument must first defeat this obstruction.

---

## §11. What remains (honest)

1. **The middle of the prime range is untouched.** The theorems here close
   `p <= sqrt(w+1)`; CS-EXCL closes the top. Nothing closes
   `sqrt(w+1) < p <= r'^{n/(4 ceil((w-1)/2))}`, and §7 proves the natural
   character-sum tool cannot. This is the honest (S1) verdict.
2. **CC-sparsity is not proved and is not easier than (ES)** (§6). The
   round-17 conditional (K5) should be read with §4 and §6 attached.
3. **SP-TERNARY has no `n`-uniform form.** It is an exact certified
   criterion per `(n,p,w)`, not a theorem in `n`.
4. **The `p = 5` ternary anomaly is unexplained** (§5): a flat model
   predicts ~110 codewords and the truth is 0.
5. **Scale.** Exhaustive over all `2^n` subsets at `n in {16,32}`; at
   `n = 64` exhaustive over `r' <= 4` (all characteristics) and `r' <= 6`
   (`p in {3,5,7,17}`); `n = 128` only at `r' <= 4`. The prize row is
   `n = 2^41` — §3 and §10 are deductions from theorems proved for all `n`,
   not extrapolations, but no measurement validates them at `n = 2^41`.
6. **Even-window conditions are used nowhere in the proofs.** The census
   shows they matter (`p = 7` at `n = 32` empties at `w = 7`, while the odd
   conditions alone never suffice below `w = 9`). A version of SP-COVER
   using the even conditions would lower every threshold and is the most
   obvious next step.
7. **`w = 3` remains the hard row**, as in round 17: SP-COVER first bites
   at `w >= 4` (`p = 5, 13`) and `w >= 6` (`p = 3`), so the `w = 3`
   collapse still has no proof.
