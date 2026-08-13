# Cycle 230: full-lift mean-Gram/global-line profile (2026-08-13)

The cross-layer global-line node stopped when the coarse Johnson cap at
`H=e-floor((e-K)/3)-1` changed sign. The already-proved mean-centered Gram
cap is legal at that exact boundary. Composing the full suffix-minimum
prefix profile with the one-time high-union line charge gives

```text
|Z| <= sum_(h=1)^H (B_h-B_(h-1))*floor(e/h) + (N-m+1).
```

The exact profile, rather than the weaker two-threshold substitution, pays

```text
KoalaBear:   e<=96150, endpoint 479693401;
Mersenne-31: e<=98229, endpoint 16488216.
```

At KoalaBear `e=96151`, the `H=64105` cap loses theorem legality with
`T=-4625043784`. At Mersenne `e=98230`, every cap remains legal but the
profile is `17415873`, over budget by `638658`. Neither is unsafe.

```text
start:                   ed3154d06
canonical prize:         c8d48cd4b (no newer Fable commit)
result:                  NARROWED; one PROVED composition node
DAG delta:               +1 PROVED node, +4 edges
critical status delta:   none; replacement target remains TARGET
full-lift residuals:     KoalaBear 96151<=e<=1044238;
                         Mersenne 98230<=e<=1044241
delta-star movement:     none
compute:                 528 official supports and about 34 million
                         constant-memory cap cells under RAMguard;
                         no Modal
next route action:       improve the Mersenne prefix profile by 638658 or
                         replace the KoalaBear endpoint chord theorem;
                         in parallel, attack rank-10 exception-12
export:                  przchojecki/rs-mca PR #1165 head c09423b8b;
                         manuscript corollary, exact note, and verifier;
                         #1164 comment 5276545030;
                         #1166 dependency comment 5276545038
```
