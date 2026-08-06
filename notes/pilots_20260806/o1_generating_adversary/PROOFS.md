# (O1) ON GENERATING ROWS — the adversarial proofs

Round 18, 2026-08-06. Pilot `notes/pilots_20260806/o1_generating_adversary/`.
Verifier `verify.py`, stages S0-S10, **187 PASS, 0 FAIL**, digest
`O1_GEN_ADVERSARY_ALL_PASS`. Log `VERIFY_LOG.txt`.
Run: `tools/ramguard local -- python3 notes/pilots_20260806/o1_generating_adversary/verify.py`.

Notation. `n = 2^41`, `q = p^e = |F|`, `L := log2 q`, `e_p := v_2(p-1)`,
`k := ord_n(p)`, `D := log2 k`, `m := |W|/2`, `T := {-1,0,1}^m`,
`t` the Newton parameter, `R := |Lambda_K1|`, `S := 2^{e_p-1}`,
`C := k` (nested top window), `Delta := dim_{F_p} L * log2 p - m` (bits).
**GENERATING** means `k = e`, i.e. `F_p(mu_n) = F_q`.

**The two live `Lambda`-parity readings** (`t_naming` CATCH-E; both live):

- **reading A** — `t` is the largest Newton index, the ambient condition set
  is `Lambda_full = {1..t}`, and the K1 sector is its ODD part, so
  `R = |Lambda_K1| = ceil(t/2)`. (`f2_adm`'s reading; `t_naming`'s 5-to-1
  favourite.)
- **reading B** — `R = |Lambda_K1| = t`.

Every statement below names the reading it needs.

---

## 0. Surfaces (verbatim, each machine-checked at its line by S0)

`critical/nodes/rules_freeze/statement.md:9`:

> THE RULES-FACT (closed by citation, not proof): the operative prize rules are exactly — smooth domain = coset of a power-of-2-order subgroup; k <= 2^40; |F| < 2^256; rates EXACT in {1/2, 1/4, 1/8, 1/16} ...

`notes/pilots_20260806/f2_tq_pin/PROOFS.md:114` (the admissible region):

> ```
>     v_2(e) <= 2,      e <= 6,      log2 p >= 39,
> ```

`notes/pilots_20260806/f2_tq_pin/PROOFS.md:174` (the crude balance):

> ```
>                         t · L  >=  n .                                (C)
> ```

`notes/pilots_20260806/f2_tq_pin/PROOFS.md:182` (the exact FM+gate balance):

> ```
> >    = min { t : t * L  >=  log2 C(n, n-k-t) + 128 }.                        (T*)
> ```

`notes/pilots_20260804/f2_opening/PROOFS.md:94` (the unconditional floor),
`:219` (LEMMA 3's inequality), `:225` (LEMMA 3's conclusion),
`:56` (`Z(L)`), `:273` (class G = *"both parity parts nonzero"*).

`notes/pilots_20260806/f2_adm/PROOFS.md:184-185`:

> ```
> >   (iii) dim_{F_p} L  =  C · min(S, R)      EXACTLY,
> >   (iv)  Z(L)  =  prod_c Z_c  =  Z_1^C .
> ```

`notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:99` (SL-1: `wt >= R+1`),
`:36` (*"`w >= 2R+1` is **twice** the bound proved below"*),
`:171` (*"**`char > w` fails by two orders of magnitude.**"*),
`:240` ((M2)), `:247` ((M3)).

`background/nodes/dli_wcl_newton_short_window_exclusion/statement.md:8-22`
(PROVED, the stronger sibling; quoted in full in §3.1).

`notes/pilots_20260802/f2_fixed_sector/REPORT.md:31`:

> **Theorem A (per-sector parity trichotomy, proved, elementary)**: every sector is antipodally closed; per sector G / K1 / K2 as above; ...

`notes/pilots_20260802/f2_deployed_windows/REPORT.md:55`:

> ... the degenerate class is exactly {c : even-part trace-zero on the sector} — codim_j = min(m_j, t/2) F_p-conditions.

---

## 1. (V4, RUN FIRST) THE GENERATING CENSUS — is the surviving scope vacuous?

### THEOREM G1 (the census). *Verified: S1.1-S1.5.*

> At `n = 2^41` an admissible row is GENERATING (`k = ord_n(p) = e`) **iff**
>
> ```
>     (e_p, e, k)  in  { (>= 41, 1, 1),  (40, 2, 2),  (39, 4, 4) }.
> ```
>
> In particular `e in {3, 5, 6}` can **NEVER** generate.

*Proof.* `(Z/2^41)^*` has order `2^40`, so `k = ord_n(p)` is a **2-power**
(S1.1, exhaustively on a surrogate modulus). `F_p(mu_n) = F_{p^k}` is a
subfield of `F_q`, so `k | e`. Hence `k = e` forces `e` to be a 2-power;
with `e <= 6` (`f2_tq_pin:114`) this leaves `e in {1,2,4}`.

Admissibility forces `e_p >= 39 >= 2`, i.e. `p ≡ 1 (mod 4)`, so LTE gives
`v_2(p^j - 1) = e_p + v_2(j)` and therefore `k = 2^{(41-e_p)_+}` (S1.2,
verified for every prime `p ≡ 1 mod 4` below 3000 and every `A <= 13`).
Setting `k = e`:

```
   e = 1  <=>  2^{(41-e_p)_+} = 1  <=>  e_p >= 41
   e = 2  <=>  41 - e_p = 1        <=>  e_p = 40
   e = 4  <=>  41 - e_p = 2        <=>  e_p = 39
```

and in each case `v_2(q-1) = e_p + v_2(e) = 41` exactly, so `n | q-1` holds
with no slack. QED

**COROLLARY G1.1.** `f2_adm` CATCH-4's empty class `(e_p,e) = (40,6)` was
never inside `(O1)`'s surviving scope in the first place: `k = 2 != 6 = e`,
so it is non-generating whether or not it is empty. The brief's
*"e = 3, 6 need ord odd parts"* is **impossible**, not merely unrealised —
`ord_{2^41}(p)` has no odd part at all.

### THEOREM G2 (non-emptiness — the vacuity attack FAILS). *Verified: S2.*

> All three generating classes are realised at `n = 2^41`.

Witnesses, with primality established **twice** by me — deterministic
Miller-Rabin (12 bases; deterministic below `3.3e24`, which covers every
`p` here) and, **by a disjoint route**, a Lucas `(p-1)` certificate, which
is a *proof* rather than a test because `p - 1 = c·2^{e_p}` factors
completely:

| class | `p` | Lucas witness | `p-1` primes | `e_p` | `L = e log2 p` |
|---|---|---|---|---|---|
| `(>=41,1,1)` | `3·2^41+1 = 6597069766657` | `a = 5` | `{2,3}` | 41 | 42.584963 |
| `(40,2,2)` | `27·2^40+1 = 29686813949953` | `a = 5` | `{2,3}` | 40 | 89.509775 |
| `(39,4,4)` | `5·2^39+1 = 2748779069441` | `a = 3` | `{2,5}` | 39 | 165.287712 |
| `(39,4,4)` **prize-max** | `18446735827372343297` | `a = 3` | `{2,13,467,5527}` | 39 | **255.999997420** |

Every row: `v_2(p-1) = e_p` exactly, `k = e`, `v_2(q-1) = 41`,
`log2 p >= 39`, `L < 256`. `f2_adm`'s CATCH-4 is independently replayed
(S2.10): `c in {1,3,5}` all composite at `e_p = 40`.

**VERDICT V4: the empty-class sweep FAILS. `(O1)`'s surviving scope is
NON-VACUOUS — exactly three classes, all realised, including at the
prize-max corner `L -> 256`.**

---

## 2. (V2) THE COSET ATTACK — does the rules-level domain cost anything?

### THEOREM C1 (exact coset invariance of (O1)). *Verified: S6, three rows, exact.*

> Let `g in F_q^*`, `W <= mu_n` antipodally closed, `Lambda` odd. Put
> `gW := {gx : x in W}`. Then
>
> ```
>   (i)   gW is antipodally closed and has the same antipodal pair count m;
>   (ii)  phi_g : (C_l)_{l in Lambda} |-> (g^l C_l)_{l in Lambda} is an
>         F_q-linear BIJECTION of K1(Lambda) with chi_{phi_g(c)}(x) = chi_c(gx);
>   (iii) L(gW) = L(W) as subspaces of F_p^m — hence dim L, L^perp, Z(L)
>         and the minimum ternary weight are the SAME objects;
>   (iv)  E_{c in K1}[T_{gW}(c)] = E_{c in K1}[T_W(c)]   EXACTLY.
> ```

*Proof.* (i) `-(gx) = g(-x)` and `-1 in mu_n` (`n` even). (ii)
`chi_c(gx) = Tr(sum_l C_l g^l x^l) = chi_{phi_g(c)}(x)`; `g^l != 0` so
`phi_g` is bijective, and it preserves the support `Lambda`, hence maps
`K1(Lambda)` onto itself. (iii) With `y_i` one representative per antipodal
pair of `W`, `gy_i` is one per pair of `gW`, and
`(chi_c(gy_i))_i = (chi_{phi_g(c)}(y_i))_i`; as `c` runs over `K1(Lambda)`
so does `phi_g(c)`, so the two images coincide **as sets**. Equivalently at
the dual: `sum_i eps_i (gy_i)^l = g^l sum_i eps_i y_i^l`, so `L^perp` is
literally unchanged. (iv) is (ii)+(iii) plus the fact that an average over
a finite set is invariant under a bijection of that set. QED

**S6 checks (iii)-(iv) on three rows** — two generating (`p=5,q=25,n=8`;
`p=41,q=1681,n=16`, both `k = e = 2`) and one non-generating
(`p=17,q=289,n=16`, `k=1<e=2`) — each with a coset representative
`g` chosen **outside `mu_n` and outside `F_p = F_{q_{j-1}}`. The ternary
dual sets are literally equal; `Z(L)` is equal; the minimum weight is
equal; and `sum_c T_W(c)` is equal as an exact element of `Z[zeta_p]`,
computed by a **disjoint route** (group-ring arithmetic in
`Z[X]/(X^p-1)`, no LEMMA-1 shortcut). On the `p=17` row both routes agree
at `sum_c T_W = 1114384` and reproduce `E_c[T_W] = 3856` — the same 3856
that `f2_opening` LEMMA 3 reports as its tight instance.

### COROLLARY C1.1 (the scope of `f2_adm` CATCH-6, narrowed).

The same `g` at which S6 confirms coset invariance is one at which the
antipodal-descent identity `y^{q_{j-1}} = -y` **fails** (S6, replaying
`f2_adm` S3.I). So CATCH-6's gap is real but it is **confined to the
parity/descent machinery**, and `f2_opening` LEMMA 5 already proved that
machinery is *the wrong functional for (O1)*. Nothing in `(O1)`'s chain
uses antipodal *descent*; it uses antipodal *closure*, which is
coset-invariant by C1(i).

### COROLLARY C1.2 (the coset does NOT rescue `k < e`).

On a coset one may have `F_p(g·mu_n) = F_p(g, mu_n) = F_q` while
`F_p(mu_n) = F_{p^k} ⊊ F_q`, so "the domain generates the field" is
*weaker* on a coset than `k = e`. It does not help: by C1(iii) the dual
condition is `g^l · sum_i eps_i y_i^l = 0`, i.e. `sum_i eps_i y_i^l = 0`,
an equation in `F_{p^k}` — LEMMA ADM-3's constant is still `ord_n(p)`.
Hence `dim L` and the LEMMA-3 ratio `k/e` are unchanged, and **`f2_adm`
CATCH-1 is coset-robust** (S6, the `k=1<e=2` row).

**VERDICT V2: the coset attack FAILS at EXACTLY zero cost.** The attack
needed the coset to cost a constant; it costs a factor of **exactly 1**,
under both parity readings (nothing in C1 mentions `Lambda`'s parity beyond
"odd"). Net gain for the lane: one of `f2_adm`'s two NEW open obligations
(*"the coset form of the antipodal law"*) is **closed for the `(O1)`
sub-question**.

---

## 3. (V3) THE `Z_1` LOWER-BOUND ATTACK

### 3.1 THEOREM D1 (the DLI stronger law APPLIES on admissible rows). *Verified: S7.*

`background/nodes/dli_wcl_newton_short_window_exclusion/statement.md:8-22`
(PROVED), verbatim:

> Let `F` be a field of characteristic zero or characteristic greater than
> `w`. Let `omega in F` have exact order `2N`, and let
> `P(X) = sum_(i=1)^w s_i X^e_i`
> be a reduced signed polynomial with distinct `e_i in {0,...,N-1}` and
> `s_i in {+1,-1}`. If
> `P(omega^(2j-1)) = 0  for j=1,...,ell`
> and `w<=2ell`, then no such polynomial exists.

> **THEOREM D1.** On EVERY admissible row `p > m >= w`, so the hypothesis
> *"characteristic greater than `w`"* HOLDS, and every nonzero ternary
> relation on a window `W <= mu_n` with `Lambda` a run of `R` consecutive
> odd exponents starting at 1 satisfies
>
> ```
>            wt(eps)  >=  2R + 1        (twice SL-1's R+1).
> ```

*Proof of the hypothesis.* Any window has `m = |W|/2 <= n/2 = 2^40`, so
`w <= 2^40`. Write `p = c·2^{e_p} + 1`, `c` odd. If `e_p >= 41` then
`p > 2^41 > 2^40 >= w`. If `e_p = 40` then `p > 2^40 >= w`. If `e_p = 39`
then `c = 1` is impossible, since `3 | 2^39 + 1` (as `39` is odd), so
`c >= 3` and `p >= 3·2^39 = 1.5·2^40 > 2^40 >= w`. In every case
`p > w`. QED (S7.1-S7.5)

*Proof of the identification.* Let `y` generate `mu_n`, `omega := y`,
`2N := n`. The half-system of any antipodally closed `W` is
`{y^{a_i}}` with the `a_i` **distinct in `{0,...,N-1}`** (because
`y^{a+N} = -y^a`), and a ternary `eps` with support of size `w` is exactly a
reduced signed polynomial `P(X) = sum_i eps_i X^{a_i}`. The kernel condition
`sum_i eps_i y^{a_i l} = 0` for `l = 1,3,...,2R-1` is
`P(omega^{2j-1}) = 0`, `j = 1..R`. So `ell = R`, and `w <= 2R` is excluded.
QED

**Contrast, and why this is new.** `f2_sl1_powersums/PROOFS.md:171`
correctly records that on the KoalaBear tower
`char = 2^31-2^24+1 ~ 2.13e9` while `w` reaches `m_16 = 2^38 ~ 2.75e11`, so
*"`char > w` fails by two orders of magnitude"* — that verdict is
**tower-specific** and must not be carried onto admissible rows, where the
field cap `|F| < 2^256` with `e <= 6` forces `p >= 2^39` and the
inequality **reverses**. S7 replays the law on three toy rows in the
`char > w` regime (no relation below `2R+1`), and **re-derives two of
`f2_sl1_powersums`'s six counterexamples myself** (`char = 3^2, n = 8`:
min weight `3 = char < 5 = 2R+1`; `char = 5^2, n = 12`: min weight
`5 = char < 7 = 2R+1`), confirming that `char > w` is necessary, not
cosmetic.

### 3.2 PROPOSITION D2 (what the gift buys: (M3) halves, and stays vacuous). *Verified: S8.*

With minimum distance `d`, the `f2_sl1_powersums` §4 argument gives, per
LEMMA ADM-2 class (length `S`, codimension `R`):

```
    Z_1  <=  1 + 3^{S-d+1} · 2^{-d} ,       Z_1 < 2   <=>   d > 0.6131472·(S+1).
```

- SL-1 (`d = R+1`) needs `R/S > 0.6131472`;
- DLI (`d = 2R+1`) needs `R/S > 0.3065736`.

> **At every GENERATING row `R/S = 1/log2 p`, EXACTLY.**

*Proof.* `S = 2^{e_p-1} = 2^{40-D} = 2^40/k` and, under reading A with the
balance `t = n/L`, `R = ceil(t/2) = n/(2L) = 2^40/(e log2 p)`. At `k = e`,
`R/S = k/(e log2 p) = 1/log2 p`. QED (S8.2, rel. error `< 1e-12` at all
four witnesses)

Since admissibility forces `log2 p >= 39`, DLI's criterion needs
`log2 p < 3.2619` and misses by **`>= 11.96x`** over the whole admissible
region (`19.62x` at prize-max), against SL-1's `>= 23.91x` (`39.24x`).

**The gift is real and it halves the shortfall — it does not close it.**

### 3.3 PROPOSITION D3 (the attack from below fails, and by how much). *Verified: S9.*

To refute `(O1)` at a generating row one needs `Z(L) = Z_1^C >= 2^{Theta(n)}`,
so certainly `Z_1 >= 2`, i.e. `sum_{eps != 0} 2^{-wt(eps)} >= 1`. By
THEOREM D1 every term is `<= 2^{-(2R+1)}`, so the adversary must exhibit

```
        #{nonzero ternary codewords}  >=  2^{2R+1} = 2^{8,589,934,681}
```

at the prize-max witness. Against that:

1. **Symmetry cannot supply it.** The class code is **negacyclic**: if
   `sum_s eps_s zeta^{sl} = 0` for all `l` then so is the shift
   `(-eps_{S-1}, eps_0, ..., eps_{S-2})`, because `zeta^S = -1`. Shifts and
   the global sign flip generate a group of order `4S = 2^{e_p+1} = 2^40`.
   A single seed relation therefore inflates the count by at most `2^40`,
   short of the requirement by `2^{8,589,934,641}` (S9.3). Equivalently: an
   orbit construction can push `Z_1` above 2 only from a seed of weight
   `<= log2(4S) = e_p + 1 <= 42`, and SL-1 alone already forbids weight
   `<= R = 4.29e9`.
2. **Counting cannot supply it.** The random-subspace baseline
   (`f2_sl1_powersums/PROOFS.md:288-292`) gives
   `E[Z_1] ~ 1 + 2^S/p^R`, and at generating rows
   `S - R·log2 p = 0` **exactly** (S9.4: `-46.02` bits out of `S = 2^38`,
   the integer residue of §4.1). So the baseline predicts `Z_1 ~ 2` and
   `Z(L) = Z_1^C <= 2^C <= 16` — i.e. **`(O1)` TRUE with `o(n) <= 4 bits`**.
3. **DLI is nowhere near tight at prize scale.** The heuristic minimum
   ternary weight is `gamma*·S` with `H(gamma*) + gamma* = 1`,
   `gamma* = 0.227092` (S9.6), while `2R+1 = 0.03125·S` — a factor
   **7.27** below (S9.7). At `f2_sl1_powersums`'s toy scale the ordering is
   the opposite (`2R+1` is *attained* in 18/39 configurations); the
   agreement there is an artefact of `2R+1 > gamma*·S` at small `S` and is
   **not evidence about the official row**.

**VERDICT V3: the attack from below FAILS.** It needed either a ternary
kernel element at prize scale (none constructed; none can come from the
code's only visible symmetry) or a `2^{Theta(S)}` over-representation of
low-weight ternary codewords relative to the random baseline (none found —
and MDS structure pushes the *other* way, since the code has **no**
codewords below its designed distance). `SL-1b'(adm)` is untouched.

---

## 4. (V1) THE ZERO-MARGIN ATTACK

### 4.0 First, a correction to the attack's premise. *Verified: S4, S10.5.*

The brief asks for *"ANY strict loss anywhere in the chain (a positive-entropy
defect, a **constant > 1**, an `o(n)` that is really `Theta(n)`)"*. The first
two do **not** kill `(O1)`: its target is `2^{n/2 + o(n)}`, so any
multiplicative loss of `2^{O(1)}` — or indeed `2^{o(n)}` — is absorbed. The
"zero margin" of `f2_adm` THEOREM ADM-B is zero in the **ratio of
exponents** (LEMMA 3 degenerates to Corollary 1.1 and certifies nothing),
**not** in the sense that `(O1)` is a knife edge any constant tips. **Only a
`Theta(n)` loss in the exponent kills.** Everything below is calibrated to
that bar.

### 4.1 PROPOSITION Z1 (integrality and the ceiling: an `O(L)` residue only). *Verified: S4.*

Under reading A with `dim L = k·ceil(t/2)` (LEMMA ADM-2 with
`min(S,R) = R`, valid since `k < L`, S3.9):

```
   Delta  =  k·ceil(t/2)·log2 p  -  n/2  =  (L/2)·(t + [t odd])  -  n/2 .
```

Because `n/L` is irrational (`p` odd, `2^m` a 2-power), `Delta != 0` always.
Over the whole non-vacuous regime `t <= floor(n/L)` and the `(C)`-threshold
`t = ceil(n/L)`:

| class | `t = ceil(n/L)` | `Delta` | `t = floor(n/L)` | `Delta` |
|---|---|---|---|---|
| `(>=41,1,1)` | 51638492239 | **+41.10** | 51638492238 | −1.49 |
| `(40,2,2)` | 24567409040 | **+28.84** | 24567409039 | +28.84 |
| `(39,4,4)` | 13304214959 | **+96.10** | 13304214958 | −69.18 |
| prize-max | 8589934679 | **+184.10** | 8589934678 | −71.90 |

`|Delta| <= L <= 256` bits everywhere; the worst shortfall over the whole
regime is `-71.90` bits. **This is `o(n)` by a factor `n/(2·128) = 8.59e9`
and cannot kill `(O1)`.** (S4.11 independently reproduces `f2_adm`'s banked
`R = 4,294,967,340` at the witness.)

So: at the `(C)`-threshold LEMMA 3 **HOLDS** at every generating class, with
a positive integer residue of at most 184 bits — the exact content of
"exactly saturated".

### 4.2 THEOREM Z2 (THE ENSEMBLE DICHOTOMY — the attack lands). *Verified: S5.*

> **Setting.** A generating admissible row, the nested full-domain window
> `W = D` (`m = n/2`), **reading A**. By LEMMA ADM-2, `dim L = k·ceil(t/2)`,
> so LEMMA 3 (`f2_opening/PROOFS.md:219,225`) makes `(O1)` require
>
> ```
>        k·ceil(t/2)·log2 p  >=  n/2 - o(n)     <=>     t·L  >=  n - o(n) ,
> ```
>
> using `L = e·log2 p = k·log2 p` at `k = e`. **The `(O1)` requirement is
> therefore literally the balance `(C)` — with zero slack.** Now:
>
> **(i) Full-subset calibration.** If `t` is set by `(C)` (block ensemble =
> all `2^n` subsets of the domain, entropy `n`), then `t·L >= n` and
> `(O1)`'s necessary condition holds, with the `O(L)` residue of Z1.
> **`(O1)` SURVIVES.**
>
> **(ii) Fixed-slice calibration.** If `t` is set by the exact FM+gate
> balance `(T*)` — block ensemble = the size-`(n-k-t)` slice, entropy
> `log2 C(n, n-k-t)`, plus the 128-bit gate — then
>
> ```
>        n - t*·L   =   (2n / (L^2 ln 2)) · (1 + O(L^{-2}))        and
>        Delta      =   -(n - t*L)/2 + O(L)   =   -n/(L^2 ln 2) + O(L),
> ```
>
> so, because the rules cap `L < 256`,
>
> ```
>     E_{c in K1}[T_W]  >=  4^m / p^{dim L}  =  2^{ n/2 + n/(L^2 ln 2) + O(L) }
>                       >=  2^{ n/2 + n/45426 } ,
> ```
>
> a `Theta(n)` excess. **`(O1)` is FALSE by `2^{Theta(n)}` at every
> generating admissible row.**

*Proof of the closed form.* `(T*)` is the least `t` with
`t·L >= log2 C(n, n-k-t) + 128`, so at the crossing
`n - t*L = n - log2 C(n, n/2 - t*) - 128 + O(L)`. The de Moivre-Laplace
expansion (verified by `t_naming` N2 and re-verified here to rel `< 1e-5`,
S5.5) gives
`log2 C(n, n/2 - t) = n - (1/2)log2(pi n/2) - 2t^2/(n ln 2) - (4/3)t^4/(n^3 ln 2) - ...`,
whence
`n - t*L = 2t*^2/(n ln 2) + (4/3)t*^4/(n^3 ln 2) + (1/2)log2(pi n/2) - 128 + O(L)`.
Substituting `t* = n/L·(1 + O(L^{-2}))` gives the stated form. `Delta` then
follows from `Delta = (L/2)(t* + [t* odd]) - n/2`. QED

**Measured (S5, all four witnesses):**

| class | `L` | `t_(C)` | `t_(T*)` | `n − t*L` | `Delta_(T*)` |
|---|---|---|---|---|---|
| `(>=41,1,1)` | 42.584963 | 51638492239 | 51556561743 | 3.4890e9 | **−1.7445e9** |
| `(40,2,2)` | 89.509775 | 24567409040 | 24558567124 | 7.9144e8 | **−3.9572e8** |
| `(39,4,4)` | 165.287712 | 13304214959 | 13302810105 | 2.3221e8 | **−1.1610e8** |
| **prize-max** | 255.999997 | 8589934679 | **8589556515** | 9.6810e7 | **−4.8405e7** |

Every `Delta` strictly negative; every one matched by the closed form
`−n/(L^2 ln 2)` (S5.6, residue `<= L`); and `(n − t*L)/n` is **`n`-invariant**
across `n = 2^39..2^42` (S5.8, spread `1.0000040`), which is exactly the
statement that the loss is `Theta(n)` and not `O(polylog n)`.

**Independent validation of the `(T*)` solver:** it reproduces
`f2_tq_pin`'s banked `t*` at `L = 255.9` to the last digit at **all four
rates** — `8592912739 / 7014660390 / 4722556392 / 2943177800` (S5.2, S5.3)
— and reproduces the witness-row `t* = 8,589,556,515` of
`f2_tq_pin/PROOFS.md:138` exactly.

### COROLLARY Z2.1 (the `0.0044%` is the sign of `(O1)`). *Verified: S5.7.*

At prize-max the relative gap is `(n − t*L)/n = 0.004402%`, and
`2/(L^2 ln 2) = 0.004403%`. This is **exactly** `f2_tq_pin` CATCH-4's
"agreement to `0.0044%`" and **exactly** `t_naming` CATCH-C's identification
of that number as `2/(L² ln 2)`. Both banked readings call it *agreement*.
At a generating row it is not agreement: it is precisely the quantity that
decides whether LEMMA 3 — a PROVED necessary condition for `(O1)` — holds
or fails, and it fails by `2^{4.84e7}`.

**On the tower this was invisible**: LEMMA 3's margin there was `7.89x` in
the ratio, i.e. a slack of `6.1e10` in `t`, which swallows a `9.7e7`-bit
recalibration without a trace. Zero margin is what makes the two
calibrations distinguishable.

### 4.3 PROPOSITION Z3 (the reading dependence, stated in advance). *Verified: S3, S5.9.*

> `ratio := dim L · log2 p / m  =  k/e` (reading A) `= 2k/e` (reading B),
> nested top window.

| `(k,e)` | reading A | reading B |
|---|---|---|
| (1,1) **gen** | 1.0000 SATURATED | 2.0000 margin |
| (1,2) | 0.5000 **REFUTED** | 1.0000 SATURATED |
| (1,3)…(1,6) | 0.333…0.167 REFUTED | 0.667…0.333 REFUTED |
| (2,2) **gen** | 1.0000 SATURATED | 2.0000 margin |
| (2,4) | 0.5000 **REFUTED** | 1.0000 SATURATED |
| (2,6) | 0.3333 REFUTED | 0.6667 REFUTED |
| (4,4) **gen** | 1.0000 SATURATED | 2.0000 margin |

Consequences, both new:

- **Generating rows are never refuted by LEMMA 3 under either reading**
  (ratio `1` or `2`). THEOREM Z2 is therefore **reading-A-only**: under
  reading B, `Delta_(T*) ~ +n/2` (S5.9: `+1.0994e12` bits at prize-max) and
  the `9.68e7`-bit recalibration is swamped. Registered in advance as A4's
  own control; it behaves as predicted.
- **`f2_adm`'s D3 refutation scope is reading-dependent**: `(1,2)` and
  `(2,4)` flip **REFUTED → SATURATED** under reading B. Its CATCH-1 headline
  witness `(k,e) = (1,6)` survives **both** readings (reading-B refuted set
  `{(1,3),(1,4),(1,5),(1,6),(2,6)}`), so CATCH-1 itself is safe; the table
  around it is not.

**A structural argument that reading A is forced** (registered as A5,
confirmed at S3.10-S3.12, quotes checked at S0). `f2_fixed_sector/REPORT.md:31`
banks a **proved per-sector parity TRICHOTOMY** `G / K1 / K2`, and
`f2_opening/PROOFS.md:273` defines class `G` as *"both parity parts
nonzero"*. A trichotomy with non-empty `K2` and `G` **requires** the ambient
condition set to contain both parities; hence `Lambda_full != Lambda_K1` and
`|Lambda_K1| = ceil(t/2)`. Independently,
`f2_deployed_windows/REPORT.md:55` states the parity-pure sector's own
condition count as *"codim_j = min(m_j, t/2) F_p-conditions"* — `t/2`, in
the lane's own words. This upgrades `t_naming` CATCH-E from "5-to-1 by
weight of evidence" to "forced by a banked theorem", but it is an argument
about internal consistency, **not** a proof about the maintainer's
intention, and I do not close CATCH-E here.

### 4.4 PROPOSITION Z4 (the `(O1) => (O2)` step is lossy at generating rows). *Verified: S10.*

`f2_opening` THEOREM B gives `E_c[V_b] <= E_c[T_W]`, and THEOREM B' gives
the sharp slice law `E_c[V_b] = C(m, b/2)` — but B' needs LEMMA 2's
hypothesis, which `f2_adm` THEOREM ADM-A proves **UNSATISFIABLE at every
moving rung of every admissible row**. So on generating rows only the crude
step survives, and against the `b`-resolved scale `C(m,b/2) ~ 2^{m H(beta)}`,
`beta := b/(2m)`, it loses

```
       2^{ m (1 - H(beta)) }   =   2^{Theta(n)}   for every beta bounded away from 1/2
```

(S10: `2^{5.84e11}` at `beta = 0.1`, `2^{2.08e11}` at `0.25`,
`2^{3.19e10}` at `0.4`; only at `beta = 1/2` does it collapse to the
`sqrt(m)` Stirling factor, `20.33` bits). `(O2)` **as literally stated**
(target `2^{n/2+o(n)}`) remains implied — but then it is no constraint at
all, and the Hamming-slice fence that motivated it
(`f2_fixed_sector/REPORT.md:33`) is **not** answered on generating rows.
This is the same dichotomy as Z2 seen from the consumer's end: the fence
demands the fixed-size slice, and the slice is exactly the ensemble whose
calibration makes `(O1)` false.

**VERDICT V1: the zero-margin attack LANDS — conditionally, and the
condition is decidable.** `(O1)` at generating rows is
**TRUE under (reading A + full-subset calibration)**, with all slack
`<= 184` bits; **FALSE by `2^{n/(L^2 ln 2)} >= 2^{4.84e7}` under
(reading A + fixed-slice calibration)**; and **TRUE with a factor-2 exponent
margin under reading B** either way.

---

## 5. THE MINIMAL SURVIVING FORM OF (O1)

Everything else in the chain is exact, so this is the whole of it:

> **(O1-gen).** Let `n = 2^41`, `p` an odd prime, `q = p^e` with
> `(e_p, e) in {(>=41,1), (40,2), (39,4)}` and `e·log2 p < 256`; let
> `D = g·mu_n` (any `g in F_q^*`) be the rules-level smooth domain,
> `W = D`, `m = n/2`. Let `Lambda_K1` be a run of `R` consecutive odd
> exponents `1, 3, ..., 2R-1` with `R >= n/(2L)`. Then, **exactly**,
>
> ```
>     E_{c in K1(Lambda)}[ T_W(c) ]   =   2^{n/2} · Z_1^{e} ,
> ```
>
> where `Z_1 = sum_{eps} 2^{-wt(eps)}` runs over the ternary kernel of the
> negacyclic prime-field GRS code
>
> ```
>     [ S, S-R, R+1 ]_p ,   S = 2^{e_p-1} = 2^40/e ,   R/S = 1/log2 p ,
> ```
>
> evaluation points the half-system of `mu_{2^{e_p}} <= F_p^*`, whose ternary
> sub-code has minimum weight `>= 2R+1` (THEOREM D1, `char > w`).
> `(O1)` holds **iff** `Z_1 <= 2^{o(n)/e}`.
>
> **Scope conditions, both necessary and both currently unpinned:**
> (a) `Lambda`-parity reading A or B (`t_naming` CATCH-E) — under B the
> statement has a factor-2 exponent margin and is robust;
> (b) the block ensemble against which the condition count is calibrated —
> full power set (`(C)`) or fixed-size slice (`(T*)`). **Under (reading A +
> slice) the statement is FALSE and no bound on `Z_1` can save it.**

Coset-invariance (THEOREM C1) means `g` may be dropped without loss:
`(O1-gen)` is a statement about `mu_n`.

---

## 6. CATCHES

- **CATCH-A (maintainer-level, new).** **The banked "0.0044% agreement"
  between `(C)` and `(T*)` IS the sign of `(O1)` on generating rows.** At
  zero margin the two calibrations of the condition count differ by exactly
  `n - t*L = 2n/(L^2 ln 2)` bits, and half of that is LEMMA 3's shortfall:
  `(O1)` holds under the full-subset calibration and is FALSE by
  `2^{n/(L^2 ln 2)} >= 2^{4.84e7}` (prize-max) — up to `2^{1.74e9}` at
  `L = 42.58` — under the slice calibration. `f2_tq_pin` CATCH-4 and
  `t_naming` CATCH-C both identify the number and both read it as
  *agreement*; it is a `Theta(n)` disagreement wherever LEMMA 3 has no
  margin. **Decidable, and it decides mystery 2's F2 lane on the only rows
  it still lives on.**
- **CATCH-B (against `f2_adm` D3, and against the brief's premise).**
  `f2_adm`'s "LEMMA 3 exactly saturated, margin 1.000" is **reading-A-only**:
  under reading B the ratio is `2k/e`, generating rows carry margin
  **2.000**, and the classes `(1,2)` and `(2,4)` flip **REFUTED →
  SATURATED**. `f2_adm`'s claim that its §3.2 result is *"independent of
  that collision"* is true of `t`'s **value** and false of `Lambda`'s
  **parity convention** — the two differ by exactly the factor 2 that
  `t_naming` CATCH-E is about. CATCH-1's `(1,6)` witness survives both
  readings and is unaffected.
- **CATCH-C (against this pilot's own brief).** "Any strict loss anywhere
  kills it" is too strong: `(O1)`'s `+o(n)` absorbs every `2^{O(1)}` and
  `2^{o(n)}` loss. The largest loss available from integrality, ceilings and
  the irrationality of `n/L` is `<= L/2 <= 128` bits (measured worst:
  `-71.90`), short of the `Theta(n)` bar by `8.59e9`. Only Z2's ensemble
  loss clears it.
- **CATCH-D (an uncited banked gift, and its limit).**
  `dli_wcl_newton_short_window_exclusion` (PROVED) **applies on every
  admissible row** — `p > m` always, by an elementary argument
  (`3 | 2^39+1` kills the only edge case) — giving `wt >= 2R+1`, twice
  SL-1's bound. `f2_sl1_powersums`'s verdict that the node *"does not apply
  at the official row"* is correct **for the tower** and reverses under the
  admissible field cap; no F2 file has noticed the reversal. Its limit is
  equally sharp: at prize scale `2R+1 = 0.03125·S` sits `7.27x` **below**
  the heuristic true minimum `0.2271·S`, so the doubled distance improves
  `(M3)` from `23.9x`-vacuous to `11.96x`-vacuous and no further.
- **CATCH-E (scope, closing half of `f2_adm` CATCH-6).** `(O1)` is
  **exactly** coset-invariant (THEOREM C1: the same `L`, the same `L^perp`,
  the same `Z`, the same average, verified by a disjoint `Z[zeta_p]` route).
  The rules-level coset therefore costs the `(O1)` obligation **nothing**,
  and CATCH-6's gap is confined to the parity/descent machinery — which
  LEMMA 5 already proved cannot pay `(O1)`. Also: the coset does **not**
  rescue `k < e` rows even though `F_p(g·mu_n)` may equal `F_q` when
  `F_p(mu_n)` does not, so `f2_adm` CATCH-1 is coset-robust.
- **CATCH-F (scope, new).** `ord_{2^41}(p)` is always a 2-power, so
  `e in {3,5,6}` can **never** generate: `(O1)`'s surviving scope is exactly
  three classes, all non-empty. `f2_adm` CATCH-4's empty class `(40,6)` was
  doubly out of scope (non-generating as well as empty).
- **CATCH-G (the fence is not answered on generating rows).** `(O1) => (O2)`
  is lossless only against `(O2)`'s stated target, at which `(O2)` is no
  constraint; against the `b`-resolved scale the step loses
  `2^{m(1-H(beta))} = 2^{Theta(n)}`, and THEOREM B' — which supplied the
  exact slice law — is **vacuous at every moving rung of every admissible
  row**. The Hamming-slice fence that created `(O2)` is therefore open again
  on exactly the rows `(O1)` still lives on.
- **CATCH-H (upgrade to `t_naming` CATCH-E).** The K1/K2/G trichotomy is a
  **proved** theorem (`f2_fixed_sector/REPORT.md:31`) and class `G` is
  defined as *"both parity parts nonzero"*; a non-empty `G` forces the
  ambient condition set to carry both parities, hence
  `|Lambda_K1| = ceil(t/2)`. Together with
  `f2_deployed_windows/REPORT.md:55`'s *"codim_j = min(m_j, t/2)"* this
  makes reading A **internally forced**, not merely favoured 5-to-1.

---

## 7. REGISTRATION OUTCOMES (PREREG appendix A1-A11)

- **A1 CONFIRMED and strengthened** — exactly three generating classes,
  `e in {1,2,4}`, all non-empty; `e in {3,5,6}` impossible.
- **A2 CONFIRMED** — reported as CATCH-C against the brief.
- **A3 CONFIRMED** — `|Delta| <= L`; worst `-71.90` bits; at the banked
  witness `Delta = +184.10 > 0`, and my `R` reproduces `f2_adm`'s
  `4,294,967,340`.
- **A4 CONFIRMED, including the `0.0044%` prediction to the digit**, and its
  pre-registered reading-B control behaved exactly as registered (`+n/2`).
- **A5 CONFIRMED** — and by a stronger source than I expected
  (`f2_deployed_windows/REPORT.md:55` states `t/2` outright).
- **A6 CONFIRMED, both parts** (exact invariance; no rescue of `k<e`).
- **A7 CONFIRMED** — `char > w` on every admissible row.
- **A8 CONFIRMED** — `R/S = 1/log2 p` exactly; `11.96x` / `19.62x`.
- **A9 CONFIRMED** — the orbit no-go; baseline `Z_1 ~ 2`.
- **A10 CONFIRMED** — factor `7.27`, the toy/prize ordering does reverse.
- **A11 HELD** — no `Z_1` bound claimed, no reading chosen, no status flip.

Nothing self-falsified this round. I record that as a **weakness of the
registration**, not a strength: A1-A10 were all registered after reading the
full record, and the only genuinely surprising result (CATCH-A) was
registered as A4 because I had already seen `f2_tq_pin`'s two `t` values
before writing it down. The registration took less risk than it looks.

---

## 8. SCOPE — what is NOT claimed

- **Nothing here bounds `Z_1`.** `SL-1b'(adm)` is untouched and remains THE
  terminal. The random-subspace figure `Z_1 ~ 2` and `gamma* = 0.2271` are
  **heuristics**, explicitly not theorems.
- **THEOREM Z2 is conditional on two unpinned choices**, both named:
  the `Lambda`-parity reading (CATCH-E, maintainer-owned) and the ensemble
  calibration (CATCH-A, new). I price both; I choose neither. Under
  (reading B) or (full-subset calibration) `(O1)` at generating rows
  **SURVIVES** and my attack fails.
- `t_naming` (N3) flags *"feeding `t*` into LEMMA 3"* as a wrong-`t`
  consumption. I am **not** substituting `t_XR` for `t_F2`: I am asking
  which **ensemble** `t_F2`'s own balance should be calibrated against, and
  observing that `f2_tq_pin` derives `(C)` from `q^t > 2^n` while `(T*)`
  uses `C(n,n-k-t)`. A maintainer may judge this the same defect; disclosed
  rather than buried.
- LEMMA ADM-2, LEMMA ADM-3 and THEOREM ADM-A are **inherited** from
  `f2_adm`, not re-proved at scale; S6/S7 re-verify their *structure* on
  toys only (`p <= 41`, `n <= 16`, `m <= 8`).
- All headline numbers use the **nested** window reading at the full-domain
  window. The new-part reading doubles the ratios (`max(2,k)/e`) and changes
  none of the verdicts in kind.
- Everything is at `n = 2^41`; `n = 2^40` shifts exponents by one and is not
  tabulated. S5.8 checks only that the `Theta(n)` scaling is `n`-invariant.
- No status flip is proposed for any minted node. DRAFT ONLY; no file
  outside `notes/pilots_20260806/o1_generating_adversary/` was written; no
  commit, no push; `z1_ternary_mass/` was **not** read.
