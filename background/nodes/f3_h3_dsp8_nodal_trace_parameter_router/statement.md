# DSP8 nodal-trace parameter router and marginal envelope

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_nodal_target_divisor_pruning`
- **dependencies:** `f3_h3_dsp8_unit_trace_elliptic_curve_router`,
  `f3_affine_coset_pair_optimized_stepanov`

Fix a singular trace `sigma=3c`, where `c^3=1`. Every affine nonnode point
of the trace curve has the unique rational parameterization

```text
r=-c/[theta(1+theta)],
u=-c theta^2/(1+theta),
v= c(1+theta)^2/theta,                               (NTP1)
```

with `theta notin {0,-1}` and `theta^2+theta+1!=0`. The latter two tangent
directions, when present, map back to the node and are counted separately.
Let `Q=F_p^*/H`, write `[x]` for a quotient class, and put `C=[c]`. The three
roots in `(NTP1)` lie in `H` exactly when

```text
A=[theta] in Q[3],       [1+theta]=C A^2.            (NTP2)
```

Thus each singular trace fiber is a union of at most three fixed affine
coset-pair intersections, plus the node when `c=1`. If `N_sigma` is the
number of ordered affine subgroup points `(r,u)` on that fiber, then on every
official row

```text
N_sigma<12n^(2/3)+1.                                  (NTP3)
```

For two nonnode parameters `theta,phi`, the retained DSP8 target is independent
of `c` and factors exactly as

```text
t=((theta phi-1)(theta phi+theta+1)
   (theta phi+theta+phi)(theta phi+phi+1))
  /(theta^2 phi^2(1+theta)^2(1+phi)^2).              (NTP4)
```

Let `G_sing^0,G_sing^A` be the raw curve-point/quotient records from
`G_25^0,G_25^A` whose common trace satisfies `sigma^3=27`. Then

```text
G_sing^0+G_sing^A
 <12n^(2/3)(12n^(2/3)+1)^2.                          (NTP5)
```

This is a uniform `O(n^2)` marginal envelope, but it does not pay the DSP8
constant. Indeed the available class-blind consequence is only

```text
10G_sing^0+17G_sing^A
 <204n^(2/3)(12n^(2/3)+1)^2,                         (NTP6)
```

whose leading coefficient is `29376`, versus the complete DSP8 allowance
`892`. Closing or deleting the nodal locus therefore requires exploitation
of richness, signed disjointness, the factorization `(NTP4)`, or its
correlation with the quotient line; marginal point bounds alone are fenced.
