# C2 primitive square-root falsifier: preregistration

## Question

The proved primitive telescoping identity reduces C2'' to

```text
J_prim = 2^(nm)(Z_0-C_1)/(Z_m product_(j<m) B_j) <= 2^21.
```

At the official `n=2^41`, the scale-free inequality

```text
J_prim <= sqrt(2n)                                      (SQRT)
```

would give exactly the required 21 bits. This pilot tries to falsify
`(SQRT)` before any proof effort. It does not add `(SQRT)` to the DAG.

## Frozen grid

Use `t=2`, where the full tower has one junction and an exact dynamic
program over `F_q^2` reaches larger `n` than the existing meet-in-the-middle
bank:

```text
n=32:  q in {97,5857}                 controls
n=64:  q in {193,257,449,577,769,1153}
n=128: q in {257,641,769,1153}
n=256: q in {769}
```

Every listed `q` is prime and `q=1 mod n`. The fixed controls must reproduce
the banked ratios, including the current maximum at `(32,2,5857)`.

## Exact statistic

For each row compute exact integers:

```text
Z_0 = #{x in {0,1}^n : p_1(x)=p_2(x)=0},
C_1 = Z_0(q,n/2,1),
Z_1 = weighted level-one even-block census,
B_0 = weighted first odd-block census,
J_prim = (Z_0-C_1) 2^n/(Z_1 B_0).
```

The gate is integer-only:

```text
FIRE iff ((Z_0-C_1)2^n)^2 > 2n (Z_1 B_0)^2.
```

## Interpretation

- Any firing kills `(SQRT)` as a universal C2 route.
- Survival is numerical evidence only, with no `t=2 -> t=2^33` transport.
- The pilot may suggest a sharper or weaker candidate, but no fitted
  candidate becomes a DAG premise.
- A row timeout is reported as partial output, never silently dropped.

## Compute and cost

Each row is one Modal task with four CPUs, 4 GiB, a 240-second subprocess
timeout, and a 300-second container timeout. The launcher checkpoints after
each returned row. The frozen grid has 13 rows and is expected to cost well
below one dollar. No local census is permitted.
