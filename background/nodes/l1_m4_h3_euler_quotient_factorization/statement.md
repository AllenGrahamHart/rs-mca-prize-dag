# L1 m=4, h=3 Euler quotient factorization

- **status:** PROVED
- **dependency:** `l1_m4_h3_cartier_resonance_reduction`
- **consumer:** `l1_mixed_petal_amplification`

Use the surviving notation

```text
g(Y)=Y^3+aY+b,    R=X^nu U,    nu in {0,1,2,3},
g(R)D=X^n-alpha,  n=4(p+1),    h=deg H<=3-nu.          (EQF1)
```

Put

```text
V=nu U+XU'.                                             (EQF2)
```

Then the domain derivative and the Wronskian equation give the exact
factorization

```text
D(2aR+3b)V=H g(R)-4 alpha U.                            (EQF3)
```

In particular,

```text
H(0)!=0,
V!=0,       deg V=p+h-4.                               (EQF4)
```

Since `0<=h<=3-nu`, the Euler derivative `V` has degree in the interval

```text
p-4<=deg V<=p-nu-1.                                    (EQF5)
```

Thus only `3-nu-h` of its top possible coefficients vanish. At `nu=3`, the
Cartier theorem has `h=0`, so `deg V=p-4` exactly.

This factorization does not exclude any of `nu=0,1,2,3`, classify their
solutions, count components, classify nonembedded `h=2`, treat `m=8,16`, or
close L1.
