# Budget-three antipodal generic Euler cubic-norm gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_euler_divisor_gate`

Retain `(GED1)--(GED6)` over the canonical generic floor. Use the monic-first
resultant convention

```text
Res(V,f)=product_(V(alpha)=0) f(alpha).                (GCN1)
```

The Euler divisibility implies the exact scalar identity

```text
Res(V,T) Res(V,U)^3=(-d)^v.                           (GCN2)
```

All three resultants in `(GCN2)` are nonzero. On the official row,

```text
d=2^39=(2^13)^3,       v=2^36-2=2 mod 3,
v is even.                                                (GCN3)
```

Therefore

```text
Res(V,T) is a nonzero cube in the base field.          (GCN4)
```

Write the nonzero linear residual as

```text
T=t_1(Y-tau).
```

Since `V` is monic and `v` is even,

```text
Res(V,T)=t_1^v V(tau).
```

Modulo cubes `t_1^v=t_1^2`, so every generic candidate satisfies the one-scalar
gate

```text
t_1^2 V(tau) in (F^*)^3.                              (GCN5)
```

For a finite base field of order `q=1 mod 3`, this is equivalently

```text
(t_1^2 V(tau))^((q-1)/3)=1.                          (GCN6)
```

When `q=2 mod 3`, cubing is bijective and `(GCN5)` is vacuous; the full
Euler remainder `(GED5)` remains load-bearing. This theorem does not prove
that `(GCN5)` fails uniformly, and passing the scalar gate is not sufficient
for Euler divisibility or the generic canonical-span certifier.
