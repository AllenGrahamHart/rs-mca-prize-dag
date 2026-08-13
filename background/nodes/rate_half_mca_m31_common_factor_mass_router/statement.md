# Mersenne common-factor mass router

- **status:** PROVED
- **scope:** Mersenne full-lift support `e=130237`
- **residual:** a low-degree factor with at most 4,049 inside exceptions

Let `P` be a primitive polynomial representative of the full common factor
of the weight-264 interpolation kernel, and let
`d=deg_(Y,Z) P`.  Then `1<=d<=52`.  Every unsafe family forces at least

```text
t_d=7583-(52-d)^2
```

distinct selected polynomial pairs lying on `P`.  In particular `t_d>=4982`.
Their inside common cores force

```text
#{x in E: P(x,r_0(x),r_1(x))=0} >= 126188.
```

Thus at most 4,049 of the 130,237 inside coordinates are exceptional to the
common factor.  This does not classify `P` or prove safety of its concentrated
branch.
