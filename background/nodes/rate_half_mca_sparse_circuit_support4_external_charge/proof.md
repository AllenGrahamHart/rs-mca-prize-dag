# Proof

Retain the notation of the joint zero-carrier theorem.  First suppose
`delta=0`.  Then `Lambda intersect E_B=Lambda`, so every support-four label
has a representation on `B`.  Comparing it with its circuit representation
uses at most

```text
|B|+4=K-t+4<=K
```

evaluation functionals.  Vandermonde independence forces the circuit
support into `B`.  This gives the first line of `(EC1)`.

Now suppose `delta>0`.  Circuits contained in `B` contribute at most
`C(b,4)`.  Fix `1<=j<=4` and consider a circuit `D` with exactly `j` points
outside `B`.  Delete one of those outside points.  The remaining independent
three-set `A` has `j-1` points outside `B`.  The joint zero-carrier theorem
says that `A` together with all its completions has at most `delta+3` points
outside `B`.  Hence `A` has at most

```text
delta+3-(j-1)=delta+4-j                         (1)
```

outside completion points.

There are at most

```text
C(b,4-j) C(N,j-1)                               (2)
```

possible three-sets `A` of this shape.  Every circuit `D` in the stratum is
charged exactly `j` times, once for each choice of its deleted outside point.
Multiplying (1) and (2), dividing by `j`, and taking the integer floor gives
the `j`-th summand of `(EC1)`.  Summing the disjoint values of `j` and the
inside stratum proves the support count.

Every support-four circuit extends to at most `C(m-4,7)` eleven-sets, proving
`(EC2)`.  The joint theorem restricts `t,delta` to `(EC3)`, so maximizing
over that finite rectangle is branch-safe.  Direct exact evaluation gives
the five printed `K'=45` caps.  QED.
