# H3 unordered-product cutoff-12 candidate compiler

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_dsp8_correlation_bound` (evidence/router)
- **dependencies:** `f3_h3_global_resultant_compression`,
  `f3_h3_shifted_product_sidon`

Let `n=2^s`, `s>=2`, put `d=n-1`, and use

```text
c_a=1-zeta_n^a,                       1<=a<n,
F_n(X)=product_a(X-c_a),
Pcal_n(T)=product_(a,b)(T-c_a c_b).
```

Define the diagonal and unordered shifted-product polynomials

```text
Delta_n(T)=product_a(T-c_a^2),
Ucal_n(T)=product_(1<=a<=b<n)(T-c_a c_b).          (UPC1)
```

Both lie in `Z[T]`, are monic, and have

```text
Delta_n(T)=Res_X(F_n(X),T-X^2),
Ucal_n(T)^2=Pcal_n(T)Delta_n(T),
deg Ucal_n=n(n-1)/2.                               (UPC2)
```

Thus `Ucal_n` is the unique monic square root in `Z[T]` of the printed
resultant product; unordered root pairs need not be enumerated.

Put `R=Z[1/2]`. The shifted-product Sidon theorem makes `Ucal_n` squarefree
over characteristic zero. Introduce one inverse-selector variable `Y` and
put

```text
J_(n,12)=(Ucal_n^[0],Ucal_n^[1],...,Ucal_n^[12],
          (T-1)Y-1) in R[T,Y].
```

This is the unit ideal over `Q[T,Y]`, and its scalar intersection with `R`
has a unique positive odd generator

```text
(a_(n,12)^neq)=J_(n,12) intersect R.               (UPC3)
```

The selector is load-bearing: it removes the identity fiber `t=1`, whose
product multiplicity can be large even when the DSP8 locus is empty.

For every prime `p=1 mod n`, let `H<=F_p^*` have order `n`, put
`A=(1-H)\{0}`, and define

```text
P(t)=#{(x,y) in A^2:xy=t},
D(t)=#{x in A:x^2=t},
U(t)=#{unordered {x,y} with repetition in A:xy=t}.
```

Then

```text
P(t)=2U(t)-D(t),                 0<=D(t)<=2,        (UPC4)
p divides a_(n,12)^neq
  iff some t!=1 has U(t)>=13.                       (UPC5)
```

In particular,

```text
some t!=1 has P(t)>=25  =>  p divides a_(n,12)^neq. (UPC6)
```

On the selected `t!=1` locus, the converse has one explicit boundary only.
If `U(t)>=14`, then `P(t)>=26`; if `U(t)=13`, then `P(t)=26-D(t)`, so the
sole false-positive profile for cutoff 25 is

```text
U(t)=13,       D(t)=2,       P(t)=24.              (UPC7)
```

At `n=8192`, the scalar compiler uses a degree-`33,550,336` polynomial and
thirteen Hasse-derivative generators. The ordered formulation would use
degree `67,092,481` and twenty-five generators. This is an exact candidate
compression, not an official-scale elimination algorithm, factorization,
cost bound, or proof that `P(t)<=24`.
