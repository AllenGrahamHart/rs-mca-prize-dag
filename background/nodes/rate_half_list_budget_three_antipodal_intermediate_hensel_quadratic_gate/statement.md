# Budget-three antipodal intermediate Hensel quadratic gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_intermediate_hensel_certifier`

Retain `(IHC1)--(IHC9)` on the maximal official intermediate floor. In
addition to `Delta,kappa` from `(IHC4)`, define

```text
Delta_1=[z^h] C_*^2/B,       kappa_1=[z^(2h)] C_*.   (IHQ1)
```

For the unique normalized Hensel solution `C_u`, put

```text
q=u z^h C_*/B,       C_u=C_* V(q).                  (IHQ2)
```

Then `V` is the universal normalized solution of

```text
V^3(1+qV)=1,
V=1-q/3+q^2/3 mod q^3.                              (IHQ3)
```

Consequently

```text
C_u=C_*-(u/3)z^h C_*^2/B
          +(u^2/3)z^(2h)C_*^3/B^2 mod z^(3h).       (IHQ4)
```

Every valid intermediate solution has degree at most `2h-2`. Its first two
forbidden coefficients therefore give the simultaneous scalar gates

```text
3kappa-uDelta=0,
u^2-uDelta_1+3kappa_1=0.                            (IHQ5)
```

Thus the three cases in `(IHC8)` sharpen to

```text
Delta!=0              ==> test only u=3kappa/Delta,
Delta=0, kappa!=0     ==> reject,
Delta=0, kappa=0      ==> test at most the two roots of
                           X^2-Delta_1 X+3kappa_1.   (IHQ6)
```

In particular, the degenerate branch never retains a free scalar. Repeated
roots and nonsplit quadratics count as one or zero base-field candidates.
Every retained candidate must still pass full polynomiality, the exact
multiplied Hensel identity, quartic distinct splitting, and Möbius matching.
This theorem does not prove that those finitely many candidates reject.
