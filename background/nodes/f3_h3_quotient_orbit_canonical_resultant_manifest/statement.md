# H3 quotient-orbit canonical resultant manifest

- **status:** PROVED
- **closure:** proof
- **consumers:** `f3_h3_dsp8_correlation_bound`,
  `f3_h3_official_order_template_survivor`
- **dependency:** `f3_h3_quotient_galois_orbit_scalar_decomposition`

Let `n=2^s`. For `1<=j<=s-1`, put

```text
L=2^(j+1),       d=phi(L)=2^j,       m=s-j-1,
W_odd(L)={w:1<=w<L, w odd, w!=1},
W_even(L)={w:1<=w<L, w even}.                         (QRM1)
```

Every odd-dilation orbit on the ordered nonidentity quotient lifts has
exactly one representative in the following three families:

```text
2^m(1,w),       w in W_odd(L),
2^m(1,w),       w in W_even(L),
2^m(w,1),       w in W_even(L).                      (QRM2)
```

Thus `(j,+,w)` for `w in W_odd(L) union W_even(L)` and `(j,-,w)` for
`w in W_even(L)` are canonical block identifiers. They give
`3(2^j-1)` blocks at degree `2^j` without constructing any orbit.

Put

```text
Phi_L(Z)=Z^d+1,
S_w(Z)=1+Z+...+Z^(w-1).
```

The monic irreducible polynomial of the `+` block is exactly

```text
q_(j,+,w)(T)=Res_Z(Phi_L(Z),T-S_w(Z)) in Z[T].       (QRM3)
```

For `w in W_even(L)`, let `a=v_2(w)`. Then

```text
N_(j,w)=Res_Z(Phi_L(Z),S_w(Z))=2^(2^a-1),            (QRM4)

q_(j,-,w)(T)
 =N_(j,w)^(-1) Res_Z(Phi_L(Z),S_w(Z)T-1)
 =N_(j,w)^(-1) T^d q_(j,+,w)(T^(-1)) in Z[1/2][T].  (QRM5)
```

Consequently the quotient polynomial has the formula-generated
factorization

```text
Qhat_n(T)
 =product_j product_(w in W_odd(L) union W_even(L)) q_(j,+,w)(T)
            product_(w in W_even(L)) q_(j,-,w)(T).  (QRM6)
```

This is an exact contributor manifest for the orbitwise cutoff-35 scalar
annihilators. It removes orbit enumeration and makes every block reproducible
from `(j,sign,w)`. It does not identify the scalar support of distinct or
reciprocal blocks, compute any resultant or annihilator at official scale,
reduce total degree, prove a runtime bound, or close C36'.
