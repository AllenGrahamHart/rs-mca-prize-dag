# HGE4 primitive shift-pair orbit aggregate router

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `x82_square_shift_certifier_keys`, `f3_shiftpair_weld`, and
  `f3_hge4_primitive_shift_pair_aggregate_adapter`

Fix an official row and a width `4<=h<=H_max`. The domain `H=mu_n` acts on
ordered primitive top shift pairs by

```text
gamma.(P,Q)=(gamma P,gamma Q).
```

This action is free. If `O_h^prim` is the number of its orbits, then

```text
SP_h^prim=n O_h^prim.                               (OAR1)
```

If `A_h^left` counts ordered primitive pairs with `1 in P`, without further
rotation canonicalization, then every orbit has exactly `h` such
representatives and

```text
A_h^left=h O_h^prim.                                (OAR1a)
```

Consequently the stronger orbit aggregate

```text
sum_(h=4)^H_max O_h^prim<=14n^2                    (OAR2)
```

implies `f3_hge4_norm_gate_count`.

For the entropy benchmark

```text
M_h=binom(n,h),
Fbar_h=M_h/p^(h-1),
B_h=(M_h-1)Fbar_h,
```

the per-width condition `(PSA3)` in the aggregate adapter is equivalently

```text
O_h^prim<=7000 max(1,B_h).                         (OAR3)
```

Every official `h>=4` row also satisfies

```text
Fbar_h<1,
7000n max(1,B_h)<M_h.                              (OAR4)
```

Thus the naive route that bounds every support's primitive neighbor degree
by one uniform integer and then sums over all `M_h` supports can meet `(PSA3)`
only when that integer is zero. A nonzero proof must instead use an averaged
falling-factorial estimate, an orbit aggregate such as `(OAR2)`, or a proved
sparse-active-support decomposition. This is a route separation, not a claim
that primitive shift pairs are empty.
