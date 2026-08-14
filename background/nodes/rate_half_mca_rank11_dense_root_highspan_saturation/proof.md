# Proof

Subtract the descended dense pair line from the fixed core interpolant:

```text
D_H(X,Z)=H(X,Z)-a_0'(X)-Zb_0'(X).
```

The fixed anchor deck contains eighteen actual records owned by that pair.
At their distinct slopes `gamma_1,...,gamma_18`, their deviations vanish,
so

```text
D_H(X,gamma_i)=0.                                    (1)
```

It also contains ten actual records whose deviations form a basis of `V'`.
Those ten vectors are values of `D_H`. Therefore the span of all values of
`D_H` contains `V'`. Every coefficient of `D_H` already lies in `V'` by
the ten-flat containment theorem, so

```text
span{coefficients of D_H}=V'.                        (2)
```

Let

```text
q(Z)=product_(i=1)^18 (Z-gamma_i).
```

Equation (1), applied coefficientwise in the codeword variable, gives

```text
D_H(X,Z)=q(Z)G(X,Z),       deg_Z G<=13.              (3)
```

Write `q(Z)=Z^18+q_17 Z^17+...+q_0` and
`G=sum_(j=0)^13 G_j Z^j`. Since `q` is monic,

```text
(D_H)_31=G_13,
(D_H)_30=G_12+q_17 G_13,
...
(D_H)_18=G_0+q_17G_1+...+q_5G_13.
```

Descending triangular elimination shows

```text
span{(D_H)_18,...,(D_H)_31}=span{G_0,...,G_13}.      (4)
```

All coefficients of `D_H=qG` lie in the right-hand span. Combining (2)
and (4) yields

```text
span{(D_H)_18,...,(D_H)_31}=V'.                     (5)
```

The subtracted pair line has slope degree one. Hence `(D_H)_j=H_j` for
every `j>=2`, and (5) proves that the high coefficients span `V'`.

Now let `W` be an over-budget absorbing correction space. The ten-flat
collapse gives `W<=V'`, while absorption gives `H_j in W` for every
`j>=2`. Equation (5) therefore gives `V'<=W`. Thus `W=V'` and
`dim W=10`.

This equality identifies one common correction space for every surviving
component. It supplies no bound on the number or aggregate mass of those
components.
