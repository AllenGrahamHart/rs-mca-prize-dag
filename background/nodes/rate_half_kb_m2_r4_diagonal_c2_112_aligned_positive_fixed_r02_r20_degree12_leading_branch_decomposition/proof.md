# Proof

The pinned branch constructor rebuilds the literal `F04-R02` and `F04-R20`
systems and selects the common degree-12 resultant factor together with the
two essential post-reconstruction rows. Exact coefficient extraction in
`x` gives degrees `6,36,35`. Factoring the three leading coefficients over
`QQ[s,p]` gives the census in the statement; every factor is compared with
the complete transported named-unit key set and is nonnamed.

For the `R02` prefix, each step uses

```text
lc_x(B) A - lc_x(A) x^(deg_x(A)-deg_x(B)) B.
```

The leading term cancels exactly. The coefficient content in `QQ[s,p]` is
removed only by checked exact division. The first two contents are one; the
third is the printed degree-23 factor. The resulting hashes, degrees, and
term counts are bound by the verifier.

The function-field run is retained only as a fence: it converts the exact
degrees but times out during the first remainder. It supplies no theorem.

The two large-curve runs impose the printed irreducible degree-22 and
degree-23 leading factors before any full intersection. Their exact seed
bases and reduced-row metrics are complete, but both final Gröbner calls hit
the 780-second cap. A second implementation pseudo-divides both rows by the
degree-12 factor in `x`, reducing every coefficient modulo the degree-22
curve after each cancellation. All 60 exact cancellations complete and
give the terminal metrics in the statement; only the final intersection
times out. These bounded execution facts are the additional proved route
cuts. They supply no emptiness theorem.
QED.
