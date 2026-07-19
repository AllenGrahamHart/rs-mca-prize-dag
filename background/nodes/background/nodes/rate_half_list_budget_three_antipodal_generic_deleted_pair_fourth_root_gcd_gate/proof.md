# Proof

Differentiate `D_0Q=x^N-1` to obtain

```text
D_0Q'=Nx^(N-1)-D_0'Q.                                (1)
```

Since `A=xU_0^2`,

```text
A'=U_0^2+2xU_0U_0'.                                  (2)
```

The constant ODE `(COD3)`, with `N=8M`, is

```text
(2N-4)D_0U_0-2xD_0'U_0-8xD_0U_0'=kappa.             (3)
```

Dividing `(3)` by two and rearranging gives

```text
xD_0'U_0+2D_0U_0+4xD_0U_0'=ND_0U_0-kappa/2.         (4)
```

Use `Q=A^2+R` in `(1)`, subtract `2D_0AA'`, and apply `(2)--(4)`. This gives

```text
D_0R'=Nx^(N-1)-ND_0xU_0^4+(kappa/2)xU_0^3-D_0'R.    (5)
```

On the other hand,

```text
x^N=1+D_0Q=1+D_0x^2U_0^4+D_0R.                      (6)
```

Multiplying `(5)` by `2x` and substituting `(6)` cancels the two
`D_0x^2U_0^4` terms and yields `(FGG3)`.

Now suppose a branch passes. The fourth-power router proves both

```text
T=W^4,       T=h_j^2S^2.                              (7)
```

As in its proof, `(7)` gives `W^2=+/-h_jS`; hence `S` is a nonzero scalar
multiple of `W^2`. The scalar identity also writes

```text
R=AS+T=S(A+h_j^2S).                                  (8)
```

Therefore `W^2` divides `R`, and differentiation of `(8)` shows that `W`
divides `R'`. Both terms on the right after solving `(FGG3)` for `P` are
then divisible by `W`, so `W|P`.

Since `S` is a scalar multiple of `W^2`, the divisibility `W|P` gives
`S|P^2`. It also places `W` inside `gcd(S,P)`, proving

```text
deg gcd(S,P)>=deg W=M-1.
```

No coprimality with `xD_0` is needed: multiplication by those factors in
`(FGG3)` can only increase divisibility. QED.
