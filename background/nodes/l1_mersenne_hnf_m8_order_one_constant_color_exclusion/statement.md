# L1 Mersenne HNF m=8 order-one constant-color exclusion

- **status:** PROVED
- **dependency:** `l1_mersenne_hnf_order_one_frobenius_gate`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the four official `(m,h)=(8,7)` next-to-maximal rows

Put `d=c-1`, `r=rho*c`, and remove the known order-one root:

```text
P_(rho,c)(W)=(W+1/d)L_(rho,c)(W),       deg L=6.     (CCE1)
```

For every root `x_i` of `L`, its Frobenius color

```text
epsilon_i=x_i^(p+1)
```

lies in `mu_8`. These six colors cannot all be equal.

More precisely, if `epsilon_i=epsilon` for every `i`, put

```text
zeta=d^(p+1) in mu_8,       alpha=epsilon*zeta.      (CCE2)
```

The first reciprocal coefficient equation forces

```text
r=1-alpha.                                           (CCE3)
```

The cases `alpha=1` and `alpha=-1` are impossible. In every other case the
second reciprocal coefficient equation forces

```text
30alpha*d=(alpha+1)zeta+12alpha^2.                   (CCE4)
```

Hence `d in F_(p^2)`, `zeta in {+1,-1}`, and, with
`s=alpha+alpha^(-1)`, its norm equation is

```text
12zeta*s^2+(1+12zeta)s+146-924zeta=0.               (CCE5)
```

The five possible traces of an eighth root are
`s=2,-2,0` or `s^2=2`. None satisfies (CCE5) in an official
characteristic. Therefore every surviving non-base-field `h=7` packet has
a genuinely nonconstant root-color assignment. This does not exclude the
remaining color strata, prove cyclotomic divisibility from the bounded
identities, construct an inner lift, or promote L1.
