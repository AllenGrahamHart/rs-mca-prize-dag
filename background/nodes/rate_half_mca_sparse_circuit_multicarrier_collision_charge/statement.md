# Fixed-union multicarrier collision charge

- **status:** PROVED
- **correction dimension:** `10`
- **target support:** `2<=d<=9`

Let `V<=P_K` have dimension ten and empty common zero set.  Let `D` be a
fixed set of `u` domain points and let `W<=V` have dimension `g`, with every
polynomial in `W` vanishing on `D`.  For target support `d`, put

```text
r_d=g+1-d.
```

Whenever `r_d>0`, every independent target `(d-1)`-deletion carrier has at
most

```text
R_d=K-r_d-u
```

points outside `D`.  Consequently the number of target-support-`d` circuit
supports is at most

```text
C(u,d) + sum_(j=1)^d floor(
  C(u,d-j) C(m-u,j-1) max(0,R_d-j+1) / j
).                                                        (MC1)
```

Their selected eleven-set incidence is at most `(MC1) C(m-d,11-d)`.

## Falsifier

A target deletion for which `W intersect H_A` has dimension below
`g+1-d`; a carrier with more than `K-r_d-u` points outside `D`; or a target
circuit omitted from the inside stratum and all exact outside strata.
