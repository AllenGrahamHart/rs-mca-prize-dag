# L1 Mersenne HNF m=8 cubic three-two-one role-factor compiler

- **status:** PROVED
- **dependencies:** `l1_mersenne_hnf_m8_cubic_three_two_one_role_polynomial_compiler`, `l1_mersenne_hnf_m8_order_one_cubic_three_double_affine_color_compiler`
- **consumer:** `l1_mixed_petal_amplification`
- **scope:** the ordered color-role ratio in every cubic `3+2+1` packet

Retain

```text
A=lambda^2-lambda+1,
B=(lambda+1)(2lambda-1)(lambda-2)                   (RFC1)
```

from (TAC1). Define

```text
Omega_1=B^2+50A^3,

Omega_2=B^4-224B^2A^3-578A^6,

Omega_3=B^4-4B^2A^3+54A^6,

Omega_4=125B^4-2404B^2A^3+13448A^6.                (RFC2)
```

Their degrees are `6,12,12,12`, and

```text
Omega_321(lambda)=product_(i=1)^4 Omega_i(lambda)   (RFC3)
```

is a nonzero rational scalar multiple of the degree-42 role polynomial
`Lambda_321(lambda)` from (RPC3). Consequently the common-quadratic
`3+2+1` core may be split into exactly four rational role packets by

```text
Omega_i(lambda)=0,       lambda*(lambda-1)!=0.       (RFC4)
```

The four packets represent respectively one rational affine shape and three
quadratic-conjugate shape pairs. They retain all ordered multiplicity roles,
including repeated role-ratio values with their natural multiplicities. No
packet is declared empty.
