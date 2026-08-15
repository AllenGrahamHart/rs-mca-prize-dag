# Proof

Put `n=1048598`, `m=67494`, `q=12`, and
`R_min=274980728111260126`.

## 1. Kernel capacity

Use the proved uniform corank-one cap `8147918`.  For coranks two through
nine retain the canonical-basis caps and all extension factors
`C(12,d+1)`.  The complete kernel capacity is

```text
K_cap=2273421575008467450492290640797843465217921029627020608340.
```

## 2. Full-rank capacity

The integral heavy-owner theorem scans every core `9<=j<=21`.  Its largest
chart cap is `9269974099565290` at `j=21`, so the single global rank-nine
mark capacity is

```text
G=C(n,9)*9269974099565290
 =39154510888407363352144142841152217924627132772903654230071396600.
```

The twelve-completion branch uses the parent structured vector.  In the
complementary branch, the near-saturation theorem gives the support
`2,3,4` caps

```text
26976765544297626187032777583778108529876750,
80942289326850303820580142737960784746097750,
161908567951387946577119676170547680391323000.
```

Support five retains its eleven-completion cap

```text
249353970847446220150824023617719132736307931.
```

Weighting by the exact premiums `26,18,11,5` gives the printed active
premium `P_*`.  The joint shadow ledger therefore bounds full-rank
incidence by

```text
F_cap=floor((G+R_min P_*)/45)
     =901790983907425884981637631119717314733273741651299178720895580.
```

Adding `K_cap` gives the stated total capacity.

## 3. Every admissible record count

The dense-locator theorem requires

```text
ceil((990810934/10^9) R_actual C(m,11)).
```

After clearing `45*10^9`, its record coefficient minus the sparse premium
coefficient is

```text
142592124149011960898547706352746409135803204672329212960>0.
```

At `R_min`, the full unfloored cross is

```text
55472929048268454837480986456869581783514432677116652456199927410432960>0.
```

Hence the contradiction persists for every larger record population.
Exact integer evaluation gives the printed gap.
