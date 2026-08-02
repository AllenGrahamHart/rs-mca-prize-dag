# KoalaBear positive 433-1a cell-5 reciprocal trace quadratic

Let `p=2130706433` and `i=16711679`, so `i^2=-1` in `F_p`.  In cell 5,
sign row `(-1,-1)`, let `I_sat` be the three-minor common ideal saturated by
the printed source-label and common-chart guards.  Its projection to
`F_p[b,t]` is principal:

```text
I_sat intersect F_p[b,t] = <P(b,t)>,                         (KBRT-1)

P = A0(t)(b^4+1) + A1(t)(b^3+b) + A2(t)b^2,
A0 = t^4-2i t^3-4i t^2-2i t-1,
A1 = -8i(t^4+1),
A2 = -2t^4+4i t^3-24i t^2+4i t+2.                          (KBRT-2)
```

The generator has total degree eight and 19 terms.  It is reciprocal in
`b`.  Since the common guards include `b!=0`, put `u=b+b^{-1}`.  Then

```text
P(b,t) = b^2 Q(u,t),
Q(u,t) = A0 u^2 + A1 u + A2-2A0.                            (KBRT-3)
```

The trace-quadratic discriminant factors exactly as

```text
disc_u(Q) = -48(t-i)^2(t+i)^4(t^2-(2i/3)t-1).               (KBRT-4)
```

Thus the guarded common projection descends to one quadratic trace equation;
after removing the already-forbidden `t=+-i` factors, its square class is
controlled by `-48(t^2-(2i/3)t-1)`.

This does not reconstruct `r,c`, classify the signed pair, impose the colored
edge, delete cell 5 or `433-1a -> O0b`, close K3, or prove either Prize result.
