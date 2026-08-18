# Dimension-two common-core shortening

- **status:** PROVED
- **scope:** the scalar-dimension-two output of the quotient pair-pencil
  direction router

Let `J` be the complete received-pair core common to all selected quotient
types. Then

```text
|J|>=ceil((38*134940-2097152)/37)=81908.             (CS1)
```

More precisely, choose one pair of types for each of 38 projectively
distinct scalar directions and let `I_l` be its pair-core intersection.
Then

```text
I_l intersection I_r=J       for l!=r,              (CS2)
38*134940-37|J|<=2097152.                            (CS3)
```

Subtract the common codeword pair on `J`, puncture `J`, and divide both the
received values and every explanation by the nonzero squarefree-locator
values. This reversibly shortens

```text
(n,K,m) -> (n-|J|,K-|J|,m-|J|),
```

preserves `m-K=67472`, all first-owned records, and quotient pair cores of
size `(m-|J|)-2`.

Thus the live alternative is:

1. scalar dimension three or four; or
2. a chronology-preserving common-core shortening by at least 81908.

## Falsifier

A dimension-two scalar family whose 38 direction intersections do not share
one core; a smaller common core; overlap of two residual direction petals;
or failure of the reversible shortening and invariant excess.
