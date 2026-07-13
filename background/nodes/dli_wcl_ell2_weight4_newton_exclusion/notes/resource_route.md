# Retired order-1024 norm route

Before the Newton proof was noticed, Modal run
`ap-uTKpLGESwJrztApixjtGHb` measured the resource cost of extending the
weight-3 norm method to weight 4. The single implementation reported

```text
22,639,016,960 raw signed supports
     4,677,210 normalized-section construction upper bound
     4,636,056 distinct normalized-section keys
       100,926 affine-Galois classes
```

The class enumeration took 111.59 worker-seconds. A deterministic spread
sample of 256 class norms then produced 203 complete PARI factorizations and
53 bounded 110-second timeouts, with no ambient candidate among the completed
sample. The run terminated as `SAMPLE_PARTIAL`; it is not an exclusion theorem
and the zero-hit observation is not evidence about the 53 unresolved norms or
the unsampled classes.

The exact algebraic proof uses both odd moments and supersedes this route.
Scaling the first-moment-only factor sweep would discard the decisive
structure and is therefore retired. The script and compressed partial artifact
are retained only to make that route decision reproducible.
