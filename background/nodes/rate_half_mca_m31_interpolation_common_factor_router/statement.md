# Mersenne interpolation common-factor router

- **status:** PROVED
- **scope:** Mersenne full-lift support `e=130237`
- **residual:** positive-degree common interpolation factor

On the gauged inside support, let `I_264` be the vector space of polynomials
of weight at most 264 for weights `(1,5,5)` on `(X,Y,Z)` that vanish at every
received point `(x,r_0(x),r_1(x))`.  Then

```text
dim I_264 >= 131175-130237 = 938.
```

If an unsafe family exists, recursive capped-core peeling forces 2,705
distinct affine explanation-line pairs `(a_i,b_i)`.  Every pair is a common
zero of `I_264` over `F(X)`.  Since every kernel member has total `(Y,Z)`
degree at most 52, two coprime members have at most `52^2=2704` common zeros.
Consequently all members of `I_264` share a factor of positive `(Y,Z)` degree
over the algebraic closure of `F(X)`.

The coprime interpolation branch is therefore paid.  The common-factor
branch remains open and must be classified or charged; this node does not
identify every such factor with a split pencil.
