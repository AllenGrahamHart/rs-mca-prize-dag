# DLI ell-two weight-five pair ideal-index obstruction

- **status:** PROVED
- **closure:** proof

Let `M` be a power of two, `d=M/2`, and

```text
O_M = Z[X]/(X^d+1) = Z[zeta_M].
```

Fix a legal normalized pair `x=zeta_M^i`, `y=zeta_M^j` in the
pair-quadratic router and put

```text
u=x+y, A=xy, v=-1-u, C=u(v-A).
```

Define `C_m=C^m`, `V_m=v^m`, and the cleared Dickson quantity

```text
E_m = v^m D_m(v,C/v).
```

For powers of two it can be computed without division from

```text
C_1=C, V_1=v, E_1=v^2,
C_(2m)=C_m^2,
V_(2m)=V_m^2,
E_(2m)=E_m^2-2C_m V_m.
```

Set

```text
F=C_M-V_M, G=E_M-2V_M.
```

Let `L_(i,j)` be the `d x 2d` integer matrix whose columns are the
multiplication-by-`F` and multiplication-by-`G` matrices in the power basis
of `O_M`. If it has full rational row rank, let

```text
Delta_M(i,j) = gcd of all d x d minors of L_(i,j)
             = [O_M : F O_M + G O_M].
```

If a characteristic-`q` split row contains a guarded router solution with
this normalized pair, then

```text
q divides Delta_M(i,j).
```

Odd Galois dilation does not change `Delta_M(i,j)`. Consequently, the open
official slot `(ell,w)=(2,5)` has the following exact finite exclusion
certificate: take one legal pair from each odd-dilation orbit at `M=1024`,
compute the corresponding indices, and prove that none has a prime divisor
`q<2^256` with `v_2(q-1)>=41`.

The repository has not completed that certificate. This node proves the
ideal-index reduction, not the emptiness of the official slot.
