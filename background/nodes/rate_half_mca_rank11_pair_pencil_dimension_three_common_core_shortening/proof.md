# Proof

## Affine-plane occupancy

Let `A` be an affine plane in the scalar polynomial space and suppose it
contains `t` selected types. If their affine span has dimension at most one,
the affine-line cap gives `t<=15`. Otherwise translate one selected point to
zero; the difference space has dimension two.

Factor its polynomial gcd. As in the dimension-two incidence theorem, the
coordinates in the resulting common received-pair core have multiplicity
`t`, while every other coordinate fiber is an affine line and has
multiplicity at most 15. The common core has size at most `K-1`. Thus

```text
t(m-2)<=t(K-1)+15(n-(K-1)),
t<=floor(15(n-K+1)/(m-K-1)).                         (1)
```

The official denominator is

```text
(m-2)-(K-1)=m-K-1=67471,
```

and exact division gives

```text
floor(15*1048577/67471)=233.                         (2)
```

This proves the affine-plane cap in every case.

## Dimension-three global core

Now suppose the full scalar span `W` has dimension three. Factor its gcd and
let `J` be the received-pair core common to all 520 types. At a gcd root, all
pair codewords agree, so a coordinate has core multiplicity 520 or zero. At
a non-gcd root, evaluation on the primitive three-dimensional scalar space is
a nonzero linear functional. Types whose pair cores contain the coordinate
lie in one affine plane fiber, so `(2)` caps their number by 233.

As before `j=|J|<=K-1`. Counting core incidences gives

```text
520(m-2)<=520j+233(n-j).
```

Since `520-233=287`,

```text
j>=ceil((520*1116046-233*2097152)/287)=319539.       (3)
```

The common-core shortening theorem depends only on every pair codeword and
the received pair agreeing on `J`, not on scalar dimension. It therefore
subtracts the common pair, punctures `J`, and divides punctured received
values and explanations by `L_J`. It is reversible and preserves all
first-owned records, quotient-core deficiency two, and `m-K=67472`.

At the minimum in `(3)`, direct subtraction gives

```text
n'=2097152-319539=1777613,
K'=1048576-319539=729037,
m'=1116048-319539=796509,
s'=m'-2=796507.
```

Finally

```text
233n'-520s'=414183829-414183640=189.
```

QED.
