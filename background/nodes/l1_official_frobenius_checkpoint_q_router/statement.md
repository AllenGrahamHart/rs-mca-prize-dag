# L1 official Frobenius-checkpoint Q router

- **status:** PROVED
- **role:** replace arbitrary-depth locator prefixes by p-free power sums and
  a uniformly bounded checkpoint ledger
- **consumer:** `l1_mixed_petal_amplification`

## Official checkpoint bound

Use the official generated-field setup and write `p=char(F)`. The order bound
and strict field cap give

```text
f>=n/(p+1),       f log_2 p<256.                       (FQ1)
```

The proved lower bound `p>=3583` implies `log_2 p>11`, hence

```text
p>=11n/256>n/24.                                      (FQ2)
```

Consequently every prefix depth `d<=n-1` contains at most

```text
r=floor(d/p)<=23                                      (FQ3)
```

positive multiples of the characteristic.

## Mixed prefix coordinates

For a root set `A` and `1<=j<=d`, put

```text
E_j(A)=the j-th elementary symmetric function,
S_j(A)=sum_(x in A) x^j,
C_j(A)=S_j(A) if p does not divide j,
       E_j(A) if p divides j.                         (FQ4)
```

On monic degree-`a` polynomials with `a>=d`, the map

```text
(E_1,...,E_d) <-> (C_1,...,C_d)                       (FQ5)
```

is a triangular polynomial coordinate equivalence. Thus every depth-`d`
locator-prefix fiber is exactly one mixed prefix fiber consisting of the
p-free power sums and at most 23 elementary-symmetric Frobenius checkpoints.

Applying `l1_exact_shell_fixed_cofactor_prefix_transport`, every exact-shell
fixed-cofactor cell at every depth is a subset of one such mixed Q fiber; the
scalar top shell is exactly that fiber. When `d<p`, the checkpoint ledger is
empty and `(FQ5)` reduces to the ordinary Newton window.

## Coarse-fiber and union accounting

Let `Fib_mix(s,c)` fix the p-free power-sum vector `s` and the checkpoint
vector `c`, and let `Fib_free(s)` forget `c`. Then

```text
Fib_mix(s,c) subset Fib_free(s),
Fib_free(s)=disjoint union_c Fib_mix(s,c).             (FQ6)
```

Thus a max-fiber theorem proved directly for the larger coarse p-free fiber
transfers to every mixed fiber with **no checkpoint loss**. This is a
strictly stronger alternative to proving a bound uniformly after
conditioning on the checkpoint values.

There are at most `q^r` ambient checkpoint vectors. The official cap and
`n>=2^13` give

```text
q^r<2^(256*23)=2^5888<n^453.                           (FQ7)
```

Consequently a uniform conditional bound `|Fib_mix(s,c)|<=M` implies the
qualitative polynomial estimate

```text
|Fib_free(s)|<n^453 M.                                 (FQ8)
```

This does not pay the finite prize ledger. If `r>=1` and `M>=1`, the raw
right side `q^r M` is at least `q`, so that bound cannot imply
`q^r M<=q/2^128`. Any prize-facing proof must therefore use direct coarse
p-free flatness, retain the realized checkpoint in each owned cell, or
coalesce checkpoint values inside the collective Pade-graph theorem.

## Scope

This theorem is global in depth but proves no max-fiber estimate. A future
p-free power-sum theorem may bound the coarse fiber directly, or retain and
uniformly condition on the at most 23 checkpoints. Raw union over `q^r`
checkpoint values preserves only a qualitative polynomial statement; it is
not paid by the finite prize threshold. The positive-cofactor targets still
require collective Pade-graph control. The special F2 summit is a possible
technique source, not a proved supplier.
