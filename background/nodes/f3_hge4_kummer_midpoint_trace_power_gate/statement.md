# HGE4 Kummer midpoint trace-power gate

- **status:** PROVED
- **closure:** proof
- **consumers:** `f3_hge4_kummer_trace_power_gcd_compiler`,
  `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_near_third_belyi_necklace_bound`,
  `f3_hge4_near_third_kummer_midpoint_pencil`

Retain a primitive near-third pencil over `F_p` from the two dependencies:

```text
m=3h+e,       0<e<h,       c=h+e,
U=S-ay^h,     V=S+ay^h,     D=UV,
DW=1-y^m,     W=ZS+lambda y^c,
kappa=1-a^2lambda,
U,V | 1-y^m,                    S | 1-kappa y^m.
```

Put

```text
u=[y^h]U,       v=[y^h]V,       x=v/u.
```

Then

```text
u,v in mu_m,       x in mu_m\{1,-1},
kappa=-(1+x)^2/(8x)
     =-(x+x^(-1)+2)/8.                            (KTP1)
```

The proved primitive Kummer collapse makes `kappa` an `m`-th power in
`F_p^*`. Hence every survivor satisfies the exact scalar gate

```text
(-(x+x^(-1)+2)/8)^((p-1)/m)=1.                   (KTP2)
```

Equivalently, with the Dickson--Chebyshev recursion

```text
C_0(X)=2,       C_1(X)=X,
C_(j+1)(X)=X C_j(X)-C_(j-1)(X),
```

the trace `tau=x+x^(-1)` lies in the finite set

```text
C_m(tau)=2,       tau!=2,-2,
(-(tau+2)/8)^((p-1)/m)=1.                         (KTP3)
```

Before the power test there are exactly `(m-2)/2` such trace values. Swapping
the ordered outside factors sends `x` to `x^(-1)` and preserves `tau` and
`kappa`.

Moreover every surviving `x` is a square in `F_p^*`. If `(p-1)/m` is odd,
this is equivalent to

```text
x in mu_(m/2),
```

so only `m/4-1` trace values remain before the full `m`-th-power test. This
parity case can occur only at the top exact-ratio level `m=n`; at every proper
dyadic divisor `m<n`, the quotient `(p-1)/m` is even.                 (KTP4)

This is a necessary candidate gate. It does not bound the number of pencils
above one trace, count any orbit, prove a width empty, or establish the HGE4
aggregate.
