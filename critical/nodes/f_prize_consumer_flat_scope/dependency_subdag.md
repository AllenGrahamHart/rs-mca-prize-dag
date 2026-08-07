# Dependency sub-DAG

```text
f_spi_hankel_consumer_descriptor [PROVED] --------req--+
                                                       +--> f_prize_consumer_flat_scope [CONDITIONAL]
f_imgfib_consumer_descriptor [TARGET] -------------req--+

f_prize_consumer_flat_scope [CONDITIONAL]
  --ev---> f_global_packing_step [TARGET]
  --req--> f_primitive_case [CONDITIONAL]
```

Supporting exact interfaces:

```text
f_termination_mds [PROVED coordinate branch] ----------------ev--+
l1_rootfree_rational_q_projective_packing [PROVED punctured cell]-ev--+--> f_imgfib_consumer_descriptor [TARGET]
```

The full-locator Pade theorem identifies a polynomial section, not a linear
Conjecture-F flat. The root-free rational-Q theorem extracts an exact linear
cell, but it does not prove the full LIST caller inventory.
