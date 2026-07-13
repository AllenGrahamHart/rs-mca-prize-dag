# Local-envelope route limit

This audit asks whether repeatedly combining the cogirth charge with the
minimum-basis collision-line chart can pay another high-core selector rank.
It does not change either theorem.

Put `a=s-1`, let `b` be the minimum number of core bases on a collision
line, and write

```text
N_b=min(n,R+b+a-1),
D=C(h+a,a),
L=floor(R/h).
```

The two proved bounds give the pointwise envelope

```text
E_s(b)=min(
  floor(C(N_b,a)(N_b-a)/D),
  L floor(C(N_b,a)/b)
).
```

This envelope can be maximized without scanning the potentially enormous
range `1<=b<=C(k,a)`.  Before chart saturation, the cogirth term is
nondecreasing, while

```text
C(R+b+a-1,a)/b
```

decreases until `(a-1)b<=R` ceases to hold and then increases.  After chart
saturation, the cogirth term is constant and the line term is nonincreasing.
The two unfloored terms cross when

```text
b(R+b-1)=L D.
```

Consequently an exact integer maximum is attained at `b=1`, at chart
saturation, or at one of the two integers neighboring that crossover.  The
verifier evaluates those points, together with the harmless terminal
endpoint, using integer floors throughout.

Modal app `ap-3SsE1JL5IiiOkotzT89CcR` returned

```text
rowc-r1_4:  local_PA_s<=4
rowc-r1_8:  local_PA_s<=4
rowc-r1_16: local_PA_s<=4
prize-r1_4: local_PA_s<=11
prize-r1_8: local_PA_s<=11
prize-r1_16:local_PA_s<=10
```

These are exactly the already-paid ranges after the existing rank-four
handoff.  Thus minimum-basis self-localization plus the present cogirth and
line charges cannot by itself close another official P-A rank.  Any further
XR increment must add structural information, not another iteration of this
arithmetic envelope.


[w6 audit 2026-07-13: the paid ranges quoted here inherit catch #158 -- at RowC 1/16 the rank-4 handoff is conditional (line-admitting b <= 47 or line-covered hulls); the line-free/line-uncovered rank-4 sub-case remains open and is not fenced by this envelope, which presupposes the covering step; the rank-five kill is unconditional on the covered branch.]
