# L1 coarse p-free tame-tail distance upgrade

- **status:** PROVED
- **role:** remove the false half-depth collision strata below the
  characteristic
- **consumers:** `l1_coarse_pfree_wronskian_neighbor_compiler`,
  `l1_mixed_petal_amplification`

## Tame Wronskian lower degree

Let `F` have characteristic `p`. For disjoint nonempty `t`-sets `X,Y`, put

```text
F_X=product_(x in X)(Z-x),       F_Y=product_(y in Y)(Z-y),
W=F_X'F_Y-F_XF_Y'.                                  (TTD1)
```

If `t<p`, then

```text
deg W>=t-1.                                          (TTD2)
```

The strict inequality is necessary. Over `F_4`, the p-free depth-two
collision `{0,1}`, `{alpha,alpha+1}` has `t=p=2` and constant Wronskian.

## Upgraded coarse distance

In a coarse p-free depth-`d` fiber on `a`-sets, distinct members have tail
width

```text
t>=tau_p:=max(ceil((d+2)/2), min(d+1,p)).             (TTD3)
```

Equivalently,

```text
d<p:       t>=d+1,
d>=p:      t>=max(ceil((d+2)/2),p).                  (TTD4)
```

Thus the coarse map has the full-prefix distance throughout the ordinary
Newton window. At every checkpoint depth, no collision exchanges fewer than
`p` roots. Under the official generated-field hypotheses,

```text
d>=p  =>  t>=p>n/24.                                 (TTD5)
```

The improved packing subset size and cap are

```text
s_p=a-tau_p+1,
max_z |Phi_free^(-1)(z)|
 <=floor(binom(n,s_p)/binom(a,s_p)).                 (TTD6)
```

## Sharp tame fixture

Over `F_5`, the disjoint pairs

```text
X={0,1},       Y={2,4}
```

have equal first moments. Here `d=1`, `t=d+1=2<p`, and

```text
W=Z+2,
```

so `deg W=t-1`. Both `(TTD2)` and `(TTD3)` are sharp.

## Scope

This is a characteristic-safe collision-distance and packing upgrade. It
deletes all formal half-depth certificate strata below `tau_p`; it does not
bound the surviving exchange-subset multiplicity, prove row-sharp Q, or
close L1.
