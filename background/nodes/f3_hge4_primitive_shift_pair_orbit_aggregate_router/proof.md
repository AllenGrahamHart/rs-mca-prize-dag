# Proof

Let an element `gamma in H` stabilize an ordered primitive pair `(P,Q)`.
Then `gamma P=P` and `gamma Q=Q`. If `gamma!=1`, its order `c` is a divisor
of `n` with `c>=2`. The cyclic group `H` has a unique subgroup of order `c`,
namely `<gamma>`. Both `P` and `Q` are unions of its orbits.

The quotient map `x->x^c` has kernel `<gamma>`. Every orbit is a complete
fiber of this map, so the two locators have the form

```text
L_P(X)=A_c(X^c),       L_Q(X)=B_c(X^c).
```

The pair is therefore a pullback at the common quotient scale `c`, contrary
to primitivity. The stabilizer is trivial. Orbit-stabilizer now gives orbit
size `n`, proving `(OAR1)`.

Within one free ordered orbit, `1` lies in the left support precisely after
scaling by `x^(-1)` for one of the `h` distinct elements `x in P`. These
scales are distinct, and no other scale puts `1` in the left support. Hence
each orbit contributes exactly `h` left-anchored representatives, proving
`(OAR1a)`.

The aggregate adapter proves `N_h^strip<=SP_h^prim`. Summing `(OAR1)` gives

```text
sum_h N_h^strip<=n sum_h O_h^prim.
```

Thus `(OAR2)` implies the binding `14n^3` norm-gate budget.

Substitution of `(OAR1)` into

```text
SP_h^prim<=7000n max(1,B_h)
```

and cancellation of `n` proves the equivalence `(OAR3)`.

It remains to prove `(OAR4)`. Since `p>=n^2`,

```text
Fbar_h
 <=n^h/(h! n^(2h-2))
 =n^(2-h)/h!
 <=1/(24n^2)<1.                                   (1)
```

Likewise

```text
B_h<M_h^2/p^(h-1)<=n^2/(h!)^2<=n^2/576.           (2)
```

For `4<=h<=n/2`, binomial monotonicity gives

```text
M_h>=binom(n,4).
```

At `n=8192`, exact expansion gives

```text
binom(n,4)>7000n(1+n^2/576).                       (3)
```

After multiplying by `576/n`, the difference in `(3)` is

```text
f(n)=24(n-1)(n-2)(n-3)-7000n^2-4032000.
```

It is positive at `8192`, and

```text
f(n+1)-f(n)=72n^2-14216n-6856>0
```

thereafter. Combining `(2),(3)` proves

```text
7000n max(1,B_h)
 <=7000n(1+B_h)
 <M_h.
```

Finally, if `d_h(P)` is the number of primitive partners of `P`, then
`SP_h^prim=sum_P d_h(P)`. A proof using only `d_h(P)<=D_h` and
`SP_h^prim<=M_hD_h` would need

```text
D_h<=7000n max(1,B_h)/M_h<1.
```

For an integer uniform degree bound this says `D_h=0`, proving the stated
route separation. QED.
