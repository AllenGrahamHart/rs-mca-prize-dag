# proof: dli_circle_log_integral_constant

Use the classical integral

```text
int_0^{pi/2} log(cos u) du = -(pi/2) log 2.
```

By periodicity and symmetry,

```text
int_0^1 log |cos(2 pi x)| dx
  = (1 / 2pi) int_0^{2pi} log |cos u| du
  = (1 / 2pi) * 4 * int_0^{pi/2} log(cos u) du
  = -log 2.
```

Therefore

```text
int_0^1 log |cos(2 pi x)|^2 dx
  = 2 int_0^1 log |cos(2 pi x)| dx
  = -2 log 2.
```
