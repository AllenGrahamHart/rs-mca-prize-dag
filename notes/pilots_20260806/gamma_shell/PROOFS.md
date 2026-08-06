# PROOFS — THE GAMMA-SHELL QUESTION (round 20, THE PRIORITY)

Opus pilot, `notes/pilots_20260806/gamma_shell/`. Every claim below is
registered in `PREREG.md` §P0–P7 **before** computation. Machine checks in
`toy_shell.py` (stages `siglift / dsbiject / shell / mult / count / census /
pipeline` + a permanent `failclosed` that exits 1) and `shell_exhibit.py`
(stages `row / shell / bound / compare / region / profile` + `failclosed`).
Totals: **245,402 checks, 0 failures**; both `failclosed` controls exit 1.

---

## §0. The objects, quoted

**The crossing count and the shell**, verbatim
`notes/pilots_20260804/crossing_w2_opening/PREREG.md:5-25`:

> From `background/nodes/xr_band_key_lemma_pencil_mass` MC-1 (PROVED,
> general `w`): with `H = x_0 mu_n` (`n | q-1`, split),
> `u = X^{n-1} + c X^{k+w-1}`, `c != 0`, `r' = n-k-w`, the codewords of
> agreement `>= k+w` with `u` are EXACTLY indexed by
>
> ```text
> {T <= H : |T| = r', e_1(T) = ... = e_{w-1}(T) = 0, prod T = gamma},
> gamma = (-1)^{r'+1} c.
> ```
>
> Write `T = T(S) = {x_0 zeta^i : i in S}` ... Define the WINDOW SET
>
> ```text
> W_w := {S <= Z/n : |S| = r', e_s(T(S)) = 0 for s = 1..w-1}
> ```
>
> ... and `sig(S) := sum_{i in S} i mod n`.
> The crossing count is `X_w(gamma) := #{S in W_w : prod T(S) = gamma}`.

Since `prod T(S) = x_0^{r'} zeta^{sig(S)}` and `zeta` has order `n`, the
gamma-SHELL **is exactly a `sig` class mod `n = 2^41`**: `X_w(gamma) =
#{S in W_w : sig(S) = t(gamma)}`, and `c` is a FREE parameter of the received
word, so **every one of the `2^41` shells is realised by an actual received
word**. Hence for every shell `t`,

```text
(REALISE)      L_1(k+w)  >=  X_w(zeta^t · x_0^{r'})  =  #{S in W_w : sig(S) = t}.
```

**The obligation**, verbatim
`critical/nodes/rate_half_list_adjacent_crossing/statement.md:7-23`:

> ```text
> q=|F|,
> B*=floor(q/2^128),
> L_1(a)=max_u #{c in C: agr(c,u)>=a}.
> ```
>
> There is an agreement index `a_L(C)` such that
>
> ```text
> L_1(a_L(C)) <= B* < L_1(a_L(C)-1).                 (RHL-ADJ)
> ```

**The lower bound already banked**, verbatim same file `:25-41`:

> ```text
> a_L(C)>=k+17,179,869,184 = k+2^34.                  (RHL-LB)
> ```

**The deep stratum**, verbatim
`background/nodes/crossing_dsa_refutation/statement.md:16-21`:

> **LEMMA DS.** At n = 2^41, w = 2^v, r' = 2^40 - w, the deepest
> stratum a = v-1 has n_a = 2^{42-v}, L = 2^{41-v}, r'_a = L - 2
> (uniformly in v — ONE one-parameter family (2L, L-2)), a single
> surviving condition p_1(S') = 0, and the stratum members biject with
> reduced solutions WITH NO SIDE CONDITIONS (LEMMA FREE: zero lift
> constraints — every non-structural reduced solution lifts freely).

**The fibre law**, verbatim `notes/pilots_20260806/crossing_low_w/PROOFS.md:169-178`:

> > **LEMMA TC.** The single deep-stratum condition depends on `S'` only through
> > `eps in {0,±1}^L`. The fibre over `eps` has size
> > `C(L-U, (r'_a-U)/2)` where `U = |supp(eps)|`, nonempty iff `U ≡ r'_a (mod 2)`
> > and `U <= r'_a`; and ... `eps = 0` is exactly the structural fibre, of size
> > `C(L, r'_a/2)`.

**The open question this pilot owns**, verbatim
`background/nodes/crossing_dsa_refutation/statement.md:71-76`:

> ## NOT claimed
>
> Emptiness at prime rows (heuristic only); the gamma-shell population
> of the accidents (the crossing NODE's budget question at tower rows
> is RE-OPENED, not decided); ...

**The row**, verbatim `notes/pilots_20260806/es_g_lanes/PROOFS.md:174-179`:

> ```
> p = 6597069766657 = 3·2^41 + 1   (prime; p ≡ 1 mod 2^41, so delta = 1)
> e = 6,  q = p^6,  log2 q = 255.509775 < 256,  2^41 | q−1,  k = 2^40
> B* = floor(q/2^128) = 242251802232021244567343686397347233808 (log2 B* = 127.510)
> ```

**The lane's live-range criterion**, verbatim
`notes/pilots_20260806/es_g_lanes/full_run.txt:126-127`:

> ```
> Which w the crossing lane can actually use: structural count S(v) = C(2^(41-v), 2^(40-v)-1)/2^(41-v)
>    w=2^34: log2 S =   117.1491   (needs log2 B* >= this, i.e. log2 q >= 245.1491)
> ```

---

## §1. (G1) THE SIG-ARITHMETIC OF THE PERIODIC LIFT

> **LEMMA SL (SIG-LIFT).** Let `a = v-1`, `n_a = 2^{42-v}`, and let `S` be the
> lift of `S' <= Z/n_a`, i.e. `S = {j + n_a t : j in S', 0 <= t < 2^a}`. Then
>
> ```text
> sig(S)  =  2^a · sigma'(S')  +  |S'| · n_a · 2^{a-1} · (2^a - 1)   (mod n),
> ```
>
> `sigma'(S') = sum_{j in S'} j` taken as an INTEGER. At the crossing family's
> deep stratum (`|S'| = r'_a`) the second term VANISHES mod `n`, so
>
> ```text
> sig(S)  =  2^a · sigma'(S')  (mod n),      depending on S' only through
> sigma'(S') mod n_a.
> ```

**Proof.** `sum_{i in S} i = sum_{j in S'} sum_{t<2^a} (j + n_a t)
= 2^a sigma'(S') + |S'| n_a (2^a-1)2^a/2`, which is the displayed formula.
For the vanishing: at the prize shape `v = 34`, `|S'| = r'_a = 126`,
`n_a = 256`, `a = 33`, the second term is `126·256·2^32·(2^33-1)
= 63·2^41·(2^33-1) ≡ 0 (mod 2^41)`. In general `|S'| = r'_a = L-2` is even and
`n_a 2^{a-1} = 2^{41-v+v-1} · ... = 2^{40}`-type, giving `r'_a · 2^{40} ≡ 0`
whenever `r'_a` is even. ∎

**MANDATORY TOY GATE (falsifier F1), PASSED.** `toy_shell.py siglift`:
exhaustive over **every** subset of `Z/n_a` (all sizes, not merely `r'_a`) at
all three DSA gate shapes `(n,w) = (32,8), (64,8), (64,16)` — 256 + 65,536 +
256 = **66,048 subsets, 0 failures**, and the second term is `0 mod n` at
`|S'| = r'_a` in all three shapes.

*Independent re-check of the imported bijection:* `toy_shell.py dsbiject`
re-derives LEMMA DS/FREE from scratch (direct evaluation of all `w-1` window
conditions, no lemma used) at the three shapes × 5 primes each — **40,350
checks, 0 failures**, reproducing round 18's structural counts
`C(n/M, r'/M)` exactly.

### 1.1 The shell map of the accident family

> **THEOREM SM (the shell map).** At `n = 2^41`, `w = 2^v`, deep stratum
> `a = v-1`:
>
> 1. **(CONCENTRATION)** Every deep-stratum member — structural or accidental
>    — has `sig(S) in 2^a·Z/n`. The whole deep stratum therefore occupies at
>    most `2L = n_a` of the `n = 2^41` shells. At `v = 34`: **256 shells out of
>    2^41, a concentration factor of `2^33`.**
> 2. **(STRUCTURAL SHELLS)** A structural `S'` is a union of `r'_a/2` antipodal
>    pairs `{j, j+L}`, so `sigma' = 2·(sum j) + (r'_a/2)·L` is EVEN; structural
>    members occupy exactly the `L` shells `2^{a+1}·Z/n`, and are EXACTLY
>    equidistributed over them, `|W^struct|/L` per shell.
> 3. **(ACCIDENT PARITY)** An accident with `sigma'` even lands **in a
>    structural shell**; with `sigma'` odd it lands in one of the `L` shells
>    disjoint from the structural ones.
> 4. **(FIBRE SPREAD)** Within one `eps`-fibre, `sigma' = const + 2·(sum of the
>    chosen zero-pair indices)`, so a single fibre spreads over at most `L`
>    shells, all of one parity class.

**Proof.** (1) is LEMMA SL: `sig = 2^a sigma'`. (2): `sum over a pair
{j, j+L}` is `2j + L`; summing `r'_a/2` pairs gives `2·(sum j) + (r'_a/2)L`,
even since `L` is even; equidistribution: the structural shell index is
`2^{a+1}·(subset-sum of an `r'/M`-subset of `Z/(n/M)`) `, and
`gcd(n/M, r'/M) = gcd(128, 63) = 1` at `v = 34`, for which the number of
`m`-subsets of `Z/N` with prescribed sum mod `N` is EXACTLY `C(N,m)/N` (the
Ramanathan/Lehmer count; only the `d = 1` term survives). (3) is immediate
from `sig = 2^a sigma'` and (2). (4) is LEMMA TC's fibre description: the `U`
forced positions are fixed and each chosen zero-pair contributes `2j + L`. ∎

At `v = 34`: `|W^struct| = C(128,63) = 23582666872052266206656578733667004800
= 2^124.1491`, and `v_2(C(128,63)) = 7` exactly, so

```text
structural per shell = C(128,63)/128
                     = 184239584937908329739504521356773475 = 2^117.1491
```

which **reproduces the banked `[B4]` figure `2^117.1491` EXACTLY**
(`es_g_lanes/full_run.txt:127`; `verify_rows.py:156-176`). This is the
pilot's dictionary check: an independent derivation of the same number from
the shell arithmetic.

**TOY GATE (falsifier F2), PASSED.** `toy_shell.py shell` — 844 checks, 0
failures over the three shapes × 5 primes: every deep-stratum `sig` lies in
`2^a Z`, the count of occupied shells never exceeds `2L`, every structural
`sig` lies in `2^{a+1} Z`, the structural per-shell profile is CONSTANT and
equals `|W^struct|/L`, and the parity rule holds set-by-set. **Both branches
of (ACCIDENT PARITY) are exercised**: at `(64,8)` the 8 accidents land on the
8 STRUCTURAL shells when `p = 193`, and on 8 disjoint NEW shells when
`p = 577`.

*Dictionary gate:* `toy_shell.py census` runs a FULL `W_w` census
(meet-in-the-middle, no lemma used) at `(16,4)` × 6 primes and `(32,8)` × 5
primes, verifies LEMMA X (`sig` fibres equal within classes mod
`d = gcd(r',n)`), verifies `X_w(gamma) = #{S : sig(S) = t}` for **every** one
of the `n` shells, and locates the deep stratum inside the whole census —
324 checks, 0 failures.

---

## §2. (G2) THE PROVED ACCIDENT COUNT — Cauchy–Schwarz with the LEMMA TC weight

Round 18 proved ONE relation and hence `>= C(108,53) = 2^104.267` accidents.
That is 13 bits short of mattering. The following upgrades the count from
*one relation* to *essentially the heuristic total*, **with proof**.

Fix the deep stratum, put `Q = p^{delta_a}` (so `theta` generates
`F_Q` over `F_p`), and let

```text
D = { x in {0,1}^L : x_{L-1} = 0, |x| even },      |D| = 2^{L-2},
phi(x) = sum_j x_j theta^j  in  F_Q.
```

> **LEMMA MULT.** For a nonzero `eps in {0,±1}^L` with `eps_{L-1} = 0` and
> `U = |supp eps)| even, `#{(x,y) in D^2 : x - y = eps} = 2^{L-2-U}` exactly;
> and every difference of two distinct elements of `D` is such an `eps`, with
> `U` even and `2 <= U <= L-2 = r'_a`.

**Proof.** `x = y + eps` forces `y_j = 0` where `eps_j = +1` and `y_j = 1`
where `eps_j = -1`; off `supp(eps)` and off the index `L-1` (fixed to 0 in
both) the `L-1-U` coordinates are free subject to `|y|` even, giving
`2^{L-2-U}` choices; then `|x| = |y| + (#\{+1\} - #\{-1\})` is even because
`U` is even. Conversely `x - y` has `eps_{L-1} = 0`, so
`supp(eps) ⊆ [0, L-1)`, whence `U <= L-1`, and `U = |x| + |y| - 2|x ∧ y|` is
even, so **`U <= L-2 = r'_a`**. ∎

*The last sentence is load-bearing:* it is exactly why the fibre
`C(L-U, (r'_a-U)/2)` of LEMMA TC is always NON-empty for these `eps`. Excluding
coordinate `L-1` from `D` — THEOREM DSA's own trick — is what buys it.

> **THEOREM AC (the accident count, PROVED).** With
> `rho_min := min over even U in [2, r'_a] of C(L-U,(r'_a-U)/2) / 2^{L-2-U}`,
> the number `N_acc` of NON-structural deep-stratum reduced solutions obeys
>
> ```text
> N_acc  >=  rho_min · ( |D|^2 / Q  −  |D| )        (unconditional).
> ```

**Proof.** Let `P := #{(x,y) in D^2, x != y, phi(x) = phi(y)}`. Since
`phi` takes at most `Q` values, Cauchy–Schwarz gives
`P = sum_gamma |phi^{-1}(gamma)|^2 − |D| >= |D|^2/Q − |D|`.
By LEMMA MULT, `P = sum_eps 2^{L-2-U(eps)}` summed over the nonzero relations
`eps` (`sum_j eps_j theta^j = 0`) with `eps_{L-1} = 0` and `U` even; each such
`eps` has `2 <= U <= r'_a`, so LEMMA TC gives it a fibre of
`C(L-U, (r'_a-U)/2) >= rho_min · 2^{L-2-U}` reduced solutions, all
non-structural (`eps != 0`), and fibres over distinct `eps` are disjoint
(each `S'` determines its `eps`). Summing, `N_acc >= rho_min · P`. ∎

`rho(U) = C(L-U,(r'_a-U)/2)/2^{L-2-U}` is increasing in `U`, so
`rho_min` is attained at `U = 2`: `rho_min = C(L-2, (L-4)/2)/2^{L-4}`.
At `L = 128`: `rho_min = C(126,62)/2^124 = 0.279327484 = 2^-1.8400`.

**TOY GATE (falsifier F3), PASSED.** `toy_shell.py mult` verifies LEMMA MULT
exhaustively at `L = 4, 6, 8` (every difference vector of every ordered pair;
4,899 checks). `toy_shell.py count` verifies the whole chain exhaustively at
`(L, 2L) = (8,16)` with `p = 17` and `(16,32)` with all seven primes
`97, 193, 257, 353, 449, 577, 641` — **198,907 checks, 0 failures**:
the Cauchy–Schwarz step, the identity `P = sum_eps 2^{L-2-U}` (EXACT match),
and `N_acc >= rho_min·(|D|^2/Q − |D|)` against the TRUE accident count
computed by an independent meet-in-the-middle counter (cross-checked against
brute force at `L = 8`). Observed slack: **2.40×–2.52×**, i.e. the bound is
tight to ~1.3 bits — as expected for a Cauchy–Schwarz bound against a
near-equidistributed map.

**CATCH (mine, found by the gate).** The relation set also contains
**odd-support** `eps`. These arise from no difference of two `D`-elements
(both have even weight) AND have an EMPTY LEMMA-TC fibre (`U ≡ r'_a mod 2`
fails, `r'_a` even). They contribute to NEITHER side of the inequality. A
version of the argument that summed over all relations would be wrong in the
`P`-identity; restricting to even `U` is necessary and sufficient. Registered
as the reason `toy_shell.py count` exits 0 only after the restriction.

### 2.1 At the prize row

`shell_exhibit.py bound` (7 checks, 0 failures), `delta_a = ord_256(p) = 1`
so `Q = p`:

```text
|D| = 2^126,   Q = p = 2^42.5850,   Q < |D|  (Cauchy-Schwarz non-vacuous)
P    >= |D|^2/Q − |D|            = 2^209.4150
rho_min = C(126,62)/2^124        = 2^-1.8400
N_acc >= 306423098481036698674274279159834205215320026136000788784454004
      = 2^207.5751                                                (PROVED)
```

Two sanity conditions, both checked: the proved bound is **below** the banked
heuristic total `C(256,126)/p = 2^209.043` (as it must be), and **above**
round 18's single-relation figure `C(108,53) = 2^104.267` (a 103-bit
improvement).

---

## §3. (G2/G3) THE COMPARISON — exact integers

By THEOREM SM(1) the `N_acc` accidents occupy at most `2L = 256` shells, so
some shell carries at least `N_acc / 256` of them; by (REALISE) that shell is
realised by an actual received word. `shell_exhibit.py compare`, **pure
integer arithmetic at the comparison** (floats only for display):

```text
B*                        =                     242251802232021244567343686397347233808
max-shell accident count >= 1196965228441549604196383902968102364122343852093753081189273
structural per shell      =                      184239584937908329739504521356773475

log2 B*                   = 127.5098
log2 max-shell accidents  = 199.5751
log2 structural per shell = 117.1491

max-shell // B*           = 4940996175934053617705
```

> **THEOREM BB (the budget break, at the DSA witness row).**
> At `p = 3·2^41+1`, `e = 6`, `q = p^6`, `n = 2^41`, `k = 2^40`, `w = 2^34`:
>
> ```text
> L_1(k + 2^34)  >=  max_gamma X_{2^34}(gamma)  >  B*,     by 72.0653 bits.
> ```
>
> Consequently `a_L(C) > k + 2^34` at that row: **agreement `k + 2^34` is
> UNSAFE.**

**Control (checked):** the STRUCTURAL family alone stays *within* budget, by
`127.5098 − 117.1491 = 10.3607` bits — reproducing the banked margin. **The
break is caused entirely by the accidents**, not by a re-reading of the
structural count.

**End-to-end gate.** `toy_shell.py pipeline` runs the *entire* inequality
chain used above — `N_acc >= rho_min(|D|^2/Q − |D|)` then
`max-shell >= N_acc/2L` — at the toy shape `(n,w) = (64,4)`
(`a=1, n_a=32, L=16, r'_a=14`) against the **brute-force per-shell accident
profile**, for five primes. All 31 checks pass; accidents occupy exactly
`2L = 32` shells; observed slack of the pigeonhole bound against the true
maximum: **2.42×–2.60×**.

### 3.1 The row region, and the WORST row (P7)

`shell_exhibit.py region`. Two conditions must hold for the break: the lane
must WANT `w = 2^34` (`B* >= 2^117.1491`, i.e. `log2 q >= 245.1491`,
`es_g_lanes/full_run.txt:127`) and Cauchy–Schwarz must be non-vacuous
(`Q = p^{delta_a} < 2^126` — **exactly THEOREM DSA's own regime condition**).

```
  e   delta_a  log2 p LIVE window     break sub-window   min margin
  2   1        [122.5745, 128.0000)   [122.576, 123.306]    +0.0011
  3   1        [ 81.7164,  85.3333)   [81.717,  85.333] FULL +28.8267
  4   1        [ 61.2873,  64.0000)   [61.288,  63.999] FULL +50.1634
  4   2        [ 61.2873,  64.0000)   [61.288,  61.653]     +0.0011
  5   1        [ 49.0298,  51.2000)   [49.030,  51.199] FULL +62.9633
  5   2        [ 49.0298,  51.2000)   [49.030,  51.199] FULL +11.7638
  6   1        [ 40.8582,  42.6667)   [40.859,  42.667] FULL +71.4934
  6   2        [ 40.8582,  42.6667)   [40.859,  42.667] FULL +28.8267
```

- **`e = 1` (the recorded PRIME rows) are UNTOUCHED.** The live lane needs
  `log2 q = log2 p >= 245.149 > 126`, so `Q = p >= 2^126 > |D|` and
  Cauchy–Schwarz is VACUOUS. This reproduces THEOREM DSA's dichotomy
  (`crossing_dsa_refutation/statement.md:52-53`) from an independent
  direction.
- **`e in {3,4,5,6}` at `delta_a = 1`: the break covers the ENTIRE live
  window**, worst-case margin `+28.83` bits (at `e = 3`), and `+71.49` bits
  across the whole `e = 6` window.
- **`e = 2` and `(e,delta_a) = (4,2)`: PARTIAL** — a sub-window only.
- The **minimum margin over the break region is `+0.0011` bits**, attained at
  the *region boundary* (`e = 2`, `log2 p = 123.3056`). That is the boundary
  by definition and carries no information; the honest worst-case statement is
  the per-`(e,delta_a)` table above.

**Honest scope:** the region is characterised by inequalities on
`(log2 p, e, delta_a)`. Existence of an actual admissible row inside it is
established by the WITNESS row, verified exactly (`shell_exhibit.py row`, 16
checks: primality by deterministic Miller–Rabin, `q < 2^256`, `2^41 | q−1`,
`k <= 2^40`, `B* >= 3`, `w <= p`, `p >= 2^39+1`, `theta` of exact order 256,
`p ≡ 1 mod 256`). I do **not** re-derive `es_g_lanes`' 19-pair `(class, e)`
labelling; I give the region directly.

---

## §4. (G3) WHAT ACTUALLY BREAKS — the consumer chain, traced

The chain (edges verified in both `dag.json` and the `node.json` shards):

```
rate_half_list_adjacent_crossing --req--> list_adjacency_closing
   --req--> list_large_m_scope_closure --req--> list_grand --req--> prize
   --req--> f1_pole_list_threshold_location --req--> f1_case_pole
        --req--> f1_classification --req--> ext_lift --req--> mca_safe
        --req--> mca_grand --req--> prize
```

Every step is `req`; there is **no `alt` and no `gate:any`** anywhere on
either route (`critical/nodes/*/node.json`, `"alternatives": []` at every
node; the DAG's only alt touching the chain is `route_noslack -> mca_safe`,
whose status is REFUTED and whose parent has `"gate": "all"`). Confirmed by
the roadmap, verbatim `notes/roadmap/sections/04-board-anatomy.md:15-18`:

> - **Wired bottlenecks** (no alt, no upstream substitute):
>   `l1_mixed_petal_amplification`, `rate_half_list_adjacent_crossing`,
>   `rate_half_band_closure`, + the dossier. There is NO MCA-only resolution
>   (F1 pole pricing imports the base-row list threshold).

**Now the load-bearing honesty step (registered as P5).** I checked the
LOGICAL FORM of each consumer statement before calling anything a refutation.

1. **(RHL-ADJ) is NOT refuted, and CANNOT be.** It asserts *"There is an
   agreement index `a_L(C)` such that ..."*. `L_1` is non-increasing with
   `L_1(n) <= 1 <= B*` and `L_1(k) > B*`, so such an index exists for trivial
   reasons. Making `L_1` larger at one agreement **relocates** `a_L(C)`; it
   cannot falsify an existence claim.
2. **(RHL-LB) is not refuted — it is STRENGTHENED.** The banked bound is
   `a_L(C) >= k + 2^34`; THEOREM BB gives `a_L(C) >= k + 2^34 + 1` on the
   break region.
3. **The grand challenges are DETERMINATIONS, not conjectures.** Verbatim
   `critical/nodes/list_grand/node.json:13`:
   > `"For each admissible C and constant m: exhibit adjacent delta with |Lambda(C^{==m},.)| crossing 2^-128 |F| at it. ..."`
   and `critical/nodes/mca_grand/node.json:13`:
   > `"For each admissible C: exhibit adjacent a with B_C(a-1) > floor(q_line/2^128) >= B_C(a), all conventions printed. ..."`
   There is no threshold *value* asserted in either that a larger list could
   contradict. Verbatim `notes/JOINT_PRIZE_RESOLUTION_PROTOCOL.md:17-20`:
   > `Resolve both Proximity Prize grand challenges, ordinary LIST and MCA, for the`
   > `actual challenge specification. A counterexample that relocates a threshold`
   > `is a valid route to resolution; preserving a conjectured threshold is not`
   > `an objective.`
4. **What DOES die** is the campaign's *working localisation*: the programme of
   pinning `a_L(C) = k + 2^34` by proving safety at the bracket bottom. At
   break-region rows, `L_1(k+2^34) > B*` is now PROVED, so **no route
   whatsoever — not merely the (ES) route — can establish safety at
   `w = 2^34` there.** THEOREM DSA killed our intermediate; THEOREM BB kills
   the *claim* the intermediate was serving.
5. **A catch against a banked criterion.** `es_g_lanes/full_run.txt:126-127`
   prices the lane's usable `w` by `B* >= S(v)` (structural per shell). At
   break-region rows that criterion is **wrong**: `B* >= S(34)` holds yet the
   true shell count exceeds `B*` by up to 72 bits. The criterion must be
   re-priced with an accident term.
6. **`mun` [B4] survives as written but not as read.** Verbatim
   `notes/pilots_20260804/mun_anticoncentration/verify_rows.py:171-175`:
   > `print("  => the MC/coset family MISSES B* by %.2f bits at the bracket"` …
   > `print("     bottom and by more above: the UNSAFE leg of (RHL-ADJ)")`
   > `print("     cannot be fired by the coset construction anywhere in")`
   > `print("     [2^34, 2^39].  Consistent with the banked staircase, whose")`
   The claim is scoped to *the coset construction* and remains TRUE (my
   control check reproduces the `10.36`-bit miss). What is now false is the
   strategic reading that the unsafe leg cannot be fired at `w = 2^34` at
   all: a NON-coset construction fires it.

**Therefore the verdict is BUDGET-BREAK WITH THRESHOLD RELOCATION, and it is
a CANDIDATE for coordinator replay — not a claimed resolution, and NOT a
refutation of either grand challenge.** Anyone reporting this as "the grand
challenge is refuted" would be overclaiming; the grand challenges ask for a
threshold *plus converse*, and this moves the threshold by (at least) one
step at a sub-family of rows.

---

## §5. (G3) RE-POSE GUIDANCE — what the node should claim instead

The (ES) route is dead at tower rows and the safe side at `w = 2^34` is dead
on the break region. The node's rate-half obligation should be re-posed as:

1. **Lower side (now PROVED here, on the break region):**
   `a_L(C) >= k + 2^34 + 1`, strengthening (RHL-LB) by one step.
2. **Safe side: move to `w = 2^35`.** At the witness row the deep stratum
   there is comfortably within budget (`shell_exhibit.py profile`):
   structural per shell `2^54.624`, proved max-shell accidents `2^73.061`,
   against `log2 B* = 127.510` — a **54-bit** margin.
3. **The safe-side statement must carry an explicit per-shell accident term**,
   i.e. replace "(ES): `|W_w| = C(n/M, r'/M)`" by
   ```text
   X_w(gamma)  <=  S(v)  +  Acc_deep(v, p, delta_a)  +  Acc_shallow(v, p),
   ```
   with `S(v) = C(2^{41-v}, 2^{40-v}-1)/2^{41-v}` and `Acc_deep` an **upper**
   bound on the maximal-shell deep-stratum accident population. **Nothing in
   this pilot supplies that upper bound** — THEOREM AC is a LOWER bound. This
   is the honest next obstacle, and it is now the crux of the safe side.
4. **`Acc_shallow` is untouched.** Strata `a < v-1` and aperiodic `S` are not
   analysed anywhere (LEMMA OE gives the recursion; it has never been carried
   out). A safe-side claim needs them too.

---

## §6. (G4) THE PT-2 INTERACTION — is the verdict stable across the bracket?

`shell_exhibit.py profile`, at the witness row (`log2 B* = 127.510`):

```
  w      L     n_a    r'_a   struct/shell  2^{L-2}   log2 max-shell  verdict
  2^34   128   256    126    2^117.149     2^126     199.575         BREAK
  2^35   64    128    62     2^54.624      2^62       73.061         within
  2^36   32    64     30     2^24.076      2^30      -               no proved acc
  2^37   16    32     14     2^9.482       2^14      -               no proved acc
  2^38   8     16     6      2^2.807       2^6       -               no proved acc
  2^39   4     8      2      2^0.000       2^2       -               no proved acc
```

> **The verdict is NOT uniform across the bracket. It is a statement about the
> bracket's LOWER ENDPOINT `w = 2^34` and nothing else.**

- At `w = 2^35` the same machinery is *within* budget by 54 bits: `|D|` drops
  to `2^62` while `Q = p` is unchanged, so the Cauchy–Schwarz bound collapses
  from `2^207.6` to `2^80.1`, and the shell divisor only halves.
- At `w >= 2^36` the bound is VACUOUS (`Q >= 2^{L-2}`), matching THEOREM DSA's
  own coverage table (`crossing_low_w/PROOFS.md:363-371`) — falsifier F6 did
  not fire.
- Hence the **re-pose is stable**: only the endpoint moves; the rest of the
  bracket `[2^35, 2^39]` is unaffected by the accident term at the deep
  stratum.

**The PT-2 watch line is the right alarm, and this is its tower-row
instance.** Verbatim
`notes/pilots_20260806/tern_unification_adversary/REPORT.md:69`:

> **COROLLARY PT-2 (new, campaign-relevant).** The crossing bracket's lower
> endpoint `w = 2^34` clears the ternary threshold `log2(3)·2^33` by only
> **0.336 bits**. One step below the bracket (`v = 33`, `L = 256`) gives
> `tau = 1` and `+149.75` bits — the deep stratum would be supercritical at
> the **recorded PRIME rows**, not just tower rows.

Two honest qualifications on how PT-2 relates to what is PROVED here:

1. My proved bound is **strictly weaker** than the ternary heuristic: it needs
   `Q < 2^{L-2}`, the heuristic needs `Q < 3^L`. The gap is
   `L(log2 3 − 1) − 2` bits `= 76.9` bits at `L = 128`. So the proved break
   region is a strict sub-region of the heuristic one.
2. Consequently, **PT-2's `v = 33` prime-row scenario is NOT reachable by this
   argument**: at `v = 33`, `L = 256`, `|D| = 2^254` while prime rows have
   `Q = p ≈ 2^256 > |D|`, so Cauchy–Schwarz is vacuous there too. The prime
   rows remain protected against *this* method at every `v` in and below the
   bracket. PT-2's alarm is about the *heuristic* margin, and it stands
   un-upgraded.

---

## §7. Self-checks and negative controls

- **Fail-closed, proven not asserted.** `toy_shell.py failclosed` and
  `shell_exhibit.py failclosed` inject a false check and exit **1**; all 13
  substantive stages exit **0**. Totals: 245,402 checks, 0 failures.
- **No floats at the comparison.** `stage_compare` compares Python integers;
  `rho_min` and the Cauchy–Schwarz bound are exact `Fraction`s truncated
  DOWNWARD (`int(...)`, the conservative direction). Floats appear only in
  `log2` display strings.
- **Both directions of the count are cited.** The count lower bound is
  THEOREM AC (proved here, toy-gated, 2.4× slack observed); the budget upper
  bound `B* = floor(q/2^128)` is the node's own definition
  (`statement.md:7-23`) recomputed from `q = p^6`.
- **The banked numbers are reproduced, not assumed**: `log2 B* = 127.510`,
  `S(34) = 2^117.1491`, `|W^struct| = 2^124.149`, `L·log2 3 = 202.875`,
  `C(108,53) = 2^104.267`, `C(256,126)/p = 2^209.043`.
- **A defect of my own, found and fixed:** the first `stage_row` used base 3
  to build `theta`, which is not guaranteed to have full 2-power order mod
  `p`; the check FAILED and was repaired to use a quadratic non-residue with
  the order verified. Reported rather than buried.
- **A second defect, found by the gate:** the odd-support relations (§2
  CATCH). Both sides of the inequality must exclude them.

## §8. What is NOT proved

1. **No UPPER bound on the shell population** anywhere. THEOREM AC is a lower
   bound; the safe side needs an upper bound and does not have one.
2. **Only the deep stratum `a = v-1`.** Strata `a < v-1` and aperiodic `S`
   contribute more members in unknown shells; they can only make the break
   larger, but they are not counted.
3. **`delta_a = 4` and most `delta_a = 2` rows** are handled only through the
   crude `Q = p^{delta_a} < 2^{L-2}`; a Frobenius-adapted pigeonhole would
   enlarge the region.
4. **The 19-pair `(class, e)` labelling of `es_g_lanes` is not reproduced**;
   the break region is given as inequalities plus one exactly-verified row.
5. **Prime rows (`e = 1`) are untouched**, and this method cannot touch them
   at any `v` in the bracket (§6.2).
6. **Toy scale is `n_a <= 32`, `L <= 16`.** The prize-row statements are
   consequences of lemmas proved for all `L`, instantiated at `L = 128` with
   exact integer arithmetic — not extrapolated.
