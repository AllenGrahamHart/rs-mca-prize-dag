# Dependency sub-DAG

```text
rate_half_cyclic_rotated_prefix_floor [PROVED, lower endpoint] --+
                                                                  +--> rate_half_list_integer_johnson_safe_anchor [PROVED]
exact balanced-incidence double count [proved in packet] --------+

rate_half_list_integer_johnson_safe_anchor [PROVED]
  --ev--> rate_half_list_adjacent_crossing [TARGET]
```

The edge to the target is evidence because the safe anchor does not prove its
predecessor unsafe.
