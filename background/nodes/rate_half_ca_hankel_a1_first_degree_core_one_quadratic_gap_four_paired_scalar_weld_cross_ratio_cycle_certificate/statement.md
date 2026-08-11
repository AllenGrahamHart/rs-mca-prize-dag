# `A=1` quadratic paired scalar-weld cross-ratio cycle certificate

- **status:** PROVED
- **closure:** local multiplicative certificate for the unique weld survivor
- **consumer:** `rate_half_band_crossing_location`

Retain the complement incidence graph `H`, row polynomials `P_x), fiber
polynomials `F_delta), and weld matrix `W). On every edge put

```text
c_(delta,x)=P_x(delta)/F_delta(x).                  (CRC1)
```

All these scalars are nonzero. The weld has a nonzero kernel if and only if
its edge labels are a multiplicative coboundary:

```text
c_(delta,x)=zeta_delta/lambda_x.                   (CRC2)
```

Equivalently, for every even cycle

```text
x_1-delta_1-x_2-delta_2-...-x_s-delta_s-x_1
```

in `H),

```text
product_(i=1)^s
 c_(delta_i,x_i)/c_(delta_i,x_(i+1))=1,
x_(s+1)=x_1.                                       (CRC3)
```

For two fibers and two common nonincident rows, the length-four condition is
the explicit cross-ratio identity

```text
P_x(delta)P_y(epsilon)F_delta(y)F_epsilon(x)
 =P_y(delta)P_x(epsilon)F_delta(x)F_epsilon(y).    (CRC4)
```

## Extremal profile

Any three selected fibers have at least

```text
R-3n=6+d_A                                         (CRC5)
```

common row neighbors. Consequently `(CRC4)` for every nonincidence
rectangle is a complete certificate: it implies every cycle identity
`(CRC3)`, hence

```text
rank W=R-1.                                        (CRC6)
```

A single failed cross-ratio instead gives `rank W=R` and excludes the
boundary.

## First strict profile

Every two fibers have at least `4+r_A` common row neighbors. For a pair
`delta,epsilon`, the cross-ratios make

```text
q_(delta,epsilon)
 =c_(delta,x)/c_(epsilon,x)                        (CRC7)
```

independent of the common neighbor `x). The length-four identities,
together with the transition-triangle identities

```text
q_(delta,epsilon)q_(epsilon,theta)q_(theta,delta)=1
                                                        (CRC8)
```

for every fiber triple, are a complete certificate for `rank W=R-1).
Failure of either a rectangle or a transition triangle gives `rank W=R`.

When the certificate passes in either profile, choose one base fiber,
recover all `zeta_delta` from the `q)'s, and then recover

```text
lambda_x=zeta_delta/c_(delta,x)                    (CRC9)
```

from any fiber adjacent to `x). The result is independent of the choice
and is the unique projective weld vector. The next test is exactly
`Krow lambda=0), followed by the retained source/Hankel constraints.

## Scope

The theorem supplies local exclusion witnesses and a reconstruction
algorithm. It does not prove that a cross-ratio or transition triangle fails
for every allowed profile.
