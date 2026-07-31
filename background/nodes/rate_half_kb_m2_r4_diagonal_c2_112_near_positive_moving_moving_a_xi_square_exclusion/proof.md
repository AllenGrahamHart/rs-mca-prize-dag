# Proof

Normalize `a=xi=2`, `(eta,ell)=(c,d)`, and `w=1/c`. The moving-moving
interpolation uses the internal edges `{2,b}` and `{2,1/b}`. Assign the
residual over `c` to `(W-1/2)^2` and that over `d` to `(W-1/d)^2`.

Direct source reconstruction gives the four product/sum cores. After exact
division by the finite-incidence square in the product equations, their
degree, term-count, and digest records are

```text
c product (4,8,6) 299 5b27d4da822910b2
c sum     (4,12,8) 567 f5399a196459bb4f
d product (4,6,8) 284 72568ee71be7f479
d sum     (4,10,9) 532 48c4bf1306aae34b.             (1)
```

Each core is reciprocal in `b`. Writing `s=b+1/b` and checking the reverse
lift term by term gives

```text
c product (2,8,6) 181 736a52293558c61d
c sum     (2,12,8) 342 3164f186a76328f5
d product (2,6,8) 172 f0bba9bf4f23b8d2
d sum     (2,10,9) 321 2414ff4e8cdee299.             (2)
```

The within-`c` and within-`d` eliminants have respective digests
`830a8747ce80372c` and `43a8347e92f7f81d`. Their full factor and
multiplicity censuses are pinned by both implementations. Removing factors
supported on the admissibility divisor leaves three components on each
side:

```text
c: fb37b983fcfb060a, 9396ced8aa4cfa67, 21ee8a55421c92a9,
d: 9622b8845f94fd73, c7aea723bf6f84a1, dbac8f34560fc4e3. (3)
```

All nine pair projections are computed and factored over `QQ`, then factored
completely modulo `p=2130706433`. Their projection digests are

```text
1f08ddfc48ccd364  7b1a60698f1d453d  7baa9d358b67c4b3
266373746bf5a434  9088c346e4574364  801c3e3307141c22
259d7f61b4116377  2e12bb9e81d5076a  4a842f51757132b7. (4)
```

Standard linear factors force `d` to `2,1,-1,1/2`. Every other irreducible
factor whose degree divides six is retained. Deduplication gives exactly six
linear, five quadratic, three cubic, and one sextic factor. Higher degrees
cannot have a root in `F_(p^6)`.

For each retained factor, adjoin all four trace equations `(2)` over `F_p`
and saturate by

```text
c d; c,d in {2,1/2,1,-1}; c-d; cd-1;
2s-5; s^2-4; cs-c^2-1; ds-d^2-1;
5cd-4c-4d+5; 4c^2d-2c^2-3cd+3c+2d-4.             (5)
```

Every saturated Groebner basis is `[1]`. The factors in `(5)` are exactly
the zero, collision, inversion-fixed, reciprocal (`b=c^{+/-1}` or
`b=d^{+/-1}`), `z=1`, and finite-incidence exclusions in trace coordinates.
Thus no admissible deployed-field point remains.

The primary reconstructs the source by direct matrix inversion and uses
resultants. The no-import audit reconstructs it with
`DomainMatrix.solve_den`, verifies the fraction-free matrix identity and
the reciprocal reverse lift, and obtains both elimination layers from
terminal subresultants. Both independently recover `(1)`--`(5)` and the 15
unit saturations. QED.
