# `A=1` core-one quartic-carrier exclusion

- **status:** PROVED
- **closure:** degree-four pole interpolation with carrier descent
- **consumer:** `rate_half_band_crossing_location`

Retain a failing half-distance `A=1` profile with fixed core `s=1`. Put

```text
d=rho-1,       Delta=d-2e,       T=4e+1-ell,
p<=O<=Delta,   b=floor(p/5).                            (QCE1)
```

Assume

```text
3(e+1)<rho+1.                                          (QCE2)
```

Then the profile is impossible whenever

```text
b+ell+3<e.                                             (QCE3)
```

The point not covered by the ordinary noncontainment argument is also
excluded. If a pole-clearing form of bidegree `(4,b)` contains a component
on which the Forney contact section is nonzero, that component must have
bidegree `(4,1)`. All other components are contact-inactive, so the Forney
numerator factors through them. Dividing the full recurrence by their
product would leave a degree-four rational kernel vector for a pencil whose
primitive kernel has degree `d>4`, a contradiction.

On the official row `rho=4m`, `m=2^37`, the bounds `p<=Delta` and
`ell<=4e-rho-1` therefore exclude the complete core-one prefix

```text
m+1<=e<=floor(16m/13)-1.                              (QCE4)
```

The first core-one degree not excluded by this theorem is

```text
floor(16m/13)=169155635042.                            (QCE5)
```

## Scope

The theorem does not exclude core-free profiles or core-one degrees at or
above `(QCE5)`.
