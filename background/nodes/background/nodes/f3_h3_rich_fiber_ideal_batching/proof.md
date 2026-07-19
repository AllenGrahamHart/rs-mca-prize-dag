# Proof

The proved dyadic shifted-product Sidon theorem says that distinct unordered
pairs have distinct shifted products in characteristic zero. Hence every
`alpha_i` is nonzero, and so is the ideal `J`.

Every factor `1-zeta^e` is divisible by `pi=1-zeta`, because

```text
1-zeta^e=(1-zeta)(1+zeta+...+zeta^(e-1))
```

after choosing the representative `1<=e<n`. Thus every `beta_i` belongs to
`(pi)^2`, and therefore every difference `alpha_i` belongs to `(pi)^2`.
The common finite-field product says exactly that `alpha_i` reduces to zero
under `zeta -> g`, so `alpha_i` also belongs to `P`.

The ideals `(pi)` and `P` lie above the distinct rational primes `2` and `p`.
They are comaximal, whence

```text
(pi)^2 intersect P=(pi)^2 P.
```

It follows that

```text
J subset (pi)^2 P.                                  (1)
```

For a power-of-two cyclotomic field,

```text
N((pi))=|Phi_n(1)|=2,
N(P)=p.
```

Ideal norms reverse divisibility under inclusion. Equation `(1)` therefore
gives

```text
4p=N((pi)^2 P) divides N(J).                         (2)
```

For every generator, `(alpha_i) subset J`, so the same inclusion law gives

```text
N(J) divides N((alpha_i))=|Norm_K/Q(alpha_i)|.        (3)
```

Taking the gcd in `(3)` and combining with `(2)` proves `(IB)`.

Finally, let `J_2=(alpha_i,alpha_j)` and suppose the two principal norms have
gcd `4p`. Applying `(IB)` to these two generators gives

```text
4p divides N(J_2) divides 4p.
```

Thus `N(J_2)=4p`. Since `J_2 subset (pi)^2 P` and the two integral ideals
have the same norm, they are equal. This proves `(SAT)`.
