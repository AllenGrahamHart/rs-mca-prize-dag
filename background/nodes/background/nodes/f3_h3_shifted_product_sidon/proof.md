# Proof

Write `zeta=zeta_n`. For a nonidentity root `zeta^e`, let `r(e)` be the
2-adic valuation of its exponent, represented in `{0,...,n-1}`. At the unique
prime of `Q(zeta)` above `2`, normalized by `v(1-zeta)=1`, the cyclotomic
tower gives

```text
v(1-zeta^e)=2^r(e).                              (1)
```

Suppose

```text
(1-x)(1-y)=(1-u)(1-v),                           (2)
```

where `x,y,u,v` are nonidentity `n`th roots. Applying `(1)` to `(2)` gives

```text
2^r(x)+2^r(y)=2^r(u)+2^r(v).
```

An integer has a unique binary expansion, so an unordered sum of exactly two
powers of two determines the unordered pair of exponents, including the
equal-exponent carry case. After swapping `u,v` if necessary, write

```text
r(x)=r(u)=r,       r(y)=r(v)=q,       r<=q.      (3)
```

## Different valuation levels

Assume `r<q`, put `eta=zeta^(2^r)`, and let `K0=Q(eta^2)`. Then

```text
Q(eta)=K0 direct_sum eta*K0.
```

The roots `y,v` lie in `K0`, while `x,u` lie in `eta*K0`. Separating `(2)`
into its two quadratic-tower components gives

```text
1-y=1-v,             x(1-y)=u(1-v).
```

Therefore `y=v`; since `y!=1`, the second equality gives `x=u`.

## One valuation level

Assume `r=q`. If `eta` has order two then all four roots equal `-1` and the
claim is immediate. Otherwise the same quadratic decomposition applies. All
four roots lie in `eta*K0`, while their pairwise products lie in `K0`.
Separating

```text
1-x-y+xy=1-u-v+uv
```

gives

```text
xy=uv,              x+y=u+v.
```

The monic quadratics `(T-x)(T-y)` and `(T-u)(T-v)` are equal, so
`{x,y}={u,v}`. The map `x -> 1-x` is injective, proving `(SID)`.

If a nonidentity quotient has two representations

```text
d/c=d'/c',       c,d,c',d' in A,
```

then `dc'=d'c`. By `(SID)`, either the two ordered representations agree, or
`d=c` and `d'=c'`. The latter case is the identity quotient. Thus every
nonidentity quotient fiber over `C` has size at most one.

## Finite-characteristic transfer

Let a non-swap collision occur in `A_p`, and lift the four root exponents to
`x,y,u,v in mu_n(C)`. The just-proved theorem says

```text
alpha=(1-x)(1-y)-(1-u)(1-v)
```

is a nonzero algebraic integer. Reduction at the prime of `Q(zeta_n)` selected
by the chosen primitive root modulo `p` sends `alpha` to zero. Hence `p`
divides its rational norm. Every Galois conjugate has the six-root expansion

```text
alpha=xy-x-y-uv+u+v,
```

so its complex absolute value is at most `6`. Multiplying over the `phi(n)`
conjugates proves

```text
0<|Norm(alpha)|<=6^phi(n).
```

The transfer is per collision. It supplies no pair-coprimality or per-prime
aggregate bound, which is exactly the remaining C36' issue.

Finally, for every finite row and nonidentity `t`, write

```text
R(t)=1+(R(t)-1)
```

on quotient support and multiply by `Q(t)`. Summing proves `(AD)`. The Sidon
corollary shows that `R(t)-1` counts only finite-characteristic quotient
nonuniqueness. This interpretation adds no estimate to the exact identity.
