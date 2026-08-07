# PROOFS — BB method transport -> accident UPPER bound / nu(A) (round 22)

Opus pilot, `notes/pilots_20260807/bb_nu_transport/`. Every claim below is
registered in `PREREG.md` under `# PILOT REGISTRATIONS` (§P0–P9) **before**
computation. Machine checks in `transport.py` (stages
`mfun / census / relations / dict / prize / nu` + a permanent `failclosed`
that exits 1), output in `full_run.out` and `failclosed.out`.
Totals: **1550 checks, 0 failures**; `failclosed` exits 1.

---

## §0. The objects, quoted

**The window set and the shell**, verbatim
`notes/pilots_20260806/gamma_shell/PROOFS.md:27-34`:

> > ```text
> > W_w := {S <= Z/n : |S| = r', e_s(T(S)) = 0 for s = 1..w-1}
> > ```
> > ... and `sig(S) := sum_{i in S} i mod n`.
> > The crossing count is `X_w(gamma) := #{S in W_w : prod T(S) = gamma}`.

**The realisation direction**, verbatim `.../gamma_shell/PROOFS.md:42-44`:

> ```text
> (REALISE)      L_1(k+w)  >=  X_w(zeta^t · x_0^{r'})  =  #{S in W_w : sig(S) = t}.
> ```

**The crux this pilot was pointed at**, verbatim
`.../gamma_shell/PROOFS.md:476-483`:

> 3. **The safe-side statement must carry an explicit per-shell accident term**,
>    i.e. replace "(ES): `|W_w| = C(n/M, r'/M)`" by
>    ```text
>    X_w(gamma)  <=  S(v)  +  Acc_deep(v, p, delta_a)  +  Acc_shallow(v, p),
>    ```
>    with `S(v) = C(2^{41-v}, 2^{40-v}-1)/2^{41-v}` and `Acc_deep` an **upper**
>    bound on the maximal-shell deep-stratum accident population. **Nothing in
>    this pilot supplies that upper bound** — THEOREM AC is a LOWER bound. This
>    is the honest next obstacle, and it is now the crux of the safe side.

and verbatim `critical/nodes/rate_half_list_adjacent_crossing/statement.md:4085-4089`:

> side of the localisation moves to w = 2^35 (54-bit deep-stratum
> margin, stable across [2^35, 2^39]); the open crux is an
> ACCIDENT UPPER BOUND on shell populations. e = 1 prime rows
> untouched and provably unreachable by the method.

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

**The total identity**, verbatim `.../crossing_low_w/PROOFS.md:175`:

> > sum_{eps} C(L−U(eps), (r'_a−U(eps))/2)  =  C(2L, r'_a).

**The warning of record**, verbatim
`notes/pilots_20260807/red_closability_probes/REPORT.md:37`:

> **Exact finite countermodel**, both counts computed exhaustively on
> `RS[F_5,|D|=4,k=2]`: at `a=2`, `L_1 = 6 > B* = 5 >= B_C = 5` — so
> `L_1(a) > B*` does **not** imply `B_C(a) > B*`.

**The M route**, verbatim `critical/nodes/averaged_slope_conversion/statement.md:19-29`:

> ```text
> E[Y(A)] >= E[N(A)]-(q/2)C_t(A).
> ```
> Consequently, for every integer `B>=1`, if
> ```text
> nu(A)=E[N(A)]-(q/2)C_t(A) > B-1,
> ```
> some received pair has at least `B` distinct finite bad slopes witnessed by
> `A`. Prize use takes `B=B*+1`, so the strict certificate is `nu(A)>B*`.

and the first moment, verbatim `critical/nodes/averaged_slope_conversion/proof.md`:

> ```text
> E[N(A)]=|A|(1-q^(-t))q^(1-t).
> ```

---

## §1. (D1) THE METHOD ANATOMY — nine steps, graded by direction

The target functional is `Acc_deep := max_gamma #{deep-stratum accidents in
shell gamma}` and the direction is **UPPER**. BB's target functional is the
same object with direction **LOWER**. Grading each named step by what it
proves (direction / functional / row region):

| # | step | what it PROVES | direction | transports to an UPPER bound? |
|---|---|---|---|---|
| BB-1 | LEMMA DS / FREE | deep stratum ↔ `S' ⊆ Z/n_a`, `\|S'\|=r'_a`, one condition | **bijection** | **YES** — bijections are direction-free |
| BB-2 | LEMMA SL | `sig(S) = 2^a σ'(S') mod n` | **exact identity** | **YES** |
| BB-3 | THEOREM SM(1) | the stratum meets at most `2L` of the `n` shells | upper bound on the *support size*, i.e. a **lower**-bound instrument for the max | **NO** — concentration is what makes the max LARGE; it is anti-monotone for the target |
| BB-4 | THEOREM SM(2) | structural per-shell count `= C(L,r'_a/2)/L` **exactly** | **exact (two-sided)** | **YES** — the one genuinely two-sided quantitative step in BB |
| BB-5 | LEMMA MULT | `#{(x,y)∈D²: x−y=eps} = 2^{L-2-U}` exactly | **exact** | **YES**, but only ever used inside BB-7 |
| BB-6 | LEMMA TC | fibre over `eps` has size `C(L−U,(r'_a−U)/2)` exactly | **exact** | **YES** — usable as a per-fibre cap |
| BB-7 | THEOREM AC | `P ≥ \|D\|²/Q − \|D\|` (Cauchy–Schwarz) | **strictly LOWER** | **NO** — C–S in this form has no reverse; an upper bound on `P` needs max-fibre control |
| BB-8 | pigeonhole | `max-shell ≥ N_acc/2L` | **strictly LOWER** | **NO** — `max ≤ mean` is false |
| BB-9 | (REALISE) | `L_1(k+w) ≥ X_w(γ)` for **every** `γ` (`c` free) | quantifier, direction-free | **YES**, but it *raises* the obligation: an upper bound must hold for every `γ`, not one |

**Registered prediction P1 (6 transport / 3 fail): HELD, exactly.** The three
that fail are BB-3, BB-7, BB-8 — and they are precisely the three steps that
carry **all** of BB's quantitative power. What survives is scaffolding: a
bijection (BB-1), an identity (BB-2), and exact fibre/shell counts (BB-4,
BB-5, BB-6). The scaffolding cannot manufacture a `1/Q` factor, because every
occurrence of `Q` in BB enters through BB-7.

**Consequence, stated plainly: BB's METHOD does not transport.** The
concentration mechanism is not merely unhelpful for the upper bound — it is
the source of the difficulty. Anything that concentrates the accidents into
few shells *raises* `Acc_deep`. What an upper bound needs is the opposite of
BB's engine: an **equidistribution / spreading** statement.

---

## §2. (D2) WHAT THE SURVIVING STEPS DO GIVE

The surviving steps do yield an upper bound. It is not a transport of BB's
mechanism; it is what is left when the mechanism is removed.

> **PROPOSITION U1 (trivial cap).** At `n = 2^41`, `w = 2^v`, deep stratum
> `a = v−1`, for **every** shell `gamma`,
> ```text
> Xdeep(gamma)  <=  C(2L, L−2) = C(n_a, r'_a).
> ```

**Proof.** By BB-1 the deep-stratum members of `W_w` biject with a subset of
`{S' ⊆ Z/n_a : |S'| = r'_a}`; drop the condition `p_1(S')=0` and the shell
constraint. ∎ (Equivalently: it is the banked LEMMA TC total identity
`sum_eps C(L−U,(r'_a−U)/2) = C(2L,r'_a)`, `crossing_low_w/PROOFS.md:175`,
read as an inequality.)

> **PROPOSITION U2 (shell cap).** With
> ```text
> M(N,m) := max_gamma #{S' ⊆ Z/N : |S'| = m, sigma'(S') ≡ gamma mod N},
> ```
> for **every** shell `gamma`,
> ```text
> Xdeep(gamma)  <=  M(2L, L−2)  =  ( C(2L,L−2) + C(L,(L−2)/2) ) / (2L),
> ```
> the maximum being attained at **odd** `gamma`.

**Proof.** By BB-2 the shell index of a deep-stratum member is
`sigma'(S') mod n_a`, `n_a = 2L`; drop only the condition `p_1(S')=0`.
For the closed form, extract the count by roots of unity: with `w = e^{2πi/N}`,
`Π_{j<N}(1 + y w^{tj}) = (1 − (−y)^d)^{N/d}` where `d = N/gcd(t,N)`, so the
`y^m` coefficient vanishes unless `d | m` and equals
`(−1)^{m+m/d} C(N/d, m/d)`. Hence
```text
#{|S'|=m, sum ≡ gamma} = (1/N) sum_{d | gcd(N,m)} (−1)^{m+m/d} C(N/d,m/d) c_d(gamma),
```
`c_d` the Ramanujan sum. At `N = 2L`, `m = L−2` (`L` a power of two, `L ≥ 4`)
`gcd(N,m) = 2`, `c_1 ≡ 1`, `c_2(gamma) = (−1)^gamma`, and
`(−1)^{m+m/2} = +1`, giving `(C(2L,L−2) ∓ C(L,(L−2)/2))/(2L)` for
`gamma` even / odd. The odd value is the larger. ∎

**Novelty, subtracted honestly.** The counting identity itself is banked and
already used in this lane — verbatim `gamma_shell/PROOFS.md:173-175`:

> `gcd(n/M, r'/M) = gcd(128, 63) = 1` at `v = 34`, for which the number of
> `m`-subsets of `Z/N` with prescribed sum mod `N` is EXACTLY `C(N,m)/N` (the
> Ramanathan/Lehmer count; only the `d = 1` term survives).

That is the **coprime** case applied to the **structural sub-family**
`(N,m) = (L, r'_a/2) = (128,63)`. U2 is the `gcd = 2` case (the `d = 2` term
survives) applied to the **unconditioned superset** `(N,m) = (2L, L−2)`.
The qualitative parity split is likewise banked, verbatim
`gamma_shell/PROOFS.md:162-164` THEOREM SM(3): *"An accident with `sigma'`
even lands in a structural shell; with `sigma'` odd it lands in one of the
`L` shells disjoint from the structural ones."* U2's "attained at odd
`gamma`" is the quantitative refinement of that. **Novelty label: LOW —
a one-line corollary of banked instruments.** Its value is not depth; it is
that it is the *first* upper bound of record on this quantity, and it is
below `B*`.

**Machine verification** (`transport.py mfun`, 30 checks): the closed form is
checked against an exact DP over all `C(2L,L−2)` subsets at
`L = 4, 8, 16, 32, 64`; the profile is constant on each parity class; the
maximum is at odd `gamma` in every case.

### 2.1 Toy verification against exhaustive truth

`transport.py census` computes, at the registered cells, the **full**
per-shell profile by meet-in-the-middle over all `C(2L,L−2)` subsets — no
lemma used — and subtracts the structural profile computed independently.
At `L = 4, 8` a plain brute force over all subsets is run as a second,
independent counter and agrees exactly.

| cell | `L` | `p` | `N_acc` | `Amax` | `Xmax` | `Occ` | U1 | U2 | U2 slack | `p` |
|---|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 17…97 | 0 | 0 | 1 | 0 | ok | ok | 4.00 | — |
| B | 8 | 17 | 416 | 30 | 30 | 16 | ok | ok | 16.80 | 17 |
| B | 8 | 97 | 80 | 8 | 9 | 16 | ok | ok | 56.00 | 97 |
| B | 8 | 113 | 16 | 2 | 7 | 8 | ok | ok | 72.00 | 113 |
| B | 8 | 193 | 16 | 2 | 9 | 8 | ok | ok | 56.00 | 193 |
| B | 8 | 241 | 0 | 0 | 7 | 0 | ok | ok | 72.00 | 241 |
| C | 16 | 97 | 4848608 | 151930 | 151930 | 32 | ok | ok | **96.97** | 97 |
| C | 16 | 193 | 2432064 | 76308 | 76411 | 32 | ok | ok | **192.81** | 193 |
| C | 16 | 257 | 1823616 | 57366 | 57366 | 32 | ok | ok | **256.82** | 257 |
| C | 16 | 353 | 1332800 | 41876 | 42139 | 32 | ok | ok | **349.62** | 353 |
| C | 16 | 449 | 1042272 | 32888 | 32969 | 32 | ok | ok | **446.87** | 449 |
| C | 16 | 577 | 808256 | 25620 | 25620 | 32 | ok | ok | **575.05** | 577 |
| C | 16 | 641 | 744128 | 23962 | 24677 | 32 | ok | ok | **597.02** | 641 |

U1 and U2 hold in every cell (P6.1, P6.2 held). **The measured U2 loss factor
`M/Xmax` tracks `Q = p` to within a few percent at CELL-C** — machine-checked
(`0.25p <= slack <= 4p`). This is the quantitative statement of what U2 throws
away: exactly the `1/Q` factor, i.e. the relation condition.

### 2.2 The candidate that the naive transport would give — and its status

> **(U3), registered as the naive transport of BB-4 + SM(4):**
> `Amax <= N_acc / L` (accidents spread over their parity class at least as
> evenly as the structural family spreads over its `L` shells).

**My registered prediction P6.3 said (U3) would be FALSIFIED. It was NOT.**
(U3) holds at all 17 cells; the worst observed `R3 = Amax·L/N_acc` is
**exactly 1.0000**, attained at CELL-B `p = 113` and `p = 193` (the
single-parity cells, `Amax = 2`, `N_acc = 16`, `L = 8`). Per registered
falsifier **F2 I therefore state: (U3) has no proof here, absence of a
counterexample at `L ≤ 16` is not a proof, and (U3) is labelled HEURISTIC
and is NOT used.**

Even if (U3) were proved it would buy nothing: it needs an upper bound on
`N_acc`, and the only one available is U1, giving
`Amax <= C(2L,L−2)/L = 2·M(2L,L−2)` — one bit **worse** than U2.

### 2.3 At the prize row (exact integers)

`transport.py prize`. Witness row `p = 3·2^41+1 = 6597069766657`, `e = 6`,
`q = p^6`, `B* = ⌊q/2^128⌋ = 242251802232021244567343686397347233808`
(`log2 B* = 127.5098`) — reproduced, not assumed.

```
  v    L     2L    r'_a   S(v)=struct/shell   C(2L,r'_a)   M(2L,r'_a)   U2 vs B*
  34   128   256   126    2^117.1491          2^251.6279   2^243.6279   above B*  (VACUOUS)
  35   64    128   62     2^54.6242           2^124.0820   2^117.0820   BELOW B*
  36   32    64    30     2^24.0755           2^60.4910    2^54.4910    BELOW B*
  37   16    32    14     2^9.4818            2^28.8125    2^23.8125    BELOW B*
  38   8     16    6      2^2.8074            2^12.9672    2^8.9773     BELOW B*
  39   4     8     2      2^0.0000            2^4.8074     2^2.0000     BELOW B*
```

At `v = 35`, exact integers:

```
C(128,62)  =    22510727468777163197263097882136686400   (2^124.0820)
M(128,62)  =   175865058349821587492501468423454912      (2^117.0820)
B*         =   242251802232021244567343686397347233808   (2^127.5098)
```

> **COROLLARY U2-ROW.** At the DSA witness row, for every shell `gamma`, the
> deep-stratum population at `w = 2^35` obeys `Xdeep(gamma) <= 2^117.0820`,
> a margin of **+10.4278 bits** below `B*`; and at every `v ∈ [35,39]` the
> same holds with margin growing to `+125.5` bits. At `v = 34` U2 is
> **VACUOUS** (`2^243.63 > B*`) — consistent with THEOREM BB, which proves the
> budget genuinely breaks there.

Dictionary checks passed: `S(34) = 2^117.1491`, `|W^struct| = 2^124.1491`,
`S(35..38) = 2^{54.624, 24.076, 9.482, 2.807}`, `log2 C(256,126) = 251.6279`,
`B*` — all banked values reproduced.

**P6.6 bracket, held:** `log2 M(128,62) − log2 p = 74.4970`, which sits
`+1.4360` bits **above** gamma_shell's banked PROVED max-shell lower bound
`73.061` at `w = 2^35`. The proved floor and the proved cap bracket the truth,
and the whole 42.6-bit width of U2's looseness is the missing `1/Q`.

### 2.4 The row region — and the one thing U2 has that BB does not

U2 contains **no `p` and no `delta_a`**. It is a pure counting bound, so it
applies at **every** admissible row, including the `e = 1` prime rows that
`gamma_shell/REPORT.md:91` records as *"untouched, and unreachable by this
method at any `v` in the bracket"*. Its price is a budget threshold:

```
  v    log2 M(2L,r'_a)   min log2 q needed   share of the live e=1 prime window
  34   243.6279          371.6279             0.00%
  35   117.0820          245.0820             8.64%
  36    54.4910          182.4910            58.15%
  37    23.8125          151.8125            82.42%
  38     8.9773          136.9773            94.15%
  39     2.0000          130.0000            99.67%
```

(live `e = 1` window `log2 p ∈ [129.5849625, 256)` from `B* ≥ 3`,
`crossing_gap/REPORT.md:118`.) P6.5 held: coverage is monotone in `v`, zero at
`v = 34`, and `8.64% < 10%` at `v = 35`.

---

## §3. (D3) THE nu(A) VARIANT — a SIGN mismatch, not merely a type mismatch

**Type mismatch, first.** `X_w(gamma)` is a deterministic count at one
adversarially chosen received word; `nu(A) = E[N(A)] − (q/2)C_t(A)` is a
first-moment functional over uniformly random received **pairs**. BB's
max-over-shells step (BB-8) is not a missing ingredient of the M route: the M
route already owns its own max-over-instances step, inside
`averaged_slope_conversion` (*"Since `Y(A)` is integer-valued, not every pair
can have `Y(A)<=B-1`; hence one pair has `Y(A)>=B`"*, `proof.md`). And the
counted objects differ exactly as in the round-21 countermodel: subsets of
`Z/n` indexing codeword supports versus post-paid `(k+t)`-supports carrying
MCA slopes.

**The decisive fact is a sign.** `E[N(A)] = |A|(1−q^{−t})q^{1−t}` depends on
`A` **only through `|A|`** — the first moment is structure-blind (verified
exactly, `transport.py nu`). Every structural property of `A` therefore
enters `nu(A)` only through `C_t(A)`, and `C_t(A)` enters with a **minus**
sign. Concentration produces collisions; collisions are exactly what
`C_t(A)` measures. So concentration **lowers** `nu(A)`.

> **THEOREM AT (anti-transport).** Write `N = Σ_z X_z`, `Y = #{z : X_z > 0}`,
> and let `RHS := N − (1/2)Σ_z X_z(X_z−1)` be the exact right-hand side of
> `averaged_slope_conversion` (so `nu(A) = E[RHS]`). Then
> ```text
> RHS  <=  (3/2)N  −  N²/(2Y).
> ```
> In particular if the contributions concentrate into `Y <= N/3` distinct
> slopes then `RHS <= 0`, hence `nu(A) <= 0 < B*`. Under uniform
> concentration by a factor `kappa = N/Y`, `RHS = N(3 − kappa)/2` exactly.

**Proof.** `Σ_z X_z² ≥ N²/Y` by Cauchy–Schwarz over the `Y` occupied slopes,
so `Σ_z X_z(X_z−1) = Σ_z X_z² − N ≥ N²/Y − N`, and
`RHS ≤ N − (N²/Y − N)/2 = (3/2)N − N²/(2Y)`. At `Y = N/3` this is `0`. The
uniform case is direct substitution. ∎

**Machine verification** (`transport.py nu`, exhaustive over **all**
occupancy vectors with `N ≤ 14`, 1203 checks, exact `Fraction` arithmetic):
the conversion inequality `RHS ≤ Y`, the Cauchy–Schwarz form, and
`Y ≤ N/3 ⇒ RHS ≤ 0` all hold with 0 failures; the largest concentration ratio
`N/Y` admitting `RHS > 0` in that range is `14/5 = 2.8 < 3`. The threshold
constant is exactly **3** (P7.3 / F5 held).

**The number that settles it.** BB's deep-stratum concentration factor is
`2^33` (256 shells out of `2^41`, `gamma_shell/PROOFS.md:151-157`).
`kappa = 2^33` gives `RHS = N(3 − 2^33)/2 < 0` for every `N ≥ 1`.
**Shell concentration does not bound `nu(A)` — in the only direction the
M route cares about, it destroys it.** The round-21 lead (*"BB's method …
is the same shape the node's `M` route needs"*,
`red_closability_probes/PROOFS.md:417-421`) is, on this reading, **backwards**:
the shapes are opposed, not aligned.

**What WOULD bound `nu(A)` below** (the constructive half of D3): a family `A`
with (i) large `|A|` — the only lever on `E[N(A)]`, which is `|A|`-linear;
and (ii) a **proved anti-concentration / spreading** certificate keeping
`C_t(A)` small, i.e. `Y ≈ N` — the family's supports must land on nearly
pairwise-distinct slopes. Plus the payload hypotheses the node names
(post-paid ownership, exact strict-overlap profile, ambient MCA slope field,
first-match ownership). Note that this is not a gap BB could ever fill: it
asks for the negation of BB's conclusion.

---

## §4. (D4) THE HONEST REMAINDER

**What is gained.** `Acc_deep` — the missing term of gamma_shell's re-pose —
now has an upper bound of record, `Acc_deep(v) ≤ M(2L, L−2)`, unconditional,
`p`-free, below `B*` for `v ≥ 35` on an explicit row region. That is one of
the three terms of `X_w(gamma) ≤ S(v) + Acc_deep + Acc_shallow`; `S(v)` was
already exact (BB-4).

**What is NOT gained, precisely.**

1. **`Acc_shallow` is untouched and unreachable by this argument.** U1/U2 use
   periodicity, and only the deepest stratum `a = v−1` is periodic. Strata
   `a < v−1` and aperiodic `S` have candidate sets of size `C(n_{a'}, r'_{a'})`
   with `n_{a'} = 2^{41−a'}` — astronomically above `B*`. So **this is not a
   safe-side certificate**, and by (REALISE) it does not bound `L_1(k+w)`.
2. **U2 is lossy by exactly the missing `1/Q` factor** — 42.6 bits at
   `v = 35` (`2^117.08` proved cap versus `≈2^74.5` heuristic truth, bracketed
   above the banked `2^73.061` proved floor). Recovering it means using the
   relation condition, and that reduces to:

> **THE NEXT DECISIVE TEST.** An upper bound on `Acc_deep` better than U2
> requires an **upper** bound on the weight enumerator of the relation set
> ```text
> R  =  { eps ∈ {0,±1}^L  :  Σ_{j<L} eps_j θ^j = 0 in F_Q },
> ```
> because `A_deep(gamma) ≤ Σ_{eps ∈ R\{0}} C(L−U(eps), (r'_a−U(eps))/2)`
> (BB-6, direction-free), and the fibre weight is decreasing in `U`. Measured
> exhaustively (`transport.py relations`): `#R ≈ 3^L/Q` to within 0.3% at
> `L = 16` (e.g. `p = 97`: `#R = 443777` vs `3^16/97 = 443780.6`), and the
> minimum support `U_min` is 3–4. The lattice-point count that would prove
> `#R ≲ 3^L/Q` is controlled by the **minimum `l1` weight** of a nonzero
> relation — which is exactly the instrument
> `critical/nodes/integer_code_distance_cert` / Z-1/Z-2, which round-21
> PROBE 1 found permanently stuck at `ell = 1`
> (`red_closability_probes/REPORT.md:17-18`).

So the crossing safe side and the round-21 red land on the **same** missing
instrument. That is the sharpest statement this pilot can make about the
remainder.

**A second, independent route already banked and not pursued here.** LEMMA
Y/MW (`notes/pilots_20260804/crossing_w2_opening/REPORT.md:118`) proves
`W_w ⊆ BCH_w` always, with **equality when `w ≤ p`**, and records that at
every official rate-half razor row `p ≥ 2^39+1 > w`. So `X_w(gamma)` *is* a
constant-weight-with-prescribed-`sig` count in a cyclic code of designed
distance `w`. An upper bound on constant-weight counts in that code would
bound **all** strata at once, `Acc_shallow` included — the thing U1/U2 cannot
do. That lane's own anchor list already files this as A5 (*"THE HEART"*,
OPEN, external) and A6 (character sums). Nothing here closes it; naming it is
the honest handoff.

**The crux, restated with what was gained.**

> Old: *"an ACCIDENT UPPER BOUND on shell populations"* — nothing supplies one.
> New: the **deep-stratum** term is supplied unconditionally and `p`-freely by
> U2, below `B*` for `v ≥ 35`. The crux is now **`Acc_shallow` plus aperiodic
> `S`**, i.e. an upper bound on the constant-weight population of `BCH_w` in a
> prescribed `sig` class — and, if one wants the deep-stratum term sharp
> rather than merely sufficient, an upper bound on the ternary relation
> weight enumerator, gated by the same minimum-distance instrument that
> round-21 PROBE 1 found stuck.

---

## §5. Catches

- **CATCH-T1 (against banked prose).** `gamma_shell/REPORT.md:24` reads
  *"at `(64,8)` accidents land on the structural shells at `p=193` and on 8
  disjoint new shells at `p=577`"*, phrased in `PROOFS.md:196-199` as *"the 8
  accidents land on the 8 STRUCTURAL shells"*. The **8** is a count of
  accident-occupied **shells**, not of accidents: the artifact
  `gamma_shell/toy_shell.out` prints `shells: total=8 struct=8 acc=8`, and my
  exhaustive census (two independent counters) finds **16** accidents on those
  8 shells at `p=193`, and 16 on 8 disjoint odd shells at `p=577`. I
  re-verified every column of that banked table exactly (`transport.py dict`,
  including `acc=0` at `p ∈ {257,449,641}` and at all five `(32,8)` cells).
  **The banked artifact is right; the REPORT/PROOFS prose is ambiguous and
  reads as an accident count.** No banked verdict is affected — the shell
  counts are what the theorem uses. *(Self-correction: my first `dict` stage
  asserted the prose reading and FAILED 2/2; the failure was mine, and the
  investigation is what located the ambiguity.)*
- **CATCH-T2 (a 0.067-bit collision that will mislead a reader).**
  `S(34) = C(128,63)/128 = 2^117.1491` (banked, `v = 34`, structural) and
  `M(128,62) = 2^117.0820` (new, `v = 35`, unconditioned cap) differ by
  `0.0671` bits; likewise `C(128,63) = 2^124.1491` versus
  `C(128,62) = 2^124.0820`. Exact relation `C(128,63)/C(128,62) = 66/63`.
  They are **different objects at different `v`**. A search subagent I
  dispatched inferred from this collision that my draft had an off-by-one in
  `(L−2)/2`; it does not — at `v = 35`, `L = 64`, so the second Ramanujan
  term is `C(64,31)`, while at `v = 34`, `L = 128`, it is `C(128,63)`, which
  is the banked `|W^struct|`. Machine-checked that all four integers are
  distinct.
- **CATCH-T3 (my own defect, found by my own gate).** My first `E[N(A)]`
  check wrote `q**(1-t)`, which is a **float** in Python for `t > 1`; the
  exact-`Fraction` comparison failed 3/3. Repaired to `Fraction(1, q**(t-1))`.
  Reported, not buried.

## §6. Self-checks and negative controls

- **Fail-closed, proven not asserted.** `transport.py failclosed` injects a
  false check and exits **1** (`failclosed.out`); the six substantive stages
  exit **0**. Totals: **1550 checks, 0 failures**.
- **Two independent counters.** The per-shell profiles are computed by
  meet-in-the-middle and, at `L ≤ 8`, also by plain brute force over all
  `C(2L,L−2)` subsets; they agree exactly.
- **A third, structurally independent counter.** `transport.py relations`
  recomputes `N_acc` as `Σ_{eps ∈ R\{0}} C(L−U,(r'_a−U)/2)` (LEMMA TC) from an
  independent ternary meet-in-the-middle, and it equals the census `N_acc` at
  **all 17 cells**. The banked total identity
  `Σ_eps C(L−U,(r'_a−U)/2) = C(2L,r'_a)` is verified at every cell.
- **BB-4 re-verified independently:** the structural profile is exactly
  equidistributed over the even shells, and `L | C(L,(L−2)/2)`, at every cell
  and at every `v ∈ [34,39]`.
- **No floats at any comparison.** `U1 < B*` and `U2 < B*` compare Python
  integers; the `nu` stage uses exact `Fraction`s. Floats appear only in
  `log2` display strings.
- **`theta` of exact order `2L`** is verified by checking `θ^{2L}=1` and
  `θ^{2L/q} ≠ 1` for every prime `q | 2L`; primality by deterministic
  Miller–Rabin.
- **Scope:** toy scale is `2L ≤ 32`, `L ≤ 16` — the same scale as
  gamma_shell. Every prize-row number is exact integer arithmetic from
  propositions proved for all `L`, not an extrapolation.

## §7. What is NOT proved here

1. **`Acc_shallow` and aperiodic `S`** — untouched, and unreachable by U1/U2.
2. **No safe-side certificate.** U2 bounds one of three terms; it does not
   bound `X_w(gamma)` and therefore does not bound `L_1(k+w)`.
3. **(U3) is unproved** and labelled heuristic despite holding at all 17 cells.
4. **U2 is 42.6 bits lossy** at `v = 35`; the sharp bound needs a relation
   weight-enumerator upper bound.
5. **No status flip is claimed for any node.**
