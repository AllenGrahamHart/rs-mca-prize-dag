# Moving-xi mixed chart: exact deployed-field frontier

**Status:** exact primary narrowing evidence; not yet a PROVED node.

Normalize `a=2`, `xi=b`, `(eta,ell)=(c,d)`, and `w=1/c`. Assign the two
distinct residual roots `1/b,1/d` at both q-roots. The four primitive
conditions, after removing `H^2` from each product condition, have degrees

```text
              (deg_b,deg_c,deg_d)   terms   digest
c product          (3,6,5)           154    5117a5676cc0bdb9
c sum              (3,10,7)          341    b052e13bbf0f28fe
d product          (3,6,5)           150    70cb7c16ac2f1e3e
d sum              (3,10,7)          341    0ed07280609cd604
```

The within-`c` resultant leaves residual components `(3,2)` and `(16,14)`
with digests `bed4496a0af11b8c`, `842d5d9a084f107e`. The within-`d`
resultant leaves the same degrees with digests `8d63799ea7b1c3fc`,
`39ad8e659560b1b1`. Standard collision, inversion-fixed, incidence, and
`z=1` factors are removed explicitly.

## Four component pairs

- Low/low projects to standard support, `19d-17`, and
  `2d^3-19d^2+19d-14`. Direct modular lex bases and exact quotient-field
  reconstruction put every `F_(p^6)` point on `b=0`, `b=1/2`, `b=c=1`,
  `c=d`, `cd=1`, or `z=1`.
- Low/high has one degree-40 characteristic-zero factor. Modulo
  `p=2130706433` it has degrees `1,2,2,4,4,27`. The degree `1,2,2`
  fibers are fully reconstructed and forbidden; the other degrees cannot
  have roots in `F_(p^6)`.
- High/low has one degree-40 factor. Modulo `p` it has degrees `1,1,6,32`.
  The degree `1,1,6` fibers are fully reconstructed and forbidden; degree
  `32` cannot enter `F_(p^6)`.
- High/high is handled without its expensive direct resultant. A point must
  lie on one of the two nonstandard cross-product factors. Projecting the
  high within-`c` component against each cross-product factor and discarding
  irreducible degrees not dividing six leaves eleven nonstandard field
  factors: three linear, five quadratic, two cubic, and one sextic. Modular
  lex bases followed by exact `F_p`, `F_(p^2)`, `F_(p^3)`, or `F_(p^6)`
  quotient reconstruction classify every point as `b=1/2`, `b=c=1`,
  `cd=1`, `z=1`, or finite-incidence. For cubic `d`, the Frobenius audit
  also checks that no quadratic-over-`F_(p^3)` `b` point is omitted.

The low cross-product/cross-sum pair audits independently narrow to
`d=1/2`; the high pair narrows to `d in {-1,1,2,1/2}`. These are redundant
checks, not required by the cross-product coverage above.

## Artifact

`kb_c2_112_near_moving_xi_mixed.py`, SHA-256
`d56f6c5878572bb11d9c50a9cc119767545e15d25bad9b68afcd5d8e155c7701`.
Every completed mode ran serially under `ramguard tiny` and a 60-second wall
limit. The direct high/high resultants were deliberately abandoned after
both characteristic-zero and modular attempts reached that limit; the
cross-product route makes them unnecessary.

## Promotion gate

Do not count this as chart 9 yet. Promotion requires:

1. replace exploratory output with pinned, fail-closed assertions for every
   component digest, modular factor census, field gcd, and forbidden point;
2. shard the assertions so every verifier remains below 60 seconds;
3. add a no-import fraction-free source reconstruction and an independent
   component/factor audit;
4. replay both paths modulo `p`, pin hashes, and only then mint the scoped
   PROVED mixed-chart node.
