# DLI WCL scope guardrail

- **status:** PROVED
- **closure:** proof

## Statement

The extension of WCL-ZONE from official DLI production rows to all isolated
generated prime-field C1' rows is false. At

```text
(q,n',N,ell) = (65537,512,256,1),
omega         = 15028,
```

`omega` has exact order `512` and

```text
1 + omega^95 - omega^146 = 0 mod q.
```

This is a primitive reduced weight-3 relation and has a full signed-shift
orbit of size `2N=512`. It is a first owner at the smallest positive level,
so its single-orbit C1' ledger charge is

```text
2N 2^-3 = 64 > 1/32.
```

The row satisfies the isolated C1' aspect conditions, but it is not an
official DLI production row: `v_2(q-1)=16`, whereas the production tower's
top generated subgroup has order `2^41`.

## Falsifier

Failure of primality, exact order, the displayed relation, primitiveness,
full orbit size, the C1' aspect pins, or the ambient-scope separation.
