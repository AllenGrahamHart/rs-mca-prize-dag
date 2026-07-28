# E1 prize N=256 square-mass-18 m=2 high-variance exclusion

- **status:** PROVED
- **closure:** analytic proof plus dual exhaustive third-moment certificate
- **scope:** prize-envelope `N=256`, profile `(a,b,c)=(4,2,0)`, cofactor `m=2`
- **dependencies:** `e1_prize_n256_s18_variance_cofactor_windows`

Use the parent notation

```text
R=|Norm(F(zeta))|,       R=2p,
V=(1/128) sum_(u odd) (|F(zeta^u)|^2-18)^2.
```

No prize-row collision with cofactor `m=2` exists at any variance

```text
V in {106,114,122,...,250}.
```

Consequently every residual `m=2` collision candidate satisfies

```text
10<=V<=98,       V=2 mod 8.
```

Two independent complete normalized enumerators give the exact maximum third
central moment through `V=194`; cubic Hermite majorants exclude the twelve
chambers from `V=106` onward. The profile-specific inequality `4L<=E+35`,
exact universal layer caps, and cubic Hermite majorants exclude the seven
remaining chambers `V=202,...,250` without a support census.
