# Proof

Fix source signs and a target lane. On the proved cell-11 four-basis tower,
canonical matching `12` gives

```text
P_u(u)=Pair(-de,u),        P_f(f)=Pair(de,sigma_c*c*f),
```

where `u=df`, and both cuts are quadratic. Since `d=u/f` and
`e=de*f/u`, the deleted positive-`DE` squared-sum equation gives

```text
R(u,f)=(u^2+de*f^2)^2-S*f^2*u^2=0.                (RS12-DE12)
```

The pinned compiler uses the division-free degree-eight construction,
pseudo-reduces modulo `P_f`, and norms the necessary cut through
`1,t,b,bt`, retaining all leading-coefficient drops.

The adapter runs all 16 source-sign/target-lane rows. Its complete root union
has 200 case-labeled candidates and lifts to 160 guarded source points. Of
256 Cartesian `(u,f)` rows, 224 fail (RS12-DE12). The other 32
reconstruct `d,e,v` and have a nonzero final cut
`Pair(sigma_o*v,b*f)`. No zero-`f` survivor, colored solution, witness,
or unresolved branch occurs.

An external compiled Frobenius/gcd pass reconstructs all 114 roots of the 33
unique polynomial profiles and certifies that each squarefree root-part
degree equals its printed root count. The independent audit validates each
profile, validates all 32 leading-boundary payments against the exact tower,
and directly replays all 256 `(u,f)` rows.

Exact exchange of the identical positive `DE` copies supplies `xi=1`,
and the generic matching transport supplies pairing `13`, giving the orbit
printed in the statement. QED.
