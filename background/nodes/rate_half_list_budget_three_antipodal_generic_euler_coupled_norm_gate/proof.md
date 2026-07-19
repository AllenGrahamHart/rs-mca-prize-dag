# Proof

At every root `alpha` of `V`, the generic norm expansion reduces to

```text
Q_0(alpha)=U(alpha)^4.                                (1)
```

Multiplication over all roots of the monic `V`, with multiplicity, gives

```text
N_Q=N_U^4.                                            (2)
```

The Euler cubic-norm dependency gives

```text
N_TN_U^3=(-d)^v.                                      (3)
```

The quotient pencil has `gcd(U,V)=1`, and `V` shares no factor with `Q_0`:
if both vanished at one point, `(1)` would force `U` to vanish there as well.
The Euler gate also proves `gcd(V,T)=1`. Hence all norms are nonzero.

Equation `(2)` proves the fourth-power condition. Raise `(3)` to the fourth
power and substitute `N_U^12=N_Q^3` from `(2)`:

```text
N_T^4N_Q^3=(-d)^(4v)=d^(4v),
```

which proves `(GNC3)`.

The multiplicative group of a finite field is cyclic. Its fourth-power
subgroup has index `g_4=gcd(4,q-1)` and is the kernel of exponentiation by
`(q-1)/g_4`, proving `(GNC4)`. The exact coupling remains an independent
necessary equality after the character tests. QED.
