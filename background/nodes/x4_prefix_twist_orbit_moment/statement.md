# Prefix twist-orbit constancy and moment amplification

- **status:** PROVED
- **closure:** proof
- **upstream alignment:** independent replay of `prop:twist-orbit` and
  `prop:q-orbit-moment` in `rs-mca`'s archived `grande_finale_v2.tex`

Let a cyclic group `H` of order `N` act by multiplication on `D`. For the
depth-`t` elementary locator-prefix fibers `F_z` of `A`-subsets, multiplication
by `zeta in H` gives a bijection

```text
F_(z_1,...,z_t) -> F_(zeta z_1,zeta^2 z_2,...,zeta^t z_t).
```

Put `I(z)={i:z_i!=0}` and

```text
s(z)=N                         if z=0,
s(z)=gcd(N,{i:i in I(z)})      otherwise.
```

The twist orbit of `z` has exactly `N/s(z)` prefix values, all with the same
fiber size. If

```text
Q=|B|^t,
R(z)=Q |F_z| / binom(N,A),
Gamma_r=Q^(r-1) sum_y (|F_y|/binom(N,A))^r,
```

then for every integer `r>=2`,

```text
Gamma_r >= (N/s(z)) R(z)^r / Q.                    (TO-1)
```

Consequently `Gamma_r<=G` implies

```text
R(z) <= (G Q s(z)/N)^(1/r).                        (TO-2)
```

For `N=2^ell`, a nonzero prefix has
`s(z)=2^min_{i in I(z)} v_2(i)`. In particular, any nonzero odd-index
coordinate gives a full `N`-element orbit.
