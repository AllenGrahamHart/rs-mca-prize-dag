# Proof

For every classified row `x in U_0`, the split-row theorem gives

```text
Z(G(-,x))={off-line supported slopes containing x}. (1)
```

No assigned center is in this root set. Hence

```text
G(gamma,x)!=0       (gamma in {alpha,beta,theta}, x in U_0). (2)
```

At a small center, all roots of `Qbar(gamma,X)` are the points of
`U_0\M_gamma`. Equation `(2)` proves coprimality there.

At the large center, the locator roots are the points of
`U_0\M_(gamma_0)` together with `x_*`. Equation `(2)` handles the first
set. If `G(gamma_0,x_*)` were zero, `(gamma_0,x_*)` would be a common
point of the coprime curves `Qbar=0` and `G=0`. It is not among the
mandatory intersections over off-line supported slopes, so it would
survive in the effective residual cycle `Z_4`. But

```text
pi_*Z_4=2div(S_B)                                 (3)
```

is supported only at the collision parameter `tau`, and `tau` is not an
assigned center. This contradiction proves

```text
G(gamma_0,x_*)!=0.                               (4)
```

Equations `(2),(4)` prove `(CCP3)`. In `(CCP5)`, both `g_off` and `S_B`
are nonzero at `gamma_0`: the unique center factor was removed from
`g_off`, and the collision is off the center line. Equation `(4)` then
gives `T_3(gamma_0)!=0`, proving `(CCP4)`.

It remains to specialize the Pade identity. At a center, `Lambda=0`, so
`(CCP1)--(CCP2),(CCP6)` give

```text
chi_gamma R_gamma L_rest,gamma B_src(gamma,X)
 =L_Mgamma L_rest,gamma P_F(gamma,X).             (5)
```

Cancel the nonzero polynomial `L_rest,gamma`. The factor `R_gamma` is
coprime to `L_Mgamma`: this is automatic in a small class, and in the
large class it uses `x_* notin U_0`. Therefore `(5)` forces

```text
L_Mgamma divides B_src(gamma,X).                 (6)
```

Define `C_gamma=B_src(gamma,X)/L_Mgamma`. Equation `(5)` becomes exactly
`(CCP7)`. The quotient is nonzero: at any root `x` of
`L_rest,gamma`, the source definition gives

```text
B_src(gamma,x)=omega_x(gamma)L_U0'(x)!=0.         (7)
```

Finally `deg_X B_src<=|U_0|-1`. Subtracting the class sizes gives

```text
|U_0|-1-(n+2)=3e-3=d-1,
|U_0|-1-(n+3)=3e-4=d-2.                          (8)
```

This proves `(CCP8)` and completes the proof. QED.
