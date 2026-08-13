# `A=1` shape-A coefficient syzygy-bundle cubic splitting

- **status:** PROVED
- **closure:** the coefficient linear series has only degree-one, -two, and
  -three minimal syzygies
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A. Let `V subset S_m=F[U,V]_m` be the parameter coefficient
space of `G`, with

```text
m=e-2,       r=dim V=sr(G).                        (CSB1)
```

The parameter coefficient map is basepoint-free. Over an algebraic closure,
write its syzygy bundle as

```text
0 -> E -> V tensor O_P1 -> O_P1(m) -> 0,
E=sum_(i=1)^(r-1) O_P1(-mu_i).                     (CSB2)
```

Then

```text
mu_i in {1,2,3}       for every i.                 (CSB3)
```

If `c_j=#{i:mu_i=j}`, then

```text
c_1+c_2+c_3=r-1,
c_1+2c_2+3c_3=m,
2c_1+c_2=3r-(e+1).                                 (CSB4)
```

Moreover, the inverse-prolongation space `J` from the three-class
Koszul/Gram router has

```text
dim J=c_1.                                         (CSB5)
```

Equivalently, with `K_2=3r-(e+1)`, every profile is determined by `c_1`:

```text
c_2=K_2-2c_1,
c_3=r-1-K_2+c_1,
max(0,2r-e)<=c_1<=floor(K_2/2).                    (CSB6)
```

At the earlier three-source-class rank bound

```text
r_0=61083979322,       K_2=2,                      (CSB7)
```

there are exactly two conditional profiles:

```text
(c_1,c_2,c_3)=(1,0,61083979320),
(c_1,c_2,c_3)=(0,2,61083979319).                   (CSB8)
```

These two profiles are excluded by the later locator-interpolation rank
amplification. If the common source-Gram matrix is nonzero, only profiles
with `c_1>0`
can survive. More quantitatively,

```text
c_1>=max(0,2r-(n+2)).                              (CSB9)
```

## Scope

The theorem classifies the coefficient syzygy bundle. The displayed former
boundary profiles are now excluded, but the higher-rank profiles remain. A
closing argument must use split-fiber or Hankel information to eliminate
the permitted degree-one through degree-three splitting types.
