# Published input

I. Vyugin and S. Makarychev, *Solutions of polynomial equation over
F_p and new bounds of additive energy*, arXiv:1504.01354, Theorem 2.

For an absolutely irreducible polynomial of bidegree `(m,n)` with
`P(0,0)!=0` and `deg P(x,0)>=1`, and a multiplicative subgroup `G` satisfying

```text
100(mn)^(3/2)<|G|<p^(3/4)/3,
```

the number of points in a product of two cosets of `G` is at most

```text
16 m n^2 (m+n) |G|^(2/3).
```

Source: https://arxiv.org/abs/1504.01354

The proof uses `(m,n)=(2,2)`, `(2,3)`, and `(1,1)`. Every application
prints the coordinate change that supplies the two affine hypotheses; the
worst constant is `1440` for `(2,3)`.
