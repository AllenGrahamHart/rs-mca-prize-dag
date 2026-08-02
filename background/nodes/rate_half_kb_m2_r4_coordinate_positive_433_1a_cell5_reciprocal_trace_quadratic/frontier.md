# Frontier

Use `(KBRT-3)--(KBRT-4)` instead of the four-variable common ideal.  Introduce
one conic coordinate `w` with

```text
w^2 = -48(t^2-(2i/3)t-1),
```

recover the two trace branches `u`, and only then lift `b` through
`b^2-u b+1=0`.  The deployed `F_p` rational-lift child now reconstructs
`r,c` injectively from `(b,t)` using one `r` chart and four `c` charts.
Reduce the signed `DE+`,`DE-` rows chartwise before appending the residual
`BE` cubic.

Do not rerun generic standard bases or Singular function fields at the
deployed characteristic.
