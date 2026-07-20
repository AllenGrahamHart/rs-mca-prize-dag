# Budget-three fiber-two c=2 gap-only parity counterexample

- **status:** PROVED
- **closure:** proof by explicit counterexample
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_generic_two_window_square_reduction`

The primary and secondary two-window gaps do not force a quartic denominator
to consist of two antipodal pairs without the official torsion and
square-class hypotheses.

Over `F_53`, put `H=8` and

```text
E(z)=1+z+11z^2+34z^3+43z^4,
A(z)=E(z)^(-1/4)=sum_(n>=0) a_n z^n.                 (GPC1)
```

The four-term recurrence gives

```text
a_14=a_15=0,       a_16=2!=0.                       (GPC2)
```

For the two windows

```text
L=sum_(n=0)^7 a_nz^n,       T=sum_(n=0)^7 a_(16+n)z^n,
```

one has

```text
LT/2 = C^2 mod z^8,
C=1+22z+49z^2+3z^3+16z^4.                           (GPC3)
```

Thus the normalized square root has zero coefficients at degrees six and
seven, and in fact also at degree five. Nevertheless `E` is not even and its
four distinct roots

```text
{2,24,46,48}
```

are not closed under negation. Hence this is a split squarefree nonparity
solution of the gap-only system.

It is not an official denominator packet: the root orders are
`52,13,13,52`, rather than divisors of `N=8H-8=56`, and the roots have mixed
quadratic character. Therefore this counterexample does not refute the live
official implication. It proves that any parity-forcing argument must use
the `mu_N` torsion and square-class conditions essentially; the two-window
differential identity alone cannot suffice.
