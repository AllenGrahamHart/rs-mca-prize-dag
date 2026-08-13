# `A=1` shape-A all-excess domain-map birationality

- **status:** PROVED
- **closure:** every nontrivial minimal tensor presentation has a birational
  domain coefficient map
- **consumer:** `rate_half_band_crossing_location`

Retain an official Shape-A all-excess survivor and any minimal tensor
presentation of rank `r>=2`:

```text
G(t,X)=sum_(j=0)^(r-1) A_j(t)B_j(X).               (DBR1)
```

The domain coefficient map

```text
b:P^1_X -> P^(r-1),
b(X)=[B_0(X):...:B_(r-1)(X)]                       (DBR2)
```

is basepoint-free and birational onto its projective image.

If `d_X` is its degree onto the image, the exact norm and split-row ledgers
give

```text
d_X | n,
d_X | (R+z) for some z in {0,1}.                   (DBR3)
```

On the official row,

```text
R=3n+7,
gcd(n,R)=gcd(n,7)=1,
gcd(n,R+1)=gcd(n,8)=1,                             (DBR4)
```

so `d_X=1`.

## Scope

This applies uniformly to every tensor rank at least two. It allows
distinct points of `U_0` to have the same projective row type only as
different normalization branches over a singular image point. It does not
bound those singularities or exclude a survivor by itself.
