# Budget-three antipodal generic deleted-pair nonharmonic scalar router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_mobius_ratio_router`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_remainder_square_router`,
  `rate_half_list_budget_three_antipodal_generic_deleted_pair_harmonic_exclusion`

Retain the official maximal-row split-quadratic deleted-pair branch. Thus

```text
N=8M=2^38,       p=1 mod 4N,
r^(4N)=1,       r^4!=1,       q_out in mu_N\{1,-1}.  (NSR1)
```

After the constant ODE has produced `D_0,U_0`, put

```text
Q=(x^N-1)/D_0,       A=xU_0^2,       R=Q-A^2,
R=AS+T,       deg T<deg A.                            (NSR2)
```

For the three source pairings define

```text
a_0=r^2,             b_0=(r^2-r+1)^2,
a_1=(r-1)^4,         b_1=(r+1)^4,
a_2=(r^2+1)^2,       b_2=(r^2-4r+1)^2.               (NSR3)
```

The deleted-pair square pencil exists if and only if, for at least one
`j in {0,1,2}`, all of the following tests pass:

```text
deg S=2M-2,       4b_j T=a_j S^2,                    (NSR4)
y_0=4b_j/a_j-2,       y_(m+1)=y_m^2-2,
y_0 notin {2,-2},       y_38=2,                       (NSR5)
Z=S/(1+q_out) is a nonzero square in F_p[x],          (NSR6)
```

where `q_out` is either root of

```text
X^2-y_0X+1=0.                                         (NSR7)
```

The trace gate `(NSR5)` forces both roots of `(NSR7)` to lie in `mu_N`.
They are `q_out` and `q_out^(-1)`, and the square test `(NSR6)` has the same
truth value for either root. Thus `q_out` is no longer a search variable:
the complete nonharmonic deleted-pair classifier consists of three exact
one-variable identities in the lift ratio `r`, one length-38 scalar trace,
and one root-independent polynomial-square test.

This theorem does not prove that the three tests reject uniformly on the
official torsion family, and it does not eliminate the lift ratio `r` or
materialize the official-degree polynomials.
