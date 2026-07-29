# Proof - L1 Mersenne HNF m=8 order-one cubic three-two-one role weld

Equation (TQC7) is `R=(lambda-1)S`. Since `S=B!=0`, it is equivalent to
(TRW2). Write `t=R/S`. Direct substitution into (RFC1) gives

```text
A(lambda)=(1+t)^2-(1+t)+1
         =(S^2+RS+R^2)/S^2=A_0/S^2,

B(lambda)=(2+t)(1+2t)(t-1)
         =(2S+R)(S+2R)(R-S)/S^3=B_0/S^3.          (1)
```

The first role factor in (RFC2) has common denominator `S^6`; its numerator
under (1) is the first line of (TRW4). Each remaining factor has common
denominator `S^12`; its numerator is the corresponding remaining line of
(TRW4). Because `S!=0`, this clearing is reversible. The inherited
`R!=0` is exactly `lambda!=1` together with `S!=0`.

Equations (TQC3) and (TQC6) express `a,g_2,B,u,v,g_3` through
`(g_1,y,r,d)`, so (TRW1)--(TRW4) add no variable. Conversely, a solution
of one welded packet reconstructs `lambda=1+R/S`, satisfies the matching
factor in (RFC2), and recovers (TQC7). The weld is therefore equivalent to
the four-factor common-quadratic role split on the listed saturations. QED.
