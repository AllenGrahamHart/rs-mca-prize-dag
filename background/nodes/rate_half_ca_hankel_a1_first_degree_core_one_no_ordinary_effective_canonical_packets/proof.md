# Proof

Fix a packet in `(NOE1)`. Let

```text
C_tot=sum_gamma c_gamma=Delta-w,
0<=w<=v.                                               (1)
```

The distinguished row has `d_*=e-c` supported incidences, each consuming at
least one rank-loss degree. Thus the rank-loss budget outside those baseline
copies is at most

```text
p=C_tot-d_*=u-w<=2.                                    (2)
```

At one distinguished point let `b` be zero or one according as `x_*` is
outside or inside `Q_min`, and let `r>=1` be its multiplicity in the excess
factor. The horizontal intersection multiplicity is

```text
m=b+r.                                                 (3)
```

Equation `(2)` gives `m<=4`. If `n` is the positive vertical intersection
multiplicity, the local cube identity gives

```text
m+n=0 mod 3.                                           (4)
```

For `m=1,2,3,4`, the least possible `n` is respectively `2,1,3,2`; in every
case

```text
2n>=m.                                                 (5)
```

The same inequality is immediate at an unsupported vertical point, where
`m=0` and `n` is a positive multiple of three.

Let `K_*` be the total contact multiplicity on the distinguished fibre and
let `O_*` be the omission contributed by the excess roots at `x_*`. Summing
`3k=m+n` over that fibre gives

```text
K_*-d_*=(O_*-e+2c)/3.                                  (6)
```

The omission outside the distinguished roots is at most the rank-loss
budget outside their baseline copies. Therefore

```text
O_*>=O-p
    =(Delta-v)-(u-w)
    =e-4+u-u+w=e-4+w.                                  (7)
```

Substitute `c=2+u` into `(6),(7)`:

```text
K_*-d_*>=(2u+w)/3.                                    (8)
```

The left side is an integer. It is at least one for `u=1` and at least two
for `u=2`; for `u=0` it is nonnegative. The total residual contact degree is
exactly `u`. Hence equality of available degrees forces all of `E_u` onto
the distinguished fibre (trivially also when `u=0`).

At a supported point, the coefficient of `Z_c-E_u` is

```text
(n-1)-(k-1)=n-k=(2n-m)/3>=0                           (9)
```

by `(5)`. At an unsupported point it is
`n-k=2n/3>=0`. Thus `H_2=Z_c-E_u` is effective. Its degree is

```text
c-u=2,                                                 (10)
```

and the signed Picard relation becomes `(NOE3)`.

It remains to identify the pushforward orbit. The effective divisor `H_2`
is a proper subdivisor of the vertical fibre: locally its coefficient is
`n-k<n`. Hence the length-two quotient

```text
O_C(H_2)/O_C
```

is annihilated by the base uniformizer, and the corresponding subspace
`t pi_*O_C(H_2)/t pi_*O_C` lies in the nilpotent ideal of the fibre algebra
supported on `H_2`. It vanishes on the other `d_*>0` reduced supported
factors and therefore has zero intersection with the constant line. Its
projection to the negative block has rank two. The elementary-modification
classification gives `(NOE4)`. QED.
