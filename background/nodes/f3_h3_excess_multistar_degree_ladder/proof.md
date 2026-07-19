# Proof

Swapping the two ordered product coordinates shows that the number of
unordered representations of `t` is

```text
U=(P+D)/2.                                          (1)
```

The rich-fiber norm-cutoff theorem proves that a representation can have
squared coefficient norm greater than three only if it is diagonal or
contains the root `-1`. There are exactly `D` diagonal representations and at
most one representation containing `-1`, because its other shifted factor is
forced by `2(1-y)=t`. Removing their union from `(1)` gives

```text
m>=U-D-1=(P-D)/2-1,
```

which is `(EML1)`. This subtraction is conservative when `{-1,-1}` belongs to
both exceptional classes.

Now take all `m` small coefficient vectors. Distinct unordered root pairs give
distinct vectors by the characteristic-zero shifted-product Sidon theorem.
Their pairwise squared distances are even, and distance two is impossible in
one odd-prime product fiber by the proved 2-primary exclusion. Let `a` and `b`
count distances four and six. Every other distance is at least eight. The
centroid identity gives

```text
4a+6b+8(C(m,2)-a-b)
  <= sum_(E<F)||v_E-v_F||^2
   = m sum_E ||v_E||^2-||sum_E v_E||^2
  <=3m^2.
```

Writing `W=2a+b` and rearranging yields

```text
2W>=m(m-4),
```

which proves `(EML2)`. The weighted handshake identity gives

```text
m Delta>=2W>=2 ceil(m(m-4)/2).
```

Taking ceilings proves the first form of `(EML3)`. If `m` is even then
`m(m-4)` is even and the expression is `m-4`. If `m` is odd then
`m(m-4)` is odd, so the extra half-unit makes the final ceiling `m-3`. This
proves the displayed parity form.

Suppose now that `P=18+e`. The swap identity forces `P` and `D` to have the
same parity. If `e` is odd, then `D<=1`; if `e` is even, then `D<=2`.
Substitution in `(EML1)` gives in both cases

```text
m>=7+ceil(e/2),
```

proving `(EML4)`. The function `L(m)` is nondecreasing, so `(EML3)` implies
`(EML5)`. Its values at `m=8,9,11` are `4,6,8`, which gives the stated excess
thresholds.

If no center has weight six, then `(EML5)` forces `e<=2`. At `e=1`, parity
forces `D=1`. At `e=2`, the case `D=0` would improve `(EML1)` to `m>=9` and
hence force weight six, so only `D=2` remains. This proves `(EML6)`.

Finally choose a minimal set of edges at a guaranteed center whose weights
sum to the asserted threshold `L`. Since every positive edge has weight one
or two, the set contains between `ceil(L/2)` and `L` leaves. The normalized
multistar ideal argument already proved in
`f3_h3_weighted_multistar_router` applies verbatim: all generators vanish at
the same degree-one row prime, so the row prime divides the ideal norm, and
odd dilation reduces the complete sieve to one fixed primitive root. QED.
