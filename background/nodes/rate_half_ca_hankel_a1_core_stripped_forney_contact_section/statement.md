# `A=1` core-stripped Forney contact section

- **status:** PROVED
- **closure:** contracted full-recurrence boundary divisibility
- **consumer:** `rate_half_band_crossing_location`

Retain a failing half-distance `A=1` profile with fixed core size
`s in {0,1,2}`. Put

```text
d=rho-s,       Delta=d-(s+1)e,       T>=rho+2,        (A1S1)
```

and let `C:Qbar(z;X)=0` be the residual kernel curve of bidegree `(d,e)`.
Then `C` is reduced and mixed, and the contracted Hankel recurrence produces
a nonzero section

```text
s_F in H^0(C,O_C(-rho-1,e+1)),
deg_C O_C(-rho-1,e+1)=Delta.                          (A1S2)
```

More explicitly, if `x_0,...,x_(d+rho-1)` are the contracted syndrome
moments and

```text
qbar^vee=u^d Qbar(z;u^(-1)),
N_F=[qbar^vee sum_(i=0)^(d-1)x_i u^i]_(<d),           (A1S3)
```

then the associated numerator has contact order `d+rho` at domain infinity.

## Scope

For `s=0` this recovers the core-free contact theorem. The statement does
not itself exclude a profile.
