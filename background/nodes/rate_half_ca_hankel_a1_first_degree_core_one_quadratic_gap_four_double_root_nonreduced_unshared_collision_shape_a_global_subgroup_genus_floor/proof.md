# Proof

The shape-A pure-split theorem makes `G` absolutely irreducible of exact
bidegree `(m,n)`. Hence on its normalization `C`, the parameter coordinate
has degree `n` and the row coordinate has degree `m`.

For every one of the `R` classified rows `x`, the proved dual-MDS biform
reduction gives

```text
G(t,x)=lambda_x product_(delta in A_x)(t-delta),
lambda_x!=0,       |A_x|=m,       A_x subset H,     (1)
```

with distinct roots. Also `x in H`. Every pair `(delta,x)` in `(1)` is a
smooth point of `G=0`, because `delta` is a simple root of the row
polynomial. It therefore gives one distinct point on `C`. Thus

```text
# {z in C:t(z) in H, X(z) in H} >= Rm=P.           (2)
```

We next check the multiplicative-independence hypothesis. If `t` and `X`
were multiplicatively dependent modulo constants, the image of `C` in the
two-dimensional torus would be a translated subtorus. Its primitive
binomial equation would have bidegree `(m,n)`. For fixed `delta in H`, its
row equation would therefore have the form

```text
X^n=c delta^(+/-m).                                (3)
```

Now `N` is a power of two and `n=2^38-3` is odd, so `gcd(n,N)=1`.
Equation `(3)` has at most one solution in `H`. The pure-split theorem
supplies a parameter fiber with `n>1` distinct roots in `H`, a
contradiction. Hence `t` and `X` are multiplicatively independent modulo
constants.

Apply the audited Corvaja--Zannier positive-characteristic gcd theorem on
`C` to

```text
u=t^N,       v=X^N.                                (4)
```

The characteristic exceeds `2^167>N,m,n`, so both differentials are
nonzero. Their degrees are `Nn` and `Nm`. Every point counted in `(2)`
lies outside the zero and pole set and contributes at least one to the gcd
sum. Consequently

```text
P <= max{
  3(2N^2mn chi_C)^(1/3),
  12N^2mn/P_char
}.                                                 (5)
```

Exact arithmetic gives

```text
12N^2mn<2^167<P_char,                              (6)
```

so the second term in `(5)` is less than one. The first term must carry
`P`. Cubing and rearranging gives

```text
chi_C>=ceil(P^3/(54N^2mn))
     =262353693488940318721.                       (7)
```

The zero and pole supports of a degree-`d` rational function contain at
most `2d` points. Therefore the union `S` for `t` and `X` satisfies

```text
|S|<=2n+2m.                                        (8)
```

Using `chi_C=|S|+2g(C)-2`, equations `(7)--(8)` imply

```text
g(C)>=ceil((262353693488940318721-2(m+n)+2)/2)
    =131176846286340314460.                        (9)
```

This proves `(SGF3)--(SGF5)`. QED.
