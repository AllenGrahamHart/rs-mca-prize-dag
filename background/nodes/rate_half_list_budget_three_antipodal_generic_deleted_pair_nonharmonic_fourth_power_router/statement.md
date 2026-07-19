# Budget-three antipodal generic deleted-pair nonharmonic fourth-power router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_nonharmonic_scalar_router`

Retain the complete official nonharmonic scalar-router data and put

```text
chi=r+r^(-1).                                         (NFR1)
```

The source torsion gives `chi notin {0,2,-2}` and, under the trace recurrence
`chi_(m+1)=chi_m^2-2`, gives `chi_40=2`. For the three pairings define

```text
h_0=1/(2(chi-1)),
h_1=(chi-2)/(2(chi+2)),
h_2=chi/(2(chi-4)),                                  (NFR2)

y_0=4(chi-1)^2-2,
y_1=4(chi+2)^2/(chi-2)^2-2,
y_2=4(chi-4)^2/chi^2-2.                              (NFR3)
```

Every denominator used by an admitted branch is nonzero. With the Euclidean
data `R=AS+T` from `(NSR2)`, the complete deleted-pair square pencil exists
if and only if at least one `j in {0,1,2}` passes

```text
deg S=2M-2,       T=(h_jS)^2,                        (NFR4)
y_(j,0)=y_j notin {2,-2},
y_(j,m+1)=y_(j,m)^2-2,       y_(j,38)=2,             (NFR5)
T=W^4 for a nonzero polynomial W of degree M-1.       (NFR6)
```

Equivalently the three scalar identities in `(NFR4)` can be checked without
division as

```text
4(chi-1)^2T=S^2,
4(chi+2)^2T=(chi-2)^2S^2,
4(chi-4)^2T=chi^2S^2.                                (NFR7)
```

Thus neither an outer ratio, a root of its reciprocal quadratic, nor a
root-dependent polynomial-square test remains. The live deleted-pair task is
uniform rejection of three trace-indexed exact fourth-power identities.

This theorem does not prove that `(NFR4)--(NFR6)` reject uniformly, and it
does not provide a compressed representation of the official-degree
Euclidean quotient and remainder.
