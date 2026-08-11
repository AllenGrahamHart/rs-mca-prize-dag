# `A=1` Forney numerator absorbs the pole ideal

- **status:** PROVED
- **closure:** fibrewise recurrence-factor ideal membership
- **consumer:** `rate_half_band_crossing_location`

Retain any live half-distance `A=1` profile with fixed core
`s in {0,1,2}`. On the reduced residual curve

```text
C:Qbar=0,       bideg Qbar=(d,e),       d=rho-s,
```

let

```text
H=product_(gamma in Z)L_gamma,
G=product_(x in D\S)(X-x),       J=(H:G) in O_C.       (FPA1)
```

Let `N_F` be the core-stripped Forney numerator from the full recurrence,
representing the nonzero contact section

```text
s_F in H^0(C,O_C(-rho-1,e+1)).                        (FPA2)
```

Then

```text
N_F|_C in J.                                          (FPA3)
```

Equivalently, `N_F G/H` is regular on `C`. In line-bundle form, one contact
copy cancels every finite pole of the residual-domain-locator ratio:

```text
s_F G/H in H^0(C,O_C(N-s-rho-1,e+1-T)).               (FPA4)
```

This is scheme-theoretic ideal membership, including exceptional supported
fibres and nonreduced fibre intersections. It is stronger than the degree
bound `length(O_C/J)<=O`.

## Scope

The theorem does not assert that the contact divisor equals the pole scheme;
it only contains it.
