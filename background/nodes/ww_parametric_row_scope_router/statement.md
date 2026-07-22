# W3 parametric row-scope router

- **status:** PROVED
- **dependencies:** `official_row_primes_pinning`, `descriptor`
- **consumer:** `ww_row_envelope_clause` (evidence only)

The prize statement specifies an admissible family of Reed-Solomon rows; it
does not specify a named finite registry of "official rows" or literal row
primes.  Write a row by the admissible input tuple

```text
(p,e,s,rho),  q=p^e,  n=2^s,  k=rho*n.
```

For every such input, the proved row descriptor computes the exact row
constants, including `q`, `n`, `k`, and

```text
B*=floor(q/2^128).
```

Consequently, a finite pre-enumerated official-row registry and a table of
rowwise field orders were not prerequisites for testing W3.  A prize-scope
universal claim would instead have required either:

1. one family-uniform proof over every admissible descriptor; or
2. a proved-total parameterized certificate generator and checker which take
   the exact row descriptor and cell data as input.

Certificates for finitely many named exhibits remain valid calibrations, but
do not discharge W3's universal quantifier by themselves.

This router does **not** prove the W3 challenger envelope. It made the row and
scope exact enough to distinguish W3's safe-side claim from an invalid
all-cell extension. The later `ww_spending_cell_fiber_layout_counterexample`
refutes that extension at an admissible unsafe spending cell. W3 remains open
but retired from the prize path, so no certificate campaign is currently
owed.
