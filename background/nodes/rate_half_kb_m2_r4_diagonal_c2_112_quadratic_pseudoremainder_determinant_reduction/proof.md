# Proof

The pseudo-division loop maintains (QPR-1) exactly. At a zero of `D`, it
gives `a^3 P=H`. The reconstruction relation gives

```text
V H = V(r1 w+r0) = V r0-U r1 = Delta_D(P).
```

If `a` and `V` are units, these two identities prove both directions of
(QPR-3). No radical or sampled-point inference is involved.

The parent quadratic-reconstruction node proves that, on `R=0,V!=0`, the
first two q-slice rows vanish at `w=-U/V`. The exact Sage replay then applies
(QPR-1) separately to the two quartic rows and verifies every polynomial
identity before factorization.

For `B0`, its leading coefficient is a named linear unit times `K8`. The
two determinants factor as named units times `K8` times the displayed
degree-34 irreducible cores. Cancelling only factors explicitly inverted on
the chart proves the replacement. The recorded finite-field Groebner basis
establishes the final dimension and basis census. QED.
