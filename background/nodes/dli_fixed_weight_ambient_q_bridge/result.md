# Result

`PROVED` as an exact reduction.

The C2'' correlation target now has a route expressed in upstream's Q
language:

```text
weighted ambient Q
 = sum_w Bin(n,1/2)(w) (q^t/L_w) kappa_img(w)
 <= 2^21.
```

The Haar denominator needs no further lower-bound theorem; Fourier positivity
pays it by `q^-t`. The remaining work is finite ambient prefix flatness,
which consists of both image-normalized primitive Q and effective-image
occupancy with constants. This is narrower than a new multi-event correlation
theorem and directly exposes the nontransport from upstream's asymptotic Q.

Subsequent adjudication: `dli_ambient_q_sqrt_route_no_go` proves that imposing
the target square-root scale on this sufficient upper bound is false. The
bridge remains exact, but it is too lossy to replace the actual Haar
denominator in the route of record.
