## MCA O0b `FFF` q5 coefficient bank (2026-08-17)

### Exact result

The compressed finite-pair equation is now retained canonically as

```text
q5(s) = C0 + C1*s + C2*s^2
C0: degree 44, 761 terms
C1: degree 44, 782 terms
C2: degree 44, 799 terms
```

Each coefficient is a reduced representative modulo the 48-element
admissible base-graph basis and has an independently checked hash in compute
request 77. The extraction completed in Modal app
`ap-1GgCht615t6eZJCKSKStPA`.

### Consequence

The previous 3,126-term whole normal form no longer needs to be regenerated
or adjoined. The remaining problem is a low-degree common-root calculation:
`q5` is quadratic in `s`; both compressed `q7` and `q6` are
quadratic in `E`.

### Next decision gate

1. Decompose `q6(E,s)` by powers of `E` and form the exact quadratic
   resultant `R76(s)=Res_E(q7,q6)`.
2. Reduce the coefficients of `R76(s)` separately modulo the admissible
   base graph.
3. Eliminate `s` against the banked quadratic `q5(s)`, with explicit
   leading-coefficient strata so degree drops cannot be lost.
4. A unit admissible base ideal closes the necessary `q5,q7,q6`
   subsystem and hence `FFF`; surviving finite strata become the exact
   input for the omitted `q4` equation.
