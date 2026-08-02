# KoalaBear positive 433-1a cell-5 finite-candidate first-batch exclusion

- **status:** PROVED
- **scope:** 23 values in the proved 69-fiber router for cell 5 and signs
  `(-1,-1)`
- **consumer:** `rate_half_band_closure`

Fresh exact finite-field recomputation covers 23 routed values: the 13
regular guard/chart-norm candidates and ten coefficient-pole candidates for
which the primitive factor/map chain remains regular.  Chart 2 is used at 22
values; the sole chart-2 exception `t=1860858030` uses chart 3.

Across all 23 fibers, exact factorization of the five specialized primitive
parents gives 433 finite subfactor rows, preserving parent degrees
`4,4,4,8,4`.  Every row is excluded by exactly one of these audited reasons:

```text
383  common gcd is 1 or the target guard e^2-1;
 16  primitive subfactor has degree >1 over F_p;
 34  every F_p root of the common gcd has e=0 or
     e^2 in {1,b^2,c^2}.
```

In the second case, an actual deployed packet would have
`s=x1+2*x0+3b in F_p`, so it cannot lie on a non-linear irreducible factor of
the primitive coordinate.  The third case violates target nonzero or target
square-distinctness guards.  Therefore all 23 deployed fibers contain no
admissible `DE+/DE-/BE` realization, and hence no packet in this cell and sign
row.

This leaves 46 values in the exceptional router.  It does not treat those
values, another sign row or matching cell, delete cell 5 or `433-1a -> O0b`,
close K3, a Prize row, or either Prize result.

## Falsifier

An omitted finite subfactor, a surviving base-field gcd root satisfying all
printed target guards, a non-linear primitive factor containing an
`F_p`-valued primitive coordinate, or an admissible packet at one of the 23
listed values.
