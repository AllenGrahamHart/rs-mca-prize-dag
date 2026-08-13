# Sparse-direction top-third affine-line payment

- **status:** PROVED
- **closure:** exact-layer affine-line caps for the top third of deficits
- **scope:** one shortened support-wise MCA-bad family after a codeword direction gauge

## Exact-layer theorem

Use

```text
N=R+K,       m=d+K,       c=K-1,
r_1=b+q,     E=supp(q),   |E|=e<d,       n=N-e.
```

Assume `e>=K`, put

```text
s=floor((e-K)/3),       H=e-s-1.
```

and assume `N-m>s`.

For `0<=r<=s`, the number `L_r` of selected explanations with exact
outside deficit `h=e-r` obeys

```text
L_r <= floor((n-c)/(m-e+r-c)).                       (TT1)
```

Every such explanation owns at most one selected slope.

## Prefix-plus-top-third profile

For `1<=h<=H`, let `C_h` be any proved cumulative cap on the number
`N_h` of explanations with outside deficit at most `h`, and put

```text
B_0=0,       B_h=min_(h<=v<=H) C_v.
```

Then

```text
|Z| <= sum_(h=1)^H (B_h-B_(h-1))*floor(e/h)
       + sum_(r=0)^s floor((n-c)/(m-e+r-c)).         (TT2)
```

If the punctured Johnson caps `J_h` are defined through `H`, and
`u=floor(e/2)`, then

```text
|Z| <= (e-1)J_u+J_H
       + sum_(r=0)^s floor((n-c)/(m-e+r-c)).         (TT3)
```

## Official branch closure

Exact endpoint arithmetic gives uniform bounds over every remaining
support `e<d`:

```text
KoalaBear K=14:   |Z|<=11496959 < 274980728111395087;
Mersenne K=6:     |Z|<=11496238 <          16777215.
```

Together with the preceding nodes, every sparse-direction support
`1<=e<d` is paid.  The full-lift top-rank residual intervals become

```text
KoalaBear:   67472<=e<=1044238;
Mersenne-31: 67448<=e<=1044241.
```

## Nonclaims

This does not treat `e>=d`, use the full-lift near-MDS extension structure,
prove either deployed row, or provide an unsafe certificate.

## Falsifier

Three high-deficit explanations that violate the affine-line conclusion, a
legal exact layer exceeding `(TT1)`, a selected family exceeding `(TT2)`,
or an incorrect uniform official-row comparison.
