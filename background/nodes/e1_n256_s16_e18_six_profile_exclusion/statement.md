# E1 N=256 E=18 six-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=36`, all six routed
profiles are impossible collision profiles. Independent folded-chord and
direct-negacyclic engines each exhaust 26,219,123,456 vectors and agree:

```text
profile        actual   full conductor   proper conductor
(6,3)            2410             1100               1310
(2,4)            3096             1622               1474
(5,1,1)           842              226                616
(1,2,1)           208               18                190
(0,0,2)             4                0                  4
(2,0,0,1)         152               28                124
total             6712             2994               3718
```

The conductor theorem excludes all 3,718 proper-conductor representatives.
FLINT and PARI/GP agree on all 2,994 full-conductor norms, with 895 distinct
values. Six whole norms are at least `2^250`; this refutes the stronger whole-
norm cutoff. Removing each norm's power of two gives

```text
N_max     = 3244660049331064070204285700733501169431397018164712582311239362105072116226,
odd_max   = 1622330024665532035102142850366750584715698509082356291155619681052536058113,
odd_max < 2^250 < 2*odd_max.
```

No odd part reaches `2^250`. Since a pair-feasible row prime is odd and
greater than `2^250`, it divides none of the residual norms.
