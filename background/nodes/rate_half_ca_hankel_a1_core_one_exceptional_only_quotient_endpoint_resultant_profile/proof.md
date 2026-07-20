# Proof

The two-sided saturation theorem says that every root `a` of the squarefree
exceptional locator `A` has exactly `e` distinct supported parameter roots in
`Q(z;a)`. One is the simple exceptional root `z=0`; the other `e-1` are
ordinary. Therefore `(QER2)` has a zero of multiplicity `2e=deg A` at zero,
and its multiplicity at an ordinary slope `zeta` is exactly

```text
a_zeta=|G_zeta intersect R_A|.                         (1)
```

All remaining factors are absorbed in the product of the nonzero leading
coefficients, denoted by `kappa`.

At the sharp endpoint, the first profile of the sharp-ceiling theorem has

```text
a_zeta=(e-1)/2=k_0
```

for every ordinary slope. Multiplying the linear factors with these
multiplicities proves `(QER3)`.

In the second profile, the minimal complement has exceptional intersection
size

```text
r-h=(e+1)/2=k_0+1,
```

the unique complement of size `3(e+1)/2+1` has intersection size
`(e-3)/2=k_0-1`, and every other intersection has size `k_0`. Thus

```text
R_A(z)=kappa z^(2e)P_ord(z)^k_0
       (z-z_min)/(z-z_max).                            (2)
```

The denominator in `(2)` cancels one of the factors already present in
`P_ord`; clearing it gives the polynomial identity `(QER4)`.

Both identities list the exceptional factor and every ordinary factor with
the multiplicity from `(1)`, so they are also complete multiplicity ledgers
inside their respective incidence profiles.

The two-sided saturation theorem gives the full factorization

```text
Res_X(P_X,Q)=c_X z^(r-1)P_ord^r
            =c_X z^(2e)P_ord^r.                       (3)
```

Resultant multiplicativity for `P_X=AH_A` says that `(3)` is the product of
`R_A` and `Res_X(H_A,Q)`. Divide `(3)` by `(QER3)` in the flat profile. The
`z^(2e)` factors cancel and `r-k_0=3(e+1)/2`, proving `(QER5)`.

In the swapped profile, divide `(3)` by `(2)`. The factor deviations reverse,
giving

```text
Res_X(H_A,Q)=kappa'P_ord^(r-k_0)
             (z-z_max)/(z-z_min).
```

Clearing the factor already present in `P_ord` proves `(QER6)`. QED.
