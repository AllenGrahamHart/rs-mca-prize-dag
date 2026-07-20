# Budget-three fiber-two c=1 coefficient-resultant elimination

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_fiber_two_cycle_mismatch_trace_resolvent_elimination`

Retain

```text
D_*(Y)=Y^4-e_1Y^3+e_2Y^2-e_3Y+e_4
      =product_(A in Omega)(Y-A),                    (C1R1)
```

the outer invariants `I,J`, and the twelve norms
`N_(A;B,D)` from the dependency. Every root of `D_*` is nonzero.

For indeterminates `A,C), put

```text
S=e_1-A-C,       P=e_4/(AC),
Nhat(A,C)=(AC)^6 N(A;S,P).                           (C1R2)
```

Here `N(A;S,P)` means the printed formula `(MTR6)` with
`B+D=S,BD=P`. The apparent denominator in `(C1R2)` cancels:
`Nhat` is a polynomial of degree at most 18 in each of `A,C`.

Define the divided quartic

```text
H(A,C)=(D_*(C)-D_*(A))/(C-A)
 =C^3+(A-e_1)C^2+(A^2-e_1A+e_2)C
    +A^3-e_1A^2+e_2A-e_3,                            (C1R3)
```

and the coefficient-only scalar

```text
R_1=Res_A(D_*(A), Res_C(H(A,C),Nhat(A,C))).           (C1R4)
```

Then the entire `c=1` completion-root packet passes if and only if

```text
R_1=0.                                               (C1R5)
```

More precisely,

```text
R_1=e_4^36
    product_(A,C in Omega, A!=C) N_(A; Omega\{A,C}). (C1R6)
```

The ordered pair `(A,C)` is exactly the repeated completion square and
unused residual square; its complement is the unordered pair `{B,D}`.
Thus `(C1R4)` neither loses nor adds a candidate.

This replaces root factoring and twelve indexed tests by one constant-degree
iterated resultant in the coefficients of `D_*` and the canonical outer
quartic. It does not prove `R_1` nonzero after the official coefficient
gaps, exclude the `c=1` stratum, or authorize a large computation.

