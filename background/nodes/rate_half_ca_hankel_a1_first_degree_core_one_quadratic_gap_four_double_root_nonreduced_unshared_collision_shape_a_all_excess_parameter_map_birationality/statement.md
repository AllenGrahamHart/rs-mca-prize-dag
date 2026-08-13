# `A=1` shape-A all-excess parameter-map birationality

- **status:** PROVED
- **closure:** every nontrivial minimal tensor presentation has a birational
  parameter coefficient map
- **consumer:** `rate_half_band_crossing_location`

Retain an official Shape-A all-excess survivor and any minimal tensor
presentation of rank `r>=2`:

```text
G(t,X)=sum_(j=0)^(r-1) A_j(t)B_j(X).               (ABR1)
```

The parameter coefficient map

```text
a:P^1_t -> P^(r-1),
a(t)=[A_0(t):...:A_(r-1)(t)]                       (ABR2)
```

is basepoint-free and birational onto its projective image.

More exactly, if `d` is its degree onto the image, then the exact split-row
and column-deficit ledgers give

```text
d | m,
d | (3e-z) for some z in {0,1}.                    (ABR3)
```

On the official row

```text
m=e-2=183251937961,
gcd(m,3e)=gcd(m,6)=1,
gcd(m,3e-1)=gcd(m,5)=1,                            (ABR4)
```

so `d=1`.

## Scope

This applies uniformly to every tensor rank at least two. It does not bound
the degree, singularities, or linear normality of the image in ranks four
and higher, and does not exclude any survivor by itself.
