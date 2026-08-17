# Proof

The split common-system adapter identifies the five O0b common records in
every lane with the already certified O0a packet. The rank-drop parent has
removed rank at most four, so every retained point has product rank five and
lies in at least one of the six maximal-cofactor charts.

For cell `0`, the pinned chart certificate is the Cartesian product of four
source-sign rows and six charts. All twelve chart rows with unequal source
signs have dimension `-1`, basis size one, and basis `1`. Thus neither mixed
sign row has a common point. The outside graph is irrelevant once the common
system is empty, and copying across six lanes and 105 labels proves the
1,260-row exclusion.

For equal signs, the old cell-0 common proof factors the chart equations and
uses the nonzero source guard to obtain the necessary alternatives

```text
A_s: c=s*i*b,  r=b^(-1),
     x*b*(1+alpha_s*b)+alpha_s+s*i*b=0;

B_s: c=-s*i*b, r=b,
     x*(b+alpha_s)+b*(alpha_s*b+s*i)=0.
```

The component certificate has exactly the four `component/sign` rows and
reduces all ten common Vieta rows to zero in each row. This classifies the
surviving common locus but does not decide its changed O0b outside graph.

Finally, direct orbit enumeration restricts the proved Klein-four actions to
the mixed-sign cell-0 rows. `S0` has 18 size-two and 96 size-four orbits;
`SDE/SDF` has 60 size-two and 180 size-four orbits. Their total is 354.
Subtracting the proved raw and quotient closures gives the stated frontier.
Each equal-sign orbit has two component branches, hence 708 next-stage cases.
QED.
