# Strict-A=3 m=2 product-lift hunt: result

## Verdict

No product-code lift was found. Across eight 52-second Modal workers,
`599,897` independently sampled placements all gave stacked parity-check
rank exactly `32`, hence zero row-scale nullity:

```text
rank 32: 599897
positive nullity: 0
full-support biform lifts: 0
Hankel-compatible lifts: 0
```

Run:
`https://modal.com/apps/allengrahamhart/main/ap-dPpY3BMeJ2K3jWxK879KVv`.

## What was tested

At `m=2`, exact endpoint saturation forces 31 double-root domain rows and
one single-supported-root row. The double-root incidence graph is uniquely
shaped up to relabelling: `K_9` minus a two-edge path centered at the
singleton vertex and minus a perfect matching on the remaining six
vertices.

For each trial over `F_97`, the worker chose nine supported slopes, one
unsupported residual root, and a random placement of the 32 forced row
labels on `D=mu_32`. It then asked whether arbitrary nonzero row scales make
all three quadratic coefficient vectors members of `RS[D,8]`. A survivor
would have been reconstructed and sent to the exact four-layer Hankel
compatibility system.

## Zero-power declaration

The null result is not a theorem and is weak evidence about existence. A
generic `72 x 32` parity system is expected to have full column rank over
`F_97`; a realizable placement, if one exists, must occupy a very thin and
structured subset of the assignment space. Increasing this random sample
would mostly repeat the same generic-rank observation.

The useful conclusion is methodological: do not continue random placement
sampling. A successor must classify the near-saturated biform or search a
coverage-defined structured family. The already-proved quartic-coset lift
obstruction handles the strongest natural structured family currently in
hand.
