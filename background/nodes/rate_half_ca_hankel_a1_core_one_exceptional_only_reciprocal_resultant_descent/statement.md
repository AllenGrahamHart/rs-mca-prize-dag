# `A=1` core-one exceptional-only reciprocal-resultant descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_unit_resultant_collapse`

Retain the corrected exceptional-only system. Put

```text
a=[X^r]Q=E q_bar,       j_inf=[X^(D_0-r)]J!=0,
q_(r-1)=[X^(r-1)]Q,     b_(D_0-1)=[X^(D_0-1)]B_1.   (RRD1)
```

Reverse `Q` and `B_1` at their proved fixed degrees:

```text
F(t,Y)=Y^r Q(t,1/Y),
G(t,Y)=Y^D_0 B_1(t,1/Y).                            (RRD2)
```

The infinity coefficients give `F(t,0)=E q_bar` and
`G(t,0)=-j_inf q_bar`. Therefore

```text
C(t,Y)=j_inf F(t,Y)+E G(t,Y)=Y L(t,Y),
Delta_inf=L(t,0)=j_inf q_(r-1)+E b_(D_0-1).         (RRD3)
```

Using the same nonzero scalar `c_X` as the two-sided and unit-resultant
theorems, the descended pair has the exact resultant

```text
Res_Y(F,L)=c_X E^(r-1).                              (RRD4)
```

Moreover,

```text
gcd(q_bar,Delta_inf)=1.                              (RRD5)
```

Thus the entire `q_bar` factor in `Res_Y(F,G)` is the removable common
point at reciprocal infinity. After its first Euclidean cancellation no
nonexceptional parameter factor remains, and at every root of `q_bar` the
first reciprocal coefficient `Delta_inf` is nonzero. This is an exact
one-step classification gate, not an exclusion of the corrected square or
a claim that `E` or `q_bar` is root-free.
