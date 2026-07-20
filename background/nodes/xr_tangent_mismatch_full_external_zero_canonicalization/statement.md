# Full-external-zero mismatch canonicalization

- **status:** PROVED
- **consumer:** `xr_tangent_support_mismatch_bridge`

In the setting of the external-zero factor reduction, fix one selected
exact-`A` witness `(p_z,S_z)` for each retained slope and put

```text
q_z=p_z-(c_0+z c_1) != 0,
Z_z={x in D\T:q_z(x)=0},       d_z=|Z_z|.
```

Then `d_z<=K-1`, the full locator `P_(Z_z)` divides `q_z`, and the quotient
has degree below `K-d_z`. On `T`, after scaling the error line by
`P_(Z_z)^(-1)`, the quotient has agreement at least `A-d_z`. Thus its
agreement excess over dimension remains at least

```text
(A-d_z)-(K-d_z)=A-K.
```

After fixing any deterministic first-match order on witness/codeword pairs,
this assigns each retained slope to one full-external-zero chart. It removes
the spray over subsets of external witness zeros, but does not bound the
number of distinct full charts.
