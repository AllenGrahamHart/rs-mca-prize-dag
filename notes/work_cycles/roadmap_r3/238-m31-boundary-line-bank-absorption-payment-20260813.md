# Cycle 238: M31 boundary-line-bank absorption payment (2026-08-13)

The fixed-cutoff stack previously closed each normalized direction class
with an outside-core line cap.  Retaining the classes as affine-line slots
is stronger.  In exact layer `h`, with direction-class cap `J_h`,

```text
|D_h| = 1-J_h + sum_(j=1)^J_h |L_(h,j)|.
```

Summing these identities above cutoff `h0=65272`, together with the
optional synchronized top line, gives

```text
|Z| <= C_e + sum_(i=1)^G_e |L_i|.
```

If the family is unsafe, one line slot is large.  Total-core packing then
forces a common core, and the existing absorption theorem puts every
high-deficit explanation on that line while one punctured ordinary-Johnson
cap pays the rest.

A constant-memory C replay pays all

```text
101157<=e<=124805.
```

At the endpoint,

```text
prefix:          1636955
line groups:       34560
base charge:      1604577
forced line:          440
forced core:        65220
low list cap:         126
final bound:     16706559
slack:              70656.
```

At adjacent `e=124806`, the same legal compiler gives `16831491`, over
budget by `54276`.  This is a method wall, not an unsafe certificate.

```text
start:                   0ffb738f0
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream frontier:       #1163-#1166; #1165 @ 6cc937eb
result:                  NARROWED; one PROVED interval payment
DAG delta:               +1 PROVED node, +5 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       124806<=e<=1044241
delta-star movement:     none
compute:                 6.7-second constant-memory C replay under RAMguard;
                         no Modal
next route action:       sharpen the line-bank low-list payment at e=124806
                         or bridge toward the high-support interval
export target:           extend przchojecki/rs-mca PR #1165
```
