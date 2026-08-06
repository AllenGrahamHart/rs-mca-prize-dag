# Z_1 TERNARY MASS — the proofs (SL-1b′ on the admissible object)

Round 18, 2026-08-06, pilot `notes/pilots_20260806/z1_ternary_mass/`.
Verifier `verify.py`, stages S0–S12, **81 checks, 0 FAIL**, exit 0, digest
`Z1_TERNARY_MASS_ALL_PASS`. Log: `VERIFY_LOG.txt`. Registrations
Z-A1…Z-A14 appended to `PREREG.md` before any computation.

Notation follows `f2_adm/PROOFS.md` §1.4. The object of record
(`f2_adm/PROOFS.md:232-235`, verbatim):

> **COROLLARY ADM-2.2 (the terminal is a prime-field GRS code).** `Z(L)` is
> determined by ONE class: `Z(L) = Z_1^C`, `C <= 4`, where `Z_1` is the
> ternary mass of an explicit `[2^{e_p-1}, 2^{e_p-1} - R, R+1]_p` GRS code
> whose evaluation points are the half-system of `mu_{2^{e_p}} <= F_p^*`.

and the mass itself (`f2_adm/PROOFS.md:465`, quoting
`f2_sl1b/PROOFS.md:571`, verbatim):

> *"prove `Z(L) = sum_{eps in L^perp ∩ T} 2^{-wt(eps)} <= 2^{o(m)}`."*

**`Z` is a WEIGHTED mass, not a count.** Everything below turns on that.

---

## 0. SUBTRACTION LEDGER (hard law 5) — declared before any claim

Five surfaces swept (`critical/`, `background/`, `notes/`, `archive/`,
`experiments/`+`dag.json`+`upstream_dag/`+`formal/`), excluding the sibling
`o1_generating_adversary/`, which was not read.

- **BANKED — the collision identity is NOT ours.**
  `background/nodes/dli_c1_l1_block_owner_ledger/statement.md:15,18-19`,
  verbatim: `Z = sum_(d in ternary kernel) 2^(-wt(d)).` … *"The banked
  collision identity"*. Machine form:
  `notes/pro_briefs_20260801/responses/verify_brief1_c1r3_program_arithmetic.py:169-189`,
  verbatim `require(collision_pairs == (1 << n) * z, "fiber/relation
  collision identity")`.
- **BANKED — the fibre-variance identity is NOT ours, and §2's inequality is
  its one-line corollary.**
  `notes/pro_briefs_20260801/responses/BRIEF1_PRO_DOSSIER.md:47,52`,
  verbatim:

  > With `Z = sum_(d in ternary kernel) 2^(-w(d))` and `r = q^L/2^N`:
  > `sum_s (m_s - 2^N/q^L)^2 = 2^N (Z - 1/r)`  (Boolean fibre variance)

  The left side is a sum of squares. **Nobody in the repo draws the
  conclusion `Z >= 1/r`.** §2 draws it and transports it; the identity is
  cited, not claimed.
- **BANKED — the Newton short-window exclusion**
  (`background/nodes/dli_wcl_newton_short_window_exclusion`, PROVED), quoted
  verbatim in §1. §1 transports it; §3 extends it. The *mechanism* is the
  node's.
- **BANKED — the first moment.** `f2_sl1_powersums/PROOFS.md:291`, verbatim:
  `E[ Z(L) ]  =  1 + (2^m - 1)(p^{m-d} - 1)/(p^m - 1)   ~   1 + 2^m / p^d .`
  §2 shows the same quantity is a *pointwise floor*.
- **BANKED — the norm route is already priced as dead.**
  `f2_sl1_powersums/PROOFS.md:262-266`, verbatim: *"Secondary (norm) bound,
  recorded and DOMINATED … giving `w >= p^{2R/n}` … Recorded so nobody
  re-runs it."* §6 re-prices it at the admissible row.
- **BANKED — every ternary relation is an accident of `p` at 2-power order.**
  `f2_sl1_powersums/PROOFS.md:266-271` (the `Z`-basis argument), itself
  banked at `critical/nodes/bounded_coeff_norm_gate`. §7 uses it and
  verifies it.
- **NOT FOUND anywhere** (searched exhaustively): a lower bound on `Z`
  beyond `Z >= 1`; any pointwise/unconditional reading of the first moment
  (the repo asserts the opposite, see CATCH-Z2); any `l1`/Lee sphere-packing
  bound on ternary codewords; any integer-coefficient extension of the
  Newton node.

---

## 1. THEOREM Z-1 (the crosswalk): the DLI law transports

`background/nodes/dli_wcl_newton_short_window_exclusion/statement.md:8-22`,
**verbatim**:

> Let `F` be a field of characteristic zero or characteristic greater than
> `w`. Let `omega in F` have exact order `2N`, and let
> `P(X) = sum_(i=1)^w s_i X^e_i`
> be a reduced signed polynomial with distinct `e_i in {0,...,N-1}` and
> `s_i in {+1,-1}`. If
> `P(omega^(2j-1)) = 0  for j=1,...,ell`
> and `w<=2ell`, then no such polynomial exists.

**Hypothesis match at the admissible object** (S1.1–S1.5; the object is
`f2_adm`'s COROLLARY ADM-2.2 with `p = 18446735827372343297`,
`e_p = 39`, `S = 2^38`, `R = 4,294,967,340`):

| DLI hypothesis | admissible object | verdict |
|---|---|---|
| `char F > w` | `p = 1.845e19`, `w <= S = 2.749e11` | **HOLDS**, margin `6.71e7` |
| `omega` of exact order `2N` | `2N = 2^{e_p} = 2^39`, `v_2(p-1) = 39` exactly | **HOLDS** |
| `e_i` distinct in `{0..N-1}` | `N = 2^38 = S`; the half-system IS `{omega^e : 0<=e<N}` | **HOLDS** |
| `P(omega^{2j-1}) = 0`, `j = 1..ell` | `Lambda = {odd l : l <= t}` starts at `l = 1` (`f2_sl1_powersums/PROOFS.md:121`) | **HOLDS**, `ell = R` |

**THEOREM Z-1.** On the admissible object every nonzero ternary vector of
`L^perp` has

```text
        wt  >=  2R + 1  =  8,589,934,681 ,
```

twice the characteristic-free floor `R+1` of THEOREM SL-1.

*Proof.* All four hypotheses hold, as tabulated; apply the banked node. ∎

**Why it failed on the tower and works here** (S1.8–S1.9). The tower had
`char = p = 2^31-2^24+1 = 2.13e9 < m_16 = 2^38`
(`f2_sl1_powersums/PROOFS.md:170-173`, verbatim: *"`char > w` fails by two
orders of magnitude"*). The admissible object has `p/w_max = 6.71e7`
instead of `7.75e-3`. **This is the F2↔DLI crosswalk's first real
dividend.** Its size is priced in §5 and §6: it is a factor 2 on the
distance, `1.3869x` on the discharge criterion, and — §6 — **exactly
nothing on the mass**.

**SCOPE (Z-A2, S4.2, S9.6): the shift is load-bearing.** The hypothesis is
the *first* `ell` odd powers. Over the grid, 43 configurations with a
shifted run (`a >= 1`) and `char > w` have min ternary weight `< 2R+1`; the
smallest is `2N=12, p=13, R=1, a=1` with min weight `2 < 3`, and
`f2_sl1b`'s own smallest witness (`p=7`, `Lambda = {5,7}`, i.e. `a = 2`,
min weight `3 < 5 = 2R+1`, `char 7 > 3`) is one of them (S9.6). The
transport is legitimate **only** because the official `Lambda` starts at
`l = 1`; it must not be quoted for shifted windows. The characteristic-free
`R+1` floor survives every shift (S4.3, 696 configurations, 0 violations).

---

## 2. THEOREM Z-FLOOR: the first moment is a POINTWISE floor

**THEOREM Z-FLOOR.** For **every** `F_p`-subspace `L ⊆ F_p^m` (no MDS, no
GRS, no genericity, no randomness),

```text
        Z(L)  =  sum_{eps in L^perp ∩ T} 2^{-wt(eps)}   >=   2^m / p^{dim L} ,
```

with equality iff the syndrome map is exactly balanced on `{0,1}^m`.

*Proof.* Let `A` be a parity-check matrix for `L^perp`, i.e. `L^perp =
ker A` with `rank A = d = dim L`, and for `s in F_p^d` put
`F_s = {b in {0,1}^m : Ab = s}`. Counting pairs two ways:

```text
   sum_s |F_s|^2 = #{(b,b') in {0,1}^m x {0,1}^m : Ab = Ab'}
                 = #{(b,b') : b - b' in ker A}.
```

Every difference `b - b'` lies in `T = {0,±1}^m`, and for a FIXED
`eps in T` the number of pairs with `b - b' = eps` is `2^{m - wt(eps)}`
(coordinates with `eps_i = ±1` are forced; the `m - wt(eps)` coordinates
with `eps_i = 0` are free). Hence

```text
   sum_s |F_s|^2  =  sum_{eps in T ∩ ker A} 2^{m - wt(eps)}  =  2^m · Z(L).
```

This is the **banked collision identity** (§0), verified exactly here on 336
configurations (S2.1). Now Cauchy–Schwarz over the at most `p^d` attained
syndromes, with `sum_s |F_s| = 2^m`:

```text
   (2^m)^2  =  (sum_s |F_s|)^2  <=  p^d · sum_s |F_s|^2  =  p^d · 2^m Z(L),
```

so `Z(L) >= 2^m/p^d`. ∎

Equivalently: the banked fibre-variance identity of §0 has a sum of squares
on its left, so `Z - 1/r >= 0`. **The inequality is one line from a banked
identity and nobody had drawn it.** That is the whole of the novelty claim
here, and §§4–6 are what it buys.

*Verified:* S2.2 — 696 configurations, exact rational arithmetic, 0
violations; S2.5 — it strictly beats the banked unconditional floor
`Z(L) >= 1` (`f2_opening/PROOFS.md:90`) on 92 configurations, by up to
`675.6x`; S2.4 — wherever `2^m > p^{dim L}` a nonzero ternary kernel vector
is *forced*, confirmed on all 112 such configurations; S2.6 — the same
argument floors the ternary **count**, `|T ∩ L^perp| >= 2^m/p^{dim L}`
(take the largest fibre and subtract a fixed element of it).

**COROLLARY Z-FLOOR.1 (the floor is tight, so it cannot be improved).**
`max(1, 2^m/p^d) <= E_random[Z] <= 2·max(1, 2^m/p^d) + 1` (S2.3, 696
configurations, 0 exceptions), with `E_random` the banked exact first moment
`f2_sl1_powersums/PROOFS.md:291`. The pointwise floor and the ensemble mean
agree to within a factor 2: **no subspace can beat the random baseline at
this statistic by more than a factor 2**, and LEMMA 3 is therefore not a
heuristic threshold but a forced one.

**COROLLARY Z-FLOOR.2 (LEMMA 3 re-derived).** `(O1)`'s requirement
`Z(L) <= 2^{o(n)}` forces `dim L · log2 p >= m - o(n)`. This is
`f2_opening`'s LEMMA 3 with the identical constant, now obtained from
Cauchy–Schwarz in three lines and independently of the K1 machinery.

---

## 3. THEOREM Z-2: the DLI theorem extends to integer coefficients

The node is stated for `s_i in {+1,-1}`. For §5 we need it for
*differences* of ternary vectors, whose entries lie in `{0,±1,±2}`.

**THEOREM Z-2 (`l1` extension).** Let `F` have characteristic `0` or
`> w`, let `omega in F` have exact order `2N`, and let `c in Z^N` be
nonzero, indexed by `e in {0,...,N-1}`, with **`l1`-weight**
`w := sum_e |c_e|`. If

```text
        sum_e c_e omega^{(2j-1)e} = 0   for j = 1,...,ell     and   w <= 2ell,
```

then `c = 0` — i.e. no such `c` exists.

*Proof.* Form the **multiset** `M` of roots: for each `e` with `c_e != 0`
include `r_e := sign(c_e)·omega^e` with multiplicity `|c_e|`; `|M| = w` and
every element is nonzero. For odd `m`, `sign(c_e)^m = sign(c_e)`, so the
power sums of `M` are

```text
   p_m = sum_{r in M} r^m = sum_e |c_e|·sign(c_e)^m·omega^{me}
       = sum_e c_e omega^{me},
```

and the hypothesis is exactly `p_1 = p_3 = ... = p_{2ell-1} = 0`. Newton's
identity `m a_m = sum_{i=1}^m (-1)^{i-1} a_{m-i} p_i` holds for the
elementary symmetric functions of a multiset; the node's induction applies
verbatim (odd `i` kill `p_i`; even `i` leave an earlier odd `a_{m-i}`), and
`char F > w` makes `m` invertible for `m <= w`. So `a_m = 0` for every odd
`m <= min(w, 2ell-1)`.

If `w` is odd then `w <= 2ell-1`, so `a_w = ± prod_{r in M} r = 0`,
impossible since every root is nonzero.

If `w` is even, all odd `a_m` vanish through `a_{w-1}`, so
`prod_{r in M}(T - r)` is an even polynomial and `M` is stable under
negation **with multiplicity**. But `-r_e = sign(c_e)·omega^{e+N}` (using
`-1 = omega^N`), and `M`'s distinct values are `{sign(c_e) omega^e}` with
`e in {0,...,N-1}`. Matching `-r_e` to some `r_{e'}` gives either
`omega^{e'} = omega^{e+N}`, i.e. `e' ≡ e + N (mod 2N)` — impossible for
`e, e' in {0,...,N-1}` — or `e' = e` with `sign(c_{e'}) = -sign(c_e)`,
also impossible. So `M` is not negation-stable: contradiction. ∎

The `{+1,-1}` case is the node's, recovered at `|c_e| in {0,1}`; the proof
is the node's proof with multiplicities inserted. **Reported back to the
DLI lane as CATCH-Z5:** the sign restriction in
`dli_wcl_newton_short_window_exclusion` is not needed — the theorem holds
for all integer coefficients once `w` is read as the `l1` weight, and the
node's `w <= 2ell` cutoff is unchanged.

*Verified:* S5.1 — 84 configurations swept exhaustively over `{0,±1,±2}^N`
at shift 0 with `char > w`; no nonzero integer vector of `l1`-weight `<= 2R`
lies in the kernel, 0 violations.

**COROLLARY Z-2.1 (`l1` separation).** On the admissible object, distinct
ternary codewords `c != c'` of `L^perp` satisfy `||c - c'||_1 >= 2R+1`
(apply Z-2 to `c - c'`; its `l1` weight is at most `2S = 2^39 < p`, so
`char > w` holds). *Verified:* S5.2 — 12 configurations, 80,146 codeword
pairs, 0 violations.

---

## 4. The dichotomy, and the three-way seam

Write the nested reading of `f2_adm`'s ladder: `m = n/2`, `C = k`,
`S = m/C`, `dim L = C·min(S,R) = C·R`, `L = log2 q = e·log2 p`, and
`R = #{odd l <= t}` so `R·log2 p = tL/(2e)`.

**THEOREM Z-3 (the mass dichotomy).** On every admissible row,

```text
      Z(L)  >=  2^{ m ( 1 - (k/e)·(tL/n) ) } .
```

*Proof.* THEOREM Z-FLOOR gives `Z >= 2^{m - dim L·log2 p}`, and
`dim L·log2 p = C·R·log2 p = k·tL/(2e) = m·(k/e)(tL/n)` using `m = n/2`. ∎

Two consequences, and they are the whole verdict.

**(a) `k < e`: (O1) is FALSE at the level of the object.** The counting
balance (C) (`f2_tq_pin/PROOFS.md:174`, verbatim `t · L  >=  n`) gives
`tL/n >= 1`, so

```text
      Z(L)  >=  2^{ m (1 - k/e) }  =  2^{Theta(n)} ,
```

against `(O1)`'s requirement `Z <= 2^{o(n)}`. This **refutes (O1)
unconditionally on every admissible row with `k < e`** — not a necessary
condition failing, but the mass itself exceeding its target, by counting
alone. At `f2_adm` CATCH-1's exhibited row (`p = 3·2^41+1`, `q = p^6`,
`k = 1`, `e = 6`, verified prime with `v_2(p-1) = 41` at S7.2) this reads
`Z >= 2^{5n/12}` — **exactly** `f2_adm/REPORT.md:44`'s *"excess `2^{5n/12}`
(nested) / `2^{n/6}` (the looser reading)"*, reproduced by a fully
independent route (S7.3, S7.4). Two independent proofs of the same
exponent is the strongest confirmation available for that catch.

**(b) `k = e`: the floor is silent, and it is silent for a reason.** The
exponent becomes `m(1 - tL/n) <= 0` **iff** the counting balance holds.
Hence:

> **CATCH-Z3 (the seam has a third face).** On `k = e` rows the three
> statements
> *(i)* the counting balance (C) `tL >= n`,
> *(ii)* LEMMA 3's necessary condition `dim L·log2 p >= m`, and
> *(iii)* the vacuity of the unconditional mass floor
> are **the same inequality**. `f2_adm/REPORT.md:40` already identified
> (i)–(ii) as one seam (*"the necessary condition and the average-vs-sum
> seam are the same inequality"*); (iii) says the object's own mass sits on
> that same knife. There is no slack anywhere in the architecture because
> there is only one inequality.

*Verified:* S6.6–S6.8 — `S = m/k` exactly, `R log2 p = m/e` up to the
rounding of `R`, hence `ratio = R log2 p / S = k/e = 1.000000000167` at the
witness, reproducing `f2_adm/PROOFS.md:373`'s saturation table from the
mass floor alone.

---

## 5. The knife edge at `k = e`: a 64-bit window

At the witness the floor exponent per class is `S - R·log2 p` with
`S = 2^38 = 274,877,906,944`. High-precision (80 digits, S6):

| reading of the minimal admissible `t` | `R` | floor exponent | verdict |
|---|---|---|---|
| `t = ceil(n/L)` (integer condition count) — **the banked `R`** | 4,294,967,340 | **−46.0249 bits** | floor vacuous |
| `t = n/L` (exact balance `tL = n`) | 4,294,967,339 | **+17.9751 bits** | **floor FIRES** |

**One condition of `Lambda` is worth `log2 p = 64` bits of floor** (S6.4:
measured difference 63.99999 bits), and the two defensible readings of the
minimal `t` **straddle zero**. The relative margin is `1.674e-10` of the
object's size (S6.5).

**CATCH-Z8.** Under the exact-balance reading the counting argument alone
forces `Z_1 >= 2^{17.98}`, hence `Z = Z_1^C >= 2^{71.90}` at `C = 4`: on
the banked witness row **`L^perp ∩ T != {0}` is PROVED, with no conjecture
and no heuristic** — the strong form of SL-1b′ is refuted there. Under the
banked reading the same argument misses by 46 bits and says nothing. The
entire counting-level verdict for mystery 2's terminal is decided inside a
single 64-bit window on an object of `2.75e11` bits, by the choice between
`t = n/L` and `t = ceil(n/L)`.

**This does not refute (O1).** `2^{71.9}` is `2^{o(n)}` for `n = 2^41`. It
refutes the *exact-zero* form only — which is precisely CATCH-Z1's point.

---

## 6. What the transport is worth, and the structural no-go

**The discharge ladder** (S8, thresholds solved to 300 bisection steps).
With the banked `(M2)` injectivity bound `|L^perp ∩ T| <= 3^{m-R}`
(`f2_sl1_powersums/PROOFS.md:236-241`), the transported weight floor, and
COROLLARY Z-2.1's `l1` packing (balls of `l1`-radius `R` around ternary
codewords are disjoint, and each contains at least
`sum_{j<=R} C(S,j)` ternary points — choose `j` coordinates and change each
at `l1`-cost 1):

| route | discharge needs | shortfall at the witness |
|---|---|---|
| `(M3)` banked (Singleton + `R+1`) | `R/S > 0.613147` | **39.24x** |
| **+ DLI transport** (Singleton + `2R+1`) | `R/S > 0.442114` | **28.30x** |
| **+ `l1` sphere-packing** (volume + `2R+1`) | `R/S > 0.333333` | **21.33x** |
| forced by saturation | `R/S = 1/log2 p = 0.015625` | — |

The transport is worth a factor `1.3869x`, the packing a further `1.3266x`,
`1.8394x` cumulative — and all three fail (S8.1–S8.4). The banked `(M3)`
threshold `0.61315` is reproduced exactly (S8.1) as a control.

**THEOREM Z-NOGO.** On any admissible row with `k = e`, saturation pins
`R/S = 1/log2 p` exactly. Any bound of the "minimum-distance + counting"
family — i.e. `Z <= 1 + (3^{S}/V)·2^{-alpha R}` with `V` a Singleton or
volume factor and `alpha` a constant — discharges SL-1b′ only if
`R/S` exceeds a constant of the family, at best `1/3`. Hence discharge
requires `log2 p <= 3`, i.e. `p <= 8`. **Every admissible row has
`log2 p >= 39`** (`f2_tq_pin/PROOFS.md:114`, verbatim `log2 p >= 39`). ∎

So the family is not merely short at this row; it is **structurally
incapable** of ever closing SL-1b′ on an admissible row (S8.5). This is
what forecloses routes (a) and (c) of the brief and leaves only route (b).

**Route (a) — the norm sandwich — is dead, quantified (S8.9).**
`background/nodes/dli_c1_ternary_relation_norm_sandwich` is a statement in
`Z[zeta_2N]`: its Claim 4 excludes weight `<= w` only for admissible primes
`q > w^{N/2}`, i.e. here `p > w^{2^37}` — satisfied only by `w = 1`. Its
prime-field shadow, banked and already priced as dominated
(`f2_sl1_powersums/PROOFS.md:262-266`), gives `w >= p^{2R/n} = p^{1/64} =
2.0000` at the admissible object, dominated by THEOREM Z-1's `2R+1` by a
factor **`4.295e9`**. Nothing in the DLI norm machinery reaches this row.

**Route (c) — the `C <= 4` class structure — cannot help by itself.**
`Z = Z_1^C` powers any bound up, but the floor and the ceiling both scale
with `C` in the same way (§4 already carries `C` through), so the
factorisation localises the problem without narrowing it.

**Route (b) — second moments / Weil sums — is the only live route, and its
obstruction is sized.** Expanding with additive characters,
`Z_1 = p^{-R} sum_{u in F_p^R} prod_{s<S} (1 + 2cos(2π f_u(omega^s)/p))`
with `f_u` a sparse odd polynomial of degree `<= 2R-1 = 2^33`. The main
term is the floor of §2. Controlling the `p^R ≈ 2^S` error terms needs
equidistribution of `f_u` on a multiplicative subgroup of size `2^39`
inside `F_p` with `p ≈ 2^64`: square-root cancellation is `~ sqrt(p)·log p
= 2^32·64 = 2^38` against a subgroup of size `2^39` — **a factor 2 of
headroom**, and the mass needs the *product* over `S = 2^38` points, i.e.
joint equidistribution, which no banked instrument supplies. *(Sizing, not
a theorem; stated so nobody re-derives it.)*

---

## 7. Calibration (Z3): what the object actually does

Grid (Z-A12): `2N in {8,12,16,20,24,32}`, primes `p ≡ 1 mod 2N`, `R <= 5`,
shifts `a in {0,1,2,3}` — **696 configurations**, 201 of them carrying a
nonzero ternary kernel. Exhaustive over `3^N` for `N <= 8` and
meet-in-the-middle for `N in {10,12,16}`; the two code paths agree on every
`N <= 8` row (G.1), which is the disjoint-route control.

**(i) The floor holds and is tight.** 0 violations in 696 configurations
(S2.2); within a factor 2 of the ensemble mean everywhere (S2.3).

**(ii) The measured mass is systematically BELOW the random mean.** Over
the 14 saturated rows (`R log2 p / S in [0.90,1.10]`, the miniatures of
`k = e`), `Z/E_random in [0.502, 0.947]`, median `0.769` — **below 1 on all
14** (S3.2, S3.3). This is Z-A13's clause 2 and it fires.

**(iii) The mechanism is exactly the transported weight floor.** The
refined first moment restricted to weight `> 2R`,
`E[Z | wt > 2R] = 1 + (sum_{w > 2R} C(S,w))/p^{dim L}` (the `2^w` sign
patterns and the `2^{-w}` weights cancel), reduces the mean absolute
prediction error from `0.1236` to `0.0789` — **1.57x better** (S3.6) — and
is then **unbiased**: mean signed residual `−0.0095` over 258 rows, 51.6%
below (S3.7). So the deficit against random *is* the excluded low-weight
mass, and nothing else is detectable.

**(iv) Against the ensemble, not the mean.** `f2_sl1_powersums/PROOFS.md:302-307`
poses the question as *"the deployed `L` is no worse than a random subspace
at this one statistic"*; a mean is not a median, so 400 random codimension-`d`
codes were drawn at each saturated point (S11). The deployed GRS code lands
at percentiles `[0.0%, 47.0%]` on the 8 valid miniatures — **at or below the
median at every one** (S11.2). *Honest null:* "better than random" is **not**
established — the percentiles spread over the bulk, and the near-extremal
appearance at the first four rows was small-sample selection, self-caught by
widening the prime list (S11.3).

**(v) CATCH-Z6 — my own registered grid was contaminated.** At composite
`2N` there are `p`-INDEPENDENT ternary relations: the same kernel vectors
occur for *every* `p ≡ 1 mod 2N` (S11.4: `2N=12` → 8 common vectors of min
weight 3, `2N=20` → 8, `2N=24` → 80). At 2-power `2N` there are **none**
(S11.5), because the half-system is a `Z`-basis of `Z[zeta_{2N}]`
(`f2_sl1_powersums/PROOFS.md:266-271`) and every relation is an accident of
`p`. **Only 2-power `2N` rows are valid miniatures of the official object**;
Z-A12's `2N in {12,20,24}` rows carry structural mass the official
`2N = 2^39` object cannot have. All conclusions above are quoted on the
valid subset.

**(vi) What the transport is worth at the official row: nothing (S12).**
The refinement in (iii) deletes the mass carried by weights `<= 2R`. At the
official row `(2R+1)/S = 1/32` while the binomial peak carrying the mass is
at `S/2`: the deleted fraction is at most `2^{-1.743e11}` by Chernoff.
**The crosswalk doubles the DISTANCE and moves the MASS by a factor
`1 - 2^{-Theta(S)}`.** It is measurable at `N = 8` (where the floor covers 5
of 8 coordinates) and exactly nil at `2^33` of `2^38`.

---

## 8. Consistency with the 61 `f2_sl1b` witnesses (Z-A14)

`f2_sl1b/REPORT.md:25`'s smallest witness (`p=7, k=2, n=12, W=mu_12, m=6,
Lambda={5,7}`) was replayed in `F_49` built as `F_7[x]/(x^2-3)` (S9):
`dim L = 4` ✓, min ternary dual weight `3` ✓, `(R-A)` satisfied
(`7^4 = 2401 >= 3^6 = 729`) ✓. My floor gives `Z >= 2^6/7^4 = 0.0267`
against the measured `Z = 1.5625` — **consistent; a lower bound cannot deny
their existence** (S9.5). Two further readings of the witness family:

- It is a **shift-2** configuration with `char > w`, so it is one of §1's
  scope failures, not a counterexample to THEOREM Z-1 (S9.6).
- Its own weighted mass is `Z = 1.5625 = O(1)` even though `(R-B)`
  (`L^perp ∩ T = {0}`) fails there (S9.7). The witnesses refute the
  exact-zero form and leave the mass untouched — which is CATCH-Z1 again,
  visible in the very family that motivated SL-1b′.

---

## 9. CATCHES

1. **CATCH-Z1 (against this brief's §0, and `f2_sl1b/REPORT.md:62`).** The
   equivalence *"`Z_1 <= 2^{o(m)}` (equivalently `L^perp ∩ T = {0}` or
   nearly)"* is **false**. `Z` is weighted; the two forms differ by
   `log2 3` in the exponent — `f2_sl1_powersums/PROOFS.md:304-307` says so
   itself (*"the two differ by exactly `log2 3 = 1.58496`"*) — and at the
   admissible object the mass form is heuristically TRUE (`Z_1 ≈ 1`) while
   the exact-zero form is heuristically FALSE by `≈ (3/2)^S =
   2^{0.585·2^38}`. Measured separation: 67 configurations with `>= 16`
   ternary kernel vectors but `Z < 3`; the extreme is 1,184 ternary vectors
   with `Z_1 = 2.59` (S3.4, S3.5). Conflating them makes a knife-edge
   question look hopeless.
2. **CATCH-Z2 (against a banked statement).** `f2_sl1b/PROOFS.md:288-291`,
   verbatim: *"A first-moment threshold is a statement about an average over
   subspaces; it is not a property of any particular one."* This is **false
   in the direction (O1) needs**: THEOREM Z-FLOOR makes `2^m/p^{dim L}` a
   pointwise lower bound for *every* subspace, and COROLLARY Z-FLOOR.1 shows
   the ensemble mean exceeds it by at most a factor 2. Half of the banked
   "heuristic" is a theorem.
3. **CATCH-Z3 (the three-way seam).** The counting balance (C), LEMMA 3, and
   the vacuity of the mass floor are one inequality on `k = e` rows (§4).
4. **CATCH-Z4 (upgrade of `f2_adm` CATCH-1).** At `k < e`, (O1) is false at
   the level of the **object**, not of a necessary condition, and the
   exponent `2^{5n/12}` is reproduced exactly by an independent route.
5. **CATCH-Z5 (reported to the DLI lane).** The `{+1,-1}` restriction in
   `dli_wcl_newton_short_window_exclusion` is unnecessary: THEOREM Z-2
   extends it to all integer coefficients with the `l1` weight, same cutoff
   `w <= 2ell`, same `char > w`. New instrument for the DLI lane's own
   difference arguments.
6. **CATCH-Z6 (self-caught, methodological).** My registered calibration
   grid was contaminated by composite `2N`, which carries `p`-independent
   cyclotomic ternary relations the official 2-power object cannot have
   (§7(v)). Any future calibration of this terminal must be restricted to
   2-power `2N`.
7. **CATCH-Z7 (route (a) re-priced at the new row).** The norm sandwich
   gives `w >= 2.0000`, dominated by `4.295e9` (§6).
8. **CATCH-Z8 (the 64-bit window).** §5 — the counting-level verdict is
   decided by one condition of `Lambda`, and the two defensible readings of
   the minimal `t` straddle zero.

---

## 10. HONEST RESIDUALS

1. **SL-1b′ is NOT closed.** Nothing here proves `Z_1 <= 2^{o(m)}` at
   `k = e`. What is proved is a floor (§2), a dichotomy that kills `k < e`
   (§4), a transported distance law (§1), an `l1` extension (§3), and a
   no-go showing the whole distance+counting family cannot close it (§6).
   The `k = e` case is left **open, with its remaining route identified and
   its obstruction sized**.
2. The `2^{17.98}` firing of §5 depends on the exact-balance reading of the
   minimal `t`. **I do not resolve which reading governs** — that is the
   `t`-naming collision `f2_adm/REPORT.md:61` flags and the sibling
   `t_naming` owns. Both readings are reported; the difference is one
   condition.
3. THEOREM Z-1 is quoted at shift 0 only. Whether a `2R+1` law holds for
   shifted runs at 2-power `2N` is **open**; 43 shifted counterexamples
   exist in the grid, of which 1 is at 2-power `2N` (S4.4) — a thin sample,
   and I do not claim a general shifted failure law.
4. All calibration is at `S <= 16` against an official `S = 2^38`. The
   `(3/2)^S` count heuristic and the `Z_1 ≈ 1` mass heuristic are
   **heuristics**; only the floor, the dichotomy, the transport and the
   no-go are proved. No toy is evidence about `Z_1` at the official row —
   `f2_adm`'s residual 1 stands unaltered.
5. The Weil sizing in §6 (route (b)) is arithmetic-on-the-back-of-an-
   envelope, explicitly not machine-checked and not a theorem.
6. `C <= 4` and the nested/new-part readings are carried from `f2_adm`
   without independent re-derivation; §4's exponents are stated for the
   nested reading (which governs) with the new-part value given alongside.
7. No status flip is proposed for any minted node. DRAFT ONLY: every file
   written lies in `notes/pilots_20260806/z1_ternary_mass/`; no commit, no
   push; `o1_generating_adversary/` was not read.
8. **Process:** every number came from `tools/ramguard local -- python3`
   runs of `verify.py`. No bare `python3` was invoked at any point,
   including for file patching (Edit/Write tools were used instead).
