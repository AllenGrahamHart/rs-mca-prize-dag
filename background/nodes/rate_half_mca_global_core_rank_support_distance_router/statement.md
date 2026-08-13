# Global-core rank/support replacement target

- **status:** TARGET
- **regression:** the former rank and common-zero payments are retracted
- **surviving suppliers:** gauge equivalence, sparse-direction puncturing,
  direction-distance, repaired recursive shortening, and the corrected
  proper-subspace occupancy compiler

After whole-line global-core cancellation, write

```text
(N,K,m)=(R+s,s,d+s),       e=d_U(y_1)=R-j.
```

The exact counterexample
`rate_half_mca_affine_span_incidence_counterexample` refutes the incidence
denominator used by the former gauge-rank and common-zero gates.  Therefore
none of the old transformed-rank walls or middle-support prefixes is a
proved payment.

The corrected pair-noncontained occupancy theorem now pays the following
affine-rank cells at the first residual dimensions:

```text
KoalaBear s=14:
  q<=9: all e;
  q=10: e<=5 or e>=981108;
  q=11: e<=5 or e>=981153;
  q=12: e<=5 or e>=981861;
  q=13: e<=5 or e>=992852;
  q=14, lifted rank h=14: e<=5 or e>=992852;
  q=14, lifted rank h=15: e<=5 or e>=1044239.

Mersenne s=6:
  q=1: all e;
  q=2: e<=1 or e>=981144;
  q=3: e<=1 or e>=981363;
  q=4: e<=1 or e>=984779;
  q=5: e<=1 or e>=1037876;
  q=6, lifted rank h=6: e<=1 or e>=1037876;
  q=6, lifted rank h=7: e<=1 or e>=1044242.
```

Here `q` is the affine rank of the selected explanations and `h` is the
affine rank of the lifted pairs `(gamma,c_gamma)`, equivalently the error
affine rank.  The full-explanation lifted-rank dichotomy proves that these
are the only top-rank branches.  In the `h=q` branch a codeword gauge drops
the explanation rank to `q-1`, giving the improved occupancy suffix; in the
`h=q+1` branch no gauge drops rank.  The top-rank low prefixes and full-lift
suffixes still come from the independent sparse and recursive suppliers:

```text
KoalaBear at s=14:  e<=5 by punctured-list payment,
                    e>=1044239 by repaired direction recursion.
Mersenne at s=6:    e<=1 by punctured-list payment,
                    e>=1044242 by repaired direction recursion.
```

The full-lift branch now has an exact code-theoretic form.  With

```text
W=C+span{r_1},
```

the selected errors are a full-affine-rank sparse list in one affine coset
of the `[N,K+1]` code `W`, with unit slope fibers.  Its generalized weights
are

```text
d_1(W)=e,       d_j(W)=N-K+j-1 for 2<=j<=K+1.
```

Thus every higher generalized weight is already MDS-sharp.  Even at the
best endpoint `e=N-K`, the resulting generic affine-list ceiling is
`743896698428332665` on KoalaBear and `219426634` on Mersenne, both above
budget.

At later dimensions the repaired high-support suffix is exactly the one
defined by `rate_half_mca_direction_mismatch_recursive_shortening`; the
sparse-direction theorem must be evaluated at its own exact row.

## Target

Pay the displayed residual support intervals, especially the full-lift
top-rank cells, without reusing the refuted ordered-basis denominator.  For
the full-lift branch this now means exploiting structure of the
codimension-one RS extension beyond its generalized-weight hierarchy.  Any
further replacement must continue to distinguish:

1. local incident full rank;
2. multiplicity in each proper normal subspace; and
3. exact first-match ownership on the whole received line.

## Nonclaims

The historical rank/support products remain arithmetic records only.  This
node does not currently pay the displayed middle intervals, close a deployed
row, or close either prize.

## Falsifier

Any proposed replacement is killed by a legal family exceeding it, or by a
proper normal subspace whose occupancy exceeds the theorem's stated cap.
