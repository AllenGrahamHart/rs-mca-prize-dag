# Primitive shift-pair Haar norm-product gate

- **status:** PROVED
- **closure:** proof

Use the notation of `x4_primitive_shiftpair_dyadic_norm_router`.  Extend the
integer folds to every `0<=j<=s-1`, including levels not supplied by the
locator prefix, and put `E_j=sum_r b_(j,r)^2`.  Then the folds have the exact
shared Haar-energy identity

```text
sum_(j=0)^(s-1) E_j/2^(j+1)=2e.                    (HP-1)
```

Let `S` be any nonempty set of prefix-supplied levels at which `beta_j!=0`,
and define

```text
a_j=n_j/4=N/2^(j+2),
A_S=sum_(j in S) a_j,
R_S=sum_(j in S) f_j o_j,
M_S=sum_(j in S) M_j.
```

Then

```text
p^R_S divides product_(j in S)|Norm(beta_j)|,

p^M_S <= p^R_S
        <= product_(j in S)|Norm(beta_j)|
        <= product_(j in S) E_j^a_j
        <= (eN/A_S)^A_S.                            (HP-2)
```

The last rational power is an exact integer comparison after multiplying by
`A_S^A_S`:

```text
p^R_S A_S^A_S <= (eN)^A_S.                         (HP-3)
```

For a coefficient-primitive pair, `0 in S` when `S` is the complete active
set, so the gate is never empty.  In an exact difference-degree cell use the
full effective prefix depth `T=e-d-1` when determining the supplied levels,
`M_j`, and `o_j`.  Consequently any active-scale pattern violating `(HP-3)`
is empty.

This theorem does not show that all higher folds are active, exploit extra
divisibility created by zero folds, count the surviving patterns, or close
the X4 allowance.
