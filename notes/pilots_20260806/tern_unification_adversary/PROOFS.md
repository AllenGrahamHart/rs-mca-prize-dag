# PROOFS — the ternary unification, attacked (round 19, ADVERSARIAL)

All checks: `verify.py`, log `verify.log`, exit 0, 60 checks, 0 failures.
Run under `tools/ramguard local`. Toy grids are 2-POWER only except §6,
which deliberately probes the composite-length disanalogy.

---

## §0. Sources of record (verbatim)

**I1** — `background/nodes/f2_z1_mass_knife_edge/statement.md:12-15`:

> THE F2 TERMINAL OF RECORD (SL-1b' pinned to the MASS form) AND ITS
> PROVED CONSTRAINTS, on the admissible object (the [S, S-R, R+1]_p
> negacyclic GRS code on the half-system of mu_{2^{e_p}},
> S = 2^40/e, R/S = 1/log2 p, p >= 2^39; Z(L) = Z_1^C, C <= 4).

`:17-19`:

> **THEOREM Z-FLOOR (pointwise first-moment floor).** For EVERY
> F_p-subspace, Z(L) = sum_{eps in L^perp cap T} 2^{-wt(eps)} >=
> 2^m / p^{dim L}.

`:46-53` (the knife edge):

> **THE KNIFE EDGE.** At k = e the Z-FLOOR is silent by 46.02 bits
> out of 2.75e11 under the banked R = ceil(t/2) reading — ONE Lambda
> condition, worth log2 p = 64 bits — and FIRES at +17.98 bits under
> the exact-balance reading (in which case ternary kernel vectors
> provably exist at the witness row: Z_1 >= 2^{17.98}, the EXACT-ZERO
> form of the terminal is dead, yet Z = 2^{o(n)} so the MASS form
> survives).

The window is ALL-ODD and shift-0 — `notes/pilots_20260806/z1_ternary_mass/PROOFS.md:87-93`
(the verified hypothesis table) gives `P(omega^{2j-1}) = 0, j = 1..ell`
with `Lambda = {odd l : l <= t}` starting at `l = 1`, and
`omega` of exact order `2N`, `N = 2^38 = S`.

The generating classes — `background/nodes/f2_o1_status_split/statement.md:50-54`:

> E_{c in K1(Lambda)}[T_W(c)] = 2^{n/2}·Z_1^e EXACTLY, on
> (e_p, e) in {(>=41,1), (40,2), (39,4)} with e·log2 p < 256, coset
> droppable by C1, Z_1 the ternary mass of the negacyclic prime-field
> GRS code [S, S-R, R+1]_p on the half-system of mu_{2^{e_p}}

**I2** — `background/nodes/crossing_dsa_refutation/statement.md:28-33`:

> **LEMMA TC (the corrected pricing).** The stratum's primitive object
> is eps in {0,±1}^L — 3^L, NOT 2^{n_a} (the global functional, which
> requires log2 p >= 256 = the cap) and NOT C(n_a, r'_a) (the retired
> per-weight functional, 48.75 bits mis-priced). Requirement at
> v = 34: 202.875 (194.875 orbit-corrected, LEMMA ROT: relations come
> in orbits of size 2L; Poisson estimates over-predict by 2L).

`:35-41` (THEOREM DSA) and `:52-56`:

> **THE DICHOTOMY.** e = 1 prime rows are NEVER in the DSA regime:
> B* >= 3 forces log2 p >= 129.585 > 126. The recorded prize rows are
> untouched and RE-PRICED (HEURISTIC, labelled): expected relation
> count 3^128/p = 2^{-53.1}, orbit-corrected 2^{-61.1} — a 53-61 bit
> margin replacing the 0.089-bit global-functional cliff.

**I3** — `background/nodes/es_ternary_suppression_instruments/statement.md:55-58`:

> (E-2) CC-sparsity IS the (ES) shape
> again, at half length over the ternary alphabet — not a smaller
> lemma;

LEMMA AB — `notes/pilots_20260806/efloor_sparsity/PROOFS.md:88-97`:

> **LEMMA AB.** Write `f_S = A + X^h B` with `deg A, deg B < h = n/2`, i.e.
> `A` is the indicator of `S n [0,h)` and `B` that of `S n [h,n)` shifted.
> Put `v := A - B in {-1,0,1}^h`. Then
> 1. `f_S = v (mod Phi_n)`, so for every **odd** `s`,
>    `f_S(xi^s) = v(xi^s)` for any primitive `n`-th root `xi` in char `p`;
> 2. `v = 0  <=>  S + n/2 = S  <=>  strat(S) >= 1`, for every odd `p`;
> 3. the number of `S` with a given `v` is exactly `2^{z(v)}`, where
>    `z(v) = #{i : v_i = 0}`.

and the object, `efloor_sparsity/PROOFS.md:300-302`:

> Let `C_odd(n,p,w) := { v in F_p^h : v(xi^s) = 0 for all odd s in [1,w-1] }`,
> a cyclic (negacyclic) code of length `h` and codimension
> `deg G = delta * #{<p>-cosets met by the odd window}.`

---

## §1. PROPOSITION NEG — the master object (A1, registration P1)

**PROPOSITION NEG.** Let `p` be odd, `N` a 2-power, `theta` of exact
multiplicative order `2N` over `F_p`, and

```text
  M(N, c, p) :=  { eps in {0,±1}^N  :  sum_j eps_j theta^{(2i-1)j} = 0,
                                       i = 1..c }
```

Then `M` is exactly the ternary part of the **negacyclic** code of length
`N` over `F_p` whose zeros are the first `c` ODD powers of `theta`, and
I1, I2, I3 are each EXACTLY `M(N,c,p)` at

| inst | `N` | `c` | `theta` | source |
|---|---|---|---|---|
| I1 | `S = 2^40/e` | `R` | `omega`, order `2N = 2^{e_p}` | knife_edge:12-15; z1 PROOFS:87-93 |
| I2 | `L = 2^{41-v}` | `delta_a = ord_{2L}(p)` | `theta`, order `2L` | dsa:28-41 |
| I3 | `h = n/2 = 2^40` | `ceil((w-1)/2)` | `xi`, order `n = 2h` | AB:88-97; efloor PROOFS:300-302 |

*Proof.* In each case the root of unity has order exactly TWICE the vector
length, so `theta^N = -1`; hence for ODD `s`, evaluation at `theta^s` kills
`X^N + 1`, and the ambient algebra is `F_p[X]/(X^N+1)`. I3's is written out
in the source (`Phi_n(X) = X^h + 1`, es_coprimality/PROOFS.md:11-22). In each
case the window is a run of consecutive odd exponents starting at 1
(I1: `Lambda = {odd l : l <= t}` from `l = 1`; I2: the single exponent 1;
I3: odd `s` in `[1, w-1]`). ∎

**The three brief-listed disanalogies (ii) and (iv) are ABSORBED.** (ii) the
condition count is the free parameter `c` (`4.3e9` vs `1`); (iv) "half-system
vs theta-powers vs cyclic" is one structure in three notations — all three
are evaluation at odd powers of a primitive `2N`-th root.

**Scope caveat (verified, §6 of verify.py).** Negacyclicity requires the
window to be ALL-ODD. On mixed-parity windows the negacyclic shift does NOT
close the code (even-index conditions evaluate `X^N` to `+1`, odd ones to
`-1`; no single algebra `X^N ± 1` carries both). Verified non-vacuously at
`N = 16, p = 97`: all-odd `{1}`, `{1,3}` closed; MIXED `{1,2}` (4796 nonzero
codewords) and `{1,2,3}` (52) NOT closed; all-even `{2,4}` (4368) not closed.

---

## §2. PROPOSITION FIB — the obligations are one functional
##      (A1 disanalogies (i) and (iii), both REFUTED as stated)

The brief asserts *"(iii) I2's eps arises as a DIFFERENCE of binary
indicators (fibred, LEMMA TC), I1's ternary vectors are native"*
(PREREG.md:46-48). **This is FALSE.** I1's ternary vectors are fibred too,
and the `2^{-wt}` weight IS the fibre size.

`notes/pilots_20260806/z1_ternary_mass/PROOFS.md:141` defines

> for `s in F_p^d` put `F_s = {b in {0,1}^m : Ab = s}`

and `:144-155`:

> ```
>    sum_s |F_s|^2 = #{(b,b') in {0,1}^m x {0,1}^m : Ab = Ab'}
>                  = #{(b,b') : b - b' in ker A}.
> ```
> Every difference `b - b'` lies in `T = {0,±1}^m`, and for a FIXED `eps in T`
> the number of pairs with `b - b' = eps` is `2^{m - wt(eps)}`

So `eps = b - b'` is a difference of two BINARY vectors, and
`2^{m-wt(eps)}` is the number of binary preimages.

**PROPOSITION FIB.** All three obligations are the statement
`Phi(C; mu) = (the eps = 0 term) x (1 + delta)`, where
`Phi(C; mu) = sum_{eps in C cap T} mu(eps)` and `mu(eps)` is the number of
binary preimages of `eps` in the instance's binary domain:

| inst | binary domain | `mu(eps)` | `Phi` | target |
|---|---|---|---|---|
| I1 | full cube `{0,1}^m` | `2^{m-wt(eps)}` | `2^m Z(L)` | `delta <= 2^{o(m)}` |
| I3 | full cube `{0,1}^n` (via `S`) | `2^{z(v)} = 2^{h-wt(v)}` | `#{S : conds}` | `delta = 0` |
| I2 | constant-weight slice `|S'| = r'_a` | `C(L-U, (r'_a-U)/2)` | `|W_w|` | `delta = 0` |

I1 and I3 have the SAME `mu`: `2^{h-wt}` (LEMMA AB clause 3) is
`2^h` times I1's `2^{-wt}`. I2's is a binomial, because the crossing lane
fixes the weight (`|T| = r'` in (ES), `r'_a = L-2` in LEMMA DS).

**Consequence — the real split is not (i)/(iii) but CONSTANT-WEIGHT vs
FULL-CUBE.** Disanalogy (i) (mass vs existence) and (iii) (fibred vs native)
are the same phenomenon seen twice, and they resolve each other: I1's "mass"
IS a count, of binary pairs. What genuinely differs is the binary domain
(full cube for I1, I3; a constant-weight slice for I2), hence the fibre
weight.

---

## §3. THEOREM PT — the criticality coordinate and the phase transition
##      (A2 + A4; the load-bearing disanalogy)

For `M(N,c,p)` put

```text
   tau   := c log2 p / N            B := N(1 - tau)          Tcrit := N(log2 3 - tau)
```

`B` is exactly `log2` of THEOREM Z-FLOOR's floor (`2^N/p^c`), so Z-FLOOR is
informative iff `tau < 1`; `Tcrit` is the `log2` first-moment count of
nonzero ternary codewords (`3^N/p^c`), so they are expected present iff
`tau < log2 3 = 1.58496`.

**THEOREM PT.** On their live rows,

| inst | `tau` | `B` (bits) | `Tcrit` (bits) | regime |
|---|---|---|---|---|
| I1 (any admissible row) | `1` | `-46.02` | `+0.585 * 2^38` | **SUPER**critical |
| I2 (`v=34`, `e=1` prime) | `2` | `-128` | `-53.125` | subcritical |
| I3 (`w=2^34`, official) | `2` | `-2^40` | `-0.415 * 2^40` | subcritical |

**I1 sits at `tau = 1` identically, and this is FORCED**, not incidental: the
saturation pin `R/S = 1/log2 p` (THEOREM Z-NOGO) says exactly `c log2 p = N`.
Equivalently `R log2 q = m = n/2` up to the `R = ceil(t/2)` rounding, which is
why the residue is `< log2 q` bits and is *e-independent* — verified at both
`e = 4` and `e = 1`.

**Verification that the coordinate is the right one, not numerology.** It
reproduces four banked constants it was not fitted to (verify.py §1):

- I1 knife edge `B = -46.0249` vs banked `-46.02`; the exact-balance
  reading (one Lambda condition fewer) `+17.9751` vs banked `+17.98`; the
  step between them `63.999999 = log2 p` vs banked "worth log2 p = 64 bits".
- `Tcrit(I1) = 0.584963 * 2^38` vs CATCH-Z1's `(3/2)^S = 2^{0.585*2^38}`.
- `3^128 = 2^202.8752` vs LEMMA TC's `202.875`.
- `Tcrit(I2) = -53.1248` vs banked `2^{-53.1}`; orbit-corrected
  `-61.1248` vs banked `2^{-61.1}` (the correction is `log2 2L = 8`).

**COROLLARY PT-1 (the pun's exact location).** I1 and {I2, I3} lie on
OPPOSITE sides of the ternary counting threshold. No single monotone target
statement specializes to both obligations: at I1 the solution set is
astronomically populated (`2^{+6.4e11}` expected at the shared row), so only
a MASS bound can be true; at I2/I3 it is expected empty, so EMPTINESS is the
meaningful target. **This is why CATCH-Z1 had to re-pin the F2 terminal to the
mass form** — the re-pin is forced by `sign(Tcrit)`, not by taste.

**COROLLARY PT-2 (new, and campaign-relevant).** In I3's own coordinate the
threshold is `w_tern = log2(3) * 2^33 = 2^33.66445`. The crossing bracket's
lower endpoint `w = 2^34` clears it by only **0.336 bits**. In I2's
coordinate, one step below the bracket (`v = 33`, `L = 256`) gives `tau = 1`
and `Tcrit = +149.75` — i.e. the deep-stratum ternary count would be
SUPERCRITICAL at the RECORDED PRIME ROWS, not merely at tower rows. The
crossing lane's obligation is therefore true (if it is) by a 0.336-bit margin
in `w` at its hardest end.

---

## §4. THEOREM SR — the shared admissible row (A2; the anti-(ES) result)

The (ES) collapse was a REGIME failure —
`background/nodes/esg_lane_rescope/statement.md:12-18`:

> THE (ES-G) TERMINAL RE-SCOPE OF RECORD: the round-15 "unified
> terminal of four lanes" is WITHDRAWN — the four lanes' field
> regimes are MUTUALLY UNSATISFIABLE ... No single row satisfies
> all four; the unification was of statement SHAPE, not regime.

**THEOREM SR.** The three ternary instances' admissibility predicates are
SIMULTANEOUSLY SATISFIABLE. Any prime `p` with

```text
   v_2(p-1) = 41,     log2 p in [255.9113, 256)
```

is admissible for all three at once: for I1 it is the `e = 1` generating
class (`ord_n(p) = 1 = e`, `e_p = 41`, so `S = 2^40 = 2^40/e`,
`e log2 p < 256`) — `f2_o1_status_split/statement.md:50-54`; for I2 it is a
recorded `e = 1` prime row with `B* = floor(q/2^128) >= 3`, provably OUTSIDE
the DSA regime so the crossing question is OPEN there —
`crossing_dsa_refutation/statement.md:52-56`; for I3 it is the official row
`q` prime with `v_2(q-1) >= 41` — `efloor_sparsity/PROOFS.md:545-550`.
Existence is unconditional (Dirichlet/PNT for `1 mod 2^41`). Explicit
exhibit (Miller-Rabin, 40 fixed bases), chosen inside the prize-max sliver
`log2 Q in [255.9113, 256)` of `u2c_giant_tnull_dichotomy/statement.md:16-17`:

```text
p = 108887375294690666722882806605166818982732176609682603652941949788724960165889
```

**So A2 does NOT reproduce the (ES) failure.** Unlike (ES), a common row
exists and is explicit.

**But there is NO SHARED DISCHARGE.** On that very row the three instances
sit at `tau = 1, 2, 2` with `Tcrit = +6.43e11, -53.1, -4.56e11` bits.
Regime-compatible, criticality-incompatible. **This is a failure mode the
(ES) post-mortem did not register**, which is why I registered
CRITICALITY-COMPATIBILITY as a third gate (PREREG §9).

**CATCH-19-ADV-1 (against the brief).** PREREG.md:61 states *"I1 lives at
k = e generating rows, p ~ 2^39-2^64"*. The `2^64` upper end is UNSOURCED —
no node pins it. The banked pins are `p >= 2^39`
(`f2_z1_mass_knife_edge/statement.md:15`) and `e log2 p < 256`
(`f2_o1_status_split/statement.md:50-54`), which at `e = 1` admit
`p` up to `2^256`. `2^64` is the *witness row's* prime
(`f2_adm/REPORT.md:10`, `e = 4`), not a family bound. The brief's own
premise for A2's disjointness is therefore wrong, and in the direction
FAVOURABLE to the unification.

---

## §5. THE TRANSFER MATRIX (A3), with exact hypothesis matching

`.` = the instrument's home instance.

| instrument | I1 | I2 | I3 |
|---|---|---|---|
| **Z-FLOOR** | . | APPLIES, VACUOUS | APPLIES, VACUOUS |
| **Z-1 / D1** | . | APPLIES, yield `3` | APPLIES, yield `w+1` |
| **Z-NOGO** | . | APPLIES (no-go) | APPLIES (no-go) |
| **LEMMA ROT** | APPLIES (`2N`) | . | APPLIES (`2h`) |
| **DSA** | FAILS by 2 bits | . | FAILS by `2^40` bits |
| **CS** | FAILS (hyp) + vacuous | binary parent | . |
| **SP-COVER/UNIFORM** | FAILS by 9 bits | FAILS by 41 bits | FAILS by 3 bits |

**Z-FLOOR → I2, I3.** Hypothesis match is TOTAL: `z1_ternary_mass/PROOFS.md:130-136`
states it *"For **every** `F_p`-subspace `L ⊆ F_p^m` (no MDS, no GRS, no
genericity, no randomness)"*. So it transfers verbatim. Its CONTENT is null:
the floor is `2^B` with `B = -128` (I2) and `-2^40` (I3), both `< 1`, while
`eps = 0` already contributes `1`. **Vacuity is exactly `tau > 1`** — the
transfer fails for the reason THEOREM PT names.

**Z-1/D1 → I2, I3.** The four banked hypotheses
(`z1_ternary_mass/PROOFS.md:87-93`) are: `char F > w`; `omega` of exact order
`2N`; exponents distinct in `{0..N-1}`; and the window a run of consecutive
odd exponents from `l = 1`. §1 verified all four for I2 (`c = 1`) and I3
(`c = ceil((w-1)/2)`). Yield `2c+1`: for I2 that is `3` — TRUE but elementary
(`theta^i = ±theta^j` is impossible for `0<=i,j<L`); for I3 it is
`2*2^33+1 = w+1`, a genuine factor-2 improvement on the naive half-length BCH
bound `2^33+1`. Verified on every 2-power toy (verify.py §3, 24 grids,
449,208 codewords, min weight `>= 2c+1` throughout).
**The instrument's yield is proportional to `c`, the very parameter that
differs by `2^32` across the instances.**

**LEMMA ROT → I1, I3.** `crossing_low_w/PROOFS.md:330-332` needs only that
the relation set be closed under `eps -> -eps` and the twisted rotation of
order `2L` — i.e. exactly negacyclicity. By PROPOSITION NEG all three are
negacyclic (all-odd windows), so ROT transfers verbatim with orbit constant
`2N`: `2^{e_p}` for I1, `n = 2^41` for I3. Verified (verify.py §3, §6).
Numerically: the correction is `41` bits against `Tcrit` of `6.4e11` (I1) and
`-4.6e11` (I3) — real but negligible. On the toys the correction is
*measurable*: it improves the calibration from 22/24 to 23/24, and the single
residual miss sits at a 0.56-bit margin.

**DSA ↔ Z-FLOOR (P6 — the strongest cell).** DSA's engine is
*"pigeonhole (|domain| > |codomain|)"* (`crossing_low_w/PROOFS.md:404-405`)
on `2^{L-2}` binary vectors mapping to `F_{p^{delta_a}}`; two collide and
their DIFFERENCE is ternary. That is the SAME collision that defines
`sum_s |F_s|^2` in Z-FLOOR's proof (§2). **DSA = Z-FLOOR's existence
corollary + support control** (`-2` bits, from restricting to a subcube to
force `U <= r'_a`). Hypothesis `p^{delta_a} < 2^{L-2}` is exactly
`tau < 1 - 2/N`. Verified on toys: every grid with `p^c < 2^{N-2}` produced a
nonzero ternary codeword supported in the first `N-2` coordinates, and every
grid with floor `> 1` produced a nonzero codeword.
**Applied to I1, DSA fails by EXACTLY 2 bits** — because saturation puts I1 at
`tau = 1` identically. I1's 46-bit knife edge and I2's DSA boundary are the
SAME boundary.

**CS → I1: FAILS twice.** (a) As banked, its hypotheses are a 0/1 indicator
SET (`S <= Z/n` with `|S| = r'`, `x_1 != 0`) and a char-0 ideal norm in
`O_K = Z[zeta_n]` (`es_coprimality/PROOFS.md:202-225`); I1's object is
ternary and in char `p`. (b) Even granting the natural ternary extension
(`r' -> U`, the ternary support), CS4 reads `c log2 p > (N/2) log2 U`. At I1
saturation gives `c log2 p = N` exactly, so the condition collapses to
`U < 4` — **PROVABLY VACUOUS** (verified: `U < 4.000000`). Against Z-1's
`2R+1 = 8,589,934,681` that is 9 orders of magnitude short.

**SP-COVER/SP-UNIFORM → all three: FAILS, for ONE shared reason.**
`v_2(p-1) >= 41` and `p` odd force `v_2(p^2-1) >= 42`, so LEMMA COS/
SP-UNIFORM need an odd window reaching `2^42`. I1's window top is `~2^33`
(short 9 bits), I3's `<= 2^39` (short 3 bits), I2's is `2^1` (short 41).
**CATCH-19-ADV-2:** CATCH E-3 is banked as an (ES)/E_floor-lane defect
(`es_ternary_suppression_instruments/statement.md:57-62`). It is not — it is a
property of the SHARED ROW: the official smooth-domain gate `v_2(q-1) >= 41`
blind-spots SP-COVER in ALL THREE instances simultaneously.

**Consistency cross-check (a null, reported).** Z-FLOOR firing at `+17.98`
together with Z-1's min weight `2R+1` forces `>= 2^{8.59e9}` ternary
codewords at I1; `3^S = 2^{4.36e11}` is available and the first moment
predicts `2^{1.61e11}`. Consistent — no instrument pair is in conflict.

---

## §6. LEMMA ZB — CATCH-Z6 promoted to a proof (A4, P11)

**LEMMA ZB (the Z-basis property).** A `p`-INDEPENDENT ternary relation of
length `N` at `2N`-th roots is a ternary `v` of degree `< N` with
`Phi_{2N} | v` over `Z`. At 2-power `2N`, `Phi_{2N}(X) = X^N + 1` has degree
exactly `N`, so no nonzero `v` of degree `< N` is divisible by it: **there are
none**. At composite `2N`, `deg Phi_{2N} = phi(2N) < N` leaves room. ∎

Verified, and CATCH-Z6's exact counts reproduced (verify.py §4):
`2N = 8, 16, 32` → 0 relations; `2N = 12` → 8 (min weight 3); `2N = 20` → 8;
`2N = 24` → 80. Compare `z1_ternary_mass/REPORT.md:35`: *"`2N=12` → 8 common
vectors of min weight 3; `2N=20` → 8; `2N=24` → 80 ... (`2N=8,16` → 0, the
`Z`-basis property)"*.

**All three instances sit at 2-POWER `N` in their live regimes**
(I1 `S = 2^40/e`; I2 `L = 2^{41-v}`; I3 `h = 2^40`), hence all three are
structurally immune. **A4 finds NO disanalogy on the length axis** — this
axis is a shared positive.

---

## §7. THE GRADED VERDICT

- **OBJECT unification: SURVIVES (proved, §1).** Exactly the ternary part of
  a negacyclic `F_p`-code with an all-odd shift-0 window; stronger and more
  specific than the round-18 phrase "ternary vectors in p-ary codes from
  cyclotomic windows".
- **REGIME unification: SURVIVES as SATISFIABILITY (proved, §4), with NO
  shared discharge.** An explicit common admissible row exists — the exact
  opposite of (ES)'s mutual unsatisfiability — but the instances sit at
  `tau = 1, 2, 2`, so no instance's answer constrains another's.
- **METHOD unification: SURVIVES (§5), and is currently INERT.** Four
  instruments transfer with exact hypothesis matches (Z-FLOOR, Z-1/D1,
  Z-NOGO, ROT), one identification is proved (DSA = Z-FLOOR's corollary +
  support control), and one obstruction is shared (SP-COVER's blind spot).
  Every transferred instrument is provably vacuous or insufficient at its
  target's live `tau`. Real, but it has not yet moved any obligation.
- **STATEMENT unification: SURVIVES ONLY AS A SCHEMA; KILLED as a
  theorem-unification (§2, §3).** PROPOSITION FIB writes a single
  parametrized statement whose specializations ARE the three banked
  obligations exactly, so the brief's registered A1 test is PASSED. But the
  target parameter `delta` is NOT free: it is pinned by `sign(Tcrit)`, and
  CATCH-Z1 proves the two settings have OPPOSITE truth values at one object.
  A schema that classifies without implying is a taxonomy, not a theorem.

**Methodological finding (offered for adoption).** The registered A1 test —
"is there one parametrized statement whose specializations are the
obligations exactly?" — is PASSABLE BY A TAXONOMY, and A2 as registered
(regime disjointness) is not the only regime failure mode. The gate that
actually separates this candidate's real content from its decoration is
CRITICALITY-COMPATIBILITY: *do the instances lie in a common `tau`-interval
on which the instruments are non-vacuous?* Here they do not.

---

## §8. Catches, subtraction, residuals

**Catches raised.**
- **CATCH-19-ADV-1** — the brief's `p ~ 2^39-2^64` for I1 is unsourced; the
  banked pins admit `p` up to `2^256` at `e = 1` (§4).
- **CATCH-19-ADV-2** — CATCH E-3 is a SHARED-ROW property, not an
  (ES)-lane defect (§5).
- **CATCH-19-ADV-3** — the brief's disanalogy (iii) ("I1's ternary vectors
  are native") is FALSE; they are differences of binary vectors and the
  `2^{-wt}` weight IS the fibre size (§2). The real split is
  constant-weight vs full-cube.
- **CATCH-19-ADV-4** — I4 is not an independent instance: LEMMA TC's `3^L` is
  the CARDINALITY of I2's ambient ternary cube, and LEMMA TC is a CROSSING
  lemma, not a band one. Counting it as a fourth instance inflates 3 to 4 —
  the same inflation that made "(ES) discharges all four consumers"
  attractive (`mun_anticoncentration/REPORT.md:53`).
- **CATCH-19-ADV-5 (process)** — the round-19 quarantine is POROUS. My
  subtraction sweep, searching only outside the quarantined dirs, recovered
  the sibling's headline results from
  `notes/pilots_20260802/CAMPAIGN_LEDGER.md:1815-1875`.

**Subtraction (prior art) — what is NOT novel.**
- The `(3/2)^S` count and the `1/log2 3 = 0.6309` saturation ratio are
  ALREADY BANKED: `z1_ternary_mass/PROOFS.md:487-489`;
  `f2_adm/PROOFS.md:518-521`; and the threshold pair itself at
  `notes/pilots_20260804/f2_sl1_powersums/PROOFS.md:296-298`.
- Z-FLOOR ≡ DSA, the shared negacyclic frame, and the `2^{z(v)}` ≡ `2^{-wt}`
  identification are ABSENT from the open surface but ALREADY BANKED by the
  quarantined sibling per `CAMPAIGN_LEDGER.md:1820-1822`, `:1847-1851`,
  `:1860-1864`. **I claim no novelty for them.** Their value here is as
  INDEPENDENT CONFIRMATION: my `-46.0249 / +17.9751` were computed and logged
  before the subtraction sweep ran, and the ledger records the sibling
  reproducing the same two constants to four decimals.
- Genuinely ABSENT from the whole repo: the Z-1 transport to `C_odd`
  (min weight `w+1`, §5); COROLLARY PT-2 (the `0.336`-bit bracket margin and
  the `v = 33` supercriticality, §3); CATCH E-3 as a shared-row property.

**Honest residuals.**
1. `Tcrit` is a FIRST MOMENT. It is a heuristic for presence/absence, exactly
   as the banked `3^128/p = 2^{-53.1}` re-pricing is labelled HEURISTIC. The
   PROVED half is the `tau < 1` side (Z-FLOOR/DSA pigeonhole).
2. The toy sweep calibrates only. Per
   `f2_z1_mass_knife_edge/statement.md:68-69`, no toy is evidence about any
   official row. The structural results (§1, §2, §6) are algebraic identities,
   not extrapolations.
3. The Z-1 → I3 transport gives `w+1` against a length of `2^40`: seven orders
   short of CC-sparsity. It is an improvement, not a route.
4. The shared-row exhibit is a Miller-Rabin probable prime; the EXISTENCE
   claim rests on Dirichlet/PNT, not on the exhibit.
5. The ternary extension of CS (used only to prove CS vacuous at I1) is not
   proved; if someone proves it, §5's verdict is unaffected — it is vacuous
   there either way.
6. I did not test I2's constant-weight fibration against a constant-weight
   version of Z-FLOOR. That is the one cell where a genuinely new instrument
   might exist.
