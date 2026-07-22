# `A=1` endpoint derivative-resultant reciprocity

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_endpoint_resultant_profile`

Retain the sharp endpoint notation

```text
e=2^38-1,       k_0=(e-1)/2,
Q(z;X)=A(X)+zq_1(X)+...+z^e q_e(X).
```

Both `q_1` and `q_e` are units modulo the monic exceptional locator `A`.
In the flat endpoint profile,

```text
Res(A,q_1)=Res(A,q_e) P_ord(0)^k_0.                 (QDR1)
```

In the swapped profile,

```text
z_max Res(A,q_1)
 =z_min Res(A,q_e) P_ord(0)^k_0.                    (QDR2)
```

Since `k_0=2^37-1` is odd, the corresponding field square classes are

```text
[Res(A,q_1)/Res(A,q_e)] = [P_ord(0)]                (flat),
[Res(A,q_1)/Res(A,q_e)] = [z_min z_max P_ord(0)]    (swapped). (QDR3)
```

Equivalently, `(QDR1)--(QDR2)` give the norm of the top normalized
split-frame coefficient `p_(e-1)=q_e/q_1` in `F_field[X]/(A)`. This is a
necessary endpoint identity, not an exclusion of either profile.
