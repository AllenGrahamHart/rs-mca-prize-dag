# Proof

After rank-`(10-d)` shortening, the unshortened chart has code dimension
`K'-10+d`.  Deleting `z` zero normals leaves

```text
n_z=R+d+t,       m_z=w+d+t,       t=K'-10-z.
```

At `t=0` the chart is complete.  The projective-paving cap theorem gives
`P_d`.  For `t>=1`, retain the pointwise count in the proof of support-local
transversality before its endpoint maximization.  With automatic margin
one it gives `F_d(t)`.

The successive ratio has sign

```text
F_d(t+1)/F_d(t)-1
  has sign d*t+(d+1)(w+d)-R.
```

That affine expression increases with `t`, so `F_d` first decreases and
then increases.  Its maximum on the integer interval
`1<=t<=K'-10` is therefore at `t=1` or `t=K'-10`.  Combining those two
charts with the separately sharpened `t=0` chart proves `(IG)`.

For `d=1`, delete the zero normals.  The incident rank-two matroid has no
loops and has full rank, so its `w+1+t` elements occupy at least two
parallel classes.  It owns at least `2(w+t)` ordered independent pairs and
hence has record bound

```text
G(t)=(R+1+t)_fall_2/(2(w+t)).
```

The sign of `G(t+1)/G(t)-1` is the sign of `t+2w-R`, so `G` also has one
turn and is maximized at an endpoint.  Exact cross multiplication at the
largest official value `t=R-10` gives `G(0)>G(R-10)`.  Thus the complete
cap `floor(G(0))=8147918` is uniform in corank one.

Direct exact evaluation of `(IG)` at `K'=377674` gives the two printed
values.  A larger valid upper bound does not prove that either complete cap
is false; it proves that the uniform promotion is not supplied by these
parents.
