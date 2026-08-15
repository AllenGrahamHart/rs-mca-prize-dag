# Proof

Put `q=35`, `n=1048621`, and `m=67517`.  At source support `c`, the universal
completion theorem and branch-lattice refinement partition the completion
maximum into

```text
M_c=q-s,       0<=s<=9-c,
M_c<=q-(10-c).
```

There are `11-c` alternatives.  Taking their Cartesian product for
`c=2,...,9` gives exactly `9!=362880` disjoint exhaustive leaves.  Every
leaf inherits the baseline sparse cap; terminal alternatives add their
source and valid cross-support caps, while fallback alternatives add their
lower source ceiling.

Exactly

```text
6*5*(9*8*5*4*3*2)=259200
```

leaves have terminal support-four and support-five defects.  Since
`q>s_4+s_5` throughout their ranges, the external-carrier theorem applies
on every such leaf.  Intersect its support-four incidence cap before applying
the deficit weights `C(11-c,2)`.

A streaming enumeration of all leaves, independently replayed, gives the
worst final premium

```text
40126324034612056409620566967689123241580103372,       (1)
```

at the unique all-fallback label.  Without the joint cap, the worst terminal
leaf would have premium

```text
41119280132819537082584175767452500583010727727,
```

which is unsafe.  Thus both the full fallback product and the joint terminal
charge are needed.

Retaining the all-core rank-nine chart and every kernel corank gives

```text
kernel capacity =
20541224524206770168358957675733727352177985505266924004331,

rank-nine marks =
39188933245978335442844817333731704607806583940216121605190822065.
```

Using (1), complete full-rank and total capacities are

```text
913143619008078468726311141809692801590446007571848493844592126,
913164160232602675496479500767368535317798185557353760768596457.
```

Sharp isolated incidence gives demand

```text
914781132033911037023306142255422245003715593805730189113734390.
```

The difference is the positive gap printed in the statement.  The cleared
record coefficient and floor-record cross are respectively

```text
142851171448156502676296279588073248696830521058,
88933449071959883975465281842954032725457453660703558982586308,
```

so the contradiction persists above the record floor.

Repeating the complete branch replay at `K'=46` identifies the all-fallback
leaf again, now with premium

```text
41485443362306086690496505287800656619099676245,
```

and the negative gap printed in the statement.  Thus this exact payment
closes `K'=45` and first fails at `K'=46`.  QED.
