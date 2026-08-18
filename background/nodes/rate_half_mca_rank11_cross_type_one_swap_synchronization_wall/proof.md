# Proof

Records have one first-owned pair type, so the record sets belonging to
different types are disjoint. If a 32-record packet contained at least `a`
records from each of two types, it would contain at least `2a` records. For
`a>=17`, this exceeds 32. Thus the anchor type is unique.

Let `P` and `Q` be packets anchored at different types `p` and `q`. Write
`P_p,P_q,Q_p,Q_q` for their corresponding record subsets. At least `a`
records of `P` belong to `p`, while at most `32-a` records of `Q` can belong
to `p`; hence

```text
|P_p intersection Q_p|<=32-a.
```

The symmetric bound holds for type `q`. Records of all other types can be
common to both packets, but each such common record consumes one slot in both
packets and reduces by one the slots available for each of the two cross-type
intersections. More explicitly, if `t` common records have types other than
`p,q`, then

```text
|P intersection Q|<=t+2(32-a-t)=64-2a-t<=64-2a.      (1)
```

This bound is sharp at the set-system level: take `a` records of `p` and
`32-a` of `q` in `P`, reverse the counts in `Q`, and share every minority
record. Substitution gives 28 for `a=18` and 24 for `a=20`.

Packets sharing 31 records are adjacent by one swap. Since `31>28`, no such
edge joins packets with different 18-anchors; a fortiori it cannot join
different 20-anchors. Anchor type is therefore constant on every connected
component of the one-swap packet graph.

The deployed degree-18 partial-relative interface and the stronger local
heavy-ruling interface require respectively 18 and at least 20 records on
the chosen anchor line. Their 31-overlap rigidity can synchronize packets
inside one type, as already proved, but cannot cross between types. The
combinatorial obstruction says nothing about compatibility under a stronger
theorem using less overlap or different ownership semantics.

For completeness, this does not mean the general atom-collision theorem needs
31 shared records. Its primitive root-free corollary needs only two. If two
distinct certificates share `r=28` supports, the general collision bound

```text
r(m'-g)<=n'-g
```

forces

```text
g>=ceil((28m'-n')/27)=1079711-c,                    (2)
```

where `(n',m',K')=(n-c,m-c,K-c)`. The common-zero part `H` has size at most
the denominator degree `d=67472`, so

```text
|G\H|>=1012239-c.                                   (3)
```

Every point in `G\H` lies in at least 27 of the 28 supports. The deck has 14
records from each pair type, so such a point lies in at least two supports of
each type and therefore in both pair cores. Distinct Reed--Solomon pairs can
share at most

```text
K'-1=1048575-c
```

core coordinates. Bound `(3)` is short of that contradiction by exactly
`36336`. Thus the collision theorem routes a distinct quotient atom into a
large-core/nonprimitive exception but does not currently eliminate it. This
is the exact remaining compatibility interface. QED.
