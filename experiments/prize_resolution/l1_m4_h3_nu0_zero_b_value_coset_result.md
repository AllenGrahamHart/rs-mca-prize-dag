# Nu=0, b=0 value-coset certificate

- **status:** complete exact 16-case certificate on all four official
  `m=4` characteristics
- **script:** `l1_m4_h3_nu0_zero_b_value_coset_check.py`
- **resources:** local RAMguard, below one second, negligible memory

The exact quotient-ring output is:

```text
p=8191:        only (epsilon,eta)=(1,1), degenerate u=v=1;
p=131071:      only (epsilon,eta)=(1,1), degenerate u=v=1;
p=524287:      the degenerate pair and valid (1,-1),(-1,1);
p=2147483647:  the degenerate pair and valid (1,-1),(-1,1).
```

The valid pairs contain both roots of their quadratic. Writing
`z=s/R(0)`, with `s^2=-a`, they give `z^2+z-1=0` or
`z^2-z-1=0`. In either case `t=z^2` obeys `t^2-3t+1=0`, hence

```text
a^2+3aR(0)^2+R(0)^4=0.
```

Thus the zero-`b` arm is empty on the first two official characteristics and
has the printed invariant on the latter two. This does not exclude the
latter arm or any nonzero-`b` endpoint.
