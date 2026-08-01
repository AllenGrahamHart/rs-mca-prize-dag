# Proof

The complete-fiber compiler gives `(KBN0W-1)`.  With no loop locator, the
loop-stratified compiler writes `A_1=C` with `deg C<=2`; its five sum rows are

```text
C(s)+q_sD(s)=0.                                         (1)
```

Hence `v_s=-C(s)` is the restriction of a quadratic polynomial to `K`, and
the rank assertion follows.

Conversely, choose three labels.  Their distinct first coordinates determine
a unique polynomial `C` of degree at most two with `C(s)=-v_s` on those
labels.  The two remaining `4 x 4` determinants say exactly that their rows
lie in the same three-dimensional evaluation graph, so `C(s)=-v_s` there as
well.  Equation `(1)` is therefore recovered on all five fibers.  Rescaling
the projective kernel rescales `C` and does not affect this equivalence. QED.
