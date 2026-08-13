# Mersenne common-factor base-field component descent

- **status:** PROVED
- **scope:** the higher-degree full-gcd branch at Mersenne `e=130237`
- **residual:** a base-field component union carrying almost all factor mass

Let `F=F_(p^4)` with `p=2^31-1`, put `K=F(X)`, and let `P` be the
primitive full interpolation gcd with

```text
2<=d=deg_(Y,Z)(P)<=43.
```

Factor the radical of `P` into geometric irreducible components.  The
union `P_K` of the components individually defined over `K` contains at
least `5079` of the selected `K`-rational polynomial pairs.  In
particular, one absolutely irreducible `K`-component contains at least
`132` selected pairs.

The size-`807` cores of the pairs on `P_K` force

```text
#{x in E:P_K(x,r_0(x),r_1(x))=0}>=126263.
```

Thus the base-field component union has at most `3974` exceptional inside
coordinates.  This does not classify any component or assert that `P` is
irreducible.
