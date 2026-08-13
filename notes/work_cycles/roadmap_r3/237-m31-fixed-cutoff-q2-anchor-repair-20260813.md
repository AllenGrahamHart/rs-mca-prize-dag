# Cycle 237: M31 fixed-cutoff residue-two anchor repair (2026-08-13)

The first support beyond the fixed-cutoff interval has residue `q=2`.
That residue pays exactly the two units needed to synchronize both boundary
layers with two top anchors.  Splitting by the number of top anchors, and
then by whether first-boundary missed sets intersect, gives five exhaustive
cases.

At `e=101156`, the optimized fixed-cutoff charge is `16895280`.  Removing
the first two boundary charges leaves `16352671`.  In the two-top case,
unsafety would force at least `424545` members on the synchronized line,
hence common core `67452=m-2`; the existing core-absorption theorem then
gives the contradiction bound `3813497`.

The remaining four cases replace the coarse first-boundary charge by either
the outside-core line cap `94742`, the small cardinality cap one, or the
pairwise-disjoint missed-set cap three.  Their largest bound is

```text
16705799 < 16777215,
```

with slack `71416`.  Thus `e=101156` is safe.  At adjacent `e=101157`, the
residue resets to zero, so this repair stops there without claiming an
unsafe certificate.

```text
start:                   4ed5eeb60
canonical prize:         c8d48cd4b (no newer Fable commit)
upstream frontier:       #1163-#1166; #1165 @ f2936369
result:                  NARROWED; one PROVED support payment
DAG delta:               +1 PROVED node, +5 edges
critical status delta:   none; replacement target remains TARGET
Mersenne residual:       101157<=e<=1044241
delta-star movement:     none
compute:                 constant-size exact arithmetic under RAMguard;
                         no Modal
next route action:       repair the residue-zero wall at e=101157 using a
                         sharper boundary-class or top-size split
export target:           extend przchojecki/rs-mca PR #1165
```
