# Proof

Fix `x in M_alpha`. Its source form vanishes at `alpha`, while `x` belongs
to `S_beta`, so the light locator row `Qbar(t;x)` vanishes at `beta`.
Therefore `omega_xQbar(t;x)` is divisible by `Lambda_2`. Its quotient has
exact degree `e-1`, and its roots are the `e-1` off-line supported slopes
whose supports contain `x`. The same argument applies to `M_beta`.

If `x` lies in neither missing set, its locator row vanishes at both
endpoints. Division by `Lambda_2` and multiplication by its linear source
again gives a polynomial of degree at most `e-1`. This proves the
polynomial assertion in `(STB2)` and the row-root claim in `(STB5)`.

The fixed-line source representation and global locator equation give

```text
sum_(x in U_0)omega_x(t)Qbar(t;x)x^j=0,
0<=j<=d.                                            (1)
```

Every summand is divisible by `Lambda_2`, so division proves `(STB3)`.

The orthogonal complement on the `n_0=3p-1` evaluation points has dimension

```text
n_0-(d+1)=(3p-1)-2p=p-1.                            (2)
```

It is the dual GRS space

```text
(R(x)/L_U0'(x))_(x in U_0),       deg R<=p-2.       (3)
```

Indeed, for `0<=j<=d`, the numerator degree is at most

```text
(p-2)+d=3p-3=n_0-2,                                 (4)
```

so the Lagrange leading-coefficient identity gives orthogonality; dimensions
then give equality. Applying `(3)` coefficientwise in `t` proves `(STB4)`.
The nonempty missing classes give exact parameter degree and `(SBR4)` gives
their count `(STB5)`.

Cycle 131 proves `(STB7)`. Fix a clean slope. Write its actual support as

```text
S_delta={s_0} disjoint_union I_delta
                   disjoint_union P_delta,
|I_delta|=p-2,       |P_delta|=p+1,                 (5)
```

where `I_delta subset U_0` and `P_delta` lies outside `U`. There is no
padded factor. Specializing the homogeneous locator identity at `delta`
therefore leaves only its nonzero projective normalization scalar
`chi_delta`, so

```text
Qbar(delta;X)=chi_delta A_delta(X)B_delta(X).        (6)
```

The minimum-word circuit argument used in Cycle 128 applies verbatim to
`X_delta=U_0\I_delta`: for one `kappa_delta!=0`,

```text
omega_x(delta)B_delta(x)L_U0'(x)=kappa_delta
                                      (x in X_delta). (7)
```

Equations `(STB2)`, `(STB4)`, `(6)`, and `(7)` give

```text
G(delta,x)
 =[chi_delta kappa_delta/Lambda_2(delta)]A_delta(x)
                                      (x in X_delta). (8)
```

Equation `(8)` gives agreement on `X_delta`. Both sides vanish on
`I_delta`, so they agree at every point of `U_0=X_delta disjoint_union
I_delta`. Their degrees are at most `p-2<|U_0|`; hence they are equal
polynomials.
This proves `(STB9)`, and one clean fiber makes the domain degree exact.
The official substitutions are direct. QED.
