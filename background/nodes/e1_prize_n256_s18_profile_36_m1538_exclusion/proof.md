# Proof

Write the coefficient polynomial as

```text
F=S+2H,
```

where `S` has six coefficients in `{+1,-1}` and `H` has three coefficients
in `{+1,-1}`, on disjoint supports. Let `P` be the support polynomial of `S`
over `F_2`. Cofactor `1538` has 2-adic valuation one, so the parent theorem
gives

```text
ord_(X=1)(P)=1.                                      (2)
```

## Complete singleton-support reduction

Condition (2) says that the sum of the six singleton exponents is odd. Hence
the singleton support contains an opposite-parity pair. Translation sends one
endpoint to zero, and multiplication by an odd unit modulo 128 sends their
odd difference to one. These operations are a monomial shift and a Galois
automorphism; they preserve energy and the coefficient profile, allowing for
sign changes that are enumerated below.

It therefore suffices to enumerate

```text
{0,1,a,b,c,d},       2<=a<b<c<d<=127.                (3)
```

There are `binom(126,4)=10009125` sets in (3), of which `5005539` satisfy
(2). Let `Q` be the set of positive-half lags where the singleton
autocorrelation is odd. If `E<=6`, then `|Q|<=6`. Exact folded-chord parity
leaves the following normalized counts:

```text
|Q|=1: 297       |Q|=2: 18        |Q|=3: 6836
|Q|=4: 350       |Q|=5: 11490     |Q|=6: 8216.
```

Canonicalizing by all support-point translations and all 64 odd units gives
exactly 1969 affine orbits. The committed orbit file prints every
representative.

## Mod-four heavy-position equation

For fixed singleton support and signs, write `A_S` for the 63 positive-half
autorrelations. If a target has energy at most six, every odd entry is
`+1` or `-1`, while an even entry is zero except for at most one entry equal
to `+2` or `-2`. Thus every target with energy in `{2,...,6}` is one of:

```text
E=|Q|,             signs independently chosen on Q;
E=|Q|+4<=6,        the same plus one signed magnitude-two entry off Q. (4)
```

Modulo four, the three heavy signs disappear after division by two:

```text
(A_target-A_S)/2
 = P H^* + H P^*                  in F_2.             (5)
```

For each possible heavy position `h`, the right side of (5) contributes one
explicit 63-bit folded-chord column. Hence the support of `H` must solve an
exact three-column XOR equation.

The complete ledger covers all 1969 support orbits, all
`1969*32=63008` singleton sign assignments after fixing global sign, and all
2216832 targets in (4). The primary engine stores two-column XORs and probes
the third position, making 270453504 lookups. An audit engine independently
stores all three-column XORs and makes one lookup per target. Both find the
same 16970 heavy-support candidates and replay all eight heavy-sign choices,
for 135760 exact autocorrelation tests. Neither finds energy in `{2,...,6}`.

The lower boundary is sharp: the committed verifier checks the `mu=1`,
energy-eight vector

```text
-X^5 +X^16 -2X^27 -X^36 +X^38 -2X^69 -2X^80 +X^102 +X^122.
```

This proves (1). The parent has already excluded `V=0,2`, and its logarithmic
window leaves only `V=4,6,8,10,12` for `m=1538`. All are now impossible.
