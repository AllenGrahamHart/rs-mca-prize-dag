# Proof

Let `x` be a bad domain row with `K_x=0`. The local trace theorem gives
`K_x=-H_xJ_x`. If `J_x=0`, its relation

```text
Phat_xE_Z=Qhat_xV_x
```

forces `Qhat_x|E_Z`. As in the allocation theorem, this is impossible: when
`D_*=0` the right side has degree zero; when `D_*=1`, divisibility forces
`epsilon_x=1` and then `deg Qhat_x=delta_x+1>=2`. Hence `H_x=0`, so
`A_x=B_x=0`. The factor `X-x` divides `A,B`, and trace vanishing says it also
divides `K`. Multiplying over these rows proves the `X_0` divisibilities.

If the exceptional trace vanishes, the two allocations and their
divisibilities are exactly those proved in the allocation theorem. If it is
active, no exceptional factor is removed. This gives `(ACR2),(ACR3)`.
Substitute those factorizations and `B_X=X_0X_1`,
`E_Z=Z_WZ_BE_a` into the two complements and first weld identity. Cancelling
`Z_W`, `X_0`, and `X_0Z_WZ_B`, respectively, gives `(ACR4)`. Nonvanishing of
`K_a` follows from `K!=0`.

Now let `x` be a root of `X_0`. At a clean supported slope `gamma`, the
second equation in `(ACR4)` specializes to

```text
Q(gamma;X)A_a(gamma;X)=P_X(X)X_1(X).                 (1)
```

The root sets of `P_X,X_1,X_0` are disjoint. Therefore `Q(gamma;x)!=0` at
every clean slope. The row `q_x` can have at most the one exceptional
supported root, and only when `D_*=1`. Its deficit is at least `e_*-D_*`.
Summing over the `z` zero-trace rows gives `(ACR5)`.

If `D_*=0`, even one such row would cost `e_*`, but

```text
C_*=e-5b-1<e-b=e_*.
```

Thus `z=0`. Suppose `D_*=1`. Two zero rows would cost at least
`2(e_*-1)>C_*`, so `z<=1`. If `z=1`, then

```text
C_*>=e_*-1
```

becomes `e-5b>=e-b-1`, hence `4b<=1` and `b=0`. The zero row has no clean
roots. If it also lacks the exceptional root, its deficit is `e` and consumes
all `C_*=e`; hence `c=1`, there is no active domain row, and the exceptional
trace must be active by the trace-free exclusion. If it has the exceptional
root, its deficit is `e-1`, leaving exactly one unit of capacity. There is
therefore exactly one further bad row, of deficit one, and it is active by
the definition of `X_1`. This proves `(ACR6)` and exhausts the cases. QED.
