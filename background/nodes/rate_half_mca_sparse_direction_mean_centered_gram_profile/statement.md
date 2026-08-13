# Sparse-direction mean-centered Gram profile

- **status:** PROVED
- **closure:** PSD post-Johnson list cap and exact deficit-profile payment
- **scope:** one shortened support-wise MCA-bad family after a codeword
  direction gauge

## Ordinary-list lemma

Let `S_1,...,S_L` be distinct `A`-subsets of an `n`-set with pairwise
intersections at most `c`, where `A>c`.  Put

```text
g=nc-A^2,
T=(n-A)^2-(n-1)g.
```

If

```text
g>=0,       2A^2>=nc,       T>0,                    (MC0)
```

then

```text
L <= floor((n-1)n^2(A-c)/(A*T)).                    (MC1)
```

## Exact MCA profile

Use

```text
N=R+K,       m=d+K,       c=K-1,
r_1=b+q,     E=supp(q),   |E|=e<d,
n=N-e.
```

For each deficit threshold `1<=h<=e`, put `A_h=m-h` and define a raw
cumulative explanation cap `C_h` as follows:

```text
if A_h^2>nc:
  C_h=floor(n(A_h-c)/(A_h^2-nc));
otherwise, if (MC0) holds for A_h:
  C_h=floor((n-1)n^2(A_h-c)/(A_h*T_h)),
  T_h=(n-A_h)^2-(n-1)(nc-A_h^2).
```

Assume one of these cases defines every `C_h`.  Put

```text
B_0=0,       B_h=min_(h<=v<=e) C_v.
```

Then

```text
|Z| <= sum_(h=1)^e (B_h-B_(h-1))*floor(e/h).       (MC2)
```

Together with the preceding low-support payments, `(MC2)` expands the
complete certified walls to

```text
KoalaBear K=14:   e<=64047,   j=R-e>=984529;
Mersenne K=6:     e<=65454,   j=R-e>=983122.
```

The endpoint profile values are `181731868` and `16101127`.  At the next
KoalaBear support the endpoint `T` is `-1499457466`, so `(MC1)` is
unavailable.  At the next Mersenne support all caps remain legal, but
`(MC2)=17120123>16777215`.

## Nonclaims

This does not pay either adjacent support, claim optimality of the
mean-centered cap, use the full-lift near-MDS extension structure, or close
an official row.

## Falsifier

A legal block family exceeding `(MC1)`, a legal selected family exceeding
`(MC2)`, or an incorrect endpoint, adjacent profile, or hypothesis sign.
