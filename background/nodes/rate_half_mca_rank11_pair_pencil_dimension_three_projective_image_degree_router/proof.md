# Proof

Let `W_0` be the residual three-dimensional scalar direction space and put
`G=gcd(W_0)`. At a residual coordinate where `G` vanishes, every selected
scalar type evaluates to the same value. If that value agreed with the
received pair, the coordinate would belong to the already-shortened global
common received core. It does not, so its residual owner multiplicity is
zero.

At `q=3170`, the exact deficit from full 218-fold occupancy is

```text
Delta=218n'-3170s'=14709668-2952K'.                (1)
```

Every official-domain root of `G` spends 218 units of this deficit. Hence

```text
z:=|D' intersection Z(G)|<=floor(Delta/218).        (2)
```

This decreases from 310 to 12 on the 23 endpoint rows.

Now put `W=G^(-1)W_0`. Choose a basis `f_0,f_1,f_2` of `W` and let `d` be
the largest degree of a member of `W`. Homogenize the basis to degree `d`.
The three homogeneous forms have no common zero at a finite point because
`W` is primitive. They have no common zero at infinity because some member
of `W` has degree exactly `d`. They therefore define a
basepoint-free morphism

```text
phi:P^1 -> P^2,       x |-> [f_0(x):f_1(x):f_2(x)]. (3)
```

Let `C` be the scheme-theoretic image, let `c=deg C`, and let `e` be the
degree of the finite map from `P^1` to `C`. Pulling back a hyperplane gives

```text
phi^* O_C(1)=O_(P^1)(d).
```

Taking degrees proves

```text
d=e deg O_C(1)=ec.                                  (4)
```

The image is not a line: a line containing it would give a nonzero linear
relation among the basis polynomials. Hence `c>=2`, proving `(PI1)`.
This degree calculation includes inseparable degree. A geometric fiber has
at most `e` distinct points in every case.

At a full residual coordinate `x`, one has `G(x)!=0` by `(2)`, and
evaluation on `W_0` differs from evaluation on `W` by the nonzero scalar
`G(x)`. It is therefore represented by `phi(x)`. The direction space of its
affine owner plane is the kernel of that evaluation functional. Coordinates
with the same projective evaluation normal lie in one geometric fiber of
`phi`, even when their affine owner planes are parallel rather than equal.
Thus at most `e` full owner coordinates share one normal. If `N_full` is
the number of distinct normals among the `F_218` full coordinates, then

```text
N_full>=ceil(F_218/e).                              (5)
```

Write a represented direction polynomial as `G bar(T)`. The
direction-saturation theorem gives it at least `K'-2609` distinct
official-domain roots. Removing the at most `z` common roots leaves

```text
|Z_D'(bar(T))|>=K'-2609-floor(Delta/218).            (6)
```

This lower bound rises from 2,041 to 2,361 across the endpoint rows. The
primitive direction `bar(T)` is the pullback of one projective line under
`phi`, so in particular

```text
d>=2041.                                            (7)
```

Suppose first that `c=2`. The image is a geometrically integral conic. It
has a base-field rational point, for example the image of any base-field
point of `P^1`, so it is base-field isomorphic to `P^1`. Factor `phi`
through this isomorphism. The resulting degree-`e` self-map of `P^1` is
represented by coprime homogeneous forms `A,B` of degree `e`, and the conic
embedding is the quadratic Veronese map. After a base-field projective
change of target coordinates,

```text
[f_0:f_1:f_2]=[A^2:AB:B^2].                         (8)
```

Both triples are basepoint-free sections of `O_(P^1)(2e)`, so the
projective equality has only a nonzero constant proportionality factor.
This proves the asserted equality of homogeneous polynomial spaces. A
projective direction is a target linear form, and `(8)` pulls it back to a
binary quadratic in `A,B`.

Equations `(4)` and `(7)` give `2e=d>=2041`, hence `e>=1021`. More
precisely the row-wise lower bound is half the right side of `(6)`, rounded
up. The endpoint degree cap gives

```text
e=d/2<=floor((K'-1)/2)<=2490.                       (9)
```

Applying `(5)` with the largest allowed `e` on each row gives the exact
normal floors 398 at `K'=4960` and 422 at `K'=4982`.

Finally suppose `c>=3`. Equations `(2)` and the endpoint degree cap give

```text
e=d/c<=floor((K'-1)/3).                            (10)
```

Using

```text
F_218>=-13661092+2953K'
```

in `(5)` and evaluating the 23 integer rows proves the lower bounds 597
through 633 in `(PI3)`. QED.
