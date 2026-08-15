# Uniform corank-three projective cap

- **status:** PROVED
- **proposition:** every official corank-three canonical-basis chart has at
  most `983902549` records.

After deleting all global zero normals, put `a=t+1`.  The incident normal
matroid is loopless rank four on `m=a+67474` elements, every parallel class
has size at most `a`, and every rank-two flat has size at most `a+1`.
The rank-four bounded point/line theorem supplies the exact recursive basis
floor `Q_a(67474)`.  Double counting gives

```text
M_3(t)<=floor((1048576+t)_rise_4/(4Q_a(67474))).
```

An exact finite certificate checks every `0<=t<=1048566`; the maximum is
`983902549` at `t=0`, and no row exceeds it.
