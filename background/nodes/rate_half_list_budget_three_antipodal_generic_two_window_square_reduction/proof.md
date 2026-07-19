# Proof

The primary gap and `r=2h-3` give a unique formal tail

```text
A-B=z^(2h)T_hat,       T_hat(0)=c.                     (1)
```

Let `Q=(1-z^d)/E`. Since `EA^4=1`,

```text
Q=A^4-z^dA^4.                                         (2)
```

We need coefficients only through degree `3h-1`. For `h>=2`, this is below
`d=8h-8`, so `(2)` gives `Q=A^4 mod z^(3h)`. Therefore

```text
z^(-2h)(Q-B^4)
 =T_hat(A^3+A^2B+AB^2+B^3) mod z^h.                  (3)
```

Equation `(1)` implies `A=B mod z^(2h)`, hence the parenthesis in `(3)` is
`4B^3 mod z^h`. If `Rbar=z^(-2h)(Q-B^4)`, then

```text
Rbar=4B^3T_hat mod z^h,       Rbar(0)=4c.             (4)
```

The dependency defines

```text
P^2=Rbar/(Rbar(0)B^2) mod z^h,       P(0)=1.
```

Substitution of `(4)` gives `P^2=B T_hat/c mod z^h`.
Reducing `B` and `T_hat` modulo `z^h` produces exactly `L` and `T`, proving
`(TWS4)`.

The characteristic is greater than `d`, so two is invertible. A unit series
with constant term one has a unique normalized square root modulo `z^h`.
The final two coefficients of `P` vanish exactly when that root has degree at
most `h-3`. This is equivalent to `(TWS5)`, including uniqueness of `C`.

Finally differentiate `EA^4=1` to obtain

```text
E'A+4EA'=0.                                            (5)
```

Insert `(1)` into `(5)` and isolate the terms containing `B`. Direct
differentiation gives `(TWS6)`. The left side is a polynomial of degree at
most

```text
max(3+r,4+r-1)=2h.
```

The right side is divisible by `z^(2h-1)`, so its remaining factor is a
polynomial of degree at most one. QED.
