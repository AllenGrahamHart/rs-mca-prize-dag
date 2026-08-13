# Cycle 234: M31 residue-zero direction-class router (2026-08-13)

At the first residual support `e=98232`, the residue resets to zero and the
anchor synchronization used by the preceding two boundary closes no longer
applies.  The exact boundary layer nevertheless has a sharp internal
classification.

Fix one boundary explanation.  Every other explanation determines a
nonzero normalized codeword direction `p` that agrees with the gauged
direction on at least

```text
A=2H-e=32746
```

coordinates.  Distinct directions have intrinsic agreement sets meeting in
at most `K-1=5` coordinates.  The constant-block Johnson count therefore
allows only three direction classes.  Each class and the anchor form a
nonzero affine codeword line; outside-core packing caps that line at `484`.
Subtracting the repeated anchor gives the exact boundary cap

```text
|D| <= 1+3(484-1)=1450.
```

The independently truncated prefix through `H-1` is `16432695`.  Hence an
unsafe family would need at least `343071` slopes in the synchronized top
line.  Line packing then forces that line's common core to have size at
least `67452=m-2`.  This is a structural terminal, not a safety proof: the
remaining task is to classify or pay affine lines with only two off-core
agreements per member.

```text
start:                   8480282da
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream frontier:       #1163-#1166; #1165 @ f771b92d
result:                  NARROWED; one PROVED residue-zero router
DAG delta:               +1 PROVED node, +5 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       98232<=e<=1044241
residue-zero terminal:   unsafe => top line >=343071 and core >=m-2
delta-star movement:     none
compute:                 one exact 65k-cap replay under RAMguard; no Modal
next route action:       classify the m-2 common-core line, including the
                         one- and two-private-coordinate strata
export target:           extend przchojecki/rs-mca PR #1165
```
