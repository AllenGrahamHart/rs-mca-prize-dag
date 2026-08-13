# `A=1` quadratic nonreduced collision Pade/split-jet dictionary

- **status:** PROVED
- **closure:** exact moment and split-biform formulas for the two collision scalars
- **consumer:** `rate_half_band_crossing_location`

Retain an unshared nonreduced nonzero-jet collision in odd characteristic.
Put `z=t-tau`, `y=X-x_*`, and define the two divided rows

```text
U(t,X)=[Q(t,X)-Q(t,x_*)]/(X-x_*),
W(t,X)=[U(t,X)-U(t,x_*)]/(X-x_*).                 (PSD1)
```

At `tau`, exact root multiplicity two gives

```text
W_tau=Q(tau,X)/(X-x_*)^2,
W_tau(x_*)!=0.                                    (PSD2)
```

Let `q=y^2+c_1y+c_0` be the local quadratic factor and write

```text
P_F=b+ay mod q,
lambda_0=a(0),       lambda_1=[z]a.               (PSD3)
```

For the contracted moment functional `Phi_t`, put

```text
A(t)=Phi_t(W(t,X))=P_(F,X)(t,x_*),
E_i(t)=Phi_t(X^iW(t,X)).                           (PSD4)
```

Then

```text
A=a mod z^3,
lambda_s=[z^s]A       (s=0,1),                    (PSD5)

[z^s]E_i=x_*^i lambda_s       (s=0,1).            (PSD6)
```

If `lambda_0=0`, then `W_tau` lies in the specialized Hankel kernel and
the first derivative moment pairing is

```text
[z] Phi_t(W(t,X)^2)=lambda_1 W_tau(x_*).           (PSD7)
```

The same scalars are exact split-biform jets. Let `L=L_U0` and let
`Lambda` be the three-center parameter locator. Unsharedness implies
`Lambda(tau)L(x_*)!=0`. Then

```text
lambda_0=-Lambda(tau)G_X(tau,x_*)/L(x_*),          (PSD8)

lambda_0=0
 => lambda_1=-Lambda(tau)[z]G_X(t,x_*)/L(x_*).     (PSD9)
```

Consequently the complete local router has the global interpretation

```text
G_X(tau,x_*)!=0:                         [4];
G_X(tau,x_*)=0, [z]G_X(t,x_*)!=0:        [1,3];
G_X(tau,x_*)=[z]G_X(t,x_*)=0:            [2,2].   (PSD10)
```

## Scope

The dictionary does not prove that any line of `(PSD10)` is empty. It
turns the remaining local alternatives into explicit first-order global
split-biform and contracted-source conditions. Shared nonreduced roots and
characteristic two are not covered.
