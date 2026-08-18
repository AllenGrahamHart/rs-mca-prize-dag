# DLI cyclic-band tensor and owner deletion

- **status:** PROVED
- **closure:** exact Fourier tensor identity
- **consumer:** `dli_c2pp_joint_reserve`

Let `n=4r`, let `zeta` have exact order `n` in an odd-characteristic field,
and draw `X in {0,1}^n` uniformly. Define the two cyclic Fourier null events

```text
E_1 = {sum_i X_i zeta^(fi)=0 for every f in {1+4l: 0<=l<r}},
E_2 = {sum_i X_i zeta^(fi)=0 for every f in {2+4l: 0<=l<r}}.
```

Then

```text
P(E_1)=(4/16)^r,
P(E_2)=(6/16)^r,
P(E_1 intersect E_2)=(2/16)^r,

P(E_1 intersect E_2)/(P(E_1)P(E_2))=(4/3)^r.             (CB1)
```

Thus dense cyclic-character rows and disjoint Fourier bands still do not
imply a polynomial-loss product correlation bound.

Every vector in `E_1 intersect E_2` is invariant under the shift `i->i+r`,
and hence under the antipodal shift `i->i+n/2`. Therefore

```text
Prim intersect E_1 intersect E_2 = empty.                 (CB2)
```

The complete exponential excess is quotient-periodic and is removed by the
DLI first-owner deletion.

This does not bound the truncated low-frequency bands in C2''. It proves
that cyclic phase progression and spectral disjointness alone are
insufficient, while also showing that primitive ownership exactly repairs
this canonical obstruction.
