# Proof

Write `c=m-2h`. Since the root sets of `P,Q,R` partition `mu_m`, equation
`(CTG1)` holds with `R` monic and squarefree. The characteristic hypothesis
makes `2,m,h` nonzero in `K`.

Define

```text
H=(d/m) X P' R.                                     (1)
```

If `alpha` is a root of `P`, differentiate `PQR=X^m-1` and evaluate at
`alpha`. Since `Q(alpha)=d` and `alpha^m=1`,

```text
m alpha^(-1)=P'(alpha)dR(alpha),
H(alpha)=1.                                         (2)
```

If `beta` is a root of `Q`, then `P(beta)=-d` and `Q'=P'`, so the same
calculation gives

```text
m beta^(-1)=-dP'(beta)R(beta),
H(beta)=-1.                                         (3)
```

The roots are simple. Hence `(2)` and `(3)` imply

```text
H-1=PA,       H+1=QB                               (4)
```

for polynomials `A,B`. The leading term of `(1)` is
`(dh/m)X^(m-h)`, which is nonzero. Therefore

```text
deg A=deg B=m-2h=c,
lc(A)=lc(B)=dh/m.                                  (5)
```

Subtract the two equations in `(4)` and use `Q=P+d`:

```text
P(B-A)+dB=2.                                       (6)
```

Suppose `h>c`. By `(5)`, `deg(B-A)<=c-1`. If `B-A` were nonzero, then
`P(B-A)` would have degree at least `h`, whereas `dB` has degree `c<h`;
the left side of `(6)` could not be constant. Thus `B=A`, and `(6)` becomes
`dB=2`. This contradicts `deg B=c>0`. Hence `h<=c`, proving `(CTG2)`.

If `m` is a power of two and `h>0`, the equality `3h=m` is impossible.
Thus `3h<m`. The exact-ratio compiler and near-square union router identify
every orbit counted by `E_h^prim(m,p)` with a pair satisfying the hypotheses;
the official condition `p=1 mod n`, with `m|n`, gives `p>n>=m`. This proves
`(CTG3)` and `(CTG4)`. QED.
