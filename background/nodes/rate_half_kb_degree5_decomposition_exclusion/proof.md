# Proof

In the `m=5` row, the outer map has degree 12 with two order-five poles and
two simple poles. Above each simple outer pole, equation

```text
e_h r=5
```

forces one source point with `e_h=5`. These two points contribute
`2*(5-1)=8` to the ramification divisor of the degree-five map `h`. This is
the full Riemann-Hurwitz degree `2*5-2=8`; there is no other ramification.

Call the two points `x_0,x_infinity`. They are distinct roots of the source
polynomial and hence lie in `K`. Their images are the two distinct simple
poles of the outer map. Choose `phi in PGL_2(K)` sending them to `0,infinity`
and choose a target coordinate over the algebraic closure sending their
images to `0,infinity`. The normalized degree-five map `g` then has

```text
div(g)=5[0]-5[infinity].                             (KB5-1)
```

Therefore `g(x)=c x^5` for some nonzero geometric scalar `c`. Target
normalization and `c` do not change equality of values. For any two points
`x,y in P^1(K)`, therefore,

```text
h(x)=h(y)  iff  phi(x)^5=phi(y)^5.                  (KB5-2)
```

Now `p=2130706433` is `3 mod 5`, so `p^6=4 mod 5` and
`gcd(5,p^6-1)=1`. The fifth-power map permutes `K^*`, and it also fixes
`0` and `infinity`; it is injective on `P^1(K)`. Equation `(KB5-2)` says
every `h`-fiber contains at most one `K`-point.

The proved divisor adapter gives the contradiction: the 12 simple outer
zeros each have a complete unramified `h`-fiber consisting of five distinct
active roots in `K`. Hence the `m=5` row is empty. QED.
