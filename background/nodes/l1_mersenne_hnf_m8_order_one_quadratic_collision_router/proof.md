# Proof - L1 Mersenne HNF m=8 order-one quadratic-collision router

Let `x,y` be the two roots in a repeated color `epsilon`. Every quadratic
fiber has root sum `S`, and the pointwise color equations give

```text
x+y=S,
x^p=epsilon/x,       y^p=epsilon/y,
xy=(C-epsilon)/A.                                    (1)
```

Taking the `p`th power of the first equation yields

```text
S^p(C-epsilon)=A epsilon S.                          (2)
```

If two distinct colors are repeated, subtract their equations in (2):

```text
S^p+A S=0,       C S^p=0.                           (3)
```

Assume first that `S!=0`. Then

```text
C=0,       A=-S^(p-1),       B=S^p,
x^p=E(x)/x=A x+B=:phi(x)                             (4)
```

for every root `x` of `L`, including singleton-color roots. Thus the affine
map `phi(W)=AW+B` carries the roots of `L` to the roots of `L^[p]`, and

```text
L^[p](phi(W))=A^6 L(W).                              (5)
```

The inherited order-one split-value identity gives one nonzero `K` such
that, at every root of `L`,

```text
x(x-1)P'(x)=K.                                      (6)
```

Apply Frobenius to (6), differentiate (5), and use
`P=(W-x_0)L`. For one nonzero scalar `lambda`, all six roots of `L` satisfy

```text
A^5 phi(W)(phi(W)-1)(phi(W)-x_0^p)
 =lambda W(W-1)(W-x_0).                             (7)
```

Both sides have degree three. Hence (7) is a polynomial identity, and
`phi` permutes the marked triples

```text
{0,1,x_0} -> {0,1,x_0^p}.                           (8)
```

The marked points are distinct: `x_0` is nonzero, while `x_0=1` would give
`c=0`; the same holds after Frobenius. Write `q=x_0` and `qstar=x_0^p`.
The six permutations in (8), followed by the constraints in (4), leave
only

```text
phi(W)=1-W,        S=1,                              (9)
```

or

```text
qstar=q/(q-1),     phi(W)=(1-qstar)W+qstar,
S=q.                                                     (10)
```

Indeed, the two permutations with `phi(0)=0` have `B=0`, contrary to
`S!=0`; the permutation `phi=qstar(1-W)` has `S=1` and would force
`qstar=B=S^p=1`; and the permutation
`phi=(qstar-1)W+1` has `B=1=S^p`, hence `S=1` and `qstar=0`.

Case (9) is impossible. Every reduced root then has `x^p=1-x`, so its color
`x(1-x)` lies in `F_p intersect mu_8={+1,-1}`. Color `+1` gives
`x^2-x+1=0`, whose roots have order six and cannot be `n`th roots for
power-of-two `n`. Color `-1` gives one quadratic and therefore at most two
roots, fewer than the six distinct roots of `L`.

In case (10), every repeated pair has sum `q=x_0`. Normalize it as

```text
u=x/q,       v=y/q,       u+v=1,
beta=u^(p+1)=v^(p+1) in mu_8.                        (11)
```

The two pointwise Frobenius equations imply

```text
uv=beta,       u^p=v.                                (12)
```

Thus `beta` is an `F_(p^2)/F_p` norm and lies in
`F_p intersect mu_8={+1,-1}`. If `beta=1`, then
`u^2-u+1=0`, again giving forbidden order six. If `beta=-1`, the unordered
pair `{u,v}` is the unique root pair of `X^2-X-1`. For fixed `q` this gives
only one repeated root pair and one repeated color, contrary to the two
distinct repeated colors under consideration. This eliminates (10).

Therefore `S=0`, proving (QCR2). Three repeated colors would pair all six
roots as `+/-x`, making their sum zero. But the coefficient calculation
below gives their sum `-6/d!=0`. Hence exactly two colors are repeated.

It remains to prove (QCR3). Write

```text
L(W)=W^6+l_1W^5+l_2W^4+l_3W^3+l_4W^2+l_5W+l_6.
```

From the hypergeometric coefficients and the differential equation at
`y=1`,

```text
l_1=6/d,
l_2=(30+r*d)/(2d^2),
l_3=(60+r*d*(d+8))/(3d^3),
l_5/l_6=-6d/(r-1).                                  (13)
```

The value `r=1` is impossible already in the first derivative equation
`(r-1)g'(1)/g(1)=r-7`.

Split `L` into its odd and even parts:

```text
L(W)=V(W^2)+W O(W^2),
O(Y)=l_1Y^2+l_3Y+l_5,
V(Y)=Y^3+l_2Y^2+l_4Y+l_6.                           (14)
```

Two distinct antipodal pairs give two distinct common roots of `O` and
`V`. Since `O` has degree two and nonzero leader, `O` divides `V`. The
constant coefficient of the remainder is

```text
l_6-(l_5/l_1)*(l_2-l_3/l_1)=0.                     (15)
```

Substituting (13) into (15) gives

```text
1=-[210+r*d*(1-d)]/[18(r-1)],
r*(18+d-d^2)+192=0,                                 (16)
```

which proves (QCR3) and the router. QED.
