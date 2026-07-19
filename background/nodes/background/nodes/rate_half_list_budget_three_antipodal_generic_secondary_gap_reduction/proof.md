# Proof

Divide `(SGR1)` by the unit `E` and subtract `B^4`. This gives

```text
R=e_2z^(2h)B^2C^2+e_3z^(3h)BC^3+e_4z^(4h)C^4.        (1)
```

Because `e_2`, `B(0)`, and `C(0)` are nonzero, `(1)` has exact order `2h`.
The divisions in `(SGR3)` are therefore valid in the formal power-series
ring, and

```text
J=e_2C^2+e_3z^h C^3/B+e_4z^(2h)C^4/B^2.              (2)
```

Evaluation at zero proves `j_0=e_2C(0)^2!=0`. Reducing `(2)` modulo `z^h`
and dividing by `j_0` yields

```text
J/j_0=(C/C(0))^2 mod z^h.                              (3)
```

The characteristic exceeds `d`, so two is invertible. A unit series with
constant term one has a unique square root with constant term one. Both `P`
and `C/C(0)` have that normalization, so `(3)` proves `(SGR4)`.

On the official generic boundary, direct substitution gives

```text
h=r-v=s/2+1,       deg C=v=h-3.                        (4)
```

The coefficients of `C/C(0)` in degrees `h-2` and `h-1` vanish. Congruence
`(SGR4)` transfers those two vanishings to `P`, proving `(SGR5)`. All inputs
to `J` are determined by `E` because the dependency uniquely determines `B`.
Thus `C`, and hence `V`, is determined up to its nonzero leading scalar by
the truncation of `P` through degree `h-1`. QED.
