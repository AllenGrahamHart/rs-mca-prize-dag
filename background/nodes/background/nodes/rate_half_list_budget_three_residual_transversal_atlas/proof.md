# Proof

We repeatedly use the following elementary pencil observation. Three
pairwise-coprime degree-`h` members of one constant pencil have disjoint root
sets. If the unconsumed domain is a large block `T` and an exceptional set
`E`, and the pencil parameter on `T` is a nonconstant rational function whose
fiber equation has degree at most `r`, then every further member has at most
`r+|E|` domain roots. If `h>r+|E|`, no further member can be fully
domain-split of degree `h`.

All edge roots below are distinct because the incidence blocks form a
partition of the evaluation domain.

## The dense branches

In both `K_4-e` and `K_4`, the four tight factors

```text
b_02, b_03, b_12, b_13
```

are nonzero constant multiples of four distinct linear edge locators. The
`012` and `013` triangle identities therefore give `(RTA1)`. A ratio
`c(X-a)/(X-b)` with `a!=b` is nonconstant and injective away from its pole:
equality at `x,y` reduces to `c(a-b)(x-y)=0`. The Plucker identity divided by
`b_02b_03` gives `(RTA2)`.

The exceptional factor has degree six for `K_4-e` (one full point and five
edge points) and degree eight for `K_4` (two full points and six edge points).
A further member of `<A_0,A_1>` receives at most one root from each of
`T_2,T_3`, proving `(RTA3)`. Since `deg A_0=deg A_1=d-2`, the inequalities
`d-2>8` and `d-2>10` give the thresholds `d>=11` and `d>=13`.

Now take a deficit-free triangle, for example `012`, and let `3` be its
complementary label. Its three displayed members have root sets

```text
T_2 union E_01,       T_0 union E_12,
T_1 union E_02,
```

omitting an empty edge block when appropriate. On `T_3`, the ratio of the
last two members is

```text
(A_1 e_02)/(A_0 e_12)
  =(b_13 e_02)/(b_03 e_12).
```

In `K_4-e` and `K_4` this is a nonzero scalar times a quotient of two
products of distinct linear factors. Its fiber equation has degree at most
two. It cannot be constant: equality of the numerator and a scalar multiple
of the denominator would identify their two-element root sets, but all four
displayed edge roots are distinct.

For `K_4-e`, after the three members are removed, the exceptional points are
the full point and the three edges incident with label `3`, so `|E|=4`.
For `K_4`, they are the two full points and those three edges, so `|E|=5`.
The residual caps are therefore six and seven. The member degree is `d-1`,
giving the thresholds `d>=8` and `d>=9`. The two `K_4-e` triangles are
interchanged by the canonical symmetry, and all four `K_4` triangles are
obtained by relabeling, so this proves every dense printed-pencil assertion.

## Triangle plus singleton

Here `A_0,A_1,A_2` have degree `d-1`, `A_3` has degree `d-2`, the singleton
has label `3`, and the only edge locators are `e_01,e_02,e_12`. All six
quotients are nonzero constants. The `013` identity reads

```text
q_01 e_01 A_3+q_13 A_0=q_03 A_1,
```

and the `012` identity reads

```text
q_01 e_01 A_2+q_12 e_12 A_0=q_02 e_02 A_1.
```

They prove the pencil memberships in `(RTA4)`. The first three root sets are
`T_0`, `T_1`, and `T_3 union E_01`; the remaining domain is `T_2` together
with the singleton, the full point, and the `02,12` edge points. On `T_2`,
the `012` identity gives the first formula in `(RTA5)`, an injective Mobius
map. Thus `r+|E|=1+4=5`, while the member degree is `d-1`.

For the degree-`d` pencil, the three existing members consume

```text
T_0 union E_12,       T_1 union E_02,
T_2 union E_01.
```

On `T_3`, the `013` identity makes `A_1/A_0` constant, so the displayed
pencil parameter is the second Mobius map in `(RTA5)`. Only the singleton
and full point remain exceptional. Hence the residual cap is three. The
thresholds follow from `d-1>5` and `d>3`. Permuting `0,1,2` proves the other
two degree-`d-1` pencils.

## Pendant

Here `A_0,A_1,A_2,A_3` have degrees `d-2,d-1,d-1,d`; the four edge blocks
are `03,12,13,23`; and there are no singleton or full points. The tight
`012` identity is

```text
q_01 A_2+q_12 e_12 A_0=q_02 A_1,
```

which proves `(RTA6)`. These members consume `T_2`, `T_0 union E_12`, and
`T_1`.

At a root of `A_3`, the `013` identity

```text
A_3b_01+A_0b_13=A_1b_03
```

gives `(RTA7)`. Its fiber equation has degree at most two because
`deg b_13<=2` and `deg(b_03e_12)=2`. It is nonconstant: if
`b_13=c b_03e_12`, evaluating at the root of `e_13` gives zero on the left
and a nonzero value on the right, since the `13,03,12` edge roots are
distinct. The remaining exceptional points are exactly the `03,13,23` edge
points. Thus a further member has at most five domain roots, while its degree
is `d-1`; `d>=7` suffices.

The split-fiber atlas lists `1+2+4+2+4=13` pencils outside the cycle. The
prior path theorem handles its two, and the arguments above handle the other
eleven. Every threshold is far below `d=2^39`. QED.
