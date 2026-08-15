# Proof

Put `Lambda=V^perp`, so `dim Lambda=q`.  Evaluation functionals at at most
`K` distinct points are independent on `P_K`.  If `T` has size eleven and
evaluation rank ten on `V`, annihilator duality gives

```text
dim(Lambda intersect E_T)=11-rank(ev_T|V)=1.       (1)
```

Thus `T` selects one label, with one minimal circuit support.  The empty
common zero hypothesis excludes support one.

Fix a support size `2<=c<=5` and delete one point from a circuit.  The
remaining `(c-1)`-set `A` is independent.  Hence

```text
H_A={f in V:f|_A=0},       dim H_A=11-c.           (2)
```

Every circuit completion of `A` is a common zero of `H_A`.  If `z` distinct
points are common zeros, division by their degree-`z` locator embeds `H_A`
in `P_(K-z)`, so

```text
z<=K-dim H_A=K+c-11.
```

The `c-1` points of `A` are already common zeros.  Therefore `A` has at
most

```text
K+c-11-(c-1)=K-10=q                              (3)
```

circuit completions.

Suppose some `A` has all `q` completions.  Their labels have private
nonzero completion coordinates in the evaluation basis on their union
with `A`; hence they are independent and span `Lambda`.  Their carrier has
size

```text
|U|=c-1+q<=q+4.
```

For any other sparse label with support `D`, the representations on `U`
and `D` agree because

```text
|U union D|<=q+9=K-1,
```

within the Vandermonde independence range.  Thus `D subset U`.  There are
at most `C(q+4,c)` possible supports and `C(m-c,11-c)` eleven-set extensions
of each, proving `S_c`.

Otherwise every independent deletion has `b<=q-1` completions.  A
rank-ten eleven-set containing one completion cannot contain a second:
their private coordinates make the two labels independent, contradicting
(1).  For one fixed `A`, its `b` completions therefore contribute at most

```text
b C(m-c+1-b,11-c)                                 (4)
```

eleven-sets.  Sum (4) over at most `C(m,c-1)` deletions.  Every
support-`c` circuit is charged exactly `c` times, once for each deleted
point.  Division by `c` and the final integer floor prove `U_c`.

For the official rows, `q-1<=10`.  The ratio

```text
(b+1)C(N-b-1,e) / (b C(N-b,e))
```

is at least one exactly while `b<=(N-e)/(e+1)`, where
`N=m-c+1` and `e=11-c`.  Since the threshold is above 6700 on every
official specialization, (4) is increasing through `b=q-1`.  QED.
