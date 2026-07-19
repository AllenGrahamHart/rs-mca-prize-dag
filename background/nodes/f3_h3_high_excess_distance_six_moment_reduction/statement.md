# H3 high-excess distance-six moment reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_distance_four_fiber_degree_cap`,
  `f3_h3_excess_budget_degree_tradeoff`

For the selected high tail, put

```text
M_6,33=sum_(t!=1,P(t)>=33) N_6(t)R(t).             (H6M1)
```

Every retained target satisfies

```text
P(t)-18 <=(8/21)N_6(t).                            (H6M2)
```

The constant is sharp for the integer bounds used here: on the antipodal
branch, excess `16` permits `m=15`, norm-aware centroid weight `98`,
distance-four count `28`, and hence the guaranteed `N_6=42`.

Consequently

```text
136 M_6,33
  <=21(300n^2-238(n-1)(n-2))                       (H6M3)
```

implies the selected `E=14` tail estimate and therefore C36'. Conservatively,

```text
M_6,33 <=(651/68)n^2 <9.574n^2.                   (H6M4)
```

Thus no distance-four moment estimate is needed for this route. The complete
remaining analytic object is the distance-six part `I_6` of the canonical
edge–quotient incidence router.
