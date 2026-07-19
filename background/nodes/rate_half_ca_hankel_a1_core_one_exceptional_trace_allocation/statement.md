# `A=1` core-one exceptional-trace allocation

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_active_trace_core_reduction`

In every official active core, the first complement has the full supported
product:

```text
Q V_a+P_X W_a=P.                                      (ETA1)
```

When `D_*=0`, this is immediate because `P_cl=P`. Suppose `D_*=1`.

1. If the exceptional trace is active, then `E_a=E_Z` and `(ETA1)` is the
   first equation of `(ACR4)`.
2. If the exceptional trace is zero, the allocation `Z_W=E_Z` is impossible.
   The only allocation is

   ```text
   Z_B=E_Z,       Z_W=E_a=1.                          (ETA2)
   ```

   Moreover every bad-domain trace is active (`X_0=1,X_1=B_X`), and

   ```text
   q_0=Q(gamma_0;X) is squarefree of degree r-1 and divides G_X. (ETA3)
   ```

Thus the active cores have exactly the following exceptional forms:

```text
D_*=0:
  QV_a+P_XW_a=P,
  QA_a+P B_a=P_XX_1,
  W_aB_a-X_1=QK_a;

D_*=1, exceptional trace active:
  QV_a+P_XW_a=P,
  QA_a+P_cl B_a=P_XX_1,
  W_aB_a-X_1E_Z=QK_a;

D_*=1, exceptional trace zero:
  X_1=B_X,
  QV_a+P_XW_a=P,
  QA_a+P B_a=G_X,
  W_aB_a-B_X=QK_a.                                   (ETA4)
```

The theorem removes the `Z_W` branch and every mixed zero-exceptional/
zero-domain core. It does not exclude the three active systems in `(ETA4)`.
