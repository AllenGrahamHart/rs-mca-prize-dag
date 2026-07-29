# Proof

All 18 coefficients are singletons modulo two. Reducing their exponents
modulo 16, equal residues cancel in pairs. The residual parity support is an
even subset of `{0,...,15}`. The empty support has multiplicity at least 16;
the complete Hasse-derivative census over nonempty even subsets gives

```text
mu in {1,...,10}                                    (1)
```

whenever the local valuation is at most ten, and every value in `(1)` lifts
to 18 distinct exponents in `{0,...,127}`.

The square-mass-18 field-floor bound gives

```text
m<=floor(18^64/(B_P 2^128))=2013.                  (2)
```

Odd prime exponents in a conductor-256 norm are divisible by their residue
degrees, and the odd part of both the row prime and the cofactor is one
modulo 256. Intersecting `(1)--(2)` with that sieve leaves exactly

```text
2,4,8,16,32,64,128,256,512,1024,514,1028,1538.     (3)
```

The ten powers of two give ten pure ideal families. Each of 514, 1028, and
1538 has 128 split prime-ideal families. The common-ideal height argument is
profile-independent at fixed square mass 18, so every family contains at
most one 256-vector shift/sign orbit.

The cofactor-1538 exclusion depends only on square mass 18, local valuation
one, and autocorrelation, so it transports. For cofactor 1028, the universal
energy window leaves `{2,3,4,5,6}` and the four proved energy leaves exclude
that complete set. Thus only the ten pure families and 128 cofactor-514
families remain, proving

```text
T_018<=138,
|D_018|<=256*138=35328.                             (4)
```

The cofactor-514 product ceiling and logarithm/shape leaves use only square
mass, local valuation one, and autocorrelation. They transport verbatim and
confine every occupied split family to the 15 printed magnitude profiles at
energies five through twelve.

If at most five cofactor-514 ideals are occupied, `(4)` sharpens to

```text
T_018<=10+5=15,
|D_018|<=256*15=3840<3994.                          (5)
```

The dictionary multiplicity is

```text
M_33(0,18)=1117325838856821897682125205459304448.
```

Hence the worst-case charge under `(5)` is

```text
M_33(0,18)*3840/2
=2145265610605098043549680394481864540160.          (6)
```

Subtracting `(6)` from the current residual gives

```text
R=86073582443276011446219038016747383207.           (7)
```

Exact dictionary ordering makes `(4,4,S=20)` next, with

```text
M_next=522452937039935372855706187881128712.
```

Finally,

```text
floor(2R/M_next)=329,
M_next*329<=2R<M_next*330.                          (8)
```

Equations `(5)--(8)` prove the payment implication. QED.
