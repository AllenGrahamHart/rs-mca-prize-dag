# Proof - reciprocal-quadratic PMA obstruction

Put `N=n/2`, let `G` be the subgroup of order `N`, and let `A=H\G`. Since
`n` is a power of two and `N` is even, `-1 in G`; hence `A` is a union of
antipodal pairs. Fix `r in A` and define

```text
Q(x)=x^(-1)+rx.
```

This function is nonzero and injective on `A`. Indeed, `Q(x)=0` would give
`r=-x^(-2) in G`. For distinct `x,y in A`, equality `Q(x)=Q(y)` gives
`r=(xy)^(-1) in G`, again impossible because `xy in G`.

Choose one point from every antipodal pair in `A`; call the resulting set
`X`, and put `Y=-X`. Thus `|X|=|Y|=M=N/2`. A bijection `pi:X->Y` will later
define the sunflower petals, and the label of `{x,pi(x)}` is `Q(x)`. The
labels are therefore distinct and nonzero.

Fix a five-set `S subset X`. Its product lies in `A`, so

```text
t_S=r product(S) in G.
```

Let `D` be a three-subset of `G` with product `t_S`. With monic locators
`L_D,L_S`, put

```text
P(X)=1+rX^2,
W(X)=(P(X)L_D(X)-rL_S(X))/X.                           (1)
```

The numerator in `(1)` has zero constant term because

```text
L_D(0)=-product(D)=-r product(S),
L_S(0)=-product(S).
```

Its degree-five terms also cancel. Therefore `W` is a polynomial of degree
at most three. For every `x in S`,

```text
W(x)=P(x)L_D(x)/x=Q(x)L_D(x).                          (2)
```

For `x in X\S`, the difference in `(1)` is `rL_S(x)!=0`, so `(2)` fails.
At every `d in D`,

```text
W(d)=-rL_S(d)/d!=0.                                    (3)
```

We next count triples. For any `t in G`, choose ordered distinct `d_1,d_2`;
then `d_3=t/(d_1d_2)` is forced. Of the `N(N-1)` choices, at most `N` have
`d_3=d_1` and at most `N` have `d_3=d_2`. Hence the number of unordered
distinct triples of product `t` is at least

```text
N(N-3)/6.                                               (4)
```

The background can be chosen without losing the exponent. For fixed `(S,D)`,
the nonzero cubic `W` has at most three roots in `G`. Among the `N-3` choices
`b in G\D`, at least `N-6` satisfy `W(b)!=0`. Summing over all `S,D` and
averaging over `b in G`, there is one background for which at least

```text
binom(M,5)(N-6)(N-3)/6                                 (5)
```

pairs `(S,D)` satisfy `D subset C=G\{b}` and the exact-background condition.

Fix this `b`. For a pair counted in `(5)`, choose `pi:X->Y` uniformly. A
selected petal at `x in S` becomes full only if `pi(x)` is another root of

```text
W(Z)-Q(x)L_D(Z).
```

This nonzero cubic already has root `x`, so it has at most two roots in `Y`.
The union bound over five selected points costs at most `10/M`.

We also force aperiodicity. The point `-x` lies in `Y`; its petal label is
`Q(pi^(-1)(-x))`. Since `Q` is injective on `X`, agreement at `-x` forbids
at most one preimage under `pi`. Over the five points this costs at most
`5/M`. Consequently the expected fraction for which no selected petal is
full and every selected `x` has nonagreeing antipode is at least

```text
1-15/M.                                                 (6)
```

Some bijection realizes at least the expectation. Every unselected petal has
its `X`-endpoint outside `S`, so `(2)` fails there and it cannot be full.
Thus all surviving objects are diffuse. Their agreement supports are not
invariant under `x->-x`; every nontrivial subgroup of the cyclic two-group
`H` contains `-1`, so their stabilizers are trivial.

Finally define the planted sunflower word to be zero on `C union {b}=G` and
`Q(x)L_C` on the petal `{x,pi(x)}`. For every surviving `(S,D)`, set

```text
f=L_(C\D)W.
```

Its degree is at most `(k-4)+3=k-1`. Equations `(2)` and `(3)`, together with
`W(b)!=0`, show that `f` is an actual exact `(d,r)=(3,0)` non-planted source
codeword, not merely an auxiliary-list element. The missed core recovers
`D`, and `(1)` recovers `S` once `D,W` are fixed, so all counted codewords are
distinct. Multiplying `(5)` by `(6)` and taking the integer floor proves
`(RQ-LB)`.

The final official-row inequality is exact integer arithmetic replayed by
`verify.py`.
