# Conflict-4 F1 pole rate-scope audit

## Verdict

**RESOLVED.** The F1 pole/list import is rate preserving.  The clean-rate MCA
extension column does not depend on either rate-half red leaf.

## Source-level proof

The proved interleaved import works with

```text
D subset B subseteq K,       C_K=RS[K,D,kappa],
Phi(C_K)=C_B^e,              C_B=RS[B,D,kappa].
```

Neither coordinate expansion nor the pole construction changes `D` or
`kappa`; the tower recursion changes only the intermediate coefficient
field.  Hence every invoked base row has the same rate `kappa/|D|` as the
ambient row.  The proof is packaged as
`f1_pole_same_rate_scope_router`.

## Dependency consequence

The all-rate DAG path

```text
list_adjacency_closing
  -> f1_pole_list_threshold_location
  -> f1_case_pole -> f1_classification -> ext_lift -> mca_safe
```

is sound for the full prize.  It is deliberately global, however, and cannot
be used to infer the minimal premises of the clean-rate subproblem.  After
projecting the path rate by rate:

- ambient rates `1/4,1/8,1/16` consume their clean-rate list crossings;
- ambient rate `1/2` consumes `rate_half_list_adjacent_crossing`;
- `rate_half_band_closure` remains a separate rate-half MCA premise.

Therefore the clean-rate milestone excludes exactly the two rate-half
mathematical leaves

```text
rate_half_band_closure,
rate_half_list_adjacent_crossing.
```

On the current 21-red critical surface, the clean-rate mathematical milestone
has 19 leaves, not the stale 20-of-22 count in the drafting materials.

## Nonclaims

No list crossing or MCA safe row is proved here.  In particular,
`l1_mixed_petal_amplification` remains load-bearing for the clean list and F1
pole columns.  The result validates a partial-credit scope; it does not make
an MCA-only resolution possible.

## Upstream-v4 side finding

Przemek's `main@32a41660` adds the Grande Finale v4 moving-root theorem for a
genuine one-parameter projective locator pencil.  It does not presently
discharge our XR mismatch leaf: our canonical generic charts are arbitrary
MDS kernel-ray charts, and no proved cover places all of their selected
locators in one pencil or pays the number of pencils.  Importing the local
pencil bound without that cover would repeat the support-to-slope error the
v4 workboard explicitly forbids.
