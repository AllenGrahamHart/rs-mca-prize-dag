# `A=1` quadratic extremal coprime-resultant four-slack ledger

- **status:** PROVED
- **closure:** exact residual intersection capacity after mandatory factors
- **consumer:** `rate_half_band_crossing_location`

Retain the extremal paired profile and write

```text
Q(t,X)=Qbar(t;X),       G(t,X)=the split biform.
```

The two curves are coprime. Their parameter resultant

```text
R_QG(X)=Res_t(Q(t,X),G(t,X))                       (CRS1)
```

is therefore nonzero. Put

```text
d=deg_X Q=3e-2,       deg_t Q=e,
n=deg_X G=p-3,        m=deg_t G=e-2,
R=|M|=3p-3+d_A.                                   (CRS2)
```

Every classified row contains the same `m` distinct parameter roots in
the two curves. Hence

```text
R_QG(X)=L_M(X)^m T_QG(X),                          (CRS3)
```

with

```text
d_A=0: deg T_QG<=2e-5,
d_A=1: deg T_QG<=e-3.                              (CRS4)
```

Let `Z_0` be the complete set of zero-excess off-line slopes and put

```text
r_0=sum_(delta in Z_0)r_delta,
r_bad=sum_(a_delta>0)r_delta,
r_0+r_bad=e-6-d_A.                                (CRS5)
```

For every `delta in Z_0`, the padded factor `R_delta(X)` is a common
vertical-fiber factor of `Q` and `G`. When `d_A=0`, let `x_circ` be the
exceptional row. Exactly `e-3` off-line supported slopes contain it, and
each gives a common point of the two curves. Therefore

```text
d_A=0:
(X-x_circ)^(e-3) product_(delta in Z_0)R_delta(X)
 divides T_QG(X),                                  (CRS6)

d_A=1:
product_(delta in Z_0)R_delta(X) divides T_QG(X).  (CRS7)
```

After removing these mandatory factors, one obtains a nonzero polynomial
`W_QG` satisfying the unified bound

```text
deg W_QG<=4+r_bad.                                 (CRS8)
```

Every additional local intersection multiplicity at a classified row,
exceptional-row incidence, or selected padded root, and every other common
point outside the classified rows, must be paid from `(CRS8)`. Selected
actual-support roots are transverse and consume no extra multiplicity
beyond their first intersection copy.

## Scope

The theorem does not prove `r_bad=0` or force five residual intersections.
It reduces the full extremal curve intersection problem to a degree-four
core plus one allowance for each unit of padding carried by a positive-
excess slope.
