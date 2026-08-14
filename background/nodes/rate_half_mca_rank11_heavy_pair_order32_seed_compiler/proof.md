# Proof

Let `Z_lo` be the selected post-near records with `theta<=387` and let
`P` be their distinct fixed minimizing pair types. The rank-eleven
interleaving theorem gives

```text
|P|<=Q_10(387)
    =floor(C(1048586,10)/C(67095,10))
    =869784434119.                                  (1)
```

Split `P=P_1 disjoint_union P_2`, where a type in `P_1` owns exactly one
record and a type in `P_2` owns at least two. Equation (1) gives

```text
records owned by P_1 <=869784434119.                (2)
```

## The heavy family cannot have a large common core

For `p=(a,b)` put

```text
H_p={x:r_0(x)=a(x), r_1(x)=b(x)}
```

and let `J_2=intersection_(p in P_2) H_p`. If
`|J_2|>=K-4922`, shorten all heavy pair differences on any
`K-4922` points of `J_2`. The proved shared-core endpoint applies to the
heavy ordered pairs: at most `94943` distinct types occur, and every type
owns at most `n-m+1=981105` records. Together with (2),

```text
|Z_lo| <=869784434119+94943*981105
       =962933486134.                               (3)
```

The high-margin family costs at most `274790124064526354`, and the disjoint
near-rational charge is `134944`. Under the large-heavy-core assumption the
whole line therefore has at most

```text
134944+274790124064526354+962933486134
 =274791086998147432
 =B_*-189641113247655,
```

contrary to unsafety. Hence

```text
|J_2|<K-4922.                                       (4)
```

There are many low records: unsafety and the two complementary charges give

```text
|Z_lo|>=B_*+1-134944-274790124064526354
       =190604046733790.                            (5)
```

In particular `P_2` is nonempty by (1), (2), and (5).

## At most eleven heavy pairs recover the complete heavy core

After the reversible gauge, all explanations lie in `c_0+C'` with
`dim C'=10`. For a minimizing pair attached to
`h_gamma in c_0+C'`,

```text
b in C',       a=h_gamma-gamma*b in c_0+C'.
```

Fix `p_0=(a_0,b_0) in P_2` and define the component space

```text
V=span{a-a_0,b-b_0:(a,b) in P_2} subseteq C'.
```

Thus `dim V<=10`. Greedily choose pair types `p_1,...,p_t` from `P_2`
until their two component differences from `p_0` span `V`. Every selected
pair adds at least one new component direction, so

```text
t<=dim V<=10.                                       (6)
```

Moreover,

```text
intersection_(i=0)^t H_(p_i)=J_2.                  (7)
```

Indeed, inclusion from right to left is immediate. Conversely, at a point
in all selected cores, `p_0` equals the received pair and every selected
component difference vanishes. Those components span `V`, so every heavy
pair difference vanishes there; every heavy pair therefore equals the
received pair.

## Two slopes per pair force the support core

Each selected `p_i` is heavy. Choose two of its distinct owned records.
For a fixed pair, the rank-eleven ratio identity makes the exception sets

```text
S_gamma\H_p
```

disjoint across distinct slopes. Hence the intersection of the two selected
supports is contained in `H_p`. Taking all selected pairs and using (4),
(6), and (7), at most

```text
2(t+1)<=22
```

actual records have support intersection smaller than `K-4922`.

Finally, (5) supplies enough further distinct low-margin records to pad the
selection to exactly `32`. Adding supports can only shrink their common
intersection. Every record was selected before this argument and no label,
slope, support, pair, or chronology is changed. This proves the compiler.
