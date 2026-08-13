# Proof

Minimality makes both coefficient families linearly independent. A common
zero of all `B_j` inside `U_0` would make the corresponding row
polynomial identically zero. A common zero outside `U_0` would root all
`3e` parameter fibers, but the norm divisor outside `U_0` has degree
only `2e-7<3e`. The same homogeneous argument treats infinity. Hence
`b` is basepoint-free. The pure split fibers have exact degree `n`, so

```text
b^*O(1)=O_(P^1)(n).                                 (1)
```

If `d_X` is the degree onto the normalization of the image, pullback of a
generic hyperplane gives `d_X|n`.

Fix `x in U_0` and factor `b` through the normalization of its image.
Choose one of the `m` slopes `delta` incident to `x`. The corresponding
hyperplane contains `b(x)`, so `G(delta,X)` vanishes on the complete
scheme-theoretic normalization fiber through `x`. Its actual-support
factorization has a simple root at every point of that fiber which lies in
`U_0`. Thus all `U_0` points in the fiber are unramified. This conclusion
holds using each of the `m` incident slopes.

If a point `y` of ramification index `h_y` in this fiber lies outside
`U_0`, then

```text
G(delta,y)=0
```

for all `m` distinct incident slopes. Each pullback vanishes to order at
least `h_y`, so `y` contributes at least `m h_y` to the homogeneous divisor

```text
N(X)/L_U0(X)^m,
N(X)=product_(delta in Gamma)G(delta,X).            (2)
```

The concentrated norm identity gives its exact degree

```text
3en-Rm=2e-7=2m-3.                                  (3)
```

Two units of scheme-theoretic outside fiber degree would consume at least
`2m`, contradicting `(3)`. Across all normalization fibers meeting `U_0`,
the total outside fiber degree is therefore at most one.

The fibers partition `U_0`, and every inside point has degree one. If the
outside fiber degree is zero, every class has size `d_X`, so `d_X|R`. If it
is one, exactly one class has `d_X-1` points in `U_0`, while every other
class has `d_X`; hence `d_X|(R+1)`. This proves `(DBR3)`.

Finally `R=3n+7`, so

```text
gcd(n,R)=gcd(n,7)=1.                                (4)
```

Also `n=274877906941` is odd, and

```text
gcd(n,R+1)=gcd(n,8)=1.                              (5)
```

Combining `d_X|n` with either `(4)` or `(5)` forces `d_X=1`. QED.
