# Proof

Away from the norm denominators and registered construction guards, a zero
of a colored cut forces its field norm numerator to vanish.  At a pole or
construction boundary the norm argument is not used, so those roots are
included explicitly.  Thus every possible exception lies over the union of
the base-field roots of the eight numerators, eight denominators, and the
four guards repeated in each case row.

Exact `gcd(P(q),q^p-q)` computations give 136 incidences but only eight
distinct `q` values.  Three annihilate the genus-two projection denominator.
At each remaining value, exact quadratic root extraction for

```text
y^2=(q^3+2q^2+q+4)/(q^3+6q^2+q)
```

is exhaustive.  Two values have no `F_p` root.  At the final three values,
every root makes a Mobius denominator or one of
`b c (b^2-1)(c^2-1)(b-c)(b+c)` vanish.  Therefore no candidate reaches the
guarded common locus, before an `r` choice is even possible.

The primary verifier independently recomputes every `F_p` root set using
pure-Python polynomial gcd arithmetic, rebuilds the eight-value incidence
union, and replays all `y,b,c` boundary classifications.  Hence no guarded
point satisfies either necessary cut, and all 240 formal systems are empty.
QED.
