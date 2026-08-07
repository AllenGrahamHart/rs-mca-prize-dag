# KoalaBear degree-12 R20 K10-zero leading-drop exclusion

- **status:** PROVED
- **field:** `F_p0`, where `p0=2130706433`
- **scope:** the complete named-open `K10=0` complement in all four fixed
  `R20` degree-12 branches

For either representative `F04-R20` or `F06-R20`, write the four q-slice
rows as `A0,B0,A1,B1` in `w`, and write

```text
B0=b2*w^2+b1*w+b0.
```

On `K10=0`, named openness makes `b2=0`. For `P` in `{A1,B1}`, of degree
`d=4`, define the division-free linear-root evaluation

```text
H_P = sum_(i=0)^d P_i*(-b0)^i*b1^(d-i).
```

Let `R12` be the selected degree-12 first-pair resultant factor. In both
representatives, the ideal

```text
(R12,K10,H_A1,H_B1) subset F_p0[x,s,pvar]
```

saturated by `s`, the degree-6 leading factor `L6`, and every transported
named-open factor is the unit ideal. Hence neither representative has a
geometric admissible point on the `K10=0` branch. Complete-system inversion
transports the result to `F05-R20` and `F07-R20`.

## Falsifier

A source point on the printed complete open satisfying `R12=K10=0`, or a
nonunit saturated ideal in either representative.
