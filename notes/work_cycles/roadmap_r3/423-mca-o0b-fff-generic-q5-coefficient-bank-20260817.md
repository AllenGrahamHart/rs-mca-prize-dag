## MCA O0b `FFF` generic `q5` coefficient bank (2026-08-17)

### Exact result

All three coefficients in the generic quadratic

```text
q5 = C0 + C1*s + C2*s^2
```

now have exact eight-term representatives in the dimension-eight base
algebra:

```text
coefficient  fiber degree  quotient terms  normal-form SHA-256
C0           2             8               e008780fd3d46e30c2471900384068de9b384cf3f3a99fbb038d00364b3428c3
C1           2             8               76be8227ceaae91dd6e96df64fbc80ee40f058fb9bb94bebaf7f69df66ee702d
C2           2             8               e890823e9f38e2919f38a73bcd0b7d20c52882e5ea069a05abfa147f637f8ce8
```

`C0,C2` come from Modal app `ap-fjg7OlClGiYgb3VTpj1ygf`; the bounded `C1`
resume is app `ap-cAjaWfMQ5IXbHuWAoxPmXR` with result SHA-256
`899f7706130a8ef3d6556ecc14aeda397868dcd8261db5f6df96c85519d3fc1c`.

### Next decision gate

Embed the three retained representatives in
`GF(p)(t)[s,x,r,c,b]`, form their 24-term quadratic, and compute the
certified `q5` extension of the ten-element base basis. Retain the resulting
quotient dimension and all input/output denominators before moving to `q7`.

### Proof boundary

This closes coefficient reduction only. It does not assert that the `q5`
extension is empty or handle any exceptional specialization.
