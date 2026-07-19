# Budget-three antipodal generic deleted-pair remainder-square router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_constant_ode`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_mobius_ratio_router`

Retain the remaining split-quadratic deleted-pair data with

```text
N=8M,       D_0 monic of degree 2,
U_0 monic of degree 2M-1,       q in mu_N\{1}.        (RSR1)
```

Here `U_0` is the unique possible constant-ODE direction and `q` lies on one
of the three Möbius-ratio branches. Define

```text
Q=(x^N-1)/D_0,       A=xU_0^2,       R=Q-A^2.         (RSR2)
```

Then the complete half-degree square-pencil factorization exists if and only
if one of the following deterministic tests passes.

If `q!=-1`, perform the unique Euclidean division

```text
R=A S+T,       deg T<deg A.                            (RSR3)
```

The exact acceptance conditions are

```text
deg S=2M-2,
T=q S^2/(1+q)^2,
Z:=S/(1+q) is a nonzero square in F_p[x].              (RSR4)
```

If `q=-1`, the exact acceptance condition is

```text
-R=W^4 for a polynomial W of degree M-1.              (RSR5)
```

On a nonharmonic survivor, `Z=W^2` reconstructs the missing direction and

```text
Q=(A+Z)(A+qZ).                                        (RSR6)
```

Moreover the Euclidean remainder `T` in `(RSR4)` is itself an exact fourth
power in `F_p[x]`. On a harmonic survivor, `(RSR5)` gives

```text
Q=(A+W^2)(A-W^2).                                     (RSR7)
```

Thus after `D_0`, the torsion lift ratio, and one of the three torsion outer
ratios are selected, no coefficient of `V_0` and no common outer scale remains
free. This theorem does not prove that the tests `(RSR4)--(RSR5)` always
reject on the official torsion family.
