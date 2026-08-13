# Refutation

The former proof correctly showed that a failure of full incident-normal
rank on one selected support would make that support pair-contained.  It
then reused the remainder of the affine-span incidence proof unchanged.
That step is invalid.

For a proper subspace `W` of the normal space, the old argument asserted a
Reed-Solomon root bound on the number of coordinates with `v_x in W`.  When
the annihilating relation has nonzero slope coordinate, it involves the
received direction rather than a codeword.  Direction separation bounds
agreement only by `m-1`; it does not give the much smaller codeword-root
cap used in the ordered-basis product.

The exact counterexample makes the gap sharp.  Each zero-explanation witness
has 20 copies of one normal line and one transverse normal.  Its normals
span dimension two, but it has only 40 ordered bases.  The rejected proof
charges it for

```text
m*w=21*20=420
```

ordered bases.  The resulting bound 23 is violated by 31 selected slopes.
See `rate_half_mca_affine_span_incidence_counterexample` for the complete
construction and two independent replays.
