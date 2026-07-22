# L1 Pade split-section/support-moment inversion

- **status:** PROVED
- **role:** identify exact L1 shells with upstream support and split-pencil censuses
- **consumer:** `l1_mixed_petal_amplification`

## Three counts

Let `H` be any `n`-point evaluation set, let `U:H->F` have interpolant
`Uhat` of degree below `n`, and fix `m>=k`.  Define

```text
C_m(U) = #{A subset H: |A|=m and U|A extends to degree <k},
Z_a(U) = #{P in F[Z]_<k: agr_H(U,P)=a},
S_m(U) = #{split monic degree-m locators L_A:
           deg(Uhat mod L_A)<k}.
```

Then

```text
S_m(U)=C_m(U)=sum_(a=m)^n binom(a,m) Z_a(U).          (PS1)
```

The split-locator count `S_m` is exactly the full-locator Pade-section split
count before the complement gcd guard.  The exact-shell count at level `m`
is `Z_m`; imposing the guard deletes the contributions from codewords with
more than `m` agreements.

## Exact inversion

The triangular transform `(PS1)` is invertible:

```text
Z_a(U)=sum_(m=a)^n (-1)^(m-a) binom(m,a) C_m(U).      (PS2)
```

In particular

```text
Z_m(U)<=C_m(U).                                      (PS3)
```

Thus a row-sharp upper bound for upstream's support/lattice/split-pencil
census transfers directly to the corresponding exact L1 shell.  Conversely,
an exact-shell profile reconstructs every support moment by `(PS1)`.

## Scope

The identity is valid for arbitrary evaluation sets and uses no smoothness.
It does not prove a row-sharp bound, preserve primitive/quotient owner labels
under inversion, or identify the final guard-pruned interior numerator and
finite reserve conventions.  The named strict-interior base-field support
floor routes to higher-shell Q by a separate proved node; other
field-sensitive residuals remain interface obligations.
