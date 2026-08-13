# Proof

For the prefix `h<=h0`, use the independently truncated full-lift
punctured Johnson/mean-centered profile.

Fix one exact layer `h0<h<=H`.  Every assigned explanation owns at most one
slope because `2h>e`.  Choose an inside agreement `h`-set for each member
and fix an anchor.  The normalized codeword direction from every other
member to the anchor agrees with the gauged direction on at least
`A_h=2h-e` coordinates.  It is nonzero, because the gauged direction is
pointwise nonzero on its support.  Distinct directions have intrinsic
agreement sets meeting in at most `c=K-1` coordinates.  The constant-block
Johnson count therefore permits at most `J_h` direction classes.

Each class and the anchor form one nonzero affine codeword line.  Every
member has exactly `m-h` outside agreements.  Its outside common core lies
in the zero set of the line direction and has size at most `c`.  The stated
guards make the packing ratio increase with core size, so the line has at
most `Q_h` members.  Subtracting the repeated anchor gives

```text
|D_h|<=1+J_h(Q_h-1)=D_h.
```

Summing the disjoint prefix and exact boundary layers leaves only the
cross-layer synchronized top line and proves `(BS1)`.

Suppose `(BS1)` does not pay directly and the whole family is unsafe.  Then
the top line has at least `L_e=B-F_e+1` members.  Total-core line packing
forces the printed `g_e`.  Its nonzero degree-`<K` direction has at most `c`
zeros outside the gauged direction support, so at least `u_e=g_e-c` common
core coordinates lie inside that support.

Any assigned explanation of deficit `h>=a_e=e-u_e+K` has an inside
agreement set meeting this inside common core in at least `K` coordinates.
Two top anchors and restriction injectivity put that explanation at its
actual slope parameter on the same affine line.  Thus every such slope is
charged once by `N-m+1`.

Every remaining explanation has deficit at most `a_e-1`, hence outside
agreement at least `m-a_e+1`.  The punctured ordinary Johnson theorem gives
at most `M_e` such explanations, and the crude owner cap `e` gives `(BS2)`.

The exact official scan checks every guard and integer in
`98232<=e<=101156`.  Supports through `101149` satisfy the direct branch;
the final six satisfy the absorption branch.  At `e=101156`, `F_e>B`, so
this fixed-cutoff proof correctly stops without asserting unsafety.
