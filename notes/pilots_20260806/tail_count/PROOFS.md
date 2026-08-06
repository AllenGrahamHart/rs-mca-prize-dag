# THE TAIL-COUNT CRITERION — derivations (round 20, GENERATIVE)

Pilot derivations for `notes/pilots_20260806/tail_count/PREREG.md`.
Machine backing: `verify_tail.py` (+ `tc_lib.py`, `t2_lib.py`,
`t2_stage.py`, `stages2.py`), log `VERIFY_LOG.txt`.

DRAFT ONLY. Nothing here is minted; nothing outside this directory was
touched.

---

## §0. The state, quoted

The terminal's open form,
`background/nodes/f2_z1_mass_knife_edge/statement.md:62-69`, verbatim:

```
62	NO NAMED ROUTE REMAINS. What survives of (b): the exact 1+cos
63	character form (the object is a sum of p^R NON-NEGATIVE terms — no
64	cancellation exists in principle; the true criterion is the
65	TAIL-COUNT |{u : P(u) >= 2^{cS}}| <= 2^{(1-c)S+46+o(S)} for all c);
66	two favourable reductions (oddness => COMPLETE subgroup sums, no
67	partial-sum loss; AM-GM => first moment in V_1 only, no L2->Linf
68	loss); and the recorded lead: the doubling/log-sine exact identity
69	(Prop 10 — Dedekind-sum-shaped, no bound known). Route (a)
```

The ledger it comes from, `notes/pilots_20260806/tern_route_b/PROOFS.md:243-246`:

```
243	> **LEDGER (exact).** `Z_1 <= 2^{o(S)}` holds **iff**
244	> `|U_c| <= 2^{(1-c) S + 46.02 + o(S)}` for every `c in [0,1]`.
245	> In particular at `c = 1`: at most `2^{o(S)}` tuples `u` may have
246	> `P(u)` within `2^{o(S)}` of the maximum `2^S`.
```

LEAD 1, `notes/pilots_20260806/tern_route_b/PROOFS.md:517-520`:

```
517	    N(u)  =  2^{n_0(u)} prod_{c != 0} ( 1 - omega^c )^{ n_{c/2}(u) - n_c(u) } ,
518	
519	    log2 P(u) = -S + 2 n_0(u)
520	                  + 2 sum_{c != 0} ( n_{c/2}(u) - n_c(u) ) log2| 2 sin(pi c/p) | ,
```

and its recorded status, same file `:530-536`:

```
530	the correlation between the value distribution `n(u)` of an odd
531	polynomial on a 2-power subgroup and its own dilate `n(2 . )`, against
532	log-sine weights. That is a real reformulation (a Dedekind-sum-shaped
533	object), and it is a strictly *finer* invariant than `V_1` — but I
534	have no bound for it, and it does not by itself evade §3.7: any
535	argument that ends by counting low-`l_1` relations re-enters the
536	distance+counting family. I record it as a lead, not a route.
```

The family trap, `notes/pilots_20260806/tern_route_b/PROOFS.md:426-431`:

```
426	`log2 p >= 39`.** This is not a coincidence of arithmetic but of
427	inputs: the moment evaluation consumes a *distance* theorem (Z-2) and
428	a *count* (Chebyshev), so it is a member of the distance+counting
429	family that Z-NOGO already killed. What Z-NOGO forbids is not a
430	particular ladder but any argument whose only structural input is
431	"low-`l_1` combinations cannot vanish".
```

LEAD 2, `notes/pilots_20260806/tern_small_scale_laws/PROOFS.md:466-470`:

```
466	4. **Over-representation at `p=7, w=4` is unexplained.** 288 ternary
467	   codewords against a TWT-corrected flat prediction of 0.595 — a 484x
468	   *excess* (9 orbits where 0.019 are expected). LEMMA TWT explains the
469	   weights (`7, 14`) but not the multiplicity. There is a second,
470	   opposite-signed structural mechanism here that I have not identified.
```

Notation is that of `tern_route_b/PROOFS.md:47-61`, plus (new here)

```
    d(c)    := -2 log2|cos(pi c / p)|  >= 0,     d(0) = 0      (LOCAL COST)
    cost(u) := sum_{s<S} d(c_s(u)),              c_s(u) = f_u(zeta^s)
    C*      := { (f_u(zeta^s))_{s<S} : u in F_p^R }  <=  F_p^S  (VALUE CODE)
    Delta   := R log2 p - S                      (the row's SATURATION CONSTANT;
                                                  46.02 at the official row)
    E(c)    := log2|U_c| - [(1-c)S + Delta]      (the CRITERION EXCESS)
```

---

## §1. (T1a) THE DOUBLING LEAD TELESCOPES — LEAD 1(a) IS A MIRAGE

### THEOREM 1 (the cost form).

```
    log2 P(u)  =  S  -  cost(u)  =  S  -  sum_{s<S} d(c_s(u)) ,
```

*Proof.* `1 + cos t = 2 cos^2(t/2)`, so
`log2(1 + cos(2 pi c/p)) = 1 + 2 log2|cos(pi c/p)| = 1 - d(c)`. Sum over
`s < S`. []

### THEOREM 2 (Proposition 10 telescopes to Theorem 1).

Write `L(c) := log2|2 sin(pi c/p)|` for `c != 0`. Reindexing the first
sum of `PROOFS.md:520` by `c = 2b`,

```
    sum_{c!=0} n_{c/2} L(c)  =  sum_{b!=0} n_b L(2b) ,
```

so Prop 10's right-hand side equals

```
    -S + 2 n_0 + 2 sum_{c!=0} n_c [ L(2c) - L(c) ] .
```

Now `sin(2x) = 2 sin x cos x` and `|sin(pi (2c mod p)/p)| = |sin(2 pi c/p)|`
give, for every `c != 0`,

```
    L(2c) - L(c)  =  log2|2 cos(pi c/p)|  =  1 - d(c)/2 .
```

Hence the RHS is `-S + 2 n_0 + 2(S - n_0) - sum_{c!=0} n_c d(c) = S - cost(u)`,
which is Theorem 1. []

Machine-verified at G1–G4 over **every** tuple `u` (all `289 + 113 + 241 +
9409` of them): Prop 10's RHS, the cost form, and the direct product agree
to `< 7e-13`; the per-value identity `L(2c) - L(c) = 1 - d(c)/2` holds for
every `c != 0` to `< 3.1e-14`; and `prod_{c!=0}|cos(pi c/p)| = 2^{-(p-1)}`
exactly (`verify_tail.py` IDENT, P1a–P1d).

> **CATCH-T1 (against the round-19 lead, and against the node's
> statement).** `statement.md:68-69` records "the doubling/log-sine exact
> identity (Prop 10 — Dedekind-sum-shaped, no bound known)" as the surviving
> lead of route (b). **The doubling map cancels.** Summing Prop 10 by parts
> over `c -> 2c` returns the elementary identity `log2 P = S - sum_s d(c_s)`,
> which is `log(1+cos t) = log 2 + 2 log|cos(t/2)|` applied `S` times and
> contains no arithmetic beyond it. The `(1 - omega^{2c})/(1 - omega^c)`
> rewriting *creates* the log-sine weights and the doubling shift; summing
> by parts *destroys* both. **There is no Dedekind sum here to bound.**
> Prop 10 is still a true identity and still finer than `V_1` — but its
> fineness is the fineness of the value multiset `{n_c}`, not of the
> doubling map, and LEAD 1 attack line (a) (orbit telescoping / Dedekind-sum
> literature shapes) has no object to act on.

Note what the collapse *gives*: the cost form is a **sum of independent
local costs**, which is what makes §§2–5 possible. The lead was worth
chasing; it terminates in a better-shaped object than it started with.

---

## §2. (T1) THE NORMALISED LEDGER — the criterion has no free constants

### THEOREM 3 (normalised form of the ledger).

For every `c`, `|U_c| <= 2^{(1-c)S + Delta}` **iff**
`Pr_u[ P(u) >= 2^{cS} ] <= 2^{-cS}`, where `u` is uniform on `F_p^R`.

*Proof.* `|U_c| = p^R Pr`, and `2^{(1-c)S+Delta} = 2^{(1-c)S + R log2 p - S}
= p^R 2^{-cS}`. []

So the ledger's `+46.02` is **exactly** the saturation constant
`Delta = R log2 p - S`, and the criterion in normalised form,

```
    Pr_u[ P(u) >= 2^{cS} ]  <=  2^{-cS + o(S)}   for every c in [0,1],
```

**contains no reference to `p` or `R` at all**. It is a pure
large-deviation statement about the random variable `log2 P(u)/S`. Two
immediate consequences:

- **`c = 0` is trivial** (`|U_0| = p^R` and the allowance is exactly `p^R`);
  the criterion is an equality there, with no slack and no content.
- **`c = 1` is a theorem** (§7): `|U_1| = 1`, so `E(1) = -Delta` EXACTLY.

### COROLLARY 4 (the knife edge IS the `c = 1` slack).

`E(1) = -Delta`, and `Delta` is the knife-edge constant of
`statement.md:46-52`: `-46.025` under the banked `R = ceil(t/2)` reading,
`+17.975` under exact balance. Hence the tail criterion has **46.02 bits of
slack at `c = 1` under the banked reading, and a 17.98-bit deficit under
exact balance** — the deficit being absorbable only by the `o(S)` term.
This reproduces THEOREM Z-FLOOR's firing from the opposite direction: the
`u = 0` atom contributes `p^{-R} P(0) = 2^{-Delta}` to `Z_1`, which is
exactly the `2^{17.98}` floor of `statement.md:49-52` under exact balance.
Measured at every toy row: `max_c E(c) = -Delta`, attained at `c = 1`
(`verify_tail.py` PROF).

---

## §3. (T1b) WHAT THE OBJECT EXACTLY SUPPLIES — and the trap self-check

### THEOREM 5 (the value code is MDS; `R`-wise independence).

`C*` is a GRS code `[S, R]_p`: `f_u(zeta^s) = zeta^s g_u((zeta^s)^2)` with
`deg g_u <= R-1`, and `z |-> z^2` is a bijection `Y -> mu_S`. Hence:

1. any `R` coordinates of the codeword determine `u` (interpolation);
2. for every `s`, `c_s(u)` is **exactly uniform** on `F_p` as `u` ranges
   over `F_p^R`;
3. for any `R` distinct `s_1,...,s_R`, `(c_{s_1},...,c_{s_R})` is **exactly
   uniform** on `F_p^R` — the value vector is `R`-wise independent.

*Proof.* (1) is Vandermonde/GRS invertibility. (2),(3): the map
`u |-> (c_{s_i})_i` is `F_p`-linear with invertible matrix by (1). []

### COROLLARY 6 (exact moments).

```
    E_u[ log2 P(u) ]        =  -S ( 1 - 2/p )                    EXACTLY,
    Var_u[ log2 P(u) ]      =  S Var(d)         (R >= 2)         EXACTLY,
    E_u[ sum_c n_c(u)^2 ]   =  S + S(S-1)/p                      EXACTLY.
```

*Proof.* By Theorem 5(2), `E_u[d(c_s)] = (1/p) sum_c d(c) = -(2/p)
sum_{c!=0} log2|cos(pi c/p)| = 2(p-1)/p`, using
`prod_{c!=0}|cos(pi c/p)| = 2^{-(p-1)}` (from `prod_{c!=0}|sin(2 pi c/p)| =
prod_{c!=0}|sin(pi c/p)|` and the double-angle formula). Then Theorem 1.
For the variance, Theorem 5(3) with `R >= 2` makes the coordinates
pairwise independent, so covariances vanish. For the energy,
`E[sum_c n_c^2] = S + sum_{s != s'} Pr[c_s = c_{s'}]` and
`u |-> f_u(x) - f_u(y)` is a nonzero linear functional for `x != y` in `Y`
(its `r = 0` coefficient is `x - y != 0`), so each probability is `1/p`. []

All four verified exactly (integer arithmetic for the marginals, the
`R`-subset joint law and the energy; `< 1e-7` for the archimedean means)
at G1–G4 and again at every profiled row (`verify_tail.py` DIST, PROF).

> **FAMILY-TRAP SELF-CHECK (mandatory, PREREG §2).** Corollary 6 consumes
> **no distance theorem and no count**. The only structural input is that
> `u |-> f_u(x) - f_u(y)` is a nonzero functional, i.e. that a nonzero
> polynomial of degree `< 2S` has `< 2S` roots — a Vandermonde fact of
> degree, not an `l1`-relation count, and in particular NOT THEOREM Z-2.
> Its "threshold in `p`" is vacuous: the statements are exact for every
> `p`. **This is the brief's requested evasion of Corollary 8, and this
> paragraph is the "SAY HOW".** The trap re-enters one line later, at
> Theorem 9, and I flag it there.

---

## §4. (T1) THE CRITERION IS SATURATED BY THE FLAT MODEL — the binding layer

Let the flat model be: `c_1,...,c_S` i.i.d. uniform on `F_p` (which
Theorem 5 certifies for any `R` of them, and no more). Write
`X_s := log2(1 + cos(2 pi c_s/p)) = 1 - d(c_s)`.

### THEOREM 7 (the flat CGF, in closed form).

As `p -> infinity`, `Lambda(theta) := log2 E[2^{theta X}]` satisfies

```
    Lambda(theta)  =  log2 binom(2 theta, theta)  -  theta
                   =  [ ln Gamma(2 theta + 1) - 2 ln Gamma(theta + 1) ]/ln 2
                      - theta ,
```

so `Lambda(1) = 0` and `Lambda'(1) = 1/ln 2 - 1 = 0.4426950409...`.

*Proof.* `E[(1 + cos t)^theta] = 2^theta (1/pi) int_0^pi cos^{2 theta} phi
dphi = binom(2 theta, theta) 2^{-theta}`. `Lambda(1) = log2 E[1+cos] = 0`.
`Lambda'(1) = [2 psi(3) - 2 psi(2)]/ln2 - 1 = 1/ln2 - 1`. []

### COROLLARY ZM (zero margin, and where it binds).

Under the flat model `Pr[P >= 2^{cS}] = 2^{-I(c) S + o(S)}` with
`I(c) = sup_theta (theta c - Lambda(theta))`. Since `Lambda(1) = 0`,

```
    I(c)  >=  1 * c - Lambda(1)  =  c        for EVERY c,
```

with **equality iff `theta = 1` is the maximiser, i.e. iff
`c = Lambda'(1) = 1/ln 2 - 1 = 0.442695...`**. Therefore:

> **the flat model satisfies the tail criterion with margin `I(c) - c >= 0`,
> and the margin is EXACTLY ZERO at `c* = 1/ln 2 - 1 = 0.4427`.**

Measured margin profile (`verify_tail.py` THR): `0.157` at `c = 0`,
`0.055` at `0.2`, `0.021` at `0.3`, `0.0021` at `0.4`, **`0.0000` at `c*`**,
`0.0042` at `0.5`, `0.037` at `0.6`, `0.28` at `0.8`, `2.00` at `1`.
The finite-`p` constant `m_1(p) = (1/p) sum_c (1+cos)(log2(1+cos))` was
computed at `p = 17, 97, 673, 65537`: `0.4421636, 0.4426922, 0.4426950,
0.4426950409` — converging to `c*` like `O(1/p^2)`.

**This is the sharpest statement I can make about where the terminal
lives.** The criterion is not slack anywhere: it is an *equality* at
`c = 0` (trivially), an *equality up to `Delta`* at `c = 1` (Corollary 4),
and *exactly saturated by the flat model* at `c* = 0.4427`. A proof of the
terminal must therefore show the value distribution is flat-like **to
within `2^{o(S)}` at the single layer `c*`** — no layer can be given away,
and no "we lose a constant factor per coordinate" argument can survive,
because a loss of `epsilon` per coordinate costs `epsilon S` and the
available margin at `c*` is `0`.

---

## §5. (T1c) THE STRUCTURE THEOREM — the tail is a small-values count

### THEOREM 9 (structure of the tail).

```
    U_c  =  { u :  cost(u) <= (1-c) S }  =  { u : sum_{s<S} d(c_s(u)) <= (1-c)S } ,
```

i.e. **the tail is exactly the set of GRS codewords of small log-cost**;
and for every `delta in (0,1]`,

```
    u in U_c  ==>  #{ s : d(c_s(u)) > (1-c)/delta }  <  delta S ,
```

so at least `(1-delta) S` coordinates of the codeword lie in the interval
`A(D) = { c : d(c) <= D }`, `D = (1-c)/delta`, of relative length
`rho(D) = (2/pi) arccos(2^{-D/2})`.

*Proof.* Theorem 1 and Markov. []

**What this converts the problem into.** `A(D)` is a symmetric interval
around `0` mod `p`. So the tail count is a **box count for the
Construction-A lattice** `L(C*) = { v in Z^S : v mod p in C* }`, of
determinant `p^{S-R}`; the criterion asks that `L(C*)` have no more points
in the box `A(D)^S` than the volume heuristic gives. This is the
"parametrized family count" the brief asked for: **the family is
"codewords in a box", and the criterion is exactly "`C*` is not unusually
smooth".**

Two supplies exist for such counts, and I ran both.

### THEOREM 10 (supply A — interpolation; and it dies at EVERY `p`).

If `m := |A(D)| >= 2`, then `R` coordinates in `A(D)` determine `u`, so
`|U_c| <= binom(S,R) m^R`, and the criterion needs

```
    H(1/L)  +  (1/L) log2(m/p)  <=  -c ,        L := log2 p, R/S = 1/L.
```

**This fails for every `c in (0,1)` and every `p`.** As `c -> 0`,
`D -> L/(L-1) -> 1`, `m/p -> rho(1) = 1/2`, and the condition becomes
`H(1/L) - 1/L <= -c < 0`, while `H(1/L) > 1/L` for every `L > 2`.
Machine-checked over `log2 p in {2,3,4,8,16,32,64,128,1024,2^20}`: the best
`c` gives `-0.708, -0.669, -0.607, -0.430, -0.278, -0.171, -0.101, -0.059,
-0.011, -0.0005` — **negative everywhere, with no threshold in `p`**
(`verify_tail.py` THR-3/THR-4).

> **The mechanism of failure is worth naming: it is the ENTROPY OF THE
> POSITION SET.** The bound pays `S H(R/S) = 0.1161 S` bits to say *which*
> `R` coordinates are small, and recovers only `R log2(1/rho) = 0.0156 S`
> bits from the smallness of the values. Position entropy beats value
> savings by a factor `~ log2(L)` — and this ratio is `H(1/L) L / 1 ->
> log2 L`, so it *worsens* as `p` grows.

> **FAMILY-TRAP SELF-CHECK.** Theorem 10 consumes a distance-type input
> (MDS/interpolation) and a count (`binom(S,R)`), so it IS a
> distance+counting member in the sense of `PROOFS.md:426-431`. Its
> threshold is not `p <= 8.30` but `NO p AT ALL` — strictly worse than
> Corollary 8. Reported as DEAD FAMILY, not as progress.

### THEOREM 11 (supply B — the Z-2 moment bound, run per layer).

Lemma 5 of round 19 gives `P(u) >= 2^{cS} => V_1(u) >= eta_c |H|`,
`eta_c = 2^c - 1`. Chebyshev on the `2k`-th moment with
`N_k <= (2k-1)!! |H|^k` (`k <= R`, THEOREM Z-2) gives
`Pr <= sqrt2 (2k/(e eta_c^2 |H|))^k`, maximised at `k = min(R, eta_c^2 S)`.
With `R/S = 1/L`, `|H| = 2S`, the criterion at layer `c` needs

```
    (1/L) log2( e eta_c^2 L )  >=  c        (branch k = R),   or
    log2(e) eta_c^2            >=  c        (branch k = eta_c^2 S).
```

At `L = 64` the certified set of layers is **EMPTY** (`max_c` of the LHS
minus `c` is `-5.0e-5`, attained only in the degenerate limit `c -> 0`
where the criterion is trivial anyway). Bisecting in `L`, the set becomes
nonempty exactly at `log2 p <= 3.0529`, i.e. `p <= 8.299`, and then only at
`c = 1`. **This is COROLLARY 8's threshold, recovered layer by layer**
(`verify_tail.py` THR-1/THR-2).

> **FAMILY-TRAP SELF-CHECK.** Distance (Z-2) + count (Chebyshev) => dead
> family; threshold `p <= 8.30` against `log2 p >= 39`. Flagged.

---

## §6. (T1c/T4) THE ONE PROVED LAYER — the endpoint theorem

### THEOREM 12 (endpoint).

Let `d_min := d(1) = -2 log2 cos(pi/p) > 0` be the least nonzero local
cost. If

```
    1 - c  <  d_min ( 1 - R/S ) ,
```

then `U_c = {0}`, i.e. `|U_c| = 1` and the criterion holds at layer `c`
with `Delta` bits to spare.

*Proof.* `cost(u) <= (1-c)S < d_min (S - R)` forces the number of `s` with
`c_s(u) != 0` to be `< S - R`, so at least `R` coordinates of the codeword
vanish; by Theorem 5(1) any `R` coordinates determine `u`, and the zero
codeword comes from `u = 0`. No union bound over position sets is needed —
the conclusion is the same for every choice — which is exactly why
Theorem 10's entropy term is absent here. []

At the official row (`Decimal`, 60 digits): `d_min = 2^{-124.168}`,
`1 - R/S = 0.984127`, so

```
    U_c = {0}   for every   c  >  1 - 2^{-124.191} .
```

**Honest size of this result:** the proved range has width `2^{-124.19}`.
It is an ENDPOINT, not a range — it proves the `c = 1` layer of the ledger
(`PROOFS.md:245-246`: "at most `2^{o(S)}` tuples `u` may have `P(u)` within
`2^{o(S)}` of the maximum") in the strongest possible form (`exactly one`),
and nothing else. Verified at G1–G4 and at every profiled row: `max_u log2
P = S`, attained exactly once, at `u = 0`.

---

## §7. (T4) THE OBSTRUCTION — why both supplies fail, and what is missing

Collecting §§3–6, the object supplies exactly three kinds of information:

| input | what it gives | trap status |
|---|---|---|
| MDS / `R`-wise independence (Thm 5) | all moments of the value vector up to order `R`; the exact mean, variance, energy (Cor 6) | clean (no distance theorem, no count) |
| THEOREM Z-2 (`l1 <= 2R` relations vanish) | `N_k <= (2k-1)!!|H|^k` for `k <= R` (Thm 11) | DEAD FAMILY, `p <= 8.30` |
| interpolation / GRS (Thm 5(1)) | `u` from any `R` coordinates (Thms 10, 12) | DEAD FAMILY, no `p` at all |

and the criterion demands a tail probability `2^{-cS}` at `c* = 0.4427`.

> **THE STRUCTURAL DEFICIT, stated exactly.** All three inputs are
> `R`-local: each certifies only statements about `R` coordinates at a
> time. A tail bound at level `2^{-cS}` derived from `k`-local information
> costs at least `~k` bits of exponent per certificate and `k <= R = S/L`,
> so the best exponent any `R`-local argument can reach is `O(R log(...)) =
> O(S log2(e L)/L) = 0.116 S` at `L = 64`, against the required `c* S =
> 0.443 S`. **The gap is the factor `L / log2(e L) = 8.60`, and `L/log2 L`
> is exactly the shape that makes COROLLARY 8's threshold `log2 p =
> O(log log p)`.** This is why route (b)'s two supplies and this pilot's
> third all land on the same wall: they are not three arguments, they are
> three readings of `R`-wise independence, and `R`-wise independence is
> `log2 p` times too weak — by exactly the saturation constant.

> **AND THE FOURIER ESCAPE IS CIRCULAR.** The classical non-local
> instrument for a lattice box count is Poisson summation. For
> `L(C*)` the dual lattice is Construction-A over `C*^perp` scaled by
> `1/p`, and `C*^perp` is (a scaling of) the parity-check side of the
> original problem: Poisson summation on the box count returns
> `sum over the dual code of the Fourier transform of the box`, which is
> the identity of LEMMA 1 read backwards, i.e. `Z_1` itself. **The tail
> count and the mass are Poisson duals; neither can be computed from the
> other without new input.** (Structural observation, not a theorem: it
> shows the two standard instruments are the *same* instrument here, it
> does not prove no argument exists.)

**Consequence for the board.** The terminal now has a named quantitative
target (`c* = 0.4427`), a named required strength (`Pr <= 2^{-0.443 S}`),
and a named deficit (`R`-locality, short by the factor `log2 p / log2(e
log2 p) = 8.60`). Any future route must supply information that is NOT
`R`-local — e.g. a genuine equidistribution theorem for `f_u(H)` valid for
*individual* `u`, which is what Weil would have given had it not been
vacuous by 26 bits (`PROOFS.md:312-317`).

---

## §8. (T2) THE `p = 7, w = 4` CREATION MECHANISM — identified

The cell (`ssl_lib.py:10-12`): `I3(32,7,4) = CT(16, 7, T)`,
`T = <7>`-closure of `{1,3}` mod `32` `= {1,3,5,7,17,19,21,23}`,
`ord_32(7) = 4`, `F_7`-rank `8`, `288` codewords of weights `{7,14}`.
Independently re-censused here from scratch (own `F_{7^4}` construction,
own meet-in-the-middle over `3^16`), reproducing the banked row
`ssl PROOFS.md:114` `6560 / 0 / 16640 / 148224` and `288` with spectrum
`{7: 32, 14: 256}` (`verify_tail.py` T2/CTRL, T2/CELL).

### THEOREM 13 (the mechanism: decimation + composition).

1. **Decimation.** Every one of the 32 weight-7 codewords is supported on
   a single sublattice: 16 on the even coordinates, 16 on the odd
   (measured; `MIXED` count `0`). Under `v(X) = g(X^2)` the conditions
   become `g(eta^s) = 0`, `eta = omega^2` of order 16, and `s` matters only
   **mod 16**: `T mod 16 = {1,3,5,7}`, so `|T| = 8` collapses to `4`. The
   even-sublattice system therefore has `F_7`-rank **4, not 8** — a
   `7^4 = 2401`-fold density gain. Measured: length 8, rank 4, dim 4.
2. **One orbit.** That `[8,4]_7` code is self-dual (`T' u (-T')` = all odd
   residues mod 16), so LEMMA TWT forces `7 | wt`, i.e. `wt = 7`; it
   contains exactly `16` ternary words = ONE free negacyclic orbit.
3. **Composition.** Even- and odd-supported codewords have disjoint
   supports, so every sum of one of each is again a ternary codeword:
   `16 x 16 = 256`, and the measured weight-14 stratum is **exactly** that
   set (verified as a set equality).

Hence `288 = 16 + 16 + 16*16` **exactly**, and the entire cell is generated
by ONE orbit at the halved length.

### The ledger for the `484x`

```
  flat + TWT prediction for the whole cell                       0.5951
  --- even-supported weight-7 stratum ---
  flat (rank 8):        C(8,7) 2^7 / 7^8                     =  0.000178
  after DECIMATION      C(8,7) 2^7 / 7^4                     =  0.4265
  per LEMMA ROT orbit of size 16                             =  0.0267 orbits
  MEASURED                                                   =  1 orbit (16 words)
  --- odd-supported weight-7 stratum: identical by rotation  =  16 words
  --- mixed weight-14 stratum ---
  flat:                 C(8,7)^2 2^14 / 7^8                  =  0.1819
  FORCED by composition (16 x 16)                            =  256
  MEASURED                                                   =  256
```

So the `484x` factors as **`7^4` (decimation rank collapse) x `16` (orbit
quantization) x `9` (composition: `288/32`)**, leaving a single residual:
one orbit occurred where `0.0267` were expected. That residual is a
**single Poisson event** (`P(>=1) = 2.6%`), not a `484x` anomaly.

### Why `p = 7` and nothing else

Cross-`p` scan of the decimated cell `CT(8, p, {1,3,5,7} mod 16)`
(`verify_tail.py`/probe): the collapse `|T mod 16| = 4` happens only for
`p in {7,17,23}` in `{3,...,47}` (those with `ord_16(p) = 2`); of these,
LEMMA TWT forces `p | wt` with `wt <= 8`, which is **impossible for
`p = 17, 23`** — measured ternary counts `0` and `0`. `p = 7` is the only
prime in the scan where a nonzero multiple of `p` fits inside the
sublattice length.

> **CATCH-T2 (the creation mechanism needs `p = O(1)`).** The second
> ingredient of the mechanism is the condition `p <= (sublattice length)`.
> That is a `p <= O(1)` condition of exactly the shape THEOREM Z-NOGO and
> COROLLARY 8 produce on the *bounding* side. **Creation-by-self-
> orthogonality and discharge-by-distance+counting die at the same place**:
> `p` bounded by a length. At `log2 p >= 39` neither can operate. This is a
> genuine structural symmetry of the object, and it says the small-`p`
> over-representations are not evidence of danger at the prize rows.

---

## §9. (T2) TRANSPORT — THEOREM D: no analogue at the F2 parameters

### THEOREM 14 (decimation dichotomy).

At the official object, index the sublattices of `Y ≅ Z/S` (all of them:
`S = 2^38` is a 2-power, so every subgroup is `2^k Z/S`). At level `k` the
sublattice has length `A = 2^{38-k}`, `xi = zeta^{2^k}` has order `2A`, and
the window `Lambda = {1,3,...,2R-1}` acts through `Lambda mod 2A`. Then

```
    the window COLLAPSES (two exponents coincide)  <=>  2A <= 2R-2  <=>  A <= R-1 ,
    the sublattice code has POSITIVE dimension     <=>  A > R .
```

These are **mutually exclusive**, and `A = R` is impossible because `R` is
not a 2-power (`v_2(R) = 2` for the banked `R = 4294967340`;
`R = 4294967339` is odd). Verified for both `t`-readings over all 39
levels: **no level has both** (`verify_tail.py` TR-1..TR-3), and the same
dichotomy holds at every toy `I1` row and every level (TR-4).

*Why:* the crossover sits at `A ≈ R`, and `2R - 2 = S/32.00` exactly
because `R/S = 1/log2 p` — **the saturation constant is what separates the
two conditions.** The official window is a SHORT INITIAL SEGMENT of
diameter `S/32`; the `p=7` cell's `T` is SPREAD (it contains `s` and
`s+16`), which is what let it collapse.

**Transport verdict: the mechanism provably does NOT transport** — by two
independent routes: (i) Theorem 14 (no decimation level both collapses and
retains dimension); (ii) the TWT ingredient needs `|T| >= N/2` and
`p <= length`, and at the official row `R/S = 1/64` and `log2 p >= 39`,
so it fails on both counts — which is CATCH-19D
(`ssl PROOFS.md:372-382`) re-derived independently.

**Banked as a tail-count constraint.** Since `Z_1 = p^{-R} sum_u P(u)`, a
creation mechanism producing many ternary kernel vectors would force `Z_1`
large and hence (Theorem 3) force the tail count large. Theorem 14 says
the only creation mechanism actually observed in the small-scale census
cannot operate at the official parameters, so **it forces no tail**. This
removes a candidate refutation of the terminal; it does not prove the
terminal.

> **MISS (registered prediction P6/P7 partially wrong).** I pre-registered
> H1 (ternary generator polynomial) as the likely mechanism with prior
> ~0.5, and P7's transport argument via the generator's constant term
> `+- zeta^{R^2}`. **H1 is REFUTED**: the generator is
> `h = 1 + 2X^2 + 2X^4 + 5X^6 + X^8` (symmetric residues
> `[1,0,2,0,2,0,-2,0,1]`), not ternary, weight 5 not 7. The true mechanism
> is decimation + composition, and `h`'s being a polynomial in `X^2` is a
> *consequence* of the decimation, not the cause. P7's conclusion (no
> transport) stands, but by Theorem 14, not by the constant-term argument I
> registered. Reported as a miss, not absorbed.

---

## §10. (T3) THE MEASURED TAIL PROFILE

Grid exactly as pre-registered (`PREREG.md` §C): `S = 2^{v_2(p-1)-1}`
forced by `p`, `Lambda = {1,3,...,2R-1}` so the exponent `0` never occurs
(**no shift-0 cell**, CATCH-19B structurally absent, asserted in code), all
lengths `2S` 2-powers (CATCH-Z6 automatic). Every row exhaustive over all
`p^R` tuples; nothing sampled.

Reported per row: `E(c) = log2 Pr + cS` (Theorem 3) and `E_nz(c)`, the same
with the `u = 0` atom removed — `u = 0` lies in every `U_c` and is exactly
the trivial-character term, so `E_nz` is the genuine tail.

```
 row              S    R   Delta     Z_1            max_c E(c)   max_c E_nz(c)
 G1 p=17    (A)   8    2   +0.175    1.250000       -0.175 @1.00  -2.375 @0.10
 G2 p=113   (A)   8    1   -1.180    2.375000       +1.180 @1.00  (empty)
 G3 p=241   (A)   8    1   -0.087    1.500000       +0.087 @1.00  -1.713 @0.15
 G4 p=97    (A)  16    2   -2.800    9.387207       +2.800 @1.00  +0.600 @0.55
 G5 p=353   (A)  16    2   +0.927    1.156250       -0.927 @1.00  -2.727 @0.45
 G6 p=673   (A)  16    2   +2.789    1.097656       -2.789 @1.00  -2.197 @0.45
 B  p=193   (B)  32    2  -16.815    1.153e5       +16.815 @1.00  -4.385 @0.15
 B  p=193   (B)  32    3   -9.223    5.984e2        +9.223 @1.00  -1.377 @0.45
 B  p=577   (B)  32    2  -13.655    1.290e4       +13.655 @1.00  -1.745 @0.30
 B  p=641   (B)  64    2  -45.352    4.490e13      +45.352 @1.00  (empty)
 B  p=257   (B) 128    1 -119.994    1.324e36     +119.994 @1.00  (empty)
 B  p=769   (B) 128    2 -108.826    5.754e32     +108.826 @1.00  (empty)
 A7 p=65537      32768 1     ---     UNREACHED (p^R S = 2.15e9 evaluations)
```

Readings:

1. **`max_c E(c) = -Delta` at `c = 1` on EVERY row**, exactly — Corollary 4
   measured. FAMILY B rows are far off-saturation (`Delta` very negative),
   so their `Z_1` is dominated by the `u = 0` atom (`2^{-Delta}`); that is
   an artefact of off-saturation, not a tail signal, which is precisely why
   `E_nz` is reported.
2. **The genuine tail obeys the criterion's decay at every row measured**:
   `E_nz(c) < 0` at every `(row, c)` except one cell (`G4`, `+0.600` at
   `c = 0.55`). No row shows `E_nz` growing with `S`: the `S = 8, 16, 32`
   families give `-2.4/-1.7`, `+0.6/-2.7/-2.2`, `-4.4/-1.4/-1.7`.
3. **The binding layer is measured where COROLLARY ZM predicts it.**
   `argmax_c E_nz` = `0.45, 0.45, 0.45` on the three rows with enough
   resolution and enough tail (`G5, G6, p=193 R=3`), against
   `c* = 0.4427`. The grid step is `0.05`.
4. **Against the flat model**, the measured tail sits `1.4`–`2.9` bits
   BELOW the flat rate function across the whole `c`-range (row `p=193,
   R=3`: excess `-2.56, -2.59, -2.69, -2.80, -2.56, -2.86, -2.70, -2.70,
   -2.91, -1.38` at `c = 0.00..0.45`), tightening exactly at `c*`.
5. **Calibration clause (standing, `statement.md:64-69`).** No toy is
   evidence about `Z_1` at the official row. Toys here verify IDENTITIES
   (Theorems 1, 2, 5, Cor 6, Thm 13) and measure CONSTANTS
   (`m_1(p)`, `E_nz`, the `484x` ledger). Nothing in §§4–7 or §9 depends on
   a toy. In particular "the measured tail is below flat" is NOT a claim
   that the object beats random.
6. **AK-UNIT respected**: every statement bounds an archimedean magnitude
   or counts exactly; no congruence conclusion about any count is drawn.

---

## §11. Summary table

| # | statement | status |
|---|---|---|
| Thm 1 | `log2 P(u) = S - cost(u)`, `d(c) = -2log2|cos(pi c/p)|` | PROVED, machine-verified |
| Thm 2 | Prop 10 telescopes to Thm 1 — no Dedekind content (CATCH-T1) | PROVED, machine-verified |
| Thm 3 | normalised ledger: criterion `<=> Pr[P >= 2^{cS}] <= 2^{-cS+o(S)}` | PROVED |
| Cor 4 | `E(1) = -Delta`: the knife-edge constant IS the `c=1` slack | PROVED, measured |
| Thm 5 | `C*` is MDS; values are exactly `R`-wise independent | PROVED, machine-verified |
| Cor 6 | exact mean `-S(1-2/p)`, variance `S Var(d)`, energy `S + S(S-1)/p` | PROVED, exact |
| Thm 7 | flat CGF `= log2 binom(2t,t) - t`; `Lambda(1) = 0` | PROVED |
| Cor ZM | flat model saturates the criterion; binding layer `c* = 1/ln2 - 1` | PROVED |
| Thm 9 | tail = small-values/box count for the GRS code `C*` | PROVED |
| Thm 10 | interpolation supply dies at EVERY `p` (position entropy) | PROVED (dead family) |
| Thm 11 | Z-2 moment supply certifies an empty `c`-range; threshold `p <= 8.30` | PROVED (dead family) |
| Thm 12 | `U_c = {0}` for `c > 1 - 2^{-124.191}` — the one proved layer | PROVED |
| Thm 13 | `p=7,w=4`: `288 = 16 + 16 + 16^2` by decimation + composition | PROVED, machine-verified |
| Thm 14 | decimation dichotomy: no analogue at the official row | PROVED |

NOT claimed: any tail bound at the official row for `c <= 1 - 2^{-124.19}`;
that no argument can supply one (§7 is a structural deficit, not a no-go);
any statement about the `t`-reading; that the measured `E_nz` profile is
evidence about the official row.
