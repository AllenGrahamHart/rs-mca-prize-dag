# Proof

Use the low-margin heavy-pair basis from the degree-18 seed compiler. Anchor
it at the pair `p_0` owning at least `220` slopes, and let
`p_1,...,p_t`, `1<=t<=10`, be the other basis pairs. Their complete cores
intersect in `J_2`, where

```text
|J_2|<=K-4923.                                        (1)
```

## A fixed 31-record deck

Retain eighteen records owned by `p_0` and an off-`p_0`-line record owned by
`p_1`. If `t<=6`, take two records from every basis pair and add arbitrary
distinct low-margin fillers until there are `31` records. Every basis core
is then represented twice.

For `7<=t<=10`, start with the 32-record schedule from the degree-18
compiler and remove the second record of one twice-represented basis pair.
The resulting 31-record schedule has respectively

```text
t:                         7  8  9 10
singly represented pairs:  1  3  5  7.               (2)
```

Choose the removed record so the fixed off-line record remains. In all
cases, at most seven basis pairs are singly represented. Two records from a
fixed pair force their support intersection into its complete pair core;
one record can retain at most `theta<=387` exceptions outside that core.
Thus the exact common support `C_*` of the 31 anchors satisfies

```text
|C_*| <= (K-4923)+7*387 = K-2214 < K.                (3)
```

All records, explanations, supports, and locators are now fixed once and for
all.

## Classify every slope through one fixed star

For any post-near record `z` outside the anchor deck, put

```text
T_z=A_* union {z}.
```

Its exact common support is contained in `C_*`, hence has size below `K`.
Cancel that exact support, apply the eighteen-root degree pin, and run the
support-collapsed extraction and exact lift. The tuple remains non-global-
affine because the same eighteen dense-pair explanations and fixed off-line
explanation occur in every `T_z`. Therefore every target tuple has slope
degree `18..31` and reaches one of the lifted scalar-locator or high-
complexity interfaces.

The lift returns to the original exact locators. This point is essential:
any two target tuples share the identical `31` indexed triples

```text
(gamma_i,h_i,Lambda_i),       i in A_*.               (4)
```

The anchors themselves are covered by any one target tuple; the unsafe line
has vastly more than 31 post-near records, so such a target exists.

## C/S/A/E globalization

Apply the active first-match taxonomy to each local interface. First
maximalize the tuple's fixed explanations. If their maximal agreement sets
have nonempty common intersection, retain the tuple in route `(C)`. The
proved cancellation adapter gives a typed punctured-domain residual, but the
deployed spread theorem is not claimed on that punctured domain.

Now assume no star tuple enters `(C)`. A high-complexity tuple outside
quotient, extension, field-drop, clone, denominator-root, and near-sunflower
exceptions is a primitive spread core on the original deployed domain,
which is exactly route `(S)`. Any named failure is route `(E)`. Pure-locator
and denominator-root scalar certificates also enter `(E)` directly.

It remains to consider the case in which every target tuple is a primitive
root-free scalar-locator rational atom. Two such certificates share the 31
fixed records in (4). Atom collision rigidity says that either they are
projectively identical or their collision fixed set produces the quantified
near-sunflower/nonprimitive branch. The latter is `(E)`. Outside `(E)`, all
star certificates are therefore one projective certificate. Since the union
of the star tuples is the complete post-near family, every explanation lies
in one coherent rational atom with the same received-line owner. Owner
localization and its remaining large-owner image input are precisely route
`(A)`.

The intrinsic near deletion is disjoint and costs at most `2w=134944`.
Nothing above proves the four terminal payments. The only terminal not
already named by upstream S/A/E is the explicitly retained local
common-core residual `(C)`. This establishes the router without conflating
that residual with exception routing.
