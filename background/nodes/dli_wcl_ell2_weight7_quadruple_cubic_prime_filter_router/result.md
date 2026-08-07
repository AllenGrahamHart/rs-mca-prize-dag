# Result

The inherited `(2,7)` recursive-norm route is now proof-grade and its prior
saturation gap is repaired:

```text
candidate obstruction: gcd(Norm(F),Norm(G));
all prime factors:      apply H_p/gcd(H_p,u) and reconstruct;
Norm(u)-shared factors: never delete before that embedding-aware test;
route size:             94,652,815 affine candidate orbits.
```

This removes the need for a separate weight-four norm census merely to make
saturation sound. It does not make the full route affordable. The next
useful `(2,7)` theorem must batch the free complement product, shrink the
401,712 selected-quadruple shapes, or replace per-orbit norms by a genuinely
joint obstruction. Repeating sampled rows or launching the complete census
has lower proof value and is not authorized.
