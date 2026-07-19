# `A=1` core-one active-trace core reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_trace_free_exclusion`

Retain the official core-one maximal-degree face. Let `X_0` be the product of
the roots `x` of `B_X` for which the domain trace `K_x` vanishes identically,
and write

```text
B_X=X_0X_1.                                            (ACR1)
```

Every factor of `X_0` divides `A,B,K`; every root of `X_1` has an active
factorization `K_x=-H_xJ_x!=0`.

If `D_*=1` and the exceptional trace vanishes, allocate `E_Z=Z_WZ_B` exactly
as in the trace-free allocation theorem: `Z_W` divides `V,W`, or `Z_B`
divides `B`. Put `E_a=1`. If the exceptional trace is active, put

```text
Z_W=Z_B=1,       E_a=E_Z.                              (ACR2)
```

For `D_*=0`, all three forms are one. There are biforms
`A_a,B_a,V_a,W_a,K_a`, with `K_a!=0`, such that

```text
A=X_0A_a,       B=X_0Z_BB_a,
V=Z_WV_a,       W=Z_WW_a,
K=X_0Z_WZ_BK_a,                                      (ACR3)
```

and the complete active-core system is

```text
Q V_a+P_X W_a=P_cl Z_B E_a,
Q A_a+P_cl Z_B B_a=P_X X_1,
W_aB_a-X_1E_a=QK_a.                                  (ACR4)
```

Every root of `X_1` is an active domain trace, and `E_a=E_Z` exactly when the
exceptional trace is active. The trace-free exclusion proves that at least
one factor in `X_1E_a` is active.

Write `z=deg X_0`. A zero-trace bad row has no clean supported root, so its
deficit is at least `e_*-D_*`. Exact capacity gives

```text
z(e_*-D_*)<=C_*.                                      (ACR5)
```

At the official row this leaves exactly the following alternatives:

1. `z=0`: every bad-domain trace is active;
2. `z=1,b=0,D_*=1`, and, writing `epsilon_0` for the exceptional incidence
   at the zero-trace row,

   ```text
   epsilon_0=0:       c=1, X_1=1, E_a=E_Z;
   epsilon_0=1:       c=2, X_1 has one root of deficit 1. (ACR6)
   ```

No second zero-trace bad row is possible. This is an exact normalization and
capacity classification of the remaining active branch; it does not exclude
the displayed active cores or close `rate_half_band_closure`.
