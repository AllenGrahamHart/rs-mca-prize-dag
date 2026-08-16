# Adjacent-flat circuit coupling

- **status:** PROVED
- **scope:** finite matroids; representability is not required

Let `M` be a finite matroid on `N` labelled elements.  Fix `r>=1` and
`B>=r`, with `N>=B`.  Assume every rank-`r` flat has at most `B` elements
and every rank-`(r+1)` flat has at most `B+1` elements.  If `C_j` is the
number of `j`-element circuit supports, then

```text
(r+2) C_(r+2)
 <= (B-r) C(N,r+1) - (N-B) C_(r+1).               (AFC)
```

The rank-three instance is the existing support-4/5 coupling.  The
rank-four instance couples support five to support six.

## Falsifier

A finite matroid satisfying both flat-size hypotheses whose adjacent
circuit census violates `(AFC)`.
