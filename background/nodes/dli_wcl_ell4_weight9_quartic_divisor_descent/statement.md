# WCL `(4,9)` quartic-divisor descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `dli_wcl_slot_4_9_emptiness`
- **dependency:** `dli_wcl_newton_short_window_exclusion`

Let `K` be a field of characteristic zero or characteristic greater than
`9`, containing `omega` of exact order `2048`. For a reduced signed
weight-nine relation put

```text
rho_i=s_i omega^e_i,       0<=e_i<1024,
p_j=sum_i rho_i^j.                                      (QDD1)
```

Assume

```text
p_1=p_3=p_5=p_7=0.                                    (QDD2)
```

Let `a_9=product_i rho_i`. Since `9^(-1)=1593 mod 2048`, there is a unique
common dilation

```text
lambda=a_9^(-1593) in mu_2048                         (QDD3)
```

for which the normalized roots `lambda rho_i` have product one. Dilation
preserves reducedness and `(QDD2)`.

There is then a unique monic quartic

```text
A(Y)=Y^4+c_3Y^3+c_2Y^2+c_1Y+c_0                       (QDD4)
```

such that the normalized root locator is

```text
F(X)=product_i(X-lambda rho_i)=X A(X^2)-1.             (QDD5)
```

Put

```text
G(Y)=Y A(Y)^2-1.                                      (QDD6)
```

Then

```text
G(Y)=product_i(Y-(lambda rho_i)^2),
G(Y) divides Y^1024-1.                                (QDD7)
```

Conversely, every monic quartic `A` over `K` satisfying the divisibility in
`(QDD7)` reconstructs one normalized reduced relation satisfying `(QDD2)`:
for every root `y` of `G`, put

```text
rho=A(y)^(-1).                                        (QDD8)
```

Then `rho^2=y`, the nine reconstructed roots are distinct and nonantipodal,
their product is one, and their first four odd power sums vanish. Thus
common-dilation orbits of `(4,9)` relations are in bijection with the monic
quartics in `(QDD7)`.

This gives a fixed characteristic-only elimination endpoint. Divide
`Y^1024-1` by the monic degree-nine polynomial `G` and write

```text
(Y^1024-1) mod G=sum_(j=0)^8 R_j(c_0,c_1,c_2,c_3)Y^j. (QDD9)
```

The `R_j` lie in `Z[c_0,c_1,c_2,c_3]`. The ideal

```text
I=(R_0,...,R_8)                                       (QDD10)
```

has no characteristic-zero point. Consequently there is a nonzero integer
`Delta` and polynomials `H_j` over `Z` such that

```text
Delta=sum_(j=0)^8 H_j R_j.                            (QDD11)
```

Every finite characteristic supporting a `(4,9)` relation divides any such
certified `Delta`. Computing and factoring one certificate, then checking
its characteristics against the official field constraints, is sufficient
to close the slot. This theorem does not compute `Delta` or prove the slot
empty.

## PELL FORM + SMALL-ANALOGUE EVIDENCE (2026-07-26)

Rearranging `(QDD5)`/`(QDD7)`, with `P(Y) = prod_i (Y - (lambda rho_i)^2)`:

```text
P(Y) + 1 = Y A(Y)^2,          i.e.   Y A(Y)^2 - P(Y) = 1.
```

So the cell asks: **is there a squarefree product of `1024`-th roots of unity which
becomes `Y` times a perfect square after adding `1`?** Equivalently `P` has 9
distinct roots in `mu_1024` while `P + 1` has one simple root (at `0`) and four
double roots (at the roots of `A`) — a Davenport-type "`P` and `P+1` both highly
structured" condition. Setting `Y = 0` recovers `prod y_i = 1`.

**Two structural facts this form exposes** (invisible in the `R_j` eliminant):

1. `P' = A^2 + 2 Y A A' = A (A + 2 Y A')`. Since `P | Y^1024 - 1` is squarefree,
   `gcd(P, P') = 1`, hence **`gcd(P, A) = 1` and `gcd(P, A + 2YA') = 1`**.
2. At every root, `A(y)^2 = y^{-1}`, so `A` maps the nine roots into `mu_2048`;
   taking the product over all nine and using `prod y_i = 1` gives
   `(prod_i A(y_i))^2 = 1`, i.e. `Res(P, A) = +/- 1`.

**Small-analogue evidence — CORRECTED 2026-07-27. The first table below was
ARTEFACT, not evidence.**

There is a local constraint I had not extracted: `A(y)^2 = y^{-1}` forces every root
`y_i` to be a **quadratic residue**. Now `mu_N` lies entirely inside the squares iff
`2N | p-1`; otherwise only half of `mu_N` is available. So an analogue is
**faithful only when `2N | p-1`** — which is exactly the official situation, since
`N = 2^10` and `2^41 | p-1` make the constraint vacuous there.

My first analogues mostly failed that test:

| `p` | `N` | `2N \| p-1`? | squares in `mu_N` | verdict |
|---|---|---|---|---|
| 17 | 16 | no | 8 | **vacuously impossible: 9 roots needed, 8 squares exist** |
| 97 | 32 | no | 16 | unfaithful — constraint bites artificially |
| 193 | 64 | no | 32 | unfaithful |
| 257 | 128 | **yes** | 128 | faithful, but sampled at ~0.005% |

So the headline "exhaustive over 83,521 quartics at `(17,16)`, zero hits" was
**counting-impossible before any algebra ran**, and carried no information at all.

**Faithful, exhaustive re-run** (`2N | p-1`, all of `mu_N` square, as officially):

| `p` | `N` | product-one 9-subsets | `P+1 = Y A(Y)^2` |
|---|---|---|---|
| 97 | 16 | 715 | **0** |
| 193 | 16 | 715 | **0** |
| 257 | 16 | 715 | **0** |
| 353 | 16 | 715 | **0** |

These four are genuine exhaustions of a faithful analogue. They remain
route-selection evidence only — `N = 16` uses nine of sixteen roots where the
official cell uses nine of `1024`, a very different density — but unlike the first
table they are not artefact.

**Fence, per this node's own standing rule:** *small analogues are falsification and
route-selection evidence only; a no-hit analogue never proves the official uniform
statement.* The exhaustive `N = 16` row is a genuine (if tiny) exhaustion; the
sampled rows cover a vanishing fraction of `p^4` and are weak. This is a reason to
believe the slot is empty and to keep attacking it, **not** a closure.

**Route fenced (checked, negative): Mason–Stothers cannot work here, at any `N`.**
With `a = P`, `b = 1`, `c = Y A^2`, pairwise coprime by fact 1 above,
`deg rad(abc) = deg P + 0 + deg rad(Y A^2) = 9 + 5 = 14` against `max deg = 9`, so
abc reads `9 <= 13` — satisfied. A contradiction would need `deg rad(abc) <= 9`,
impossible since `rad(P) = P` already has degree 9. The obstruction is structural,
not a matter of sharpening constants — and it is the same reason abc failed on the
`s=2` bridge pencil.

### Global-invariant routes are ALL vacuous here (2026-07-27)

Three global invariants were tried on the Pell form and every one collapses to an
identity forced by `P + 1 = Y A(Y)^2` itself. Recorded so the lane stops re-deriving
them.

1. **`Res(P, A) = 1`, identically.** At each root `a_j` of `A`,
   `P(a_j) = a_j A(a_j)^2 - 1 = -1`, so `Res(P,A) = prod_j P(a_j) = (-1)^4 = 1`.
   From the other side `Res(P,A) = prod_i A(y_i)`, so this is exactly `prod rho_i = 1`
   — the product-one condition restated. **No new information.**

2. **The `mu_N`-product is an identity.** With `T = prod_{y in mu_N} (P(y)+1)` and
   `R = prod_{y in mu_N} A(y)`,

```text
T = prod_y y A(y)^2 = (prod_{y in mu_N} y) * R^2 = -R^2      (N even).
```

3. **Hence the quadratic-character condition is VACUOUS.** `-T = R^2` is a square by
   construction, so `chi(-T) = 1` *always* and excludes nothing. Verified over
   `(p,N) = (17,16), (97,32), (193,64), (257,128)`: the identity held on every one
   of 1153 / 2139 / 2134 / 1821 admissible quartics, and `-T` was a square in every
   single case.

**Method note (a real trap).** A first pass built `mu_N` as the first `N` powers of
an element with `N` distinct powers. That is *not* the order-`N` subgroup unless
`N = p-1`; it coincided at `(17,16)` and was wrong at `(97,32)`, `(193,64)`,
`(257,128)`, where it made the identity appear to *fail*. The correct construction
is `h = g^{(p-1)/N}` for a primitive root `g`. A wrong `mu_N` here would have read
as evidence of an obstruction where there is none.

**Lane-level fence.** Together with the abc fence above and the strict-endpoint norm
fence on `rate_half_band_closure`, the pattern is now unambiguous: **global
multiplicative invariants — resultants, norms, `mu_N`-products, quadratic characters
— are forced by the defining identity on these configurations and carry no
information.** They are consequences, not constraints. Any future attack in either
the WCL descent lane or the rate-half endpoint lane must use *local* structure
(root-by-root incidence, ramification profiles, the double-root pattern of `P+1`)
rather than a global product.

## EXISTENCE WITNESS at a faithful analogue — the configuration is NOT structurally obstructed (2026-07-27)

**A genuine `(4,9)` relation exists at `(p, N) = (257, 128)`.** Explicitly, over
`F_257` with `mu_128` the order-128 subgroup (faithful: `2N = 256` divides
`p-1 = 256`, so all of `mu_128` are squares, as officially):

```text
A(Y) = Y^4 + 58 Y^3 + 240 Y^2 + 133 Y + 86
P(Y) = Y A(Y)^2 - 1   has the nine distinct roots
       {50, 121, 133, 140, 146, 196, 197, 208, 235} subset mu_128,
```

with product one; `rho_i = A(y_i)^{-1}` satisfies `rho_i^2 = y_i`, `prod rho_i = 1`,
every `rho_i in mu_256`, all pairwise non-antipodal, and

```text
p_1 = p_3 = p_5 = p_7 = 0     -- the ell = 4 window conditions, exactly.
```

A 250,000-tuple meet-in-the-middle sample (0.15% of the search space) found **1530
distinct such quartics**, so solutions are abundant here, not exceptional. The
expected-count heuristic predicted ~34 at this analogue and undercounts by ~45x,
but its qualitative picture is right.

### Why this is the most useful fact on the cell

**There is no structural obstruction to the `(4,9)` configuration.** It is
realizable, and abundantly. Therefore:

> **Any proof that the official cell is empty MUST use the arithmetic SIZE of the
> characteristic — `p > 2^167` against `N = 1024`. Structure alone can never
> suffice, at any level of cleverness.**

The expected count is `C(N,9)/(N p^4)`: at `(257,128)` that is `~2^5` and solutions
exist; at the official row it is `< 2^-607` and they do not. Emptiness is a *density*
phenomenon driven by `p >> N`, not a structural impossibility.

This retroactively explains every failed route on this node and its neighbours —
abc/Mason-Stothers, `Res(P,A)`, the `mu_N`-product, the quadratic character, the
ramification profile. **All are structural, hence all were doomed before they were
tried.** They failed for a single common reason, not six separate ones.

**Consequence for the lane:** the standing fence is strengthened from "global
multiplicative invariants are vacuous" to the sharper "**no structural argument can
close a WCL zero-event cell; the proof must be quantitative in `p`**". The live
route is a rigorous counting or character-sum bound over `mu_N`, where losing even
hundreds of bits against a `2^607` margin would still close the cell.

### Calibration of the counting heuristic — it does NOT calibrate (2026-07-27)

The expected-count heuristic `E = C(N,9)/(N p^4)` was tested against the actual
solution count at faithful analogues, by meet-in-the-middle sampling:

| `p` | `N` | solutions found | estimated total | heuristic `E` | ratio |
|---|---|---:|---:|---:|---:|
| 257 | 64 | 23–26 | ~30 | 0.099 | **~300** |
| 257 | 128 | 752 | ~8,900 | 34.1 | **~260** |
| 641 | 64 | 0 | 0 | 0.0026 | undetermined |
| 769 | 64 | 0 | 0 | 0.0012 | undetermined |

**The heuristic undercounts by a factor of roughly 300** at both testable points.
The cause is visible: `P_A = Y A^2 - 1` is *not* a random monic degree-9 polynomial
with constant term `-1`. It takes the value `-1` with multiplicity pattern
`(1,2,2,2,2)`, and such polynomials split far more readily than random ones. The
naive "probability of splitting" step is therefore wrong.

**And the `p`-dependence cannot be measured.** At `p = 641, 769` the predicted
counts drop to `~10^-3`, so observing zero is uninformative and no ratio can be
extracted. Solutions are only abundant enough to count when `p` is small relative
to `N` — **exactly the regime unlike the official row**.

**Consequence, stated plainly.** The `2^-607` margin quoted above is an
**unvalidated extrapolation**. It is sound for *route selection* — it says the cell
is not delicate, and it correctly predicted that a faithful analogue with small `p`
would contain solutions (it does, abundantly). It is **not** a quantitative claim
about the official row, and must not be cited as one. A rigorous argument would not
need the heuristic; but neither can the heuristic tell that argument how much room
it has.

**No shift symmetry.** The 728 distinct solution root-sets at `(257,128)` fall into
728 distinct orbits under multiplication by `mu_128` — none coincide. That is
forced: rescaling `y -> zeta y` sends `P` to `zeta^9 P(Y/zeta)`, which is again of
the form `Y A^2 - 1` only when `zeta^9 = 1`, and `gcd(9,128) = 1` makes that
`zeta = 1`. So the abundance is genuine multiplicity, not one orbit seen many times.

## THE CLEAN FORM — the cell is a symmetric-function condition on `mu_{2N}` (2026-07-27)

The quartic, the divisibility and the elimination all disappear. At a root,
`A(y)^2 = y^{-1}`; put `u = A(y)`, so `u^2 = y^{-1}` and, since `2N | p-1`,
`u in mu_{2N}` with `y = u^{-2}`. The condition `A(u^{-2}) = u`, multiplied by `u^8`,
is `c_0u^8 + c_1u^6 + c_2u^4 + c_3u^2 + 1 = u^9`, i.e.

```text
prod_{i=1}^{9} (X - u_i) = X^9 - c_0X^8 - c_1X^6 - c_2X^4 - c_3X^2 - 1.
```

Matching elementary symmetric functions gives the whole cell:

> **`(4,9)` holds iff there are nine distinct `u_1,...,u_9 in mu_{2N}` with**
> ```text
> e_2 = e_4 = e_6 = e_8 = 0        and        e_9 = prod u_i = 1.
> ```
> **The quartic is then read off: `c_0 = e_1`, `c_1 = e_3`, `c_2 = e_5`,
> `c_3 = e_7`, and the roots are `y_i = u_i^{-2}`.**

So `A` is not an unknown at all — it is *determined* by the odd symmetric functions
of the `u_i`, and the only conditions are that the four **even** ones vanish and the
product is one. Five conditions on a 9-subset of a cyclic 2-group. (Note the
duality with the original pose, where the `rho_i` had vanishing **odd power sums**.)

**Verified on the witness** at `(257,128)`: `u = (6,22,39,55,70,99,133,196,237)`,
all in `mu_256`, with `e_2 = e_4 = e_6 = e_8 = 0`, `e_9 = 1`, and
`(e_1,e_3,e_5,e_7) = (86,133,240,58) = (c_0,c_1,c_2,c_3)` — exactly `A`.

### The counting model, now calibrated

The corrected expectation is `E' = C(2N, 9) / p^5` — five conditions, and the roots
live in `mu_{2N}`, **not** `mu_N`. That doubling is what the earlier model missed:

| `p` | `N` | old `C(N,9)/(N p^4)` | **new `C(2N,9)/p^5`** | observed |
|---|---|---:|---:|---:|
| 257 | 64 | 0.099 | **17** | ~30 |
| 257 | 128 | 34.1 | **10,069** | ~8,900 |

The new model is within 12% at the larger analogue and a factor 2 at the smaller,
and it explains the old model's error exactly: the ratio is `2^9 N/p`, which is
`255` at `(257,128)` against the ~260 discrepancy observed.

**Officially:** `2N = 2048`, `p > 2^167`, so `C(2048,9) = 2^80.5` against
`p^5 > 2^835`, giving an expected count `< 2^-754`. Unlike the previous figure this
rests on a model that has been checked against ground truth twice.

**This is the form a rigorous count should attack**: bound the number of 9-subsets
of `mu_{2N}` with four vanishing even symmetric functions and product one. No
quartic, no divisibility, no elimination ideal — a pure symmetric-function question
on a cyclic 2-group.

### Final form: one quartic, one equation, one subgroup

The `u_i` can be eliminated too. With `u^2 = t` and `u^9 = e(t)`, writing
`u^9 = u t^4` gives `e(t) = +/- u t^4`, hence `(e(t)/t^4)^2 = t`:

> **`(4,9)` holds iff there is a quartic `e` with `e(0) = 1` such that**
> ```text
> e(t)^2 = t^9        for NINE distinct t in mu_N,
> ```
> **and then `u = e(t)/t^4`, `y = t^{-1}`, `A` = the reverse of `e`.**

Since `deg(e(T)^2 - T^9) = 9`, nine is the maximum possible: the cell asks for
`e(T)^2 - T^9` to **split completely over `mu_N`**.

Verified on the witness: `e = 86T^4 + 133T^3 + 240T^2 + 58T + 1` gives exactly the
nine `t in mu_128` shown, product one, each recovering its `u`.

This is the whole cell in one line, with no quartic-as-unknown, no divisibility
condition, no elimination ideal, and no auxiliary group. It is a *Pell-type
condition on a subgroup*: a fixed low-degree polynomial must take square values —
specifically the values `t^9` — at nine points of `mu_N`.

**The rigorous target is now sharply stated:** bound the number of quartics `e` for
which `e(T)^2 - T^9` splits completely over `mu_N`. Equivalently, bound
`#{monic degree-9 divisors of T^N - 1 of the shape T^9 - e(T)^2}`. The map
`e -> T^9 - e(T)^2` is injective on `{e : e(0)=1}`, so this is a question about how
often a `p^4`-parameter family meets the `C(N,9)` split polynomials — Weil/Deligne
territory, and quantitative in `p`, which the existence witness proved is the only
kind of argument that can work.
