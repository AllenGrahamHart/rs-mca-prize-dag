# Proof

Fix an independent `(c-1)`-set `A` obtained by deleting one point from a
support-`c` circuit.  Independence gives

```text
H_A={f in V:f|_A=0},       dim H_A=11-c.                  (1)
```

Every completion of `A` is a common zero of `H_A`.  If there are `b`
completions, all polynomials in `H_A` vanish on the `c-1+b` points formed by
`A` and those completions.  Dividing by their locator embeds `H_A` into
`P_(K-c+1-b)`.  Therefore

```text
11-c<=K-c+1-b,
b<=K-10=q.                                                (2)
```

The completion labels have private nonzero coordinates at their respective
completion points.  Any two are linearly independent.  A selected
eleven-set has evaluation rank ten, so annihilator duality says that the
annihilator labels supported on it form a line.  It therefore contains at
most one of the `b` completions.

For fixed `A`, choose that one completion in `b` ways and the remaining
`11-c` coordinates outside `A` and all completion points in

```text
C(m-c+1-b,11-c)
```

ways.  Sum over at most `C(m,c-1)` deletions.  Every selected support-`c`
circuit is counted exactly `c` times, once for each deleted circuit point.
Divide by `c`, maximize over the integer interval `0<=b<=q`, and take the
integer floor.  This proves `(UC2)`.
