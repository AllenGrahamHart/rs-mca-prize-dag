# `A=1` exceptional Forney norm-discriminant square gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_forney_residue_self_dual_algebra`

Retain the monic squarefree exceptional locator `A` of degree `2e`, the
Forney numerator `Phi`, minimal-support locator `B_T`, and exceptional
derivative coefficient `q_1`. Every resultant below is nonzero. Then a
high-distance endpoint packet necessarily satisfies

```text
Xi_A=
 Res_X(A,q_1) Res_X(A,Phi)
 ---------------------------------  in (F_field^x)^2. (HNS1)
 Res_X(A,B_T) Disc(A)
```

Equivalently, if `C=q_1Phi/B_T mod A`, then

```text
Norm_(R_A/F_field)(C)/Disc(A) is a square.           (HNS2)
```

This square-class gate applies to both the MDS and dependent-complement
branches. A nonsquare value is an exact endpoint rejection certificate. No
claim is made here that `(HNS1)` is always nonsquare on either official
profile.
