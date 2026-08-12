# `A=1` nonreduced collision ordinary-companion norm gate

- **status:** PROVED
- **closure:** every low-degree companion has a bounded global norm quotient
- **consumer:** `rate_half_band_crossing_location`

Retain one ordinary-even factor `Q(t,X)` from shapes B--D of the
factorwise Bezout classification. Put

```text
(m,n)=bideg Q in {(2,3),(4,6)},
Gamma=the 3e off-line supported slopes,
L_0(X)=L_U0(X),       |U_0|=R=3p-2,
N_Q(X)=product_(delta in Gamma)Q(delta,X).         (OCN1)
```

Then every factor in `(OCN1)` is nonzero and

```text
N_Q(X)=L_0(X)^m S_Q(X),
deg S_Q<=3en-Rm=7m/2.                             (OCN2)
```

The quotient is coprime to the complete classified-row locator:

```text
gcd(S_Q,L_0)=1.                                   (OCN3)
```

At the collision heavy row `x_*`, it has a forced divisor of degree `m/2`:

```text
(X-x_*)^(m/2) divides S_Q.                        (OCN4)
```

Consequently there is a polynomial `E_Q` such that

```text
(m,n)=(2,3):
  S_Q=(X-x_*)E_Q,       deg E_Q<=6;

(m,n)=(4,6):
  S_Q=(X-x_*)^2E_Q,     deg E_Q<=12.              (OCN5)
```

For every `x in U_0`, let `A_x(Q)` be the `m` roots of `Q(-,x)` in
`Gamma` and define

```text
D_x(Q)=
 product_(delta in A_x(Q)) partial_XQ(delta,x)
 product_(delta in Gamma\A_x(Q)) Q(delta,x).       (OCN6)
```

Then every displayed factor in `(OCN6)` is nonzero and

```text
S_Q(x)=D_x(Q)/L_0'(x)^m.                          (OCN7)
```

Since `deg S_Q<=14<R`, these values determine the bounded quotient
uniquely by Lagrange interpolation on `U_0`.

## Scope

The theorem does not prove that `E_Q(x_*)` is nonzero, that `E_Q` has a
forbidden root, or that a companion is impossible. It converts each
companion into one degree-six or degree-twelve residual-norm gate that is
nonzero on `U_0`; its value at `x_*` is deliberately left open.
