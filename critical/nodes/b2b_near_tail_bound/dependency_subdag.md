# Dependency sub-DAG

```text
x4_exact_slice_f2_guard_route_cut [PROVED]
  --ev--> b2b_near_tail_bound [PROVED]

b2b_near_tail_bound --req--> x4_exactlist_staircase_split [CONDITIONAL]
b2b_near_tail_bound --ev--> u2c_exact_slice_extras_budget [TARGET]
```

The near-tail proof reproduces the short comparison giving `t_XR<N/128`, so
the broader route cut is evidence rather than a logical prerequisite. The
interpolation and complement lemmas were already proved inside this packet.
