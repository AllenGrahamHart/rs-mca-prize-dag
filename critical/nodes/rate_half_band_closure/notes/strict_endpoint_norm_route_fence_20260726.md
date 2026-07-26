# Strict A=3 endpoint: the transposed normal form, and why subgroup-norm
# arithmetic on it is route-dead (2026-07-26)

Scope: the strict budget `B = 2^39` residual of `(K5-CA)`, at the first endpoint
`e = m = 2^37`, sharp cap `h = 0`, `T = 4m+1`, in the cleanest sub-case `O = 0`.
Notation as in `rate_half_ca_hankel_strict_a3_slope_slack_ledger` (SSL1–SSL16):
`rho = r = 4m-1`, `N = 16m = 2^41`, `R = 8m`, `A = 3`, `D` a multiplicative coset
of order `N`, `P_D(X) = prod_{x in D}(X-x) = X^N - c`.

Artifact: `verify_strict_endpoint_norm_fence.py` (stdlib, exact integers).

## 1. The transposed normal form

SSL14 records the **slope-side** product `J R = H^rho S`, where
`R = prod_{x in D} Q(U,V;x)`. Two equivalent restatements are worth having on
record, because they move the endpoint into the smooth-domain frame.

**(a) Resultant form.** Since `P_D` is monic of degree `N`,

```text
R(U,V) = prod_{x in D} Q(U,V;x) = Res_X( X^N - c , Q(U,V;X) ),
```

a binary form of degree `N e = 16m^2`, and SSL14 says it equals
`prod_{gamma in Z} L_gamma^{u_gamma} * S` with `deg S = C`. At `O = 0`, `C = 1`:

```text
Res_X( X^N - c , Q ) = H(U,V)^{4m-1} * S(U,V),      S linear, H squarefree, deg H = 4m+1.
```

So the resultant of the smooth-domain polynomial with `Q` has radical of degree
only `4m+2` against its own degree `16m^2` — an extreme perfect-power condition.

**(b) Transposed (domain-side) form — the one not previously recorded.** Dually,
each supported slope has `u_gamma = rho`, so
`Q_gamma(X) = c_gamma prod_{x in Rt(gamma)}(X-x)` with `Rt(gamma) subset D`,
`|Rt(gamma)| = 4m-1`. Every `x in D` lies in exactly `d_x` of these sets, and at
`h = 0`, `O = 0` we have `d_x = m` for all `x` except a single `x_0` with
`d_{x_0} = m-1`. Hence

```text
(X - x_0) * prod_{gamma in Z} Q_gamma(X) = kappa * (X^N - c)^m,     kappa = prod_gamma c_gamma.
```

Degrees check: `1 + (4m+1)(4m-1) = 16m^2 = N m`. This exhibits the endpoint as a
factorization of an **m-th power of the smooth-domain polynomial** into `4m+1`
members of an `(m+1)`-dimensional space `W = span(Q_0,...,Q_m)` that lie on a
**degree-`m` rational normal curve** in `P(W)` (SSL4), plus one linear factor.

## 2. The natural attack, and why it dies

Form (b) invites an obvious attack: `D` is a coset of the cyclic 2-group
`mu_N`, `N = 2^41`, so compare **norms** — take leading and constant
coefficients of the identity and read off a multiplicative condition on the root
sets. Write `pi_gamma = prod_{x in Rt(gamma)} x`.

Leading coefficients give `kappa = prod_gamma c_gamma`. Constant terms give,
using `|Rt(gamma)| = 4m-1` odd so `Q_gamma(0) = -c_gamma pi_gamma`, and
`(-1)^{4m+1} = -1`:

```text
(-x_0) * prod_gamma ( -c_gamma pi_gamma ) = kappa (-c)^m
  =>   x_0 * kappa * prod_gamma pi_gamma = kappa (-c)^m
  =>   prod_{gamma in Z} pi_gamma = (-c)^m / x_0.                    (NORM)
```

**(NORM) carries no information.** It is not a constraint on the configuration;
it is a *consequence* of the covering ledger, and it holds for **every** set
system with the right multiplicities, algebraically realizable or not:

```text
prod_gamma pi_gamma = prod_{x in D} x^{d_x} = (prod_{x in D} x)^m / x_0 = (-c)^m / x_0,
```

since `prod_{x in D} x = -c`. The two derivations are the same identity, so
comparing them is circular.

The cyclic-exponent form dies the same way. With `D = d_0 mu_N`, `x = d_0 zeta^{a_x}`,
`(NORM)` reduces mod `N` to

```text
m * sum_{x in D} a_x - a_{x_0}  ==  -a_{x_0}   (mod N),
```

and `sum_{x in D} a_x = N(N-1)/2 == N/2 (mod N)`, so the left side needs
`m * N/2 == 0 (mod N)`. At official scale `m * N/2 = 2^37 * 2^40 = 2^77`, and
`77 >= 41`, so it vanishes identically. **The congruence is satisfied for every
admissible configuration and every choice of `x_0`.** There is no parity or
2-adic obstruction here to be found.

## 3. Fence (what not to spend a session on)

Do **not** attempt to exclude the strict `A=3` sharp-cap endpoint by subgroup-norm
or multiplicative-parity arithmetic on the root-set products `pi_gamma`, nor by
comparing leading/constant coefficients of the form-(b) factorization. Every such
comparison is an identity forced by the incidence ledger, and the 2-adic
congruence is vacuous because `m * N/2 == 0 (mod N)` at official scale by a
margin of `2^36`.

Note the exponent margin is enormous, so this is not a near-miss that a sharper
constant could rescue: it fails by 36 powers of two.

What survives, and is the actual target: the endpoint asks whether `4m+1`
totally-`D`-split polynomials of degree `4m-1` can lie on a **degree-`m` rational
normal curve** in an `(m+1)`-dimensional space, with each domain point covered
exactly `m` times (one point `m-1`). The live information is the interaction of
that RNC/linear-series structure with the split condition — not the multiplicative
bookkeeping, which is now fenced.

## 4. Non-claims

- Excludes no stratum; closes no budget. `rate_half_band_closure` stays TARGET.
- Sub-case `O = 0` is stated for cleanliness; the `O > 0` version replaces `C = 1`
  by `C = 1+O` and `S` by a degree-`(1+O)` form, and the (NORM) argument degrades
  identically — still an identity, still no obstruction.
- Form (a) is a restatement of SSL14, not new content. Form (b) and the fence in
  §2–§3 are the new material.
