# Proof

Fix a source-sign row and target lane on the proved cell-4 four-basis tower.
For `xi=0`, the residual product list is

```text
de, -de, df, sigma_o ef, bf, sigma_c cf.
```

At matching `9=((0,4),(1,2),(3,5))`, put `u=df`. The first two paired cuts
are

```text
P_u(u)=Pair(-de,u),        P_f(f)=Pair(de,bf),
```

and both are quadratic. Since `d=u/f` and `e=de*f/u`, the omitted squared-
sum equation is

```text
J(u,f)=(u^2+de*f^2)^2-s*f^2*u^2=0.                  (1)
```

The division-free degree-eight construction in the matching-4 theorem
applies verbatim after exchanging the signed `DE` inputs to `P_u,P_f`.
Writing `P_u=A*u^2+B*u+C`, its cleared linear remainder numerators `L,N`
give `A*N^2-B*L*N+C*L^2`; pseudo-reduction modulo `P_f`, multiplication by
the `P_f` leading coefficient, and the four-basis tower norm retain every
leading-degree drop.

For each of 16 sign/lane rows, the compiler unions every field root of the
norm numerator, norm denominator, and all inversion-guard numerators and
denominators. It lifts the union through the original quadratic `t`,
quadratic `b`, linear `c`, and compact-kernel equations. At every guarded
source point it solves `P_u=P_f=0`, tests (1), reconstructs `d=u/f` and
`e=de/d`, and checks `Pair(sigma_o*ef,sigma_c*cf)` and the target guards.

The direct ledger has 288 candidate `r` values and 544 guarded source
points. Of 1,472 `(u,f)` rows, 1,280 fail (1); all 192 survivors have a
nonzero final colored-pair cut. There is no boundary, colored solution,
witness, or unresolved branch, proving `xi=0` empty.

Deleting `xi=1` instead preserves the complete residual system and every
guard value-for-value, so the 16 `xi=1` cases transport from `xi=0`. Thus all
32 stated cases are empty. QED.
