# Full-lift top-third common-core payment

- **status:** PROVED
- **closure:** top-third affine lines with a pair-noncontained total-core cap
- **scope:** the remaining pair-noncontained full-lift MCA branch

Use

```text
N=R+K,       m=d+K,       c=K-1,       t=N-m,
r_1=b+q,     E=supp(q),   |E|=e,       n=N-e.
```

Put

```text
s=floor((e-K)/3),       H=e-s-1,       r_0=max(0,e-m).
```

Assume `e>=K` and `N-m>s`.  For `r_0<=r<=s`, let `L_r` count selected
explanations with exact outside deficit `h=e-r` and put
`A_r=m-e+r`.  Then

```text
L_r <= Q_r,
Q_r = t+1                                      if A_r<=c,
Q_r = floor((n-c)/(A_r-c))                    if A_r>c.   (FC1)
```

Every such explanation owns one slope.  If positive punctured-Johnson caps
exist through `H` and `u=floor(e/2)`, then

```text
|Z| <= (e-1)J_u+J_H+sum_(r=r_0)^s Q_r.          (FC2)
```

Exact official-row evaluation extends the complete full-lift payments to

```text
KoalaBear:   e<=95943;
Mersenne-31: e<=67452.
```

At KoalaBear `e=95944` the prefix denominator at `H` is `-1037`.  At
Mersenne `e=67453`, `(FC2)=17248067>16777215`.  The residual intervals are

```text
KoalaBear:   95944<=e<=1044238;
Mersenne-31: 67453<=e<=1044241.
```

## Nonclaims

The adjacent failures are proof-method and budget walls, not unsafe
certificates.  This node does not close either deployed row.
