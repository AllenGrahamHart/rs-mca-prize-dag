# KoalaBear m2 r2 residual dihedral star-graph rigidity

- **status:** PROVED
- **scope:** the surviving `n=3,6` factor cases inside the actual
  `(m,r,delta)=(2,2,4)` row
- **dependencies:**
  `rate_half_kb_m2_r2_dihedral_degree2_source_star_exclusion` and the
  full-V4 source-cover conjugation law
- **consumer:** `rate_half_band_closure`

For one generic pole of the outer map, the regular `D_n` incidence between
the `n` quotient values in each endpoint coordinate is the bipartite cycle
`C_(2n)`. Each `Z` value therefore sees a distinct unordered pair of
adjacent `Y` values.

Let `w,tau(w)` be the two endpoint labels over one such `Z` value. If one
point of `D_w=psi^*[w]` has star `{t,s}`, then the full-V4 source action

```text
c eta c^(-1)=eta*a,       a:(T,X)->(tau(T),b(X))
```

forces the two stars over `D_(tau(w))` to be

```text
{t,tau(s)} and {tau(t),s}.
```

Together the two endpoint lifts use every edge of the cross graph
`K_(2,2)` exactly once. Distinct `Z` values have distinct adjacent
`Y`-pairs for `n>=3`, and distinct outer poles have disjoint quotient
fibers. Since the selected pole fibers contain all six poles of `F`, the
complete source-star graph is therefore exact:

```text
n=3: two disjoint copies of K_(2,2,2);
n=6: the two-point blow-up of C_6.
```

All 24 roots of the complete source divisor are simple, all 24 star
vertices have weight one, the defect is zero, and every one of the twelve
source labels has degree four. Thus the quartic defect gate cannot delete
either residual profile.

This theorem does not construct either profile. It closes no `m=2` type,
owner, payment, `u=2`, endpoint, adjacent certificate, or Prize row.

## Falsifier

A generic `D_n` incidence outside `C_(2n)`, a source lift not exchanging
the two cross-edge orientations as printed, a repeated star in `n=3,6`,
or a source label of degree other than four.
