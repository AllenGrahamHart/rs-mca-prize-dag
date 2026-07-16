# Proof

In the extension-list notation, the one loop is a coordinate where every
kernel word vanishes but which is not persistent on the whole affine family.
At that coordinate a selected error has the form

```text
b(x)+gamma q(x).
```

Two distinct slopes cannot both make this zero: otherwise `q(x)=b(x)=0`,
making the coordinate persistent. Thus at most one selected member agrees at
the loop.

Before deletion every member has at least `5+h` agreements. Delete the loop
and the possible member agreeing there. Every remaining member still has at
least `m=5+h` agreements, while the number of remaining members is at least
`B`. The P-B pair cap is `3+u+v=4` and deletion cannot increase it. With
`u=0`, the normalized kernel is exactly `GRS_4`, proving (D1).

Apply the multiplicity-sensitive peeling argument with comparison budget
`B-1`. The regular family has size at least `B`, hence greater than that
budget. A four-set can be charged at most `r-1` times, and the same
delete-all contradiction gives

```text
d_r=C(m,4)-floor((r-1)C(N,4)/B).
```

The Vandermonde kernel makes every four-set a basis. Members sharing one lie
on its exact collision line, and the pair cap four makes different four-sets
through one member define different lines. This proves the rich-line claim.

At `r=2`, a retained member has at most

```text
floor(C(N,4)/B)=1,3,4
```

unreused four-sets on the three rows. If `[S]q=0` on a selected five-set,
then for every four-set `T subset S` the direction `q-I_Tq` also vanishes at
the fifth point. Reuse of `T` would therefore give two selected members with
five common agreements, contradicting the pair cap. All five four-subsets of
`S` would be unreused, impossible because the displayed complements are
less than five. Hence every denominator is nonzero.

If the selected codeword is `gamma q+p`, with `deg p<4`, fourth divided
differences on its agreement set give

```text
[S]U=gamma[S]q.
```

This proves the monochromatic-clique claim. Newton interpolation also gives

```text
Phi(T union {x})-gamma=(U-c)(x)/(q-I_Tq)(x),
```

so equal-color stars are exactly the ratio fibers and maximal-minor zeros.

The interpolation hyperplanes `p(x)=q(x)` over one selected block are in
simple position: fourfold intersections are `I_Tq`, and the nonzero fifth
divided differences exclude fivefold concurrence. The star-configuration
evaluation bound says that a nonzero degree-`d` direction polynomial is
nonzero on at least `C(m-d,4)` of the `C(m,4)` directions. Comparing this
with complements `1,3,4` gives maximum excluded degrees `5,5,3`.

Finally, a line with `r` retained members gives `r-1` distinct external ratio
fibers of size at least `m-4=h+1`. Each contributes `C(h+1,2)` zero-minor
records per incident four-set. The external agreement sets of different line
members are disjoint, so the line population is at most
`floor((N-4)/(h+1))`. Maximizing

```text
d_r(r-1)C(h+1,2)
```

over the exact positive range in (D2) gives `97,650`, `52,530`, and `1,782`,
completing the reduction.
