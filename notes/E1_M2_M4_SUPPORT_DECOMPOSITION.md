# E1 m2 and m4 support decomposition

## Status

Exact draft lemma, not a DAG node. The proof and deterministic verifier are
ready, but the Modal workspace is over its spend limit. No census or cofactor
exclusion is claimed.

## Cofactor 2

Cofactor `m=2` forces exact multiplicity one in the six-term binary
singleton support. If `o` is the number of odd exponents, the first Hasse
derivative is `o mod 2`, so

```text
o in {1,3,5}.
```

Every support therefore contains both parities and is primitive. The exact
raw and normalized counts are

```text
sum_(o=1,3,5) binom(64,o)binom(64,6-o) = 2711826432,
sum_(j=0,2,4) binom(63,j)binom(63,4-j)  =    5005539.
```

The second count fixes an odd-separated pair to `{0,1}`. The free twist
`F(X)->F(-X)` reduces the 32 normalized singleton signs to 16 while retaining
all eight heavy-sign patterns, hence 128 joint representatives.

The existing `m=514` work uses the same exact-multiplicity-one predicate and
can supply implementation code. Its committed atlases are filtered by the
small `m=514` chamber set, however, and are not a complete `m=2` atlas.

## Cofactor 4

Cofactor `m=4` forces exact multiplicity two. For mod-four occupancies
`(c_0,c_1,c_2,c_3)`, Lucas gives

```text
D_0=c_0+c_1+c_2+c_3=0,
D_1=c_1+c_3=0,
D_2=c_2+c_3=1                         (mod 2).
```

Exactly 20 of the 84 six-part occupancy compositions satisfy these
conditions. They split exhaustively into:

```text
primitive mixed-parity raw supports:      1280933888
imprimitive one-parity raw supports:        74979328
```

Every primitive orbit admits `{0,1}` normalization, and direct occupancy
counting leaves `2,501,824` normalized candidates before affine
canonicalization.

In the imprimitive branch, translation makes every singleton exponent even
and writes `P(X)=T(X^2)=T(X)^2` over `F_2`. Exact multiplicity two of `P`
therefore becomes exact multiplicity one of `T` in `Z/64`. Its normalized
support count is

```text
sum_(j=0,2,4) binom(31,j)binom(31,4-j) = 279155.
```

If all three heavy exponents are also even, the full cyclotomic norm is a
square and cannot equal `4p` for odd prime `p`. This removes
`binom(58,3)=30,856` of the `binom(122,3)=295,240` heavy triples per quotient
support. Every surviving triple has an odd heavy exponent, so `F(-X)` acts
freely on the eight heavy-sign patterns. The primitive and once-divided
branches both have 128 joint sign representatives after the twist quotient.

## Route consequence

The three remaining low cofactors now have exact first-stage support plans:

| cofactor | support branches | normalized candidate inputs | joint sign reps |
|---:|---|---:|---:|
| `2` | primitive `mu=1` | 5005539 | 128 |
| `4` | primitive `mu=2` | 2501824 | 128 |
| `4` | once-divided quotient `mu=1` | 279155 | 128 after square removal |
| `8` | primitive `mu=3` | 1269760 | 128 |

These are pre-canonicalization inputs, not orbit counts or cost projections.
The next authorized work after account re-enable is atlas measurement and an
exact product ledger, not a full radius census.

## Replay

```bash
./tools/ramguard modal -- modal run \
  experiments/prize_resolution/e1_profile_36_mu1_mu2_support_decomposition_modal.py
```
