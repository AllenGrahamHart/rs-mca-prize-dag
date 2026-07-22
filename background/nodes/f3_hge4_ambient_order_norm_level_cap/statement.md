# HGE4 ambient-order norm level cap

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_hge4_norm_gate_count`
- **dependencies:** `f3_hge4_exact_ratio_tower_orbit_compiler`,
  `f3_hge4_cyclotomic_norm_quarter_width_exclusion`

Fix an official row

```text
n=2^s,       13<=s<=41,
p prime,     p==1 mod n,       p>=n^2,
```

and an exact dyadic ratio level `m=2^a|n`, `a>=4`. If a primitive ordered
top shift pair has width `h>=4`, then

```text
n^(2 floor(h/2)) < (4h)^(m/4).                    (AON1)
```

In particular, after the proved quarter-width reduction `h<=m/4-1`, put

```text
C(m,n)=ceil(ma/(8s)),
H_amb(m,n)=2C(m,n)-1.                              (AON2)
```

Every surviving exact-level pair satisfies

```text
h<=min(m/4-1,H_amb(m,n)).                          (AON3)
```

There is a sharper parity gate. Write

```text
j=s-a,       d=m/4-h>=1.
```

Then the complete primitive population is empty whenever

```text
d even:  4(25s-36)d       <=25jm,
d odd:   4(25s-36)d+100s  <=25jm.                 (AON4)
```

The gate applies to both free and antipodal-swap pairs.

At the top level `m=n`, `(AON3)` is exactly `h<=m/4-1`. Every useful proper
level retains the stronger ambient order instead of weakening `p>n^2` to
`p>m^2`. At `n=2^41,m=2^40`, the coarse cap is

```text
h<=268173567751,
d=m/4-h>=6704339193.
```

Thus the whole free-and-swap population is empty through
`d=6704339192` at that level. The parity gate strengthens this to emptiness
through `d=6948379850`, with first potentially live defect `d=6948379851`.
This is a width deletion, not an estimate for the surviving lower widths and
not a proof of the HGE4 aggregate.
