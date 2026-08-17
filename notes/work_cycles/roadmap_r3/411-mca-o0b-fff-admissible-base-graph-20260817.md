## MCA O0b `FFF` admissible base graph (2026-08-17)

### Exact result

The already route- and rank-saturated common curve was lifted through
`a2m*x=a0m` and saturated only by the new base guards
`x,a0m,a2m`.

```text
initial graph:      dimension 1, basis size 53
after x != 0:      dimension 1, basis size 53
after a0m != 0:    dimension 1, basis size 48
after a2m != 0:    dimension 1, basis size 48
final basis hash:  7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e
Modal app:          ap-yefWfdW7toawtaFcRFwAG1
```

The admissible base graph survives. Therefore no FFF closure is claimed.
The 48-element basis is an exact, smaller source for all subsequent outside
equations.

### Checker repair

The preregistered checker expected the `UNIT=0` marker inside a retained
30 kB stdout tail. Printing 48 basis polynomials displaced that marker. The
post-run repair relies instead on the explicit nonunit field plus dimension,
basis cardinality, and an independently recomputed basis hash. All three
hostile mutations remain rejected; the mathematical acceptance criteria are
unchanged.

### Next decision gate

1. Reduce the compressed quadratic `q5(s)` coefficient-wise modulo the
   48-element admissible graph basis.
2. Retain the exact coefficient normal forms and their hashes. Factor or
   stratify the quadratic before any global basis construction.
3. Combine it with the two quadratics in `E` from `q7,q6` through
   low-degree resultants on the one-dimensional base graph.
4. Do not adjoin the unreduced or whole-normal-form `q5` globally.
