# Replay and candidate thresholds

The finite verifier exhausts two small RS syndrome charts, checks every
high-direction line against the exact Hamming-ball bound, and includes a
low-direction mutation with `q>N^2` on which all field slopes lie in the ball.
It also computes the exact excess threshold for an MDS chart direction at all
six XR candidates. Modal app `ap-FC3D6o03DHNPeQylx9YCPz` returned

```text
XR_DIRECTION_DISTANCE_RAY_BOUND_PASS
finite_max=3,2 paid_directions=12,104
rowc-r1_4:d<=0 rowc-r1_8:d<=0 rowc-r1_16:d<=0
prize-r1_4:d<=45210182 prize-r1_8:d<=38693399
prize-r1_16:d<=8985287
```

The focused verifier completed in `0.155` seconds on its Modal worker. The
large prize-row thresholds are conditional only on the chart direction being
MDS, meaning `d_U(y_1)=R`; arbitrary directions use the exact displayed
distance test in the theorem.
