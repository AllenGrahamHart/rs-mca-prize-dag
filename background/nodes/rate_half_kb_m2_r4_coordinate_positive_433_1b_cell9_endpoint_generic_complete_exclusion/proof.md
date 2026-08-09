# Proof

At a leading-open point put `x=-t^2` and evaluate the common kernel as
`A(x),B(x),beta(x)`.  Since `A(x)!=0`, the missing product and squared sum
are fixed by

```text
m=B(x)/A(x),       S=x beta(x)^2/A(x)^2.
```

For `BF`, set `f=m/b`; for `sigma_c CF`, set
`f=sigma_c*m/c`.  The remaining target variables are `d,e`.  Delete the
endpoint record from

```text
de, de, -de, df, sigma_o ef, bf, sigma_c cf
```

and apply the exact paired-resultant equation to each pair in each of the 15
perfect matchings.  Saturate the resulting three equations by nonzero and
pairwise non-antipodal guards for `1,b,c,d,e,f`.

The exact Cartesian ledger has

```text
32 source points * 4 target lanes * 15 matchings = 1920 systems.
```

Singular computes a reduced unit basis in every system.  Therefore no
guarded target lift exists at any leading-open endpoint candidate. QED.
