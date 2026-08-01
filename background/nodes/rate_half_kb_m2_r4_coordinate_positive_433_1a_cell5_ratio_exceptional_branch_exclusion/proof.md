# Proof

The parent proves that `c=bx`, division by the unit `b^2`, and collection in
`b` preserve the guarded cell-5 common ideal.  It also proves that the
complement of `a1!=0` is exactly `(KBREB-1)`; no generic denominator branch
is omitted.

The certificate compiler reconstructs `a0,a1,L1,L2` directly from the parent
Vieta minors.  It atomically translates every common and target guard under
`c=bx`, giving the 22 factors `(KBREB-2)`.  Adjoining
`z*product(KBREB-2)-1` is the standard exact saturation encoding: its
projection consists precisely of solutions on which every guard is nonzero.

Singular computes the standard basis in
`F_2130706433[b,x,r,t,z]`.  The sealed output is

```text
dim=-1, size=1, vdim=0, basis={1}.
```

Thus the saturated ideal is the unit ideal and has no algebraic-closure
point.  The parent branch cover then leaves only `a1!=0`. QED.
