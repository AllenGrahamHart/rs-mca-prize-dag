# E1 profile-(2,10) cofactor-1028 energy-two exclusion

- **status:** PROVED
- **closure:** bounded-deviation logarithm minorant with exact rational margins
- **scope:** binding prize rate-`1/8` row, profile `(2,10,S=18)`, cofactor `1028`

No profile-`(2,10,S=18)` collision on a prize-envelope row with cofactor
`1028` has positive-half autocorrelation energy `E=2`.

At energy two every conjugate deviation lies in `[-4,4]`. On this interval,

```text
log(1+x/18) >= x/18-x^2/549.
```

The exact conjugate moments consequently give

```text
log Norm(F(zeta_256)) >= 64 log(18)-256/549
                       > log(1028*p_max).
```

Together with the separate energy-five/six exclusion, the live
cofactor-`1028` energy set is now `{3,4}`. This node makes no assertion about
either remaining energy.
