# `A=1` exceptional Hankel self-dual evaluation code

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_coefficient_rank_one_flag`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_forney_numerator_normal_form`

Let `R_A` be the `2e` squarefree exceptional roots of `q_0=A`, and use the
nonzero exceptional source weights

```text
h_0=sum_(a in R_A) beta_a c(a),       beta_a!=0.     (HSD1)
```

Evaluate the coefficient plane on those roots:

```text
C_q=ev_(R_A)(W_q)=ev_(R_A)(H_q) subset F_field^(2e). (HSD2)
```

Then

```text
dim C_q=e,
C_q=C_q^(perp beta),                                  (HSD3)
```

where

```text
<x,y>_beta=sum_(a in R_A) beta_a x_a y_a.            (HSD4)
```

In particular, the column matroid of any generator matrix `G` of `C_q` is
complement-self-dual. More precisely, for every `e`-subset `I` of `R_A` and
its complement `J`, write `Delta_I,Delta_J` for the corresponding maximal
minors in the induced orders. Then

```text
Delta_J^2 product_(a in J)beta_a
 =(-1)^e Delta_I^2 product_(a in I)beta_a.           (HSD5)
```

Thus `Delta_I` is nonzero if and only if `Delta_J` is nonzero. The weighted
square law is an exact exceptional-root certificate for the high-distance
classifier. It does not yet classify all such self-dual evaluation codes or
exclude an endpoint profile.
