# Cycle 455: DLI ambient-Q square-root route no-go

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: 0df91c655
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
```

Canonical and upstream remained unchanged.

## Action

Stress-test the scale-free ambient strengthening suggested by the new
fixed-weight Q bridge before investing in a finite Q proof.

## Result: ambient route FALSIFIED, Haar candidate survives

The complete `(n,t)=(32,2)` high-cap analogue contains 189 primes
`32768<q<65536`, `q=1 mod 32`. Exact meet-in-the-middle censuses find 56
ambient failures. The first explicit certificate is

```text
q=33409, Z_0=384, C_1=256, primitive=128,
K_amb=1116161281/33554432=33.264...>8.
```

The separately preregistered exact Haar follow-up computes both marginals on
all 189 rows. No true square-root failure occurs; the maximum is

```text
J_prim=2097152/505197=4.151...<8       at q=37217.
```

At `q=33409`, the denominator reduces the ratio to `1.853...`. Therefore the
formal-codomain floor is too lossy at the target scale. The ambient-Q bridge
is valid, but its scale-free use is retired. C2 proof search must retain the
actual Haar marginals or an equivalent owner-sensitive normalization.

## Burn-down

```text
node/workboard item: dli_c2pp_joint_reserve / HAAR-21
result: one candidate route REFUTED; true Haar candidate survives 189-row sweep
DAG delta: +1 PROVED background node, +1 req edge, +1 evidence edge
critical status delta: none
new assumptions: none
Modal runs: ap-cyl68HXbcxGroGwKLkgEzV, ap-f5LlJXuPCIZakI3SGTNs57
Modal spend: eight tiny containers, all compute <=3.26 seconds
next action: exploit the exact marginal inflation/primitive-orbit coupling;
             do not attack image/ambient flatness in isolation
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_ambient_q_sqrt_route_no_go/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_ambient_q_sqrt_route_no_go/verify_audit.py
```
