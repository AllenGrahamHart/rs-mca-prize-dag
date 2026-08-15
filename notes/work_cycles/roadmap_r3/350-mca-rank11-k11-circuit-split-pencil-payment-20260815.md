# Cycle 350: MCA rank-11 K'=11 circuit/split-pencil payment (2026-08-15)

Cycle 349 closed the minimal row `K'=10`.  The next row has a
ten-dimensional correction hyperplane in `RS_{<11}` and admits the proved
eight-petal fixed-chart witness, so another chart-local record cap cannot
work.  This cycle retains every neighboring nine-shadow and the one global
hyperplane functional.

## Core-offset selected-support cap

For selected petal mass `P`, common-core offset `r`, owner weights
`s_p<=P-1`, and total mass `S`, the new abstract theorem bounds

```text
sum_L [sum_p C(x_(L,p),2)+rP]
```

by three explicit terms.  Balanced lines pay their offset using the line
count forced by cross charge `X_L>=floor(P^2/4)`.  Clean dominant lines pay
through disjoint light mass and the existing exact slack factorization;
heavy-collision lines inject into heavy-owner pairs.

At `K'=11`, a rank-nine chart has common core `j in {9,10}`.  The two exact
caps are

```text
j=9:  9274924665987729,
j=10: 9275866238180030.
```

Thus every rank-nine nine-shadow has uniform capacity
`C_*=9275866238180030`.

## Circuit payment

Every component eleven-set has rank ten and one circuit `C_T`.  If
`|C_T|>=6`, it has at least 45 rank-nine shadows, so all high-circuit
incidences together are at most `C(n',9)C_*/45`.

If `|C_T|<=5`, its circuit is a support of one representation of the global
functional cutting out `V'`.  Two such supports have union size at most ten;
Vandermonde independence forces the representations to be identical.  All
low-circuit incidences therefore contain one fixed support `C_*`, and one
record contributes at most `C(m'-1,10)` of them.

At the minimum record count, high plus low capacity is

```text
870719390190680409022824387604193486699840723094988553120053384,
```

whereas full dense-locator incidence requires

```text
901408286315387898338134887980054663001598216883356906995509296.
```

The gap is

```text
30688896124707489315310500375861176301757493788368353875455912.
```

Its record coefficient is positive, so the contradiction persists for every
allowed larger record count.  The fixed-chart eight-petal witness is not
refuted: its full circuit creates 54 neighboring rank-nine shadows, which are
now charged globally.

The abstract audit tested 845,481 exhaustive weighted `F_3` instances and
2,240 deterministic `F_5` instances in one 512 MB Modal container.  Primary
and independent application replays checked 8,099 Vandermonde subsets, all
605 circuit-shadow omissions, exact arithmetic, and hostile mutations.

```text
result:                PROVED K'=11 component-row closure
newly closed row:      11
remaining rank nine:  12..15528
new nodes:             2 PROVED
new premise:           none
compute:               exhaustive toy audit on Modal; exact arithmetic local
next route action:     K'=12 codimension-two quotient-support census and
                       core offsets j=9,10,11
```
