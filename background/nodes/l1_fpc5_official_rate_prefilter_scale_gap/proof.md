# Proof: official-rate prefilter scale gap

Fix one row and scale in `(SG1)`. The three upper endpoints satisfy

```text
M<=4(R-1).
```

Since `k/4` is an integer on every official row,

```text
ell=floor(((R-1)k+1)/M)>=k/4.                         (1)
```

For a touched-petal count `t>=4`, put `h=t ell`. Then `(1)` gives
`h>=k=N+1`. The ordinary Johnson condition in `(PF6)` would require

```text
d^2<=N(2d-h).
```

But

```text
d^2-N(2d-h)=(d-N)^2+N(h-N)>0.                        (2)
```

Thus only `t=2,3` can survive.

For either remaining value of `t`, every condition in `(PF6)` except the two
Johnson conditions puts `d` in the exact integer interval

```text
L=ceil(t ell/2),
U=min {
  ell(M-2)-1,
  N,
  (t-1)ell+b,
  floor((N+(t-2)ell+b)/2)
}.                                                    (3)
```

If `t ell>N`, equation `(2)` again makes the interval empty. Otherwise,
because `(3)` has `d<=N`, the ordinary Johnson condition is equivalent to

```text
(N-d)^2<=N(N-t ell),
d>=N-floor(sqrt(N(N-t ell))).                         (4)
```

Intersect `(3)` with `(4)`. Put `c=(t-1)ell`. Values `d<c` have `u<0` and
need no joint-background test. If `b=0`, the same is true of the only
possible nonnegative-`u` endpoint. In the remaining branch `d>=c`, `b>0`,
the last condition in `(PF6)` is

```text
G(d)=(N+b)d^2-2N(c+b)d+N(c^2+b t ell)<=0.             (5)
```

For integer `d`, `(5)` is decided exactly from

```text
4(N+b)G(d)
  =(2(N+b)d-2N(c+b))^2-Delta,
Delta=4N^2(c+b)^2-4(N+b)N(c^2+b t ell).              (6)
```

Equations `(3)--(6)` are constant-time integer tests for each row, scale,
and `t`. The primary verifier exhausts all 4,608 `t in {2,3}` cells using
the exact square-root interval in `(6)` and checks all 55,296 `t>=4` cells
using `(2)`. It finds no survivor in `(SG1)`. An independent verifier uses
a binary search for `(4)` and a convex integer minimization of `(5)`, again
finding none.

Finally, direct substitution checks every `(PF6)` inequality for the three
printed boundary tuples. Therefore the three low-rate cutoffs are exact for
the stated prefilter. QED.
