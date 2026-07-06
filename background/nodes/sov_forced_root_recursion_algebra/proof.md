# proof: sov_forced_root_recursion_algebra

Work over odd characteristic. Let

```text
S(X) = X^h + s_{h-1}X^{h-1} + ... + s_0
```

be a monic degree-`h` polynomial, and let `L(X)` be a monic degree-`2h`
locator. The coefficient of `X^d` in `S^2`, for
`d = 2h-1, 2h-2, ..., h`, has the form

```text
2 s_{d-h} + known higher terms.
```

The only appearances of the still-unknown coefficient `s_{d-h}` are the two
products with the leading coefficient of `S`, namely

```text
X^h * s_{d-h}X^{d-h}
    and
s_{d-h}X^{d-h} * X^h.
```

All other contributions use coefficients already recovered at higher degrees.
Since `2` is invertible, the equation

```text
[X^d] S^2 = [X^d] L
```

solves uniquely for `s_{d-h}`. Descending from `d = 2h-1` to `d = h` recovers
all coefficients of `S`. This is exactly the generalized recursion used in
the SOV helper.

After `S` is fixed, the obstruction coordinates are definitions:

```text
O_i = [X^i](S^2 - L),     1 <= i <= h-1.
```

Thus the recursion produces the unique forced root and the printed
obstruction vector.

For the X79 shifted-constant trade model, take monic degree-`h` polynomials
`A` and `B` with `B - A = delta` constant, and set

```text
L = A B,          S = (A+B)/2.
```

Then

```text
S^2 - L = ((A+B)^2 - 4AB)/4 = (A-B)^2/4 = delta^2/4,
```

which is constant. Hence every coefficient in degrees `1, ..., h-1`
vanishes. Since `S^2` and `L` have the same top coefficients, the recursion
recovers this midpoint `S`, and all obstruction coordinates are zero.
