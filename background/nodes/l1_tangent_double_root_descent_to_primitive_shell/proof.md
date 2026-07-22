# Proof - L1 tangent double-root descent

## 1. Affine tangent fiber

For a member of the exact-`D` stratum, the Hasse root-pinning theorem gives
`D^2|U-P`.  The monic remainder `P_D=U mod D^2` therefore satisfies

```text
P=P_D mod D^2.                                        (1)
```

If `2r<=k`, then `deg P_D<2r<=k`, and division by `D^2` gives a unique
polynomial `R` with

```text
P=P_D+D^2R,       deg R<k-2r.
```

Conversely every such `R` gives a degree-below-`k` solution of `(1)`.  This
proves `(TD3)`, including the singleton convention when `k=2r`.

If `2r>k`, two solutions of `(1)` would differ by a nonzero multiple of
`D^2` of degree below `k<2r`, which is impossible.  This proves the rigid
claim.

## 2. Agreement-set transport

The definition of `P_D` makes `W_D` in `(TD2)` a polynomial.  From `(TD3)`,

```text
U-P=D^2(W_D-R).                                       (2)
```

Every root of `D` is an agreement root.  At any `x in H'`, `D(x)` is
nonzero, so `(2)` gives

```text
U(x)=P(x)  <->  W_D(x)=R(x).                          (3)
```

Consequently the original complete agreement set has size `a` exactly when
the reduced complete agreement set has size `a-r`.  If `L_0` is its reduced
locator, then `L=DL_0`.

## 3. Exact owner equals reduced primitivity

Write `W_D-R=L_0Q_0`.  Equation `(2)` and `L=DL_0` give

```text
Q=DQ_0.                                               (4)
```

The factors `D`, `L_0`, and `Omega' / L_0` have disjoint domain roots.
Therefore

```text
gcd(L,Q)=D             <-> gcd(L_0,Q_0)=1,
gcd(Q,Omega/L)=1       <-> gcd(Q_0,Omega'/L_0)=1.
```

The conjunction of the two reduced gcd conditions is precisely
`gcd(Q_0,Omega')=1`.  Thus exact tangent ownership by `D`, including the
original complement guard, is equivalent to primitivity of the reduced
exact shell.  The constructions `P -> R` and `R -> P_D+D^2R` are inverse,
which proves the bijection.

## 4. Parameter ledger

Deleting the `r` roots of `D` gives `n'=n-r`; `(TD3)` gives `k'=k-2r`; and
agreement transport gives `a'=a-r`.  From `(4)`, `e'=e-r`.  Finally

```text
w'=a'-k'=(a-r)-(k-2r)=w+r.
```

This proves `(TD4)`.
