# Proof

The Euler gate gives

```text
TU^3+d=0 mod V.                                       (1)
```

Over an algebraic closure, evaluate `(1)` at every root `alpha` of the monic
`V`, with multiplicity, and multiply. This gives

```text
product_alpha T(alpha) product_alpha U(alpha)^3=(-d)^v,
```

which is `(GCN2)`. The proved `gcd(V,TU)=1` makes both resultants on the left
nonzero.

The official integer `d=2^39` is the cube of `2^13`, while `v` is even.
Hence `(-d)^v` is a nonzero cube. The second factor on the left of `(GCN2)`
is already a cube, proving `(GCN4)`.

If `T=t_1(Y-tau)`, then

```text
Res(V,T)=t_1^v product_alpha(alpha-tau)
        =t_1^v(-1)^vV(tau)
        =t_1^vV(tau).                                 (2)
```

Also `2^36=1 mod 3`, so `v=2^36-2=2 mod 3`. Thus `t_1^v` and `t_1^2`
represent the same cube class, proving `(GCN5)`.

The multiplicative group of a finite field is cyclic. If `q=1 mod 3`, its
cube subgroup is exactly the kernel of exponentiation by `(q-1)/3`, proving
`(GCN6)`. If `q=2 mod 3`, three is coprime to `q-1`, so cubing is an
automorphism and the scalar condition is automatic. QED.
