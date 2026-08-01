# Refutation proof

The identities `(KBP3N-R2)` follow by multiplying `H(r,X)` at the two
lifts `X,-X` over a root of `E` or `D`; the symbolic checker still verifies
them exactly.  They concern ordinary polynomial resultants.

For the displayed `F_13` fixture, loop interpolation gives

```text
D(W)=4+7W+6W^2,       E(W)=9+5W+2W^2,
B(W)=W-1.
```

At `(x,p,s)=(2,2,3)` and `(3,3,4)`, direct substitution gives

```text
E(x^2)=pD(x^2),       xB(x^2)+sD(x^2)=0,
```

and similarly at `y`; `D` is nonzero on the four guarded common values.
Evaluating the exact resultants in `(KBP3N-R1)` gives `(KBP3N-R4)`, so the
ordinary norm at `U=1` is `8`.

The signed 433 root-low incidence graph has two divisor copies of the
ramified antipodal edge at target `1`, together with neighbors `b,c`; its
printed product is `bc=6`.  These values differ in `F_13`.  The former
proof's sentence equating roots of `H(r,X)` with the divisor-weighted graph
multiset was therefore invalid at ramification. QED (refutation).
