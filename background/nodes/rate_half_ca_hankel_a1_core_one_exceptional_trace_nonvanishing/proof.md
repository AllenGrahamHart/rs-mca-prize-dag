# Proof

Assume `D_*=1` and suppose the exceptional trace is zero. The exceptional
allocation theorem proves that every domain trace is active, so `X_0=1`, and
gives the third system in `(ETA4)`. It also proves that the exceptional fiber
`q_0` is squarefree of exact degree `r-1`.

At `gamma_0`, the full supported product `P` vanishes. The second complement
therefore becomes `(ETN3)`. Both sides are nonzero polynomials. Degree
additivity gives

```text
deg_X A_a(gamma_0;X)=D_0-(r-1)=D_0-r+1.              (1)
```

No zero domain trace was cancelled, hence `A_a=A`. The original slope-side
complement theorem gives the exact global degree `deg_X A=D_0-r`.
Specialization cannot increase `X`-degree, contradicting `(1)`. Thus the
exceptional trace is active whenever `D_*=1`. Substitution in `(ETA4)` leaves
exactly the two systems `(ETN6)`. QED.
