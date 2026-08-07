# Primitive shift-pair zero-fold norm divisibility

- **status:** PROVED
- **closure:** proof

Use the dyadic folds of `x4_primitive_shiftpair_dyadic_norm_router`, and put

```text
C(X)=sum_(a=0)^(N-1)c_a X^a in Z[X].
```

Choose any prefix-supplied level set `J`.  Partition it as

```text
S={j in J:beta_j!=0},       Z={a in J:beta_a=0},
```

and assume `S` is nonempty.  With `n_j=N/2^j`, define

```text
T_2(S,Z)=sum_(j in S)sum_(a in Z) min(n_j,n_a)/2.
```

Then

```text
2^(|S|+T_2(S,Z)) p^R_S
  divides product_(j in S)|Norm(beta_j)|.            (ZF-1)
```

Combining `(ZF-1)` with the shared Haar ceiling gives the exact necessary
pattern inequality

```text
2^(|S|+T_2(S,Z)) p^R_S A_S^A_S <= (eN)^A_S.        (ZF-2)
```

Here `R_S` and `A_S` are those of the Haar norm-product gate.  In particular,
every coefficient-primitive shift pair uses a pattern with `0 in S`, and any
pattern violating `(ZF-2)` is empty.

This theorem does not identify zero folds with quotient-owned supports,
force a prescribed fold pattern, count a surviving pattern, or close X4.
