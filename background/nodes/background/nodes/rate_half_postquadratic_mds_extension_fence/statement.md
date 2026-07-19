# Post-quadratic MDS extension fence

- **status:** PROVED
- **closure:** counterexample
- **consumer:** `rate_half_band_closure`

The exact quadratic MCA staircase does not extend to the next radius by an
MDS-only argument. Let

```text
C=RS[F_5,{0,1,2,3},2],       n=4,       k=2,       r=1.
```

After nonzero parity-column scaling, take the parity-check columns to have
projective directions

```text
h_x=(1,x),       x in {0,1,2,3}.
```

There is a received pair with syndromes

```text
y_0=(0,1),       y_1=(1,4)                              (PF1)
```

that is column-far at radius one and has four CA-bad finite slopes. Explicitly,

```text
y_0+1y_1=1h_0,   y_0+2y_1=2h_2,
y_0+3y_1=3h_1,   y_0+4y_1=4h_3.                       (PF2)
```

Thus

```text
B_ca^far(n-r)>=4>r+1=2,
B_mca(n-r)>=4.                                         (PF3)
```

At `r=0` the quadratic hypothesis holds, while at `r=1` it fails:

```text
(n-r)^2-n(k+r)=9-12=-3.
```

So this is the first post-quadratic radius. It rules out extending the
official rate-half transition bound using only the universal MDS staircase or
the assertion `B_ca^far(n-r)<=r+1`. It does not refute an official
`n=2^41` theorem that uses the long smooth evaluation domain.
