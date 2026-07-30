# Proof

The saturated defect classifier gives four distinct `J_0-J_1` stars in the
two common-`K` quartics transported to `L^c`. There are exactly two such
labels of `K`: in the aligned case they are the two crossing `K` labels; in
the near-aligned case they are `tau(xi)` and the remaining crossing `K`
label not paired with `eta`. Thus `|K_Lc|=2`.

In the source-line branch, `(KBDS-3)` transports each individual component
star over a source point `x` to the reciprocal endpoint star over `s(x)`.
It sends `J_0` to `J_0` and `J_1` to the two crossing labels in `I`, so the
four mixed stars become four `I-J` stars. The universal category census has
exactly four `I-J` stars total. Hence these are all of them.

For each `k in K_Lc`, source-line transport maps both points of the complete
fiber over `k` to both points of the complete fiber over `tau(k)`. Therefore
the colored divisor is the sum of the two complete fibers over
`Omega=tau(K_Lc)`, proving `(KBQ2-1)` as a divisor identity. Since `C_H` is
squarefree, neither complete fiber can be ramified.

If `L=I`, the `L^c` destinations of common-`K` labels are precisely the two
crossing labels `J_1`, so `Omega=J_1`. If `L!=I` and `tau(eta) in K`, the
five common-`K` destinations consist of one internal `K` pair, `xi`, `eta`,
and one further crossing label `ell in J intersect L^c`. Only `xi,ell` lie
in `L^c`, proving the printed near-aligned description.

In source-line coordinates, the complete locators satisfy

```text
D_K=psi^*K_5,       D_R=psi^*R_7.
```

Substitute `(KBQ2-1)` into the universal identities

```text
Res_T(P_J,H) ~ D_K^2 C_H,
C_H Res_T(P_I,H) ~ D_R^2.
```

Both right sides are pullbacks through the surjective quadratic map `psi`,
so the left sides descend to quotient forms. Faithfulness of pullback gives
exactly `(KBQ2-2)`. No invariance of `Omega` under `tau` is used. QED.
