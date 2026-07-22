# `A=1` exceptional-only Hankel coefficient bi-isotropic plane

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_middle_adjugate_factorization`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_factor_pin`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_kernel_plane_transversality`

Use the local exceptional coordinate `z=E/H` and expand the primitive
minimal kernel vector as

```text
M(z)=M_0+zM_1,
q(z)=q_0+zq_1+...+z^e q_e,       q_0=u.              (HBI1)
```

Put

```text
W_q=span{q_0,...,q_e}.                               (HBI2)
```

Then

```text
dim W_q=e+1,                                         (HBI3)
q_i^T M_s q_j=0       for s in {0,1}, 0<=i,j<=e.   (HBI4)
```

Thus `W_q` is a maximal common totally isotropic coefficient plane for the
two symmetric Hankel forms. Its endpoint intersections are exact:

```text
W_q intersect ker M_0=span{q_0},
W_q intersect ker M_1=span{q_e}.                     (HBI5)
```

In moment coordinates, if
`(M_s)_(a,b)=h^(s)_(a+b)` and
`Q_i(X)=sum_a(q_i)_aX^a`, `(HBI4)` is the compressed family

```text
sum_(a,b)(q_i)_a(q_j)_b h^(s)_(a+b)=0.              (HBI6)
```

Whenever a finite source representation
`h^(s)_k=sum_x omega_x^(s)x^k` is used, this is equivalently

```text
sum_x omega_x^(s) Q_i(x)Q_j(x)=0.                   (HBI7)
```

The theorem supplies the full quadratic Hankel coefficient ledger for the
endpoint classifier. It does not by itself classify the coefficient plane
or exclude either quotient endpoint profile.
