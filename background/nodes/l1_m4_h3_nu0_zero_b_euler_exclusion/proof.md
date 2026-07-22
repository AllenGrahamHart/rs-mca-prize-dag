# Proof - L1 m=4, h=3, nu=0 zero-b Euler exclusion

The value-coset supplier excludes `p=8191,131071`. Suppose therefore that
`p` is `524287` or `2147483647`; it also supplies `(ZBE1)`. In particular,
`r`, `a`, and `alpha` are nonzero.

With `b=0`, the exact Euler quotient factorization is

```text
D(2aR)XR'=H R(R^2+a)-4alpha R.
```

Cancellation in the polynomial ring proves `(ZBE2)`.

Let `x` be a root of `R`. This is one of the three complete split fibers, so
`x` is a nonzero domain point, `R` is squarefree at `x`, and `D(x)!=0`.
Differentiate

```text
R(R^2+a)D=X^n-alpha,       n=4(p+1).
```

At `x`, characteristic-`p` arithmetic gives

```text
aR'(x)D(x)=4x^(n-1).
```

Since `x^n=alpha`, multiplying by `2x` gives

```text
2aD(x)xR'(x)=8alpha.                                  (1)
```

On the other hand, `(ZBE2)` evaluated at `x` makes the same quantity
`aH(x)-4alpha`. Hence

```text
H(x)=12alpha/a.                                       (2)
```

The degree-`p` locator `R` has `p` distinct roots, whereas `deg H<=3` and
`p>3`. Therefore (2) forces the polynomial identity `(ZBE3)`.

Evaluate `(ZBE2)` at `X=0`. Its left side vanishes, so

```text
(12alpha/a)(r^2+a)=4alpha.
```

Cancellation gives `3r^2+2a=0`, proving `(ZBE4)`. Finally set
`q=a/r^2=-3/2` in `(ZBE1)/r^4`:

```text
q^2+3q+1=9/4-9/2+1=-5/4=0.
```

This would require characteristic five, contrary to both remaining official
rows. The zero-`b` endpoint is empty.
