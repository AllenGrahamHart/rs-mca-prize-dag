# Budget-three fiber-two c=1 parity harmonic field router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c1_parity_mobius_router`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_even_factorization`,
  `rate_half_list_budget_three_maximal_field_degree_collapse`

Retain either residual harmonic class `H_R,H_P` from the `c=1` parity
Mobius router. Put

```text
M=2^36,       L=8M=2^39,       2L=2^40,       4L=2^41.
```

The parameter-uniform signed-factor cyclotomic bound and maximal-row field
collapse leave exactly

```text
q_field=p^2,       p=1 mod 2L.                       (CHF1)
```

Writing

```text
p=1+k*2^40,
```

the exact budget interval is

```text
29058991<=k<33554432.                                (CHF2)
```

There are `4,495,441` integer candidates before primality filtering.
All normalized denominator roots, canonical factors, outer roots, and
`iota` already lie in `F_p`.

The residual harmonic source lift also lies in `F_p`. For `H_P` this is
immediate from

```text
r=(4-3iota)/5.                                      (CHF3)
```

For `H_R`, if the possible top lift were anti-invariant, Frobenius would
send `r` to `-r`. Applying Frobenius to

```text
r^2+3(1+iota)r+iota=0                               (CHF4)
```

and subtracting gives `6(1+iota)r=0`, impossible in the official
characteristic.

Both classes therefore have fixed base-field trace tests. For `H_P`,

```text
u_0=8/5,       u_(j+1)=u_j^2-2,
r^(2^41)=1  iff  u_41=2.                            (CHF5)
```

For `H_R`, choose `zeta^2=iota`, set
`theta=(1+iota)/zeta` and `s=r/zeta`. Then
`theta^2=2`,

```text
s+s^(-1)=-3theta,       (-3theta)^2-2=16.
```

Since `zeta` has order eight,

```text
v_1=16,       v_(j+1)=v_j^2-2,
r^(2^41)=1  iff  v_41=2.                            (CHF6)
```

Thus a complete harmonic characteristic screen needs, for every integer in
`(CHF2)`, forty-one updates from `8/5` and forty updates from `16`.
A modulus divisible by five is already composite and may be rejected
without forming `8/5`.

This theorem makes that bounded screen coverage-equivalent for the harmonic
`c=1` parity subbranch. It does not evaluate the recurrences, exclude
either class, address nonharmonic matching, or authorize an unbounded run.

