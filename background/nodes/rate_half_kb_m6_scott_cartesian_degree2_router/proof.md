# Proof

## Setup

Write the terminal decomposition as

```text
f=F composed h,        deg(h)=6,        deg(F)=10.
```

Let `G` be the degree-60 geometric monodromy group, let
`B_0,...,B_9` be the ten blocks of size six, and let `N` be the kernel of
the action on those blocks. The imported actual quartic component gives a
point-stabilizer suborbit `Delta` of size four that meets blocks other than
`B_0`.

The complete primitive degree-six catalogue is

```text
H          order       socle       subdegrees
A5            60       A5          1,5
S5           120       A5          1,5
A6           360       A6          1,5
S6           720       A6          1,5
```

because the terminal inner map is indecomposable.

## Trivial block kernel

Suppose `N=1`. Then `G` is one of the 45 transitive degree-ten groups. If
`A<G_0<G` is the endpoint-stabilizer chain, then

```text
[G:G_0]=10,       [G_0:A]=6.
```

The primitive quotient of `G_0` has order divisible by 60. Hence
`600` divides `|G|`. The pinned complete catalogue leaves exactly

```text
[A5^2]2, two index-two forms of [S5^2]2, [S5^2]2, A10, S10.
```

For `A10`, the degree-ten point stabilizer is `A9`. A homomorphism from
simple `A9` to `S6` is trivial because an injection is excluded by order.
For `S10`, the point stabilizer is `S9`; its only proper nontrivial normal
subgroup is `A9`, and the resulting quotient has order two. Neither point
stabilizer has a transitive degree-six quotient.

The four remaining groups preserve two five-point blocks and have socle
`A5 x A5`. The point stabilizer meets that socle in `A4 x A5`, so its only
nonabelian composition factor is the remote `A5`. Consequently its
primitive degree-six quotient is the standard `A5` or `S5` action. Its
point stabilizer is the normalizer `D10` or `F20` of a five-cycle.
More explicitly, the remote `A5` maps isomorphically onto the quotient
socle. In the order-720 point stabilizer, the remaining `A4` has no
order-two quotient, so the image is `A5`. In the other three cases an
element inducing the outer automorphism of the remote `A5` is present, so
the image is `S5`; it cannot map into `A5` because that outer automorphism
is not inner. The index-six subgroups are conjugate five-cycle normalizers.
Thus every admissible primitive chain is conjugate to a row audited below,
rather than merely sharing its order.
The complete chain table is

```text
G type                 |G|     |G_0|  H    |A|  |M|  [M:A]
[A5^2]2               7200       720  A5   120   600    5
parity wreath, split 14400      1440  S5   240  1200    5
parity wreath, twist 14400      1440  S5   240  1200    5
[S5^2]2              28800      2880  S5   480  2400    5
```

Here `M` is obtained by enlarging the local `A4` or `S4` point
stabilizer to `A5` or `S5`, while retaining the remote five-cycle
normalizer. The independent verifier constructs all four groups from the
pinned catalogue generators and checks every displayed order and
inclusion. Thus `A<M<G` gives a monodromy block of size five, forcing an
inner-degree-five decomposition. The proved challenge-field degree-five
exclusion removes every kernel-free case.

## Nontrivial block kernel

Now suppose `N` is nontrivial. If `P_i` is its image on `B_i`, normality
and almost simplicity imply that `P_i` contains the simple socle `S_i`.
Thus `D=[N,N]` is subdirect in ten copies of `A5` or `A6`. Scott's lemma
partitions the coordinates into diagonal strips whose support sizes divide
ten.

A strip may be twisted. Call two coordinates compatible when their twist
is realized by a bijection of the six-point socle actions. Compatibility
classes are permuted by `G`, so they form a uniform invariant refinement
of the Scott supports.

Fix `alpha` in `B_0`. In a compatible coordinate of the same strip,
`D_alpha` has orbits of sizes one and five: one synchronized counterpart
and the other five points. In an incompatible `A6` coordinate it has no
fixed point. Since an `A5` subgroup has no proper orbit of size two, three,
or four on six points, that action is transitive. In a different Scott
strip, an independent simple factor is also transitive. Therefore a
four-point `D_alpha`-invariant suborbit can contain only synchronized fixed
counterparts in the compatibility class of `B_0`.

That class must contain at least five coordinates. Its uniform size divides
ten, so it is exactly five or ten. Triviality of the two-transitive action
centralizer lets the compatible twists be untwisted, and the synchronized
columns are monodromy blocks of that class size.

Size five gives the already excluded inner-degree-five decomposition.
For size ten, let `k` be the resulting degree-ten inner map. The four
points of `Delta` are in the same synchronized column as `alpha`; hence
they form a same-fiber suborbit of size four for `k`. If `k` were
indecomposable, its monodromy would be one of the nine primitive
degree-ten groups, whose nontrivial subdegrees are `3,6` or `9`, never
four. Therefore `k` has a proper right factor of degree two or five.
The degree-five alternative is impossible, leaving an inner-degree-two
decomposition.

Thus every `m=6` producer dies or routes to `m=2`. Removing its six types
from the prior 18-type frontier leaves 12 independent types in degrees
`2,3,4`. QED.
