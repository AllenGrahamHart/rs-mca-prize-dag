# L1 m=4, h=3, nu=2 fixed-point certificate

- **status:** PROVED
- **dependency:** `l1_m4_h3_nu2_base_field_normalization`
- **consumer:** `l1_mixed_petal_amplification`

Assume a surviving positive `(nu,deg H)=(2,1)` record at

```text
p in {524287,2147483647},       n=4(p+1).
```

Use the proved normalization

```text
R_0=S_e-S_e(0),
S_e(Z)=product_i (Z-d_i^(-1))^(e_i),
d_1=e_2-e_3, d_2=e_3-e_1, d_3=e_1-e_2,
e_1+e_2+e_3=p,
c=-(4/3)S_e(0),
g_0(Y)=Y^3-2c^2Y+c^3,
g_0(R_0)D_0=Z^n-A.                                  (FPC1)
```

All quantities except the domain scalar already lie in `F_p`. Let `K` be
the order-`n` subgroup and `C={z:z^n=A}` the normalized domain coset. Then

```text
C=cK,       A=c^n.                                    (FPC2)
```

Moreover, exactly one sign `epsilon in {1,-1}` satisfies

```text
R_0(epsilon c)=c,       D_0(-epsilon c)=0.             (FPC3)
```

Thus the only prime-field point of the fixed split fiber is `epsilon c`,
and the other prime-field point of the domain coset is a complement root.

The statement has a coefficient-free multiplicity form. Put

```text
w=product_i d_i^(e_i) in F_p^*.
```

Then `S_e(0)=-w^(-1)`, `c=4/(3w)`, and the sign in `(FPC3)` obeys

```text
product_i (3w-4 epsilon d_i)^(e_i)=-w in F_p.          (FPC4)
```

There is also a scalar-free factorization. Define

```text
q_i=3w/(4d_i),
F_e(W)=3/4+product_i (W-q_i)^(e_i),
E_e(W)=c^(3-n)D_0(cW).                                (FPC5)
```

Then `F_e` and the monic degree-`p+4` polynomial `E_e` lie in `F_p[W]` and

```text
(F_e(W)^3-2F_e(W)+1)E_e(W)=W^n-1,
F_e(epsilon)=1,       E_e(-epsilon)=0.                 (FPC6)
```

Consequently every genuine record is caught by two explicit scalar tests and
one canonical divisibility test on its unordered multiplicity triple; there
is no remaining input, output, or domain scalar to search. This is a
necessary certificate, not a converse, an exclusion of either official
characteristic, a treatment of `(1,2)` or `nu=0`, or an L1 closure.
