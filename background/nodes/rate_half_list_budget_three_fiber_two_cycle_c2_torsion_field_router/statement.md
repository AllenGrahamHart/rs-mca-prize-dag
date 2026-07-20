# Budget-three fiber-two c=2 torsion-field router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_maximal_field_degree_collapse`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_normalized_pair_torsion_compiler`

Work in the official normalized `c=2` chamber. Put

```text
N=2^40,       2N=2^41 divides q-1,
D_A(Y)=(Y-1)(Y-t)(Y^2-SY+P).
```

Let the scalar torsion recurrence be

```text
t_(j+1)=t_j^2,
T_(j+1)=T_j^2-2P_j,
P_(j+1)=P_j^2,       (t_0,T_0,P_0)=(t,S,P).          (TFR1)
```

If

```text
t_40=1,       T_40=2,       P_40=1,                 (TFR2)
```

then `Y^2-SY+P` splits over `F_q`, and all four roots
`1,t,c,d` of `D_A` are squares in `F_q`. Thus the split and common-square
conditions in the normalized `c=2` interface are consequences of `(TFR2)`;
they are not independent search axes. Distinctness remains the nonvanishing
condition already printed in the normalized-pair compiler.

The official field cases also reduce exactly as follows. Write `q=p^e`.
Then `e in {1,2}`. If `e=1`, or if `e=2` and
`p=1 mod N`, then

```text
t,c,d in F_p.                                        (TFR3)
```

If `e=2` and `p=-1 mod N`, then

```text
x^p=x^(-1)       for x in {t,c,d}.                  (TFR4)
```

Writing

```text
E(z)=(1-z)(1-tz)(1-cz)(1-dz)=sum_(j=0)^4 E_jz^j,
E_4=tcd,
```

the latter case has the coefficientwise reciprocal-Frobenius identity

```text
E(z)^p=E_4^(-1)z^4E(z^(-1)),
E_j^p=E_(4-j)/E_4.                                  (TFR5)
```

Here `E(z)^p` means Frobenius applied to its coefficients, not the polynomial
`E(z)^p` obtained by raising the variable powers. The identity routes every
official normalized packet into a prime-field chamber or a unitary reciprocal
chamber. It does not identify a packet with its Frobenius conjugate, force a
two-antipodal denominator, impose either coefficient gap, or exclude `c=2`.
