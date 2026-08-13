# Cycle 235: M31 residue-zero core absorption payment (2026-08-13)

The preceding router says that an unsafe family at `e=98232` must have at
least `343071` slopes on the synchronized top affine line and total common
core at least `m-2=67452`.  Since the line direction is a nonzero
degree-`<6` codeword, at most five core coordinates lie outside the gauged
direction support.  The inside common core therefore has size at least
`67447`.

Two top anchors now synchronize every selected explanation with inside
agreement size

```text
h>=98232-67447+6=30791
```

onto that same affine line.  All remaining explanations have outside
agreement at least `67454-30790=36664`.  The single cumulative punctured
ordinary-Johnson cap at that agreement is `26`.  Charging each low
explanation by the deliberately crude owner cap `e`, and the enlarged line
once, gives the contradiction bound

```text
98232*26+981129=3535161<16777215,
```

with margin `13242054`.  Thus `e=98232` is safe and the Mersenne full-lift
residual begins at `e=98233`.

```text
start:                   ec0729752
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream frontier:       #1163-#1166; #1165 @ 785fb961
result:                  NARROWED; one PROVED support payment
DAG delta:               +1 PROVED node, +5 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       98233<=e<=1044241
delta-star movement:     none
compute:                 constant-size exact arithmetic under RAMguard;
                         no Modal
next route action:       test the same unsafe-core absorption compiler at
                         e=98233 and locate its exact interval wall
export target:           extend przchojecki/rs-mca PR #1165
```
