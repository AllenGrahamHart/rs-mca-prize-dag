# Proof - L1 Mersenne HNF m=8 order-one cubic three-double affine-invariant formula

Put `w_i=v_i^2+2p/3`. Newton's identities from (AIF1) give

```text
sum v_i^2=-2p,       sum v_i^3=3eta,
sum v_i^4=2p^2,      sum w_i=0.                    (1)
```

After subtracting its mean, (AIF2) becomes `A w_i+L v_i`. Hence

```text
sum w_i^2=2p^2/3,       sum w_iv_i=3eta.            (2)
```

Since the centered values sum to zero, their second elementary invariant is
minus half their sum of squares. Equations (1)--(2) give the formula for `P`
in (AIF3).

For the centered product, expand `product_i(Aw_i+Lv_i)`. The four required
symmetric sums are

```text
product v_i=eta,
sum_i w_i product_(j!=i)v_j=2p^2/3,
sum_k v_k product_(i!=k)w_i=-p eta,
product_i w_i=eta^2+2p^3/27.                       (3)
```

Substitution of (3) proves the formula for `Q`.

Now center the HNF parameters `u_i` from (TDF2). In the scaled variables,
their elementary functions are

```text
s_1=6,       s_2=b,
s_3=(2-x)b+12x-16-q(d+2)/6.                        (4)
```

Therefore their centered invariants are

```text
p=s_2-s_1^2/3=b-12,
eta=s_3-s_1s_2/3+2s_1^3/27
   =-xp-q(d+2)/6.                                  (5)
```

Modulo the parameter cubic, the value map from (TAC5) is a quadratic map.
Its quadratic and centered-linear coefficients are

```text
A=s_1-2U=-2x,
L=U^2+V-s_2+2As_1/3=x^2+q/6-2p/3=ell.             (6)
```

Equations (AIF3), (5), and (6) prove (AIF5).

Finally substitute `T=-27Q^2/P^3` into the four factors of `Theta_8` in
(TAC5) and clear the indicated powers of `P`. This gives (AIF6), including
the `P=0` locus. On the generic branch `alpha!=0` by (TLR9) and the inherited
`q-d!=0` saturation, so (TLR5) gives (AIF7). Substitution into `D_b` and
`M_6` gives the two printed compatibility equations alongside the conic and
one factor of (AIF6). QED.
