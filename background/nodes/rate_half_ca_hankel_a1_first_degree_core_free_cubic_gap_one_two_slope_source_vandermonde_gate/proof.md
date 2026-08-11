# Proof

At a supported slope `gamma`, the split-pencil theorem represents the
syndrome by an error on the roots of `Q_min,gamma`. Its minimal recurrence
has exact degree `rho-c_gamma`, so every source weight on those distinct
roots is nonzero. The rate-half RS code has minimum distance `2rho+1`, hence
a received word has at most one codeword center within radius `rho`. This
proves `(TSV2)`.

Choose an affine slope coordinate containing `alpha,beta` and write the
received pencil as `y(t)=y_0+t y_1`. Let `f_alpha,f_beta` be the unique
centers and set

```text
f(t)=f_alpha+(t-alpha)(f_beta-f_alpha)/(beta-alpha). (1)
```

This is a codeword-valued affine line. If
`e_gamma=y(gamma)-f_gamma`, then the derivative of `y-f` is

```text
h=(e_beta-e_alpha)/(beta-alpha).                    (2)
```

Every codeword has zero syndrome moments through degree `2rho-1`. Therefore
the derivative moment functional `dot Phi` used in `(FJP4)` may be computed
from `h`:

```text
dot Phi(F)=sum_(x in D)lambda_x h(x)F(x),
deg F<=2rho-1.                                      (3)
```

For the arguments in `(FJP4)`,

```text
deg(Q_min,alpha^2AB)
 <=2(rho-c_alpha)+(c_alpha-1)+c_alpha
 =2rho-1,                                           (4)
```

so `(3)` applies. The vector `h` vanishes outside
`S_alpha union S_beta`. The factor `Q_min,alpha^2` kills every term on
`S_alpha`. At a point of `S_beta\S_alpha`, equation `(2)` gives
`h(x)=e_beta(x)/(beta-alpha)`, and every factor in `(TSV4)` is nonzero.
Equations `(3),(4)` now prove `(TSV3)--(TSV5)`.

The first-jet theorem gives `rank B_alpha=c_alpha`. A bilinear form written
as a sum of `m` evaluation rank-one forms has rank at most `m`. Applied to
`(TSV3)`, this proves `(TSV6)`.

Suppose equality holds and list the `c_alpha` distinct points of
`S_beta\S_alpha`. The evaluation matrix of polynomials of degree at most
`c_alpha-1` on those points is a square nonsingular Vandermonde matrix. The
right-radical identity from `(FJP5)` says

```text
sum_x mu_x A(x)R_alpha(x)=0                         (5)
```

for every such `A`. Invert the Vandermonde matrix in `(5)`. Since every
`mu_x` is nonzero, `R_alpha(x)=0` at all `c_alpha` points. Its degree is
`c_alpha`, proving `(TSV7)`.

In a `w=0` packet, first-jet transversality has no exceptional slope. For a
pair with positive `c_alpha`, `(TSV6)` and `(TSV2)` give

```text
|S_alpha intersect S_beta|
 <=|S_beta|-c_alpha
 =rho-c_alpha-c_beta.                               (6)
```

The same inequality is trivial when both losses are zero, and follows from
the positive-loss direction when only one is positive. Hence

```text
|S_alpha union S_beta|
 =2rho-c_alpha-c_beta-|S_alpha intersect S_beta|
 >=rho,                                             (7)
```

which is `(TSV8)`. Equality in `(7)` makes each set difference have size
equal to the opposite lower bound, and `(TSV7)` applies in every
positive-loss direction. Projective coordinate changes rescale all moments
by units and do not change ranks, radicals, or support sets. QED.
