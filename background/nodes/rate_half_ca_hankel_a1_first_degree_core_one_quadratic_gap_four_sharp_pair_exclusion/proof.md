# Proof

Assume for contradiction that distinct supported slopes `alpha,beta` obey

```text
|S_alpha union S_beta|=rho+2.                       (1)
```

The minimum-pair clone theorem applies. In one orientation, put

```text
sigma=alpha,       tau=beta,
X=S_tau\S_sigma,   |X|=r_sigma+2.                   (2)
```

The residual row forms at all `x in X` are proportional to one squarefree
degree-`e` supported-slope form `P`. Let `B` be its root set. Then

```text
|B|=e,       tau in B,       sigma notin B,          (3)
```

and every `x in X` belongs to `S_delta` for every `delta in B`. The last
assertion uses that every member of `X` is light: the only padded roots are
the named heavy rows.

We may choose an orientation for which every center indexed by `B` lies on
the projective codeword pencil through the centers at `alpha,beta`. To see
this, let `H` be the global set of padded heavy rows. It has size one in the
double-root arm and size two in the two-simple arm. Put

```text
U=S_alpha union S_beta,       |U|=rho+2.             (4)
```

For `delta in B`, the full locator `E_delta` contains `X` and the fixed core
point `s_0`. Also

```text
E_alpha union E_beta subseteq U union H.
```

Therefore

```text
|E_alpha union E_beta union E_delta|
 <=2rho+|H|-r_sigma-1.                              (5)
```

In the double-root arm, `|H|=1`, so `(5)` is at most `2rho` in either
orientation. In the two-simple arm, choose as `sigma` an endpoint with
`r_sigma>=1` if one exists; then `(5)` is again at most `2rho`. If both
endpoint deficits vanish, neither endpoint locator has a padded root, so
`E_alpha union E_beta=U`; using `|X|=2` directly improves `(5)` to
`2rho-1`.

The rate-half code has minimum distance `2rho+1`. Thus, in the selected
orientation, every `delta in B` has its assigned center on the codeword
pencil through the two endpoint centers. Put

```text
A={sigma} union B,       |A|=e+1.                   (6)
```

Subtract that codeword pencil from the received pencil. Its joint support
is exactly `U`: at the two distinct endpoint slopes its supports are
`S_alpha,S_beta`, and a nonzero projective linear coordinate cannot vanish
at both endpoints. Hence

```text
S_gamma subseteq U       for every gamma in A.      (7)
```

Remove the fixed core point and write `U_0=U\{s_0}`. Every point of `U_0`
is light, so it belongs to exactly `e` supported locators globally. On the
other hand, each nonzero residual coordinate is a projective linear form in
the slope and vanishes at at most one of the `e+1` slopes in `A`. It follows
that every point of `U_0` occurs in exactly `e` supports indexed by `A`, is
missing from exactly one of them, and occurs nowhere outside `A`.

Count missing incidences in `U_0 x A`. Since `|U_0|=rho+1`, the point count
is `rho+1`. For a fixed `gamma in A`, equations `(7)` and
`|S_gamma|=rho-r_gamma`, with `s_0 in S_gamma`, give

```text
|U_0\S_gamma|=(rho+1)-(rho-r_gamma-1)=r_gamma+2.
```

Therefore

```text
sum_(gamma in A)(r_gamma+2)=rho+1,
sum_(gamma in A)r_gamma=rho+1-2(e+1)=e-2.           (8)
```

But in both quadratic arms the packet-wide deficit is exactly

```text
sum_(all supported gamma)r_gamma=e-6:               (9)
```

in the double-root arm this is the degree of `x_*`, and in the two-simple
arm it is `|Z_1|+|Z_2|`. Since all deficits are nonnegative, `(8)` cannot
exceed `(9)`. The contradiction proves `(QSX1)`.

Now let a codeword pencil contain `h>=2` assigned centers and let `V` be the
joint support after subtraction. Any two of its endpoint errors have union
inside `V`, so `(QSX1)` gives `|V|>=rho+3`. Every nonzero projective linear
coordinate is present at at least `h-1` of the selected slopes. Hence

```text
(h-1)(rho+3)
 <=sum_(gamma in A)|S_gamma|
 =h rho-sum_(gamma in A)r_gamma.
```

Rearranging proves `(QSX2)`.

Finally fix `alpha,beta`. As in the preceding center-spread theorem, every
third slope whose full locator triple has union at most `2rho` has its
center on the codeword pencil through the first two centers. Equation
`(QSX2)` bounds the total number of centers on that pencil by

```text
floor((rho+3-r_alpha-r_beta)/3).
```

Subtracting from `T=rho+4` gives

```text
T-floor((rho+3-r_alpha-r_beta)/3)
 =ceil((2rho+9+r_alpha+r_beta)/3),
```

which proves `(QSX3)--(QSX4)`. QED.
