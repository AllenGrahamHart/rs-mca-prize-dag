# Proof

## Exact-layer line

The triple-overlap proof from the preceding top-third node does not require
`e<d`.  For an exact layer `h=e-r` with `r<=s`, any three inside agreement
sets share at least `e-3r>=K` coordinates.  Restriction injectivity puts the
entire selected layer on one affine codeword line

```text
a_gamma=A+gamma*p.
```

The condition `r>=r_0` is exactly `h<=m`; omitted higher deficits are
impossible.  Also `r<e/2`, so each explanation owns at most one slope.

## Two common-core caps

Write the transformed received line as `r_0+gamma*q`.  A coordinate is an
agreement for every member of the affine explanation line exactly when

```text
A=r_0       and       p=q
```

there.  If this total common core had at least `m` coordinates, the codeword
pair `(A,b+p)` would explain the received pair on an `m`-set, contradicting
pair noncontainment.  Thus its size `g` is at most `m-1`.  Away from the
core, each coordinate agrees for at most one line parameter.  Since every
selected explanation has at least `m` total agreements,

```text
L_r(m-g)<=N-g,
```

and hence `L_r<=N-m+1=t+1`.

If `A_r>c`, use the outside coordinates alone.  Their common core lies in
the zero set of the nonzero degree-`<K` line direction `p`, so it has size
at most `c`.  Outside-core packing gives

```text
L_r<=floor((n-c)/(A_r-c)).
```

For `A_r>c` this is no larger than `t+1`: after multiplying by
`A_r-c`, the difference is `t(A_r-c-1)+r>=0`.  This proves `(FC1)`.

## Profile and exact walls

Deficits through `H` use the same Johnson cumulative profile as before.
Splitting at `u=floor(e/2)` bounds the prefix by
`(e-1)J_u+J_H`.  The remaining possible exact layers are precisely
`r_0<=r<=s`; apply `(FC1)` with unit owner weight to prove `(FC2)`.

The primary verifier scans every newly paid support using exact integers
and quotient-grouped floor sums.  The independent audit checks the common
core packing on a finite model, recomputes endpoint line sums directly, and
uses separate uniform cap maxima to certify the KoalaBear strip.
