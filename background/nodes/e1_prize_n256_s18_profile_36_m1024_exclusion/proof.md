# Proof

Write the coefficient polynomial as

```text
F=S+2H,
```

where `S` has six signed singleton terms and `H` has three signed terms on
disjoint supports. The parent theorem gives `mu=10` and (1).

## Singleton normal form

Modulo `(X+1)^16`, reduce the six singleton exponents modulo 16 and cancel
equal residues in pairs. The exact Hasse-derivative ledger has eight
parity-support patterns of multiplicity ten; every one has weight four and
contains two residues whose difference is `2 mod 4`. Lifting those residues
gives a singleton pair of separation `2q mod 128` for odd `q`.

Translation sends its first endpoint to zero. Multiplication by an odd unit
inverse to `q` modulo 64 sends the second to two. These operations are a
monomial shift and a Galois automorphism, so they preserve the coefficient
profile, energy, and root multiplicity. It suffices to enumerate

```text
{0,2,a,b,c,d}.                                      (2)
```

Among the `binom(126,4)=10009125` sets in (2), exactly 32256 have
multiplicity ten. If `Q` is the set of odd folded singleton chord classes,
energy at most six requires `|Q|<=6`. The retained normalized counts are

```text
|Q|=2: 32       |Q|=3: 112      |Q|=4: 96
|Q|=5: 336      |Q|=6: 224.
```

Canonicalization under all support-point translations and all 64 odd units
leaves exactly 68 affine orbits.

## Exact low-energy exclusion

For each orbit, fix global singleton sign and enumerate the remaining 32
singleton sign assignments. As in the cofactor-1538 proof, every target with
energy two through six has signed unit entries on `Q` and at most one signed
magnitude-two entry off `Q`. After subtracting the singleton autocorrelation
and dividing by two, reduction modulo two gives the exact three-heavy-column
XOR equation.

The primary engine stores two heavy columns and probes the third. The audit
engine independently stores every three-column XOR. Their complete ledgers
agree exactly:

```text
affine orbits:                 68
singleton sign assignments: 2176
low-energy targets:        194816
candidate heavy supports:      606
exact heavy-sign tests:        4848.
```

Neither engine finds a vector of energy two through six. This contradicts
(1), so cofactor `1024` is impossible.
