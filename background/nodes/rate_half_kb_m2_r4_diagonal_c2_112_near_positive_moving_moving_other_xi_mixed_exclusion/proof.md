# Proof

Normalize as in the statement. Fraction-free reconstruction, followed by
removal of the incidence square from each product equation, gives

```text
c product  (5,8,7)   392  84ac13783b55222a
c sum      (5,12,9)  745  8a23e86f78587abe
d product  (5,6,7)   290  9274e57561535a30
d sum      (5,10,9)  627  4833ed35f7b07ba5.             (1)
```

Write `C_r,L_r` for the constant and leading residual coefficients before
squaring. The two product equations imply

```text
C_c L_d - C_d L_c = 0  or  C_c L_d + C_d L_c = 0.       (2)
```

After primitive incidence removal, the minus gate has digest
`66c6964895c7eb78` and factors into `c-d`, `cd-1`, two linear branches,
and one reciprocal quadratic branch in `b`. The first two are forbidden.
On each linear branch the two sum equations have one nonstandard common
curve; intersecting it with a product core gives projections of degrees
`254,256`. Their eight relevant deployed-field factors all have unit full
four-core forbidden saturation. On the quadratic branch, reduction of the
sum equations gives determinant `7a86b4bb0778e091`, compatibility
`2f87b73e36cae925`, and projection `8b81892ee39a8725` of degree `214`.
Its 14 relevant factors, including the terminal sextic, likewise have unit
full-core forbidden saturation. These are classifier indices `0..21`.

The plus gate is the irreducible reciprocal quartic
`598fd83fe93660e6`. Put `s=b+1/b`. Its trace is quadratic in `s`, with
leading coefficient

```text
q(c,d) = 4c^7d^6 - 20c^7d^5 + ... - 20d^3 + 33d^2 - 20d + 4,
digest d68dca6773113f75.                                (3)
```

## Generic chart `q != 0`

Reduce the two sum equations and two product equations to linear equations
in `b` over the quadratic trace algebra. Four independent necessary gates
(sum/sum, sum-c/product-c, sum-d/product-d, and sum-c/product-d) give the
following reduced bivariate equation pairs:

```text
sum/sum       42ba428e8e1f620a  aae92a0a95d3a7c1
same-c        c6cffc512137a57a  8fd1b3e36ff4fd64
same-d        9b391f276e13ec31  4f9231a661e6e80e
cross-side    0bde13b24e71711f  8ac04ec0e7906aa9.       (4)
```

Their base-prime `c`-resultants have degrees `11397,11241,10125,10865`.
The only common leading-degree-drop factors are
`d in {0,1,-1,2,1/2}` and are forbidden. After removing those factors, the
four projections have common degree `352`, with exactly 13 irreducible
factors of degrees

```text
1,1,5,12,12,1,1,2,2,4,4,1,1.                          (5)
```

For every factor in `(5)`, pass to its residue field, impose all eight
equations in `(4)`, and recover the common `c` fiber. Eleven fibers have
unit full-core `b` gcd. The last reciprocal pair combines to `d^2+1`; each
has a quadratic `c` fiber and quartic full-core `b` gcd, but that quartic
divides the complete forbidden product. Hence every generic fiber has unit
forbidden saturation.

Only factors whose residue degree divides six can contribute points over
the deployed field `F_(2130706433^6)`. In particular, the two degree-12
factors in `(5)` may be discarded. They were nevertheless reconstructed
and saturated as an intentional overcheck, so the certificate does not rely
on that discard.

All divisions made before `(4)` are explicit. The source contents are
products of `c=1`, `d=+/-1`, `cd=1`, and
`5cd-4c-4d+5=0`. The sum/sum common factors are `c-d`, `cd-1`, that same
bilinear factor, and
`4c^2d-2c^2-3cd+3c+2d-4`; the product gates additionally divide powers of
`q`. Every factor except `q` is in the forbidden product, and `q=0` is
handled next.

## Degree-drop chart `q = 0`

On `q=0` the quartic is

```text
b (q3 b^2 + q2 b + q3).
```

Since `b=0` is forbidden, reduce all four source cores fraction-free modulo
the reciprocal quadratic. The two product/sum determinants and two
quadratic-compatibility equations, together with `q`, have projection
degrees `869,914,857,902`. Their common deployed-field projection has degree
`772` and exactly 11 base-prime factors: six nonstandard factors of degrees
`1,1,2,2,4,4`, and the five standard values
`d=0,+/-1,2,1/2`. Direct residue-field reconstruction makes the full-core
`b` gcd a unit on all six nonstandard fibers; the other five are forbidden.
This also overcovers and therefore safely handles `q3=0`.

The primary uses exact SymPy source and trace construction with FLINT
resultants and finite-field extensions. The no-import audit independently
uses `DomainMatrix.solve_den`, reconstructs `(1)` and `(2)`, checks the
factor and reciprocal structure, rebuilds both stored candidate products,
and validates every saturation ledger entry. All stages are split below the
60-second local policy. Thus no admissible point remains. QED.
