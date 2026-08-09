# Proof

Fix one of the four signed source rows and one endpoint role. The global
common-kernel theorem writes the missing record and endpoint record on the
exact guarded cell-11 common curve. The complete-fiber Vieta identities
imply the necessary source compatibility equation

```text
(x^2 A(lambda) + B(lambda))^2
    = lambda beta(lambda)^2 x^2,
```

where `x=b` for `xi=5`, `x=c` for `xi=6`, and `lambda=-t^2`.
Thus any admissible endpoint witness lies in the common ideal augmented by
this cut and the deployed nonzero/distinctness guard.

Exact Singular elimination of `z,t,c,b` leaves one monic degree-32
polynomial in `r` for each sign/endpoint case. An independent Galois-tools
calculation computes

```text
gcd(E(r), r^p-r)
```

and obtains a monic linear polynomial in every row. The recovered roots
agree exactly with a separate finite-field factorization replay.

At each of the eight roots, the quadratic base relation has two deployed
`t` roots. One `t` fiber has an irreducible quadratic `b` relation and
therefore no deployed lift. The other has exactly two guarded `b` lifts;
linear recovery gives `c`, and direct substitution shows that the source
compatibility equation is nonzero at both. Thus all 16 deployed common
points above the eliminant roots are incompatible. The parent theorem
proves that the leading-boundary complement has no deployed point.

No endpoint source candidate exists. The conclusion precedes residual
matching, so it excludes all 15 pairings for each endpoint, totaling 30
labels. QED.
