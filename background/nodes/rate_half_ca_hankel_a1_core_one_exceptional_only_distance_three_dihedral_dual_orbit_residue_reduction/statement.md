# `A=1` distance-three dihedral dual orbit-residue reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dihedral_boundary_order_router`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_dual_row_product_power_router`

Retain either rank-two dihedral matching. Let `C(X)` be the monic active
outside-row locator, put

```text
P_T=product_(t in T) C(t),       r=2e+1,
```

and let `R_i` be the dual residue attached to the `i`th exceptional pair.

## Antipodal branch

Write

```text
A(X)=E(X^2),       u_i=a_i^2,
kappa_-=4 P_T/N^2,
W_-(U)=U^2(U-s^2)(U-x_0^2) product_(t in T)(U-t^2). (DOR1)
```

Then `E(U)=product_i(U-u_i)` and

```text
R_i=kappa_- W_-(u_i) E'(u_i)^2.                    (DOR2)
```

## Constant-product branch

If every pair is `{a_i,c/a_i}`, put

```text
u_i=a_i+c/a_i,       A(X)=X^e E(X+c/X),
kappa_c=c^e P_T/N^2,
W_c(U)=(U^2-4c)(c+s^2-sU)(c+x_0^2-x_0U)
       *product_(t in T)(c+t^2-tU).                 (DOR3)
```

Then `(DOR2)` holds with `kappa_c,W_c` in place of
`kappa_-,W_-`.

In either branch write `kappa,W` for the corresponding data. All displayed
factors at the roots of `E` are nonzero, and the `e` dual gates are
equivalent to the single split-algebra condition

```text
there is Y in F_p[U], deg Y<e, such that
Y(U)^r = kappa W(U)E'(U)^2 mod E(U).                (DOR4)
```

Their product also gives the necessary global gate

```text
kappa^e Res(E,W) Disc(E)^2 in (F_p^*)^r.            (DOR5)
```

Here the square removes the harmless sign convention in `Disc(E)`. The
reduction does not prove that `(DOR4)` is impossible in either retained
high-order field stratum.
