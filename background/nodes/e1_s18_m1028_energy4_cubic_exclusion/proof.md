# Proof

At energy four, the integral autocorrelation magnitudes have one of two
profiles: four signed units, or one coefficient of magnitude two. The second
profile has zero parity autocorrelation, whereas local valuation two requires
that parity autocorrelation to have multiplicity four at `X=1`. Hence only
four signed unit lags remain:

```text
x_u=sum_(j=1)^4 epsilon_j
       (zeta_256^(u d_j)+zeta_256^(-u d_j)),         (1)
```

where `1<=d_1<...<d_4<=63`.

Modulo two, `(1)` has parity polynomial

```text
sum_j (X^d_j+X^(128-d_j)).                          (2)
```

The verifier imposes multiplicity exactly four on `(2)` by Lucas' criterion
for Hasse derivatives. Since `257` divides the norm, `(1)+18` vanishes at a
primitive 256-th root modulo `257`. Diagonal Galois action normalizes that
root to `3`, so the complete necessary screen is

```text
18+sum_j epsilon_j(3^d_j+3^(-d_j))=0 mod 257.       (3)
```

Among all `C(63,4)` lag sets, 134,720 have multiplicity four. Screening all
16 sign assignments in `(3)` leaves exactly 8,385 types.

For a retained type, let `Omega={+/-d_1,...,+/-d_4}`, assigning coefficient
`epsilon_j` to both orientations. The conductor-256 Ramanujan sum over odd
exponents is

```text
c_256(t)=128  if t=0 mod 256,
         -128 if t=128 mod 256,
         0    otherwise.
```

Summing over one representative from each conjugate pair therefore gives

```text
sum_u x_u^3=64K,                                    (4)
```

where `K` is the signed number of ordered triples in `Omega` summing to zero,
minus the signed number summing to `+/-128`. The verifier computes `K` both
directly and from the independent relation ledger

```text
d_i+d_j=d_k,       d_i+d_j+d_k=128,
2d_i=d_j,          2d_i+d_j=128.
```

The exact distribution is

```text
K:     -36 -30 -24 -18 -12  -6    0   6  12 18 24
count:   1   1  13  38 478 704 5860 755 477 45 13.
```

In particular `K<=24`, so `(4)` gives

```text
sum_u x_u^3<=1536.                                  (5)
```

For every `t>-1`,

```text
log(1+t)<=t-t^2/2+t^3/3.                            (6)
```

Indeed, the derivative of the right side minus the left side is
`t^3/(1+t)`, and the difference vanishes at zero. With

```text
sum x_u=0,
sum x_u^2=128E=512,
```

equations `(5)--(6)` yield

```text
log Norm
 <=64log(18)-512/(2*18^2)+1536/(3*18^3)
 =64log(18)-512/729.                                (7)
```

Finally the positive cubic exponential Taylor polynomial proves exactly

```text
exp(512/729)>18^64/(1028*p_min).                    (8)
```

Equations `(7)--(8)` imply `Norm<1028*p_min`, contradicting an official-row
cofactor-1028 collision. QED.
