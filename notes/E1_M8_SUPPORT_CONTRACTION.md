# E1 m8 support contraction

## Status

Exact draft lemma, not a DAG node. The proof is algebraic and the verifier is
ready, but Modal rejected the preceding one-container probe at the workspace
spend limit. No replay, census, or critical status change is claimed.

## Statement

In prize `N=256`, profile `(3,6,S=18)`, cofactor `m=8` forces exact
multiplicity three at `X=1` in the six-term binary singleton-support
polynomial. Every such support has residue-class occupancy modulo four equal
to a permutation of

```text
(3,1,1,1).
```

Consequently it contains both parities, has no imprimitive all-one-parity
branch, admits affine normalization to contain `{0,1}`, and has only
`1,269,760` normalized candidate supports before affine canonicalization.
The free Galois involution `F(X) -> F(-X)` reduces the normalized joint sign
space from `32*8=256` to `16*8=128` representatives per heavy-position
triple.

## Proof

Let `c_r` count singleton exponents congruent to `r mod 4`. Lucas's theorem
gives the first four Hasse derivatives at one as

```text
D_0 = c_0+c_1+c_2+c_3,
D_1 = c_1+c_3,
D_2 = c_2+c_3,
D_3 = c_3                         (mod 2).
```

Exact multiplicity three means `(D_0,D_1,D_2,D_3)=(0,0,0,1)`. Hence
`c_3,c_2,c_1` are odd; because their sum with `c_0` is six, `c_0` is odd as
well. Four positive odd integers summing to six are exactly a permutation of
`(3,1,1,1)`. Conversely each such permutation has those four derivative
values, so the classification is exact.

There are 32 exponents in each residue class. Therefore the raw support count
is

```text
4 binom(32,3) 32^3 = 650117120.
```

After fixing positions zero and one, the triple class can be zero or one,
which contributes `2 binom(31,2)32^2`, or two or three, which contributes
`2 binom(32,3)32`. Their sum is

```text
1269760,
```

versus `binom(126,4)=10009125` in the unfiltered `{0,1}` atlas.

Every support meets odd residue classes. After fixing the coefficient at zero
to `+1`, `F(-X)` flips an odd singleton sign, so it has no fixed normalized
sign pattern. It preserves the cyclotomic norm and changes autocorrelation by
`A_d -> (-1)^d A_d`; hence it preserves `(E,q,L)` and product decisions. The
32 singleton sign patterns therefore form 16 free pairs while all eight
heavy-sign patterns remain represented.

## Route consequence

This is an approximately 7.9-fold support-input contraction before affine
canonicalization and a further factor-two sign contraction. The independent
Burnside ledger gives exactly `79,360` affine orbits and proves the affine
action is free. It supplies the correct first implementation for `m=8`; a
generic six-subset atlas would discard this structure. It does not exclude
any `m=8` vector or estimate the remaining radius-census cost.

When the spend limit changes, first replay this tiny lemma, then generate the
four occupancy classes in separate atomic shards. Only after measuring the
affine orbit count should a product or radius census be authorized.

## Replay

```bash
./tools/ramguard modal -- modal run \
  experiments/prize_resolution/e1_profile_36_mu3_m8_support_contraction_modal.py
```
