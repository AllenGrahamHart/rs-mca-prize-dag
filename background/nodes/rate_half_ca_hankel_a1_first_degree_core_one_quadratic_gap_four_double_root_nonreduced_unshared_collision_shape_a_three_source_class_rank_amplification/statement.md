# `A=1` shape-A three-source-class rank amplification

- **status:** PROVED
- **closure:** every Shape-A split biform has separation rank at least
  `ceil((e+1)/3)`
- **consumer:** `rate_half_band_crossing_location`

Retain Shape A. Let `Qbar(t,X)` be the first-degree core-one primitive
locator and let `G(t,X)` be the extremal dual-MDS split biform. Then

```text
sr(Qbar)=e+1,
deg_X Qbar=d=3e-2,
deg_X G=n=(3e-7)/2,
|U_0|=R=(9e-7)/2.                                  (SRA1)
```

The Shape-A condition has `d_A=1`, so the source partition is

```text
U_0=M_alpha disjoint_union M_beta disjoint_union M_theta. (SRA2)
```

Consequently

```text
sr(G)>=ceil((e+1)/3).                              (SRA3)
```

On the official row,

```text
e=183251937963,
sr(G)>=61083979322.                                (SRA4)
```

Thus tensor ranks below `61083979322`, including the complete rank-two and
rank-three branches, are impossible. Every surviving Shape-A biform has
macroscopic separation rank.

## Scope

The theorem does not exclude ranks from `ceil((e+1)/3)` through the ambient
maximum `e-1`. It strengthens the Shape-A frontier but does not close Shape
A or move the rate-half endpoint.
