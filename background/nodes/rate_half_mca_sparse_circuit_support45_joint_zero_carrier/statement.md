# Joint support-four/support-five zero carrier

- **status:** PROVED
- **correction dimension:** `10`
- **source supports:** `4,5`

Put `q=K-10`.  Suppose independent support-four and support-five deletions
have respectively `q-s_4` and `q-s_5` circuit completions, where

```text
q>s_4+s_5.
```

Let `U_4,U_5` be their completion carriers and let `H_4,H_5` be the
subspaces of `V` vanishing on those carriers.  Then

```text
dim(H_4 intersect H_5)>=4,
|U_4 union U_5|<=q+6.                              (JZ1)
```

Close `H_4 intersect H_5` under all of its common zeros in the evaluation
set.  If `B` is that zero set and

```text
H_B={f in V:f|_B=0},       t=dim H_B,
delta=K-t-|B|,
```

then

```text
4<=t<=6,       0<=delta<=min(s_4,s_5).             (JZ2)
```

For every independent three-set `A`, the union of `A` and all of its
support-four circuit completions has at most `delta+3` points outside `B`.

## Falsifier

A Grassmann-minimal three-dimensional intersection without a common zero of
`V`; a zero closure with `t` or `delta` outside `(JZ2)`; or one independent
three-set whose completion carrier has more than `delta+3` points outside
`B`.
