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
