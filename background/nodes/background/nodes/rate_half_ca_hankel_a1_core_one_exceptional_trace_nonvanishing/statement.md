# `A=1` core-one exceptional-trace nonvanishing

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_trace_allocation`

On every official active core with `D_*=1`, the exceptional trace is active:

```text
K_a(gamma_0;X)!=0.                                    (ETN1)
```

Indeed, a zero exceptional trace would force the third system in `(ETA4)`:

```text
X_0=1,       X_1=B_X,
Q A_a+P B_a=G_X,                                      (ETN2)
```

and the exceptional fiber

```text
q_0=Q(gamma_0;X)
```

would be squarefree of degree `r-1`. Specializing `(ETN2)` at the root of
`P` gives

```text
q_0 A_a(gamma_0;X)=G_X.                               (ETN3)
```

Since `deg G_X=D_0`, this requires

```text
deg_X A_a(gamma_0;X)=D_0-r+1.                         (ETN4)
```

But `X_0=1` means `A_a=A`, and the original exact complement degree is

```text
deg_X A=D_0-r.                                        (ETN5)
```

This contradiction proves `(ETN1)`. Consequently the remaining active
systems are only

```text
D_*=0:
  QV_a+P_XW_a=P,
  QA_a+P B_a=P_XX_1,
  W_aB_a-X_1=QK_a;

D_*=1:
  QV_a+P_XW_a=P,
  QA_a+P_cl B_a=P_XX_1,
  W_aB_a-X_1E_Z=QK_a,       K_a(gamma_0;X)!=0.        (ETN6)
```

Both systems remain open; this theorem does not close the face or
`rate_half_band_closure`.
