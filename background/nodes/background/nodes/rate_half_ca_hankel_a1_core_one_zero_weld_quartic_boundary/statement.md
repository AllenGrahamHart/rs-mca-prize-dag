# `A=1` core-one zero-weld quartic boundary

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_two_sided_complement_weld`

Retain the official core-one dominant component and the weld

```text
W B-B_XE_Z=Q_*K.                                      (ZWB1)
```

If `K=0`, then necessarily

```text
b=0,       e_*=e=2^38-1,       r=2e+1,
D_*=1,                                                  (ZWB2)
```

so `Q_*=Qbar` is the full irreducible residual generator. Moreover the unique
exceptional slope factor divides `W`, not `B`. There are squarefree split
polynomials

```text
F(U,V)=P_cl(U,V),       deg F=4e,
G_0(X)=product_(x in D_0')(X-x),       deg G_0=8e+4,   (ZWB3)
```

where `D_0'` consists of all but exactly three points of `D\S`, and a biform
`V_0` such that

```text
F(U,V)-G_0(X)=Q_*(U,V;X)V_0(U,V;X).                   (ZWB4)
```

The bidegrees are exactly

```text
deg Q_*=(2e+1,e),       deg V_0=(6e+3,3e),
deg(F-G_0)=(8e+4,4e)=4(2e+1,e).                       (ZWB5)
```

Thus every `K=0` model is reduced to one **quartic separated-factor
boundary**: the rank-`e+1` Hankel-apolar component `Q_*` is a one-quarter
bidegree factor of the difference of two squarefree split polynomials, one
supported on `4e` clean slopes and the other on `8e+4` residual domain
points.

For every profile with `b>0`, every profile with `D_*=0`, and the allocation
where `E_Z` divides `B`, one has

```text
K!=0.                                                  (ZWB6)
```

This theorem excludes the zero-weld branch outside `(ZWB2)--(ZWB5)`. It does
not exclude the quartic boundary or any `K!=0` model.
