# THE 8.60 R-LOCALITY DEFICIT — derivations (round 22, f2_rlocality)

Pilot derivations for `notes/pilots_20260807/f2_rlocality/PREREG.md`.
Machine backing: `verify_d1.py`, `verify_d2.py`, `verify_d3.py`
(+ `rl_lib.py`, `lp_lib.py`), logs `VERIFY_D1.txt`, `VERIFY_D2.txt`,
`VERIFY_D3.txt`.

DRAFT ONLY. Nothing here is minted. Nothing outside this directory was
touched. No status flip is claimed; verdicts + artifacts only.

---

## §0. The state, quoted verbatim

The node of record, `background/nodes/f2_z1_mass_knife_edge/statement.md:76-88`:

```
76	c* = 1/ln 2 - 1 = 0.4427, where the
77	flat model saturates with ZERO margin — no per-coordinate-loss
78	argument can survive there. Proved: U_c = {0} for
79	c > 1 - 2^{-124.19} (an endpoint, honestly, not bulk progress).
80	Both standard supplies killed with computed thresholds (Z-2
81	moments: p <= 8.30 = Corollary 8; interpolation: no p at all,
82	position entropy H(1/L) > 1/L); the common cause: every supplied
83	input is R-LOCAL, short by the factor log2 p / log2(e log2 p) =
84	8.60; the Fourier escape is circular. The measured genuine tail
85	obeys the criterion at every reachable row with the binding layer
86	measured at 0.45 (= c* to grid resolution). Remaining leads: a
87	non-R-local instrument (nothing named), and the constant-weight
88	Z-FLOOR cell (crossing-side).
```

The derivation it came from, `notes/pilots_20260806/tail_count/PROOFS.md:437-448`:

```
437	> **THE STRUCTURAL DEFICIT, stated exactly.** All three inputs are
438	> `R`-local: each certifies only statements about `R` coordinates at a
439	> time. A tail bound at level `2^{-cS}` derived from `k`-local information
440	> costs at least `~k` bits of exponent per certificate and `k <= R = S/L`,
441	> so the best exponent any `R`-local argument can reach is `O(R log(...)) =
442	> O(S log2(e L)/L) = 0.116 S` at `L = 64`, against the required `c* S =
443	> 0.443 S`. **The gap is the factor `L / log2(e L) = 8.60`, and `L/log2 L`
444	> is exactly the shape that makes COROLLARY 8's threshold `log2 p =
445	> O(log log p)`.** This is why route (b)'s two supplies and this pilot's
446	> third all land on the same wall: they are not three arguments, they are
447	> three readings of `R`-wise independence, and `R`-wise independence is
448	> `log2 p` times too weak — by exactly the saturation constant.
```

COROLLARY 8's inequality, `notes/pilots_20260806/tern_route_b/PROOFS.md:405-411`:

```
405	Theorem 7 reaches `2^{o(S)}` iff the bracket at `k = R` beats `S/R`,
406	i.e. (taking the most generous `eta -> 1`, and using `|H| = 2S`,
407	`R = S / log2 p`) iff
408	```
409	    log2( e log2 p )  >=  log2 p .
410	```
411	Solving (S10, bisection): **`log2 p <= 3.0529`, i.e. `p <= 8.30`.**
```

The instrument itself, `tern_route_b/PROOFS.md:254-256` (LEMMA 5) and
`tail_count/PROOFS.md:363-374` (THEOREM 11):

```
254	> **LEMMA 5.** `P(u) <= ( 1 + V_1(u)/|H| )^S`. Consequently, if
255	> `|V_1(u)| <= eta |H|` for every `u != 0`, then
256	> `Z_1 <= 2^{S log2(1+eta)} + 2^{S - R log2 p}`.
```

```
371	    (1/L) log2( e eta_c^2 L )  >=  c        (branch k = R),   or
372	    log2(e) eta_c^2            >=  c        (branch k = eta_c^2 S).
```

The row (`tern_route_b/PROOFS.md:58-61`): `p = 18446735827372343297`,
`e_p = 39`, `S = 2^38`, `R = 4294967340`, `log2 p = 63.999999355`,
`R/S = 1/log2 p` (saturation, `statement.md:15`).

Notation as in PREREG §A. Throughout `L := log2 p`, `eta_c := 2^c - 1`.

---

## §1. (D1) WHERE THE 8.60 LIVES — it is a `c = 1` constant

### THEOREM RL-1 (identification).

```
    8.599036  =  L / log2(e L)  =  1 / I_INSTR(1)  =  DEF_INSTR(1) ,
```

where `I_INSTR(c)` is the exponent per `S` certified by the one executable
`R`-local instrument (LEMMA 5 AM-GM `->` `V_1` `->` THEOREM Z-2 moment
`N_k <= (2k-1)!!|H|^k` `->` Chebyshev, `k <= R`), i.e. THEOREM 11's bracket.
Equivalently, `8.60` is **the multiplicative failure margin of COROLLARY 8's
inequality** `log2(e log2 p) >= log2 p`: the left side is `7.442695`, the
right side `63.999999`, and `63.999999/7.442695 = 8.599036`.

*Proof.* `I_INSTR(1) = (1/L) log2(e eta_1^2 L)` with `eta_1 = 2^1 - 1 = 1`,
so `I_INSTR(1) = log2(eL)/L`; the required exponent at `c = 1` is `c = 1`.
[] (`verify_d1.py` D1.1a/b/e; `log2(eL) = log2 L + log2 e = 6 + 1.442695`.)

### THE THREE NUMBERS (the node carries one; there are three).

| quantity | value | what it is |
|---|---|---|
| `DEF_INSTR(1) = 1/I_INSTR(1)` | **8.5990** | the instrument's deficit at `c = 1` — the node's `8.60` |
| `c*/I_INSTR(1)` | **3.8068** | the ratio the node's own sentence computes (`0.443/0.116`) |
| `DEF_INSTR(c*) = c*/I_INSTR(c*)` | **6.3130** | the deficit **at the binding layer** |

`I_INSTR(1) = 0.116292` — this is the node's "`0.116 S`". At the binding
layer the same instrument certifies `I_INSTR(c*) = 0.070124`, not `0.116`,
because `eta_{c*} = 2^{c*} - 1 = 0.359141 < 1`.

> ### CATCH-RL1 (against `statement.md:82-84` and `tail_count/PROOFS.md:441-443`) — a LAYER ERROR, flagged for the coordinator, NOT edited.
>
> The constant `log2 p / log2(e log2 p) = 8.60` is **arithmetically correct**
> and **structurally meaningful** — but it is the deficit **at `c = 1`**, and
> the node attaches it to the binding layer `c*` (`statement.md:76-84` names
> `c*` and then names `8.60` as the deficit of the supplies). Three separate
> errors ride on this:
>
> 1. **The layer is wrong.** `DEF_INSTR(c*) = 6.3130`, not `8.5990`. The
>    correct constant of record at the binding layer is **6.31**.
> 2. **The quoted sentence is internally inconsistent.** `tail_count`
>    `PROOFS.md:441-443` states the achieved exponent as `0.116 S` and the
>    required one as `0.443 S`, then names the gap as `8.60`; but
>    `0.443/0.116 = 3.81`. The `0.116` is `I_INSTR(1)`, the `0.443` is the
>    requirement at `c*`: two different layers, divided.
> 3. **At `c = 1` there is in fact NO deficit at all.** `c = 1` is the layer
>    the same pilot PROVES outright (tail_count THEOREM 12: `U_c = {0}`), by
>    a purely `R`-local argument (interpolation on the MDS value code).
>    §4 below shows the sharp `R`-local optimum at `c = 1` is *exactly*
>    `p^{-R}`, so `FLOOR_R(1) <= 1`: **`R`-locality costs nothing at the one
>    layer where `8.60` was computed.** The `8.60` measures the weakness of
>    *Chebyshev-on-`V_1`* at the endpoint, not the weakness of `R`-locality.
>
> The same paragraph also says "`R`-wise independence is `log2 p` times too
> weak" (`:448`) — a **fourth** number, `L = 64`. It is not equal to `8.60`
> either.

### THEOREM RL-2 (the four-factor decomposition).

For every layer `c` in the `k = R` branch,

```
    DEF_INSTR(c)  =  THETA(c) * AMGM(c) * GAUSS(c) * CAP(c) ,
```

with (all four named in PREREG §A, all four measured in `verify_d1.py` D1.2)

```
    THETA(c) = c / I_FLAT(c)                    LAYER   : requirement vs truth
    AMGM(c)  = I_FLAT(c) / J_FLAT(eta_c)        LEMMA 5 : the AM-GM linearization
    GAUSS(c) = J_FLAT(eta_c)/(log2(e) eta_c^2)  MOMENT  : the (2k-1)!! shape
    CAP(c)   = log2(e) eta_c^2 L/log2(e eta_c^2 L)   LOCALITY: the cap k <= R
```

The identity is a telescoping product — that is not the content. The content
is that **each factor is the loss of one separately identifiable inequality
in the chain**, and the numbers say which inequality is actually expensive:

```
  c = 1  (where 8.60 lives) :  0.015625 x  1.000000 x 44.361419 x 12.405786 = 8.5990
  c = c* (the binding layer):  1.000000 x  2.299041 x  1.034793 x  2.653612 = 6.3130
```

Readings:

- **`THETA(c*) = 1.000000` exactly** — COROLLARY ZM's zero margin, measured
  from a fresh code path (`I_FLAT(c*) = 0.4426950409 = c*`).
- **`AMGM(1) = 1.000000` exactly.** At `c = 1` the tail event
  `{cost = 0}` and the relaxed event `{V_1 = |H|}` are the SAME event
  (`all c_s = 0`), so AM-GM is lossless there. AM-GM's loss is a
  bulk-layer phenomenon: `2.299` at `c*`, and it blows up as `c -> 0`
  (`13.07` at `c = 0.15`).
- **At `c = 1` the dominant loss is `GAUSS = 44.36`, not locality.** The
  sub-Gaussian moment shape certifies exponent `log2 e = 1.4427` where the
  truth is `L = 64`. The `8.60` is then this `44.36`, divided down by
  `CAP = 12.41` upward and by the criterion's own `c=1` slack `1/64`. So
  **`8.60` is mostly a statement about Chebyshev at an endpoint**.
- **At `c*` the lossiest single step is the LOCALITY CAP, `2.654`**, with
  AM-GM second at `2.299` and the moment shape almost free at `1.035`.

### THEOREM RL-3 (the deficit is not monotone; its minimum).

`min_c DEF_INSTR(c) = 5.9692` at `c = 0.298`; `DEF_INSTR(c*) = 6.3130`;
`DEF_INSTR(1) = 8.5990`. The instrument is *worst* exactly where the
criterion has *most* slack, and the campaign's binding layer sits near the
instrument's best region — a favourable coincidence worth recording.

---

## §2. (D2) THE SHARPENING ATTEMPTS

All five attempts were registered with a prediction before running
(PREREG §C). Licensing controls first: my own from-scratch construction of
the row, the character form and the cost form reproduce the banked
`Z_1 = 1.250000` (G1) and `9.387207` (G4) of `tern_route_b/PROOFS.md:124-127`,
and the two forms agree to `2.7e-13`.

### A4 — HIGHER MOMENTS `k > R`: the cap is SHARP (verdict as registered).

`N_k = p^{-R} sum_u V_1(u)^{2k}` computed exactly at three rows:

```
 row          k      N_k     (2k-1)!!|H|^k   verdict
 G1 p=17 R=2  1       16              16     OK
 G1 p=17 R=2  2      720             768     OK      <- k = R
 G1 p=17 R=2  3    80800           61440     FAILS   <- k = R+1
 G4 p=97 R=2  2     2976            3072     OK      <- k = R
 G4 p=97 R=2  3   527360          491520     FAILS   <- k = R+1
 G2 p=113 R=1 2     1104             768     FAILS   <- k = R+1 (banked)
```

The banked G2 failure `1104 > 768` (`tern_route_b/PROOFS.md:399-401`) is
reproduced independently, and **the first failure is at exactly `k = R+1` on
all three rows**. THEOREM Z-2's hypothesis `||c||_1 <= 2R` is load-bearing
and cannot be pushed. A4 FAILS.

### A1 — DROP-AMGM (the type / binomial-moment bound): FAILS, badly.

For any law with `k`-wise uniform marginals and any target profile `nu`,
symmetrising over coordinate permutations and testing an `R`-subset against
the `nu`-typical set gives

```
    Pr[ empirical measure = nu ]  <=  (S)_k p^{-k} / prod_x (nu(x)S)_{k_x}
                                  =   2^{-k D(nu||mu) + o(k)} ,
```

`mu` uniform on `F_p`, `D` in bits, and the falling-factorial corrections
cancel to first order (`sum_x k_x^2/(2 n_x) = k^2/(2S)` on both sides).
Contracting Sanov to the mean of `d`, `min{D(nu||mu) : E_nu[d] <= 1-c}` is
exactly `I_FLAT(c)`, so

```
    I_TYPE(c)  =  (k/S) I_FLAT(c)  =  kmul * I_FLAT(c) / L .
```

At `c*`, `I_FLAT(c*) = c*` (zero margin), so `I_TYPE(c*) = kmul * c*/L` and
the deficit is **exactly `L/kmul`: 64.000 at `k = R`, 32.000 at `k = 2R`**.
Registered prediction (0.0069 / 0.0138) confirmed. A1 FAILS — it is ten
times worse than the banked instrument.

**Why:** the type bound throws away the lower-order marginals. `k`-wise
uniformity gives all `j`-wise marginals for `j <= k`, and the moment/LP
machinery uses them; the single top-order certificate does not.

### A2 — the centred `k`-th moment on the cost sum: FAILS (deficit 8.995).

`Y = sum_s X_s`, `X_s = 1 - d(c_s)`. For even `k <= R`, `E[(Y-EY)^k]` is a
degree-`k` polynomial in the coordinates, hence *exactly* determined by the
`R`-wise marginals; bound it through the centred CGF and apply Markov:

```
    Pr[Y - EY >= t] <= E[(Y-EY)^k]/t^k ,
    E[(Y-EY)^k] <= k! (theta ln2)^{-k} ( 2^{S Lam2(theta)} + 2^{S Lam2(-theta')} ),
    exponent per S = (k/S) log2( theta ln2 (t/S) e L / kmul ) - Lam2(+-theta) ,
```

with the EXACT centred CGF `Lam2(theta) = log2 C(2 theta, theta)` (the same
`C(2t,t)` as tail_count THEOREM 7, uncentred by `-theta E[X]`). Truncating
`X' = max(X, -M)` (legitimate: `X'` is a coordinate function, `Y' >= Y`)
removes the heavy lower tail of `d`. Measured at `c*`:

```
    untruncated, k = R  : exponent 0.043595
    truncated  , k = R  : exponent 0.049218   deficit 8.995   (best M = 2.0)
    truncated  , k = 2R : exponent 0.082704   deficit 5.353   [NOT LICENSED]
```

Registered prediction was deficit `8.6 +- 0.7`; measured `8.995` — **HIT**.
A2 FAILS: `8.995 > 6.313`.

> **Why `k = 2R` is not licensed, and what that tells us.** The `k = 2R` row
> would beat the banked instrument (`5.353 < 6.313`) — but the MDS value code
> is exactly `R`-wise independent (dual distance `R+1`) and NOT `2R`-wise.
> THEOREM Z-2 does supply moment information to `l1`-order `2R`, but only
> against `l1`-bounded integer relations. Expanding `d` in additive
> characters (`route_b/PROOFS.md:266-268`),
> `1 - d(c) = -1 + (1/ln2) sum_{j>=1} ((-1)^{j+1}/j) 2 cos(2 pi j c/p)`, a
> `k`-th moment of `Y` consumes relations of total `l1` weight up to `k*J`
> where `J` is the harmonic cutoff. `k*J <= 2R` with `k = 2R` forces
> `J = 1` — i.e. **the only harmonic you may keep is `j = 1`, which is
> `V_1`, which is LEMMA 5's route.** At the licensed locality radius the
> "new" moment instrument collapses onto the banked one. This is a
> structural reason, not a numerical one.

### A3 — NO-POSITION-ENTROPY: a repaired THEOREM 10 (a banked verdict corrected).

tail_count THEOREM 10 bounds `|U_c| <= C(S,R) m^R`, `m = |A(D)|`, and dies
because the position entropy `S H(R/S) = 0.1161 S` beats the value saving
`R log2(1/rho) = 0.0156 S` — "**negative everywhere, with no threshold in
`p`**" (`tail_count/PROOFS.md:346-348`), flagged DEAD FAMILY, and carried
into the node as "interpolation: no `p` at all, position entropy
`H(1/L) > 1/L`" (`statement.md:81-82`).

**That union bound is not the right `R`-local instrument.** With
`N_A := #{s : c_s(u) in A}`, `R`-wise uniformity gives EXACTLY

```
    E[ C(N_A, R) ]  =  C(S,R) rho^R ,        rho = |A|/p ,
```

(each `R`-subset lies in `A` with probability `rho^R`), and since `C(.,R)`
is non-decreasing,

```
    Pr[ N_A >= m ]  <=  C(S,R) rho^R / C(m,R) .
```

**The `C(S,R)` cancels against `C(m,R)`.** With `m = (1-delta)S` the residue
is `H(1/L) - (1-delta) H(1/((1-delta)L)) = O(delta/L)`, not `H(1/L)`.

Measured at `c*` (`verify_d2.py` D2.A3): the banked THEOREM 10 exponent is
`-0.094651` (negative: dead), the repaired one is `+0.001710` at
`delta = 0.2731` (positive: alive, with a threshold in `p` at every
`log2 p >= 3`).

> ### CATCH-RL2 (against `tail_count` THEOREM 10 and `statement.md:81-82`) — flagged, NOT edited.
> "The interpolation supply dies at EVERY `p`; the failure mechanism is the
> entropy of the position set" is **an artefact of a union bound over
> position sets, not a property of the supply.** The standard `R`-local
> instrument for the same event — the binomial moment `E[C(N_A,R)]` — pays
> no position entropy at all, and turns the exponent positive at every
> `log2 p >= 3.06`. The DEAD-FAMILY flag on THEOREM 10 should be re-read as
> "dead *as executed*", and the `H(1/L) > 1/L` diagnosis withdrawn.
>
> **This does not rescue the route.** The repaired exponent at `c*` is
> `0.00171` against a required `0.4427`: deficit `258.9`. A3 FAILS
> numerically by a wide margin, exactly as registered (`0.0017 +- 0.0005`).
> The correction matters for the *diagnosis* — the wall is locality, not
> position entropy — not for the ledger.

Threshold scan of the repaired bound (`S = 2^20`, `R = S/L`):

```
   log2 p =   2   exponent -0.005371   (dead)
   log2 p =   3   exponent +0.003224   deficit 137.3
   log2 p =   4   exponent +0.009579   deficit  46.2
   log2 p =   8   exponent +0.009728   deficit  45.5
   log2 p =  16   exponent +0.006012   deficit  73.6
   log2 p =  32   exponent +0.003284   deficit 134.8
   log2 p =  64   exponent +0.001710   deficit 258.9
   log2 p = 128   exponent +0.000872   deficit 507.7
```

### A5 — LONGER WINDOW: FAILS structurally (as registered).

`DEF_INSTR(c*)` as a function of the locality fraction `R/S = 1/Lx`:
`2.379` at `Lx = 4`, `2.380` at `8`, `2.847` at `16`, `4.061` at `32`,
`6.313` at `64`, `10.325` at `128`. The deficit *is* controlled by `R/S`
alone — but saturation pins `R/S = 1/log2 p` exactly (THEOREM Z-NOGO,
`statement.md:40-44`), so no admissible row offers a longer window. This is
Z-NOGO acting one level up: the same pin that kills distance+counting kills
the locality radius.

### A6 — BEST-OF at `c*`.

```
   banked instrument (AM-GM + Z-2 + Chebyshev, k<=R)   exponent 0.070124  deficit   6.313
   A2 truncated centred moment, k = R                  exponent 0.049218  deficit   8.995
   A1 type bound, k = R                                exponent 0.006917  deficit  64.000
   A3 repaired THEOREM 10                              exponent 0.001710  deficit 258.883
```

**No licensed attempt beats the banked instrument.** The best deficit at the
binding layer stays `6.3130`.

---

## §3. (D3) THE FORMALIZED CLASS

### DEFINITION (`k`-LOCAL).

> An upper bound `B` on `Pr_u[ cost(u) <= (1-c) S ]` is **`k`-LOCAL** iff
> `B` holds for EVERY random vector `X = (X_1,...,X_S)` on `F_p^S` whose
> every `k`-subset marginal is uniform on `F_p^k`.
>
> It quantifies over: the **locality radius** `k` (how many coordinates one
> certificate may see at once); the **moment order** (a derived quantity,
> `<= k`, since only polynomials of degree `<= k` in the coordinates are
> determined); the **window length** (it enters only through *which* `k`-wise
> marginals are uniform, and for the official object every one of them is).
>
> `OPT_k(c) := max Pr[cost <= (1-c)S]` over the class;
> `I_LOC_k(c) := -(1/S) log2 OPT_k(c)`;  `FLOOR_k(c) := c / I_LOC_k(c)`.
> **No `k`-LOCAL bound can certify an exponent above `I_LOC_k(c)`**, so no
> `k`-LOCAL argument can have deficit below `FLOOR_k(c)`.

**The object's actual supply is bracketed by `k = R` and `k = 2R`.** The MDS
value code `C*` is exactly `R`-wise independent (dual distance `R+1`,
tail_count THEOREM 5), so it is in `k = R`. THEOREM Z-2 adds moment matching
to `l1`-order `2R`, but only against `l1`-bounded integer relations, which is
strictly weaker than `2R`-wise uniformity. Hence
`FLOOR_{2R}(c) <= (the object's true floor) <= FLOOR_R(c)`.

### LEMMA RL-4 (symmetrisation).

`OPT_k(c)` is attained by a law that is both **exchangeable** (permuting
coordinates preserves `k`-wise uniformity and the event) and
**sign-symmetric** (multiplying coordinates by independent uniform signs
preserves `k`-wise uniformity, and `d(c) = d(-c)`). Such a law is exactly a
law on the folded count vector `n = (n_0,...,n_{(p-1)/2})`, `sum n = S`, and

```
    Pr[ (X_1..X_k) has folded type (k_x) ]  =  E[ prod_x (n_x)_{k_x} ] / (S)_k ,
```

so the class is cut out by finitely many LINEAR equations
`E[prod_x (n_x)_{k_x}] = (S)_k prod_x w_x^{k_x}` (`w_0 = 1/p`, `w_j = 2/p`).
**`OPT_k(c)` is therefore an exactly solvable linear program.**

### LEMMA RL-5 (LIFTING: a `k`-local floor from a two-bin pattern LP).

Let `A subset F_p` with `max_{x in A} d(x) <= 1-c`, `rho = |A|/p`, and
suppose `|A|` and `p - |A|` each admit a `k`-wise uniform code of length `S`
(true whenever they are prime powers `>= S`; at the official row
`|A| ~ 0.38 p` and `S = 2^38`, so this is free). Let `sigma in {A,B}^S` be
any exchangeable `k`-wise independent Bernoulli(`rho`) pattern; conditionally
on `sigma`, draw the `A`-positions from a `k`-wise uniform code on `A` and
the `B`-positions from one on `B`, independently. Then

1. every `k`-subset marginal of `X` is `(rho U_A + (1-rho) U_B)^{otimes k}
   = mu^{otimes k}` — uniform on `F_p^k`; and
2. `Pr[ cost(X) <= (1-c)S ] >= Pr[ sigma = A^S ]`.

Hence `OPT_k(c) >= OPTPAT_k(rho, S) := max{ Pr[N = S] : E[(N)_j/(S)_j]
= rho^j, j = 0..k }`, a **two-bin LP with `S+1` variables and `k+1`
constraints**. (An exchangeable `{0,1}^S` law is `k`-wise independent
Bernoulli(`rho`) iff its `N`-law satisfies exactly those `k+1` equations, so
the LP *is* the class of patterns and its optimum is attained by the explicit
law "draw `N ~ q*`, then a uniformly random `N`-subset".)

### PROPOSITION RL-6 (the asymptotics of the pattern LP).

The dual of `OPTPAT` is `min{ E_{Bin(S,rho)}[P(N)] : deg P <= k, P >= 0 on
{0..S}, P(S) = 1 }`. Taking `P = Q^2` with `Q` monic of degree `k/2` in the
standardised variable `Z = (N - S rho)/sqrt(S rho(1-rho))` and minimising
`E[Q(Z)^2]` (the Hermite/Gauss-quadrature extremum, value `(k/2)!`) gives

```
    OPTPAT_k(rho,S)  ~  (k/2)! ( rho / (S(1-rho)) )^{k/2}
                     ~  ( k rho / (2 e S (1-rho)) )^{k/2} ,
```

i.e. exponent per `S` equal to `(kmul/(2L)) log2( 2 e L (1-rho)/(kmul rho) )`
for `k = kmul * R`, `R/S = 1/L`. With `rho = rho(1-c) = (2/pi)
arccos(2^{-(1-c)/2})` this is the ASYMPTOTIC floor quoted in §4.

**DIRECTIONS, stated exactly (this matters).** The rigorous chain is

```
    FLOOR_k(c)  >=  FLOOR^pat_k(c) := c / ( -(1/S) log2 OPTPAT_k(rho(1-c), S) )
```

by LEMMA RL-5 — *only the exact pattern-LP value is a valid lower bound on
the class floor.* The Hermite construction is a DUAL-feasible polynomial, so
it gives `OPTPAT <= (k/2)!(rho/(S(1-rho)))^{k/2}`, i.e. it approximates
`FLOOR^pat` **from above**. Hence:

- the closed form of PROPOSITION RL-6 is an APPROXIMATION to the lifted
  floor, not a proved lower bound on it;
- `verify_d3.py` D3.3 solves the pattern LP EXACTLY at moderate `S` and
  measures the relative deviation of the closed form from the exact optimum;
- the official-row numbers quoted in §4 are therefore labelled **ASYMPTOTIC
  EVIDENCE**, not a theorem uniform in the row. The only EXACT floor in this
  pilot is the full LP at G1 (`p = 17, S = 8`), which is a genuine
  toy-scale floor and is labelled as such.

---

## §4. (D3) WHAT THE CLASS CAN AND CANNOT DO — results

### 4.1 The EXACT full LP at G1 (`p = 17, S = 8, R = 2`) — a genuine floor.

12870 states, 46 rows at `k = R = 2`. Solved exactly (to float precision) by
a from-scratch two-phase simplex (`lp_lib.py`; smoke-tested against a
textbook optimum and against the closed form `OPTPAT_1 = rho`).

```
   c        OPT_{k=R}   TRUE(GRS)   FLOOR_R   DEF_INSTR(L=4.09)
   0.2000  3.2180e-01  3.4602e-03    0.9781      6.2696
   0.3000  2.7303e-01  3.4602e-03    1.2815      3.8921
   0.4427  2.1332e-01  3.4602e-03    1.5889      2.3790   <- c*
   0.6000  1.5354e-01  3.4602e-03    1.7756      1.5689
   0.8000  8.4921e-02  3.4602e-03    1.7989      1.2532
   1.0000  3.4602e-03  3.4602e-03    0.9786      1.1766   <- = p^{-R} EXACTLY
```

> ### THE HEADLINE (P9, confirmed): `R`-LOCALITY COSTS NOTHING AT `c = 1`.
> `OPT_R(1) = 3.4602076125e-03 = 17^{-2} = p^{-R}` **exactly**, so
> `I_LOC_R(1) = R L/S = 1.0219` against a requirement of `1`, i.e.
> `FLOOR_R(1) = 0.9786 <= 1`. **There is no `R`-locality deficit at all at
> `c = 1`** — and `c = 1` is precisely the layer at which the constant `8.60`
> is computed (THEOREM RL-1), and precisely the layer that tail_count
> THEOREM 12 proves outright by a purely `R`-local (interpolation) argument.
> This is the sharpest possible refutation of "`8.60` is the structural cost
> of `R`-locality": at the layer where it is computed, the structural cost of
> `R`-locality is `1`.

At the binding layer the exact floor at G1 is `FLOOR_R(c*) = 1.5889`
(registered band `[1.2, 4.0]` — HIT), against the instrument's `2.3790` at
that row: at G1 the banked instrument is `1.50x` above the exact floor.
`OPT_R(c) >= ` the true GRS tail at every layer (the object is a member of
the class) — a sanity control that passes.

**Monotonicity in the radius, exact at G1** (`verify_d3b.py`):

```
    k = R  = 2 :  OPT(c*) = 2.133154e-01   FLOOR_2(c*) = 1.5889   [0.7 s]
                  OPT(1)  = 3.460208e-03 = 17^{-2}   FLOOR_2(1) = 0.9786
    k      = 3 :  OPT(c*) = 1.526830e-01   FLOOR_3(c*) = 1.3062   [100.2 s]
                  OPT(1)  = 2.035416e-04 = 17^{-3}   FLOOR_3(1) = 0.6524
    k = 2R = 4 :  496 rows x 12870 columns -- DID NOT FINISH inside the
                  ramguard `local` wall limit with my from-scratch simplex.
                  Reported as NOT COMPUTED, not estimated.
```

The floor falls with the radius, as it must, and it falls slowly: widening
from `R` to `3R/2` buys only `1.22x` at G1.

**And the `c = 1` optimum is `p^{-k}` for EVERY radius, exactly** (measured
`17^{-2}` and `17^{-3}`; the matching upper bound is one line — on the event
`{N_0 = S}` one has `C(N_0,k) = C(S,k)` while `E[C(N_0,k)] = C(S,k) p^{-k}`
by `k`-wise uniformity, and the bound is attained by an `[S,k]_p` RS code).
So `I_LOC_k(1) = k L / S`, which at `k = R` is exactly `R L/S = 1 + Delta/S`:
**the `c = 1` requirement is met on the nose by pure `R`-locality**, with the
knife-edge constant `Delta` as the entire margin. That is CATCH-RL1(3) in its
cleanest form.

Second exact row `p = 41, S = 4, R = 1`: `FLOOR_R(c*) = 2.7651`. Two rows is
not a law: both have `R/S = 0.25` far from the official `1/L`, and `S <= 8`.
**P13 (the `L`-dependence of `FLOOR_k`) is UNRESOLVED and reported as such** —
the exact full LP has `C(S + (p-1)/2, (p-1)/2)` states and is infeasible
beyond `p ~ 41`.

### 4.2 The lifted floor at the official row (ASYMPTOTIC EVIDENCE).

`rho(1-c*) = 0.383070`. The exact pattern LP (LEMMA RL-5) at moderate `S`,
compared with the closed form of PROPOSITION RL-6:

```
   S     k    L        OPTPAT       exact exp/S   closed form   FLOOR
   32    4    16.0     7.1101e-04     0.326807     0.383137     1.3546
   64    4    32.0     1.8319e-04     0.193974     0.222819     2.2822
   128   4    64.0     4.6366e-05     0.112473     0.127034     3.9360
   256   4   128.0     1.1702e-05     0.063996     0.071330     6.9176
   64    8    16.0     2.1090e-07     0.346514     0.383137     1.2776
```

(rows with `OPTPAT < 1e-7` are DISCARDED — my float simplex is not
trustworthy there, and the discarded points visibly break monotonicity,
which is how they were caught.)

Two convergence readings, both in the right direction:

- at **fixed `k = 4`**, the closed form's excess over the exact exponent
  falls monotonically `+17.2%, +14.9%, +12.9%, +11.5%` as `S = 32..256`;
- at **fixed locality ratio `k/S = 1/8`** (the quantity that is pinned at
  the official row), the exact exponent rises with `S`
  (`0.326807 -> 0.346514`) toward the closed form `0.383137`.

So the closed form is the `S -> infinity` limit, approached from below in the
exponent and hence from above in the floor. At `S = 2^38` the limit is the
relevant value:

```
   FLOOR_R (lifted, k = R)    =  6.2063
   DEF_INSTR(c*)              =  6.3130      (+1.7%)
   FLOOR_2R (lifted, k = 2R)  =  3.4848      (headroom factor 1.81)
```

### 4.3 The verdict on (D3).

**(a) Is the `8.60` an artefact?** Partly. `8.60` is exact arithmetic for a
`c = 1` quantity; at the binding layer the same instrument's deficit is
`6.3130`, and `R`-locality's own cost at `c = 1` is `1`. So the number `8.60`
is not the binding-layer deficit and is not a floor for the class.

**(b) Is there a floor?** Yes, and it is close to what is achieved.

- **Toy-scale, EXACT:** at G1 no `k=R`-local estimate beats `X = 1.5889` at
  the binding layer (and none beats `0.9786`, i.e. nothing, at `c = 1`).
  This is EVIDENCE, not a theorem uniform in the row.
- **Official-row, ASYMPTOTIC (LEMMA RL-5 + PROPOSITION RL-6, validated
  numerically):** no `k=R`-local estimate beats `X = 6.21`, and no
  `k=2R`-local estimate beats `X = 3.48`, at the binding layer.

**The banked instrument is therefore essentially optimal for what `R`-wise
independence alone allows (+1.7% off the `k = R` floor).** THEOREM Z-2 places
the object's actual supply strictly between `R`-wise and `2R`-wise
uniformity, so the honest statement of the remaining headroom is: **a factor
of at most `1.81`, and only if Z-2's `2R`-order information can be turned
into a genuine `2R`-wise tail bound** — which §2 (A2) shows collapses back
onto `V_1` when the harmonic budget is respected.

**Either way the deficit is structural: the floor is `>= 3.48` at the binding
layer, and `3.48 > 1`.** No `k`-local argument with `k = O(R)` can close the
terminal. What is wrong in the bank is the *number* (and the layer it is
attached to), not the *conclusion*.

---

## §5. (D4) THE WEAKEST NON-LOCAL INPUT

Collecting §§1-4: the deficit at the binding layer is a factor `6.31`
achieved against a floor of order `6.2` (`k = R`) / `3.5` (`k = 2R`). It is
therefore **structural for the class, and the class is the whole of what the
object supplies.** What is needed is an input that is not `k`-local for any
`k = O(R)`.

**THE REQUIRED STATEMENT (the weakest one that closes the gap).** For a
single interval `A subset F_p` with `rho = |A|/p = rho(1-c*) = 0.3826` and
some `delta > 0`,

```
    #{ u in F_p^R : #{ s < S : f_u(zeta^s) in A } >= (1-delta) S }
                                              <=  p^R * 2^{-c* S + o(S)} .
```

Equivalently: **no codeword of the GRS value code `C*` is unusually smooth** —
the Construction-A lattice `L(C*)` has no more points in the box `A^S` than
the volume heuristic gives (tail_count THEOREM 9's structure theorem read as
an obligation). Three features make it non-local:

1. it quantifies over `Theta(S)` coordinates at once, so no `k = O(R)`
   certificate can supply it (§3);
2. it is a statement about *individual* `u`, not about moments over `u` —
   which is exactly the shape Weil would have given
   (`tern_route_b/PROOFS.md:301-317`, vacuous by `26.000` bits);
3. it is `2^{o(S)}`-tight, so it cannot be obtained by any argument that
   loses a constant per coordinate.

**What in the bank could supply it.** Nothing does, and I name the two nearest
candidates honestly:

- **The constant-weight Z-FLOOR cell (crossing side)**, already named as a
  remaining lead at `statement.md:87-88`. THEOREM Z-FLOOR is a *pointwise
  lower* bound on `Z(L)` for every subspace, proved by one Cauchy-Schwarz on
  the banked collision identity. Its crossing-side sibling — an upper bound
  on the mass carried by constant-weight strata — is the only banked object
  that quantifies over all `S` coordinates simultaneously.
- **An ensemble average over the five generating classes**
  (`f2_o1_status_split` Addendum 3). This changes the quantifier from "for
  the row" to "on average over the class", which is strictly weaker than
  what the consumer's SUM reading needs (`f2_o1_status_split:61-68`), so it
  would have to come with a concentration statement — and concentration over
  a five-element family is not available.

**And a sharpening of the target that makes the gap worse, not better.**
`f2_repose` R2(v) records the finite target `Z(L) <= 1 + N^3`, i.e.
`Z_1 in [2^{17.98}, 2^{22.75}]` — **a 4.77-bit window**. Under that reading
the `o(S)` in the tail criterion is not `o(S)` at all but `<= 22.75` bits
absolute, against `S = 2.75e11`. Every constant in this note is a
multiplicative deficit on an exponent of size `Theta(S)`; a 4.77-bit window
leaves no room for any of them. **The non-local input has to be essentially
exact, not merely `2^{o(S)}`.**

---

## §6. Summary table

| # | statement | status |
|---|---|---|
| RL-1 | `8.5990 = L/log2(eL) = DEF_INSTR(1)` = COROLLARY 8's failure margin | PROVED, machine-verified |
| CATCH-RL1 | the node applies a `c = 1` constant at the binding layer `c*`; the right constant there is `6.3130`; the quoted sentence's own two numbers give a third value `3.81`; and `R`-locality costs nothing at `c = 1` | FORCED CORRECTION, flagged |
| RL-2 | `DEF = THETA*AMGM*GAUSS*CAP`, exact; `(1/64, 1.000, 44.36, 12.41)` at `c=1`, `(1.000, 2.299, 1.035, 2.654)` at `c*` | PROVED, measured |
| RL-3 | `min_c DEF_INSTR = 5.969` at `c = 0.298`; non-monotone | measured |
| A1 | type bound: deficit exactly `L/kmul` = `64.0`/`32.0` | PROVED, FAILS |
| A2 | centred moment, `k = R`: deficit `8.995`; at `k = 2R` it would give `5.353` but collapses to `V_1` at the licensed radius | measured, FAILS |
| CATCH-RL2 | THEOREM 10's "position entropy, no `p` at all" is an artefact of the union bound; the binomial moment `E[C(N_A,R)]/C(m,R)` pays none of it and is positive for every `log2 p >= 3.06` | FORCED CORRECTION, flagged |
| A3 | repaired THEOREM 10 exponent `0.00171` at `c*`, deficit `258.9` | measured, FAILS |
| A4 | `N_k <= (2k-1)!!|H|^k` first fails at exactly `k = R+1` at G1/G4/G2 | measured, cap SHARP |
| A5 | the deficit is a function of `R/S` alone; saturation pins it | structural, FAILS |
| RL-4/5/6 | `k`-LOCAL is an exactly solvable LP; the LIFTING LEMMA; the pattern-LP asymptotics | PROVED / ASYMPTOTIC |
| D3(a) | `OPT_R(1) = p^{-R}` EXACTLY at G1, so `FLOOR_R(1) = 0.9786 <= 1`: `R`-locality costs NOTHING at the layer where `8.60` was computed | PROVED at toy scale |
| D3(b) | exact toy floor `X = 1.5889` at `c*` (G1, `k=R`); asymptotic official-row floors `6.21` (`k=R`) and `3.48` (`k=2R`) | EVIDENCE (toy exact) / ASYMPTOTIC |
| D3 near-optimality | `DEF_INSTR(c*) = 6.3130` is `+1.7%` off the `k=R` floor and `1.81x` off the `k=2R` floor | measured |
| P13 | the `L`-dependence of `FLOOR_k` | UNRESOLVED (reported) |
| D4 | the weakest non-local input = a box/smoothness count for `C*` at exponential scale; nothing in the bank supplies it | named, OPEN |

NOT claimed: that the tail-count criterion is true or false; any status flip;
that no argument outside `k`-LOCAL exists; that a toy-scale floor is a
theorem uniform in the row; any statement about the `t`-reading.
