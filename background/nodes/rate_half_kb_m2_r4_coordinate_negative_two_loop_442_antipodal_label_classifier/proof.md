# Proof

Choose representatives `A,B,C` for the three signed `J` pairs.  At the
`A` loop the edge product is `p_A=-A^2`.  Orient the `AB` and `AC` deck
orbits by choosing the edge containing `A`; write their endpoint sums as
`s_AB,s_AC`.  Their products obey

```text
p_A-p_AB=-A s_AB,       p_A-p_AC=-A s_AC.         (1)
```

Use `k_A` as the loop anchor in `(KBNW-2)`.  Cancelling the common nonzero
factors involving `k_A`, then substituting `(1)` and
`q_E=x_E s_E` with `x_E^2=k_E`, gives

```text
x_AB(k_AC-k_B)=x_AC(k_AB-k_B).                    (2)
```

Squaring `(2)` and expanding gives

```text
(k_AB-k_AC)(k_B^2-k_AB k_AC)=0.
```

The five `K` labels are distinct, proving the first identity in `(KB44-1)`.
Repeat with the `B` loop anchor and the `AB,BC` edges to obtain the second.
The argument is unaffected by deck-orbit orientation because each edge is
oriented by its shared loop endpoint before squaring.

Scale all five labels by `k_AB^(-1)`.  The two identities give exactly
`(KB44-2)`.  Since `K` is obtained from the three-antipodal-pair set `I` by
deleting one point, these five distinct values have two antipodal pairs and
one singleton.

It remains to inspect the fifteen perfect matchings of four of
`X,L,M,Y,Z`.  The complete table is:

```text
singleton   matching 1   matching 2   matching 3
X           LM|YZ bad    LY|MZ (3a)   LZ|MY bad
L           XM|YZ bad    XY|MZ (3b)   XZ|MY bad
M           XL|YZ bad    XY|LZ bad    XZ|LY (3c)
Y           XL|MZ bad    XM|LZ bad    XZ|LM bad
Z           XL|MY bad    XM|LY bad    XY|LM bad
```

Here a pair `UV` means `U=-V`.  For the three retained cells:

```text
LY|MZ: l=-m^2, m=-l^2  ==> l^3=-1;
XY|MZ: m^2=-1, m=-l^2 ==> l^4=-1;
XZ|LY: l^2=-1, l=-m^2 ==> m^4=-1.
```

In the first row distinctness removes `l=-1`.  Every bad cell either forces
`2=0`, forces `l=-1` or `m=-1` and hence `X=Z` or `X=Y`, or forces `Y=Z`.
For example `LM|YZ` gives `l=-m` and `m^2=-l^2`, while `XZ|LM` gives
`l^2=-1`, `l=-m`, and hence `Y=Z`.  The remaining bad cells are the same
three contradictions after interchanging `l,m` or the role names, exactly
as displayed in the exhaustive table.

Adding the negative of the singleton gives the six-sets in `(KB44-4)`.
Finally, direct substitution of the five banked `F_29` labels into the 120
role assignments finds no pair satisfying `(KB44-1)`; the verifier replays
this consequence, but it is not used in the universal argument. QED.
