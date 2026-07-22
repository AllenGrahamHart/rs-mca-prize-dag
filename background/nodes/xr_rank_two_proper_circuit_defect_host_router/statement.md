# XR proper rank-two circuits have a defect and host-core router

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rank_two_maxwell_collision_defect_identity`,
  `xr_higher_rank_rank_two_shell_maxwell_router`,
  `xr_higher_rank_uniform_split_pencil_reduction`,
  `xr_trade_circuit_arity_segre_atlas`

Let `J` be a four- or five-block rank-two row-scaling circuit that is a
proper subset of one minimal Maxwell core `G`. Put

```text
t=|J| in {4,5},       r=|G\J|,
Delta_J=2|union_(i in J) A_i|-2a-ht,
D_0=t h+(t-2)((t-1)D-2Z),
C=(t-2)I+sigma+H.                                  (PC1)
```

Then, with `delta_4=2` and `delta_5=1`,

```text
Delta_J=D_0+2C>=delta_t,
C>=max{0,(delta_t-D_0)/2}.                          (PC2)
```

The quotient in `(PC2)` is integral. If the same shell data were supported
on every block of a minimal core, the full-core bound would instead be

```text
C<=floor(-D_0/2).                                  (PC3)
```

Thus the proper-circuit and full-core defect ranges are disjoint by exactly
one integer charge at every nonpositive baseline. If `D_0<delta_t`, a proper
circuit must have at least one canonical defect type:

```text
I>0,       sigma>0,       or       H>0.             (PC4)
```

If `e` is the surplus of the host core, `Delta_G=-e` with `0<=e<=h-1`, then
the number of host blocks outside the circuit obeys

```text
r>=ceil((Delta_J+e)/h)
 =ceil((D_0+2C+e)/h).                               (PC5)
```

There are also exact shell cutoffs for the baseline-positive branch
`D_0>=delta_t`. The pair-mass floor implies

```text
t=4:  D<=2h-2 if D is even,   D<=2h-3 if D is odd;
t=5:  D<=floor((5h-1)/3) if D is even,
       D<=floor((5h-10)/3) if D is odd.             (PC6)
```

Above the appropriate cutoff every proper owner is necessarily in the
defect-bearing branch `(PC4)`.

This theorem separates and prunes pointed records. It does not bound the
number of proper-circuit embeddings, choose a canonical witness inside a
positive defect type, count surviving host cores, classify higher trade rank
or nonuniform cells, or prove P-A.
