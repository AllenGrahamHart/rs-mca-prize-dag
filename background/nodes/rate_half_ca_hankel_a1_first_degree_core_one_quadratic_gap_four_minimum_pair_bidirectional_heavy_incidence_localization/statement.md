# `A=1` quadratic minimum-pair bidirectional heavy-incidence localization

- **status:** PROVED
- **closure:** both split pencils are coupled and every residual root is heavy-deficit free
- **consumer:** `rate_half_band_crossing_location`

Retain either core-one quadratic `u=4` arm and a minimum pair

```text
|S_alpha union S_beta|=rho+3,       rho=3e-1.       (BHL1)
```

Put

```text
X=S_beta\S_alpha,       |X|=r_alpha+3,
Y=S_alpha\S_beta,       |Y|=r_beta+3,
R=r_alpha+r_beta,       n=|X|+|Y|=R+6.              (BHL2)
```

The rank-two barycentric normal form is valid in **both** orientations,
without any endpoint-deficit restriction. Let `G_X,G_Y` be the common
parameter gcds of the row forms on `X,Y`. They have one common degree `g`
and one common nonendpoint root set `C`:

```text
Z(G_X)=C disjoint_union {beta},
Z(G_Y)=C disjoint_union {alpha},
|C|=g-1.                                             (BHL3)
```

Let `R_x` be the `e-g` roots left after removing `G_X` or `G_Y` from the
row form at `x in X union Y`. Then all `n` sets `R_x` are pairwise disjoint,
and

```text
r_delta=0       for every delta in union_x R_x.     (BHL4)
```

Let `Sigma` be the set of `T=3e+3` supported slopes. Write

```text
L=C union {alpha,beta},       |L|=g+1,
W=Sigma \ (L union union_x R_x),
s=|W|=(R+5)g-(R+3)e+2.                              (BHL5)
```

Thus `s>=0`, every positive heavy deficit lies in `L union W`, and

```text
(R+5)g >= (R+3)e-2.                                 (BHL6)
```

If `d_L=sum_(delta in L)r_delta`, exact missing-incidence counting on the
endpoint center line gives

```text
3g+d_L<=3e-2.                                       (BHL7)
```

The packet-wide deficit is `e-6`. Since a slope in `W` has deficit at most
one in the double-root arm and at most two in the two-simple arm,

```text
double root:  d_L>=e-6-s,
              (R+2)g>=(R+1)e-6;

two simple:   d_L>=e-6-2s,
              (2R+7)g>=2(R+2)e-8.                  (BHL8)
```

Combining `(BHL6)` and `(BHL8)`, for the official
`e=183251937963` the lower bounds are

```text
              R=0             R=1             R=2
double   109951162778    122167958642    137438953471

              R=0             R=1             R=2
two      109951162778    122167958642    133274136700

              R=3             R=4
two      140963029202    146601550370.              (BHL9)
```

## Scope

The theorem localizes the supported heavy-row factors: they cannot meet any
residual split-pencil root set. It does not prove `W` empty, force all heavy
incidences into `G_X union G_Y`, or exclude a minimum pair. Those are the
remaining compatibility tasks.
