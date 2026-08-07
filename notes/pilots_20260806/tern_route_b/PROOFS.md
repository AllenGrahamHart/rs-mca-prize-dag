# ROUTE (b) — the character-sum form of Z_1, and its ledger

Round 19, 2026-08-06. Pilot derivations for
`notes/pilots_20260806/tern_route_b/PREREG.md`. Machine backing:
`verify_route_b.py`, log `VERIFY_LOG.txt`, **137/137 PASS**.

DRAFT ONLY. Nothing here is minted; nothing outside this directory
was touched.

---

## §0. The object, quoted

`background/nodes/f2_z1_mass_knife_edge/statement.md:55-59`, verbatim:

```
55	**THE OPEN TERMINAL (residual, not claimed):** prove
56	Z_1 <= 2^{o(m)} at k = e. The only live route is (b): Weil-type /
57	square-root cancellation for products over the 2^{e_p}-subgroup
58	inside F_p (sizing: sqrt(p)·log p = 2^38 vs subgroup 2^39 — a
59	factor-2 headroom; back-of-envelope, not a theorem).
```

The code, `notes/pilots_20260806/f2_adm/PROOFS.md:182-185`, verbatim:

```
182	>   (i)   L^perp  =  (+)_{c=1}^{C} ker(A_c),   A_c = ((ζ^s)^l)_{l in Lambda, s<S},
183	>   (ii)  each ker(A_c) is the dual of a GRS code over F_p:  [S, S-R, R+1]_p, MDS,
184	>   (iii) dim_{F_p} L  =  C · min(S, R)      EXACTLY,
185	>   (iv)  Z(L)  =  prod_c Z_c  =  Z_1^C .
```

The mass, `notes/pilots_20260804/f2_opening/PROOFS.md:56`, verbatim:

```
56	    Z(L) := sum_{eps in L^perp cap {-1,0,1}^m} 2^{-wt(eps)},
```

The half-system and the window, `notes/pilots_20260806/z1_ternary_mass/verify.py:135`
and `:145`, verbatim:

```
135	    """omega of exact order twoN in F_p^*; half-system y_e = omega^e, e < N."""
145	    return [[pow(y, 2 * a + 1 + 2 * r, p) for y in ys] for r in range(R)]
```

**NOTATION (fixed for the whole note).** `p` prime, `e_p = v_2(p-1)`,
`zeta in F_p^*` of exact order `2^{e_p}`, `S = 2^{e_p-1}`,
`Y = {zeta^s : 0 <= s < S}` (the half-system),
`H = mu_{2^{e_p}} = Y u (-Y)`, `|H| = 2S`,
`Lambda = {1, 3, ..., 2R-1}` (shift `a = 0`),
`A[r,s] = (zeta^s)^{2r+1}`, `T = {0,+1,-1}^S`,
`Z_1 = sum_{eps in T, A eps = 0} 2^{-wt(eps)}` (the `eps = 0` term
included, so `Z_1 >= 1` always).
`e_p(t) := exp(2 pi i t / p)`. For `u in F_p^R`,
`f_u(X) := sum_{r<R} u_r X^{2r+1}` — an ODD polynomial of degree
`<= 2R-1`, and `u |-> f_u` is `F_p`-linear.
Official row (`f2_adm/PROOFS.md:89-91`, `f2_tq_pin/PROOFS.md:131`):
`p = 18446735827372343297`, `e_p = 39`, `S = 2^38`,
`R = 4294967340` (banked) or `4294967339` (exact balance),
`log2 p = 63.999999355`.

---

## §1. (R1) THE EXACT CHARACTER-SUM FORM

### LEMMA 1 (the identity).

```
    Z_1  =  p^{-R}  sum_{u in F_p^R}  P(u),
    P(u) := prod_{s<S} ( 1 + cos( 2 pi f_u(zeta^s) / p ) ) ,
```
and for the unweighted sibling,
```
    |T cap ker A|  =  p^{-R} sum_{u in F_p^R} prod_{s<S}
                          ( 1 + 2 cos( 2 pi f_u(zeta^s) / p ) ) .
```

*Proof.* The syndrome of `eps in T` is
`sigma(eps)_r = sum_{s<S} eps_s (zeta^s)^{2r+1} in F_p`, `r < R`. The
syndrome group is `F_p^R`, an ADDITIVE group, so its indicator is a sum
over ADDITIVE characters:
`[sigma = 0] = p^{-R} sum_{u in F_p^R} e_p(<u, sigma>)`. Now
```
   <u, sigma(eps)> = sum_r u_r sum_s eps_s (zeta^s)^{2r+1}
                   = sum_s eps_s f_u(zeta^s) .
```
Hence
```
   Z_1 = sum_{eps in T} 2^{-wt(eps)} p^{-R} sum_u e_p( sum_s eps_s f_u(zeta^s) )
       = p^{-R} sum_u prod_{s<S} ( 1 + (1/2) e_p(c_s) + (1/2) e_p(-c_s) )
       = p^{-R} sum_u prod_{s<S} ( 1 + cos(2 pi c_s / p) ),   c_s := f_u(zeta^s),
```
the middle step being the expansion of the product over the three
choices `eps_s in {0, +1, -1}` with weights `1, 1/2, 1/2` — the `1/2`
is exactly the `2^{-wt}` weighting, one factor per nonzero coordinate.
Dropping the `2^{-wt}` weighting replaces the local weights by
`1, 1, 1`, giving `1 + 2cos`. []

**Machine verification (EXACT, no floating point).** Working in
`Z[x]/(x^p - 1)` with `Sigma := sum_u prod_s (2 + x^{c_s} + x^{-c_s})`,
Lemma 1 is equivalent to the integer identity
```
   Sigma = 2^S p^R Z_1 * e_0  +  2^S p^{R-1} (2^S - Z_1) * J,
   J := 1 + x + ... + x^{p-1},
```
(using `sum_u x^{<u,sigma>} = p^R [sigma=0] + p^{R-1} J`). Verified
digit-exactly at G1, G2, G3, G4 — `verify_route_b.py` S2, and the
double-precision form at all six grid rows to relative `< 5e-14`
(S3). `Z_1` itself is computed exactly twice (meet-in-the-middle over
syndromes, and brute force over `3^S`) and the two agree (S1).

### CATCH-B1 (against our own bank). `z1_ternary_mass/PROOFS.md:394` is wrong for `Z_1`.

Verbatim, `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:394`:

```
394	`Z_1 = p^{-R} sum_{u in F_p^R} prod_{s<S} (1 + 2cos(2π f_u(omega^s)/p))`
```

The local factor `1 + 2cos` is the UNWEIGHTED one: that formula
computes `|T cap ker A|`, not the weighted mass `Z_1`. The correct
local factor for `Z_1` is `1 + cos`. Machine-separated at all six grid
rows (S3): e.g. at G1 (`p=17, S=8, R=2`) the `1+2cos` form returns
`17.000000` and `|T cap ker A| = 17`, while `Z_1 = 1.25`; at G4
(`p=97, S=16, R=2`) it returns `4833.000000 = |T cap ker A|` against
`Z_1 = 9.387207`. The line is a *sizing* line, explicitly disclaimed
as non-theorem at `z1_ternary_mass/PROOFS.md:545-546`, so nothing
downstream breaks — but the discrepancy is not cosmetic: the two
formulas differ by `(3/2)^S` in the trivial-character term
(`3^S` vs `2^S`), i.e. by `0.585 S = 2^37.2` bits at the official row.

### CATCH-B2 (against the round-19 brief). The tuples are ADDITIVE.

`notes/pilots_20260806/tern_route_b/PREREG.md:30` says
`Z_1 = p^{-R} sum over multiplicative-character tuples`. The syndrome
lives in the additive group `F_p^R`; its indicator is a sum over
additive characters. (The brief's own local-factor hint at
`PREREG.md:34-35`, `(1 + 2^{-1}(chi(x) + chi(x)^{-1}))`, is the right
SHAPE and evaluates to `1 + cos` once `chi` is read additively —
so the hint is right and the label is wrong.) Multiplicative
characters do enter route (b), but one level down (§3, the indicator
of the subgroup `H`), not at the syndrome level.

---

## §2. THE HALF-SYSTEM IS NOT A HALF (the first favourable finding)

### LEMMA 2. For every `j` and every `u`,
```
    2 Re W_j(u)  =  V_j(u) := sum_{x in H} e_p( j f_u(x) ) ,
    W_j(u) := sum_{s<S} e_p( j f_u(zeta^s) ) ,
```
so `V_j(u)` is REAL and is a COMPLETE character sum over the FULL
subgroup `mu_{2^{e_p}}`.

*Proof.* `zeta^S = -1` (`zeta` has order `2S`), so `H = Y u (-Y)`
disjointly. Every exponent in `Lambda` is odd, hence
`f_u(-x) = -f_u(x)`. Therefore
`sum_{x in H} e_p(j f_u(x)) = sum_{s<S} [ e_p(j c_s) + e_p(-j c_s) ]
= 2 sum_{s<S} cos(2 pi j c_s / p) = 2 Re W_j(u)`. []

**This answers PREREG.md:44-47 outright.** The brief asks whether
"the relevant complete sum [is] over the FULL subgroup, recovering
exact Gauss sums, or genuinely over the half, where partial-sum losses
bite?" — Answer: **the full subgroup, exactly.** Because the mass
`Z_1` is real, only `Re W_j` ever appears, and oddness of `Lambda`
converts `Re W_j` into half a complete subgroup sum with NO error
term. Route (b) pays no partial-summation / Polya–Vinogradov loss.
Machine-verified as an exact `F_p` multiset identity plus the numeric
consequence at `j = 1,2,3` on all six rows (S4).

---

## §3. (R2) THE CANCELLATION LEDGER

### 3.1 PROPOSITION 3 — there is no cancellation to exploit.

Every local factor obeys `1 + cos theta >= 0`, so `P(u) >= 0` for
every `u`, and
```
    Z_1  =  p^{-R} sum_u P(u)
```
is a sum of `p^R` NON-NEGATIVE reals. **No cancellation between
character tuples is available, in principle.** The name "square-root
cancellation for products over the 2^{e_p}-subgroup"
(`statement.md:56-58`) misdescribes the mechanism: what route (b)
needs is (i) SMALLNESS of each `P(u)` — i.e. equidistribution of the
value multiset `f_u(H)` in `F_p` — and (ii) a COUNT of the exceptional
`u`. Cancellation appears only one level down, inside a single
`V_1(u)`, and its job there is to certify equidistribution, not to
cancel anything at the top level.

Two floors fall out for free, which is a useful cross-check of the
decomposition against the bank:

- **Z-FLOOR in one line.** `Z_1 >= p^{-R} P(0) = 2^S p^{-R}` because
  every other term is `>= 0`. This is THEOREM Z-FLOOR
  (`statement.md:17-24`) for the single class, obtained without the
  Cauchy–Schwarz step. Verified at all six rows (S6b).
- **A finer line floor (new).** `P(u) = 2^{-S} |N(u)|^2` with
  `N(u) = prod_{x in Y} (1 + omega^{f_u(x)}) in Z[omega]`,
  `omega = e^{2 pi i/p}`. Since `u |-> f_u` is linear,
  `sigma_t(N(u)) = N(tu)` for `sigma_t in Gal(Q(omega)/Q)`, so
  `prod_{t in F_p^*} P(tu) = 2^{-S(p-1)} Nm(N(u))^2 >= 2^{-S(p-1)}`
  (`1 + omega^c != 0` for odd `p`, so `N(u) != 0` and its norm is a
  nonzero rational integer). By AM-GM the average of `P(tu)` along
  every punctured line through the origin is `>= 2^{-S}`. Verified at
  G1, G2 (S6b).

### 3.2 PROPOSITION 4 — the main term is not the main term (P4).

The trivial-character term is `p^{-R} P(0) = 2^S p^{-R}`, i.e.
`2^{S - R log2 p}`. At the official row (S9, exact `Decimal`):

| reading | `R` | `log2(main term)` |
|---|---|---|
| banked `R = ceil(t/2)` | 4294967340 | **`-46.025`** |
| exact balance | 4294967339 | **`+17.975`** |

Both reproduce the banked knife edge (`statement.md:46-52`) to
0.005 bits, which validates the decomposition against the bank.

But `Z_1 >= 1` unconditionally (the `eps = 0` term). Hence, under the
banked reading, **the error term exceeds the main term by at least
46.02 bits, unconditionally and with no hypothesis at all.**

The brief's R2 target — "what bound per tuple is needed for the total
error to stay below the main term at k = e" (`PREREG.md:40-42`) — is
therefore *unsatisfiable as posed*: no bound of any strength makes the
nontrivial part smaller than `2^{-46.02}`, because the nontrivial part
is provably `>= 1 - 2^{-46.02}`. At the official row the trivial
character carries essentially none of `Z_1`; the whole quantity lives
in the "error". The correct target is `error <= 2^{o(S)}`.

### 3.3 The exact requirement (the ledger, stated).

`Z(L) = Z_1^C` with `C <= 4` (`f2_adm/PROOFS.md:185`), so the terminal
`Z(L) <= 2^{o(m)}` is exactly `Z_1 <= 2^{o(S)}`. Since
`p^R = 2^{S + 46.02}` and `P(u) <= 2^S` always, stratifying by
`U_c := { u : P(u) >= 2^{cS} }` gives the

> **LEDGER (exact).** `Z_1 <= 2^{o(S)}` holds **iff**
> `|U_c| <= 2^{(1-c) S + 46.02 + o(S)}` for every `c in [0,1]`.
> In particular at `c = 1`: at most `2^{o(S)}` tuples `u` may have
> `P(u)` within `2^{o(S)}` of the maximum `2^S`.

This is the honest form of "what bound per tuple is needed": it is not
a per-tuple bound at all, it is a **tail-count** bound. Two ways to
supply it, §3.4 (uniform) and §3.5 (moments).

### 3.4 LEMMA 5 (the AM-GM reduction) — and why the uniform route caps.

> **LEMMA 5.** `P(u) <= ( 1 + V_1(u)/|H| )^S`. Consequently, if
> `|V_1(u)| <= eta |H|` for every `u != 0`, then
> `Z_1 <= 2^{S log2(1+eta)} + 2^{S - R log2 p}`.

*Proof.* `a_s := 1 + cos(2 pi c_s/p) >= 0`, so AM-GM gives
`prod_s a_s <= ((1/S) sum_s a_s)^S`, and by Lemma 2
`sum_s a_s = S + Re W_1 = S + V_1/2`, i.e.
`(1/S) sum_s a_s = 1 + V_1/(2S) = 1 + V_1/|H|`. []

Verified at every `u` on all six rows, worst ratio `1.000000` (S5).

Lemma 5 is strictly stronger than the Fourier/majorant route. Writing
`log(1+cos theta) = -log 2 + 2 sum_{j>=1} ((-1)^{j+1}/j) cos(j theta)`
gives
`log2 P(u) = -S + (1/ln 2) sum_{j>=1} ((-1)^{j+1}/j) V_j(u)`, which
needs a bound on `V_j` for ALL `j <= J` and loses a factor `~ log J`
to the harmonic weights (and needs a Beurling–Selberg-type majorant to
handle the log singularity at `theta = pi`). AM-GM needs **only
`j = 1`** and loses no `log J`. So the ledger's input is:

> **THE NEEDED INPUT (uniform form).**
> `max_{u != 0} |V_1(u)| = o(|H|)` — any `o(1)` relative cancellation
> in the complete subgroup sums `sum_{x in mu_{2^{e_p}}} e_p(f_u(x))`,
> uniformly over the `p^R - 1` odd polynomials `f_u` of degree
> `<= 2R-1`.

**The uniform route looks capped.** `eta` must be `o(1)` for
`2^{S log2(1+eta)}` to be `2^{o(S)}`; but `max_{u != 0} |V_1(u)|/|H|`
is measured (S7) at `0.502, 0.462, 0.432, 0.553, 0.584, 0.633` on
G1..G6 — a constant fraction, *rising* with `p`, not falling.
Equivalently `max_{u != 0} log2 P(u) / S` is measured at
`0.164, -0.178, 0.221, 0.572, 0.476, 0.645`.

A degree count suggests the same at the official row: `f_u = X g(X^2)`
with `deg g <= R-1`, and `z |-> z^2` is a bijection `Y -> mu_S`, so
`u` can be chosen making `f_u` vanish at any `R-1` prescribed points
of `Y`, i.e. at `2(R-1) = |H|/log2 p - 2` points of `H`, each
contributing `+1` to `V_1(u)`.

> **HONESTY.** That is a HEURISTIC, not a theorem: the remaining
> `|H| - 2(R-1)` unit vectors are not provably `O(sqrt|H|)`, and by
> the standing calibration clause (`statement.md:64-69`) the toy
> measurements are not evidence at the official row. **I claim no
> lower bound on `max_u |V_1(u)|`.** Nothing in Theorem 7 or
> Corollary 8 depends on this paragraph; it is recorded only as the
> reason I did not pursue the uniform route further.

### 3.5 PROPOSITION 6 (P6) — Weil is vacuous, and by DEGREE.

Decomposing the indicator of `H` over the `d = (p-1)/2^{e_p}`
characters trivial on `H` and applying Weil to each twisted sum,
```
    |V_1(u)|  <=  deg(f_u) sqrt(p)  <=  (2R-1) sqrt(p) .
```
Non-vacuity (i.e. beating the trivial `|H|`) needs
`deg(f_u) <= |H| / sqrt(p)`. At the official row (S9, exact
`Decimal`):

```
    |H| / sqrt(p)      =  2^39 / 2^32     =  128.00
    deg(f_u)           =  2R - 1          =  8,589,934,679 = 2^33.000
    deg * sqrt(p)      =  2^65.000        vs  |H| = 2^39
    => VACUOUS by exactly 26.000 bits.
```

So the Weil input is useful only for `u` supported on the first **64**
of `R = 4,294,967,340` coordinates — a fraction `p^{-(R-64)}` of
tuple space.

> **CATCH-B3 (against the node's sizing).** `statement.md:56-59` and
> `z1_ternary_mass/PROOFS.md:398-400` size route (b) as
> "`square-root cancellation is ~ sqrt(p)·log p = 2^32·64 = 2^38`
> against a subgroup of size `2^39` — **a factor 2 of headroom**".
> That comparison silently drops the DEGREE factor in the Weil bound.
> With the degree restored the comparison is `2^65` against `2^39`.
> **The factor-2 headroom does not exist; the deficit is 26 bits.**
> (The `log p` in `sqrt(p)·log p` is a Polya–Vinogradov-shaped factor
> for an *interval*; by Lemma 2 there is no interval here, so it does
> not belong either — the sizing is wrong in both factors, once
> favourably and once fatally.)

The toy grid straddles the vacuity boundary and confirms the criterion
(S7): `deg*sqrt(p) < |H|` at G1 (12.4 vs 16), G2 (10.6 vs 16),
G3 (15.5 vs 16), G4 (29.5 vs 32) — "useful"; and `>= |H|` at
G5 (56.4 vs 32), G6 (77.8 vs 32) — "VACUOUS". The official row sits
26 bits inside the vacuous side.

### 3.6 THEOREM 7 (the ledger, executed: the unconditional bound).

Weil being vacuous, the only remaining supply for the tail count is a
MOMENT bound, and the only structural theorem available to evaluate
the moment is THEOREM Z-2. Verbatim,
`background/nodes/f2_z1_mass_knife_edge/statement.md:36-38`:

```
36	**THEOREM Z-2 (gift back to DLI).** The Newton short-window
37	exclusion holds for ALL integer coefficients with w read as the l1
38	weight — the {+1,-1} restriction is unnecessary.
```

with the transported floor `2R+1` from THEOREM Z-1
(`statement.md:31-32`: "the min ternary weight is >= 2R+1 =
8,589,934,681").

> **THEOREM 7.** Unconditionally at the official row (given Z-1/Z-2),
> ```
>     Z_1  <=  2^{0.8908 S}   =   2^{2.448e11} ,
> ```
> against the trivial bound `Z_1 <= 2^S`. The saving is
> `0.1092 S = 3.001e10` bits of exponent.

*Proof.* Fix `k <= R` and `eta in (0,1]`. Split
`Z_1 <= (1+eta)^S + p^{-R} G(eta|H|) 2^S`, `G(T) := #{u != 0 :
|V_1(u)| >= T}`, using Lemma 5 on the first part and `P <= 2^S` on the
second. By orthogonality,
```
    sum_{u in F_p^R} |V_1(u)|^{2k}  =  p^R N_k ,
    N_k := #{ (x,y) in H^k x H^k : sum_i x_i^l = sum_i y_i^l,  l in Lambda } ,
```
(the map `x |-> (x^l)_{l in Lambda}` is injective on `H` since
`1 in Lambda`). Reduce each `x_i = sigma_i z_i` with `z_i in Y`,
`sigma_i = +-1` (legitimate because every `l` is odd): a solution is
exactly an integer vector `c` on `Y` with `sum_z c_z z^l = 0` for all
`l in Lambda` and `||c||_1 <= 2k`. For `2k <= 2R` THEOREM Z-2 forces
`c = 0`, i.e. the two signed multisets coincide; every such
configuration admits a perfect matching of `+`-slots to `-`-slots
carrying equal `z`, so
```
    N_k  <=  (2k-1)!! |H|^k  <=  sqrt(2) ( 2k |H| / e )^k        (k <= R).
```
Chebyshev then gives `G(eta|H|) <= p^R N_k (eta|H|)^{-2k}`, and the
tail term is `<= (1+eta)^S` as soon as
```
    k log2( e eta^2 |H| / (2k) )  >=  S ( 1 - log2(1+eta) ) + O(1).
```
The left side is maximised at `k = min(R, eta^2 S)`; since
`R/S = 1/log2 p` (saturation, `statement.md:15`), `k = R` for
`eta >= 1/sqrt(log2 p)`. Numerically optimising over `eta` at the
official row gives `eta = 0.8540`, `k = R = 4.295e9`, and
`c = 0.8908`. [] (S10.)

`N_k <= (2k-1)!! |H|^k` is machine-verified for every `(row, k)` with
`k <= R` (S8): G1 `N_2 = 720 <= 768`, G4 `N_2 = 2976 <= 3072`,
`N_1 = |H|` with equality everywhere.

**The cap `k <= R` is SHARP, not an artefact.** At G2 (`p=113, R=1`)
the bound already FAILS at `k = 2 = R+1`: `N_2 = 1104 > 768`
(S8). Z-2's hypothesis `||c||_1 <= 2R` is exactly what is load-bearing.

### 3.7 COROLLARY 8 — route (b)'s ledger lands on Z-NOGO's threshold.

Theorem 7 reaches `2^{o(S)}` iff the bracket at `k = R` beats `S/R`,
i.e. (taking the most generous `eta -> 1`, and using `|H| = 2S`,
`R = S / log2 p`) iff
```
    log2( e log2 p )  >=  log2 p .
```
Solving (S10, bisection): **`log2 p <= 3.0529`, i.e. `p <= 8.30`.**

Compare `background/nodes/f2_z1_mass_knife_edge/statement.md:40-44`,
verbatim:

```
40	**THEOREM Z-NOGO.** Saturation pins R/S = 1/log2 p, so the entire
41	distance+counting family (M3 and all sharpenings: 39.2x -> 28.3x
42	with Z-1 -> 21.3x with l1 packing) discharges only if p <= 8 —
43	against an admissible floor of log2 p >= 39. NO bound in that
44	family can ever close the terminal.
```

Route (b)'s only executable implementation lands on **the same
threshold, `p <= 8`, against the same admissible floor
`log2 p >= 39`.** This is not a coincidence of arithmetic but of
inputs: the moment evaluation consumes a *distance* theorem (Z-2) and
a *count* (Chebyshev), so it is a member of the distance+counting
family that Z-NOGO already killed. What Z-NOGO forbids is not a
particular ladder but any argument whose only structural input is
"low-`l_1` combinations cannot vanish".

**Honesty on the constant.** The `e` in the threshold comes from
Stirling in `(2k-1)!!`; with the cruder `N_k <= (2k)^k |H|^k` the
condition becomes `log2(log2 p) >= log2 p`, satisfied by NO `p`. So
`8.30` is the *most generous* constant I can prove, and the true
threshold is `<= 8.30`. The SHAPE — `log2 p <= O(log log p)` versus an
admissible `log2 p >= 39` — is constant-free. Gap at the official row:
**60.95 bits in `log2 p`**, or equivalently the exponent budget
delivers `R log2(e log2 p) = 3.197e10` of the `S = 2.749e11` bits
required, short by a factor **8.60** (**`2.429e11` bits**).

---

## §4. (R3) THE STRUCTURED-SET PRECEDENT TEST

The brief's premise, `PREREG.md:20-23`: "the L2/sqrt method loses 1-2
orders at every fixture because sqrt-cancellation is exactly what
fails on structured sets".

### CATCH-B4 — the causal clause is a gloss the round-15 record does not support.

The round-15 finding, verbatim,
`notes/pilots_20260804/mun_anticoncentration/REPORT.md:87`:

```
87	**The square-root barrier, measured** (`verify_fourier.py` F4): the L2 bound exceeds the truth by 1–2 orders of magnitude at every fixture, because `sqrt(sum N^2) ~ C(n,r')/sqrt(p)` while the truth is `~C(n,r')/p`. **The loss is exactly `sqrt(p) ~ 2^128` at the prize rows — the entire budget.**
```

The stated cause is the **L2 -> L-infinity conversion**
(`max_b N(b) <= sqrt(sum_b N(b)^2)`), not a failure of cancellation on
structured sets. Round 15's own F4 table shows the second moment
sitting within 1.4% of the flat/random value at all but the smallest
fixture (replayed ratios `1.0686, 2.9298, 1.0000, 1.0137, 1.0050,
1.0000`) — i.e. square-root cancellation *held* there; only the
mean-to-max conversion failed. (The "1-2 orders" figure is itself
loose: the measured `L2 bound / true max` ratios are
`2.92, 2.03, 4.12, 6.64, 9.10, 9.85`, i.e. 0.31-0.99 decimal orders,
and they track `sqrt(p)` — cite the `sqrt(p)` factor, not the orders.)

So the precedent must be applied on its true mechanism. Doing that,
route (b) is **genuinely different in two respects and identical in
the fatal one**:

| round-15 failure mode | does it hit route (b)? |
|---|---|
| **L2 -> L-inf conversion loses `sqrt(p)`** (`REPORT.md:87`; also `background/nodes/u2c_giant_tnull_dichotomy/notes/F2_L3_DESIGN.md:29-37`) | **NO.** Lemma 5 (AM-GM) turns the product into a FIRST-moment statement in `V_1`; no mean-to-max conversion occurs anywhere in §3. Genuinely new. |
| **partial-sum / interval losses over a subgroup** (`f2_opening/REPORT.md:45`: "Pólya–Vinogradov/Burgess are interval bounds, wrong shape for a subgroup") | **NO.** Lemma 2: oddness of `Lambda` makes the object a COMPLETE subgroup sum. Genuinely new, and favourable. |
| **Weil vacuous by DEGREE** (`mun_anticoncentration/REPORT.md:71`: "needs `deg·sqrt(q_char) < n`; measured `2^54.5`–`2^166.9` vs `n = 2^41`. … Misses by 13.5–107 bits"; `f2_opening/REPORT.md:45`: "**Weil** vacuous (folded degree up to `n_j−1 ≫ √q`); **subgroup Gauss sums** need `|H| > √q` and fail at every rung (`2^25` vs `2^31` at rung 1)") | **YES, identically.** §3.5: `deg·sqrt(p) = 2^65` vs `|H| = 2^39`, **vacuous by 26 bits**. Same mechanism, same shape, same verdict. |

**R3 verdict: the headroom is illusory.** Route (b) escapes the two
round-15 losses that the brief feared, and dies of the third, which
the brief did not name. Two genuinely new favourable structures
(complete-sum reduction; AM-GM first-moment reduction) are real gains
and are banked in §2 and §3.4 — they are what makes Theorem 7
possible at all. They do not touch the degree deficit.

---

## §5. (R5)(iii) THE 2-POWER GAUSS-SUM DIRECTION

### PROPOSITION 9 (P8) — the briefed exactness does not exist here.

`PREREG.md:69-72` proposes: "at 2-power conductor the relevant
Gauss/Jacobi sums have KNOWN exact evaluations (quadratic + quartic
residue symbols) — this may make parts of the error term EXACT rather
than bounded."

The multiplicative characters that enter (§3.5) are those **trivial on
`H = mu_{2^{e_p}}`**, i.e. of order dividing `d = (p-1)/2^{e_p}`.
Since `v_2(p-1) = e_p` EXACTLY (`f2_adm/PROOFS.md:89`: `e_p = v_2(p-1)
= 39`), `d` is **ODD**. The quadratic and quartic residue symbols have
order 2 and 4, so they are precisely the characters that never appear.
Their classical exact evaluations (`tau(chi_2) = sqrt p` or
`i sqrt p`; the quartic Gauss/Jacobi sums via `p = a^2 + b^2`) govern
sums over the index-2 and index-4 subgroups — the *squares* and
*fourth powers* — which is the opposite object to `mu_{2^{e_p}}`
(index `d`, odd). **The route-(b) sums admit no classical closed
evaluation on that ground.**

### PROPOSITION 10 — the one genuine 2-power exactness found (a doubling identity).

Let `n_c(u) := #{ s < S : f_u(zeta^s) = c }`, `omega = e^{2 pi i/p}`.
Then `P(u) = 2^{-S} |N(u)|^2`, `N(u) = prod_{c} (1 + omega^c)^{n_c}`,
and using `1 + omega^c = (1 - omega^{2c})/(1 - omega^c)`,
```
    N(u)  =  2^{n_0(u)} prod_{c != 0} ( 1 - omega^c )^{ n_{c/2}(u) - n_c(u) } ,

    log2 P(u) = -S + 2 n_0(u)
                  + 2 sum_{c != 0} ( n_{c/2}(u) - n_c(u) ) log2| 2 sin(pi c/p) | ,
```
with `c/2 := c * 2^{-1} in F_p` and `sum_{c != 0} (n_{c/2} - n_c) = 0`
(so the identity is normalisation-free). Machine-verified at G1-G4
(S6). This is EXACT, not a bound, and it is the only place the
2-power structure enters exactly: the entire dependence on `p` is
through the **doubling map `c |-> 2c` on `F_p`** and the classical
log-sine weights.

**Honest status of this lead.** It converts the problem into: bound
the correlation between the value distribution `n(u)` of an odd
polynomial on a 2-power subgroup and its own dilate `n(2 . )`, against
log-sine weights. That is a real reformulation (a Dedekind-sum-shaped
object), and it is a strictly *finer* invariant than `V_1` — but I
have no bound for it, and it does not by itself evade §3.7: any
argument that ends by counting low-`l_1` relations re-enters the
distance+counting family. I record it as a lead, not a route.

---

## §6. (R4) TOY VALIDATION — the measured table

Grid pre-registered at `PREREG.md` §C (2-power only, CATCH-Z6; `S =
2^{e_p-1}` is a 2-power by construction, so the grid rule is
automatic). `R = round(S/log2 p)`. All rows verified against the
pre-registration (S0).

```
  row  p      S    R      max|V_1|        |H|    sqrt|H| Weil deg*sqp   max/|H|  maxlgP/S
  G1   17     8    2         8.030         16      4.000     12.369    0.5018    0.1638
  G2   113    8    1         7.395         16      4.000     10.630    0.4622   -0.1778
  G3   241    8    1         6.915         16      4.000     15.524    0.4322    0.2212
  G4   97     16   2        17.706         32      5.657     29.547    0.5533    0.5721
  G5   353    16   2        18.698         32      5.657     56.365    0.5843    0.4764
  G6   673    16   2        20.254         32      5.657     77.827    0.6329    0.6453
```

Readings:

1. **Parseval is exactly right.** RMS `|V_1|` over `u != 0` measured
   `3.894, 3.723, 3.873, 5.648, 5.656, 5.657` against `sqrt(|H|) =
   4.000, 4.000, 4.000, 5.657, 5.657, 5.657`. The TYPICAL tuple shows
   full square-root cancellation, to three digits. Route (b)'s problem
   is entirely in the tail, never in the bulk.
2. **The maximum is a constant fraction of `|H|`, and rising with
   `p`.** `max|V_1|/|H|` = `0.50, 0.46, 0.43, 0.55, 0.58, 0.63`.
   Combined with the `eta >= 1/log2 p` lower-bound construction
   (§3.4), this is the measurement that kills the uniform route.
3. **The Weil vacuity criterion `deg <= |H|/sqrt(p)` is confirmed
   on both sides** (G1-G4 useful, G5-G6 vacuous), which is the
   criterion §3.5 applies at the official row.
4. **Calibration clause (standing).** All six toys have `Z_1` between
   `1.098` and `9.387` — the terminal is TRUE at toy scale. Per
   `statement.md:64-69` ("no toy is evidence about Z_1 at the official
   row") this is NOT evidence for the terminal. The toys are used here
   only to verify IDENTITIES (Lemmas 1, 2, 5; Props 3, 10) and to
   measure CONSTANTS (`max|V_1|/|H|`, the Parseval RMS, the `N_k`
   bound and its sharpness). Nothing in §3.6-§3.7 depends on a toy.
5. **AK-UNIT respected.** Every statement above bounds an archimedean
   magnitude; no congruence conclusion about any count is drawn
   anywhere.

---

## §7. (R5) VERDICT — see the pilot report.

Summary of what is proved here, in dependency order:

| # | statement | status |
|---|---|---|
| Lemma 1 | the exact `1+cos` character form of `Z_1` | PROVED, exactly machine-verified (4 rows exact, 6 numeric) |
| Lemma 2 | `2 Re W_j = V_j`, a COMPLETE subgroup sum | PROVED, machine-verified |
| Prop 3 | `P(u) >= 0`: no top-level cancellation exists; Z-FLOOR in one line; the Galois-norm line floor | PROVED, machine-verified |
| Prop 4 | the error exceeds the main term by `>= 46.02` bits unconditionally; R2's literal target is unsatisfiable | PROVED |
| Ledger | `Z_1 <= 2^{o(S)}` iff `|U_c| <= 2^{(1-c)S + 46 + o(S)}` for all `c` | PROVED (exact restatement) |
| Lemma 5 | AM-GM: `P(u) <= (1 + V_1(u)/|H|)^S` | PROVED, machine-verified |
| Prop 6 | Weil vacuous by exactly 26.000 bits; CATCH-B3 | PROVED |
| Thm 7 | `Z_1 <= 2^{0.8908 S}` unconditionally | PROVED (modulo Z-1/Z-2 as banked) |
| Cor 8 | the ledger closes only for `p <= 8.30` = Z-NOGO's threshold | PROVED |
| Prop 9 | quadratic/quartic exactness does not apply (`d` odd) | PROVED |
| Prop 10 | the exact doubling identity for `log2 P(u)` | PROVED, machine-verified |

NOT claimed: any bound on `max_u |V_1(u)|` at the official row; any
tail count at the official row; that Theorem 7's constant `0.8908` is
optimal; that `8.30` is the canonical threshold constant (it is the
most generous provable one); anything about the `t`-reading.
