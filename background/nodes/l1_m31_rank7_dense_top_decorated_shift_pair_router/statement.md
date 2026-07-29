# M31 rank-seven dense top decorated shift-pair router

- **status:** PROVED
- **closure:** proof with independent exact-arithmetic replay sources
- **requires:** `l1_m31_rank7_zero_excess_two_block_incidence_router`
- **consumer:** `l1_mixed_petal_amplification` and the M31 LIST stress-row
  upper route

## Dense top stratum

Retain the exact residual constants

```text
N=1053557,  k=4981,  t=k-1=4980,
m=72428,    w=m-k=67447,    M0=2157929.
```

Let `S_i` be the exact combined agreement support of each member in a
zero-excess proper-`G` family of size `M>=M0`. Then

```text
|S_i|=m,                 |S_i intersect S_j|<=t.
```

More than one tenth of all unordered member pairs satisfy

```text
|S_i intersect S_j|=t.                                  (DS1)
```

Consequently some member has at least

```text
215793                                                   (DS2)
```

top-stratum neighbors.

## Exact Pade/shift-pair identity

Interpolate the combined received table by `U`, and write

```text
U-a_i=L_i C_i,
```

where `L_i` is the monic locator of `S_i`. For a pair in (DS1), put

```text
J=gcd(L_i,L_j),   L_i=J A,   L_j=J B.
```

Then

```text
deg J=t,
deg A=deg B=w+1=67448,
gcd(A,B)=1,
A C_i-B C_j=c in F^x.                                  (DS3)
```

In particular `gcd(C_i,C_j)=1`; a nonconstant common cofactor would divide
the nonzero constant. Thus all neighbors counted in (DS2) lie in the exact
primitive first-above-threshold decorated shift-pair stratum. A source-bound
local cap of `215792` for that stratum would contradict every violating
proper-`G` class.

## Scope

This theorem supplies a sharp local successor target, not its upper bound.
It does not pay `Q=147595`, produce a v4 atom, close the M31 LIST row, treat
higher ranks, or resolve either Prize problem.
