# Cycle 454: DLI fixed-weight ambient-Q bridge

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 8b6666db1
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
```

Canonical and upstream remained unchanged. Upstream's primitive-Q theorem is
on main from `a3017697a`; it is image-normalized, asymptotic, and conditional
on a separate Sidon moment payment.

## Action

Determine whether upstream fixed-density primitive Q has an exact transport
to the local C2'' Haar correlation target, and isolate every normalization
loss.

## Result: PROVED finite compiler

Every odd Haar band is a sum of iid differences. The terminal event has the
same form after pairing antipodal terminal blocks. Their additive Fourier
transforms are therefore nonnegative, and Fourier inversion gives

```text
P(T_m) product_(j<m) P(O_j) >= q^-t.
```

On a fixed-weight slice, write `f_w` for the primitive zero-fiber size and
`L_w` for the realized image size of the full `t`-moment map. Then

```text
J_prim <= sum_w [binom(n,w)/2^n]
                  (q^t/L_w) [f_w L_w/binom(n,w)].
```

The last bracket is exactly image-normalized Q inflation. The factor
`q^t/L_w` is the effective-image defect that cannot be dropped. Vandermonde
independence and complementation prove `f_w=0` for `w<=t` and `w>=n-t`, so
the official aspect leaves only fixed-density layers.

This pays the entire Haar denominator and changes the open problem from a
multi-event correlation theorem to one weighted finite ambient-Q estimate.
The target remains open because upstream's `exp(o(n))` loss and unprinted
image defect do not imply 21 bits.

## Burn-down

```text
node/workboard item: dli_c2pp_joint_reserve / HAAR-21
result: denominator CLOSED; exact Q transport and normalization proved
DAG delta: +1 PROVED background node, +1 req edge, +1 evidence edge
critical status delta: none
upstream overlap: primitive Q + exact image/ambient normalization
new assumptions: none
Modal spend: zero
next action: attack the weighted ambient-Q numerator, preferably by proving
             a finite effective-image plus Sidon payment on the nested prefix
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_fixed_weight_ambient_q_bridge/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_fixed_weight_ambient_q_bridge/verify_audit.py
```
