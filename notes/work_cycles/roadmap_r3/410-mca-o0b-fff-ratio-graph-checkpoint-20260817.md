## MCA O0b `FFF` ratio-graph checkpoint (2026-08-17)

### Exact compression

On the guarded graph `a2m*x=a0m`, exact symbolic identities divide
`q5` and `q6` by the nonzero factors `a2m^4` and `a2m^2`
respectively, while preserving `q7`. The resulting necessary subsystem
retains every admissible `FFF` point and continues to omit `q4`.

```text
graph basis:             dimension 3, size 53 (including free E,s)
compressed q5 normal:   degree 46, 3,126 terms
previous q5 normal:     degree 90, 4,717 terms
outcome:                timeout adjoining compressed q5
Modal app:              ap-WC4Rt0hC5xsMcfle0ioaP9
```

This is a strict algebraic simplification, not a chart closure.

### Next decision gate

1. Work in the five-variable base graph `x,t,r,c,b`, before adjoining
   the free variables `E,s`.
2. Saturate that one-dimensional graph by the 16 route guards and the
   required nonzero `x,a0m,a2m` factors. Record every exact stage.
3. If the admissible graph becomes unit, close `FFF` immediately. If it
   survives, use the smaller saturated basis for coefficient-wise
   `q5` reduction and low-degree `s,E` resultants.
4. Do not repeat the unsaturated global `q5` basis.

### Resource discipline

The base-graph saturation is a single bounded Modal pilot. Local commands
remain RAM-guarded and no local CAS is authorized.
