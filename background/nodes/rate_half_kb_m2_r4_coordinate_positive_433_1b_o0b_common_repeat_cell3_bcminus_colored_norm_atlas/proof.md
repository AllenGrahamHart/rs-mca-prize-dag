# Proof

The compact-locus parent makes the five common product rows rank five on the
guarded locus.  Their signed maximal cofactors therefore span the unique
six-entry product kernel.  The same polynomial scale and loop pivot used in
the compact certificate recover `A`, `B`, and `beta` without division.

The two equations for a missing colored record are

```text
bm-k z am=0,
-r^4 betam^2-(k+z)^2 am^2=0.
```

Eliminating `z` gives `(CM-1)` in `statement.md`; the identity remains
necessary at `am=0` because no division by `am` is used.

The tower parent identifies the guarded common function field with two
successive quadratic extensions of `F_p(q)`.  The launcher implements these
extensions by explicit two-coordinate arithmetic, checks both defining
relations, computes `(CM-1)`, and takes the norm first in `r` and then in
`y`.  Its rational-function layer reduces every fraction and registers the
numerator of every inverted element.  The resulting eight coefficient rows
and four construction guards are exact.  QED.
