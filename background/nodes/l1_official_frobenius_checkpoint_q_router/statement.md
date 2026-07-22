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

## Scope

This theorem is global in depth but proves no max-fiber estimate. A future
p-free power-sum theorem must retain or uniformly condition on the at most 23
checkpoints. Raw union over `q^r` checkpoint values is not paid, and the
positive-cofactor targets still require collective Pade-graph control. The
special F2 summit is a possible technique source, not a proved supplier.
