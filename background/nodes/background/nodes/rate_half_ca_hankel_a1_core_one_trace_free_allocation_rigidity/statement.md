# `A=1` core-one trace-free allocation rigidity

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_nonzero_weld_trace_descent`

Retain the official core-one maximal-degree sharp cap and the notation of the
trace-descent theorem.

## 1. Exact defect-norm factorization

For every root `x` of `B_X`, define

```text
N_x=Qhat_x/E_Z^epsilon_x,       deg N_x=delta_x.       (TFA1)
```

The division is literal when `epsilon_x=1`, because the exceptional
supported-slope factor is then a root of `q_x` and is coprime to `R_x`.
If `S_*` is the exact dominant-component residual form from the norm identity,
then, up to one nonzero scalar,

```text
S_*=product_(x:B_X(x)=0)N_x,
deg S_*=sum_x delta_x=C_*.                             (TFA2)
```

Thus the small global norm residual is exactly the product of the local
unsupported or repeated-root quotients; no further residual factor is hidden.

## 2. Rigidity when every defect trace vanishes

Assume the factor-descent branch, so every trace in the previous theorem
vanishes and `K=B_XE_ZK_1`. Then every root of `B_X` is forced into the same
allocation:

```text
B_X divides both A and B.                              (TFA3)
```

There is no `W`-allocation for a bad domain factor. Such an allocation would
force `Qhat_x|E_Z`. If `D_*=0` this is impossible by positive degree; if
`D_*=1`, it would make `epsilon_x=1` and hence
`deg Qhat_x=delta_x+1>=2`, again impossible for the linear form `E_Z`.

If `D_*=1`, partition the exceptional factor by

```text
Z_W=E_Z, Z_B=1       when H_0=0,
Z_W=1,   Z_B=E_Z     when H_0!=0.                      (TFA4)
```

Then `Z_W` divides both `V,W`, while `Z_B` divides `B`. In the `Z_B=E_Z`
case one additionally has

```text
Qhat_0 divides B_X,
q_0=Q(gamma_0;X) is squarefree of degree r-1 and divides G_X. (TFA5)
```

For `D_*=0`, set `Z_W=Z_B=1`. There are biforms `A_1,B_1,V_1,W_1` with

```text
A=B_XA_1,       B=B_XZ_BB_1,
V=Z_WV_1,       W=Z_WW_1,                              (TFA6)
```

and the complete trace-free system reduces to

```text
Q V_1+P_X W_1=P_cl Z_B,
Q A_1+P_cl Z_B B_1=P_X,
W_1B_1-1=QK_1,       K_1!=0.                           (TFA7)
```

This theorem removes all arbitrary factor allocations from the trace-free
branch. It does not exclude the reduced complement square or any active-trace
branch, and it does not close `rate_half_band_closure`.
