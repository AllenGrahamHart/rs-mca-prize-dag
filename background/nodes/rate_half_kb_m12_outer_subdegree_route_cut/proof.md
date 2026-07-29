# Proof

The source-pencil compiler descends a target transform of the inner map and
the outer map to `K`. In the `m=12` profile the outer degree is five and its
pole divisor consists of one point `P` of order five. Since the map is
defined over `K` and the pole is unique, `P` is `K`-rational. Its zero
divisor consists of five distinct points: each is the common `h`-value of a
complete 12-point active fiber, so each lies in `K`.

The transverse image `C` is an irreducible non-diagonal component of
`F(Y)=F(Z)` of bidegree `(r,r)`. Because degree five is prime, `F` is
indecomposable; its separable geometric monodromy is primitive. Irreducible
self-correspondence components are point-stabilizer suborbits. The complete
primitive degree-five rows are

```text
(1,1,1,1,1),       (1,2,2),       (1,4),
```

with repetitions for the five primitive groups. None has subdegree three,
so `r=3` is impossible.

If `r=1`, `C` is the graph of a nonidentity Mobius transformation `sigma`
with `F composed sigma=F`. The automorphism group embeds in the degree-five
function-field extension, so its nontrivial subgroup has order five and the
cover is cyclic. In characteristic different from five, a cyclic
degree-five cover of `P^1` has exactly two totally ramified points. One is
the unique pole `P`; call the other `Q`. The ramification divisor is defined
over `K`, and after removing the unique rational point `P`, the remaining
unique point `Q` is also `K`-rational.

Choose `phi in PGL_2(K)` sending `Q` to zero and `P` to infinity. The value
`F(Q)` belongs to `K`. The divisor of `F-F(Q)` in this coordinate is

```text
5[0]-5[infinity].                                  (KB12-2)
```

Hence `F(phi^(-1)(x))=a x^5+b` with `a in K^*` and `b in K`.

Now `p=2130706433=3 mod 5`, so `p^6=4 mod 5` and
`gcd(5,p^6-1)=1`. Fifth power permutes `K`. If `b=0`, the zero at zero has
multiplicity five; if `b!=0`, the equation `a x^5+b=0` has exactly one
solution in `K`. Both contradict the five distinct simple `K`-rational
zeros of `F`. Thus `r=1` is impossible, leaving exactly `(KB12-1)`. QED.
