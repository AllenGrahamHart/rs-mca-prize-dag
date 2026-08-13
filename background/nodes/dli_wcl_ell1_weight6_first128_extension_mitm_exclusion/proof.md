# Proof certificate

For a listed row write `p-1=k*2^v`, where `k` is odd and `v` is `39` or
`40`.  Trial division completely factors `k<=2205`.  For every distinct prime
factor `r` of `p-1`, the verifier finds and checks a Pocklington witness

```text
a^(p-1) = 1 mod p,
gcd(a^((p-1)/r)-1,p) = 1.
```

The known factor is all of `p-1`, hence exceeds `sqrt(p)`, so Pocklington
proves `p` prime.  Direct modular checks prove that the displayed degree is
the exact order of `p` modulo `2^41`; consequently `F_(p^degree)` is the
generated field containing the official evaluation subgroup.  The banked
integer `q=p^degree` is below `2^256`.  Since `v>=39`, every order-512 root is
already in `F_p`.

Encode a negative reduced term `-X^e` by exponent `e+256` modulo 512.  A
reduced signed weight-6 relation becomes a six-set of exponents with no equal
or antipodal pair whose roots sum to zero.  Rotation places one exponent at
zero and forbids exponent 256.  The remaining 510 indices have 255 antipodal
pairs, yielding

```text
C(510,2)-255 = 129,540 legal pairs,
C(510,3)-255*508 = 21,849,080 legal triples.
```

Every legal normalized five-set has a two/three split.  The primary search
indexes legal pairs by their field sum, scans every legal triple, and checks
all cross-compatibility conditions on a sum match.  Thus `FOUND` is equivalent
to a reduced signed relation.  Every one of the 128 records is `EXHAUSTED`.

The independent implementation sorts pair sums and uses binary search rather
than a hash table.  It exactly replays panel indices `0,63,64,127`, covering
both endpoints of both extension classes.  Its four outputs agree with the
primary records and are also exhausted.
