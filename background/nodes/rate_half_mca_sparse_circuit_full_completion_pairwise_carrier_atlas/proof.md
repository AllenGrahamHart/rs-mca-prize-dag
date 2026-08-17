# Proof

Write `v_x` for evaluation at `x` as a functional on the ten-dimensional
correction space `V`.  Empty common zero set makes every `v_x` nonzero.  An
attaining support-two deletion is one point with projective class `P`; all
and only ground evaluations parallel to it complete a two-circuit.  Thus
`B_2` is the full parallel class and has size `M_2+1`.

Fix an attaining support-`c` deletion `A_c`, its rank-`c-1` span `F_c`,
and annihilator `H_c` of dimension `11-c`.  If `P` is outside `F_c`, then
`B_2` and `B_c` are disjoint and Grassmann gives

```text
dim(H_2 intersect H_c)>=9+(11-c)-10=10-c.
```

This is `T_c`.  If `P` lies in a proper deletion span, then `H_c<=H_2`.
There is at most one shared point, because two points of `B_2` already form
a two-circuit inside a purported support-`c` circuit.  If there is no shared
point, discard one point from the larger vanishing union.  In either case
the conservative `(b_2+|B_c|-1,11-c)` charge holds, giving `A_c`.

In the remaining position, `P` lies in `F_c` but in no proper deletion
span.  Every point of `B_2` completes `A_c` to a minimal support-`c`
circuit.  Hence `M_c>=|B_2|=M_2+1` and `B_2 subset B_c`, proving `F_c`
and `(CA1)`.

Now assume `F_3` and `F_d`.  Carrier sizes give

```text
|B_3\B_2|=(M_3+2)-(M_2+1)=r_3,
|B_d\B_2|=(M_d+d-1)-(M_2+1)=r_d.
```

Choose any `p in B_2`.  The set `A_d union {p}` is a minimal
support-`d` circuit.  Its deletion anchors cannot contain two points in the
rank-two flat spanned by `B_3`: together with `p` they would form a
dependent proper subset.  Therefore at least `d-2` anchors lie outside that
flat and hence outside `B_3`.  Thus

```text
|(B_d\B_2)\B_3|>=d-2,
```

which is equivalent to `t<=r_d-(d-2)=M_d-M_2`.  The other bound
`t<=r_3` is immediate, proving `(CA2)` and the union size in `(CA3)`.

Both `H_3` and `H_d` lie in the nine-dimensional `H_2`.  If `t=0`,
Grassmann inside `H_2` gives dimension

```text
8+(11-d)-9=10-d.
```

If `t>0`, a shared point outside the full parallel class `B_2`, together
with `P`, spans the rank-two `F_3`.  Since both points lie in `F_d`, we have
`F_3<=F_d`, hence `H_d<=H_3`; the full `11-d` dimensions vanish on the
union.  This proves `(CA3)`.  Applying the argument independently for
`d=4` and `d=5` proves Cartesian-product exhaustiveness. QED.
