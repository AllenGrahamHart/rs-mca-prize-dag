# KoalaBear m2 r4 diagonal branch coefficient compiler

- **status:** PROVED
- **scope:** the two branches of an actual diagonal-order-two component
- **dependency:** `rate_half_kb_m2_r4_diagonal_source_subfield_dichotomy`
- **consumer:** `rate_half_band_closure`

The source-subfield dichotomy has the following exact coefficient forms.

## Source-line branch

Use the geometric coordinates

```text
b(X)=-X,       s(X)=1/X,       W=psi(X)=X^2,
tau(Z)=1/Z.
```

There are unique forms

```text
deg_(T,W) U <= (2,2),       deg_(T,W) V <= (2,1)
```

such that the source equation and endpoint equation satisfy, after scaling,

```text
H(T,X)=U(T,W)+X V(T,W),
G(T,W)=U(T,W)^2-W V(T,W)^2.                         (KBDC-1)
```

For one common `epsilon in {+1,-1}`,

```text
T^2 W^2 U(1/T,1/W)=epsilon U(T,W),
T^2 W   V(1/T,1/W)=epsilon V(T,W).                 (KBDC-2)
```

The `epsilon=+1` and `epsilon=-1` source spaces have dimensions eight and
seven. In both cases the endpoint biform is in the positive reciprocal
eigenspace:

```text
T^4 W^4 G(1/T,1/W)=G(T,W).                         (KBDC-3)
```

Thus a projective endpoint biform which is anti-reciprocal, or which has no
representation `(KBDC-1)--(KBDC-2)`, cannot belong to the source-line
branch.

## Biquadratic branch

View the endpoint equation over `F=K(W)` and divide by its nonzero leading
coefficient:

```text
g(Z)=Z^4+aZ^3+bZ^2+cZ+d.
```

Its cubic resolvent

```text
R(Y)=Y^3-bY^2+(ac-4d)Y+(4bd-a^2d-c^2)              (KBDC-4)
```

splits into three distinct linear factors over `F`, and `Disc(g)` is a
square in `F`. Conversely, for an irreducible separable quartic, complete
splitting of `(KBDC-4)` is equivalent to the quartic extension being
`V4`-Galois. Denominators may be cleared, so this is an exact coefficient
test over `K[W]`.

This compiler does not prove that every source-facet packet fails its
branch test. It proves no diagonal or order-two deletion, trivial type,
owner, payment, row, or Prize result.

## Falsifier

An actual lifting branch violating the norm, reciprocal, or positive
endpoint identities; an actual non-lifting branch whose cubic resolvent
does not split over `K(W)`; or an irreducible separable quartic with split
resolvent but non-`V4` Galois group.
