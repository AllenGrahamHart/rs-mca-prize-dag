# Repeated-BC cell-11 curve projection atlas

- **status:** PROVED
- **field:** `F_2130706433`
- **scope:** the eight guarded cell-11 common rows before outside payment

For every `(epsilon_1,epsilon_2,BC sign)`, the localized common ideal has
dimension one.  Its elimination ideal in `F[b,c]` is principal and is
independent of the epsilon signs.  There are exactly two printed equations,
one for each BC sign.

Writing `x=bc` and `y=b+c`, the BC+ equation is

```text
y^2 (x-1)^2 - 2 x (x+1)^2 = 0.
```

The BC- equation is the degree-eight symmetric polynomial printed in the
geometry certificate.

## Falsifier

A missing sign row, a common dimension other than one, a second elimination
generator, epsilon dependence, or failure of either symmetric identity.
