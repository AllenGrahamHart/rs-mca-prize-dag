# Proof

The statement of `dli_dyadic_k_core` defines `W_cl` by summing `2N*2^-w(O)`
over every reduced primitive orbit in the window. Its attack contract likewise
requires the complete primitive ledger. This is the quantity occurring on the
right side of C1'.

The later lattice reframe in `PRO_DLI_CLOSE_6.md` makes the same point
explicit: multiplier shadows, additive clusters, and lifts are all lattice
points and are priced at their own weights; no independence convention is
used. Being generated from another orbit is not the same as being imprimitive
under proper signed-subvector deletion. Therefore an ownership quotient can
organize a census but cannot replace the raw weighted sum in C1'.

Formally, if `W_owner` retains only one member of each ownership class, then
`W_owner<=W_raw`. The reverse inequality needed to substitute
`W_owner<=1/32` into C1' has no stated premise. At `ell=16`, nine primitive
orbits of weight 21 in one ownership class give the abstract ledger values

```text
W_owner = 1/256 <= 1/32,
W_raw   = 9/256 > 1/32.
```

This is an interface countermodel, not a claim that this class is realizable
on an official row. It proves that deletion alone supplies no valid
implication.

For an actual level `ell`, the smallest possible nonzero raw contribution in
the window occurs at weight `ell+5` and equals

```text
2*(256 ell)*2^(-(ell+5)) = 16 ell / 2^ell.
```

This exceeds `1/32` for `ell=1,2,4,8`. Hence on precisely those low levels the
zone bound is equivalent to raw-ledger emptiness, which is invariant under an
ownership partition that retains at least one representative. At `ell=16`
the minimum is `1/256`, so weighted multiplicities can no longer be discarded.
