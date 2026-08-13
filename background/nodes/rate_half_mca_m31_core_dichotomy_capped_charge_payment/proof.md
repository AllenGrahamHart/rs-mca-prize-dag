# Proof

## High-core branch

Let a selected parameterized explanation line be

```text
c_gamma=A+gamma*p
```

with total core `G`, `|G|=g`.  Its direction `p` is a nonzero degree-`<K`
codeword, so at most `c=K-1` core coordinates lie outside the fixed
`e`-coordinate gauged direction support.  Thus its inside core has size at
least `g-c`.

Take any selected explanation with inside agreement size `h` and two line
anchors.  Their three inside agreement sets share at least

```text
(g-c)+h-e
```

coordinates.  If this is at least `K`, restriction injectivity puts the
explanation at its actual slope on the same line.  Therefore every
explanation with

```text
h>=e-g+c+K=e-g+11                              (CD1)
```

lies on that line.

Fix `b_abs=65450`.  When `g>=e+10-b_abs`, `(CD1)` absorbs every explanation
with `h>=b_abs+1`.  The exact weighted prefix `P_e(b_abs)` pays the remaining
deficits, and pair noncontainment plus off-core disjointness caps the line by
`Q=N-m+1`.  Exact replay gives

```text
max_(130222<=e<=130226) (P_e(65450)+Q)=5161307<B. (CD2)
```

This pays the entire original family as soon as any selected line enters the
high-core branch.

## Complementary capped branch

Assume no selected line enters that branch.  Every actual total core then
has the integer cap

```text
g_i<=G_e:=e+9-b_abs.                              (CD3)
```

The parent lower-aware envelope applies with `m-1` replaced by `G_e`.
Indeed, after sorting the forced lower bounds `ell_i`, start at `ell` and
greedily spend

```text
S_r-sum_i ell_i,
S_r=min(rG_e,e+C(r+1,2)c),                        (CD4)
```

filling each coordinate only to `G_e`.  The same convex exchange proves
that this vector maximizes `sum f(g_i)`.  Its floored rational sum is a valid
charge for all removed lines.

At `e=130222,130223`, every forced threshold is 18.  Fourteen total cores
of size at least 9741 give inside-core lower bounds 9736, hence

```text
14*9736-C(14,2)*5=135849>e.                       (CD5)
```

At `e=130224,130225`, every threshold is 16.  Seventy inside-core lower
bounds 2041 give

```text
70*2041-C(70,2)*5=130795>e.                       (CD6)
```

Thus the low-core branch also contradicts unsafety on all four supports.

## Adjacent wall

At `e=130226`, the guarded cutoff is 65518, weighted prefix 13575970,
line-slot count 260627, and base 13317279.  The initial forced threshold is
14, whose forced total-core lower bound is zero.  Joint charges are
nondecreasing, so later thresholds cannot increase and all subsequent lower
bounds remain zero.

Under cap `G_e=64785`, after 14763 zero-lower-bound peels, `(CD4)` has

```text
S_r=545032556=8412*64785+61136,
charge=3199542,
target=13577673.
```

The next pigeonhole threshold is one.  A slot of size two is no longer
forced, so neither core packing nor further peeling follows.  This is the
exact wall of this compiler, not an unsafe certificate.
