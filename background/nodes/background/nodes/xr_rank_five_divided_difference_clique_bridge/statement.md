# XR rank-five divided-difference clique bridge

- **status:** see `dag.json` (single source of truth)
- **consumer:** `xr_highcore_collision_count`
- **dependency:** `xr_rank_five_ratio_minor_dictionary`

Work in the retained P-A `u=v=0` rank-five core. For a five-set `S` of
evaluation coordinates, write

```text
[S]f = sum_(x in S) f(x) / product_(y in S\{x}) (x-y)
```

for the fourth divided difference, equivalently the leading coefficient of
the degree-at-most-four interpolant to `f` on `S`.

Every five-set `S` inside every retained `m=4+h` agreement set `A` satisfies

```text
[S]q != 0.                                             (DD1)
```

Consequently the global five-set coloring

```text
Phi(S)=[S]U/[S]q                                      (DD2)
```

is defined on all five-subsets of every retained agreement set. If the
selected codeword on `A` is `c=gamma q+p`, with `deg p<4`, then

```text
Phi(S)=gamma                 for every S subset A, |S|=5.  (DD3)
```

Thus every retained agreement set is a monochromatic `m`-clique, and
different retained sets have different colors. Moreover, for a four-set
`T subset A` and `x` outside `T`,

```text
Phi(T union {x})-gamma = (U-c)(x)/(q-I_Tq)(x).          (DD4)
```

Hence the ratio fibers and zero minors from the preceding node are exactly
equal-color stars of this one global divided-difference coloring.

The theorem is an exact transport from the XR collision-line core to a
base-field split-pencil/support census. It does not supply the missing
monochromatic-clique count and does not promote P-A.
