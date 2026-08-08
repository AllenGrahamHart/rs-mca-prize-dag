# Proof

Let `m=B(-t^2)/A(-t^2)` be the source-forced missing product.  In matchings
`0,1,2`, the first residual pair is the same in all three cases.  If a
positive `DE` record is missing, it is `(m,-m)`; if `-DE` is missing, it is
`(-m,-m)`.  The exact pair-resultant equation therefore gives the necessary
target-free cuts

```text
P(m,-m)=0,             P(-m,-m)=0.                (DE12-1)
```

Reduce each cut in the proved quadratic-in-`t`, quadratic-in-`b` common
algebra and take its four-dimensional multiplication norm over `F_p(r)`.
For each of four source-sign lanes, the positive cut has a degree-350 norm
numerator with eight deployed roots and the negative cut a degree-362
numerator with seven deployed roots.  The compiler unions these roots with
every numerator and denominator root introduced by the tower arithmetic.
The complete union contains 116 case-labeled candidate `r` values.

Direct replay through the original tower accounts for every candidate:
route guards, leading boundary, no deployed lift, a source-inconsistent
`A=0,B!=0` point, or direct nonzero evaluation of `(DE12-1)`.  The negative
cut has no generic zero.  The positive cut leaves exactly two generic zeros
in each source-sign lane.

At a surviving positive point the missing Vieta data impose

```text
de=m,                  (d+e)^2=S,
S=(-t^2) beta(-t^2)^2/A(-t^2)^2.                 (DE12-2)
```

For each point, target lane, and matching `0,1,2`, adjoin `(DE12-2)`, the
three residual pair equations, and the full target guard.  There are

```text
8 source points * 4 target lanes * 3 matchings = 96 systems.
```

Singular obtains the unit ideal in every system.  An independent SymPy
audit substitutes `e=m/d`, includes the squared-sum equation, saturates in
the two remaining variables, and also obtains 96 unit ideals.  The second
positive missing role follows from exact exchange of the duplicate `DE`
records.  The parent boundary theorem pays the rational leading complement.
Hence all nine stated labels are empty. QED.
