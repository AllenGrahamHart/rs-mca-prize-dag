# Proof

The fourteen singleton coefficients survive modulo two. Reducing their
exponents modulo 16 and applying the exact Hasse-derivative test over every
even residual support of size at most 14 shows that every local valuation

```text
mu=1,...,10                                           (1)
```

occurs. Any value above ten is irrelevant because the square-mass-18 norm
ceiling gives

```text
m<=floor(18^64/(B_P 2^128))=2013.                   (2)
```

As in the preceding router, odd prime exponents in a conductor-256 norm are
divisible by their residue degrees, and both the row prime and every odd
cofactor part are `1 mod 256`. Intersecting `(1)--(2)` with that sieve gives
exactly

```text
2,4,8,16,32,64,128,256,512,1024,514,1028,1538.      (3)
```

The ten powers of two give ten pure ideal families. The other three cofactors
contain one prime above `257` or `769`, each of which splits into 128
degree-one primes. The same entropy-height argument applies because it uses
only square mass 18, the common ideal, and the cofactor; it is independent of
the decomposition `18=4a+b`. Hence every fixed ideal family contains at most
one 256-vector shift/sign orbit.

The cofactor-1538 proof likewise uses only square mass 18, local valuation
one, and the integral autocorrelation: its `V<=4` envelope, Lucas exclusion,
five finite-field types, and exact norms transport verbatim. Thus `1538` is
empty and

```text
T_114<=10+128+128=266.                              (4)
```

For cofactor `1028`, the variance window leaves energies two through six.
The energy-two logarithm lower bound, the 329-type energy-three exact norm
ledger, and the energy-five/six logarithm upper bound also use only square
mass 18, local valuation two, and autocorrelation. They transport verbatim,
leaving energy four alone.

If that final energy-four certificate is empty, `(4)` improves to

```text
T_114<=10+128=138,
|D_114|<=256*138=35328.                             (5)
```

The current residual oriented cap is `39193`, so `(5)` is sufficient. The
exact profile charge would be

```text
M_33(1,14)*35328/2
=20391647614756836040054426763033478955008.         (6)
```

Subtracting `(6)` from the current residual edge budget gives

```text
2231339193048374054995899432498611923367.           (7)
```

Exact dictionary ordering makes `(0,18,S=18)` the next profile, with

```text
M_33(0,18)=1117325838856821897682125205459304448.
```

Finally,

```text
floor(2*(7)/M_33(0,18))=3994.                       (8)
```

Equations `(5)--(8)` prove the stated payment trigger. QED.
