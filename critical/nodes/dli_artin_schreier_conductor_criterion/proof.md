# proof: dli_artin_schreier_conductor_criterion

Fix a smooth curve component `C` over a field of characteristic `p`, and a
rational function `f in k(C)`. The additive phase used in the DLI Weyl sums is
the trace function of the Artin-Schreier sheaf `L_psi(f)`.

Artin-Schreier sheaves satisfy the standard equivalence

```text
L_psi(f) is geometrically trivial
    iff f = g^p - g + c
```

in the geometric function field, for some `g in kbar(C)` and constant `c`.
Replacing `f` by `f-(g^p-g)` is exactly the Artin-Schreier coboundary
relation; coboundaries give isomorphic additive local systems, and the
constant phase is the trivial geometric local system up to a scalar trace.
Conversely, a geometrically trivial Artin-Schreier torsor represents the zero
class in `kbar(C)/(Frob-1)kbar(C)` modulo constants, hence has this form.

For a nontrivial class, choose an Artin-Schreier-reduced representative,
meaning no pole order is divisible by `p` after subtracting a coboundary
`g^p-g`. The local Swan conductor of `L_psi(f)` at a pole is then the reduced
pole order, and there is no ramification away from the reduced polar divisor
and the bounded singular points of the component. Thus the global conductor is
bounded by a constant depending only on the component bookkeeping plus

```text
sum_{x pole of f_reduced} (1 + ord_x pole(f_reduced)).
```

This proves the criterion used by DLI: to establish nontriviality and
conductor control for an actual phase, it is enough to rule out the
Artin-Schreier form and bound the reduced polar divisor. Those project-specific
tasks are isolated in `dli_odd_phase_reduced_pole_budget`.
