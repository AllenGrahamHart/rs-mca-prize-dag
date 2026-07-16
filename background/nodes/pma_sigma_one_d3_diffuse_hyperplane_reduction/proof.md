# Proof - PMA sigma-one diffuse hyperplane reduction

For five distinct points, the barycentric vector `(lambda_j)` spans the
one-dimensional nullspace of the `4 x 5` Vandermonde matrix with rows
`1,x,x^2,x^3`. Since `W` has degree at most three and agrees at all five
points,

```text
0 = sum_j lambda_j W(x_j)
  = sum_j lambda_j c_j L_D(x_j).
```

Expanding the monic cubic `L_D` gives `(DH)`.

If all four `A_t` vanished, the vector `(lambda_j c_j)` would lie in the same
Vandermonde nullspace. Hence `lambda_j c_j=mu lambda_j` for every `j`, and all
`c_j` would be equal. The five points lie in distinct petals and the planted
scalars are distinct, so this is impossible. The hyperplane is nonzero.

The values `c_jL_D(x_j)` at the first four points determine `W` uniquely by
cubic interpolation. Canonical selection of the first five agreements
therefore makes `(S,D)` an injective certificate.

It remains to count split locators on a fixed hyperplane. Write its equation
on three distinct roots `a,b,c` as

```text
F(a,b,c)
 = alpha+beta(a+b+c)+gamma(ab+ac+bc)+delta abc=0,       (1)
```

where `(alpha,beta,gamma,delta)` is nonzero. For an ordered pair `(a,b)`,
equation `(1)` is

```text
P(a,b)+Q(a,b)c=0,

P=alpha+beta(a+b)+gamma ab,
Q=beta+gamma(a+b)+delta ab.                             (2)
```

Unless `P=Q=0`, equation `(2)` permits at most one `c`. Call an ordered pair
exceptional when both vanish. At least one of the symmetric bilinear
polynomials `P,Q` is nonzero. A nonzero polynomial

```text
u+v(a+b)+w ab
```

has at most `2K-1` zeros on a `K` by `K` grid: for every `a` except possibly
one, it is a nonzero linear equation in `b`; at the exceptional `a` it has at
most `K` solutions. Hence there are at most `2K-1` exceptional ordered pairs.

There are at most `K(K-1)` ordered distinct pairs in total. Charging one
third root to every nonexceptional pair and at most `K-2` roots to every
exceptional pair gives fewer than

```text
K(K-1)+(2K-1)(K-2) < 3K^2
```

ordered distinct triples. Each split monic cubic is counted in all six root
orders, so fewer than `K^2/2` split locators lie on the hyperplane.

Finally there are `binom(M,5)` choices of five petals and `2^5` choices of
one point in each. Multiplication by the fixed-hyperplane bound proves

```text
32 binom(M,5) (K^2/2) = 16 K^2 binom(M,5),
```

with strict inequality inherited from the locator bound.

