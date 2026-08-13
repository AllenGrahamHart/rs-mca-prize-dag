# Partition probe results

The deterministic follow-up probe enumerates all fifteen integer partitions
of the total excess `e=7`. For a partition `(a_1,...,a_s)`, it assigns those
positive column excesses and `21-s` zero excesses, constructs a `28`-row
incidence table of row degree five with the required column degrees, and
applies twenty degree-preserving switches.

The same `21` realizations per partition are tested over each of `F_337` and
`F_421`. Every resulting all-excess matrix has the expected `28` columns and
rank `28`:

```text
profiles=15
cases=15*21*2=630
minimum_rank=28
deficient=[]
```

Replay:

```bash
python3 background/nodes/rate_half_ca_hankel_a1_first_degree_core_one_quadratic_gap_four_double_root_nonreduced_unshared_collision_shape_a_all_excess_parameter_mds_gate/verify_probe.py
```

This is evidence only. The scan exhausts the excess partitions but samples
incidence realizations, and its `e=7` model has no positive padding degree.
It neither proves universal full rank nor excludes a block-supported kernel
on the official Shape-A profile.
