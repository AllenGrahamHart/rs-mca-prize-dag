# DLI primitive joint-ratio telescoping identity

- **status:** PROVED

Let `t=2^m` and use the exact `U`-weighted dyadic tower. Write `Z_j` for
the weighted level-`j` null census, `B_j` for the unconditional census of
junction block `j`, and `C_1` for the first saturated/coset census. Then

```text
C_1 = Z_0(q,n/2,t/2),
Z_0^prim = Z_0-C_1,
J_prim = 2^(nm)(Z_0-C_1)/(Z_m product_(j=0)^(m-1) B_j).       (PRIM-TEL)
```

Here `J_prim` is the all-weight primitive joint loss divided by the product
of its unchanged unconditional marginals. If `Z_0>C_1`, equivalently

```text
log2 J_prim = R3_full + log2(1-C_1/Z_0).
```

If `Z_0=C_1`, then `J_prim=0`. The central primitive mass in C2'' is a
submass of the all-weight primitive numerator. Consequently the exact
integer inequality

```text
2^(nm)(Z_0-C_1) <= 2^21 Z_m product_(j=0)^(m-1) B_j          (C2-INT)
```

is sufficient for the repaired C2'' target.
