# Proof

Let `A` be the independent source deletion.  Its `q-s` completion labels
have private nonzero coordinates, so they are linearly independent.  They
span a subspace `Lambda_0` of dimension `q-s` on

```text
U=A union {completions},       |U|=q+c-1-s.         (1)
```

Let `W_d` be the span of every support-`d` circuit label.  Since the full
annihilator has dimension `q`, choose at most `s` support-`d` labels whose
images span `(W_d+Lambda_0)/Lambda_0`.  Adjoining their supports to `U`
gives a carrier `B` with

```text
|B|<=q+c-1-s+sd=q+c-1+s(d-1).                     (2)
```

Every support-`d` label has a representation on `B` and its minimal circuit
representation on its own support `D`.  The union of the two
representations has size at most

```text
q+c-1+s(d-1)+d.
```

Condition `(XC1)` says that this is at most `q+10=K`.  Evaluation
functionals at at most `K` distinct points are Vandermonde independent.
The two representations must therefore agree coordinate by coordinate,
which forces `D subset B`.

There are at most `C(|B|,d)` circuit supports in `B`, and each extends to at
most `C(m-d,11-d)` selected eleven-sets.  This proves `(XC3)`.  Substituting
`c=5` in `(XC1)` gives the five displayed target sets.  QED.
