# H3 quotient Galois-orbit scalar decomposition

- **status:** PROVED
- **closure:** proof
- **consumers:** `f3_h3_dsp8_correlation_bound`,
  `f3_h3_official_order_template_survivor`
- **dependencies:** `f3_h3_dsp8_single_quotient_candidate_compressor`,
  `f3_h3_quotient_algebra_fitting_support_compiler`,
  `f3_h3_shifted_product_sidon`

Let `n=2^s`, let

```text
I_n={(u,v):1<=u,v<n, u!=v},
G=(Z/nZ)^*,       r*(u,v)=(ru,rv) mod n.           (QOD1)
```

For `(u,v) in I_n`, put `m=min(v_2(u),v_2(v))`. Its stabilizer and orbit
size are exactly

```text
Stab(u,v)={r in G:r=1 mod 2^(s-m)},
|Stab(u,v)|=2^m,       |G*(u,v)|=2^(s-1-m).        (QOD2)
```

For every `1<=j<=s-1`, the number of ordered quotient orbits of size `2^j`
is

```text
3(2^j-1).                                          (QOD3)
```

Consequently

```text
#(I_n/G)=3(n-s-1),
sum_orbits |orbit|=(n-1)(n-2).                     (QOD4)
```

At the first official order `n=8192`, this is `24,534` orbits, each of size
at most `4,096`, instead of `67,084,290` ordered quotient lifts.

Put `R=Z[1/2]`, `zeta=zeta_n`, and

```text
gamma_(u,v)=(1-zeta^v)/(1-zeta^u).
```

For an orbit `O`, define

```text
q_O(T)=product_((u,v) in O)(T-gamma_(u,v)) in R[T]. (QOD5)
```

The factors are monic irreducible polynomials of degree `|O|`, and the monic
nonidentity quotient polynomial factors exactly as

```text
Qhat_n(T)=product_O q_O(T).                         (QOD6)
```

Let `s_O,35` be the positive odd generator of

```text
(q_O,Pcal_n^[0],...,Pcal_n^[35]) intersect R.      (QOD7)
```

Then the odd prime support of the cutoff-35 scalar annihilator decomposes
exactly orbitwise:

```text
rad(s_(n,35)^X)=rad(product_O s_O,35).             (QOD8)
```

For every official prime `p=1 mod n`, this common support condition is
equivalent to a target with `P(t)>=36,R(t)>=1`, hence to
`Dbar_17^0+Dbar_17^A>0`.

Thus cutoff-35 elimination may be sharded into exactly `3(n-s-1)` independent
blocks of degree at most `n/2`, with each block carrying its own scalar
Bezout/invariant-factor certificate and checkpoint. The total degree remains
`(n-1)(n-2)`: this theorem does not prove a fast algorithm, identify
prime-adic valuations across blocks, factor any `s_O,35`, bound the survivor
moment, or close C36'.
