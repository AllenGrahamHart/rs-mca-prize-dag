# Proof

The first direction and `(PSF3)` are the residual-evaluation theorem. We
prove the reciprocal assertion.

Project the untwisted curve ideal sequence along `pi_z`:

```text
0 -> O(-rho,-m) -> O -> O_C -> 0.                     (1)
```

Since `rho>1`, direct image and relative cohomology give

```text
0 -> O -> (pi_z)_*O_C
  -> O(-m) tensor H^1(P^1_X,O(-rho)) -> 0.             (2)
```

The extension splits because

```text
Ext^1(O(-m),O)=H^1(O(m))=0,                            (3)
```

and Serre duality identifies

```text
H^1(O(-rho))=H^0(O(rho-2))^*.                          (4)
```

This proves the first equality in `(PSF4)`.

At the parameter fibre `z=S`, the point `P_*` is cut out by `X-x_0` and

```text
Q(S;X)=(X-x_0)C_0(X).                                 (5)
```

The same local elementary-modification calculation used for the other
projection says that the direction in the fibre of `(pi_z)_*O_C` is the
socle class `[C_0]`. This includes ramification: if `X-x_0` has fibre
multiplicity `e`, then `C_0` contains `(X-x_0)^(e-1)` and is a unit times
the local socle generator.

Pair the connecting class of `C_0` with
`p in H^0(P^1_X,O(rho-2))`. The local Grothendieck-residue formula and `(5)`
give

```text
Res_(Q(S;x)=0) C_0(X)p(X)dX/Q(S;X)
 =Res_(X=x_0) p(X)dX/(X-x_0)
 =c p(x_0),       c!=0.                               (6)
```

Hence the negative-block coordinate is `[ev_x0]`, proving the second line
of `(PSF2)`. It is nonzero, so the positive modification raises one
`O(-m)` summand rather than the trivial summand. This gives the second
splitting in `(PSF4)`. Formula `(PSF5)` is evaluation in the monomial basis.
QED.
