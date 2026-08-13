# Cycle 197: MCA near-rational line BC-guard rejection (2026-08-12)

The third shared route-comparison probe feeds the deployed `#1160`
near-rational counterexample through the necessary balanced-profile guard of
the cycle-19 candidate `P_BC` certificate contract.  It returns an exact
guard-level rejection.

For each displayed bad slope `gamma_i`, the word `u+gamma_i v` is nonzero
exactly on `E\{e_i}`.  Its support locator and zero numerator therefore give
a received-word lattice vector with

```text
shifted-degree ceiling = |E|-1 = 67471.
```

The candidate BC contract requires minimum shifted degree at least `67472`.
Thus all `67472` displayed bad slopes fail the guard.  This is a one-line
algebraic exclusion once the hostile record is written correctly; no field
enumeration, reduced-basis computation, or Modal run is needed.

The scope is deliberately narrow.  The cycle-19 relation remains a candidate
contract rather than an executable theorem equivalent to the independently
frozen BC owner.  Passing this control does not prove SEM-QBC soundness or
coverage, but it removes its pre-registered deployed-scale leakage falsifier.

With the three shared route-comparison probes now adjudicated, the state is:

```text
reserve repricing:        SURVIVES WITH EXPLICIT 2w PRICE
K-to-k+1 silent transport: REFUTED; original degree guard required
#1160 BC rejection:       PASSES AT NECESSARY-GUARD LEVEL
```

The next useful shared-spine action is no longer another arithmetic probe.
It is to pose the guarded `K` adapter and typed `P_BC` soundness contract so
that actual certificates, rather than schema strings, can be checked.

```text
start:                   80d430a68
result:                  PROVED candidate-BC hostile-control rejection
DAG delta:               +1 PROVED background node, +2 edges
critical status delta:   none
upstream terminal delta: one mandatory SEM-QBC regression discharged
delta-star movement:     none
compute:                 exact symbolic support-locator arithmetic only
next route action:       pose and attack typed P_BC soundness plus the
                         original-degree guarded K adapter
```
