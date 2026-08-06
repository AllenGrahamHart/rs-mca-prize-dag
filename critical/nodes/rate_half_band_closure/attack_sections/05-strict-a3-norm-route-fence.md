
## STRICT A=3 ENDPOINT: TRANSPOSED NORMAL FORM + NORM ROUTE FENCE (2026-07-26)

Full record: `notes/strict_endpoint_norm_route_fence_20260726.md`; artifact
`verify_strict_endpoint_norm_fence.py`.

Two restatements of the strict `B=2^39`, `e=m`, `h=0` sharp-cap endpoint. (a) is
SSL14 in resultant language; (b) is its transpose and was not on record.

```text
(a)  Res_X( X^N - c , Q(U,V;X) ) = H(U,V)^(4m-1) S(U,V),   S linear   [O=0]
(b)  (X - x_0) product_(gamma in Z) Q_gamma(X) = kappa (X^N - c)^m,
     kappa = product_gamma c_gamma,        1 + (4m+1)(4m-1) = 16m^2 = Nm.
```

Form (b) exhibits the endpoint as a factorization of an `m`-th power of the
smooth-domain polynomial into `4m+1` members of the `(m+1)`-dimensional space
`W=span(Q_0..Q_m)`, which lie on a degree-`m` rational normal curve in `P(W)`
(SSL4), plus one linear factor.

**FENCE — do not attack this endpoint by subgroup-norm or multiplicative-parity
arithmetic.** Comparing leading and constant coefficients of (b) gives, with
`pi_gamma = product_(x in Rt(gamma)) x`,

```text
product_(gamma in Z) pi_gamma = (-c)^m / x_0.                      (NORM)
```

(NORM) is a **consequence of the covering ledger, not a constraint**: it equals
`product_x x^(d_x) = (product_x x)^m / x_0` identically, so the two derivations
are the same identity and comparing them is circular. Verified to hold on 160
combinatorial covers with the endpoint multiplicities and no algebraic
realizability whatsoever. In cyclic-exponent form the congruence needs
`m*(N/2) = 0 mod N`; at official scale that is `2^77 = 0 mod 2^41`, vacuous with a
**36-power-of-two margin** — not a near-miss a sharper constant could rescue.

What survives is the live target: whether `4m+1` totally-`D`-split degree-`4m-1`
polynomials can lie on a degree-`m` rational normal curve in an `(m+1)`-dimensional
space with each domain point covered exactly `m` times (one point `m-1`). The
information is in the linear-series/RNC interaction with the split condition; the
multiplicative bookkeeping is now closed off.

Excludes no stratum and closes no budget; this node stays TARGET.
