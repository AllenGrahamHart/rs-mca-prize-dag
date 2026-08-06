# F2 consumer guard and depth-calibration reconciliation

- **status:** PROVED
- **closure:** proof

Let

```text
N = 2^41,
q = p^e,
B0 = F_p(mu_N) = F_(p^k),
k | e,  1 <= k <= e <= 6.
```

Use `t` for the exact depth appearing in the F2 consumer guard, without
identifying it with an agreement excess or with `|Lambda|`. The banked guard
is

```text
|B0|^t >= 2^N,  equivalently  t k log2(p) >= N.       (GD-1)
```

Then:

1. The F2 block census and syndrome object are ambient-invariant at a fixed
   `t`, but a rule choosing `t` from the ambient field size is not.
2. If `t_C` is the least integer satisfying
   `t_C log2(q) >= N`, then `(GD-1)` holds exactly for generating rows
   `k=e` on every official degree/order type.
3. If `t log2(q) < N`, then `(GD-1)` fails for every official type, including
   generating rows. In particular this applies to the exact-slice `(T*)`
   depth, for which the banked deficit `N-tL` is positive.

Consequently the exact-value mass obligation obtained by substituting the
`(T*)` depth into F2's mass formulas is outside the banked F2 consumer scope.
It becomes an F2 obligation only if the proof explicitly overrides `(GD-1)`.
The theorem does not show that the alternate `f1/ext` or fixed-slice route
closes those rows.
