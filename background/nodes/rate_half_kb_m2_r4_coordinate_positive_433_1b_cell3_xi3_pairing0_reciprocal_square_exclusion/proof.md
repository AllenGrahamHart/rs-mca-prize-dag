# Proof

After deleting `xi=3`, the residual product list is

```text
de, de, -de, sigma_o ef, bf, sigma_c cf.
```

Canonical matching zero pairs adjacent entries. Let `A_i,B_i` be the three
source-pencil coefficient pairs and write `L_i(q)=B_i-q A_i`. Direct
substitution into the paired-record determinant gives

```text
paired(q,q) = 4 L_0(q) L_1(q)^2 L_2(q).
```

Indeed, the first determinant vanishes, while the other two factors are
`-2 L_1 L_2` and `2 L_0 L_1`. The deployed characteristic is odd.
Consequently every finite `q=de` solution lies on one of the three branches
`q=B_i/A_i`. Roots of every `A_i` denominator are included in the
exceptional-root census. At direct replay, `A_i=0,B_i!=0` is an empty
branch, while `A_i=B_i=0` would be retained as an unresolved free branch.
No free branch occurs.

Let `m=df` and `s=(d+f)^2` be the missing product and squared-sum values.
On a fixed `q` branch put `y=1/d^2`. Since `f=m/d` and `e=q/d`,

```text
1 + (2m-s)y + m^2 y^2 = 0,
ef = q m y.
```

The second paired equation is therefore the quadratic

```text
paired(-q, sigma_o q m y) = 0.
```

The compiler forms the division-free resultant of these two quadratics in
`y`. Its direct norm in the six-dimensional basis
`1,t,t^2,b,bt,bt^2` agrees exactly with the quadratic-over-cubic tower norm.

The root census includes every deployed-field root of the norm numerator and
denominator, every inverse-guard numerator and denominator, and the base
cubic leading coefficient. Their union is lifted through the base cubic,
the `b` quadratic, linear `c` recovery, product-rank cofactors, and compact
kernel. At each source point the two exact `y` root sets are intersected.
For each common nonzero `y`, set `x=1/y`, enumerate every field root of
`d^2=x`, and recover `e=q/d` and `f=m/d`.

The direct replay verifies `de=q`, `df=m`, `(d+f)^2=s`,
`paired(q,q)=0`, and `paired(-q,sigma_o ef)=0`. It then evaluates the
last equation `paired(bf,sigma_c cf)` in both `sigma_c` lanes. Across all
24 branch rows there are 228 candidate `r` values, 216 lifted source
points, 112 `(y,d)` candidates, and 224 final-pair evaluations. Every final
value is nonzero. The witness, boundary, free-branch, and unresolved ledgers
are empty.

For each of four source signs and two `sigma_o` values, the three branch
rows exhaust all roots of `paired(q,q)`; each row checks both
`sigma_c` values. Hence the internal 24-row census covers exactly
`4*2*2=16` raw atlas cases. All stated cases are empty. QED.
