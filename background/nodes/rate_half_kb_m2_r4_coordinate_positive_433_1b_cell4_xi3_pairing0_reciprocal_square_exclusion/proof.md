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

The deployed characteristic is odd. Every finite `q=de` solution therefore
lies on one of the three branches `q=B_i/A_i`. Roots of every `A_i`
denominator enter the exceptional-root census. At direct replay,
`A_i=0,B_i!=0` is empty, while `A_i=B_i=0` would remain unresolved. The
24 observed zero-denominator source points are all empty branches; no free
branch occurs.

Let `m=df` and `s=(d+f)^2` be the missing product and squared-sum records.
On a fixed `q` branch put `y=1/d^2`. Since `f=m/d` and `e=q/d`,

```text
1 + (2m-s)y + m^2 y^2 = 0,
ef = q m y.
```

The second paired equation is the quadratic

```text
paired(-q, sigma_o q m y) = 0.
```

The compiler forms the division-free resultant of these two quadratics in
`y`. It norms that resultant through the exact source tower with basis
`1,t,b,bt`, as certified by the parent tower-kernel node. The candidate
`r` set is the union of all deployed-field roots of the norm numerator and
denominator and every inverse-guard numerator and denominator.

Every candidate root is lifted through the base `t` quadratic, the `b`
quadratic, linear `c` recovery, and the compact kernel. At each guarded
source point the exact `y` root sets are intersected. For each common
nonzero `y`, every field root of `d^2=1/y` is enumerated and
`e=q/d`, `f=m/d` are recovered.

The direct replay verifies `de=q`, `df=m`, `(d+f)^2=s`,
`paired(q,q)=0`, and `paired(-q,sigma_o ef)=0`. It then evaluates
`paired(bf,sigma_c cf)` in both `sigma_c` lanes. Across all 24 rows there
are 200 candidate `r` values, 72 guarded source points, 64 `(y,d)`
candidates, and 128 final-pair evaluations. Every final value is nonzero.
The witness, target-boundary, free-branch, and unresolved ledgers are empty.

For each of four source signs and two `sigma_o` values, the three branch
rows exhaust all roots of `paired(q,q)`; each row checks both `sigma_c`
values. Hence the internal 24-row census covers exactly `4*2*2=16` raw
atlas cases. All stated cases are empty. QED.
