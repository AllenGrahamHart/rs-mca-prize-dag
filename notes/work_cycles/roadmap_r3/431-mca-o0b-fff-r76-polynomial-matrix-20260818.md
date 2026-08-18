## MCA O0b `FFF` `R76` polynomial-matrix bank (2026-08-18)

### Exact denominator clearing

The rational `R76` multiplication matrix has now been cleared column by
column. For each column `j`, the exact denominator LCM `L_j` and all sixteen
entries

```text
P_ij = numerator(M_ij) * L_j / denominator(M_ij)
```

are retained over `GF(2130706433)[t]`.

```text
column-LCM degree range: 1021..1257
polynomial-entry range:  1151..1388
matrix size/nonzero:     16 x 16 / 256
```

Modal app `ap-TtH5bFr7Z3uWIjmWgiukkm` verified at `t=2` that

```text
det(P(2)) = 1087830147
product_j L_j(2) = 1089253482
det(M_R76(2)) = 244686406
det(P(2)) = det(M_R76(2)) * product_j L_j(2).
```

Polynomial-matrix SHA-256:
`15749ad35ba394a9dce27a8c759f0203746233a2fb354efcc3655d44ea205de4`;
result SHA-256:
`ea218c257268a7887bf296dcb7d9e8f97ca3591866ca04e6595b3cd8170a0dae`.

### Determinant target

The determinant is a univariate polynomial of degree at most

```text
16 * 1388 = 22208.
```

The next node can therefore start directly from this bank and compute
`det(P)` with fraction-free polynomial arithmetic. If direct determinant
extraction remains slow, exact evaluation/interpolation needs at most 22,209
good field points for a degree-bounded reconstruction, followed by independent
holdout checks.

### Checker repair

The initial outcome-neutral checker hashed dictionaries after parsing compact
sorted JSON, which changed key order relative to the launcher's canonical
hash input. The repaired checker explicitly reconstructs canonical field
order. It changes neither the result nor any mathematical assertion.

### Proof boundary

The chart remains open until `det(P)` roots and all column-LCM roots have
been extracted and the corresponding original specializations have been
closed.
