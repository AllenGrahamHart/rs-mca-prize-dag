# E1 N=256 E=33 profile-(0,6,1) exclusion

- **status:** PROVED
- **closure:** proof

No pair-feasible folded-profile `(3,4,0)` collision at `N=256`, `V=66` has
autocorrelation magnitude profile

```text
(n_1,n_2,n_3)=(0,6,1).
```

For every such putative profile, its symmetric magnitude support has the
exact form

```text
b=2 1_A+1_T,
|A|=14,  A=-A,  A subset Z/128Z \ {0,64},
T={t,-t} subset A.
```

The symmetric target-fiber lemma gives the sharp bound

```text
M_3<=1644<1732,
```

where 1732 is the exact `V=66` cubic-Hermite threshold. Hence the collision
norm is below `2^250`, contradicting pair feasibility.
