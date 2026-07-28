# Proof

The parent theorem gives `mu=9` and `2<=E<=17`.

## Singleton normal form

The exact binary residue ledger modulo `(X+1)^16` has 16 parity supports of
multiplicity nine. Every one has weight four and contains a pair of opposite
parity. Translation and an odd Galois multiplier therefore normalize that
pair to `{0,1}`. It suffices to enumerate

```text
{0,1,a,b,c,d}.                                      (1)
```

Among the `binom(126,4)=10009125` supports in (1), exactly 46592 have
multiplicity nine. Their odd folded-chord weights and raw counts are

```text
q=6:128, 7:768, 8:1024, 9:3328, 10:2176,
q=11:10496, 12:1024, 13:5888, 14:3328, 15:18432.
```

Affine canonicalization leaves 2912 orbits.

## Radius-two mod-four census

For a fixed singleton support let `Q` be its odd-chord set, `|Q|=q`. Every
target autocorrelation has an odd entry on `Q`, contributing at least `q` to
its energy. Outside `Q` every entry is even. If `T` is the set of outside
coordinates whose half-entry is odd, each member contributes at least four,
so

```text
|T|<=floor((17-q)/4)<=2.                            (2)
```

Projecting the three-heavy mod-four equation onto the complement of `Q`
therefore says that the XOR of the three heavy columns lies within the exact
Hamming ball (2) around a singleton-sign-dependent mask.

The primary engine stores projected column pairs, then probes every third
position and every radius error. The audit engine independently stores all
projected column triples and probes only the error ball. Both replay all eight
heavy signs for every support candidate and agree exactly:

```text
affine orbits:                  2912
singleton sign assignments:   93184
candidate heavy supports:     438120
exact heavy-sign tests:      3504960
primary XOR probes:       2198607872
audit XOR probes:           18021376.
```

They find no vector at energies 2 through 14 or 16, exactly two at energy 15,
and exactly two at energy 17.

## Exact norms

The four vectors have two distinct norms. FLINT resultants and independent
PARI/GP resultants agree exactly. Every norm has valuation nine, hence is
divisible by 512, but all four quotients satisfy

```text
Norm(F)/512 < B_P 2^128.                            (3)
```

A cofactor-512 collision would have `Norm(F)=512p` with
`p>=B_P 2^128`, contradicting (3).
