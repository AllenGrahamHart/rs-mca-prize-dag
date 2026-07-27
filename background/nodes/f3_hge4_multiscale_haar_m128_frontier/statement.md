# HGE4 balanced-factor Haar augmentation and the `m=128` frontier

- **status:** PROVED
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_multiscale_haar_m64_level_close`,
  `f3_hge4_cyclotomic_norm_quarter_width_exclusion`,
  `f3_hge4_nonfull_complement_third_gate`

Use the notation `(MHN1)--(MHN7)` of
`f3_hge4_multiscale_haar_m64_level_close`. In particular, `F` is the
balanced signed support polynomial, `S` is the set of nonzero Haar scales,
and the norm product ranges over

```text
O in {m} union {N_a:a in S}.
```

Balance gives `F(1)=0`, hence

```text
F(X)=(X-1)F_1(X) in Z[X].                              (MX1)
```

Every norm in the product is nonzero. Since
`|Norm(1-zeta_O)|=Phi_O(1)=2` at every dyadic order `O>=2`, the product in
`(MHN6)` has the sharpened divisibility

```text
2^(T_2(S)+1+|S|) p^R_S
  divides |Norm_m(F(zeta_m))|
          product_(a in S)|Norm_(N_a)(F(zeta_(N_a)))|. (MX2)
```

The upper bound is unchanged. Consequently the exact integer gate

```text
2^(T_2(S)+1+|S|) n^(2R_S)>=U_S                       (MX3)
```

excludes that Haar pattern. The new power of two is independent of the
structural-zero factors counted by `T_2(S)`, because `X-1` is coprime over
`Z[X]` to every dyadic `Phi_(N_a)`.

At exact ratio level `m=128` and every official ambient row `n=2^s`,
`s>=13`, exact cross-multiplied evaluation of `(MX3)` gives:

```text
12<=h<=31:          every Haar pattern is empty;
h=11:               every pattern except S={0,1,2} is empty;
h=10:               every pattern except S={0,1} and S={0,1,2} is empty;
h=9:                the patterns S={1}, {2}, {1,2} are empty.             (MX4)
```

The quarter-width theorem deletes `32<=h<=42`, and the complement-third
theorem deletes `43<=h<=64`. Therefore

```text
E_h^prim(128,p)=0                 for every 12<=h<=64. (MX5)
```

The exact `m=128` residual is contained in `4<=h<=11`, with the pattern
pruning in `(MX4)`. This is not a bound for those residual patterns, any
level `m>=256`, or the full HGE4 aggregate.
