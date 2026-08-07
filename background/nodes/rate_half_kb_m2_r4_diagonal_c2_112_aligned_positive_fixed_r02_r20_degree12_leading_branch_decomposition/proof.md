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
QED.
