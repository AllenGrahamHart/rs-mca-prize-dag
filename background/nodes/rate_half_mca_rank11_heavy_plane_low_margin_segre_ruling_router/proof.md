# Proof

## Exact margin split

After locator cancellation the row has

```text
(n,K,m)=(1048576+K,K,67472+K),
4<=K<=1010840.
```

Apply the general margin/interleaving theorem with correction dimension
four and `T=12`. For affine subranks `r=0,1,2,3,4`, the uniform
support-local caps are

```text
171618, 1357966, 21103440, 327952934, 9319299072.       (1)
```

For `r>=1`, the `K`-dependent term has successive ratio with one minimum,
so its maximum over the interval occurs at an endpoint. The second term is
independent of `K`; `r=0` is increasing. Thus (1) checks the complete
shortening interval. The high-margin family has at most `9319299072`
records, and subtracting from `M_*` proves `(SR1)`.

For the low family, the pair-list argument uses common agreement
`A=m-11`. Its ordinary four-dimensional list cap is

```text
Q_4=floor(C(1048580,4)/C(67465,4))=58361.              (2)
```

The square of this integer is `3406006321`, below the deployed field size,
so the interleaving collapse gives the same cap for ordered pairs. Fix one
pair for every record by a deterministic rule.

## Segre intersection

Use the reversible affine gauge from the support-local theorem. If `c_0`
is its fixed anchor, a chosen low pair has the form

```text
(a,b)=(c_0+A,B),       A,B in V.
```

At its owned slope `gamma`, the selected explanation is
`c_0+A+gamma B`. The heavy-plane factor presentation says its correction
`A+gamma B` lies in one original ruling plane and hence has tensor rank at
most one.

Identify `V=P tensor Q` with `2 x 2` matrices. The polynomial

```text
D_(A,B)(Z)=det(A+ZB)
```

has degree at most two. If it is nonzero, at most two field elements are
roots. Summing this bound over at most `Q_4` pair types leaves the mass in
`(SR2)` on pairs for which `D_(A,B)` is identically zero.

We recall the elementary line classification. If independent rank-one
matrices `A=u v^t` and `B=x y^t` have neither common left factor nor common
right factor, then both pairs `(u,x)` and `(v,y)` are independent. Row and
column basis changes send the span to the diagonal matrix line, which
contains a rank-two matrix. This contradicts the determinant identity.
Hence a two-dimensional all-rank-one span is `gQ` or `Pq`. A
one-dimensional span has a unique rank-one point and is assigned to its
left ruling by convention. This proves the ruling claim.

## Per-ruling capacity and nonzero alignment

Restrict the low-pair argument to a fixed ruling plane `R`, which has
dimension two. The ordinary cap becomes

```text
Q_2=floor(C(1048578,2)/C(67463,2))=241.               (3)
```

For each fixed pair, pair noncontainment injects its slopes into the
coordinates outside its common core. There are at most

```text
n-(m-11)=981115
```

such coordinates. Equations (2)--(3) and the sub-square interleaving
argument therefore give the per-ruling cap `(SR3)`. Since twice this cap is
`472897430<645992192`, at least three ruling planes occur.

For `(A,B)!=(0,0)`, the equation `A+gamma B=0` has at most one solution in
`gamma`. The one zero pair `(A,B)=(0,0)`, if present, is one fixed low pair
and has at most `981115` owners by the same outside-core injection. Thus
zero corrections cost at most

```text
(Q_4-1)+981115=1039475,
```

proving `(SR4)`. Canonically partitioning the remaining ruling pair types
by orientation proves `(SR5)` and the two-plane floor.

Finally, let a nonzero correction `C_gamma` have original factor
`g_gamma`, so `C_gamma in g_gamma Q`. If its chosen pair pencil has left
ruling `gQ`, injectivity of `P tensor Q -> V` gives

```text
gQ intersection g_gamma Q={0}
```

unless `[g]=[g_gamma]`; nonzeroness therefore synchronizes the left factor.
If its ruling is `Pq`, the same tensor calculation gives

```text
Pq intersection g_gamma Q=<g_gamma q>.
```

Thus the right factor `[q]` is synchronized exactly as stated. QED.
