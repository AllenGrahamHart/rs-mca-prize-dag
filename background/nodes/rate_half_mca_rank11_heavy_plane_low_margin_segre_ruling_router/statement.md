# Rank-eleven heavy-plane low-margin Segre ruling router

- **status:** PROVED
- **scope:** the shortened heavy `2 x 2` Segre bucket

Let `V=P tensor Q` be the four-dimensional correction space and retain the
first-owned mass

```text
M_*=9965407986.
```

For every shortened dimension `4<=K<=1010840`, split the records at
support-local margin `T=12`. Then

```text
high-margin mass <=9319299072,
low-margin mass  >= 646108914.                         (SR1)
```

Fix one low pair by a deterministic rule. The four-dimensional ordinary
pair-list cap gives at most

```text
Q_4=58361
```

distinct pair types. In tensor coordinates, write its correction pair as
`(A,B) in V^2`. Its selected explanation correction at slope `gamma` is

```text
C_gamma=A+gamma B,
```

and lies on the rank-one Segre cone. If
`det(A+ZB)` is not identically zero, this occurs for at most two slopes.
Therefore pair types whose complete pencils lie on the Segre cone carry at
least

```text
646108914-2*58361=645992192                           (SR2)
```

records. Every such pencil is contained in a ruling plane `gQ` or `Pq`.

A fixed ruling plane has correction dimension two. Reapplying the low-pair
list bound inside that plane gives

```text
Q_2=241,
(n-A)Q_2=981115*241=236448715.                         (SR3)
```

Hence the mass in `(SR2)` uses at least three ruling planes.

At most one selected slope per nonzero pair type has `C_gamma=0`; the
single zero pair type has at most `981115` owners. Thus at most

```text
(58361-1)+981115=1039475
```

ruling records have zero correction. At least

```text
645992192-1039475=644952717                            (SR4)
```

records therefore align nontrivially with their ruling. Assign
one-dimensional pair pencils to their left ruling and partition all others
by their unique left/right ruling. One orientation carries at least

```text
ceil(644952717/2)=322476359                            (SR5)
```

records and, by `(SR3)`, uses at least two ruling planes.

For a left ruling `gQ`, every nonzero selected correction also lies in its
original factor slice `g_gamma Q`, so `g=g_gamma`. For a right ruling `Pq`,
the intersection with the original slice is the line `g_gamma q`, so the
same residual factor `[q]` is synchronized across those records.

## Nonclaim

The theorem does not decide which orientation is heavy, bind different
ruling planes to one chronology owner, or pay either output. It does not
make a base-field assertion and does not close the heavy bucket.
