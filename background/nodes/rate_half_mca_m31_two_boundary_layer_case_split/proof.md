# Proof

Let `A` be the explanations of deficit greater than `H`; choose for each
one an inside agreement set of its layer size, whose missed-set size is at
most `s`.  Let `D_1` and `D_2` be the exact layers of deficits `H` and
`H-1`.  Choose an `H`-set or `(H-1)`-set from the corresponding inside
agreements.  Their missed sets then have exact sizes `s+1` and `s+2`.
Every member of `A union D_1 union D_2` owns at most one selected slope
because `2(s+2)<e`.

## At least two top anchors

Suppose `|A|>=2` and fix two anchors in `A`.  For any member of either
boundary layer, the smallest guaranteed mixed triple intersection is

```text
e-s-s-(s+2)=K+q-2=K.
```

Restriction injectivity therefore puts `A union D_1 union D_2` on the same
affine codeword line.  Pair noncontainment and total-core line packing bound
this union by `t+1`.  The remaining deficits are at most `H-2`, giving

```text
P_(H-2)+(t+1).                                          (1)
```

## Exactly one top anchor

Suppose `A={a}`.  If `|D_1|>=2`, any two members of `D_1` have with `a` a
triple intersection of size at least

```text
e-s-(s+1)-(s+1)=K+q-2=K.
```

Fixing two members shows that all of `D_1` lies on one affine codeword line.
Charge `a` separately.  Every member of `D_1` has exactly `m-H` outside
agreements, so the outside-core line-packing theorem gives

```text
|D_1|<=Q=floor((n-c)/(m-H-c)).
```

Together with the prefix through `H-1`, this is
`P_(H-1)+Q+1`.  If instead `|D_1|<=1`, charge the two exceptional members
directly and obtain `P_(H-1)+2`.

## No top anchor

Now suppose `A` is empty.  For each member `i` of `D_1`, let `R_i` be its
missed set in the direction support, so `|R_i|=s+1`.  If some pair
`R_a,R_b` intersects, then for every third member `j`,

```text
|S_a intersect S_b intersect S_j|
 = e-|R_a union R_b union R_j|
 >= e-(3(s+1)-1)
  = K+q-2
  = K.
```

The fixed pair `a,b` therefore synchronizes all of `D_1` onto one affine
line, and outside-core packing gives `P_(H-1)+Q`.

Otherwise the missed sets are pairwise disjoint.  Then

```text
|D_1|(s+1)<=e,
```

so `|D_1|<=D=floor(e/(s+1))` and the bound is `P_(H-1)+D`.

The five displayed alternatives are exhaustive, proving `(BA2)`.  Exact
evaluation gives the printed official values.  At the next support the
division `e-K=3s+q` has `q=0`, so the residue-two hypothesis correctly
rejects it.
