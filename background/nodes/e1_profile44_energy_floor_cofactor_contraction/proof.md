# Proof

Let the `64` conjugate squares be `y_u>0`, with mean `20` and average
squared deviation `V`. If `E` is the integer positive-half autocorrelation
energy, then `V=2E`. The parent proves `E>=5`, hence

```text
V>=10.                                                  (1)
```

If `L=sum_d |A_d|`, integrality gives `L<=E`. Fourier expansion therefore
gives the energy-adaptive pointwise cap

```text
y_u<=20+2L<=20+2E=20+V.                                (2)
```

For fixed `V>0`, put

```text
C(V)=V^2/(V/20-log(1+V/20)).                           (3)
```

On `0<x<=20+V`, differentiation at the two endpoints proves

```text
log x <= log 20+(x-20)/20-(x-20)^2/C(V).              (4)
```

The difference in (4) vanishes at `20` and `20+V`; its derivative is

```text
(x-20)(C(V)-40x)/(20xC(V)),
```

so those endpoints and the single interior turning point give the claimed
sign. Averaging (4), using the mean and variance, yields

```text
R=product_u y_u
 <=20^64 exp(-64 V/C(V)).                              (5)
```

The function

```text
V/C(V)=1/20-log(1+V/20)/V
```

is increasing because `log(1+x)/x` is decreasing. By (1),

```text
R<=U:=20^64 exp(-16/5)(3/2)^(32/5).                   (6)
```

Let `P=B_P 2^128` be the lower official prime endpoint. Raising (6) to the
fifth power reduces the threshold comparison to

```text
U^5=20^320 3^32/(2^32 e^16).                          (7)
```

Exact degree-`37` Taylor lower and geometric-tail upper bounds for `e^16`
certify

```text
932364 P < U < 932365 P.                              (8)
```

If `m>=932365`, then an official collision would satisfy
`R=mp>=mP>U`, contradicting (6). This proves (P44-C1). Intersecting the
exact `1133`-value parent list with `m<=932364` gives the `657` values and
valuation counts in the statement. QED.
