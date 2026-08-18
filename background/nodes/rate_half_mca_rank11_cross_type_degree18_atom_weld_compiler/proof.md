# Proof

Fix distinct large types `p,q`. Relative to `p`, start the component-span
greedy algorithm with the nonzero difference `q-p` and extend it using
actual triple-owner types until all pair-component differences are spanned.
All components lie in the same four-dimensional correction space, so the
selected secondary set has size `1<=t<=4`. Write it as

```text
q,p_2,...,p_t.
```

Because `q-p` is selected, the same represented type set recovers all
component differences relative to `q`: subtracting `q-p` translates every
difference based at `p` to one based at `q`. The intersection of the pair
cores of these `t+1` represented types is therefore the complete
triple-owner core `J_3` for both anchors.

Put

```text
b=17-3t.
```

Since `t<=4`, `b` is one of `14,11,8,5`. The `p`-anchored packet consists
of 18 records of `p`, `b` records of `q`, and three records of every
`p_2,...,p_t`. The `q`-anchored packet is symmetric. Both have size

```text
18+b+3(t-1)=32.                                      (1)
```

The large anchor and counterpart types have at least 29 records, and every
other selected type is triple-owner, so all choices exist.

Choose the same `b` records of `p` inside the first packet's 18 anchor
records and the second packet's counterpart records; do the symmetric thing
for `q`, and choose the same three records from every other type. The shared
deck has size

```text
r=2b+3(t-1)=31-3t in {28,25,22,19}.                  (2)
```

Core-saturate every exact support. Every represented type contributes at
least three records, so two supports recover its exact pair core and the
complete packet intersection is `J_3` in both packets. After canceling this
same core, the residual dimension and pair-core properties are exactly those
of the parent pole-simple packet.

Interpolate the 32 explanations coefficientwise in the slope. Eighteen
values lie on the anchor's affine codeword line. At most one record of the
distinct counterpart type lies on that line, while `b>=5`, so an off-line
value exists. The interpolation error is nonzero with 18 roots and degree at
most 31. Its degree is therefore in `18..31`, the deployed partial-relative
range.

Apply the exact support-collapsed trichotomy. The pure-locator branch is
excluded by the same union argument as the parent: two distinct represented
pair cores have union larger than `m'`. Hence each packet emits high
complexity `(AW2)` or a nontrivial scalar-locator rational certificate. The
parent common-pole argument uses only three records from every represented
type, which this construction retains, so each rational certificate is
pole-simple.

If neither packet is high complexity, the two rational certificates share
the `r>=19` supports in `(2)`. The deck contains at least five records from
each of `p,q`. The cross-type pole-simple atom-identity theorem applies and
makes the certificates projectively identical. QED.
