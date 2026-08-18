# Quadratic survivor Mobius router

- **status:** PROVED
- **scope:** the synchronized survivor emitted by the nonzero
  affine-reflection mass router

Either an admissible packet has

```text
chi>=2299571,
```

or one first-owned pair type has at least `4370` pairwise-disjoint split
fibers in one fixed coprime pencil of degree `e in {1,...,11}` outside the
normalized nonzero affine-reflection class.

If `e!=2`, retain that degree as an unclassified survivor. If `e=2`, there
is a unique nonidentity base-field Mobius involution interchanging the two
roots of every fiber. It has a trace-zero presentation

```text
phi(x)=(c-a*x)/(a+b*x),       Delta=a^2+b*c!=0.       (QM1)
```

Exactly one of the following quadratic classes occurs.

1. `b=0`: the involution is `phi(x)=s-x`. The nonzero case was already
   removed, so `s=0` and the survivor is antipodal.
2. `b!=0` and `a=0`: for `kappa=c/b in H`, the involution is the
   constant-product map `phi(x)=kappa/x`.
3. `a*b!=0`: with

   ```text
   tau=a/b,       kappa=Delta/b^2,
   phi(x)+tau=kappa/(x+tau),                         (QM2)
   ```

   both parameters are nonzero base-field elements and the shifted-inversion
   graph has at least `8740` distinct nonfixed points in the official domain.

Thus no extension-field normalization ambiguity remains in degree two. The
shifted-inversion intersection, the two global quotient classes, every
degree other than two, and the high-complexity output remain unpaid.

## Falsifier

A quadratic synchronized pencil whose locators do not span dimension two;
a common involution not defined over the base field; failure of `(QM2)`;
a constant-product fiber with `kappa` outside `H`; fewer than two graph
points per disjoint fiber; or any assertion that this classification pays a
surviving class.
