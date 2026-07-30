# E1 profile-(3,6) exact weighted payment

- **status:** PROVED
- **closure:** exact integer ledger
- **scope:** binding prize rate-`1/8` row

After the complete exclusion of profile `(4,2,S=18)`, the next profile
`(3,6,S=18)` contributes at most

```text
709758113888498314287146042668908462080
```

unordered collision pairs. This is the exact consequence of

```text
T_36(p,r)<=4,
orbit size=256,
M_33(3,6)=1386246316188473270092082114587711840.
```

The residual edge budget is

```text
64417827807586372161179904588832830040487.
```

Among every profile not already excluded or paid, the largest dictionary
weight is

```text
M_33(2,10)=1227527050040565145269313275179180544.
```

Consequently, at most `104955` remaining oriented vectors is a uniform
sufficient condition for the residual budget; `104956` is not certified by
that uniform inequality. The exact profile-weighted ledger remains the
preferred target.

