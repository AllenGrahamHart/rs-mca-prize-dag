# frontier: dli_dirichlet_log_integral

DLI is not a compute-cleanup node. It is the remaining analytic
equidistribution estimate behind the primitive-core Fourier moment.

## Proved reductions

- `pcf_evaluation_flatness/conditional.md` records the D3 reduction:
  `EJM_{2m}` implies PCF/evaluation flatness by character orthogonality and
  Holder. The algebra has a toy verifier.
- `ejm_joint_moment/conditional.md` records the D4 reduction:
  DLI implies `EJM_2` with `eta_j <= eps_j + O(1)`.
- The seen-coordinate lever is proved: every nonzero frequency is seen by at
  least `255 L_j + 1` coordinates, but this is insufficient because Dirichlet
  peaks survive arithmetic averaging.

## Open estimate

For every central profile and every nonzero frequency, prove geometric-mean
decay of the Dirichlet-kernel factors along the square-root/odd-evaluation
section:

```text
-sum_y log |mu_hat_y(P_lambda(sigma(y)))|^2
    >= 2(L_j - eps_j) log q - O(1)
```

with `sum eps_j = o(t)`.

## Routes

- `dli_log_integral_equidistribution`: log-integral equidistribution. Show the low-degree odd evaluation
  sequence samples the circle well enough that the geometric mean approaches
  the exact constant `int log |cos(2*pi*x)|^2 dx = -2 log 2`.
- `dli_odd_evaluation_discrepancy`: prove a Weil/exponential-sum discrepancy bound for the
  odd-polynomial evaluation sequence on the square-root section.
- `DLI-DWE`: use the equivalent collision form: signed `2m`-fold additive
  energy of the odd-evaluation map is at the uniform level.

The exact circle constant is now proved as `dli_circle_log_integral_constant`.

## Evidence

The statement records three calibrated rows with no falsifier; the ternary
mu_32 stress case is essentially flat and the signed midpoint stress decreases
with `N`. This is evidence only.

## Falsifier

A central profile and nonzero frequency whose Dirichlet factors stay near
peaks on enough coordinates to make `sum eps_j` linear in `t`, or an equivalent
collision-energy excess in DWE form.
