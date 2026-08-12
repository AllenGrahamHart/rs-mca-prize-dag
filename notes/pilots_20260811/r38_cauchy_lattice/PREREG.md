# PREREG — r38_cauchy_lattice (round 38)

Coordinator brief. Constraints: CONSTRAINTS.md in this dir (binding).
AUDIT-AND-DRAFT: any surgery stays coordinator-gated.

## Anchors (read these two FIRST, then register blind priors)

1. `notes/pilots_20260811/r37_third_solve/REPORT.md` (round 37)
2. `background/nodes/l1_exact_shell_balanced_shifted_lattice_reduction/statement.md`

## Mandate

THE CAUCHY-LATTICE ATTEMPT. Round 37 proved the third split
prescription is not an exact solve in (PAR) coordinates: it is
the condition that the FIRST MINIMUM of an explicit rank-2
F_q[x]-lattice ({(f,g) : f == R g mod P_0 P_inf}, deg P_0 P_inf
= 14) DROPS from its generic 7 to <= 4 — an overdetermined
type-(4,4) Cauchy interpolation, deficit 3, with an exact O(1)
test (one extended Euclid) and no known inverse. The banked
lattice-reduction machinery lives in the l1 lane (anchor 2) and
the xr syzygy router. YOUR JOB: attack the inverse. Either (a) an
ALGORITHM: exploit structure (the values t(x) are not arbitrary —
they come from (PAR) objects; S_0, S_inf are split subsets of
mu_32; the lattice varies ALGEBRAICALLY as the subsets move) to
find minimum-dropping triples faster than the q^3-blind rate —
any factor turns T=3-over-mu_32 from unreachable (8.9e3x short)
to reachable; or (b) a CHARACTERIZATION: which (S_0, S_inf, S_1)
triples admit the drop (an exact criterion in the (SCRIT) mold —
even a necessary condition prunes the search); or (c) a WALL: a
proof that the drop locus has no exploitable structure (state
what "no structure" means precisely). ALSO: the a* CONVENTION IS
RULED (coordinator, this launch): a* is PROJECTIVE — members are
degree-rho forms on P^1, roots at infinity counted (it reproduces
the banked 13 and preserves PGL_2-covariance of (PAR)). Under the
ruling, measure a* on every T >= 2 object you or prior rounds
built (regenerate as needed) — the first real F1 dataset.

## Deliverables

**D1 — THE LATTICE, STRUCTURED.** The Euclid trajectory of
(R, P_0 P_inf): the drop <=> a quotient-degree pattern (the
minimum's degree profile = the gap structure of the continued
fraction). Derive: how does the trajectory vary as ONE point of
S_1 moves? As S_1 is swapped wholesale? Is there a
divide-and-conquer (half-gcd) incremental update making a sweep
over all C(25,7) admissible S_1 cost near-linear amortized? (The
exact test is O(1) each; the question is beating enumeration by
structure, or organizing enumeration so it IS feasible:
C(25,7) = 480,700 tests/pair at q=97 — ALREADY within a ramguard
window if each test is microseconds. DERIVE THE REAL COSTS FIRST;
the blind-rate pessimism may be wrong about exhaustive-per-pair.)

**D2 — THE PUSH.** Execute the best instrument from D1 at
q = 97 and 193: sweep (S_0, S_inf) pairs (100%-s=0 via (SCRIT)'s
restriction; the bespoke double solve supplies the pairs), test
all admissible S_1 per pair. ANY T = 3 over mu_32 is the first
of its kind — full certification + a* under the ruling + push
toward T = 4 (the negative-exponent cell). If the sweep
exhausts without a hit, that is the first EXHAUSTIVE statement
about T = 3 over mu_32 on the reachable sub-locus — state its
scope exactly.

**D3 — F1 UNDER THE RULING.** a* (projective) on every T >= 2
object available; the distribution vs 7m-1 = 13; the supported-
pair overlap structure. Zero-power declared where the sample is
what it is — but this is the first F1 data with a fixed
convention.

**D4 — VERDICT.** Solve/characterization/wall status; the T
record; misses first; cross-pilot flag (do NOT read siblings).

## Blind priors to register

P(an exhaustive-per-pair sweep is feasible), P(T = 3 over mu_32
this round), P(a criterion in the (SCRIT) mold lands), P(the
Euclid trajectory admits incremental update), expected max T
over mu_32 (a number), P(a* = 13 dominates under the ruling).

---

## Pilot registrations

Written after reading EXACTLY the two named anchors
(`notes/pilots_20260811/r37_third_solve/REPORT.md`,
`background/nodes/l1_exact_shell_balanced_shifted_lattice_reduction/statement.md`)
and BEFORE any other read, any grep, any `ls`, and any interpreter
invocation. Appended with the Edit tool in two calls.

### R0 — notation (from the anchors alone)

`q ∈ {97,193}` (both have `32 | q−1`); `mu_32 ⊂ F_q^*` the 32nd roots
of unity; `rho = 7`, `m = 2`, `A = 3`, `N = 32`. `(PAR)` (anchor 1,
`REPORT.md:64-69`): the length-4 sequence `(u_0,u_1,u_2,u_3) =
(k,f,g,−h)`, `deg f = deg g = deg h = deg k = 4`, `deg L = 1`, and
`L·Q_z = (f+zg)^2 − (k+zf)(g−zh)`, so `L(Q_2,−Q_1,Q_0) = −(row_0 ×
row_1)` of the 2×3 Hankel matrix. Members `Q_0` (slope 0), `Q_2`
(slope ∞), `Q_0+Q_1+Q_2` (slope 1) after Möbius re-basing to
`{0,1,∞}`. Prescriptions `Q_0 = αP_0`, `Q_2 = γP_inf`,
`Q_0+Q_1+Q_2 = βP_1` with `P_S = prod_{x∈S}(X−x)` monic, `S ⊂ mu_32`,
`|S| = 7`. `T` = number of members split over the stated domain;
`T_mu32` and `T_bespoke` are NEVER merged (anchor 1 MISS 3). `F := f+g`.
`e(i,j) = |S_i ∩ S_j|`. `(SCRIT)`, `(CONIC)`, `(SLOT)`, `(OV4)` as in
anchor 1. Anchor 2 supplies the shifted-lattice vocabulary: `M_U`
free of rank 2, shifted weak-Popov basis with `d_1 ≤ d_2`,
`d_1+d_2 = deg(modulus)` `(BL2)`, `sdeg` `(BL1)`.

### R1 — execution order

D1 (derive real costs BEFORE any pessimism) → D2 (the push) → D3
(a* under the ruling) → D4 (verdict). Misses reported first.

### Falsifiable derivations, each with its falsifier

**(X1) THE POINTWISE THIRD-MEMBER CONDITION.** Reducing `(SLOT)` at
the prescribed points, with `F = f+g`, the third prescription is
EXACTLY the pair of pointwise systems

```text
  x ∈ S_0   :   γ P_inf(x) F(x) = β P_1(x) g(x)        (T0)
  x ∈ S_inf :   α P_0(x)  F(x) = β P_1(x) f(x)        (Tinf)
```

(derivation: on `S_0`, `f/g = Q_1/Q_2 = (βP_1−γP_inf)/(γP_inf)`; on
`S_inf`, `f/g = Q_0/Q_1 = αP_0/(βP_1−αP_0)`). **Falsifier:** any
`(PAR)` object with three split members violating `(T0)` or `(Tinf)`
at any point where `f(x)g(x) ≠ 0`.

**(X2) THE SCALES ELIMINATE — A 2×5 HANKEL MOMENT KERNEL.** Put
`G := (β/γ)g`, `H := (β/α)f`. Then `(T0)` reads
`P_inf(x)u(x) = P_1(x)G(x)` on `S_0` with `u := F`, and `(Tinf)`
reads `P_0(x)u(x) = P_1(x)H(x)` on `S_inf`. Since `deg G ≤ 4` and
`|S_0| = 7`, the 7 values `s_x u(x)`, `s_x = P_inf(x)/P_1(x)`, must be
interpolated by a degree-`≤4` polynomial — exactly 2 linear
conditions on `u`. I derive these to be the kernel of a **2×5 Hankel
matrix of moments**:

```text
  m_j = sum_{x in S_0} P_inf(x) x^j / (P_1(x) P_0'(x)),  j = 0..5
  A := pi_u(W_0) = ker [[m_0..m_4],[m_1..m_5]]   (dim 3 generically)
  n_j = sum_{x in S_inf} P_0(x) x^j / (P_1(x) P_inf'(x)), j = 0..5
  B := pi_u(W_inf) = ker [[n_0..n_4],[n_1..n_5]]  (dim 3 generically)
```

**No scan over `(λ,μ) = (β/γ, β/α)` is needed.** **Falsifier:**
`dim A ≠ 3` generically, or a `u ∈ A` whose 7 values `s_x u(x)` are
NOT degree-`≤4`-interpolable, or a genuine solution whose `u ∉ A∩B`.

**(X3) (TEST) — AN EXACT SCAN-FREE `O(1)` CRITERION, CODIMENSION 3.**
`A, B ⊂ F_q^5` are 3-dimensional, so `A ∩ B` is 1-dimensional
generically: **`u` is determined up to scale by `(S_0,S_inf,S_1)`
alone.** Recover `G` (resp. `H`) as the degree-`≤4` interpolant of
`s_x u(x)` on `S_0` (resp. of `P_0(x)u(x)/P_1(x)` on `S_inf`). Then

```text
  (S_0,S_inf,S_1) admits a T=3 object  <=>  rank[u;G;H] <= 2
                                        (3x5 matrix)  ... (TEST)
```

because `u = F = f+g = (1/λ)G + (1/μ)H`. `rank ≤ 2` on a 3×5 matrix
is codimension `(5−2)(3−2) = 3` — **matching the banked deficit 3 /
`q^{-3}` per triple exactly, from a completely different route.**
Reconstruction: `u = c_1G + c_2H` gives `g = c_1G`, `f = c_2H`,
`β = 1`, `γ = c_1`, `α = c_2`. **Falsifier:** a triple passing (TEST)
that admits no object, or an object whose triple fails (TEST); or a
measured hit rate outside `[0.5, 2]×q^{-3}` on ≥ 3e6 triples.

**(X4) `L`, `h`, `k` ARE AUTOMATIC.** `(CONIC)` gives
`L = (Q_0g^2 − Q_1fg + Q_2f^2)/(Q_0Q_2)`; the numerator vanishes on
`S_0` (because `Q_2f − Q_1g = 0` there by `(T0)`) and on `S_inf` (by
`(Tinf)`), so `L` is automatically a polynomial of degree `≤1`; then
`f | (LQ_2 − g^2)` and `g | (f^2 − LQ_0)` follow from `(CONIC)` mod
`f` and mod `g`. **So the 14 pointwise conditions are SUFFICIENT, not
merely necessary** — anchor 1 only claimed necessity.
**Falsifier:** a (TEST)-passing triple whose reconstructed `L` is not
a degree-`≤1` polynomial, or whose `h` or `k` is not a polynomial.

**(X5) THE EUCLID/CONTINUED-FRACTION CHARACTERISATION.** For the
rank-2 lattice `{(f,g) : f ≡ Rg mod P_0P_inf}`, `deg P_0P_inf = 14`:
with remainder sequence `r_{−1}=P_0P_inf, r_0=R, …` and cofactors
`v_i` obeying `deg v_i = 14 − deg r_{i−1}`, the first minimum is
`d_1 = min_i max(deg r_i, deg v_i)` and

```text
  d_1 <= 4  <=>  exists i with deg r_i <= 4 and deg r_{i-1} >= 10
            <=>  the remainder-degree sequence SKIPS {5,6,7,8,9}
            <=>  some partial quotient has degree >= 6 straddling
                 the window [5,9].
```

Generic profile: all quotients of degree 1, `deg r_i = 13−i`,
`deg v_i = i`, `d_1 = 7` — anchor 1's "generic 7". Blind-rate:
`#{R : d_1 ≤ 4} ≈ q^9` of `q^{14}`, i.e. `q^{-5}`; the two free scale
ratios restore `q^{2}`, giving `q^{-3}` per triple — the same deficit
by a third route. **Falsifier:** a drop instance whose remainder
sequence contains a degree in `[5,9]`, or a measured `#{R}` outside
`[0.5,2]·q^9`.

**(X6) I EXPECT ANCHOR 1's PER-OBJECT RATE TO BE `(q−1)×` TOO LARGE.**
Anchor 1 `REPORT.md:126-128` uses `P(T≥3 | one T=2 object) = 4.00e-6`
at `q=97` and `354.0` expected `T≥3` per `(S_0,S_inf)` pair in its
`q^4` fibre. My count: the third member is DETERMINED by the object,
and `P(a determined degree-7 form splits over mu_32 with distinct
roots) = C(32,7)(q−1)/q^8 = 4.15e-8` at `q=97`; over the `q^4` fibre
that is `3.67`, not `354`. `4.00e-6 / 4.15e-8 = 96.4 ≈ q−1`. Note
`C(32,7)/q^3 = 3.69` per pair is EXACTLY the shape anchor 1 itself
verified elsewhere (`REPORT.md:102`, `3.30` vs `3.69`), so I expect
the `354` line to be the outlier. **Falsifier:** the measured
histogram of `#(mu_32-roots of the determined third member)` over
≥ 1e4 exact `T=2` objects having mean far from the random-form value
`32/q = 0.330` (`q=97`), or a measured `T≥3` frequency near `4e-6`.

**(X7) INCREMENTAL SWEEP.** The (TEST) functionals depend on `S_1`
only through the 14 values `P_1(x)`, `x ∈ S_0 ∪ S_inf`. A DFS over
7-subsets updates those with 14 multiplications per node, so the
whole per-pair sweep is `O(1)` amortised per triple with a constant
of a few hundred field operations — **no half-gcd needed, and the
"C(25,7)=480,700 tests/pair" figure in the brief is not the binding
number: the honest sweep is over all `C(32,7) = 3,365,856` `S_1`.**
**Falsifier:** measured amortised per-triple cost > 3× the
op-count estimate, or a per-pair sweep that does not fit a ramguard
`local` window at ≤ 4 windows/pair.

**(X8) NO PURELY COMBINATORIAL CRITERION (the (SCRIT) analogue FAILS).**
`(SCRIT)` is combinatorial because `s` is a gcd degree. (TEST) is not:
it is a rank condition on moments that depend on the field VALUES of
the roots, not only on the incidence pattern. I predict **no exact
combinatorial criterion on `(S_0,S_inf,S_1)` for the drop**, and at
most necessary conditions of `(OV4)` type. **Falsifier:** any
combinatorial invariant (overlap pattern, multiplicative-character
sum, coset structure of `S_i` in `mu_32`) that separates hits from
misses in my sweep data with better than chance accuracy.

**(X9) THE PER-PAIR YIELD.** Expected number of `S_1 ⊂ mu_32` giving
`T=3` per `(S_0,S_inf)` pair with `S_0 ∩ S_inf = ∅`:
`C(32,7)·q^{-3} = 3.69` at `q=97`, `0.468` at `q=193`. **Falsifier:**
observed counts inconsistent with Poisson at these means over ≥ 3
swept pairs per field.

### P — numeric blind priors (the brief's six are P1–P6)

| id | statement | prior |
|---|---|---|
| **P1** | an exhaustive-per-pair sweep (all `S_1` for a fixed `(S_0,S_inf)`) is FEASIBLE in this round's compute | **0.72** |
| **P2** | `T = 3` over `mu_32` is achieved this round | **0.55** |
| **P3** | a criterion in the `(SCRIT)` mold (purely combinatorial, exact) lands | **0.12** |
| **P4** | the Euclid trajectory admits an incremental (half-gcd-style) update that is the operative speedup | **0.30** |
| **P5** | **expected max `T` over `mu_32` this round = 3** (P5a: bespoke-domain max = 4; P5b: `mu_32` max if ≥2 pairs sweep clean = 3) | **3** |
| **P6** | `a* = 13` is the MODAL value of `a*` over supported pairs under the projective ruling | **0.40** |
| P7 | (X3) (TEST) survives verification with no correction | 0.60 |
| P8 | (X6) fires: anchor 1's `4.00e-6` is `(q−1)×` too large | 0.65 |
| P9 | `T = 4` over `mu_32` | 0.05 |
| P10 | measured per-triple hit rate within `[0.7,1.4]×q^{-3}` | 0.70 |
| P11 | at least one ramguard run fails (OOM or wall) | 0.30 |
| P12 | I ship at least one bug requiring an Edit-and-rerun | 0.75 |
| P13 | a CATCH-24A subtraction fires load-bearing | 0.80 |
| P14 | the `q=193` sweep also produces a `T=3` (mean 0.468/pair) | 0.30 |
| P15 | I end with a WALL rather than an algorithm or a characterisation | 0.15 |
| P16 | a found `T=3` certifies as `e=m=2`, `s=0`, seprank 3, nullity 1 | 0.55 |
| P17 | the 2×5 Hankel-moment form of `A` is already banked in-repo (CATCH-24A hit) | 0.35 |
| P18 | `a*` under the ruling reproduces the "banked 13" on at least one object | 0.50 |
| P19 | the negative-exponent cell (`T = 4` over `mu_32`) is reached | 0.02 |
| P20 | (X4) holds: `L`, `h`, `k` automatic on every passing triple | 0.70 |

### R4 — MISS-2 GUARD (mean-vs-max; four clauses + two new)

(i) **No sample maximum is ever reported as a bound.** Every `T`,
every `a*`, every overlap is a sample max over the constructions I
ran, with its denominator.
(ii) **Every `T` carries its full distribution**, never only its max.
(iii) **`T_mu32` and `T_bespoke` are never merged**, never summed,
never quoted without the domain attached.
(iv) **A positive first moment is not a witness; an empty sweep is
not emptiness.** I pre-commit to converting neither the `+62.5`-bit
cell nor any exhaustive miss into a verdict in either direction.
(v) **NEW — SCOPE OF EXHAUSTION.** If a sweep exhausts, the statement
is *"for the `P` specific `(S_0,S_inf)` pairs listed, all `C(32,7)`
subsets `S_1 ⊂ mu_32` were tested and none admits a third split
member"* — never *"`T=3` over `mu_32` does not exist"*, and never
*"on the reachable sub-locus"* unless I show the swept pairs exhaust
it. With mean `3.69`/pair, one empty pair is `p = 0.025` evidence and
I will say so.
(vi) **NEW — CERTIFY BEFORE CLAIMING.** No `T=3` over `mu_32` is
claimed until rebuilt from scratch and certified against the original
`36×32` system (`deg(7,7,7)`, `s`, seprank, nullity, `M(Z)Q_Z = 0`
entrywise, generic rank, rank-drop set, rank at infinity, degree-`≤1`
kernel dimension), with the coefficient vectors printed.

### R5 — ZERO-POWER DECLARATIONS (pre-registered, before any data)

1. **A completed sweep of a handful of pairs has ZERO POWER for
`(SAT3)`, the strict endpoint, the official row, or emptiness** — a
vanishing fraction of the `C(32,7)^2` pairs.
2. **Any `T` over a BESPOKE 32-set has ZERO POWER for `mu_32`**
(anchor 1 R5.1, MISS 3 and MISS 9). The two columns stay separate
everywhere, including in the verdict line.
3. **F1/`(NEWCAP)` is declared at ZERO POWER in advance.** `a*` on a
`T=2` object is a minimum over `1` supported pair, on a `T=3` object
over `3`. That is not a minimum over a family. Under the RULED
projective convention this is the first *fixed-convention* dataset
and nothing more; **no F1 test is claimed regardless of the
histogram**.
4. **Two fields only** (`q = 97, 193`) for every structural claim.
**No lift to `Z`, no geometric irreducibility, no statement at
`q ~ 2^128`, nothing at `m ≥ 3`** (`(PAR)` is `m=2`-specific),
nothing about `Rout`, the `9/4` or `7/4` ledgers, FR-canonical, or
layer A.
5. **A failure to find `T = 4` over `mu_32` has ZERO POWER**: the
predicted yield is smaller than the `T=3` yield by a further
`q^{-3}`-type factor and I will not sweep near that.
6. **Timing/feasibility claims are about MY stdlib-Python
implementation under ramguard**, not intrinsic complexity; any
"gain" over anchor 1 is a gain over anchor 1's *instrument*.
7. **(TEST) is registered as a CONJECTURED criterion** until verified
in both directions on both fields; if only one direction verifies I
report it as necessary-only, in the miss list.
8. **`(OV4)` pruning is a NECESSARY condition only** and prunes
`≈11%` of `S_1` by my blind count (`sum_{j≤4} C(14,j)C(18,7−j) =
3,002,064` of `3,365,856`); not presented as a search win.

### R6 — CATCH-24A subtraction plan (run BEFORE every novelty claim)

Every recursive grep carries, **at the search level**,
`--exclude-dir=r38_side_door --exclude-dir=r38_urate_genericity
--exclude-dir=r38_sporadic_det --exclude-dir=pilots_20260802
--exclude-dir='prize-codex-*' --exclude-dir=.git
--exclude-dir=__pycache__ --exclude=dag.json`, over `background/`,
`critical/`, `notes/`. Hyphenated/infixed variants to search
explicitly: `Hankel moment`/`moment matrix`/`moment kernel`/`2x5
Hankel`; `scale elimination`/`scale-elimination`; `rank one`/`rank-1`/
`rank two`; `first minimum`/`first-minimum`/`successive minima`/
`minimum drop`/`minimum-drop`; `continued fraction`/
`continued-fraction`/`partial quotient`/`partial-quotient`/`quotient
degree`; `extended Euclid`/`half-gcd`/`half gcd`/`hgcd`; `Cauchy
interpolation`/`rational interpolation`/`Pade`/`Padé`; `weak Popov`/
`weak-Popov`; `dual annihilator`/`derivative weight`; `a*`/`a star`/
`a-star`/`NEWCAP`/`7m-1`/`projective convention`/`roots at infinity`;
`meet in the middle`/`meet-in-the-middle`; `T = 3 over mu_32`.

### R7 — expected misses (registered in advance)

(a) I expect at least one of (X1)–(X9) to be **wrong**, most likely
(X4) (sufficiency) or (X6) (the `(q−1)` factor).
(b) I expect the brief's `C(25,7) = 480,700` framing to be the wrong
denominator (see (X7)); saying so corrects my own brief, which I flag
rather than silently re-scope.
(c) I expect `a*` to be at **zero power** no matter what it shows
(R5.3), so P6 resolving either way is not a result.
(d) I expect that even a successful `T = 3` over `mu_32` leaves the
`+42.5`-bit `T=4` cell and `(SAT3)` untouched — **the round's
headline, if it lands, does not move the prize's exponent**.
(e) I expect the "WALL" horn (c) of the mandate to remain unproved:
(X8) is a prediction, not a theorem, and is registered as such.
