# Proof

With the corrected relative `U/V` normalization, clearing its denominator and
removing exactly `w^2(p-1)^2` gives four reciprocal quartics in `b`.
Coefficientwise reciprocity is checked before descent to `trace=b+b^-1`.
The four trace quadratics have `(total degree, terms)`

```text
(18,1181), (18,1244), (15,553), (15,574).
```

Write their `4 x 3` coefficient matrix as `M(p,t,w)`. Any common trace root
forces all four maximal minors to vanish and forces the first-two-row kernel
onto the Veronese conic. After exact open-factor division, the residual
minors have `193,222,198,234` terms.

## Common components

The three star projections share, beyond open factors,

```text
L = 4p+5t+4
```

and

```text
F = 8p^3+37p^2t+27p^2+52pt^2+89pt+27p
    +20t^3+52t^2+37t+8.
```

On `L=0`, the gcd of all four residual minors with the conic is associate to
`t^3(t+1)(t+4)(w-1)`, entirely forbidden.

For `F`, take the exact `w`-resultant of residual minor 0 and the residual
conic. It is not divisible by `F`. Their `p`-resultant has degree 272 in `t`,
digest
`963584284e8b4d2a33d09772ce68a377108c9717c479a194654989430f993c00`,
and 21 irreducible factors. For each factor, instantiate
`F_P[t]/(g(t))`, gcd `F` with the minor-conic resultant in `p`, and factor.
Every `p` gcd is linear, including factors of degrees 5, 9, and 60. Exact
replay gives:

```text
8 base-boundary factors;
8 factors with no common four-minor/conic w root;
5 linear w candidates, all with gcd one in the original trace equations.
```

Thus `F` has no admissible point, including every degree-drop specialization.

## Off-common intersections

The three noncommon projection cofactors have digests

```text
a3882e8bb2c445e70b9f594d4ddf2beadd2e2ffd64bf973e682f35908b0018f5
123228f02b6bf1687d4c37f3bc2fa36418ec860bb38d65a3bbc565b729050802
3991528db1a1f476582e3d5814df421f8fb968410f0a8994d786c54334bf5fca
```

The gcd of their two star `p`-resultants has degree 86 in `t`, digest
`26d8547631b2b7f205fc170b008ad6d4b8af92d083c15aed39c426e25c4f6882`,
and seven linear factors. Their endpoint gcds yield seven distinct `p`
candidates. Every candidate kills the base forbidden product

```text
p(p-1)(p-t+1)(p+t+1)(p+2t+4)
(4p+2t+1)(5p+4t+5)(t^2-4p).
```

The common components and finite residual intersection are exhausted, so no
common root of the original trace equations is admissible.
