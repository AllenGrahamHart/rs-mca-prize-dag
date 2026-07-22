# `A=1` exceptional quotient clean-fiber unit-resultant log-trace gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_unit_resultant_collapse`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_quotient_clean_fiber_jet_quotient_ring_compiler`

Let

```text
a(t)=[X^r]Q=E q_bar,
q_0(t)=[X^0]Q=[Y^r]F,
N_sq=n_X+r-1.                                        (QLT1)
```

At a clean slope `gamma`, use the quotient-ring compiler notation
`f=F(gamma,Y)`, `v=dot y`, `w=W_vee(gamma,Y)`, and
`j=W_vee,t(gamma,Y)`. Then `w` is a unit modulo `f`, and the split-etale
trace satisfies the exact scalar identity

```text
Tr_(K_gamma/F_field)((j+w_Yv)w^(-1))
 =(N_sq+1)E'/E+N_sq q_bar'/q_bar
  -(r-1)q_0'/q_0,                                   (QLT2)
```

with the right side evaluated at `gamma`. Equivalently, the left side is
the sum of `dot W_vee/W_vee` over all selected roots. The unknown actual
degree `m=deg_X W` cancels from `(QLT2)`. Therefore a mismatch is an exact
scalar rejection certificate available before the full Hermite or Hankel
comparisons. The theorem does not prove that either endpoint profile has a
mismatch.
