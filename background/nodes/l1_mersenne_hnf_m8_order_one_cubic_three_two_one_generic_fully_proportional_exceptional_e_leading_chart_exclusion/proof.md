# Proof - exceptional-E leading-chart exclusion

Work over a field whose characteristic `p` belongs to `P_off`. The integers
`231=3*7*11` and `247=13*19` are nonzero modulo every such `p`, so (FEQ8)
defines

```text
z=b^2=1575/247,
s=z+27=8244/247,
q=-10s/231.                                          (1)
```

From (FEQ1),

```text
E_G=-720bq^2+(240b^2-1902b-630)q
    -40b(b^2-6b+27).                                 (2)
```

Replace every occurrence of `b^2` by `z` and collect the terms with and
without `b`. This gives (FEL3). Direct substitution from `(1)` gives

```text
C_b=-8244*3950060/(61009*5929),
C_0=3233714400/(61009*231),                          (3)
```

where `61009=247^2` and `5929=77^2`. The possible numerator obstructions for
`C_b` are `8244` and `3950060`. Their official residues are

```text
                    8191    131071    524287    2147483647
8244                  53      8244       8244          8244
3950060              1998     17930     280051       3950060.
```

Thus `C_b` is a unit in all four fields. Solving `C_b b+C_0=0` and cancelling
integer factors gives

```text
b=-C_0/C_b
 =3233714400*5929/(231*8244*3950060)
 =115275930/45228187,                                (4)
```

with

```text
45228187=229*197503.                                 (5)
```

The denominator in `(4)` is a unit: `229` is smaller than every official
prime, while the residues of `197503` at the two smaller primes are `919`
and `66432`, and `197503` is smaller than the other two primes.

Now square `(4)` and compare with `z=1575/247`. Since all denominators are
units, equality would imply

```text
0=247*115275930^2-1575*45228187^2
 =3282269389229130300-3221802516408476175
 =60466872820654125.                                 (6)
```

The four nonzero remainders in (FEL7) contradict `(6)` in every official
characteristic. Therefore (FEQ8) has no solution satisfying `E_G=0`.
The additional retained equation `X_*=0` cannot restore a solution, so the
entire fixed leading chart is empty. QED.
