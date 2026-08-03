# Proof

After deleting `xi=3`, the residual product list is

```text
de, de, -de, sigma_o ef, bf, sigma_c cf.
```

Canonical matchings 1 and 2 are respectively

```text
(de,de), (-de,bf),         (sigma_o ef,sigma_c cf),
(de,de), (-de,sigma_c cf), (sigma_o ef,bf).
```

Let `A_i,B_i` be the three source-pencil coefficient pairs and write
`L_i(q)=B_i-q A_i`. Direct substitution into the paired-record determinant
gives

```text
paired(q,q) = 4 L_0(q) L_1(q)^2 L_2(q).
```

The deployed characteristic is odd. Consequently every finite `q=de`
solution lies on one of the three branches `q=B_i/A_i`. Roots of every
`A_i` denominator are included in the exceptional-root census. At direct
replay, `A_i=0,B_i!=0` is an empty branch, while `A_i=B_i=0` would be
retained as an unresolved free branch. No free branch occurs.

Let `m=df`, `s=(d+f)^2`, and `z=1/d`. Then

```text
M(z) = 1 + (2m-s)z^2 + m^2 z^4 = 0,
e = qz,  f = mz.
```

For pairing 1 the second equation is `P(z)=paired(-q,bmz)=0`; for pairing 2
it is `P(z)=paired(-q,sigma_c cmz)=0`. In both cases `P` is quadratic.
Divide the quartic `M` by `P` in the exact six-dimensional source algebra.
Every census row has linear remainder `R(z)=r_0+r_1 z`. Writing
`P(z)=p_0+p_1 z+p_2 z^2`, a common root must satisfy the division-free cut

```text
r_1^2 p_0 - r_1 r_0 p_1 + p_2 r_0^2 = 0.
```

This is `r_1^2 P(-r_0/r_1)` with denominators cleared. Every coefficient,
division, leading-coefficient, and branch exception is included in the guard
root census, so specializations lost by the generic remainder calculation
are replayed directly. The direct norm in the basis
`1,t,t^2,b,bt,bt^2` agrees exactly with the quadratic-over-cubic tower norm.

The root census includes every deployed-field root of the norm numerator and
denominator, every inverse-guard numerator and denominator, and the base
cubic leading coefficient. Their union is lifted through the base cubic,
the `b` quadratic, linear `c` recovery, product-rank cofactors, and compact
kernel. At each source point the exact roots of `M` and `P` are intersected.
For each common nonzero `z`, set `d=1/z`, `e=qz`, and `f=mz`.

The direct replay verifies `de=q`, `df=m`, `(d+f)^2=s`,
`paired(q,q)=0`, and the matching-specific second paired equation. Pairing 1
then evaluates `paired(sigma_o ef,sigma_c cf)` in all four target lanes;
pairing 2 evaluates `paired(sigma_o ef,bf)` in both `sigma_o` lanes for its
fixed `sigma_c`. Across all 36 branch rows there are 372 candidate `r`
values, 448 lifted source points, 56 `z` candidates, and 128 final-pair
evaluations. Every final value is nonzero. The witness, boundary,
free-branch, and unresolved ledgers are empty.

For pairing 1, four source signs and three internal branches give twelve
rows, each covering four target lanes, hence 16 raw cases after branch
exhaustion. For pairing 2, four source signs, three branches, and two
`sigma_c` values give 24 rows, each covering both `sigma_o` lanes, hence 16
raw cases after branch exhaustion. The branches are internal alternatives,
not distinct atlas cases. Therefore the census exhausts exactly 32 raw cases,
and all are empty. QED.
