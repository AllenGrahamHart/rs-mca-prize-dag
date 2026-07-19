# Proof

The recurrence `(DPP8)` at `M=1` gives

```text
F_2(t)=(5t^2+2t+5)/32.                               (1)
```

The central-binomial formula `(LCC3)` similarly gives the expression for
`H_3` in `(TLF1)`.

For each row `(p,r)` in `(TLF2)`, perform arithmetic modulo `p`, put
`t=r^4` and `chi=r+r^(-1)`, and evaluate `(1)`, the next recurrence
coefficient `F_3`, and the corresponding expression

```text
tH_3^2+(chi-1)^2,
t(chi-2)^2H_3^2+(chi+2)^2,
tchi^2H_3^2+(chi-4)^2.                              (2)
```

The exact certificate replay gives, in branch order,

```text
t = 334403939, 43471449, 91117748793720439379754436,
F_3 = 90326885, 59896164, 48473322157903157538287266,
matching expression (2) = 0.                        (3)
```

It also gives exactly the three nonunit powers in `(TLF4)`. Thus every row
passes `(TLF3)` and one Legendre gate but fails source torsion.

For completeness, primality is checked by a deterministic Pocklington
certificate. The verifier recursively checks complete factorizations of
`n-1`, proves the terminal factors by trial division, and finds a Pocklington
witness for every distinct prime factor. In particular, the large third
prime uses the factor

```text
239194136603342957 | p-1,
239194136603342957 > sqrt(p),
```

with witness two; its primality is certified recursively by the same
checker. Hence all three quotient rings used above are fields of
characteristic greater than `16M=16`. The displayed arithmetic proves the
claim. QED.
