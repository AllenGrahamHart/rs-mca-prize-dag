# Proof

Fix a core plane `A` and a pairwise distinct-`phi` triple `x,y,z`.  For
`i in {x,y,z}` write

```text
V_i(c)=E_i+lambda_i(c)W_i,                          (1)
```

where `lambda_i` is affine linear on `A`.  The vectors `V_i(c)` never vanish,
and the three projective points `[W_i]` are pairwise distinct.

## Positive-dimensional components

Let `C` be an irreducible positive-dimensional component on which

```text
[V_x]=[V_y]=[V_z]=rho.                              (2)
```

The common ray `rho` is constant on `C`.  Otherwise, after passing to the
projective normalization of `C`, it is a nonconstant map to `P^1`.  For each
`i`, nonconstancy forces `E_i,W_i` to be independent and `lambda_i` to be
nonconstant.  The map

```text
t -> [E_i+tW_i]
```

is then a projective automorphism.  Its inverse expresses `lambda_i` as a
Mobius function of `rho` with its unique pole at `[W_i]`.

The four affine functions `1,lambda_x,lambda_y,lambda_z` live in the
three-dimensional space of affine-linear functions on `A`, so they satisfy a
nontrivial linear relation.  Pull it back through `rho`.  At a place above
`[W_x]`, only the `lambda_x` term has a pole, hence its coefficient is zero.
The distinct poles `[W_y]` and `[W_z]` kill the other two coefficients, and
then the constant coefficient is zero.  This contradicts nontriviality.

Thus every positive-dimensional component carries one fixed selected ray.
The high-depth first-match same-ray interaction strip allows at most one
target parameter on each such component.

## The three-point cap

Put

```text
F_y=det(V_x,V_y),       F_z=det(V_x,V_z).
```

Both have degree at most two.

If they have no common positive-dimensional component, then either one has
degree at most one, giving at most two affine intersections, or both are
genuine conics.  In the latter case their top forms are nonzero multiples of
`L_xL_y` and `L_xL_z`, so they share a point at infinity.  Bezout leaves at
most three affine intersections.

If their common gcd has degree one, its component contains at most one target
and the two residual lines have at most one common point off it.  If the gcd
has degree two, it has at most two irreducible components and no residual
intersection, hence at most two targets.  If one determinant is identically
zero, the other has at most two irreducible components; if both vanish
identically, the whole plane has a constant common ray.  These cases also
contain at most two and one targets respectively.

Therefore every fixed core plane and pairwise distinct-`phi` triple owns at
most three target parameters, without a direction-evaluation genericity
hypothesis.

## Incidence and official arithmetic

The triple router already proves that every selected block supplies at least

```text
r(r-ell)(r-2ell)/6
```

pairwise distinct-`phi` triples and that every target owns at least two
selected blocks and `B_(s-2)` independent core cuts.  Applying the
unconditional three-point cap gives `(ACP1)`, and the same binomial
cancellation gives `(ACP2)`.  The exact integer inequalities used for
`(APT3)` are unchanged.

It remains to optimize over `ell`.  Put `x=d+ell`, `a=h-x`, and

```text
E=x-2ell-1.
```

At fixed `x`, the `ell`-dependent factor in `(ACP2)` is

```text
f(ell)=E(E-1)(E-2)/((a+ell)a(a-ell)).               (3)
```

The ratio `f(ell+1)<=f(ell)` is equivalent to

```text
D=6(E-2)(a^2-ell^2)-E(E-1)(2ell+1)>=0.             (4)
```

The active-defect/syzygy constraint and `x<=4h/5` give the nonnegative
integer slacks

```text
q=3x-2h-1-4ell,       t=4h-5x,       u=ell-1.
```

After substitution, `2D` is

```text
72u^3+120u^2q+132u^2t+228u^2
+50uq^2+92uqt+244uq+38ut^2+272ut+222u
+6q^3+15q^2t+51q^2+12qt^2+96qt+120q
+3t^3+39t^2+135t+63,
```

which is positive.  Hence `ell=1` is worst throughout `x<=4h/5`.
The rate-`1/4,1/8` cutoff from `(APT3)` lies below `4h/5`, so it applies to
every `ell` with `r>2ell`.  At rate `1/16`, `floor(4h/5)=3,435,973,837`
gives the uniform cutoff, while the direct `ell=1` arithmetic retains its
larger endpoint.  This proves `(ACP3)`.  QED.
