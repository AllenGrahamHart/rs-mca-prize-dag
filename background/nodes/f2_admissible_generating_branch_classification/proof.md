# Proof

On the plus branch, the proved order law is

```text
ord_(2^41)(p)=2^(41-v2(p-1))_+.
```

Official admissibility gives `ord_n(p) in {1,2,4}`. Under generation this
order equals `e`, so the three plus rows in the table follow.

On the minus branch, with `b=v2(p+1)`, the proved order law is

```text
ord_(2^41)(p)=2^max(1,41-b) in {2,4}.
```

Generation again sets this order equal to `e`. Order two is equivalent to
`b>=40`, and order four is equivalent to `b=39`, giving the two remaining
types. The branches are disjoint because they have different residues
modulo four.

For nonemptiness, the companion verifier certifies the first three plus
primes and `25*2^39-1` by Pocklington using complete factorizations of
`p-1`; the prime divisors of those factorizations are checked by trial
division. It certifies `2^61-1` by Lucas--Lehmer. The displayed valuations
and the two order formulas give the claimed orders. Direct integer checks
give `p^e<2^256` in all five rows. QED.
