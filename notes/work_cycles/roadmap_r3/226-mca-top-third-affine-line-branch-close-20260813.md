# Cycle 226: MCA top-third affine-line branch close (2026-08-13)

The terminal-deficit line argument extends separately to every exact layer
`h=e-r` satisfying `e-3r>=K`.  An assigned explanation misses at most `r`
exceptional agreement coordinates.  Any three explanations therefore share
at least `e-3r` exceptional coordinates; restriction injectivity forces all
pair directions to coincide, putting the exact layer on one affine codeword
line.

For

```text
s=floor((e-K)/3),       H=e-s-1,
```

the top `s+1` exact layers have unit slope-owner weight and caps

```text
L_r <= floor((N-e-(K-1))/(m-e+r-(K-1))).
```

The lower layers retain the punctured Johnson cumulative profile.  A
conservative two-threshold bound gives

```text
prefix <= (e-1)J_floor(e/2)+J_H.
```

Across every official support `e<d`, monotonicity of the rational Johnson
cap gives the uniform constants `31` and `47`.  Every affine-line summand
is nondecreasing in `e`, so its total is maximal at `e=d-1`.  Exact endpoint
sums yield

```text
KoalaBear:   31*(67472-2)+47+9405342 = 11496959;
Mersenne-31: 31*(67448-2)+47+9405365 = 11496238.
```

Both fit their budgets.  This closes every remaining sparse-direction cell,
not merely another adjacent support:

```text
KoalaBear residual:   67472<=e<=1044238;
Mersenne residual:    67448<=e<=1044241.
```

The proof packet prints the necessary `N-m>s` outside-slack hypothesis.
The primary verifier loops over endpoint summands; the independent audit
uses quotient grouping and a sharp finite triple-overlap model.

```text
start:                   8466d6ad7
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream export head:    #1165 @ 0b7bedf7; import note posted to #1164
result:                  BRANCH CLOSED + EXPORTED; one PROVED field-general
                         compiler
DAG delta:               +1 PROVED node, +3 edges
critical status delta:   none; replacement target remains TARGET
full-lift residuals:     KoalaBear 67472<=e<=1044238;
                         Mersenne 67448<=e<=1044241
delta-star movement:     none
compute:                 exact local integer arithmetic under RAMguard;
                         no Modal
next route action:       attack e>=d using the full-lift near-MDS extension
                         structure rather than support-only list bounds
```
