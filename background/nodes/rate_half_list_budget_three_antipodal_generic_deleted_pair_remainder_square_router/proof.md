# Proof

The constant-ODE dependency writes every complete half-degree factorization
as

```text
Q=(xU_0^2+lambda V_0^2)(xU_0^2+mu V_0^2).            (1)
```

Put `A=xU_0^2`, `q=mu/lambda`, and `Z=lambda V_0^2`. Then `(1)` is

```text
Q=(A+Z)(A+qZ)
 =A^2+(1+q)AZ+qZ^2.                                  (2)
```

The degrees are

```text
deg A=4M-1,       deg Z=2M-2,       deg Z^2=4M-4.     (3)
```

Suppose first that `q!=-1`. Subtract `A^2` in `(2)`. Since `deg Z^2<deg A`,
the uniqueness of Euclidean division by the monic polynomial `A` gives

```text
S=(1+q)Z,       T=qZ^2.                               (4)
```

The branch-collapse input carried by the ratio-router dependency proves that
`-lambda` is a square. Since `p=1 mod 4N`, `-1` is a square as well, so
`lambda` is a square. Hence `Z=lambda V_0^2` is a polynomial square. This
proves every condition in `(RSR4)` and gives `(RSR6)`.

Conversely, suppose `(RSR4)` holds and write `Z=W^2`, with `deg W=M-1`.
Equations `(RSR3)--(RSR4)` reverse to

```text
Q=A^2+(1+q)AZ+qZ^2=(A+Z)(A+qZ).                      (5)
```

Set `V_0=W`, `lambda=1`, and `mu=q`. These parameters are distinct and
nonzero. The ratio-router dependency supplies the Möbius matching for the
selected branch. Its field descent also has `p=1 mod 4N`; hence `-1` and
`-q` are squares in `F_p`, so both outer pairs split. Multiplying `(5)` by
`D_0` reconstructs the full identity with `x^N-1`.

The same congruence shows that every `q in mu_N` is a fourth power in `F_p`.
Write `q=eta^4`. Then `(4)` and `Z=W^2` give

```text
T=qZ^2=(eta W)^4,                                     (6)
```

proving the fourth-power assertion.

If `q=-1`, equation `(2)` instead gives

```text
R=-Z^2=-lambda^2V_0^4.                                (7)
```

As above, `lambda` is a square. Write `lambda=s^2`. Equation `(7)` is exactly
`(RSR5)` with `W=sV_0`.

Conversely, `(RSR5)` gives

```text
Q=A^2-W^4=(A+W^2)(A-W^2).                            (8)
```

Taking `V_0=W`, `lambda=1`, and `mu=-1` reconstructs `(1)`. The harmonic
equation in the ratio-router dependency is precisely the remaining Möbius
condition. This proves both directions and `(RSR7)`. QED.
