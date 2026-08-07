# Proof

It is enough to prove the `F04-R20` and `F06-R20` representatives. The exact
complete-system inversion theorem then supplies `F05-R20` and `F07-R20`.

For either representative, form the three degree-12 pseudo-remainder core
equations and saturate by

```text
V * K10 * (s^2-4*pvar).
```

Over `F_p0[inverse,x,pvar,s]`, the F04 and F06 saturated ideals have bases of
sizes 44 and 33. Recomputing each ideal with block order
`(inverse,x,pvar) > s` gives an exact seven-element basis. Localizing this
basis to `F_p0(s)[inverse,x,pvar]` and performing explicit coefficient-field
normal reduction gives three relations. In both representatives the
univariate relation is exactly

```text
pvar^2 + 2*(s+1)*pvar + (s+1)^2 = (1+s+pvar)^2.
```

The only denominators introduced in the other two triangular relations are

```text
s*(s+2)^2
s^8*(s+2)^9*(s^2+2*s+4)^2.
```

This proves that every point away from the three exceptional factors lies on
`1+s+pvar=0`. The exceptional support is exhaustive. For each representative,
adjoining any one of

```text
s,  s+2,  s^2+2*s+4
```

to the saturated ideal gives the unit ideal. Hence there are no exceptional
components, and every geometric point of the saturated representative ideal
lies on `1+s+pvar=0`.

Source reconstruction identifies `1+s+pvar` as a transported named boundary
required to be nonzero on the complete chart. Thus both representative
complete-open charts are empty. Exact inversion transports emptiness to their
companions. QED.
