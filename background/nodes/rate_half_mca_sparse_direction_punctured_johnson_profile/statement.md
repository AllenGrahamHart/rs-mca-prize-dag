# Sparse-direction punctured Johnson profile

- **status:** PROVED
- **closure:** field-general incidence compiler and exact official walls
- **scope:** one shortened support-wise MCA-bad family after a codeword
  direction gauge

## Statement

Let `C=RS[F,D,K]` have

```text
N=R+K,       m=d+K,
```

and suppose

```text
r_1=b+q,       b in C,       E=supp(q),       |E|=e<d.
```

For the transformed explanations `a_gamma=c_gamma-gamma*b`, define the
outside-agreement deficit

```text
h_a=m-|{x outside E:a(x)=r_0(x)}|.
```

Then `1<=h_a<=e`, and one explanation of deficit `h` owns at most
`floor(e/h)` selected slopes.

Assume the punctured Johnson denominator is positive at the weakest
agreement threshold:

```text
D_e=(m-e)^2-(N-e)(K-1)>0.                         (PJ0)
```

Put `J_0=0` and, for `1<=h<=e`,

```text
J_h=floor((N-e)(m-h-K+1)
          /((m-h)^2-(N-e)(K-1))).                 (PJ1)
```

The number of selected slopes obeys

```text
|Z| <= sum_(h=1)^e (J_h-J_(h-1))*floor(e/h)       (PJ2)
    <= (e-1)J_floor(e/2)+J_e.                     (PJ3)
```

For `e=1`, the term with index zero in `(PJ3)` is zero.

## Official walls

Exact integer evaluation proves every support in these prefixes is paid:

```text
KoalaBear K=14:   1<=e<=63908,   j=R-e>=984668;
Mersenne K=6:     1<=e<=65236,   j=R-e>=983340.
```

At the endpoints the coarse bounds `(PJ3)` are respectively

```text
4607583 <= 274980728111395087,
2605443 <=          16777215.
```

The denominators at the endpoints are `1218` and `2794`.  At the adjacent
supports they are `-5924` and `-1636`, so this Johnson theorem makes no
claim there.

## Nonclaims

This does not pay a support after the displayed wall, assert that Johnson
failure implies an MCA counterexample, close the middle-support interval,
or close either official row.

## Falsifier

A legal selected family exceeding `(PJ2)`, a punctured ordinary list larger
than `(PJ1)`, a slope fiber larger than `floor(e/h)`, or an incorrect exact
official wall.
