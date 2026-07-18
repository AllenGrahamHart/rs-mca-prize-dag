# Proof

The product energy is the number of quadruples in `A^4` satisfying

```text
ab=cd.
```

The quotient `L2` moment counts quadruples satisfying

```text
b/a=d/c,
```

or equivalently `bc=ad`. Relabeling the four variables proves

```text
sum_t R(t)^2=sum_t P(t)^2=E_x(A).                 (1)
```

Now expand the squared `L2` distance:

```text
sum_t(P(t)-R(t))^2
 =sum_tP(t)^2+sum_tR(t)^2-2sum_tP(t)R(t)
 =2E_x(A)-2N_3to1(A).
```

Rearranging proves `(ID1)`.

At `t=1`, every quotient pair has equal entries, so `R(1)=|A|=n-1`.
The optimized one-shift specialization of the proved auxiliary-polynomial
theorem in `f3_h2_stepanov_inhouse`, with its official-row parameter replay
recorded in
`critical/nodes/u1_x4_direct_column_budget/notes/F3_H3_TRACEZERO_OFFICIAL_PAYMENT.md`,
gives `P(1)<4n^(2/3)`. Since `n>=8192`, the difference
`n-1-4n^(2/3)` is positive. Therefore `(ID1)` and `(ID3)` give

```text
N_3to1(A)
 < (145/4)(n-1)^2-(1/2)(n-1-4n^(2/3))^2.         (2)
```

It remains to compare `(2)` with `(ID4)`. Put `x=n^(1/3)`. The difference
between the right side of `(ID4)` and the right side of `(2)`, multiplied by
four, is

```text
G(x)=x^6-16x^5-32x^4+284x^3+16x^2-143.           (3)
```

Official orders have `x>20`. At `x=20`,

```text
G(20)=9,958,257>0.
```

Moreover

```text
G'(x)=x^2(6x^3-80x^2-128x+852)+32x.
```

The polynomial in parentheses is `14,292` at `x=20`. Its derivative is
`18x^2-160x-128`, which is positive and increasing for `x>=20`. Hence
`G'(x)>0` there, so `(3)` is positive at every official order. This proves
`(ID4)`.

Finally,

```text
(145/4)(n-1)^2-35n^2
 =(5/4)n^2-(145/2)n+145/4>0
```

for `n>=8192`, proving the strict improvement over the old clean energy
endpoint. The theorem is only an implication because `(ID3)` remains open.
