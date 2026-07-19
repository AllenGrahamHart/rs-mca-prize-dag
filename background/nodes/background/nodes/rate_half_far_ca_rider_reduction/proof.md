# Proof

Let `B` be the CA-bad slope set. If `|B|<=1`, `(RR1)` is immediate. Fix an
anchor slope `gamma_0` with witness codeword `c_0` and agreement set `S_0` of
size at least `n-r`.

For every other bad slope `gamma`, choose `c_gamma,S_gamma`. On the
intersection `S_0 intersect S_gamma`, of size at least `n-2r`, the two line
equations solve to a code pair

```text
P_2=(c_0-c_gamma)/(gamma_0-gamma),
P_1=c_0-gamma_0 P_2.
```

Hence each non-anchor slope rides a member of the pair list at agreement
`n-2r`.

Fix one such pair `P=(P_1,P_2)` and let `E` be its column disagreement set
against the received pair. Column farness gives `|E|>=r+1`. A rider slope is
close on all but at most `r` coordinates, so on at least `|E|-r` points of
`E` it solves one nonzero affine equation

```text
(f_1-P_1)(j)+gamma(f_2-P_2)(j)=0.
```

Each coordinate admits at most one slope. Double counting rider-coordinate
incidences gives

```text
#riders(P)(|E|-r)<=|E|,
```

and `|E|/(|E|-r)<=r+1`. Summing over the pair list and adding the anchor proves
`(RR1)--(RR2)`.

Every rider pair agrees with the received pair on at least `n-2r` columns, so
each received component is within `2r` of its corresponding codeword. CA-bad
sets are invariant under translation by `C^2`, proving the doubly sparse
normalization. Finally, at rate one half,

```text
n-2r=n-2(n-a)=2a-n=2tau,
```

which proves `(RR3)--(RR4)`. QED.
