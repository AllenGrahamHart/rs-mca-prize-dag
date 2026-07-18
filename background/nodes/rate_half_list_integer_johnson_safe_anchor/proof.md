# Proof

Assume for contradiction that `ell=B+1` distinct codewords are listed at
agreement `a`. For each codeword choose an `a`-point subset `S_i` of its
agreement set. Two distinct degree-`<k` polynomials agree on at most `k-1`
evaluation points, so

```text
sum_(i<j)|S_i intersect S_j| <= binom(ell,2)(k-1).       (1)
```

For each coordinate `x`, let `d_x=#{i:x in S_i}`. Double counting gives

```text
sum_x d_x=ell*a,
sum_(i<j)|S_i intersect S_j|=sum_x binom(d_x,2).         (2)
```

If two integer degrees satisfy `d_x>=d_y+2`, replacing them by
`d_x-1,d_y+1` reduces the last sum by `d_x-d_y-1>0`. Hence its exact minimum
at fixed total `ell*a=n*d+r` has `n-r` coordinates of degree `d` and `r`
coordinates of degree `d+1`. Therefore

```text
sum_x binom(d_x,2)
 >=(n-r)binom(d,2)+r binom(d+1,2)
 =n binom(d,2)+r*d.                                    (3)
```

If `J_(n,k,B)(a)>0`, equations `(1)` and `(3)` contradict each other. Thus
no `B+1` distinct codewords are listed and `L_1(a)<=B`, proving `(IJ2)`.

Increasing the incidence total by one increases the balanced minimum in
`(3)` by `floor((ell*a)/n)`. It is therefore nondecreasing as `a` increases.
At `a=n`, all degrees are `ell` and

```text
n binom(ell,2)> (k-1)binom(ell,2),
```

so the set in `(IJ3)` is nonempty. Binary search proves the computation claim
and `(IJ4)`.

For an official rate-half row, use `B=B*`. The proved cyclic floor gives the
left side of `(IJ5)`, while `(IJ4)` gives the right side.

Finally, direct substitution into `(IJ1)` at `a=3n/4` and `a-1` proves the
first line of `(IJ6)` for `B=1,2,3`.
For the second, let

```text
a_0=floor(sqrt(n(k-1)))+1.
```

The exact bigint evaluation at `n=2^41,k=2^40` shows

```text
J_(n,k,332114441761)(a_0)<=0,
J_(n,k,332114441762)(a_0)>0.
```

No smaller `a` can be certified by `(IJ1)`: its smooth Johnson denominator
`a^2-n(k-1)` is nonpositive. Indeed, choose `ell` independent uniform
`a`-subsets of an `n`-set. Their expected total pair intersection is

```text
binom(ell,2) a^2/n.
```

The balanced expression in `(3)` is a lower bound for every realization and
therefore cannot exceed this expectation. If `a^2<=n(k-1)`, it is at most
`binom(ell,2)(k-1)`, so `(IJ1)` is nonpositive. This rules out every
agreement below `a_0` for every budget.

It remains to cover all larger budgets at `a_0` without assuming monotonicity
through the integer remainders. Put `c=k-1`,
`delta=a_0^2-nc=3015547699344`, and write `ell*a_0=n*d+r`. Expanding the
balanced expression exactly gives

```text
J_(n,k,B)(a_0)
 =ell(ell*delta-n(a_0-c))/(2n)+r(n-r)/(2n).        (4)
```

The first term is positive for
`ell>=332114441764`, hence for every `B>=332114441763`. The one remaining
budget `B=332114441762` is the exact positive comparison displayed above.
This proves the second line of `(IJ6)`. The verifier reproduces all boundary
comparisons exactly. QED.
