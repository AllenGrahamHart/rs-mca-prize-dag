# Budget-three antipodal fourth-root gap reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_reverse_residual_stratification`

Use the centered antipodal quotient-pencil notation of the dependency. Put

```text
E(z)=z^4D(z^-1),
A(z)=E(z)^(-1/4)=sum_(m>=0) a_m z^m,       a_0=1,       (FRG1)
B(z)=z^rU(z^-1).
```

The fourth root in `(FRG1)` is the unique formal series with constant term
one. If the differential residual

```text
T=dDU-Y(D'U+4DU')                                      (FRG2)
```

has degree at most three, then `U` is uniquely determined by `D` and `r`, and

```text
B(z)=sum_(m=0)^r a_m z^m.                              (FRG3)
```

Writing `E(z)=1+eta_1z+eta_2z^2+eta_3z^3+eta_4z^4`, the
coefficients in `(FRG1)` have the exact four-term recurrence

```text
4m a_m=-sum_(j=1)^4 (4m-3j)eta_j a_(m-j),             (FRG4)
```

where `a_s=0` for `s<0`.

If the quartic norm equation also has first nonzero centered outer coefficient
`q` and `h=r-deg V`, then

```text
a_(r+1)=...=a_(qh-1)=0,       a_(qh)!=0.               (FRG5)
```

On the maximal official row `r=2^37-1`, the lowest-degree strata therefore
obey

```text
generic e_2!=0:
  a_(r+1)=a_(r+2)=0,       a_(r+3)!=0;                 (FRG6)

intermediate e_2=0,e_3!=0:
  a_(r+1)=0,               a_(r+2)!=0.                 (FRG7)
```

Thus each boundary is reduced to an explicit coefficient-gap problem for the
fixed degree-four algebraic series `E^(-1/4)`. This theorem neither proves the
required coefficients nonzero nor excludes solutions above the boundaries.
