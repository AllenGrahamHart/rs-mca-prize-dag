## MCA O0b `FFF` generic `q5` route cut (2026-08-17)

### Exact result

Normal-form reduction of the raw `q5` resultant against the 10-polynomial
generic basis exceeded 300 seconds before producing a representative. Modal
app `ap-G2DYAjHI53OT1Ui7998KuR` retained only the exact input transcript;
result SHA-256
`5565e674db92a598d78f9bafcfdf7f2ffab04536ff8e99a223b2e0d9521fe46f`.
No status changes.

### Selected coefficient route

The polynomial-graph computation has already certified

```text
q5 = C0 + C1*s + C2*s^2
```

with each `Ci` reduced modulo the 48-element admissible graph basis and
retained by hash. Reduce those three coefficients independently modulo the
10-element generic basis. This avoids asking the rational-function engine to
expand and reduce the resultant. Once the three small representatives are
banked, adjoin their quadratic combination in `s`.

### Proof boundary

Coefficient-wise reduction is exact because normal form is linear over
`GF(p)(t)` and `s` is free over the base algebra. Denominator and
specialization obligations remain unchanged.
