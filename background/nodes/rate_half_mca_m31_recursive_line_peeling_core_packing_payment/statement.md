# Mersenne recursive line-peeling core-packing payment

- **status:** PROVED
- **scope:** Mersenne-31 full-lift supports `124806<=e<=130198`

Retain the pair-noncontained full-lift notation and put

```text
N=1048582,  m=67454,  K=6,  c=5,
B=16777215, Q=N-m+1=981129.
```

For each support `e`, choose the printed legal prefix cutoff `b_e`.  On a
residual assigned family whose deficits are at most `U`, retain every exact
layer `b_e<h<=U` as its bank of affine explanation-line slots.  If the
residual has more than `T` slopes, one slot has at least

```text
lambda=ceil((T-C+1)/G)
```

members, where `C` is the prefix/base charge and `G` is the number of line
slots.  Remove the entire resulting affine line, charge at most `Q` slopes,
and repeat on the residual family.  Its common core has size at least

```text
g=max(0,ceil((lambda*m-N)/(lambda-1))),
```

and at least `u=max(g-c,0)` of those coordinates lie in the gauged direction
support.

The affine lines peeled at distinct stages are distinct.  Their inside-core
sets `I_i` satisfy

```text
|I_i|>=u_i,             |I_i intersect I_j|<=c,
sum_i u_i-C(r,2)c <= e.                              (RP)
```

Thus a strict violation of `(RP)` contradicts the assumed unsafe family.
Alternatively, common-core absorption lowers the residual deficit ceiling,
after which the exact suffix-minimum prefix pays the remainder.

An exact replay proves every support

```text
124806<=e<=130198.
```

Of the `5,393` supports, `3,837` terminate with a weighted-prefix bound and
`1,556` terminate with the multi-line core-packing contradiction.  At most
five affine lines are peeled.  At adjacent `e=130199`, the certified base
charge exceeds the residual budget after nine peels before another line can
be forced; this is a method wall, not an unsafe certificate.
