# Audit - PMA sigma-one paired-core abundance obstruction

## Field-row correction

The tempting NTT prime `12289` is **not** congruent to one modulo `8192`:
`12289-1=12288=3*4096`. It cannot carry an order-`8192` multiplicative
domain. The certified replacement is the official rate-half row
`(q,n,k)=(65537,65536,32768)`, where `q-1=n`. Any stale use of
`(12289,8192,4096)` is a falsifier.

## Checked points

1. For fixed core values, `U|_(H\C) <-> phi_C` is a coordinatewise affine
   bijection. No independence assumption between different cores is used.
2. `P_M` includes both the singleton choice and the unordered pair partition.
3. The falling factorial, not `q^(M+1)`, enforces distinct petal values and a
   singleton value different from every petal value.
4. The first moment proves existence of a word with many paired cores; it
   does not identify that word or show any core has nonempty Post mass.
5. `(PA3)` counts exact minimal-agreement planted anchors and uses the proved
   two-anchor nonreuse theorem.
6. Extension-field persistence is structural only. The generated-field
   reserve remains a separate ledger.

## Exact certificate

The verifier checks primality, `q=1 mod n`, and the exact integer inequality
`E A(U)>n^6` at the replacement row. It also exhausts two small prime-field
rows and mutates both the singleton factor and the distinct-value falling
factorial.
