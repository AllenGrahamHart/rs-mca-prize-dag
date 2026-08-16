# Rank-five flat-circuit coupling

- **status:** PROVED
- **scope:** finite matroids; representability is not required

Let `M` be a finite matroid on `N` labelled elements.  Let `B>=3` and
`N>=B`.  Assume every rank-three flat has at most `B` elements and every
rank-four flat has at most `B+1` elements.  If `C_4` and `C_5` denote the
numbers of four-element and five-element circuit supports, then

```text
5 C_5 <= (B-3) C(N,4) - (N-B) C_4.                 (FC)
```

The negative term is a genuine cross-support charge.  A rich rank-three
flat creates support-four circuits, but every independent four-set made from
three points of that flat and one outside point loses support-five
completions.

## Falsifier

A finite matroid satisfying the two flat-size hypotheses whose circuit
census violates `(FC)`.
