# proof: m720_mitm_enumerator_soundness

The function `mitm_slice` has two phases.

In phase 1 it loops over every `(h-1)`-subset `tri` of `range(1,W)` and forms

```text
P = (0,) + tri.
```

It computes `sig_general(P)`, which is exactly the tuple of elementary
signatures `e_1,...,e_{h-1}`, and stores the packed `tri` in the table bucket
for that signature. For `n <= 1024`, every exponent fits in 11 bits, so
`_pack` and `unpack` are inverse on every tuple used by the scan.

In phase 2 it loops over every `h`-subset `Q` of `range(1,W)`, computes the
same lower signature, and inspects exactly the phase-1 candidates with that
signature. It then checks:

```text
P cap Q = empty,
e_h(P) != e_h(Q).
```

Thus every counted pair is a disjoint anchored trade in the declared sense.
Conversely, any disjoint anchored trade with support in `[0,W)`, with `0` in
the anchored half, appears in phase 1 under its lower signature and appears in
phase 2 as the corresponding `Q`, so it is counted.

The toral classification is delegated to `is_coset`, which tests exactly
whether a half is a full `mu_h` coset: it first requires `h | n`, then checks
that the sorted exponent set equals

```text
{r0 + j(n/h) mod n : 0 <= j < h}.
```

The pair is marked toral exactly when both halves pass this test; otherwise it
is marked non-toral.

Finally, `complete` is set only when `W == n` and the run did not abort. Hence
window slices are never silently promoted to full-row zero certificates.
This proves the stated soundness and completeness contract for the MITM
enumerator.
