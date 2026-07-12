# Proof

Put `x=d/ell`.  The top-band hypothesis says `x>=m-2`.  Direct expansion gives

```text
(a^2-d|T|)/ell^2
  = (1+x)^2-mx
  = x^2+(2-m)x+1.
```

For `m>=2`, the derivative of the final quadratic on `x>=m-2` is
`2x+2-m>=m-2>=0`.  It is therefore minimized at `x=m-2`, where its value is

```text
(m-2)^2+(2-m)(m-2)+1 = 1.
```

Hence `a^2-d|T|>=ell^2`, so the strict Johnson condition holds.  Since
`a-d=ell` and `|T|=m ell`, the exact bound from
`petal_k4_johnson_slice` becomes

```text
floor(m ell^2/(a^2-d|T|)) <= m.
```

This bounds the complete auxiliary list, and therefore also its
stabilizer-primitive sublist.  The only use of `r=0` is the identity
`a=ell+d`; for `r>0` the agreement is `ell+d-r`, and the displayed unit gap
need not survive.
