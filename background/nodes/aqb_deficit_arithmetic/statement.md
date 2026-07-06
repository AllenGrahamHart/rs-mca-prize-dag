# aqb_deficit_arithmetic

- **status:** PROVED
- **closure:** proof

## Statement

For the AQB-I constants

```text
N = 2^40,
d = 4,296,456,369,
m = 2^39 + d,
Q <= 256,
```

the finite deficit

```text
B_I = d Q - 40 - log2 C(N, m)
```

is maximized at `Q = 256` and satisfies

```text
B_I < 429,645,547.
```

Equivalently, a certified averaged gain of `429,645,547` bits clears the
finite arithmetic deficit, with equality threshold
`Qcrit = 255.900000020976...`.
