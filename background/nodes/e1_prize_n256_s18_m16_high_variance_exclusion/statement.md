# E1 prize N=256 square-mass-18 m=16 high-variance exclusion

- **status:** PROVED
- **closure:** analytic proof plus exact rational verification
- **scope:** prize-envelope `N=256`, profile `(a,b,c)=(4,2,0)`, cofactor `m=16`
- **dependencies:** `e1_prize_n256_s18_variance_cofactor_windows`

Use the parent notation

```text
R=|Norm(F(zeta))|,       R=16p,
V=(1/128) sum_(u odd) (|F(zeta^u)|^2-18)^2.
```

No prize-row collision with cofactor `m=16` exists at any of the variances

```text
V in {114,122,130,138,146,154,162,170,178}.
```

Consequently every residual `m=16` collision candidate satisfies

```text
10<=V<=106,       V=2 mod 8.
```

The proof is analytic. It uses a profile-specific autocorrelation inequality
`4L<=E+35`, six exact quadratic logarithmic majorants, and cubic Hermite
majorants with exact layer bounds at `V=114,122,130`. The accompanying
normalized census is route-planning evidence only and is not a dependency of
the theorem.
