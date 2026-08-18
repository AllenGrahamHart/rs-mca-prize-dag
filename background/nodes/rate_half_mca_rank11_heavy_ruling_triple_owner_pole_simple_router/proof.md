# Proof

## Triple-owner mass and common core

The heavy ruling orientation has mass `M_or=322476359` and at most
`Q_4=58361` chosen pair types. Types with one or two owners contribute at
most `2Q_4=116722`, so triple-owner types retain

```text
M_3=322476359-116722=322359637.                       (1)
```

Let `J_3` be their common pair core. If `|J_3|>=K-2`, cancel exactly `K-2`
common coordinates. As in the heavy-ruling seed, the residual
dimension-two pair-list cap is `Q_2=241`, while one fixed pair owns at most
`981115` slopes. Triple-owner types would then contribute at most
`236448715`. Restoring every one- or two-owner type gives at most

```text
236448715+116722=236565437<M_or,                      (2)
```

a contradiction. Thus `|J_3|<K-2`. Averaging (1) over at most `Q_4` types
gives a pair with at least `5524` owners.

Anchor at such a pair `p_0`. All pair components lie in the same
four-dimensional correction space. Greedily choose further triple-owner
types `p_1,...,p_t`, `t<=4`, whose component differences span those of all
triple-owner types. Their core intersection is `J_3`. Also `t>=1`: if all
components equaled the anchor, there would be one triple-owner type, which
together with every low-multiplicity type could own at most
`981115+116722<M_or` records.

## A core-saturated degree-20 packet

Choose three distinct owned slopes from every `p_i`, `i>=1`, and choose
`32-3t` slopes from `p_0`. The latter number is at least 20 and the dense
pair has 5524 available owners.

After ownership is fixed, choose each exact size-`m` support to contain its
assigned pair core. Pair noncontainment makes every core smaller than `m`,
so this choice exists. Two distinct supports from one pair intersect
exactly in that pair core. Since at least three records were selected from
every represented pair, the complete support intersection is exactly
`J_3`. Cancel it. The residual dimension is at least three, the residual
support intersection is empty, and every residual pair core has size at
least `m'-11`.

At most one of three records from `p_1` can lie on the anchor's parameterized
explanation line, so an off-line record remains. Coefficientwise slope
interpolation relative to the `32-3t>=20` anchor explanations gives degree
in `20..31`. This lies in the deployed partial-relative range.

Apply the exact support-collapsed trichotomy. The pure-locator case is
excluded exactly as in the core-saturated packet: two distinct residual
pair cores have intersection at most `K'-1`, hence union size at least

```text
2(m'-11)-(K'-1)=m'+67451>m'.                         (3)
```

Two slopes from each pair force the pure-locator coefficient polynomials to
vanish on this union, contradicting their degree-at-most-`m'` bound and
certificate nontriviality. Thus the output is high complexity, which lifts
to `chi>=2299571`, or a nontrivial rational certificate

```text
Qh_i'+(c_0+c_1 gamma_i)Lambda_i'=A'+gamma_iB',
deg Q<=67472.                                        (4)
```

## Common poles are impossible

Assume (4). Nontriviality of the rational branch gives
`(c_0,c_1)!=(0,0)`, so the affine scalar vanishes at at most one selected
slope. Let `x` be a residual domain point with

```text
Q(x)=A'(x)=B'(x)=0.                                  (5)
```

For every selected slope except possibly the unique scalar-zero slope,
(4)--(5) force `Lambda_i'(x)=0`. Every represented pair contributes three
slopes, so at least two of its supports contain `x`. Their intersection is
the saturated residual pair core. Hence `x` lies in every represented pair
core, whose intersection is empty after cancellation. This contradiction
proves that no point (5) exists.

Finally let `x` be any residual domain root of `Q`. If two selected supports
contained `x`, evaluating (4) on them would give

```text
A'(x)+gamma_iB'(x)=A'(x)+gamma_jB'(x)=0
```

at two distinct slopes. Thus `A'(x)=B'(x)=0`, contradicting the absence of
common poles. Every domain root of `Q` therefore occurs in at most one
selected support. A nonzero polynomial of degree at most `67472` has at
most `67472` domain roots, so the total pole-support incidence has the same
upper bound. QED.
