# Proof

Let `c_x=e-d_x` be the row deficits and

```text
C=sum_(x in D\S)c_x.
```

There are `h_j` heavy rows with `c_x>j`. Bound each of their deficits by
`e` and every other deficit by `j`. The ambient factorization gives

```text
C<=h_j e+(N-s-h_j)j.                                  (1)
```

The exact ledger gives

```text
C=ell d+eta-Delta+O>=ell d+eta-Delta.                 (2)
```

At the first degree, write `rho=3e-1`.

## Core zero

Here

```text
d=3e-1,       N=12e-4,       eta=Delta=2e-1,
ell=e-3+j.                                              (3)
```

Put `h_j=d-3-a_j=3e-4-a_j`. Substituting `(3)` into `(1),(2)` and
simplifying gives

```text
a_j(e-j)<=6e-3+j(6e+1).                               (4)
```

For `j=0,1,2`, the floors of the right side divided by `e-j` are
respectively

```text
5, 12, 18,                                             (5)
```

because the divisions are

```text
6e-3       =5e+(e-3),
12e-2      =12(e-1)+10,
18e-1      =18(e-2)+35,
```

and the official `e` is larger than every displayed remainder.

## Core one

Now

```text
d=3e-2,       N-1=12e-5,       eta=e,
Delta=e-2,    ell=e-2+j.                              (6)
```

Put `h_j=d-3-a_j=3e-5-a_j`. The same substitution gives

```text
a_j(e-j)<=3e-6+j(6e+2).                               (7)
```

The three divisions are

```text
3e-6       =2e+(e-6),
9e-4       =9(e-1)+5,
15e-2      =15(e-2)+28,                              (8)
```

so their floors are `2,9,15`. This proves `(BRT2)` and hence `(BRT3)` and
`(BRT4)`. QED.
