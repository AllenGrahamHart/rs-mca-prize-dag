# Active BC to order-32 adapter

- **status:** PROVED
- **row:** deployed KoalaBear MCA at agreement `1116048`
- **input:** canonical one-per-slope active BC certificates
- **output:** exact inputs to upstream `thm:partial-relative`

For a fixed received line, if `|Z_BC|<=31`, the cell already lies below the
order-32 exceptional cardinality threshold. If `|Z_BC|>31`, every 32-subset
of canonical certificates supplies 32 distinct bad slopes, explaining data,
and exact `m`-supports on the same line. Passing through the unique maximal
agreement sets and retaining the stored exact `m`-subsupports meets the
support normalization of the partial relative order-32 theorem.

The resulting affine, rational, near-sunflower, and primitive-spread
alternatives retain the original line and slope labels. No legacy endpoint
coordinate or parameter/carrier identification is introduced.

This adapter supplies no `(S)`, `(A)`, or `(E)` payment and does not prove a
row bound.
