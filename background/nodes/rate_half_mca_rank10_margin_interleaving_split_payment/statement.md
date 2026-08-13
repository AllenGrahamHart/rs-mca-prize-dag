# Rank-10 margin/interleaving split payment

- **status:** PROVED
- **scope:** one post-near same-support pair-noncontained MCA family after
  the reversible error-rank gauge
- **official consequence:** KoalaBear error rank ten is paid in full

Let `C=RS[F,D,K]`, `|D|=n`, `m=K+w`, and suppose the gauged explanations
of a post-near family lie in `c_0+C'`, where `dim C'=s`.  Retain exact
`m`-supports `S_gamma` and define the support-local margin of one slope by

```text
theta_gamma=min(w+1,min_(b in C')
                |{x in S_gamma:r_1(x)!=b(x)}|).
```

Fix an integer `T` with

```text
2<=T<=w+1,       A=m-T+1>K,
M_s(T)=floor(C(n-K+s,s)/C(w-T+1+s,s)),
M_s(T)^2<|F|.
```

Put `ST_0(T)=floor(n/T)`.  For `1<=r<=s`, put

```text
ST_r(T)=floor(max{
  n_fall_(r+1)/(m T (w+1)_rise_(r-1)),
  (n-K+r)_fall_(r+1)/(T (w+1)_rise_r)
}).
```

Then the post-near family satisfies

```text
|Z_post| <= max_(0<=r<=s) ST_r(T) + (n-A)M_s(T).       (MI1)
```

Consequently the complete family, including the disjoint near-rational
part, has size at most

```text
2w + max_(0<=r<=s) ST_r(T) + (n-m+T-1)M_s(T).          (MI2)
```

For the official KoalaBear row and error rank ten, the reversible gauge
has `s=9`.  At `T=667`, exact arithmetic gives

```text
(n,K,m,w) = (2097152,1048576,1116048,67472),
A         = 1115382,
M_9       = 57781140652,
max ST_r  = 5143522968716559,
(n-A)M_9  = 56727790457914040,
2w        = 134944,
total     = 61871313426765543
          < 274980728111395087 = B_*.
```

The slack is `213109414684629544`.  Among all legal thresholds for this
printed formula, `T=16` is the first that pays and `T=667` is the unique
minimizer.  This closes the direct KoalaBear error-rank-ten branch.  The
same formula does not pay error ranks eleven or twelve.

## Nonclaims

This theorem does not pay error rank at least eleven, move a v4 ledger
atom, or assert that `T=667` is optimal among all possible MCA arguments.
Its optimality claim is only for `(MI2)` with `s=9` on the printed row.
