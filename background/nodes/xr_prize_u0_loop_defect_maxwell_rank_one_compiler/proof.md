# Proof

Let `G` be the global common-root set of the affine kernel and `P_0` its
persistent subset. Since `u=0`,

```text
|G|=k-a,       |P_0|=k-a-v.
```

At every coordinate of `G\P_0`, the selected error value is a nonzero affine
function of the slope and vanishes at at most one slope. Delete the union of
those exceptional slopes; it has size at most `v`. Every retained selected
error has no zero in `G\P_0`.

Divide the affine kernel by the locator of `G` and puncture `G`. The kernel
becomes all degree-less-than-`a` evaluations on `N=R+a` points. A retained
error has at least

```text
k+h-|P_0|=a+h+v=m
```

zeros outside `G`; choose exactly `m` of them. Two chosen blocks meet in at
most `k-|P_0|=a+v` points. As in the uniform split-pencil reduction, the
extension direction is not a `GRS_a` word on any block: otherwise it and the
received offset would have kernel explanations on that block, and lifting
through `P_0` would give a tangent-paid common `k+h`-point explanation. This
proves `(LC1)` and the coherent extension normalization.

At the official cells, the retained family has at least `B+1-v` members and

```text
h(B+1-v)>2N-2(a+v).
```

Choose an inclusion-minimal nonempty core satisfying

```text
h|G|>=2|union G|-2(a+v).                              (1)
```

Writing equality with excess `e` gives `(LC2)`. Minimality gives
`e+2p_A<=h-1` for every block-private count `p_A`, hence `0<=e<=h-1`. One
block would make `h>=2h`. For two blocks, the pair cap gives union size at
least `a+v+2h`, while `(1)` would require `2h>=4h`. Thus `t>=3`.

For each block `A`, stack a full-row-rank parity check of `GRS_a|A` in the
two syndrome columns. It has `m-a=h+v` rows. On the union `V`, the two copies
of `GRS_a` give `2a` independent right-kernel directions. The received
extension pair gives one more because its direction is non-`GRS_a` on every
block. Therefore the stack has rank at most `2|V|-(2a+1)`, and its left
kernel has dimension at least

```text
(h+v)t-[2|V|-(2a+1)]
 =v(t-2)+e+1.                                         (2)
```

This proves `(LC3)`. Reading the two syndrome columns of any left relation
gives

```text
sum_A lambda_A=0,       sum_A gamma_A lambda_A=0.     (3)
```

Each row lies in the dual of an `[m,a]` GRS code and therefore has support at
least `a+1`. At an active coordinate, one coefficient cannot satisfy the
first equation in `(3)`, and two coefficients at distinct slopes cannot
satisfy both. Its active degree is at least three.

It remains to classify rank one. Let the active rows be
`lambda_i=alpha_i lambda`, with every `alpha_i` nonzero, and put
`S=supp(lambda)`. Then `S` is contained in every active block. Dual distance
and the pair cap give `(LC4)`. Equation `(3)`, evaluated at any point of `S`,
gives `(LC5)`; in particular at least three blocks are active.

For one active block `A_i`, the dual locator representation is

```text
lambda_i(x)=P_i(x)/Lambda'_(A_i)(x),       deg P_i<h+v.
```

Because the row vanishes on `A_i\S`,

```text
P_i=Lambda_(A_i\S) Q_i,       deg Q_i<w-a.           (4)
```

For `x in S`, cancellation of the complementary locator in `(4)` gives

```text
alpha_i lambda(x)=Q_i(x)/Lambda'_S(x).                (5)
```

The polynomials `Q_i/alpha_i` have degree less than `w-a<w` and agree at all
`w` points of `S`; they are one polynomial `Q`. Exact support means that `Q`
has no root on `S`. This proves `(LC6)`.

Conversely, given `(LC4)--(LC6)`, the numerator

```text
alpha_i Lambda_(A_i\S)Q
```

has degree less than `(m-w)+(w-a)=h+v`, so `(LC6)` is a dual word on every
active block. Conditions `(LC5)` give both equations in `(3)`. Hence it is a
rank-one trade, proving exactness of the classification.

Finally, at `u=0` the effective-core theorem gives the lower endpoints in
`(LC7)`, while the nonpersistent-root cap gives the upper endpoints. QED.
