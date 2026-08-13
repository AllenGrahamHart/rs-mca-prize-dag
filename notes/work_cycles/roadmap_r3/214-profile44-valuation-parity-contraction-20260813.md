# Cycle 214: profile-(4,4) valuation-parity contraction

## Route screen

The cycle first screened a direct extension of the profile-`(3,6)`
unit-associate height collapse. For profile `(4,4)`, the same entropy
argument can collapse a fixed sufficiently high-cofactor ideal family to one
orbit, but the retained frontier has hundreds of distinct split-prime ideal
families. That theorem would not approach the required seven total orbits,
so it was not banked as another non-paying router.

## Joint local invariant

Instead, the four singleton positions were classified jointly by:

```text
mu = ord_(X=1) sum_(e in T) X^e over F_2,
q  = positive-half parity weight of P(X)P(X^-1).
```

Both are translation-invariant. A complete normalized census covered all
`C(127,3)=333375` supports. Independent implementations used a Hasse
bit-test/folded mask and binomial-parity/direct coefficient array.

The exact table proves

```text
mu in {3,5,6,9,10,12,17,18,20} => q in {2,4,6}.
```

Since `E=sum A_d^2` satisfies `E=q mod 4` and cycle 213 excluded `E<=4`,
every collision on those branches has `E>=6`, hence variance `V>=12`.

## Cofactor consequence

The energy-adaptive product majorant at `V=12` is

```text
U_12=20^64 exp(-16/5)(8/5)^(16/3).
```

Exact degree-27 Taylor bounds for `e^(48/5)` certify

```text
853574 P < U_12 < 853575 P,
P=B_P 2^128.
```

Applying this threshold only to the nine forced-energy branches removes
exactly twelve of the `657` former survivors and leaves `645`. No pure branch
is newly removed, and no orbit payment is claimed.

## Banked node

`e1_profile44_valuation_parity_cofactor_contraction` is PROVED with a pinned
Modal census source/run, compact exact table, primary verifier, independent
audit, and direct evidentiary edges into the E1 pair-budget and
unsafe-crossing nodes.

## Route decision

The numerical gain is real but too small to justify iterative energy-layer
enumeration. The next selected route must address multiplicity collectively:
a direct collision-graph coloring theorem, a common-prime/ideal occupancy
bound across split families, or a weighted payment not indexed one-for-one
by cofactors.
