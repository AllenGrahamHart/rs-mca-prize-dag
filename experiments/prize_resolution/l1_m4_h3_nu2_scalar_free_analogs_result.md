# Nu=2 scalar-free small-analogue census

- **status:** complete exact analogue census
- **script:** `l1_m4_h3_nu2_scalar_free_analogs.py`
- **resources:** local RAMguard, below one second, negligible memory
- **official-row effect:** none

The script enumerates every unordered pairwise-distinct positive multiplicity
triple summing to each declared `p`. It first applies the two exact
fixed-point sign equations, constructs the canonical scalar-free `F_e` only
for survivors, and then divides `W^(4(p+1))-1` by
`F_e^3-2F_e+1` over `F_p`.

```text
p=7   triples=1     sign_hits=0   divisibility_hits=0
p=31  triples=65    sign_hits=3   divisibility_hits=0
p=127 triples=1281  sign_hits=19  divisibility_hits=0
```

Thus the sign equation is a meaningful sieve and the full divisibility kills
every surviving passport in these complete analogues. This is evidence for
official emptiness and a conformance oracle for `CR-L1-MCP-NU2`; it is not an
official-characteristic exclusion or an asymptotic theorem.
