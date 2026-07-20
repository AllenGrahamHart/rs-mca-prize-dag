# Proof

Fix `h>=4`. If two distinct `h`-subsets have the same first `h-1`
elementary symmetric functions, prefix rigidity with `m=h` and `w=h-1`
says that they differ in at least `h` points on each side. They are therefore
disjoint. At the equality stratum their two monic locators differ by a
nonzero constant. Consequently

```text
C_h=sp_(h-1)(h;H),                                 (1)
```

with the upstream convention that `sp` counts ordered pairs.

The x81 square-shift normal form identifies each F-4-minimal record with an
unordered top shift pair. The x83 dichotomy and the quotient deletion remove
the full-fiber and quotient-pullback class before a record reaches
`N_h^strip`. The x82 key convention creates at most two surviving
direct-column records from one unordered trade. Since the ordered primitive
shift-pair ledger contains exactly the two orientations of that trade,

```text
N_h^strip<=SP_h^prim<=C_h.                          (2)
```

This proves `(PSA1)`. Notice that only the quotient deletion is used. Dropping
the dihedral, moment-trade, U2-boundary, and DLI/skew deletions can only
increase the comparison count, so their operational status is irrelevant to
this upper bound.

It remains to prove the numerical compiler. Since `p>=n^2`,

```text
B_h
 <=binom(n,h)^2/n^(2h-2)
 <=n^2/(h!)^2.                                     (3)
```

Also `H_max<=n/2`, and `max(1,x)<=1+x`. Hence `(PSA3)` and `(2)` give

```text
sum_(h=4)^H_max N_h^strip
 <=7000n sum_(h=4)^H_max max(1,B_h)
 <=7000n (n/2+n^2 sum_(h=4)^infinity 1/(h!)^2).    (4)
```

For `h>=5`, consecutive squared-factorial terms have ratio at most `1/36`.
Therefore

```text
sum_(h=4)^infinity 1/(h!)^2
 <=1/576+(1/14400)/(1-1/36)
 =1/576+1/14000
 <1/553.                                           (5)
```

Substitution in `(4)` yields

```text
sum_(h=4)^H_max N_h^strip
 <(3500/n+7000/553)n^3.                            (6)
```

The coefficient is less than `14` at `n=8192`, and it decreases with `n`.
Every official row has `n>=8192`, proving `(PSA4)`. QED.

