# Proof

Let the four light coefficient positions be the vertices of the six
unit-product chords. The profile `(1,8)` has exactly one odd autocorrelation
coefficient. By the parity identity in the profile reduction, exactly one of
the six light-light chords is a diameter and the other five chords occupy
distance classes with exactly one class of odd multiplicity.

Translate the diameter endpoints to `0` and `64`, and call the remaining
light positions `x,y`. For a non-quarter point `z`, the two chords from `z`
to the diameter endpoints occupy the complementary pair

```text
P_z={||z||,64-||z||}.
```

If neither `x` nor `y` is a quarter point, the parity support of the five
non-diameter chords is

```text
P_x symmetric_difference P_y symmetric_difference {||x-y||}.
```

Two distinct complementary pairs have disjoint two-element supports. Hence
this expression has weight one only if `P_x=P_y`. Excluding the second
diameter, this gives `y=-x` or `y=64-x`. These are two distinct affine-unit
families. In each family odd units act transitively on elements of each fixed
2-adic valuation, and `x=32` is excluded, leaving representatives

```text
x=1,2,4,8,16                                           (2)
```

If one remaining light point is a quarter point, take it to be `32`. Its two
endpoint chords both have class 32 and cancel in parity. Thus
`||y-32||` must be one of the two endpoint distances of `y`. The four
solutions are `y in {16,48,80,112}`, one orbit under odd units and the
diameter stabilizer. This gives `{0,16,32,64}`. Two quarter points would form
a second diameter. Together with both five-member families above, this proves
that (1) is exhaustive. The verifier also
reconstructs this classification by enumerating every normalized light
support.

For each of the eleven representatives, the production census chooses the three
heavy positions from the other 124 positions. Multiplying all seven
coefficients by `-1` changes no chord product, so fixing the first heavy sign
positive leaves exactly 64 sign patterns. The exact coverage is therefore

```text
11 * binom(124,3) * 64 = 218,327,296.                  (3)
```

The census forms every signed folded chord coefficient, retains exactly one
coefficient of magnitude one and eight of magnitude two, and evaluates the
weighted zero-sum count defining `M_3`. Its complete per-template ledger is

```text
template                      profile vectors   max M_3
{0,64,+/-1}                       112              912
{0,64,+/-2}                       560             1200
{0,64,+/-4}                       856             1284
{0,64,+/-8}                       592             1248
{0,64,+/-16}                        0               --
{0,64,1,63}                      3280              864
{0,64,2,62}                      2992              864
{0,64,4,60}                      3504             1284
{0,64,8,56}                      3824             1356
{0,64,16,48}                      704             1296
quarter-octant                   720             1188
total                          17144             1356. (4)
```

An independent implementation forms `F(X)F(X^-1)` directly in
`Z[X]/(X^128+1)`, checks the anti-palindromic coefficients, and repeats all
of (3). It reproduces every entry of (4). Thus every actual profile-`(1,8)`
geometry has `M_3<=1356`.

The proved profile reduction gives the exact cubic-Hermite safe boundary
`M_3=1732` at `V=66`; its norm margin is strict there. Since
`1356<1732`, every candidate has collision norm below `2^250`, contradicting
pair feasibility. QED.
