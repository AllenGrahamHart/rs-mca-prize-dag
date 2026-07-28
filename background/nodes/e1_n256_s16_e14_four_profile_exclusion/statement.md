# E1 N=256 E=14 four-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor and prime-field reductions

At `N=256`, folded profile `(3,4,0)`, and variance `V=28`, all four routed
profiles are impossible collision profiles. Independent folded-chord and
direct-negacyclic engines each exhaust 26,219,123,456 vectors and agree:

```text
profile       actual   full conductor   proper conductor
(6,2)            982              540                442
(2,3)            714              184                530
(5,0,1)          100                8                 92
(1,1,1)           40                4                 36
total            1836              736               1100
```

The conductor theorem excludes all 1,100 proper-conductor representatives.
FLINT and PARI/GP agree on all 736 full-conductor norms, with 262 distinct
values. The whole-norm maximum is

```text
5848948255836721605243059534285585250067895734911016890819011517212606236162,
```

and 152 whole norms reach `2^250`. After stripping exact powers of two, the
maximum odd part is

```text
2924474127918360802621529767142792625033947867455508445409505758606303118081.
```

The inherited `odd_max<2^250` shortcut is false: six vectors, comprising
three distinct odd parts, lie in `[2^250,2^251)`. Exact PARI and FLINT
primality tests agree that all three are composite. Hence no prime
`p>2^250` divides any residual norm.
