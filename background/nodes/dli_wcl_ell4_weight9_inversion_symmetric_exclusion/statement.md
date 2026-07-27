# WCL `(4,9)` inversion-symmetric exclusion

- **status:** PROVED
- **closure:** proof plus exact certificate
- **consumer:** `dli_wcl_slot_4_9_emptiness` (component evidence)
- **dependency:** `dli_wcl_ell4_weight9_quartic_divisor_descent`

Let `K` have characteristic zero or characteristic

```text
p not in {2,3,17,19}.
```

There is no monic quartic `A in K[Y]` for which

```text
P(Y)=Y A(Y)^2-1
```

divides `Y^1024-1` and the nine roots of `P` are invariant as a set under
`y -> y^(-1)`.

In particular this component is empty at every official WCL row, since an
official characteristic satisfies `v_2(p-1)>=41` and therefore is not one
of `2,3,17,19`.

This is a component theorem. An arbitrary nine-element subset of
`mu_1024` need not be inversion-invariant, so the result does not prove the
full `(4,9)` slot empty.

## Falsifier

A field of characteristic outside `{2,3,17,19}` and a monic quartic `A`
passing both exact checks above.
