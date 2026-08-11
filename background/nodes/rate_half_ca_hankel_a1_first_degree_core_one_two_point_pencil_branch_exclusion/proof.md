# Proof

Let `R` be the DVR of the domain line at `x_*`, with uniformizer
`t=X-x_*`, and put

```text
E=pi_*O_C,       K=pi_*O_C(P_alpha+P_beta).
```

The two-point normal form says that the vertical fibre consists of `e-4`
simple points and two points of vertical intersection multiplicity two. The
local cube calculation gives contact multiplicity one at the latter points,
so they are smooth Cartier points of `C`. Choose local parameters
`s_alpha,s_beta`. Up to units,

```text
t=s_alpha^2 at P_alpha,
t=s_beta^2 at P_beta.                                 (1)
```

The fibre algebra `A=E/tE` therefore contains the two local factors

```text
Fbar[s_alpha]/(s_alpha^2),
Fbar[s_beta]/(s_beta^2),                               (2)
```

together with the `e-4` reduced factors.

The quotient `K/E` is `k_(x_*)^2` and is killed by `t`. For a positive
elementary modification, the corresponding two-dimensional subspace of the
fibre is

```text
W=tK/tE subset E/tE=A.                                (3)
```

Locally `O_C(P_alpha)=s_alpha^(-1)O_C`, so multiplication by `t=s_alpha^2`
shows that its direction in `(3)` is the class of `s_alpha`; similarly the
other direction is `s_beta`. Hence

```text
W=span(s_alpha,s_beta).                                (4)
```

Every element of `W` vanishes in all `e-4` reduced factors of `A`. The
constant class `1` is nonzero in each such factor. Since `e-4>0`,

```text
W intersect Fbar*1=0.                                 (5)
```

The natural `O` summand in

```text
pi_*O_C=O direct_sum O(-d)^(e-1)
```

is precisely the constant line. Equation `(5)` says that projection of `W`
to the negative fibre has rank two. The pushforward dichotomy identifies
that orbit with the CANONICAL splitting `(PBE1)`, whose section count is
one. This proves `(PBE2)` and excludes the PENCIL branch. QED.
