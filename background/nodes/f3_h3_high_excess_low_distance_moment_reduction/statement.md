# H3 high-excess low-distance moment reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_excess_multistar_degree_ladder`,
  `f3_h3_excess_budget_degree_tradeoff`

For each nonidentity product target `t`, let `N_4(t)` and `N_6(t)` count
unordered edges of squared distance four and six among all unordered
representations of `t` whose coefficient vectors have squared norm at most
three. Put

```text
W(t)=2N_4(t)+N_6(t),
M_33=sum_(t!=1,P(t)>=33) W(t)R(t).                 (HLM1)
```

Every retained target satisfies

```text
P(t)-18 <= (16/83) W(t).                           (HLM2)
```

The constant is sharp for the integer centroid ledger: at excess `16`, the
guaranteed small-vector count is `15` and the minimum edge weight is `83`.

Consequently the single weighted low-distance moment estimate

```text
272 M_33
  <=83(300n^2-238(n-1)(n-2))                      (HLM3)
```

implies the selected `E=14` high-tail estimate and hence C36'. The
conservative form of `(HLM3)` is

```text
M_33 <= (2573/136)n^2 < 18.92n^2.                 (HLM4)
```

This reduction retains the exact distance split

```text
M_33=2 sum_(P(t)>=33) N_4(t)R(t)
       +sum_(P(t)>=33) N_6(t)R(t).                 (HLM5)
```

The first term is governed by the proved two-variable distance-four routers;
the second is the generic six-term collision lane. No estimate for either
term is asserted here.
