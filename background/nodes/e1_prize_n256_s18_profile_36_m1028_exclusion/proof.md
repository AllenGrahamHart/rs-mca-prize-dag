# Proof

Write `F=S+2H`, with six signed singleton terms in `S` and three signed terms
in `H` on disjoint supports. The parent theorem gives `mu=2` and (1).

## Singleton normal form

Let the singleton exponents be `e_1,...,e_6`. The first two nontrivial Hasse
conditions for exact multiplicity two are

```text
sum_i bit_0(e_i)=0 mod 2,
sum_i bit_1(e_i)=1 mod 2.                            (2)
```

The first condition says that both parity classes have even size. If no two
members of one parity class differed in bit one, the second sum in (2) would
be a sum of even class sizes and would vanish. Thus some singleton pair has
difference `2q mod 128` for odd `q`. Translation and an odd Galois multiplier
normalize it to `{0,2}` without changing multiplicity, profile, energy, or
norm divisibility.

It therefore suffices to enumerate `{0,2,a,b,c,d}`. Among the
`binom(126,4)=10009125` normalized sets, 2503715 have exact multiplicity two.
If `Q` is the set of odd folded singleton chord classes, `E<=6` requires
`|Q|<=6`. The retained counts are

```text
|Q|=1: 169       |Q|=2: 206       |Q|=3: 3652
|Q|=4: 442       |Q|=5: 10162     |Q|=6: 5536.
```

Canonicalization under translations and all 64 odd units leaves 1603 affine
orbits.

## Exact geometry and the factor 257

The same mod-four heavy-position equation used in the `1538` and `1024`
children enumerates every target in (1). The pair-plus-third and triple-XOR
engines agree on the complete ledger:

```text
affine orbits:                    1603
singleton sign assignments:     51296
low-energy targets:            2409344
candidate heavy supports:         89224
exact heavy-sign tests:          713792
E=2,3,4,6 normalized vectors:         0
E=5 normalized vectors:                 16.
```

The element 3 has order 256 modulo 257, so `X^128+1` splits into its 128
primitive linear factors over `F_257`. Therefore

```text
257 divides Norm(F(zeta))
 iff F(3^u)=0 mod 257 for some odd u.                (3)
```

Both engines test all 128 roots in (3) for every one of the 16 geometry
hits. Neither finds a zero. A cofactor-1028 collision would have norm
`1028p`, divisible by 257, contradicting (3).
