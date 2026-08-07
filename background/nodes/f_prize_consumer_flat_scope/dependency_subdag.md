# Dependency sub-DAG

```text
f_spi_hankel_consumer_descriptor [PROVED] --------req--+
                                                       +--> f_prize_consumer_flat_scope [PROVED]
f_imgfib_consumer_descriptor [PROVED route retirement]-req--+

f_prize_consumer_flat_scope [PROVED]
  --ev---> f_global_packing_step [TARGET]
  --req--> f_primitive_case [CONDITIONAL]
```

Supporting exact interfaces:

```text
l1_full_petal_fpc5_payment [TARGET] --------req--+
l1_mixed_petal_amplification [TARGET] ------req--+--> imgfib [CONDITIONAL]
```

The full-locator Pade theorem identifies a polynomial section, not a linear
Conjecture-F flat. LIST's open branches remain direct L1 targets.
