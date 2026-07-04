# Frontier audit: worst-word challenger pricing

Status: TARGET, intentionally left open.

This node is the missing pricing/classification step for the low-slack
non-planted challenger class exposed by E15.  The DAG currently wires it
directly into `worst_word_planted` and gives it no predicate inputs.

To close it, one needs either:

- a proof that planted words plus the E15-successor challenger family exhaust
  the relevant worst-word supremum, with both classes priced; or
- a falsifier exhibiting a third challenger class, followed by the revised
  pricing route for that class.
