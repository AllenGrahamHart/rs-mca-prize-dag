# Cross-type scalar-pair rigidity

- **status:** PROVED
- **scope:** a sharp 28-record collision deck between two distinct
  pole-simple heavy-ruling pair types after common-core shortening

Let two distinct scalar-locator certificates share `r=28` exact supports,
with 14 records owned by each of two distinct saturated pair types. Write
their scalar coefficient pairs as

```text
s=(c_0,c_1),       s'=(c'_0,c'_1).
```

Then `s` and `s'` are proportional. Indeed, if they were linearly
independent, pole-simplicity would strengthen the atom-collision incidence
count to

```text
|G\H| >= ceil((28m'-n')/27) = 1079711-c,             (SP1)
```

where `(n',m',K')=(n-c,m-c,K-c)`. Every point of `G\H` lies in both pair
cores, but distinct Reed--Solomon pairs have core intersection at most

```text
K'-1=1048575-c.                                      (SP2)
```

The contradiction margin is the shortening-invariant value

```text
(1079711-c)-(1048575-c)=31136.                       (SP3)
```

For a degree-two split pencil

```text
u+gamma v=(c_0+c_1 gamma)L_(E_gamma),
f=-u/v,
```

the projective value at infinity is `f(infinity)=[-c_0:c_1]`. Thus every
surviving cross-type quadratic collision has the same value at infinity in
the two quotient coordinates.

This theorem removes the independent-normalization branch only. It does not
construct a 28-record deck for every pair of quotient types, identify the
two quotient maps, bound the number of proportional-scalar types, or pay the
520-type quotient population.

## Falsifier

An independent pair `s,s'` whose common-zero set `H` is not contained in the
common denominator roots; a point of `H` lying in two shared supports without
violating pole-simplicity; failure of `(SP1)` under shortening; or a surviving
independent-scalar collision between distinct pair types.
