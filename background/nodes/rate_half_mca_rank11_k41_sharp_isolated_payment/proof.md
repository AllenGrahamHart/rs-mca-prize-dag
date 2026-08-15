# Proof

Put

```text
n=1048617,       m=67513,       q=31,
R_min=274980728111260126.
```

The proved full-deficit payment evaluated every core and every kernel corank
at this adjacent row.  Its maximum rank-nine chart is `9275193525062548` at
core `40`; its active weighted completion premium is

```text
39561174868876502380458662244149949146908334937.
```

Consequently its kernel, full-rank, and total capacities are

```text
16046971808807649741426607721480807522683424615973152263500,
910209210272037933519378596037417532927979530870933219830034826,
910225257243846741169120022645139013735502214295549192982298326.
                                                               (1)
```

The rank-stratified isolated-incidence theorem gives exact component demand

```text
D(R)=R C(m,11)-C(n,11).                                (2)
```

At `R=R_min`, (2) is the number in the statement.  Subtracting (1) gives the
printed positive gap.

For variable `R`, clear the denominator 55 in the full-shadow capacity.  The
coefficient of `R` is

```text
55 C(m,11)-premium
=143297102916558158042999955475306246365479723103>0.   (3)
```

At the record floor, the complete unfloored cross, including the isolated
term `55 C(n,11)`, is

```text
217790641694614499449513956371904133229081272051117311471075418>0.
                                                               (4)
```

Equations (3)--(4) show that the contradiction persists for every
`R>=R_min`.  Exact evaluation at `K'=42` gives capacity excess

```text
2710771376158610722953158157862051010402433288229120154217278,
```

so that adjacent row is retained as the first wall of this method.  QED.
