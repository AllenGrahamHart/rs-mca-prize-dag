### 2026-08-10 FPC5 fixed-background GRS payment

The GRS syndrome-shell import now composes with the fixed-background
incidence identity. For `0<=u<=b`, each required `u`-set `R` has

```text
D=d+ell-1,       J_fix=d^2-N(d-ell).
```

The fixed chart is singleton when `D>=N`; when `D<N` and `J_fix>0`, ordinary
Johnson gives at most `Nell/J_fix` primitive supports. Summing all required
sets honestly yields

```text
|F|<=binom(b,u)
```

or

```text
|F|<=binom(b,u)Nell/J_fix,
```

respectively. Thus either branch is polynomial within any fixed distance of
`u=0` or `u=b`.

This is complementary to the prior joint-background Johnson payment because

```text
J_bg=b J_fix-Nu(b-u).
```

The new theorem can pay a positive fixed denominator even when the joint
denominator fails, but only after charging the exact background-choice
entropy. It narrows the live FPC5 wall to middle background polarity and/or
nonpositive fixed-shell Johnson, together with source/chronology aggregation.
No critical status changes.
