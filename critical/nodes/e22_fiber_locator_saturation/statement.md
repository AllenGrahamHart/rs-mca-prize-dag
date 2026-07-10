# e22_fiber_locator_saturation

- **status:** PROVED
- **closure:** proof

## Statement

Let `D` be the multiplicative subgroup domain, let `M | |D|`, and let `z` be
in the image of the quotient map

```text
pi_M(x) = x^M.
```

Then the fiber over `z`,

```text
F_z = {x in D : x^M = z},
```

has locator

```text
L_{F_z}(X) = X^M - z.
```

Consequently, for any squarefree support locator `L_R`, divisibility
`X^M-z | L_R` is equivalent to `F_z subset R`. Products of distinct quotient
fiber factors are therefore exactly local unions of full quotient fibers.

## Falsifier

A quotient value `z` whose fiber locator is not `X^M-z`, or a squarefree
support locator divisible by `X^M-z` without containing the whole fiber.
