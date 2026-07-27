# Proof

The coefficient magnitudes in profile `(3,4,0)` are

```text
2,2,2,1,1,1,1.
```

Consequently its 21 unordered support chords comprise three products of
absolute value four, twelve of absolute value two, and six of absolute value
one. The six unit products are precisely the edges among the four light
coefficient positions.

For `1<=d<=63`, reduce the signed chord formula for `A_d` modulo two. Products
of magnitude two or four vanish modulo two, while either sign of a unit
product is one. Hence

```text
A_d = number of unit-product chords in distance class d  (mod 2).  (3)
```

Every odd `A_d` therefore consumes at least one of the six unit chords. The
three profiles left by `e1_n256_s16_e34_three_profile_reduction` have numbers
of odd coefficients

```text
(6,7):      6,
(9,4,1):   10,
(12,1,2):  14.
```

The latter two exceed the unit-chord supply, proving (1). Equality in the
first line forces every unit chord to occur in a non-diameter class and forces
the six unit chords to occupy six distinct classes. This proves the circular
Sidon assertion.

It remains to record the exact diameter consequence. Diameter chords form a
matching. With no light-light diameter, a matching either has no heavy-heavy
edge and at most three heavy-light edges, or has one heavy-heavy edge and at
most one heavy-light edge. Their square masses are respectively

```text
4 d_2,             0<=d_2<=3,
16+4 d_2,          0<=d_2<=1.
```

This gives the displayed set for `D_64`. The signed-chord identity at
`V/2=34` is

```text
34=102-D_64+2C,
```

which gives the corresponding values of `C`. QED.
