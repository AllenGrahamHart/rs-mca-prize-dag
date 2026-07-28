# E1 N=256 E=24 six-profile exclusion

- **status:** PROVED
- **closure:** exact finite computation plus proved conductor reduction

At `N=256`, folded profile `(3,4,0)`, and variance `V=48`, all six profiles
from the E24 router are impossible collision profiles.

Two independent actual-vector engines each exhaust 3,056,582,144 signed
vectors on 154 affine templates.  Their exact per-profile census is

```text
profile        actual   full conductor   proper conductor
(4,5)           10878             5870               5008
(0,6)               0                0                  0
(3,3,1)          2780              836               1944
(2,1,2)           306               30                276
(4,1,0,1)         452               98                354
(0,2,0,1)           0                0                  0
total            14416             6834               7582
```

The proved conductor theorem excludes the 7,582 proper-conductor vectors.
FLINT and PARI/GP agree on the exact cyclotomic norm of every full-conductor
representative.  Among 6,834 vectors there are 2,684 distinct norms and

```text
N_max = 934000596876556404040131946795508791323292938762264172037712523409677324304,
N_max < 2^250 < 2*N_max.
```

Thus no pair-feasible row prime can divide any residual norm.
