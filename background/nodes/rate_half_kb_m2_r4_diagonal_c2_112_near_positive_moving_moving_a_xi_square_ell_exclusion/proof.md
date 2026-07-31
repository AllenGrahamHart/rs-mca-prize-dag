# Proof

Use the moving-moving interpolation with `a=xi=2`, `(eta,ell)=(c,d)`,
`w=1/c`, and source edges `{2,b},{2,1/b}`. Assign the residual over `c` to
`(W-1/d)^2` and that over `d` to `(W-1/2)^2`.

After exact removal of the finite-incidence square from the product
conditions, the primitive degree, term-count, and digest records in `(b,c,d)`
are

```text
c product (4,8,8) 380 a3c2f655933d7fa4
c sum     (4,12,9) 632 f9448c2c1e47ba1b
d product (4,5,6) 194 a9568da9b73746f3
d sum     (4,9,8) 432 34219e7d8f958227.              (1)
```

Each is reciprocal in `b`. Exact substitution through `s=b+1/b`, followed
by reverse lifting, gives

```text
c product (2,8,8) 230 162035e9c06a96e0
c sum     (2,12,9) 381 a4fe8c32d48892ac
d product (2,5,6) 118 a204237915868784
d sum     (2,9,8) 261 02be6fc5511268da.              (2)
```

The within-root eliminants have digests `4b4738172d468601` and
`7f225ae889ff6913`. Their full factor multiplicities are pinned. Every
discarded parent factor is mechanically identified with a zero, fixed,
inverse-fixed, reciprocal, or `z=1` equation. The remaining components are

```text
c: 90db6ed8f237340f, 39a8eb9fc1019be9, 4805246499888132,
d: c753072a5bf68171, 6ba62bd34c05e0ff.              (3)
```

The six pair projections have digests

```text
cacf0935414003b8  673e881e67dbe000
69f68b152fb0fb7e  e68bf89ec438dd41
c76ed153d004aadf  9c685995254fb8b6.                (4)
```

Their complete characteristic-zero and modular factor censuses are pinned.
After standard support, the only factors are `14d-11`,
`19d^3-69d^2+93d-35`, two degree-nine polynomials, and one degree-five
polynomial. The degree-five and degree-nine factors are irreducible modulo
`p=2130706433`, hence have no root in `F_(p^6)`. The first two split into
four distinct modular linear factors.

For each linear factor, adjoin the four trace equations `(2)` and saturate by

```text
c d; c,d in {2,1/2,1,-1}; c-d; cd-1;
2s-5; s^2-4; cs-c^2-1; ds-d^2-1;
5cd-4c-4d+5; 4c^2d-2c^2-3cd+3c+2d-4.             (5)
```

Every saturated basis is `[1]`. Thus every deployed-field point lies on a
forbidden locus and the chart is empty.

The primary uses direct matrix inversion and resultants. The no-import audit
uses `DomainMatrix.solve_den`, verifies the fraction-free source identity and
the reciprocal reverse lift, and derives both elimination layers from
terminal subresultants. Both recover `(1)`--`(5)` independently. QED.
