# C2 primitive square-root falsifier: report

## Verdict

The preregistered `(SQRT)` falsifier did not fire. All 13 exact rows
returned. The only ratio above one is the already banked control
`(n,t,q)=(32,2,5857)`, where

```text
J_prim = 14680064/5498847,
log2 J_prim = 1.4166572071441266,
log2 sqrt(2n) = 3.
```

Every new `n=64,128,256` ratio is strictly below one by exact integer
comparison. Thus the old row remains the maximum and has `1.5833` bits of
slack even against the proposed square-root bound.

## What was checked

For `t=2`, a C++ dynamic program computed exact arbitrary-precision values
of `Z_0,C_1,Z_1,B_0` over `F_q^2`, then applied the proved identity

```text
J_prim = (Z_0-C_1)2^n/(Z_1B_0).
```

The two `n=32` controls reproduce the frozen bank exactly. Every primitive
count is divisible by `n`, independently checking rotation-orbit ownership.
The gate `J_prim^2>2n` was evaluated with integers only. The zero-looking
floating displays on several large rows are formatting cancellation; their
stored exact numerators are strictly smaller than their denominators.

## Interpretation

`J_prim<=sqrt(2n)` remains a plausible closing theorem and would specialize
to the exact 21-bit reserve at `n=2^41`. This experiment does not prove it,
does not test tower depths above one on the new sizes, and licenses no
`t=2 -> t=2^33` transport. It should guide proof search but must not become a
DAG premise without a proof.

## Replay

```text
tools/ramguard modal -- modal run notes/pilots_20260818/c2_primitive_sqrt_falsifier/modal_run.py --output notes/pilots_20260818/c2_primitive_sqrt_falsifier/results.json
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_primitive_sqrt_falsifier/analyze.py
tools/ramguard tiny -- python3 notes/pilots_20260818/c2_primitive_sqrt_falsifier/analyze.py --tamper-selftest
```

Modal run: `ap-Wp4hwSuVlFwEDllxpual4c`. All tasks completed in at most
`8.29` seconds; 13 containers, four CPUs and 4 GiB requested per task.
The frozen result SHA-256 is
`08f8acfc3201bc0e2918cd7da4769a90224334dbee9211ad4763df477fc93022`;
the executed C++ source SHA-256 is
`d706ba994d30e99ee197860716a47c104fdb7491e6d7b9707d476142dbe8114e`.
