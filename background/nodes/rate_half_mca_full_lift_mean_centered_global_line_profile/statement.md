# Full-lift mean-centered global-line profile

- **status:** PROVED
- **closure:** compose the full prefix Gram profile with one global high line
- **scope:** the remaining pair-noncontained full-lift MCA branch

Retain the full-lift notation and put

```text
s=floor((e-K)/3),       H=e-s-1,       t=N-m.
```

Assume `A_H=m-H>K-1`. For each prefix threshold `1<=h<=H`, let `C_h` be the ordinary punctured
Johnson cap when its denominator is positive, and otherwise the proved
mean-centered Gram cap whenever its hypotheses hold. Assume every `C_h` is
defined and put

```text
B_0=0,       B_h=min_(h<=v<=H) C_v.
```

Then the full selected slope family satisfies

```text
|Z| <= sum_(h=1)^H (B_h-B_(h-1))*floor(e/h) + (t+1).    (MG1)
```

Exact official scans prove the complete walls

```text
KoalaBear:   e<=96150, endpoint 479693401;
Mersenne-31: e<=98229, endpoint 16488216.
```

At KoalaBear `e=96151`, the first undefined cap occurs at `h=H=64105`,
where the mean-centered denominator is `-4625043784`. At Mersenne
`e=98230`, every cap remains defined but `(MG1)=17415873`, exceeding budget
by `638658`. The full-lift residual intervals are therefore

```text
KoalaBear:   96151<=e<=1044238;
Mersenne-31: 98230<=e<=1044241.
```

## Nonclaims

Neither adjacent failure is an unsafe certificate. This node does not close
a deployed row or move a v4 first-match ledger atom.
