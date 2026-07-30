# Proof

At the finite source branch point, `W=X^2=0` and

```text
H(T,0)=U(T,0)~q(T).
```

Let `r,s` be the two projective roots of the reduced quadratic `q`. These
are exactly the endpoint rows vanishing at `X=0`. The complete-source row
compiler supplies

```text
H(alpha_i,X) divides B(X)/z_i(X) divides B(X)
```

for every endpoint label `alpha_i`, together with

```text
sum_i div H(alpha_i,X)=2 div B(X).
```

The ramified source pole has `ord_0(B)=2`. Since `r,s` are different from
the source label at this pole, their row divisibility retains the full
order-two factor at zero. Hence

```text
ord_0 H(r,X)<=2,       ord_0 H(s,X)<=2.             (1)
```

No other row vanishes at zero because `H(T,0)~q(T)`. Local saturation gives
the sum of the two orders as `2 ord_0(B)=4`. The two upper bounds in `(1)`
force both orders to equal two.

For either root `j in {r,s}`, expand

```text
H(j,X)=U(j,X^2)+X V(j,X^2).
```

The constant term vanishes because `q(j)=0`; exact order two forces the
linear coefficient `V(j,0)` to vanish. Thus the quadratic `V(T,0)` vanishes
on both roots of `q`, so `V(T,0) in <q>`. If it were zero, evaluation at
`W=0` in the reciprocal three-dimensional `V` space would give `V=0`,
making `H(T,X)=H(T,-X)` and contradicting source-deck distinction. This
proves `(KBRC-1)`.

At `W=0`, evaluation of both the reciprocal `U` space and reciprocal `V`
space onto endpoint quadratics is surjective. Membership of each value in
the fixed line `<q>` has rank two, and the `U,V` variables are disjoint.
The total rank is four, leaving dimensions `8-4=4` and `7-4=3`. This proves
`(KBRC-2)`.

Finally normalize `V(T,0)=q(T)`. Solving the reciprocal coefficient
relations gives `(KBOI-2)` with `w=0`; its denominator proof uses only
`J_0 intersect J_1=empty` and remains valid. The internal orbit is
unramified and supplies `V(a,z)=0` by the first parent, so `(KBOI-3)`
follows unchanged. QED.
