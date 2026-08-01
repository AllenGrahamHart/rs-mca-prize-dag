# Proof

Expanding the product and squared-sum equations of the signed outside-Vieta
atlas gives `(KBP3E-2)` and `(KBP3E-3)` directly.

Assume `A!=0`.  Modulo `P`, the powers of `w` satisfy

```text
w^2=(-Bw-C)/A,
w^3=((B^2-AC)w+BC)/A^2,
w^4=((-B^3+2ABC)w-B^2C+AC^2)/A^3.               (1)
```

Therefore the pseudo-remainder of `A^3Q` by `P` is `R_1w+R_0`.  At either
root of `P`, `Q=0` is equivalent to this linear remainder vanishing.
Taking the norm from the quadratic algebra gives

```text
A R_0^2-B R_0R_1+C R_1^2.                        (2)
```

The standard root formula for the resultant shows that `(2)` is exactly
`A^3 Res(P,Q)`, proving `(KBP3E-4)`.

If `A=0` and `B!=0`, the only finite root of `P` is `-C/B`.  Multiplying
`Q(-C/B)` by `B^4` gives `(KBP3E-5)`.  If `A=B=0`, then
`p=-a_infinity^2` and

```text
C=-(a_0^2-a_infinity^2)d_0.                      (3)
```

The loop target pairs are distinct and `D(0)=d_0!=0`, so `(3)` is nonzero;
the constant product equation has no root.

These arguments concern polynomial common roots.  A common root at one of
the five common labels or at a zero of `D` is not an outside Vieta edge, so
the parent saturation remains necessary.  The exact checker verifies the
pseudo-remainder, resultant identity, degree-drop evaluation, and the
specialized coefficients over the integer polynomial ring. QED.
