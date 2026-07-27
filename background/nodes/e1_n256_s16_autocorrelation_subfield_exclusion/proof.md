# Proof

Put `K=Q(zeta_256)` and `alpha=F(zeta_256)`. The profile has coefficient
square mass 16. If

```text
E=sum_(d=1)^63 A_d^2=V/2=38,
L=sum_(d=1)^63 |A_d|,
```

then the profile-specific chord inequality gives `4L<=E+66`, initially
`L<=26`. In the exact relaxed slack recurrence from the sparse-L1 parent,
the candidates `L=26,25,24,23` have global slacks `0,4,8,12` and relaxed
minimum energies `54,50,46,42`, respectively. All exceed 38. Hence

```text
L<=22.                                                   (2)
```

For every odd `u`, put `y_u=|F(zeta_256^u)|^2`. The autocorrelation
expansion and (2) give

```text
y_u=16+sum_(d=1)^63 A_d(zeta_256^(ud)+zeta_256^(-ud)),
0<=y_u<=16+2L<=60.                                      (3)
```

Assume now that `A_d=0` unless `4|d`. With `eta=zeta_256^4`, define

```text
beta=alpha conjugate(alpha)
    =16+sum_(4|d) A_d(eta^(d/4)+eta^(-d/4)).             (4)
```

Thus `beta` belongs to `L_0=Q(eta)=Q(zeta_64)`, of degree 32, while
`[K:L_0]=4`. The collision-norm criterion makes `alpha` nonzero, so `beta`
and its small-field norm

```text
N=Norm_(L_0/Q)(beta)
```

are nonzero. Every embedding of `L_0` lifts to an odd-character embedding of
`K`, so its value on `beta` is one of the conjugate squares in (3). Therefore

```text
0<|N|<=60^32<2^250.                                    (5)
```

Let `R=Norm_(K/Q)(alpha)`. Complex conjugation is an automorphism of `K`,
so its application does not change the rational norm. Taking norms in (4)
and using the tower law gives

```text
R^2=Norm_(K/Q)(beta)=N^[K:L_0]=N^4.
```

Hence `|R|=|N|^2`, and every rational prime dividing `R` also divides `N`.
No prime `p>=2^250` can do so by (5). The collision-norm criterion therefore
excludes every candidate satisfying (1).

The weighted-layer configuration with absolute third-moment count 2718 from
the `E=38` route report is supported entirely on multiples of four, so it is
removed by this theorem. No conclusion is drawn for nonperiodic
autocorrelation support.
