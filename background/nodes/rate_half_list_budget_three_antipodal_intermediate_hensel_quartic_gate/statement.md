# Budget-three antipodal intermediate Hensel quartic gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_intermediate_hensel_cubic_gate`

Retain `(IHCQ1)--(IHCQ6)`. Define four further coefficients

```text
Delta_3=[z^(3h)] C_*^2/B,       Gamma_2=[z^(2h)] C_*^3/B^2,
Xi_1=[z^h] C_*^4/B^3,           kappa_3=[z^(4h)] C_*.       (IH4Q1)
```

The universal Hensel series has one more exact term:

```text
V=1-q/3+q^2/3-(35/81)q^3+(154/243)q^4 mod q^5.    (IH4Q2)
```

Since a valid `C_u` has degree at most `2h-2`, its coefficient at `4h`
vanishes. Therefore every valid scalar also satisfies

```text
243kappa_3-81uDelta_3+81u^2Gamma_2
             -105u^3Xi_1+154u^4=0.                 (IH4Q3)
```

Reduce `(IH4Q3)` modulo the monic quadratic in `(IHQ5)`. Write
`d=Delta_1` and `k=kappa_1`, and put

```text
C=-81Delta_3+81Gamma_2 d-105Xi_1 d^2+315Xi_1 k
      +154d^3-924dk,
D=243kappa_3-243Gamma_2 k+315Xi_1 dk
      -462kd^2+1386k^2.                              (IH4Q4)
```

Then every valid candidate satisfies the additional linear gate

```text
C u+D=0.                                             (IH4Q5)
```

Consequently the exceptional branch in `(IHCQ6)` sharpens to

```text
A=B=0, C!=0          ==> test only u=-D/C;
A=B=C=0, D!=0        ==> reject;
A=B=C=D=0            ==> retain the at-most-two roots of (IHQ5). (IH4Q6)
```

When `A` or `B` is nonzero, intersect `(IH4Q5)` with the already unique or
empty cubic-gate branch. All candidates must still pass the original linear
gate, the monic quadratic, exact polynomiality, the multiplied Hensel
identity, quartic distinct splitting, and Mobius matching. This theorem does
not prove that the exceptional quadruple `A=B=C=D=0` is empty or that its
candidates reject.
