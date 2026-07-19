# Proof

For `D_*=0`, `(ETA1)` is immediate. Assume `D_*=1`.

If the exceptional trace is active, the active-core theorem sets
`E_a=E_Z,Z_W=Z_B=1`; its first equation is `(ETA1)`.

Now assume the exceptional trace vanishes. If `Z_W=E_Z`, the first active-core
equation is

```text
Q V_a+P_XW_a=P_cl.                                    (1)
```

The exceptional local theorem gives

```text
deg gcd(Q(gamma_0;X),P_X)>=e+3b>0.
```

At a common root over the splitting field, specialization of `(1)` at
`gamma_0` reads `0=P_cl(gamma_0)`, a contradiction. Therefore `(ETA2)` holds,
and the first equation becomes `(ETA1)`.

It remains to show that no zero domain trace accompanies a zero exceptional
trace. By the active-core theorem, a zero domain trace occurs only in one of
the two `b=0,D_*=1` boundary profiles. In the `c=1` profile there is no active
domain trace, so the theorem already forces the exceptional trace to be
active. In the `c=2` profile, let `x_0` be the zero-trace row. It is a root of
the exceptional fiber `q_0`, while it is a root of neither `P_X` nor the sole
active factor `X_1`. Under `(ETA2)`, the second active-core equation is

```text
Q A_a+P B_a=P_XX_1.                                   (2)
```

At `gamma_0`, equation `(2)` makes `q_0` divide `P_XX_1`, contradicting the
root `x_0`. Hence `X_0=1` and `X_1=B_X` whenever the exceptional trace is
zero. The squarefree degree-`r-1` assertion is exactly the `Z_B` conclusion
of the allocation theorem. Substitution in `(ACR4)` gives all three systems
in `(ETA4)`. QED.
