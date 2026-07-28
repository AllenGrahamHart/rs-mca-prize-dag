# E1 prize N=256 square-mass-18 m=4 high-variance exclusion

- **status:** PROVED
- **closure:** analytic proof plus dual exhaustive third-moment certificate
- **scope:** prize-envelope `N=256`, profile `(a,b,c)=(4,2,0)`, cofactor `m=4`
- **dependencies:** `e1_prize_n256_s18_variance_cofactor_windows`

Use the parent notation

```text
R=|Norm(F(zeta))|,       R=4p,
V=(1/128) sum_(u odd) (|F(zeta^u)|^2-18)^2.
```

No prize-row collision with cofactor `m=4` exists at any variance

```text
V in {82,90,98,...,226}.
```

Consequently every residual `m=4` collision candidate satisfies

```text
10<=V<=74,       V=2 mod 8.
```

The proof uses the profile-specific autocorrelation inequality `4L<=E+35`.
Two independent complete normalized enumerators give the exact maximum third
central moment in the eleven chambers `V=82,...,162`; cubic Hermite
majorants then exclude them. Exact universal layer caps exclude
`V=170,178,186,194`, and exact quadratic logarithmic majorants exclude
`V=202,210,218,226`.
