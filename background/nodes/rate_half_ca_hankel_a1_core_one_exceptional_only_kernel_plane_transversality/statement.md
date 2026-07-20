# `A=1` core-one exceptional-only kernel-plane transversality

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_exceptional_root_charge`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_hankel_factor_pin`

Choose a projective linear form `H` nonzero at `gamma_0`, set
`z=E/H`, and dehomogenize at `H=1`. Write

```text
M(z)=M_0+zM_1,
q(z)=u+zq_1+O(z^2),                                 (KPT1)

Q(gamma_0;X)=sum_(j=0)^(r-1)a_jX^j.
```

Define the two padded coefficient shifts

```text
u=(a_0,a_1,...,a_(r-1),0)^T=q(0),
v=(0,a_0,a_1,...,a_(r-1))^T.                        (KPT2)
```

Then

```text
ker M_0=span{u,v}.                                  (KPT3)
```

The first coefficient of the moving kernel equation and the symmetric
pairings on this plane satisfy

```text
M_0q_1+M_1u=0,                                      (KPT4)

u^TM_1u=0,       v^TM_1u=0,       v^TM_1v!=0.       (KPT5)
```

Thus the generic kernel curve continues through the line `span{u}`, while
the other exceptional kernel line `span{v}` is lifted transversely at first
order. The conditions are invariant under rescaling `u,v`, and the
nonvanishing is unaffected by replacing `H` by another local unit.

This is the compact exceptional Hankel gate. It does not classify the lower
Hankel coefficients, prove the reciprocal divisibilities, or exclude the
corrected square.
