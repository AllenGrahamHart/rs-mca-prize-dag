# Budget-three antipodal intermediate Hensel cubic gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_intermediate_hensel_quadratic_gate`

Retain `(IHQ1)--(IHQ6)`. Define three further coefficients

```text
Delta_2=[z^(2h)] C_*^2/B,
Gamma_1=[z^h] C_*^3/B^2,
kappa_2=[z^(3h)] C_*.                                (IHCQ1)
```

The universal Hensel series has one more exact term:

```text
V=1-q/3+q^2/3-(35/81)q^3 mod q^4.                  (IHCQ2)
```

Since a valid `C_u` has degree at most `2h-2`, its coefficient at `3h`
vanishes. Therefore every valid scalar also satisfies

```text
81kappa_2-27uDelta_2+27u^2Gamma_1-35u^3=0.          (IHCQ3)
```

Reduce `(IHCQ3)` modulo the monic quadratic in `(IHQ5)`. Put

```text
A=-27Delta_2+27Gamma_1Delta_1-35Delta_1^2+105kappa_1,
B=81kappa_2-81Gamma_1kappa_1+105Delta_1kappa_1.     (IHCQ4)
```

Then every valid candidate satisfies the additional linear gate

```text
A u+B=0.                                            (IHCQ5)
```

Consequently:

```text
A!=0          ==> test only u=-B/A;
A=0, B!=0     ==> reject;
A=0, B=0      ==> retain the at-most-two roots of (IHQ5). (IHCQ6)
```

All candidates must also pass the original linear gate, the monic quadratic,
exact polynomiality, the multiplied Hensel identity, quartic distinct
splitting, and Möbius matching. This theorem does not prove that the
exceptional pair `A=B=0` is empty or that its candidates reject.
